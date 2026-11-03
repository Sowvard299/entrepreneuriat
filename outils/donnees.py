"""Données publiques sourcées pour la recherche d'idée (API ouvertes, sans clé).

Chaque commande affiche les chiffres ET l'URL exacte interrogée, pour qu'un agent puisse
citer la preuve et qu'un vérificateur puisse la rejouer. Python 3, bibliothèque standard seule.

Usage :
  python outils/donnees.py taille 43.21Z          CA du secteur en France (Eurostat SBS), M€
  python outils/donnees.py croissance 43.21Z      indice de CA INSEE, moyennes annuelles
  python outils/donnees.py compter 43.21Z [--effectif 11,12]   entreprises actives (API entreprises)
  python outils/donnees.py acteurs 43.21Z         plus gros acteurs + part des 3 premiers
  python outils/donnees.py marches-publics "borne de recharge"   marchés publics notifiés (DECP)
  python outils/donnees.py echecs "borne de recharge"            procédures collectives (BODACC)
  python outils/donnees.py archive <url>          copie archivée d'une page bloquée (Wayback)
  python outils/donnees.py fiche 43.21Z           taille + croissance + compter + acteurs
  python outils/donnees.py ecran [--min 50] [--section N] [--top 40]
                                                  tous les secteurs français classés par croissance
  python outils/donnees.py controle <fichier.md>  part de chaque domaine, preuves « extrait », [HYPOTHÈSE]
"""

import re
from collections import Counter

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

UA = "Entrepreneuriat-recherche/1.0 (recherche documentaire, usage non commercial)"
AUJOURDHUI = date.today().isoformat()

# Sections NACE/NAF : première division de chaque section.
SECTIONS = [(1, "A"), (5, "B"), (10, "C"), (35, "D"), (36, "E"), (41, "F"), (45, "G"),
            (49, "H"), (55, "I"), (58, "J"), (64, "K"), (68, "L"), (69, "M"), (77, "N"),
            (84, "O"), (85, "P"), (86, "Q"), (90, "R"), (94, "S"), (97, "T"), (99, "U")]

DEPARTEMENTS = [f"{i:02d}" for i in range(1, 96) if i != 20] + ["2A", "2B",
                "971", "972", "973", "974", "976"]

# Tranches d'effectif salarié de Sirene : chaque entreprise en a une seule, donc la somme est exacte.
TRANCHES = {"NN": "non employeur ou inconnu", "00": "0 salarié", "01": "1-2", "02": "3-5",
            "03": "6-9", "11": "10-19", "12": "20-49", "21": "50-99", "22": "100-199",
            "31": "200-249", "32": "250-499", "41": "500-999", "42": "1000-1999",
            "51": "2000-4999", "52": "5000-9999", "53": "10000 et plus"}


def lire(url, tentatives=3, absent_si_400=False):
    for essai in range(tentatives):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 400 and absent_si_400:
                return {}
            if e.code == 429 and essai < tentatives - 1:
                time.sleep(2 * (essai + 1))
                continue
            corps = e.read().decode("utf-8", "replace")[:300]
            raise SystemExit(f"Erreur HTTP {e.code} sur {url}\n{corps}")
        except urllib.error.URLError as e:
            if essai < tentatives - 1:
                time.sleep(2)
                continue
            raise SystemExit(f"Réseau indisponible pour {url} : {e.reason}")


def source(url, organisme):
    print(f"Source : {organisme}, {url} (consulté le {AUJOURDHUI})")


def naf_parts(code):
    """'43.21Z' -> ('43.21', 'Z') ; '4321' -> ('43.21', '')."""
    c = code.upper().replace(" ", "")
    lettre = c[-1] if c[-1].isalpha() else ""
    chiffres = c.rstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZ").replace(".", "")
    if len(chiffres) < 2:
        raise SystemExit(f"Code NAF illisible : {code}")
    point = chiffres[:2] + ("." + chiffres[2:] if len(chiffres) > 2 else "")
    return point, lettre


def nace_eurostat(code):
    point, _ = naf_parts(code)
    division = int(point[:2])
    section = [s for d, s in SECTIONS if d <= division][-1]
    return section + point.replace(".", "")


def taux_annuel(debut, fin, annees):
    if not debut or annees <= 0:
        return None
    return ((fin / debut) ** (1 / annees) - 1) * 100


# --- Taille : Eurostat, statistiques structurelles d'entreprises -------------------------

def eurostat_serie(nace, indicateur):
    url = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?"
           + urllib.parse.urlencode({"format": "JSON", "lang": "FR", "geo": "FR",
                                     "nace_r2": nace, "indic_sbs": indicateur}))
    d = lire(url)
    if "error" in d or not d.get("value"):
        return url, {}
    temps = d["dimension"]["time"]["category"]["index"]
    inverse = {v: k for k, v in temps.items()}
    return url, {inverse[int(k) % len(temps)]: v for k, v in sorted(d["value"].items(), key=lambda x: int(x[0]))}


def taille(code):
    nace = nace_eurostat(code)
    while True:
        url, ca = eurostat_serie(nace, "NETTUR_MEUR")
        if ca or len(nace) <= 3:
            break
        nace = nace[:-1]  # repli sur le niveau supérieur si le détail est secret ou absent
    print(f"## Taille du secteur {nace} en France (chiffre d'affaires net, M€, Eurostat SBS)")
    if not ca:
        print("Aucune donnée (secret statistique ou code absent).")
        source(url, "Eurostat")
        return None, {}
    _, nb = eurostat_serie(nace, "ENT_NR")
    for an in sorted(ca):
        ligne = f"- {an} : {ca[an]:,.0f} M€".replace(",", " ")
        if an in nb:
            ligne += f" ; {nb[an]:,.0f} entreprises".replace(",", " ")
        print(ligne)
    ans = sorted(ca)
    t = taux_annuel(ca[ans[0]], ca[ans[-1]], int(ans[-1]) - int(ans[0]))
    if t is not None:
        print(f"Croissance annuelle moyenne {ans[0]}-{ans[-1]} : {t:+.1f} %/an (valeur, inflation comprise)")
    source(url, "Eurostat, sbs_ovw_act")
    return nace, ca


# --- Croissance : INSEE, indicateur d'activité et de chiffre d'affaires ------------------

def croissance(code):
    point, _ = naf_parts(code)
    essais = [point, point[:4], point[:2]] if len(point) > 4 else [point, point[:2]]
    for activite in dict.fromkeys(essais):
        url = "https://api.insee.fr/melodi/data/DS_ICA?" + urllib.parse.urlencode(
            {"ACTIVITY": activite, "FREQ": "M", "SEASONAL_ADJUST": "Y", "maxResult": 5000})
        obs = lire(url).get("observations", [])
        series = {}
        for o in obs:
            dims = o["dimensions"]
            series.setdefault(dims.get("IDX_TYPE"), []).append(
                (dims["TIME_PERIOD"], o["measures"]["OBS_VALUE_NIVEAU"]["value"]))
        if series:
            break
    if not series:
        print(f"## Croissance {point} : aucune série INSEE trouvée.")
        source(url, "INSEE Melodi, DS_ICA")
        return
    # Préférer un indice de chiffre d'affaires (valeur) à un indice de production (volume).
    type_idx = next((t for t in series if t and t.startswith("ICA")), next(iter(series)))
    par_an = {}
    for periode, valeur in series[type_idx]:
        par_an.setdefault(periode[:4], []).append(valeur)
    moyennes = {a: sum(v) / len(v) for a, v in par_an.items() if len(v) == 12}
    print(f"## Croissance {activite} (INSEE, indice {type_idx}, base 2021 = 100, CVS, moyennes annuelles)")
    ans = sorted(moyennes)[-6:]
    for a in ans:
        print(f"- {a} : {moyennes[a]:.1f}")
    if len(ans) >= 2:
        for n in (3, len(ans) - 1):
            if n < len(ans):
                t = taux_annuel(moyennes[ans[-1 - n]], moyennes[ans[-1]], n)
                print(f"Croissance annuelle moyenne sur {n} ans ({ans[-1 - n]}-{ans[-1]}) : {t:+.1f} %/an")
    if type_idx.startswith("ICA"):
        print("Indice en valeur : il inclut la hausse des prix.")
    source(url, "INSEE Melodi, DS_ICA")


# --- Comptages et acteurs : API Recherche d'entreprises ----------------------------------

API_ENT = "https://recherche-entreprises.api.gouv.fr/search?"


def codes_complets(code):
    point, lettre = naf_parts(code)
    if lettre:
        return [point + lettre]
    trouves = []
    for l in "ZABCDEFGH":
        params = {"activite_principale": point + l, "per_page": 1}
        # L'API répond 400 pour un code NAF qui n'existe pas.
        if lire(API_ENT + urllib.parse.urlencode(params), absent_si_400=True).get("total_results"):
            trouves.append(point + l)
        time.sleep(0.15)
    return trouves or [point + "Z"]


def compter_tranche(params):
    """Total pour une requête ; au-delà du plafond de 10 000, somme par département."""
    total = lire(API_ENT + urllib.parse.urlencode(params)).get("total_results", 0)
    if total < 10000:
        return total, False
    total = 0
    for dep in DEPARTEMENTS:
        total += lire(API_ENT + urllib.parse.urlencode({**params, "departement": dep})).get("total_results", 0)
        time.sleep(0.15)
    return total, True


def compter(code, effectif=None):
    tranches = effectif.split(",") if effectif else list(TRANCHES)
    for complet in codes_complets(code):
        params = {"activite_principale": complet, "etat_administratif": "A", "per_page": 1}
        comptes, approx = {}, []
        for t in tranches:
            comptes[t], par_dep = compter_tranche({**params, "tranche_effectif_salarie": t})
            if par_dep:
                approx.append(t)
            time.sleep(0.15)
        total = sum(comptes.values())
        employeurs = sum(n for t, n in comptes.items() if t not in ("NN", "00"))
        dix_plus = sum(n for t, n in comptes.items() if t not in ("NN", "00", "01", "02", "03"))
        print(f"## Entreprises actives {complet} : {total:,}".replace(",", " "))
        print(f"- employeuses (1 salarié ou plus) : {employeurs:,}".replace(",", " "))
        print(f"- 10 salariés ou plus : {dix_plus:,}".replace(",", " "))
        print("- détail : " + " ; ".join(f"{TRANCHES[t]} {n}" for t, n in comptes.items() if n))
        print("Unités légales actives au répertoire : inclut des micro-entreprises sans activité réelle.")
        if approx:
            print(f"Tranches {approx} sommées par département (une entreprise multi-sites peut compter deux fois).")
        source(API_ENT + urllib.parse.urlencode(params), "API Recherche d'entreprises (Insee Sirene, RNE)")


def acteurs(code, ca_min=None, eurostat=None):
    lignes = []
    for complet in codes_complets(code):
        seuils = [ca_min] if ca_min else [100_000_000, 20_000_000, 5_000_000, 1_000_000]
        for seuil in seuils:
            params = {"activite_principale": complet, "etat_administratif": "A",
                      "ca_min": int(seuil), "per_page": 25}
            url = API_ENT + urllib.parse.urlencode(params)
            d = lire(url)
            if d.get("total_results", 0) >= 10 or seuil == seuils[-1]:
                break
        for page in range(1, min(4, (d.get("total_pages") or 1)) + 1):
            if page > 1:
                d = lire(url + f"&page={page}")
                time.sleep(0.15)
            for r in d.get("results", []):
                # Un CA de plus de 3 ans ne dit rien de la position actuelle d'un acteur.
                fin = {a: v for a, v in (r.get("finances") or {}).items()
                       if v.get("ca") and int(a) >= date.today().year - 3}
                if fin:
                    an = max(fin)
                    lignes.append((fin[an]["ca"], an, r["nom_complet"], r["siren"], complet))
        print(f"## Acteurs {complet} avec CA ≥ {seuil / 1e6:g} M€ : {d.get('total_results', 0)} entreprises")
        source(url, "API Recherche d'entreprises (comptes annuels déposés)")
    lignes.sort(reverse=True)
    for ca, an, nom, siren, _ in lignes[:10]:
        print(f"- {nom} (SIREN {siren}) : {ca / 1e6:,.1f} M€ en {an}".replace(",", " "))
    if eurostat and lignes:
        nace, serie = eurostat
        top3 = sum(l[0] for l in lignes[:3])
        an_ref = max(serie)
        part = top3 / (serie[an_ref] * 1e6) * 100
        print(f"Part des 3 premières entités dans le CA du secteur {nace} ({an_ref}) : {part:.1f} %")
        print("Limites : parts par entité juridique et non par groupe (regrouper les filiales à la main) ;"
              " le CA d'une entreprise couvre toutes ses activités ; environ 45 % des dépôts de comptes"
              " sont confidentiels (INPI, 2025) : un gros acteur peut manquer, la part est une borne basse.")


# --- Argent public dépensé : données essentielles de la commande publique -----------------

def marches_publics(mots):
    base = ("https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/"
            "decp-2022-marches-valides/records?")
    params = {"where": f'search(objet,"{mots}")',
              "select": "count(*) as marches, sum(montant) as montant",
              "group_by": "year(datenotification)", "limit": 30}
    url = base + urllib.parse.urlencode(params)
    print(f"## Marchés publics dont l'objet contient « {mots} » (DECP)")
    for r in lire(url).get("results", []):
        an = r.get("year(datenotification)")
        print(f"- {an} : {r['marches']} marchés, {(r['montant'] or 0) / 1e6:,.1f} M€".replace(",", " "))
    print("Limites : plancher, pas un total (déclaration obligatoire seulement dès 40 000 € HT, sans sanction) ;"
          " montant = valeur maximale pour les accords-cadres ; un marché n'est pas une facture.")
    source(url, "data.economie.gouv.fr, DECP")


# --- Échecs : procédures collectives au BODACC ---------------------------------------------

def echecs(mots):
    base = ("https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/"
            "annonces-commerciales/records?")
    params = {"where": f'familleavis="collective" and search("{mots}")',
              "select": "count(*) as annonces", "group_by": "year(dateparution)", "limit": 30}
    url = base + urllib.parse.urlencode(params)
    print(f"## Annonces de procédures collectives mentionnant « {mots} » (BODACC)")
    for r in lire(url).get("results", []):
        print(f"- {r.get('year(dateparution)')} : {r['annonces']}")
    print("Limites : une entreprise peut avoir plusieurs annonces (ouverture, plan, clôture) ; recherche plein texte.")
    source(url, "BODACC, DILA")


# --- Écran : tous les secteurs français en une requête Eurostat ------------------------------

def eurostat_tous(indicateur):
    url = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?"
           + urllib.parse.urlencode({"format": "JSON", "lang": "FR", "geo": "FR", "indic_sbs": indicateur}))
    d = lire(url)
    nace = d["dimension"]["nace_r2"]["category"]
    temps = d["dimension"]["time"]["category"]["index"]
    code_de = {v: k for k, v in nace["index"].items()}
    an_de = {v: k for k, v in temps.items()}
    valeurs = {}
    for cle, v in d["value"].items():
        i_nace, i_an = divmod(int(cle), len(temps))
        valeurs.setdefault(code_de[i_nace], {})[an_de[i_an]] = v
    return url, valeurs, nace["label"]


def ecran(minimum=50.0, section=None, top=40):
    url, ca, libelles = eurostat_tous("NETTUR_MEUR")
    _, nb, _ = eurostat_tous("ENT_NR")
    lignes = []
    for code, serie in ca.items():
        if not re.fullmatch(r"[A-U]\d{4}", code) or (section and not code.startswith(section)):
            continue
        ans = sorted(serie)
        if len(ans) < 3 or serie[ans[-1]] < minimum:
            continue
        recent = taux_annuel(serie[ans[-3]], serie[ans[-1]], 2)
        long = taux_annuel(serie[ans[0]], serie[ans[-1]], int(ans[-1]) - int(ans[0]))
        rebond = len(ans) >= 2 and serie[ans[0]] > 0 and serie[ans[1]] / serie[ans[0]] > 1.25
        entreprises = nb.get(code, {}).get(ans[-1])
        lignes.append((recent, long, code, libelles.get(code, ""), serie[ans[-1]], ans[-1], entreprises, rebond))
    if not lignes:
        print("Aucun secteur ne passe les filtres.")
        return
    mediane = sorted(l[0] for l in lignes)[len(lignes) // 2]
    lignes.sort(reverse=True)
    print(f"## Secteurs français (NACE à 4 chiffres, CA ≥ {minimum:g} M€) classés par croissance récente")
    print(f"{len(lignes)} secteurs ; croissance médiane {mediane:+.1f} %/an (repère d'inflation et de conjoncture).")
    print("| Code | Secteur | CA (M€) | Croissance %/an (2 dernières années) | Écart à la médiane |"
          " %/an depuis la 1re année | Entreprises | CA moyen (k€) |")
    print("|---|---|---|---|---|---|---|---|")
    for recent, long, code, libelle, valeur, an, entreprises, rebond in lignes[:top]:
        moyen = f"{valeur * 1000 / entreprises:,.0f}".replace(",", " ") if entreprises else "?"
        nb_txt = f"{entreprises:,.0f}".replace(",", " ") if entreprises else "?"
        signe = " (rebond post-Covid ?)" if rebond else ""
        print(f"| {code} | {libelle[:60]} | {valeur:,.0f} ({an}) | {recent:+.1f} % | {recent - mediane:+.1f} pt |"
              f" {long:+.1f} %{signe} | {nb_txt} | {moyen} |".replace(",", " "))
    print("Lecture : CA en valeur (inflation comprise) ; la taille du secteur est un plafond, pas un SAM ;"
          " un CA moyen faible avec beaucoup d'entreprises signale un marché fragmenté.")
    source(url, "Eurostat, sbs_ovw_act (tous secteurs)")


# --- Contrôle qualité d'un fichier de travail ------------------------------------------------

def controle(chemin):
    texte = open(chemin, encoding="utf-8").read()
    urls = re.findall(r"https?://([^/\s)>\]]+)", texte)
    domaines = Counter(u.lower().removeprefix("www.") for u in urls)
    preuves = len(re.findall(r"^###\s", texte, flags=re.M))
    extraits = len(re.findall(r"extrait", texte, flags=re.I))
    hypotheses = texte.count("[HYPOTHÈSE")
    print(f"## Contrôle de {chemin}")
    print(f"- preuves (titres ###) : {preuves} ; URL citées : {len(urls)} ; domaines distincts : {len(domaines)}")
    print(f"- mentions « extrait » : {extraits} ; [HYPOTHÈSE] : {hypotheses}")
    for dom, n in domaines.most_common(5):
        part = n / len(urls) * 100
        alerte = "  ← au-dessus de 40 %" if part > 40 else ""
        print(f"- {dom} : {n} ({part:.0f} %){alerte}")
    if preuves and extraits / preuves > 0.3:
        print("Alerte : plus de 30 % de preuves vues en extrait de recherche.")


# --- Page bloquée : copie archivée ----------------------------------------------------------

def archive(page):
    url = "https://archive.org/wayback/available?" + urllib.parse.urlencode({"url": page})
    proche = lire(url).get("archived_snapshots", {}).get("closest")
    if proche and proche.get("available"):
        print(f"Copie archivée du {proche['timestamp'][:8]} : {proche['url']}")
        print("Citer la copie archivée ET sa date, pas la page vivante.")
    else:
        print("Aucune copie archivée : chercher une autre source.")
    source(url, "Internet Archive, API Wayback")


def main(args):
    option = lambda nom: args[args.index(nom) + 1] if nom in args else None
    if args and args[0] == "ecran":
        ecran(float(option("--min") or 50), option("--section"), int(option("--top") or 40))
        return
    if len(args) < 2 or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, valeur = args[0], args[1]
    if cmd == "controle":
        controle(valeur)
    elif cmd == "taille":
        taille(valeur)
    elif cmd == "croissance":
        croissance(valeur)
    elif cmd == "compter":
        compter(valeur, option("--effectif"))
    elif cmd == "acteurs":
        ca_min = option("--ca-min")
        acteurs(valeur, float(ca_min) if ca_min else None, taille(valeur))
    elif cmd == "marches-publics":
        marches_publics(valeur)
    elif cmd == "echecs":
        echecs(valeur)
    elif cmd == "archive":
        archive(valeur)
    elif cmd == "fiche":
        serie = taille(valeur)
        print()
        croissance(valeur)
        print()
        compter(valeur)
        print()
        acteurs(valeur, None, serie)
    else:
        print(__doc__)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1:])
