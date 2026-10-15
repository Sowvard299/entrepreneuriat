# Phase 0 : marchés par fragmentation (lentille 3) et capital/réseaux (lentille 6)

- Mission : cartographier 9 marchés français (fiches au gabarit du skill market-segment-scanner), lentilles 3 et 6.
- Date : 2026-10-13
- Recherches web utilisées : 19 / 25 (terminé ; 9 marchés, 39 preuves, voir « Bilan » en fin de fichier)
- Option A : `_recherche/`, `_recherche-v2/`, `recrutement-garages/` non lus.
- Marchés : B1 gestion locative | B2 secrétariat de cabinets de santé | B3 auto-écoles | B4 formation professionnelle | B5 entretien-réparation auto | B6 transmission de TPE | B7 aide à domicile seniors en réseau | B8 salles de sport en réseau | B9 soins vétérinaires.
- Lentille 3 (fragmentation) : B1, B2, B3, B4, B5. Lentille 6 (capital et réseaux) : B6, B7, B8, B9 (B3 et B5 ont aussi des preuves de réseaux/capital).
- Comptages Sirene : API recherche-entreprises, champ `total_results`, entreprises actives (`etat_administratif=A`), NAF rév. 2 (le filtre `activite_principale` ; l'API renvoie aussi `activite_principale_naf25`). L'API est limitée en débit (429) : comptages par région quand le total national dépasse 10 000.
- Nombre de preuves / domaines distincts : voir « Bilan » en fin de fichier.

---

## B6 : Cédants de TPE qui paient un intermédiaire pour vendre leur entreprise

### [Marché B6 : cédants de TPE/PME (1 à 49 salariés) paient un courtier ou conseil en cession, pour trouver un repreneur]
- Taille France : pas de taille publiée. Calcul bottom-up en volume d'opérations : 26 000 transmissions réalisées en 2024 (Bpifrance Le Lab, nov. 2025, entreprises de 1 à 4 999 salariés, volume) ; potentiel annuel 74 000. Dépense : aucun barème français sourcé, seulement 5 à 10 % du prix avec plancher (B6-p3, confiance faible). Scénario [HYPOTHÈSE] : 25 % des opérations passent par un intermédiaire × 6 000 € d'honoraires moyens = 26 000 × 25 % × 6 000 € = 39 M€ (réalisé 2024) ; 74 000 × 25 % × 6 000 € = 111 M€ (si le potentiel se réalise). Confiance faible.
- Croissance : non établie en %. Moteur démographique : 40 % des dirigeants veulent transmettre dans les 5 ans, 370 000 entreprises concernées d'ici 2030 (B6-p1, institutionnelle : Bpifrance). Écart réalisé/potentiel : 26 000 sur 74 000 par an. Valeur ou volume : volume.
- Moteur de croissance : vague de départs de dirigeants (échéance 2030), Bpifrance Le Lab nov. 2025 (B6-p1).
- Acteurs : intermédiaires très nombreux (experts-comptables, avocats, courtiers, plateformes) ; part des 3 premiers non publiée [HYPOTHÈSE : < 10 %]. Plateformes : fusacq 2 061 annonces de cession affichées (B6-p2) ; cessionpme bloquée.
- Clients identifiables : 370 000 entreprises potentiellement transmissibles d'ici 2030 (B6-p1). Sirene : les dirigeants personnes physiques portent une année de naissance (non exploité ici, à faire en phase 1). Zone : France entière.
- Demande : tendance 5 ans non mesurée (pas de Google Trends dans ce run).
- Modèle d'exécution : service outillé (conseil, mise en relation, dossier de présentation). Pas d'employés. Droit à vérifier par l'auditeur : la négociation de fonds de commerce relève peut-être de la carte professionnelle agent immobilier [HYPOTHÈSE à confirmer, article de loi non cité].
- Contre-preuve (obligatoire) : un expert-comptable déconseille l'intermédiaire coûteux pour une TPE cédée à son salarié, et fusacq diffuse les annonces gratuitement (B6-p3, B6-p2) : la dépense par TPE est faible et la plateforme leader est gratuite.
- Seuils CLAUDE.md : taille ✘ (39 M€ réalisé, 111 M€ potentiel, hypothèses) | croissance ✔ par moteur structurel daté 2030 (pas de %) | concentration ✔ [HYPOTHÈSE] | clients ✔ (370 000)
- Confiance : faible (honoraires non sourcés)

### B6-p1 : Bpifrance, transmissions réalisées vs potentielles
- Acteur / marché : Bpifrance Création, étude Bpifrance Le Lab nov. 2025, transmission d'entreprises 1 à 4 999 salariés
- Type : tendance (institutionnelle)
- Source : https://bpifrance-creation.fr/moment-de-vie/quel-est-marche-reprise-dentreprise-aujourdhui (date : 2025-11 pour l'étude ; page ouverte le 2026-10-13)
- Citation : « seules 26 000 transmissions ont été réalisées en 2024 »
- Chiffres : 370 000 entreprises transmissibles d'ici 2030 ; potentiel 74 000/an ; 40 % des dirigeants prévoient de transmettre sous 5 ans ; 70 % de ceux qui prévoient à plus d'un an n'ont rien préparé ; la majorité des entreprises à céder ont moins de 5 salariés
- Ce que ça dit pour nous : le flux de cédants est structurel et daté, mais 2/3 des projets n'aboutissent pas : le problème est la mise en relation et la préparation, pas le nombre de cédants.

### B6-p2 : fusacq, offre et demande d'entreprises à vendre
- Acteur / marché : fusacq.com, plateforme d'annonces de cession (gratuite pour diffuser)
- Type : recherche active
- Source : https://www.fusacq.com/ (date : 2026-10-13, page ouverte)
- Citation : « Diffusez gratuitement vos annonces »
- Chiffres : 2 061 annonces de cession d'entreprise ; 10 201 acheteurs au total dans le bloc « Vendre une entreprise » dont 9 338 acheteurs potentiels ; 407 CV de repreneurs
- Ce que ça dit pour nous : il y a plus d'acheteurs affichés que d'annonces (environ 5 pour 1), mais la mise en visibilité est gratuite : le revenu doit venir de l'accompagnement, pas de l'annonce.

### B6-p3 : honoraires d'intermédiaires, ordre de grandeur et limites pour les TPE
- Acteur / marché : cabinets de conseil en cession (Hayot, Hectélion, etc.)
- Type : recherche active (prix constatés sur sites de prestataires)
- Source : extrait de recherche (non ouverte), requête « honoraires courtier cession petite entreprise TPE ». Pages citées : https://hayot-expertise.fr/blog/mandat-cession-mandataire-banque-affaires-honoraires et https://www.hectelion.com/publications/honoraires-mandat-cession-ma-retainer-success-fee (date inconnue)
- Citation : paraphrase d'extrait, pas de citation littérale : commission de 5 à 10 % du prix de vente, plus élevée avec plancher sur les petites opérations ; un expert-comptable déconseille l'intermédiaire à une TPE cédée à un salarié
- Chiffres : 5 à 10 % (source orientée pratiques anglo-saxonnes, non française) ; aucun barème légal
- Ce que ça dit pour nous : aucun prix français fiable : c'est la première chose à valider par appels à 5 intermédiaires.

---

## B3 : Candidats au permis B qui paient une auto-école (traditionnelle ou en ligne)

### [Marché B3 : candidats au permis B (surtout 17-25 ans) paient une auto-école pour code + conduite]
- Taille France : bottom-up, permis B seul, valeur : 963 314 permis délivrés en 2025 × 1 335 € (prix moyen forfait 20 h, Codes Rousseau) = 1,29 Md€ ; × 1 500 € (prix moyen cité par le PDG d'Ornikar) = 1,45 Md€ (B3-p1, B3-p3). Xerfi : 2,1 Md€ en 2022 (B3-p4, confiance faible). Fourchette retenue : 1,3 à 1,5 Md€, confiance moyenne.
- Croissance : non établie. Volume : 1 609 329 candidats à l'épreuve pratique en 2025, pas de série pluriannuelle (B3-p3). Ornikar +33 % de CA en 2024 (B3-p2) = gain de part de marché de l'entreprise, pas croissance du marché. Prix moyen en baisse de 2 500 à 1 500 € selon Ornikar (B3-p1).
- Moteur de croissance : aucun moteur identifié de hausse de la demande. Moteur de transfert : bascule vers les plateformes (environ 20 % du marché pour les 4 premiers acteurs numériques, B3-p1).
- Acteurs : 11 657 entreprises pour 13 345 établissements en 2022, 49,8 % sans salarié (B3-p4, Insee relayé par un site de conseil). 3 premiers : Ornikar environ 10 %, avec En Voiture Simone 14 % (rachat annoncé le 2026-06-02, B3-p1).
- Clients identifiables : B2C : environ 960 000 nouveaux titulaires par an (B3-p3). B2B (auto-écoles) : voir B3-p5 (comptage API).
- Demande : non mesurée (pas de Google Trends dans ce run).
- Modèle d'exécution : service à forte main-d'œuvre (moniteurs, souvent indépendants via plateforme). Plateforme à deux faces : risque « cimetière v2 ».
- Contre-preuve (obligatoire) : le marché se consolide (Ornikar rachète En Voiture Simone en juin 2026) et le prix moyen a baissé d'environ 40 % selon le leader (B3-p1) ; goulot d'examen (création de créneaux supplémentaires annoncée, B3-p3) : la croissance n'est pas prouvée et le leader numérique a 145 M€ de CA cumulé.
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non établie) | concentration ✔ (14 %) | clients ✔
- Confiance : moyenne (bottom-up sur chiffres officiels de volume, prix issus de sources privées)

### B3-p1 : Ornikar rachète En Voiture Simone
- Acteur / marché : Ornikar et En Voiture Simone, auto-écoles en ligne
- Type : argent dépensé
- Source : https://lautomobiliste.fr/02/06/2026/ornikar-rachete-voiture-simone/ (date : 2026-06-02, page ouverte)
- Citation : « le prix moyen à 1 500 euros contre 2 500 euros »
- Chiffres : CA 2025 Ornikar 104 M€, En Voiture Simone 38 M€ (cumul environ 145 M€ selon l'article) ; environ 100 000 nouveaux candidats au permis par an (70 000 + 30 000) ; part de marché 10 % puis 14 % ; 4 acteurs numériques environ 20 % ; 3 000 enseignants indépendants
- Ce que ça dit pour nous : l'argent circule (145 M€ de CA en ligne) mais le leader vient de racheter son seul rival : peu de place pour un 3e généraliste.

### B3-p2 : Ornikar passe 100 M€ de CA
- Acteur / marché : Ornikar
- Type : argent dépensé
- Source : https://www.maddyness.com/2025/02/04/ornikar-passe-la-barre-des-100-millions-deuros-de-revenus-et-poursuit-sa-diversification/ (date : 2025-02-04, page ouverte)
- Citation : « dépassé les 100 millions d'euros de chiffre d'affaires »
- Chiffres : +33 % de CA en 2024 (déclaration de l'entreprise) ; 700 000 clients actifs sur 12 mois ; 4,5 M de clients depuis 2013 ; revendique 40 % du marché du code ; équilibre atteint sur l'activité auto-école
- Ce que ça dit pour nous : le modèle en ligne a mis plus de 10 ans à atteindre l'équilibre : ce n'est pas une piste rapide.

### B3-p3 : volumes d'examens 2025 et prix moyens
- Acteur / marché : Sécurité routière (chiffres cités), Codes Rousseau (prix), via En Voiture Simone
- Type : tendance
- Source : https://www.envoituresimone.com/demarches-et-informations/informations-permis/taux-reussite (date : mise à jour 2026-08-11, page ouverte ; la source primaire n'est pas citée sur la page)
- Citation : « 963 314 élèves ont eu leur permis, dont 585 144 du premier coup »
- Chiffres : 1 609 329 candidats à la pratique en 2025 ; taux de réussite pratique 59,9 % ; prix moyens Codes Rousseau : 1 335 € (boîte manuelle, 20 h), 1 525 € (conduite accompagnée), 1 029 € (boîte automatique)
- Ce que ça dit pour nous : le volume de base (environ 1 M de permis par an) est solide, mais la page vient d'un acteur concerné (domaine à ne pas dépasser en part de preuves).

### B3-p4 : nombre d'établissements et taille Xerfi
- Acteur / marché : enseignement de la conduite, Insee relayé par Propulse by CA, Xerfi
- Type : tendance
- Source : extrait de recherche (non ouverte) : https://propulsebyca.fr/idees-business/auto-ecole/etude-marche ; https://www.xerfi.com/presentationetude/le-marche-des-auto-ecoles_sme18 (date : 2022-2023 pour les données)
- Citation : paraphrase d'extrait, pas de citation littérale : 11 657 entreprises, 13 345 établissements (2022), 49,8 % sans salarié ; marché 2,1 Md€ en 2022 (Xerfi)
- Chiffres : voir ci-dessus ; Xerfi = confiance faible
- Ce que ça dit pour nous : le secteur est très atomisé (la moitié sont des indépendants sans salarié) ; Xerfi seul ne suffit pas.

---

## B8 : Abonnés qui paient une salle de sport en réseau (low-cost et franchises)

### [Marché B8 : adhérents (6,2 M) paient un abonnement de salle de sport ; dépense captée de plus en plus par des réseaux capitalistiques]
- Taille France : environ 2,6 Md€ en 2020 (valeur, CA des clubs ; Observatoire de la franchise, page de 2023, B8-p1) ; plus de 3,5 Md€ selon l'Union Sport & Cycle (extrait de recherche, date inconnue, B8-p3) ; fourchette 2,5 à 3,5 Md€, estimations divergentes. Confiance faible.
- Croissance : 6,2 M d'abonnés, +16 % entre 2015 et 2020 (volume, environ 3 %/an, B8-p1) ; CA 2020 +0,97 % vs 2019 (valeur, B8-p1). Basic-Fit France : CA de 559,7 à 659,8 M€ sur un an, soit environ +18 % (extrait, source primaire non identifiée, B8-p3) : c'est un gain de part d'un réseau. Aucune source institutionnelle de croissance : [HYPOTHÈSE] 3 à 8 %/an.
- Moteur de croissance : pénétration française environ 10 % selon Basic-Fit (extrait, B8-p3) ; low-cost ; 3 clubs sur 10 en réseaux de franchise (B8-p1).
- Acteurs : Basic-Fit environ 894 clubs fin 2025 (extrait B8-p3, mais Codata 2025 donne 537 clubs, +35 en 2025 : contradiction non résolue, B8-p2) ; Fitness Park plus de 410 clubs et « une centaine » d'ouvertures par an (extrait B8-p3) ; Keepcool environ 270. Part des 3 premiers : environ 1 570 clubs sur 6 900 établissements (USC) = 23 % en nombre de clubs (calcul avec périmètres et années mélangés).
- Clients identifiables : B2C : 6,2 M d'abonnés (B8-p1). B2B (entreprises du secteur) : 5 878 entreprises actives en NAF 93.13Z (B8-p4).
- Demande : non mesurée.
- Modèle d'exécution : actif lourd (loyers, équipements) ; produit/service à fort capital. Hors de portée de 5 000 € ; seule piste crédible : service aux salles indépendantes (logiciel, marketing) [HYPOTHÈSE à tester].
- Contre-preuve (obligatoire) : croissance du marché de +0,97 % en valeur sur 2019-2020 et estimations de taille qui varient de 2,5 à 3,5 Md€ (B8-p1, B8-p3) : la croissance vient des réseaux qui prennent des parts, pas d'un marché qui s'élargit.
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non établie ≥ 8 %) | concentration ✔ (23 % en nombre de clubs) | clients ✔
- Confiance : faible

### B8-p1 : Observatoire de la franchise, marché du fitness
- Acteur / marché : salles de sport en France ; Fitness Park
- Type : tendance
- Source : https://www.observatoiredelafranchise.fr/dossier-franchise/quel-est-le-marche-du-fitness-en-france-2270.htm (date : 2023-11-08, page ouverte ; chiffres de 2020)
- Citation : « près de 2,6Mds€ » (en 2020)
- Chiffres : 4 540 clubs en 2020 (+4 %) ; 6,2 M d'abonnés (+16 % de 2015 à 2020) ; 3 clubs sur 10 en franchise ; Fitness Park 273 clubs, CA 230 M€, plus de 1 M d'adhérents
- Ce que ça dit pour nous : l'argent dépensé est avéré (plus de 2,5 Md€) mais la source est ancienne et d'un portail de franchise.

### B8-p2 : classement Codata 2025 (ouvertures nettes)
- Acteur / marché : réseaux de fitness et de beauté, L'Express Franchise
- Type : argent dépensé (ouvertures)
- Source : https://lexpress-franchise.com/actualites/classement-codata-2025-enseignes-qui-ont-le-plus-etoffe-leur-parc/ (date : 2026-06-11, mis à jour 2026-06-18, page ouverte)
- Citation : pas de citation littérale pour Basic-Fit (tableau lu via résumé de l'outil) ; données : Basic-Fit 537 points de vente, +35 nets en 2025 ; Adopt 324 (+72) ; Normal 202 (+53)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : les ouvertures de 2025 sont de l'ordre de dizaines par enseigne, pas de centaines : le rythme « 100 clubs par an » de Fitness Park est une annonce à vérifier.

### B8-p3 : Basic-Fit, Fitness Park, Union Sport & Cycle (extraits)
- Acteur / marché : Basic-Fit France, Fitness Park, Keepcool, USC
- Type : argent dépensé
- Source : extrait de recherche (non ouverte) : https://www.presse-citron.net/basic-fit-double-nombre-salles-de-sport-europe-rachat-clever-fit/ et pages de modelesdebusinessplan.com (blog, confiance faible) (date : 2025-2026)
- Citation : paraphrase d'extrait, pas de citation littérale : Basic-Fit 528 clubs français fin 2021 puis 894 fin 2025 ; Fitness Park plus de 410 clubs ; USC : plus de 6 900 établissements, plus de 3,5 Md€
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : à ouvrir directement (rapport annuel Basic-Fit, USC) avant de retenir ces chiffres.

### B8-p4 : comptage Sirene des entreprises de clubs de sport
- Acteur / marché : NAF 93.13Z (activités des centres de culture physique)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=93.13Z&etat_administratif=A&per_page=1 (date : 2026-10-13, requête exécutée)
- Citation : « "total_results":5878 »
- Chiffres : 5 878 entreprises actives (sous le plafond de 10 000)
- Ce que ça dit pour nous : le nombre d'entreprises (5 878) est proche des 6 900 établissements de l'USC : peu de multi-sites, donc un tissu encore d'indépendants.

---

## B7 : Familles et départements qui paient l'aide à domicile des seniors, via des agences en réseau

### [Marché B7 : seniors (ou leurs enfants) et départements (APA) paient des heures d'aide à domicile à une agence]
- Taille France : APA (tous lieux) 6,7 Md€ en 2022 (extrait DREES, B7-p3), non ventilé entre domicile et établissement : l'ordre de grandeur de l'aide à domicile dépasse donc largement 50 M€. Franchise « services aux personnes » : 10 671 points de vente (FFF, 2025, B7-p1). Pas de calcul bottom-up fiable (panier non sourcé).
- Croissance : franchise services aux personnes CA +9,6 % en 2025 (valeur, FFF via Républik, B7-p1). Contradiction : bénéficiaires de l'APA à domicile −0,7 % fin 2025, 820 600 (DREES, provisoire, volume, B7-p3). Deux sources dont une institutionnelle, mais elles divergent.
- Moteur de croissance : vieillissement de la population [HYPOTHÈSE, projection Insee non ouverte dans ce run] ; hausse de la demande de services à domicile selon la FFF (B7-p1).
- Acteurs : Petits-fils 212 agences fin 2021, 54 ouvertures en 2021, objectif 300 en 2025 (extrait, B7-p2) ; Amelis (Sodexo), Shiva (dynamique en centre-ville, B8-p2 pour la citation). Part des 3 premiers non publiée [HYPOTHÈSE : < 10 %].
- Clients identifiables : 820 600 bénéficiaires de l'APA à domicile (B2C, B7-p3).
- Demande : non mesurée.
- Modèle d'exécution : service à forte main-d'œuvre (employeur) : piège « agence locale de plus ». À ne garder que si le seuil de SOM et un avantage difficile à copier sont démontrés.
- Contre-preuve (obligatoire) : 37 % des structures de la fédération UNA se disent en difficulté financière, 17 % en risque de rupture de trésorerie (lettre ouverte UNA, avril 2025, B7-p4) ; nombre de bénéficiaires en repli en 2025 (B7-p3).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (sources contradictoires) | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : faible

### B7-p1 : chiffres FFF 2025 par secteur
- Acteur / marché : services aux personnes en franchise, services automobiles, formation
- Type : tendance (fédération professionnelle)
- Source : https://www.republikgroup.com/articles/2f542b9a-eeb8-f111-a6a9-6045bdf5ca6d/R%C3%A9seaux,%20points%20de%20vente,%20secteurs%20moteurs%20:%20ce%20que%20r%C3%A9v%C3%A8lent%20les%20chiffres%202025%20de%20la%20franchise (date : 2026-03-10, page ouverte après redirection depuis republik-retail.fr)
- Citation : « les services aux personnes suivent avec +9,6 % »
- Chiffres : services aux personnes 10 671 points de vente, CA +9,6 % ; services automobiles 11 486 points de vente, 6,02 Md€ ; formation CA +18,6 %, points de vente +12,9 % ; bâtiment CA +7,4 % ; hôtellerie CA +9,2 % ; ensemble de la franchise (FFF) : 2 035 réseaux, 93 395 points de vente, 93,71 Md€ (+4,9 %) en 2025 (extrait de recherche, https://www.franchise-fff.com/wp-content/uploads/2026/03/FFF-CP-indicateursFranchise2025-mars2026-V2.pdf, PDF illisible)
- Ce que ça dit pour nous : la franchise de services aux personnes croît plus vite (+9,6 %) que l'ensemble (+4,9 %), mais en CA du réseau, pas en nombre de bénéficiaires.

### B7-p2 : Petits-fils, ouvertures d'agences
- Acteur / marché : Petits-fils, aide à domicile seniors en franchise
- Type : argent dépensé (investissement des franchisés)
- Source : extrait de recherche (non ouverte) : https://www.toute-la-franchise.com/news-542767-objectif-300-implantations-d-ici-2025-pour-petits-fils-qui-vise-desormais-les-villes-de-taille-moyenne.html (date : environ 2022, à confirmer)
- Citation : paraphrase d'extrait, pas de citation littérale : 212 agences après 54 ouvertures en 2021 (50 en franchise) ; objectif 300 en 2025 ; Amelis : droit d'entrée 40 000 €, investissement global 120 000 € (donnée ancienne, 2016)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : les franchisés investissent 100 000 € et plus pour ouvrir une agence : le ticket d'entrée dépasse notre budget de 5 000 €.

### B7-p3 : DREES, aides sociales à domicile 2025 (provisoire)
- Acteur / marché : bénéficiaires APA à domicile
- Type : contre-preuve
- Source : extrait de recherche (non ouverte) : https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/260903-aides-sociales-domicile-personnes-agees-aides-sociales-personnes-handicap%C3%A9e-2025 (date : 2026-09, données provisoires)
- Citation : paraphrase d'extrait, pas de citation littérale : 837 000 bénéficiaires d'aides à domicile (−0,8 %) ; APA à domicile 820 600 (−0,7 %) ; APA 2022 : 6,7 Md€
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : la demande solvabilisée par les départements recule pour la première fois depuis 2020.

### B7-p4 : UNA, difficultés financières des services d'aide à domicile
- Acteur / marché : fédération UNA (services d'aide à domicile)
- Type : plainte (fédération)
- Source : extrait de recherche (non ouverte) : https://una.fr/wp-medias/2025/04/Lettre-ouverte-UNA-VF-240425.pdf (date : 2025-04)
- Citation : paraphrase d'extrait, pas de citation littérale : 37 % des structures en difficulté financière dont 17 % en risque de rupture de trésorerie ; 18 % des aides à domicile sous le seuil de pauvreté
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : marges fines et main-d'œuvre précaire : cohérent avec le rejet des agences locales de la v2.

---

## B9 : Propriétaires d'animaux qui paient des soins vétérinaires, avec consolidation par des groupes financés

### [Marché B9 : propriétaires d'animaux paient des consultations et actes en clinique vétérinaire ; clients intermédiaires possibles : les cliniques]
- Taille France : environ 4,7 Md€ de CA des cliniques, calculé : 800 M€ pour environ 1 000 cliniques de groupes = 17 % du secteur (Asterès pour le SYNGEV, données 2022, B9-p2) donc 800 ÷ 0,17 ≈ 4,7 Md€. Valeur. Confiance faible (étude commandée par un syndicat d'employeurs).
- Croissance : non chiffrée. L'Autorité de la concurrence constate une hausse générale des tarifs (valeur, B9-p1), pas de série de volume. [HYPOTHÈSE] croissance en valeur portée par les prix.
- Moteur de croissance : entrée de fonds au capital des cliniques (« réseaux corporate »), B9-p1.
- Acteurs : un vétérinaire sur cinq exerce dans un groupe (2023) ; les six premiers acteurs détiennent 15 % des cliniques (amendement parlementaire, extrait B9-p3).
- Clients identifiables : cliniques et cabinets vétérinaires : voir comptage API NAF 75.00Z (B9-p4).
- Demande : non mesurée.
- Modèle d'exécution : exercice réglementé : nous ne pouvons pas soigner. Seul angle ouvert : service aux cliniques (logiciel, recrutement, gestion) : service outillé.
- Contre-preuve (obligatoire) : l'Autorité de la concurrence annonce une vigilance accrue et un éventuel contrôle ex post des rachats de cliniques (B9-p1) : le moteur de consolidation peut être freiné.
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non établie) | concentration ✔ (15 % des cliniques) | clients voir B9-p4
- Confiance : faible

### B9-p1 : Autorité de la concurrence, avis 25-A-12
- Acteur / marché : soins et médicaments vétérinaires
- Type : obligation / tendance (institutionnelle)
- Source : https://www.autoritedelaconcurrence.fr/en/article/autorite-de-la-concurrence-publishes-its-opinion-pricing-conditions-veterinary-medicines (date : 2025-10-24, page ouverte, version anglaise)
- Citation : « development of networks of "corporate" veterinary clinics »
- Chiffres : saisine du ministre le 2024-06-18 ; avis du 2025-10-13, publié le 2025-10-24 ; aucun chiffre de marché sur la page
- Ce que ça dit pour nous : le régulateur confirme la financiarisation et annonce une surveillance des rachats.

### B9-p2 : Asterès / SYNGEV, les groupes d'exercice vétérinaire
- Acteur / marché : groupes de cliniques vétérinaires
- Type : tendance (étude commandée par un syndicat)
- Source : extrait de recherche (non ouverte) : https://asteres.fr/site/wp-content/uploads/2023/04/ASTERES-SYNGEV-Les-groupes-dexercice-veterinaire.pdf (date : 2023-04, données 2022)
- Citation : paraphrase d'extrait, pas de citation littérale : environ 1 000 cliniques de groupes, 800 M€ de CA, 17 % du secteur ; enquête auprès de 329 vétérinaires
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : seule base de taille trouvée ; à recouper avec l'Ordre des vétérinaires.

### B9-p3 : amendement parlementaire sur la part des groupes
- Acteur / marché : cliniques vétérinaires
- Type : plainte (parlementaire)
- Source : extrait de recherche (non ouverte) : https://www.assemblee-nationale.fr/dyn/16/amendements/2600/AN/3653.pdf (date inconnue)
- Citation : paraphrase d'extrait, pas de citation littérale : en 2023 un vétérinaire sur cinq exerce dans un groupement ; les six premiers acteurs détiennent 15 % des cliniques
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : source politique, confiance faible : à traiter comme un ordre de grandeur.

---

## B5 : Automobilistes qui paient l'entretien-réparation, dans un tissu de garages indépendants face à des réseaux

### [Marché B5 : automobilistes (particuliers) paient entretien et réparation à un garage ; clients intermédiaires possibles : garages et carrosseries]
- Taille France : 31,2 Md€ HT en 2024 pour l'entretien et la réparation de véhicules (CCFA, édition 2025, d'après l'Insee ; valeur, France ; lu en extrait de recherche, B5-p1). Dont services auto en franchise : 6,02 Md€ (FFF 2025, B7-p1) = environ 19 % (calcul 6,02 ÷ 31,2).
- Croissance : +3,8 % en valeur en 2024 et +9,4 % en 2023 (CCFA, extrait, B5-p1) ; porté par l'inflation du panier moyen (environ +2 %, B5-p3). Volume en baisse : entrées en atelier −8,9 % en mécanique et −11,4 % en carrosserie sur les 4 premiers mois de 2025 (Mobilians-Solware, B5-p3). Services auto en franchise : 11 486 points de vente, +0,4 % (FFF, extrait de recherche).
- Moteur de croissance : parc vieillissant et réparations plus complexes (B5-p3) ; aucun moteur de volume.
- Acteurs : parts de marché de la rechange (Fiev-Feda, panel de 5 000 particuliers, extrait B5-p2) : mécaniciens réparateurs indépendants 33,1 %, réseaux constructeurs 31,6 %, centres auto 17,2 %, pneumaticiens 5,5 %. Parts des 3 premiers acteurs individuels non publiées [HYPOTHÈSE : < 10 %]. Réseaux en ouverture 2025 : Point S +30 centres (extrait de recherche L'Express Franchise), Mondial Pare-Brise et 123 Pare-Brise environ +20 chacun (B8-p2).
- Clients identifiables : B2C : le parc automobile (non sourcé ici). B2B : garages et carrosseries : voir B5-p5 (comptages API NAF 45.20A et 45.20B).
- Demande : non mesurée.
- Modèle d'exécution : service à forte main-d'œuvre pour réparer ; seul un service aux garages (logiciel, mise en conformité, achats) est compatible avec notre équipe.
- Contre-preuve (obligatoire) : les volumes baissent (entrées en atelier −8,9 %, CA des garages −7 % sur 4 mois 2025, B5-p3) et la croissance de 3,8 % est inférieure à 8 %.
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (3,8 % en valeur, volume en baisse) | concentration ✔ [HYPOTHÈSE] | clients ✔ (voir B5-p5)
- Confiance : moyenne pour la taille (fédération d'après l'Insee, extrait), faible pour la croissance

### B5-p1 : CCFA, CA de l'entretien-réparation
- Acteur / marché : entretien et réparation de véhicules en France
- Type : tendance (fédération, d'après Insee)
- Source : https://ccfa.fr/wp-content/uploads/2026/05/CCFA-2025-FR-67.pdf (date : 2026-05 ; PDF ouvert mais illisible, chiffres vus en extrait de recherche)
- Citation : paraphrase d'extrait, pas de citation littérale : 31,2 Md€ HT en 2024, +3,8 % ; 30 Md€ HT en 2023, +9,4 % (édition 2024 : https://ccfa.fr/wp-content/uploads/2024/10/CCFA-2024-FR-65.pdf)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : un marché de plus de 30 Md€, mais la croissance se ralentit (de 9,4 % à 3,8 %).

### B5-p2 : parts de marché des types de garages (Fiev-Feda)
- Acteur / marché : rechange automobile, garages indépendants vs réseaux
- Type : tendance
- Source : extrait de recherche (non ouverte, page auto-infos.fr en 403) : https://www.auto-infos.fr/article/les-garages-independants-restent-le-premier-choix-des-automobilistes-francais-en-2025.292514 (date : 2025-2026)
- Citation : paraphrase d'extrait, pas de citation littérale : indépendants 33,1 %, réseaux constructeurs 31,6 %, centres auto 17,2 %, pneumaticiens 5,5 % (panel de 5 000 particuliers)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : un tiers du marché reste chez les indépendants, donc dispersé.

### B5-p3 : baromètre Mobilians-Solware, 4 premiers mois de 2025
- Acteur / marché : garages et carrosseries (874 garages et 403 carrosseries)
- Type : contre-preuve
- Source : https://j2rauto.com/rechange/frequentation-des-garages-en-baisse-au-premier-trimestre-2025 (date : 2025-05-09, page ouverte)
- Citation : pas de citation littérale (tableau lu via résumé) ; entrées en atelier −8,9 % (mécanique), −11,4 % (carrosserie) ; CA garages 186,8 à 173,7 M€ (−7 %)
- Chiffres : panier moyen 401,1 € en mécanique (+2,1 %), 1 696,7 € en carrosserie (+2 %)
- Ce que ça dit pour nous : l'activité des ateliers recule en volume ; les garages ont besoin de leviers de rentabilité et de clients.

### B5-p4 : DGCCRF, contrôle de 1 600 garages
- Acteur / marché : réparateurs automobiles
- Type : obligation / plainte
- Source : https://journalauto.com/services/fraudes-dans-la-reparation-automobile-mobilians-lance-un-plan-daction-immediat/ (date : 2026-06-05, page ouverte)
- Citation : « Près de 40 % » (des 1 600 garages contrôlés en 2024 présentaient des anomalies)
- Chiffres : 1 600 garages contrôlés ; résultats publiés le 2026-06-04 ; Mobilians dit que la plupart sont des manquements d'affichage ou d'information liés à la complexité réglementaire
- Ce que ça dit pour nous : un besoin de mise en conformité administrative existe chez les garages (angle service aux garages), mais le syndicat répond par des webinaires gratuits.

---

## B1 : Bailleurs particuliers qui paient la gestion locative déléguée de leur logement

### [Marché B1 : propriétaires bailleurs (personnes physiques) paient 6 à 9 % TTC du loyer pour déléguer la gestion à une agence ou à un acteur en ligne]
- Taille France : bottom-up [HYPOTHÈSE] : environ 2 M de logements en gérance (FNAIM, document 2017, B1-p3, ancien) × 1 420 €/an (honoraires d'un T2 à 900 € de loyer chez un réseau traditionnel, B1-p2) = 2,84 Md€ ; avec le tarif digital de 950 €/an : 1,9 Md€. Parc concerné : 7,49 M de logements du secteur libre en 2020 (SDES, B1-p4). Valeur. Confiance faible (nombre de logements en gestion de 2017).
- Croissance : non établie. Seule donnée récente : Manda (ex-Flatlooker) a 8,0 M€ de CA en 2025 (B1-p1), sans année précédente dans l'API.
- Moteur de croissance : numérisation et baisse des honoraires (3,9 à 5,9 % TTC chez certains acteurs numériques contre 7 à 9 % en réseaux, B1-p2). Aucune obligation datée vérifiée dans ce run.
- Acteurs : Foncia, Citya, Orpi, Nexity, Laforêt ; numériques : Manda, Flatlooker, Hello Lou, Smartloc (B1-p2). Part des 3 premiers non publiée [HYPOTHÈSE : < 40 %]. Century 21 France SA (franchiseur) : CA 47,5 M€ en 2025, résultat net 6,8 M€ (B1-p5).
- Clients identifiables : environ 2,5 M de bailleurs personnes physiques (calcul : 5,3 M de logements ÷ 2,1 logements par bailleur, Localtis 2013, B1-p4, ancien). Entreprises NAF 68.31Z : 132 190 actives (somme sur 101 départements, B1-p6) ; ce chiffre inclut des agents commerciaux indépendants sans salarié [HYPOTHÈSE sur la composition].
- Demande : non mesurée.
- Modèle d'exécution : service outillé (gestionnaires, logiciel) ; employeur de quelques gestionnaires.
- Contre-preuve (obligatoire) : l'acteur numérique de référence, Manda, perd 1,95 M€ sur 8,0 M€ de CA en 2025 (B1-p1) et les prix numériques sont déjà 30 à 50 % sous ceux des réseaux (B1-p2).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non établie) | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : faible

### B1-p1 : Manda (ex-Flatlooker), comptes 2025
- Acteur / marché : gestion locative en ligne
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=flatlooker (date : 2026-10-13, requête exécutée)
- Citation : « "2025": {"ca": 8000196, "resultat_net": -1949412} »
- Chiffres : SIREN 822249595, NAF 68.31Z, tranche d'effectif 21 (20 à 49 salariés)
- Ce que ça dit pour nous : 8 M€ de CA mais en perte : l'acteur numérique n'a pas encore prouvé la rentabilité.

### B1-p2 : comparatif des honoraires de gestion locative
- Acteur / marché : réseaux (Foncia, Citya, Orpi, Nexity, Laforêt) et numériques (Manda, Flatlooker, Hello Lou, Smartloc)
- Type : argent dépensé (prix constatés)
- Source : https://www.cpim.fr/gestion-locative-deleguee-comparatif-2026/ (date : 2026-05-12, page ouverte ; bandeau contradictoire du 2026-07-02 ; site d'un acteur de l'immobilier, confiance moyenne)
- Citation : « Leurs honoraires oscillent généralement entre 7 et 9 % TTC »
- Chiffres : numériques 3,9 à 5,9 % TTC ; T2 à 900 € : 1 420 €/an en réseau historique, environ 950 € en numérique, environ 360 € en outil de gestion directe
- Ce que ça dit pour nous : les bailleurs paient 950 à 1 420 € par an et par logement ; la gestion en autonomie coûte environ 360 €.

### B1-p3 : FNAIM, nombre de logements en gérance
- Acteur / marché : administrateurs de biens
- Type : tendance
- Source : extrait de recherche (non ouverte) : https://www.galivel.com/media/files/fnaim_propositions_politiques_2017.pdf (date : 2017)
- Citation : paraphrase d'extrait, pas de citation littérale : environ 2 M de biens en gérance locative, sur un parc locatif privé de 6,5 M de logements
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : donnée ancienne (2017) ; c'est la seule disponible sur la part déléguée, à actualiser.

### B1-p4 : SDES et Localtis, parc locatif privé
- Acteur / marché : parc locatif privé et bailleurs
- Type : tendance (institutionnelle pour SDES)
- Source : https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 (extrait de recherche, date : rapport publié 2025-11) et https://www.banquedesterritoires.fr/bailleurs-prives-qui-etes-vous (page ouverte, date : 2013-01-07)
- Citation : « 2,1 logements locatifs » (par bailleur privé, Localtis 2013)
- Chiffres : secteur libre 7 488 milliers de logements en 2020 (SDES, extrait) ; locataires du privé 25 % des ménages en 2024 (SDES, extrait) ; bailleurs privés 53 % du parc locatif de 10 M de logements en 2013
- Ce que ça dit pour nous : une base institutionnelle existe, mais les chiffres sur la gestion déléguée sont anciens.

### B1-p5 : Century 21 France, comptes 2025
- Acteur / marché : franchiseur immobilier
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=century%2021%20france (date : 2026-10-13, requête exécutée)
- Citation : « "2025": {"ca": 47474891, "resultat_net": 6796444} »
- Chiffres : SIREN 339510695, NAF 70.22Z, tranche d'effectif 22
- Ce que ça dit pour nous : un franchiseur dégage environ 14 % de marge nette sur 47 M€ (calcul) ; le modèle réseau est rentable.

### B1-p6 : comptage Sirene des agences immobilières
- Acteur / marché : NAF 68.31Z (agences immobilières)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=68.31Z&etat_administratif=A&per_page=1&departement=XX (somme sur 101 départements, date : 2026-10-13, requêtes exécutées)
- Citation : « 68.31Z total=132190 fails=0 »
- Chiffres : 132 190 entreprises actives ; tranche d'effectif non filtrée
- Ce que ça dit pour nous : très fragmenté, avec beaucoup de micro-structures (mandataires) ; il faudra filtrer par effectif en phase 1.

---

## B2 : Cabinets de santé libéraux qui paient un secrétariat et un accueil téléphonique externalisés

### [Marché B2 : médecins, dentistes, kinés et autres libéraux de santé paient un télésecrétariat (appels, rendez-vous) à un prestataire]
- Taille France : pas de taille publiée. Calcul bottom-up [HYPOTHÈSE] : 100 000 cabinets cibles (les comptages Sirene donnent au moins 86 372 entreprises actives en NAF 86.21Z et au moins 108 176 en NAF 86.90E, B2-p3 : ce sont des entreprises, pas des cabinets avec secrétariat) × 149 €/mois TTC (tarif Webdentiste, non sourcé par URL) × 12 = 179 M€/an à 100 % de pénétration ; à 10 % : 18 M€. Prix plus bas : 99 €/mois (assistant IA Doctolib, B2-p1) donne 119 M€ à 100 % ; plus haut : 674 $/mois (annonce freelance, B2-p2). Valeur. Confiance faible.
- Croissance : non établie (aucune série trouvée). Pas de chiffre de croissance du télésecrétariat.
- Moteur de croissance : surcharge administrative des libéraux et raréfaction de l'exercice libéral (DREES, ancien, extrait de recherche) [HYPOTHÈSE de lien] ; arrivée d'assistants IA (Doctolib, DentalCall AI) en 2025 (B2-p1).
- Acteurs : Doctolib domine l'agenda ; télésecrétariats nombreux et petits (Medifil et d'autres cités en extrait) ; part des 3 premiers non publiée [HYPOTHÈSE : < 40 % pour le télésecrétariat]. DentalCall AI/Webdentiste : « plusieurs centaines de cabinets » abonnés (B2-p1).
- Clients identifiables : au moins 86 372 entreprises NAF 86.21Z et 108 176 NAF 86.90E (bornes basses, régions plafonnées) ; au moins 10 000 en 86.23Z (plafond national, dentistes) ; DREES : 47 600 chirurgiens-dentistes au 1er janvier 2025, tous modes d'exercice (B2-p4).
- Demande : non mesurée.
- Modèle d'exécution : service outillé (IA + télésecrétaires indépendantes) ; risque de main-d'œuvre si le volume d'appels est traité par des salariés.
- Contre-preuve (obligatoire) : Doctolib a lancé en octobre 2025 un assistant téléphonique IA à 99 €/mois TTC (49 € pour ostéopathes et podologues) qui traite prise de rendez-vous et renouvellements (B2-p1) : le leader de l'agenda entre sur le même budget à un prix inférieur à l'offre humaine.
- Seuils CLAUDE.md : taille ✔ (potentiel 119 à 179 M€ sous hypothèses) | croissance ✘ (non établie) | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : faible

### B2-p1 : Doctolib lance un assistant téléphonique IA à 99 €/mois
- Acteur / marché : Doctolib (assistant IA), DentalCall AI/Webdentiste, télésecrétaires
- Type : argent dépensé (prix publics) et contre-preuve
- Source : https://en-contact.com/in-france-doctolib-launches-its-ai-telephone-assistant-priced-at-euro99-per-month-including-vat (date : 2025-10-07, page ouverte, version anglaise)
- Citation : « €99 per month (including VAT) » (pour les médecins)
- Chiffres : 49 €/mois TTC pour ostéopathes et podologues ; service en bêta, prix « not set in stone » ; l'assistant ne remplace pas totalement les télésecrétaires ; DentalCall AI : plusieurs centaines de cabinets dentaires abonnés
- Ce que ça dit pour nous : un budget de 99 à 149 €/mois par cabinet est déjà accepté ; le substitut IA du leader tire les prix vers le bas.

### B2-p2 : annonces de télésecrétariat médical sur ComeUp
- Acteur / marché : freelances de télésecrétariat médical
- Type : argent dépensé (prix affichés)
- Source : extrait de recherche (non ouverte) : https://comeup.com/fr/service/524322/ameliorer-votre-relation-patient-avec-un-service-de-secretariat-medical-a-distance (date inconnue)
- Citation : paraphrase d'extrait, pas de citation littérale : Pack Essentiel 674,37 $/mois (1 praticien, 100 actions RDV), Pack Confort 1 131,56 $, Pack Sérénité 1 817,36 $
- Chiffres : prix affichés en dollars, versions de la même annonce légèrement différentes
- Ce que ça dit pour nous : des freelances vendent 650 à 1 800 $/mois, soit 4 à 12 fois le prix de l'assistant IA ; à confirmer par le nombre d'avis (non relevé).

### B2-p3 : comptages Sirene des professions de santé libérales
- Acteur / marché : NAF 86.21Z (généralistes), 86.90E (rééducation, kinés, podologues), 86.23Z (dentistes), 86.22C (spécialistes), 86.90D (infirmiers)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=86.90E&etat_administratif=A&per_page=1&region=XX (requêtes par région, date : 2026-10-13, requêtes exécutées)
- Citation : « 86.90E total=108176 capped_regions=[ 11 44 75 76 84 93] »
- Chiffres : 86.90E : 108 176 (6 régions plafonnées à 10 000, donc borne basse) ; 86.21Z : 86 372 (2 régions plafonnées, borne basse) ; 86.23Z, 86.22C, 86.90D : au moins 10 000 chacun (plafond national)
- Ce que ça dit pour nous : le nombre d'entreprises dépasse largement 3 000 mais compte des entités sans secrétariat ; l'effectif et la structure (cabinet de groupe) sont à filtrer en phase 1.

### B2-p4 : DREES, démographie de professions de santé au 1er janvier 2025
- Acteur / marché : chirurgiens-dentistes, pharmaciens, sages-femmes, pédicures-podologues
- Type : tendance (institutionnelle)
- Source : extrait de recherche (non ouverte) : https://drees.solidarites-sante.gouv.fr/jeux-de-donnees/DATA_250728-demographie-pharmaciens-chirurgiens-dentistes-sages-femmes (date : 2025-07)
- Citation : paraphrase d'extrait, pas de citation littérale : 47 600 chirurgiens-dentistes, 74 600 pharmaciens, 14 400 pédicures-podologues au 1er janvier 2025 (tous modes d'exercice)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : source officielle utile pour borner les cibles ; pas de chiffre libéral par profession dans ce run.

---

## B4 : Entreprises et particuliers qui paient des organismes de formation, secteur atomisé

### [Marché B4 : entreprises, particuliers et financeurs paient des formations à 79 000 organismes ; clients intermédiaires possibles : les organismes de formation]
- Taille France : environ 19 Md€ de CA en 2021 pour les organismes de formation (enquête ETOF Céreq/Dares, relayée par une page du 2024-11-07, B4-p1) ; valeur ; périmètre France, tous organismes déclarés. Confiance moyenne (source institutionnelle, relais secondaire, millésime 2021).
- Croissance : +13 % de CA entre 2019 et 2021, soit environ 6,3 %/an (calcul, valeur, B4-p1) ; nombre d'organismes +12 % sur la même période (79 012 en 2021). Franchise de formation : CA +18,6 % et points de vente +12,9 % en 2025 (FFF, B7-p1). Pas de série 2022-2025 de CA total.
- Moteur de croissance : financement public de la formation et certification Qualiopi exigée pour les fonds publics [HYPOTHÈSE : date et périmètre à vérifier sur une source officielle, non ouverte dans ce run].
- Acteurs : micro-organismes = 56 % des structures mais 8 % du CA ; organismes privés lucratifs = 86 % des structures et 57 % du CA ; publics et parapublics = 1 % des structures et 22 % du CA ; non lucratifs privés 21 % du CA (B4-p1). Part des 3 premiers non publiée [HYPOTHÈSE : < 10 %].
- Clients identifiables : 79 012 structures actives (2021, B4-p1) ; NAF 85.59A : au moins 10 000 entreprises actives (plafond API, B4-p3). Environ 50 000 organismes certifiés Qualiopi en 2023 (extrait, confiance faible, B4-p2).
- Demande : non mesurée.
- Modèle d'exécution : logiciel ou service outillé si la cible est l'organisme de formation ; service à forte main-d'œuvre si on forme soi-même.
- Contre-preuve (obligatoire) : 56 % des organismes ne font que 8 % du CA : en moyenne environ 34 000 € de CA par micro-organisme (calcul : 8 % × 19 Md€ ÷ (56 % × 79 012) ≈ 1,52 Md€ ÷ 44 247) : leur capacité à payer un service est faible. La période mesurée (2019-2021) est courte [HYPOTHÈSE : elle inclut un pic de financement à vérifier].
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (6,3 %/an < 8 % ; franchise +18,6 % mais sous-segment) | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : moyenne

### B4-p1 : Céreq/Dares, enquête ETOF sur les organismes de formation
- Acteur / marché : organismes de formation professionnelle
- Type : tendance (institutionnelle, relayée)
- Source : https://www.marche-public.fr/contrats-publics/Formation-professionnelle-etude-cereq-dares-2024.htm (date : 2024-11-07, page ouverte ; relais de l'étude Céreq/Dares)
- Citation : « atteignant 79 012 structures actives »
- Chiffres : +12 % de structures et +13 % de CA entre 2019 et 2021 ; CA d'environ 19 Md€ ; micro-organismes 56 % des structures, 8 % du CA ; lucratifs 86 % des effectifs et 57 % du CA ; publics 22 % du CA
- Ce que ça dit pour nous : un marché de 19 Md€ très atomisé ; la valeur est portée par une minorité d'organismes structurés.

### B4-p2 : nombre d'organismes sur Mon Compte Formation et certifiés Qualiopi
- Acteur / marché : organismes de formation (CPF, Qualiopi)
- Type : tendance (confiance faible)
- Source : extrait de recherche (non ouverte) : https://propulsebyca.fr/idees-business/formation-professionnelle/marche-formation-professionnelle (date : 2023-2024)
- Citation : paraphrase d'extrait, pas de citation littérale : 13 395 organismes actifs sur Mon Compte Formation en 2023 ; environ 50 000 certifiés Qualiopi ; financement 14,9 Md€ en 2023
- Chiffres : voir ci-dessus ; site de conseil sans méthode
- Ce que ça dit pour nous : ordre de grandeur de la cible Qualiopi (environ 50 000), à confirmer par la liste officielle.

### B4-p3 : comptage Sirene des organismes de formation d'adultes
- Acteur / marché : NAF 85.59A (formation continue d'adultes)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=85.59A&etat_administratif=A&per_page=1 (date : 2026-10-13, requête exécutée)
- Citation : « "total_results":10000 »
- Chiffres : au moins 10 000 entreprises actives (plafond de l'API atteint)
- Ce que ça dit pour nous : l'effectif réel dépasse 10 000 ; le découpage par département est à faire en phase 1.

---

## Comptages Sirene complémentaires (preuves rattachées à B3, B5, B9)

### B3-p5 : comptage Sirene des auto-écoles
- Acteur / marché : NAF 85.53Z (enseignement de la conduite)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=85.53Z&etat_administratif=A&per_page=1 (date : 2026-10-13, requête exécutée)
- Citation : « "total_results":10000 »
- Chiffres : au moins 10 000 entreprises actives (plafond de l'API), cohérent avec 11 657 entreprises (Insee 2022, B3-p4)
- Ce que ça dit pour nous : plus de 10 000 auto-écoles à joindre ; la cible B2B existe.

### B5-p5 : comptage Sirene des garages et carrosseries
- Acteur / marché : NAF 45.20A (entretien-réparation de véhicules légers) et 45.20B (autres véhicules)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=45.20A&etat_administratif=A&per_page=1 (date : 2026-10-13, requête exécutée)
- Citation : « "total_results":10000 »
- Chiffres : 45.20A : au moins 10 000 (plafond) ; 45.20B : 3 296
- Ce que ça dit pour nous : plus de 13 000 ateliers cibles ; le 45.20A est sans doute largement au-dessus de 10 000 (non découpé).

### B9-p4 : comptage Sirene des activités vétérinaires
- Acteur / marché : NAF 75.00Z (activités vétérinaires)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=75.00Z&etat_administratif=A&per_page=1 (date : 2026-10-13, requête exécutée)
- Citation : « "total_results":10000 »
- Chiffres : au moins 10 000 entreprises actives (plafond) ; Île-de-France 1 584, Auvergne-Rhône-Alpes 1 843 (requêtes par région)
- Ce que ça dit pour nous : plus de 10 000 entreprises vétérinaires (cliniques, cabinets, sociétés d'exercice) ; la cible B2B dépasse 3 000.

---

## Sources non lues

- https://www.franchise-fff.com/wp-content/uploads/2026/03/FFF-CP-indicateursFranchise2025-mars2026-V2.pdf : PDF compressé illisible (chiffres FFF vus en extrait de recherche et via Républik).
- https://www.artisanat.fr/system/files/medias/file/2026/01/20260109_LB_Transmission_reprise_VF.pdf : PDF compressé illisible (étude Bpifrance Le Lab ; chiffres pris sur bpifrance-creation.fr).
- https://ccfa.fr/wp-content/uploads/2026/05/CCFA-2025-FR-67.pdf : PDF compressé illisible (chiffre 31,2 Md€ vu en extrait de recherche).
- https://www.auto-infos.fr/article/les-garages-independants-restent-le-premier-choix-des-automobilistes-francais-en-2025.292514 : 403.
- https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 : hôte introuvable en WebFetch (lu en extrait de recherche).
- cessionpme.com, statista.com, reddit.com, pappers.fr, malt.fr : bloqués connus, non tentés.
- Non trouvés dans ce budget : nombre de logements en gérance récent (B1), honoraires français de cession (B6), CA total 2022-2025 de la formation (B4), Insee vieillissement (B7), Ordre des vétérinaires (B9), séries pluriannuelles du permis (B3), Google Trends (tous).

## Bilan

- Marchés : 9 (B1 à B9). Preuves numérotées : 39. Recherches web utilisées : 19 sur 25 (le reste en WebFetch et API). Comptages Sirene par département et par région partiels à cause du limiteur de débit de l'API (429).
- Domaines distincts : environ 28 (api recherche-entreprises, bpifrance-creation, fusacq, hayot-expertise et hectelion, lautomobiliste, maddyness, envoituresimone, propulsebyca et xerfi, observatoiredelafranchise, lexpress-franchise, presse-citron, republikgroup, toute-la-franchise, drees, una, autoritedelaconcurrence, asteres, assemblee-nationale, ccfa, auto-infos, j2rauto, journalauto, cpim, galivel, statistiques.developpement-durable, banquedesterritoires, en-contact, comeup, marche-public).
- Plus gros domaine : recherche-entreprises.api.gouv.fr avec 9 preuves sur 39 (23 %), sous le plafond de 40 %.
- Fraîcheur : beaucoup d'extraits de recherche sans citation littérale (marqués « paraphrase d'extrait ») : à rouvrir par le vérificateur avant usage.

