# Vérification des preuves : modeles-mrr-travail.md et modeles-acquire-travail.md

- Date : 2026-11-02 · Vérificateur : sous-agent haiku · Fichiers contrôlés : non modifiés
- Méthode : WebFetch (chiffres lus via résumeur, donc de seconde main), API Sirene via curl. Recherches concurrents : 2 par sujet.

## modeles-mrr-travail.md (10 preuves : M5, M6, M7 et F1 à F7)

| ID | URL | verdict | écart constaté |
|----|-----|---------|----------------|
| M6 | trustmrr.com/startup/calendesk | ≈ | Chiffres ✔ (20 918 $, 371 abo, 1,16 M$, mai 2020, 79/97 $ et 117/147 $). Citation réelle : « B2B SaaS helping therapists, psychologists, and service businesses manage bookings, payments, and client relationships. » |
| M7 | bulletpointpodcast.pages.dev (résumé de Starter Story) | ≈ | Citation paraphrasée (« Launched Bank Statement Converter in 2021 »). Date : 2025-07-20 (fichier : inconnue). Visiteurs : ~40 000/mois (fichier : ~62 500). Source originale starterstory.com : 404 |
| M5 | trustmrr.com/startup/angel-match | ✔ | Citation exacte ; 27 079 $ MRR, 325 abo, 987 394 $, janvier 2019 |
| F1 | ellty.com/blog/what-is-dealroom | ✘ | « 395 € » absent. « No monthly billing exists » : Premium 12 500 €/an min. Signal 18 000 et Foundersuite 216 000 absents. Auteur concurrent de Dealroom |
| F2 | lejournaldesentreprises.com (25 avr. 2025) | ≈ | 445 start-ups ✔, « près de 100 millions d'euros » ✔. « 12 500 BA » absent de l'article ; franceangels.org : erreur réseau (non vérifié) |
| F3 | pabau.com/fr/blog/doctolib-tarif + lonasante.com | ≈ | « Doctolib ne publie pas ses prix » ✔ ; ~135 € ✔ ; 149 € ✔ (lonasante, mensuel). 229 € absent ; Resalib 24,99 € et Liberlo 12 € absents des deux pages |
| F4 | recherche-entreprises (NAF 86.90F) | ✔ | total_results = 10 000 (plafond) ✔. « 814 » non revérifié |
| F5 | parseur.com/fr/convertir/releves-bancaires/en-excel | ≈ | « Téléversez un relevé bancaire » ✔. KontoCSV et FinConv absents de la page (elle cite Docparser, Nanonets, Docsumo) |
| F6 | parseur.com/pricing | ✔ | Gratuit 20 p. ; Micro 100 p. 49 € ; Mini 300 p. 89 € ; Starter 1 000 p. 129 € ; Premium 3 000 p. 269 € |
| F7 | resufit.com (blog, maj 2026) | ✘ | 4CVDesign 9,99 € absent ; Resume.io 29,95 $/4 sem. ; ResumeUp 29 $/mois (fichier 24,95) ; Enhancv 16,50 $ (fichier 24,99) |

Compte : ✔ 3 · ≈ 5 · ✘ 2 · ? 0. Taux d'erreur (≈ + ✘) : 7/10 = 70 %, au-dessus du seuil de 20 %.
Chiffres de score touchés : F1 (prix Dealroom) ✘ ; M7 (visiteurs, date) ≈ ; F3 (229 €) absent.

## modeles-acquire-travail.md (10 preuves : A1, A4, A8 et F1, F3, F6, F7, F8, F12, F13)

| ID | URL | verdict | écart constaté |
|----|-----|---------|----------------|
| A4 | blog.acquire.com/top-startup-listings-on-acquire-com-may-edition (21 mai 2025) | ✔ | CA TTM 278 k$, profit 142 k$, CA doublé, fondé 2021, prix 849 k$, clients non publiés. acquire.com redirige (301) vers blog |
| A1 | même article | ✔ | 4 300+ clients, churn < 2 %, 2015, CA 600 k$, profit 456 k$, prix 1,6 M$. Libellé anglais exact non relu (résumé) |
| A8 | podcasts.apple.com | ? | Domaine refusé par WebFetch (blocage) ; extrait non vérifiable |
| F1 | photographes.com | ✔ | « Sans engagement, tout inclus ! » présent ; cible photographes seulement ; « des milliers » sans chiffre |
| F3 | recherche-entreprises (NAF 74.20Z) | ✔ | total_results = 10 000 (plafond) ✔. « 7 374 à Paris » non revérifié |
| F6 | joinsecret.com/fr/kudos/alternatives | ≈ | Kudos 5 €/7 € absents de la page. Awardco, Guusto, Achievers absents ; présents : Vantage Circle, Slack, Xoxoday, Nectar, Hi5, Reward gateway, Clarity Wave |
| F7 | recherche-entreprises (tranche 32) | ✔ | 6 074 ✔ pour la tranche 32 seule ; somme 11 705 non revérifiée |
| F8 | lemlist.com/pricing | ✔ | Email 55 $/mois annuel, 69 $ mensuel ; Multichannel 87 à 109 $ ; USD ; aucun pays indiqué |
| F12 | fr.custplace.com/business/?p=22340 | ? | Domaine refusé par WebFetch (blocage) |
| F13 | recherche-entreprises (NAF 66.22Z) | ✔ | total_results = 10 000 (plafond) ✔. 66.22Y non revérifié |

Compte : ✔ 7 · ≈ 1 · ✘ 0 · ? 2. Taux d'erreur (≈ + ✘) : 1/8 vérifiables = 12,5 %, sous le seuil.

## Concurrents manqués (2 recherches par sujet, aucun résultat exploitable)
- A4 (reconnaissance Slack/Teams) : DuckDuckGo bloqué (CAPTCHA), Bing hors sujet (seul kudos.com, origine non précisée). Aucun éditeur FR trouvé ; absence non prouvée.
- M7 (conversion de relevés) : DuckDuckGo bloqué, Bing hors sujet. KontoCSV (cité par le fichier) non revérifié, domaine parqué selon le fichier.

## Actions
- modeles-mrr : relancer F1 (remplacer le prix Dealroom par 12 500 €/an min, sources à rouvrir), corriger F7 et M7 (date 2025-07-20, visiteurs 40 000), reprendre F3 (229 €) et F2 (12 500 BA).
- modeles-acquire : A8 et F12 à rouvrir par une autre source ; corriger F6 (prix et liste de concurrents).
