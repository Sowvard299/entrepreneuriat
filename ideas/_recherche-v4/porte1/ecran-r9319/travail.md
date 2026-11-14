# Écran R9319 (93.19Z) : travail
Mission : comprendre la croissance de R9319, 1 à 3 modèles qui encaissent, contre-preuve, probabilités. Date : 2026-11-03.
Recherches web utilisées : 2 sur 15 (+ 2 pages ouvertes en WebFetch). Preuves : 8. Domaines distincts : 6 (europa.eu, api.insee.fr, recherche-entreprises.api.gouv.fr, bodacc, gotrail.run, reference-trail.fr).
Statut : partiel (voir fin). Résultat des contrôles : voir fin de fichier.

### R93-01 : Taille et croissance Eurostat
- Acteur / marché : secteur R9319 France
- Type : tendance (N1)
- Source : https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=FR&geo=FR&nace_r2=R9319&indic_sbs=NETTUR_MEUR (date : 2026-11-03 ; N1 ; Eurostat)
- Citation : « 2024 : 3 181 M€ ; 14 299 entreprises »
- Chiffres : 1 615 M€ (2021) à 3 181 M€ (2024), +25,3 %/an en valeur ; entreprises 10 767 à 14 299
- Ce que ça dit pour nous : le CA double en 3 ans, mais en valeur et par entité juridique.

### R93-02 : Indice INSEE, la croissance ralentit
- Acteur / marché : secteur 93.19
- Type : contre-preuve
- Source : https://api.insee.fr/melodi/data/DS_ICA?ACTIVITY=93.19&FREQ=M&SEASONAL_ADJUST=Y&maxResult=5000 (date : 2026-11-03 ; N1 ; INSEE)
- Citation : « 2024 : 144.1 »
- Chiffres : base 2021=100 : 2020 85,6 ; 2022 119,6 ; 2023 137,0 ; 2024 144,1 ; 2025 139,4 (-3,3 % en 2025) ; +5,2 %/an sur 3 ans, +10,2 %/an sur 5 ans (rebond post-Covid inclus)
- Ce que ça dit pour nous : la croissance de +26 % est en partie un rebond 2020-2022 ; 2025 recule, sous le seuil de 8 %.

### R93-03 : Structure des entreprises (Sirene)
- Acteur / marché : 93.19Z
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=93.19Z&etat_administratif=A&per_page=1 (date : 2026-11-03 ; N1 ; Insee Sirene)
- Citation : « Entreprises actives 93.19Z : 45 634 »
- Chiffres : 2 973 employeuses ; 320 à 10 salariés ou plus ; 42 410 sans effectif connu. Le code contient beaucoup d'associations (clubs, courses) sans comptes : les requêtes API « running » et « trail » renvoient surtout des entités sans finances.
- Ce que ça dit pour nous : le marché payant réel est bien plus étroit que 14 299 ; clients B2B ≥ 3 000 non établi.

### R93-04 : Concentration et moteur de la croissance
- Acteur / marché : 93.19Z, plus gros CA déposés
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=93.19Z&etat_administratif=A&ca_min=20000000&per_page=25 (date : 2026-11-03 ; N1 ; Insee/RNE)
- Citation : « Part des 3 premières entités dans le CA du secteur R9319 (2024) : 47.3 % »
- Chiffres : FILIALE LFP 1 (créée 2021) 657,7 M€ ; ON LOCATION (hospitalité sportive) 471,9 M€ ; ASO 374,9 M€ ; GIE Rugby hospitalités 244,4 M€ (2023) ; OBIZ 99,7 M€. Top 3 = 47,3 % (borne basse) ; seuil < 40 %.
- Ce que ça dit pour nous : la croissance vient de droits de ligue et d'hospitalité de très grands événements, pas d'un segment PME accessible.

### R93-05 : Playground (organisateur d'événements de course)
- Acteur / marché : Playground, événements sportifs grand public
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=827641184 (date : 2026-11-03 ; N1 ; Insee/RNE)
- Citation : « PLAYGROUND »
- Chiffres : CA 14,40 M€ 2024, résultat +1,18 M€ ; créée 2017 ; 10-19 salariés
- Ce que ça dit pour nous : créée en 2017, 14 M€ et rentable : le modèle encaisse, mais sur de grands événements à forte jauge.

### R93-06 : Autres acteurs avec CA déposé
- Acteur / marché : LS UCPA Sports Event ; Kings League France ; F50 League France
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=502054786 (date : 2026-11-03 ; N1 ; Insee/RNE)
- Citation : « LS UCPA SPORTS EVENT »
- Chiffres : UCPA Sports Event 6,42 M€ 2024, résultat -1,49 M€ ; Kings League France (créée 2023) 12,72 M€ 2025, résultat -4,84 M€ ; F50 League 5,64 M€ 2023, résultat +0,32 M€
- Ce que ça dit pour nous : 3 acteurs avec CA déposé, mais 2 sur 3 perdent de l'argent.

### R93-07 : Prix publics d'inscription à des courses
- Acteur / marché : trails et courses, prix payé par le coureur
- Type : argent dépensé
- Source : https://gotrail.run/fr/course/flowtrail (date : 2026 ; N2 ; plateforme d'inscription)
- Citation : « Des inscriptions sur place sont possibles au tarif majoré de 2,00 € »
- Chiffres : Flowtrail 11 km 20 €, 17 km 30 €, 25 km 40 €. Prom Classic 19 / 24 / 27 € + 1,50 € de frais, jauge 15 000 (https://reference-trail.fr/quel-est-le-prix-de-la-prom-classic-2026/, N3). Troisième prix : [NON OUVERT].
- Ce que ça dit pour nous : 2 prix ouverts sur 3 requis ; panier de 20 à 40 € par inscrit.

### R93-08 : Échecs, mot-clé « sport »
- Acteur / marché : procédures collectives plein texte « sport » (tous codes)
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22sport%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; N1 ; DILA)
- Citation : « 2025 : 2701 »
- Chiffres : 1 710 (2022), 2 005 (2023), 2 378 (2024), 2 701 (2025), 2 219 déjà en 2026 ; plein texte donc bruité
- Ce que ça dit pour nous : +58 % d'annonces entre 2022 et 2025 : les échecs s'emballent.

## Analyse
- Taux de base : ensemble 69,0 % à 5 ans (SINE 2018, CLAUDE.md) ; micro-entrepreneurs 28 %. Classe exacte arts-loisirs : [NON OUVERT].
- Croyance la plus fragile : un nouvel organisateur remplit des courses à 20-40 € sans marque ni communauté. Test porte 2 : page d'inscription anticipée remboursable pour une course datée, mention « première édition » (L.221-14, L.221-18), seuil écrit avant : 100 dossards payés à 25 € pour 750 € de pub. Formalités de déclaration de la manifestation : [NON OUVERT].
- Probabilités au 2026-11-03 (ancrées sur 69 %, aucune preuve N1-N2 de demande) : P(porte 2) 25 % ; P(vie à 3 ans) 55 % ; P(CA ≥ 500 k€ à 3 ans) 10 %.
- Non établi : nombre de clients, SOM, CA de petits organisateurs (surtout des associations sans comptes), padel et coaching (probablement en 93.11Z / 93.13Z, non vérifié).

## Sources non lues
- https://www.sportbusiness.club/?p=194486 : extrait seulement.
- https://my.motherbase.ai/startup/145824-playground-event : N4, non ouvert.

## Contrôles (2026-11-03)
controle : 8 preuves, 8 domaines, max 36 % (API Sirene). verifier-citations : OK=3, ABSENT=4, BLOQUE=1, EXTRAIT=0. Les 4 ABSENT (R93-01, 02, 03, 08) et le BLOQUE (R93-04, 429) citent des lignes de sortie de outils/donnees.py (fiche, echecs), pas du JSON brut de l URL : non retrouvables par le script, à vérifier à la main.
