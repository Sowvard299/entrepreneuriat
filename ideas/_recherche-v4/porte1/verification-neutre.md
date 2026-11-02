# Vérification neutre (porte 1), 2026-11-02

Contrôle : WebFetch, curl pour l'API Sirene. Fichiers contrôlés non modifiés. Recherche web impossible : DuckDuckGo, Brave, Bing bloqués ou refusés, donc pas de « 1 recherche » par acteur.

| ID | URL | verdict | écart constaté |
|---|---|---|---|
| N-C6-2 | avere-france.org, barometre residentiel collectif T2 2026 (PDF) | ✔ | 44 331 / 32 069 / +38 % exacts. Pas de date de publication dans le texte (métadonnées : 2 sept. 2026). |
| N-C6-3 | tesla-mag.com/devis-borne-de-recharge | ✔ | 900-1 150 / 1 100-1 500 € (7 kW), 1 200-1 800 € (22 kW) exacts ; citation IRVE exacte ; maj 2026-10-15. |
| N-C6-4 | bevolt.com (actualité 279705) | ✔ | « seulement 62 % des points… disponibles 99 % du temps » exact ; 71 % en mai et 6 % > 7 jours exacts. Date des données non précisée. |
| N-C5-3 | batiweb.com (47365) | ✔ | « manquements graves » chez 34 % exact ; 1 000 professionnels ; 2025-09-30 ; échantillon de plaintes. |
| N-C5-1 | ecologie.gouv.fr/mon-accompagnateur-renov | ✔ | Citation exacte (FAQ), seuil 5 000 € TTC, maj 2026-04-20. |
| N-C1-1 | pennylane.com/fr/tarifs | ✔ | 7 / 14 / 24 / 79 € HT, citation exacte ; « 1 500 000 » = personnes, pas entreprises. |
| N-B1 | seekingalpha.com/pr/20410428 | ≈ | 630 M$ (+30 %), 81 821 acheteurs, 2026-02-24 exacts. Citation réelle : « Marketplace revenue for the full year of 2025 was $630 million, an increase of 30% year-over-year. » CA 686,6 M$ (+26 %) figure dans le tableau. |
| N-B2 | lespepitestech.com/…/tolery | ≈ | Phrase citée absente. Texte : « plateforme française de fabrication de pièces industrielles à la demande de grande qualité ». Ville : Paris (fiche) ou Challans (données entreprise), pas Nantes. Effectif 2-10, aucun CA. |
| N-B13 | API Sirene (curl, 2026-11-02) | ✔ | 25.62B : 7 970 tous effectifs, 1 587 ≥ 10 salariés ; 43.21A ≥ 10 : 3 321 ; exacts. |
| N-C1 | dogtopia.com/denver-tech-center/pricing | ≈ | 179 $/semaine et 35,80 $/jour absents. Page : « Unlimited Daycare » 185 $, « 1 Day Per Week » 53 $, « Full Day » 58 $. |
| N-C2 | dogtopia.com/pittsburgh-eastside/pricing | ✘ | Page inexistante (HTTP 404). 175 $/semaine non vérifiable. |
| N-C2 | dogtopia.com/houston/dog-daycare | ≈ | 42 $ = forfait « 1 day a week » (hebdomadaire), pas un prix à la journée. « Pay per play » : 44 $. |
| N-C1 | pet-insight.com/dogtopia-…-2025 | ≈ | « 300 sites » en 2026 exact (2026-02-04). 225 franchises, 41 propres, 266, +12 % absents ; l'article parle de 10 ans de croissance des ventes comparables. |
| N-B2 (B2C) | toute-la-franchise.com/news-club-pilates | ✔ | « 30 à 35 implantations d'ici fin 2026» exact ; 7 studios, 50 000 €, 380-450 k€, 93,5 %, 2026-01-30. |
| N-G1 | en.wikipedia.org/wiki/Mixue_Bingcheng | ✔ | « almost 60,000 stores in China and overseas » ; 59 823 ; 33,56 Md RMB ; 5,9 Md RMB ; IPO 3 mars 2025. Infobox cite le rapport 2024 : à recouper. |
| N-D1 (B2C) | fortune.com (2025-01-02, Othership) | ✔ | « Monthly Othership membership costs about $400 for 12 monthly classes ». |
| N-B3 | modelesdebusinessplan.com (pilates reformer) | ? | HTTP 429 à 3 essais. Citation « Paris reste… » non vérifiée. |
| N-C3 | zoomalia.com (Belles Truffes) ; franchise-magazine.com (PatchGuard) | ? | HTTP 403 pour les deux. 80 €/jour Paris non vérifié. |
| N-B3 (B2B) | businesswire.com (Procore) | ? | HTTP 403. 17 850 clients et 1,32 G$ non vérifiés. |
| N-D8 | xerfi.com/blog | ? | HTTP 403 puis 429. Aucune URL d'article dans le fichier : « 3 500 → 2 900 » non vérifié. |
| N-D1 | capeb.fr/actualites (page 1 sur 16) | ? | QBE non trouvé sur la page 1 (actualités de sept.-oct. 2026). URL de l'article absente du fichier. |
| N-D1 | france-epargne.fr (décennale, 600-2 500 €) | ? | Aucune URL dans le fichier : non vérifié. |

Bornes en copropriété (1 recherche) : le baromètre Avere cite les membres fondateurs de l'AFOR (oct. 2021) : Amperus, Borne Recharge Service, Parkèn Plug, Waat, Zephyre, Zeplug. Ce ne sont pas des parts de marché. Aucun montant en € dans le PDF.
Xometry (1 recherche) : investors.xometry.com en 403. Aucune taille de marché en € obtenue.

Bilan : ✔ 10 / ≈ 5 / ✘ 1 / ? 6 (22 lignes).
ID en ✘ ou ≈ portant un chiffre de score : N-B1 (630 M$, OK en chiffre), N-B2 (ville), N-C1 (Dogtopia 179 $ et 35,80 $ absents), N-C2 (Pittsburgh 404 ; Houston 42 $ = forfait hebdo), N-C1 pet-insight (225/41/266 absents).
