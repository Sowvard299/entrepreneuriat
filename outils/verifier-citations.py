#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controle mecanique des citations d'un fichier de preuves (format de chercheur.md).

PROTOTYPE issu de l'audit W1 (2026-11-03). Non branche sur les agents.

Usage : python -I verifier-citations.py <fichier.md> [dossier_cache]

Pour chaque bloc "### ID" qui a une ligne "- Source : ... URL ..." et des lignes
"- Citation : << ... >>" (guillemets francais), le script :
  1. telecharge chaque URL de la ligne Source avec curl (en-tete curl par defaut :
     aucune imitation de navigateur, un 403 reste un 403) et garde la page en cache ;
  2. convertit la page en texte (HTML : balises, scripts et styles retires ; PDF :
     pdftotext si disponible) ;
  3. cherche chaque citation mot pour mot, sans tenir compte de la casse, des espaces,
     des apostrophes et guillemets typographiques, des cesures de PDF.

Statuts par citation : OK | ABSENT | BLOQUE (HTTP >= 400 ou page vide)
                       | EXTRAIT (la ligne Source dit "extrait de recherche")
Code de sortie : 2 s'il y a au moins un ABSENT ou un BLOQUE, sinon 0. Cela permet de
l'appeler depuis un hook SubagentStop (le code 2 renvoie l'agent au travail).

LIMITES (a lire avant usage) :
  - ne dit RIEN du soutien : une phrase presente sur la page peut ne pas prouver l'enonce ;
  - une expression trouvee dans des commentaires ou un menu de la page compte comme trouvee ;
  - ne lit pas les pages rendues par JavaScript, derriere un 403 ou un controle anti-robot ;
  - si la ligne Source contient plusieurs URL, la citation est acceptee si elle figure
    sur l'une d'elles (le statut indique laquelle).
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from html.parser import HTMLParser

SKIP = ("script", "style", "noscript", "svg")
BREAK = ("p", "br", "li", "div", "h1", "h2", "h3", "h4", "tr", "td")
REPL = {0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"', 0xAB: '"', 0xBB: '"',
        0x2013: "-", 0x2014: "-", 0x2010: "-", 0x2011: "-", 0xA0: " ", 0x202F: " ",
        0xAD: None, 0x200B: None}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag in BREAK:
            self.out.append(" ")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag in BREAK:
            self.out.append(" ")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def norm(s):
    s = unicodedata.normalize("NFKC", s).translate(REPL)
    return re.sub(r"\s+", " ", s).strip().casefold()


def compact(s):
    return re.sub(r"[^0-9a-z]", "", s)


def get_page(url, cache):
    d = os.path.join(cache, hashlib.sha1(url.encode("utf-8")).hexdigest()[:16])
    os.makedirs(d, exist_ok=True)
    page, codef = os.path.join(d, "page.bin"), os.path.join(d, "code.txt")
    if not os.path.exists(page):
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-o", page,
                            "-w", "%{http_code}", url], capture_output=True, text=True)
        with open(codef, "w") as f:
            f.write(r.stdout.strip() or "000")
    with open(codef) as f:
        code = f.read().strip()
    with open(page, "rb") as f:
        raw = f.read()
    if raw[:4] == b"%PDF":
        out = page + ".txt"
        if not os.path.exists(out):
            subprocess.run(["pdftotext", page, out], capture_output=True)
        text = open(out, encoding="utf-8", errors="replace").read() if os.path.exists(out) else ""
    else:
        p = Text()
        p.feed(raw.decode("utf-8", errors="replace"))
        text = " ".join(p.out)
    return code, norm(text)


def blocks(md):
    for b in re.split(r"(?m)^### ", md)[1:]:
        ident = b.split("\n", 1)[0].split(":")[0].strip()
        m = re.search(r"(?m)^- Source :(.*)$", b)
        src = m.group(1) if m else ""
        cits = re.findall(r"(?m)^- Citation(?: \d+)? :\s*«\s*(.+?)\s*»", b)
        yield ident, src, cits


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    path = sys.argv[1]
    cache = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        tempfile.gettempdir(), "verifier-citations-cache")
    with open(path, encoding="utf-8") as f:
        md = f.read()
    counts = {"OK": 0, "ABSENT": 0, "BLOQUE": 0, "EXTRAIT": 0}
    for ident, src, cits in blocks(md):
        if not cits:
            continue
        if "extrait de recherche" in src.lower():
            for q in cits:
                counts["EXTRAIT"] += 1
                print(f"EXTRAIT  {ident}  non verifiable : {q[:70]}")
            continue
        urls = [u.rstrip(".,;)") for u in re.findall(r"https?://[^\s)»]+", src)]
        pages = []
        for u in urls:
            code, text = get_page(u, cache)
            pages.append((u, code, text))
        for q in cits:
            qn = norm(q.strip(" .…"))
            hit = None
            for u, code, text in pages:
                if qn and (qn in text or compact(qn) in compact(text)):
                    hit = u
                    break
            if hit:
                counts["OK"] += 1
                print(f"OK       {ident}  {hit[:60]}")
            elif not pages or all(c[0] in "45" or not t for _, c, t in pages):
                counts["BLOQUE"] += 1
                print(f"BLOQUE   {ident}  pages illisibles ({', '.join(c for _, c, _ in pages) or 'aucune URL'}) : {q[:60]}")
            else:
                counts["ABSENT"] += 1
                print(f"ABSENT   {ident}  {q[:90]}")
    print("\nRESUME : " + ", ".join(f"{k}={v}" for k, v in counts.items()))
    return 2 if counts["ABSENT"] or counts["BLOQUE"] else 0


if __name__ == "__main__":
    sys.exit(main())
