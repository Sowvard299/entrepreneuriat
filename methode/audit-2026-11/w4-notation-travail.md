# W4 : sources fiables pour mieux calibrer la notation (fichier de travail)

- Mission : trouver recherche académique, statistique publique et praticiens pour (1) taux de base de survie par secteur, (2) prévision par classe de référence et prévision calibrée, (3) échelles de force des preuves et grilles d'opportunité, (4) imitateurs et seconds entrants, (5) causes d'échec des start-up. Pour chaque point : la règle à tirer pour la grille.
- Date : 2026-11-03
- Recherches web utilisées : 15 / 15 (budget atteint : Insee pérennité ; Banque de France défaillances ; Mellers et Tetlock ; Golder et Tellis ; Strategyzer ; Timmons ; Y Combinator ; Shenkar ; transposition de modèles ; causes d'échec et critiques ; Cooper et al. ; Cantamessa ; méta-analyses du pionnier ; Dawes ; attribution des échecs). Les pages ouvertes en WebFetch ou téléchargées en PDF ne comptent pas dans ce budget.
- Preuves : 25 (W4-1 à W4-25) ; domaines distincts : 19 ; plus gros domaine : insee.fr 4 preuves sur 25 (16 %), ideas.repec.org 3 sur 25 (12 %), hbr.org 2 sur 25 (8 %).
- Lecture : « ouverte » = page ouverte avec WebFetch (résumé automatique) ; quand la mention « vérifié dans le HTML » est écrite, la page a aussi été téléchargée et les chiffres et citations relus dans le texte brut ; « ouverte (PDF texte) » = PDF téléchargé et lu en texte intégral avec pdftotext ; « extrait » = vu seulement dans un résultat de recherche. Sans l'une de ces mentions, les chiffres viennent du résumé automatique et sont à faire revérifier.
- Statut : partiel (budget de recherche atteint ; liste de ce qui manque à la fin de ce fichier et dans w4-notation-synthese.md)

## Lot 1 : point 1, taux de base France (Insee, Banque de France)

### W4-1 : Insee, pérennité à 5 ans par secteur, générations 2010, 2014, 2018
- Acteur / marché : statistique publique, entreprises créées au 1er semestre, activités marchandes non agricoles, hors micro-entrepreneurs, France
- Type : statistique publique (taux de base)
- Source : https://www.insee.fr/fr/statistiques/2015357 (date : 2025-09-29 ; ouverte). Enquête Sine, quadriennale.
- Citation : « Pérennité à cinq ans des entreprises créées, hors micro-entrepreneurs, selon l'activité » (titre du tableau)
- Chiffres (génération 2018 / 2014 / 2010, en %) : Commerce-réparation auto 63,9 / 54,4 / 52,4 ; Activités spécialisées, scientifiques, techniques 73,8 / 68,5 / 70,4 ; Construction 68,5 / 59,3 / 54,7 ; Enseignement, santé, action sociale 74,1 / 74,3 / 74,8 ; Hébergement-restauration 64,0 / 58,8 / 57,5 ; Services administratifs et de soutien 65,6 / 59,4 / 61,2 ; Information et communication 65,7 / 59,6 / 64,6 ; Transports-entreposage 69,2 / 67,5 / 68,5 ; Autres services 69,5 / 60,2 / 61,3 ; Industrie 73,4 / 64,2 / 67,6 ; Immobilier 69,8 / 56,2 / 56,8 ; Finance-assurance 77,3 / 67,0 / 70,7 ; Ensemble 69,0 / 61,3 / 60,4.
- Fourchette min-max des 3 générations (calcul à partir du tableau) : Commerce 52,4 à 63,9 ; Construction 54,7 à 68,5 ; Hébergement-restauration 57,5 à 64,0 ; Immobilier 56,2 à 69,8 ; Information-communication 59,6 à 65,7 ; Services administratifs 59,4 à 65,6 ; Autres services 60,2 à 69,5 ; Industrie 64,2 à 73,4 ; Transports 67,5 à 69,2 ; Finance-assurance 67,0 à 77,3 ; Spécialisées-scientifiques 68,5 à 73,8 ; Enseignement-santé 74,1 à 74,8 ; Ensemble 60,4 à 69,0.
- Ce que ça établit : à 5 ans, 23 % à 36 % des entreprises créées (hors micro-entrepreneurs) ne sont plus actives selon le secteur (génération 2018). Le taux d'un même secteur bouge de 1 à 14 points entre ses valeurs extrêmes sur les 3 générations (commerce 52,4 à 63,9 ; construction 54,7 à 68,5 ; immobilier 56,2 à 69,8), donc un taux de base se donne en fourchette, pas en point. Limite : « plus active » n'est pas « défaillante » ; l'Insee ne sépare pas ici cessions, fermetures volontaires et procédures collectives [non établi].
- Règle pour la grille : partir du taux de pérennité du secteur (fourchette sur 3 générations) comme probabilité a priori de survie à 5 ans, puis ajuster avec des éléments précis et sourcés.

### W4-2 : Insee Première n° 2070, entreprises créées en 2018 encore actives 5 ans après
- Acteur / marché : Insee, Sine 2018, hors micro-entrepreneurs
- Type : statistique publique
- Source : https://www.insee.fr/fr/statistiques/8634190 (date : 2025-09-03 ; ouverte)
- Citation : « Entreprises créées en 2018 : 69 % sont encore actives cinq ans après leur création » (titre)
- Chiffres : 69,0 % à 5 ans (1er semestre 2018, environ 120 000 entreprises dans le champ). Courbe de survie, ensemble : 1 an 94,6 ; 2 ans 88,0 ; 3 ans 81,3 ; 4 ans 74,1 ; 5 ans 69,0. Sociétés : 96,6 ; 90,5 ; 83,4 ; 75,8 ; 70,6. Entreprises individuelles hors micro : 87,2 ; 78,6 ; 73,8 ; 68,0 ; 63,3. Une note de l'Insee précise que les données à 1, 2 et 3 ans sont révisées par rapport aux précédentes, ce qui explique les 82,0 % à 3 ans de l'Insee Première 1962 (W4-3). Par secteur et forme juridique (entreprise individuelle / société) : Enseignement-santé 73,4 / 76,3 ; Transports 69,2 / 69,3 ; Spécialisées-scientifiques 66,9 / 75,8 ; Finance 60,1 / 80,2 ; Construction 55,2 / 70,3 ; Immobilier 47,9 / 73,3 ; Hébergement-restauration 47,9 / 66,0 ; Commerce 44,7 / 66,6 ; Industrie 43,5 / 77,1 ; Information-communication 33,9 / 67,3. Parmi les entreprises ayant dépassé 3 ans, 90 % sont encore actives 2 ans plus tard. Facteurs associés à une meilleure survie (régression, toutes choses égales par ailleurs) : société plutôt qu'entreprise individuelle, ressources financières initiales plus élevées, salariés à la création, expérience professionnelle. Composition, texte de l'Insee (chiffres vérifiés dans le HTML) : « Le changement de composition du champ de l'enquête explique une partie de cette hausse élevée » : l'élargissement du régime du micro-entrepreneur en janvier 2018 a retiré du champ des entreprises individuelles classiques ; la part des sociétés passe de 61 % (2014) à 79 % (2018) ; corrigée de cet effet, la hausse est de 5 points (3 points pour les sociétés, 2 pour les entreprises individuelles) au lieu de 8. Covid : parmi les entreprises encore actives en novembre 2021, 90 % le sont encore 2 ans plus tard, 88 % après un arrêt complet d'activité, 93 % avec une hausse d'activité ; la pérennité des sociétés d'hébergement-restauration est inférieure de 2,5 points à celle attendue sans la crise ; le chômage partiel « semble avoir amélioré la pérennité » (94 % contre 89 %, parmi les entreprises employeuses dont l'activité a baissé pendant la crise et encore actives fin 2021).
- Ce que ça établit : le taux de base dépend du secteur ET de la forme juridique ; sur la hausse de 8 points entre 2014 et 2018, 3 points viennent d'un effet de structure (choix du champ) et non d'une amélioration ; la génération 2018 a traversé la Covid avec des aides publiques (effet sur la survie non chiffré globalement).
- Règle pour la grille : écrire pour chaque piste le taux de base du secteur, de la forme juridique visée, et signaler que la génération 2018 est probablement un haut de fourchette.

### W4-3 : Insee Première n° 1962, survie à 3 ans par secteur et forme juridique, génération 2018
- Acteur / marché : Insee, Sine 2018, hors micro-entrepreneurs
- Type : statistique publique
- Source : https://www.insee.fr/fr/statistiques/7653231 (date : 2023-07-24 ; ouverte)
- Citation : « Entreprises créées en 2018 : huit sur dix sont encore actives trois ans après leur création » (titre)
- Chiffres : 82,0 % à 3 ans toutes entreprises (+7 points par rapport à 2014 ; le texte précise que sur les 6,8 points de hausse, 3,3 sont dus à un effet de structure lié au poids plus important des sociétés, vérifié dans le HTML). Sociétés 83,9 %, entreprises individuelles 75,2 %. Sociétés par secteur, génération 2018 : Finance 90,4 ; Industrie 88,7 ; Immobilier 87,4 ; Enseignement-santé 87,2 ; Spécialisées-scientifiques 85,9 ; Autres services 85,0 ; Construction 84,7 ; Information-communication 83,5 ; Transports 82,6 ; Services administratifs 81,6 ; Hébergement-restauration 80,9 ; Commerce 80,5. Entreprises individuelles : de 49,6 (information-communication) à 82,9 (enseignement-santé).
- Ce que ça établit : à 3 ans, 10 à 20 % des sociétés ne sont plus actives selon le secteur (survie de 80,5 à 90,4 %). L'écart entre secteurs est d'environ 10 points pour les sociétés (90,4 moins 80,5) mais d'environ 33 points pour les entreprises individuelles (82,9 moins 49,6) : la forme juridique change le taux de base autant que le secteur.
- Règle pour la grille : la porte de confirmation à 3 ans doit se comparer à ce taux sectoriel, pas à zéro.

### W4-4 : Insee Première n° 2069, micro-entrepreneurs immatriculés en 2018
- Acteur / marché : Insee, micro-entrepreneurs, France
- Type : statistique publique
- Source : https://www.insee.fr/fr/statistiques/8634000 (date : 2025-09-03 ; ouverte)
- Citation : « Micro‑entrepreneurs immatriculés en 2018 : moins de trois sur dix encore actifs cinq ans après » (titre)
- Chiffres : 28 % encore actifs à 5 ans (immatriculés au 1er trimestre 2018) ; 39 % parmi ceux qui ont réellement démarré ; 54,0 % de ceux qui ont démarré encore actifs à 3 ans. Par secteur, part encore active à 5 ans : santé humaine 50 ; industrie 43 ; autres services aux ménages 41 ; construction 36 ; enseignement 36 ; services administratifs 33 ; information-communication 27 ; hébergement-restauration 24 ; spécialisées-scientifiques 23 ; commerce 22 ; finance 22 ; conseil de gestion 17 ; transports 8 ; livraison 6. Activité terminée = aucun chiffre d'affaires positif pendant 8 trimestres de suite. Chiffre d'affaires 2023 des micro-entrepreneurs immatriculés au 1er semestre 2018 et encore actifs fin 2023 : moyenne 20 000 €, médiane 12 000 €, la moitié entre 3 000 € et 28 000 € ; moyenne la plus haute en hébergement-restauration (29 000 €), la plus basse en transports (11 000 €). L'expérience et l'investissement initial favorisent la pérennité ; pour le soutien reçu (+6 points), l'Insee écrit que « le lien de cause à effet n'est pas établi » (lecture du HTML, chiffres vérifiés).
- Ce que ça établit : le taux de base d'un projet monté en micro-entreprise est environ 2,5 fois plus bas que celui des autres entreprises (28 % contre 69 % ; 69 / 28 = 2,5), mais la population (immatriculés au 1er trimestre, y compris ceux qui n'ont jamais démarré) et la définition de « fin » (chiffre d'affaires nul pendant 8 trimestres, pas radiation) ne sont pas les mêmes.
- Règle pour la grille : ne jamais mélanger les deux taux de base ; préciser si la piste vise un statut micro ou une société.

### W4-5 : Banque de France, défaillances d'entreprises par secteur, août 2026
- Acteur / marché : Banque de France, base FIBEN, unités légales, France
- Type : statistique publique (flux de procédures)
- Source : https://www.banque-france.fr/fr/statistiques/entreprises/defaillances-dentreprises-2026-08 (date : 2026-10-09, mis à jour 2026-10-12 ; ouverte)
- Citation : « Le niveau des défaillances, toujours élevé, s'explique notamment par la conjoncture dégradée »
- Chiffres (chiffres vérifiés dans le HTML de la page ; cumul 12 mois à fin août 2026, nombre de défaillances ; évolution sur un an ; écart à la moyenne 2010-2019) : Total 70 766 (+4,8 % ; +19,3 %), contre 70 692 en juillet. Agriculture 1 795 (+13,3 % ; +32,1 %). Industrie 4 442 (+3,4 % ; 0,0 %). Construction 14 354 (−2,4 % ; −2,2 %). Commerce et réparation auto 14 076 (+2,8 % ; +7,7 %). Transports-entreposage 3 223 (+2,8 % ; +69,5 %). Hébergement-restauration 9 796 (+8,5 % ; +32,8 %). Information-communication 2 139 (+3,4 % ; +44,5 %). Finance-assurance 1 769 (+10,2 % ; +53,8 %). Immobilier 2 673 (+6,3 % ; +34,7 %). Conseils et services aux entreprises 9 040 (+8,4 % ; +41,7 %). Enseignement, santé, action sociale, services aux ménages 7 280 (+13,1 % ; +37,1 %). Par taille (tableau B, même période) : microentreprises et taille indéterminée 65 107, très petites 3 498, petites 1 578, moyennes 524, ETI et grandes 59. Plus de 1,2 million de créations sur les 12 mois (+11,4 %, Insee).
- Ce que ça établit : la Banque de France publie des NOMBRES de défaillances par secteur et par taille, sans stock d'entreprises ni taux ; l'unité est l'unité légale. La définition précise des procédures comptées n'a pas été obtenue (absente de la page et du PDF). Le contexte est dégradé : +19,3 % au-dessus de la moyenne 2010-2019, +69,5 % pour les transports, +53,8 % pour la finance-assurance, +44,5 % pour l'information-communication. Environ 92 % des défaillances (65 107 sur 70 766, calcul) touchent des microentreprises ou des unités de taille indéterminée.
- Règle pour la grille : utiliser la pérennité Insee (taux) pour le taux de base, et les défaillances Banque de France seulement comme signal de conjoncture sectorielle (écart à la moyenne 2010-2019). Un taux de défaillance par secteur n'est pas établi ici.

## Lot 2 : point 2, classe de référence et prévision calibrée

### W4-6 : Flyvbjerg 2006, les trois étapes de la prévision par classe de référence
- Acteur / marché : recherche académique (Project Management Journal 37(3), 2006), version arXiv 2013
- Type : recherche académique
- Source : https://arxiv.org/pdf/1302.3642 (date : 2006 revue / 2013-02-14 arXiv ; ouverte (PDF texte)) ; résumé : https://arxiv.org/abs/1302.3642 (ouverte)
- Citation : « Identification of a relevant reference class of past, similar projects. »
- Chiffres / contenu : trois étapes : (1) identifier une classe de référence « broad enough to be statistically meaningful but narrow enough to be truly comparable » ; (2) établir une distribution de probabilité pour la classe, avec des données empiriques crédibles sur un nombre suffisant de cas ; (3) comparer le projet à cette distribution pour établir le résultat le plus probable. La méthode consiste à « regressing forecasters' best guess toward the average of the reference class » et à élargir l'intervalle de crédibilité vers celui de la classe. Exemple cité (Lovallo et Kahneman 2003) : des étudiants s'attendent à faire mieux que 84 % de leurs pairs ; après un rappel des données de référence, leur estimation baisse de 20 %. L'auteur écrit que la classe de référence est plus difficile à choisir quand les précédents sont rares ; l'avantage de la vue extérieure est le plus fort pour les projets « non routiniers ».
- Ce que ça établit : une estimation par classe de référence part de la distribution des résultats d'un groupe comparable, puis déplace peu. C'est la méthode pour passer d'une note subjective à une probabilité ancrée.
- Règle pour la grille : définir la classe de référence AVANT de noter (secteur Insee × forme juridique × taille), écrire sa distribution, puis situer la piste ; toute probabilité au-dessus du taux de base doit être justifiée par des éléments sourcés.

### W4-7 : Wikipedia, classe de référence (source secondaire)
- Acteur / marché : encyclopédie collaborative, résumé de la méthode
- Type : tendance (source secondaire)
- Source : https://en.wikipedia.org/wiki/Reference_class_forecasting (date inconnue ; ouverte)
- Citation : « The theories behind reference class forecasting were developed by Daniel Kahneman and Amos Tversky. »
- Chiffres (vérifiés dans le HTML de la page) : tramway d'Édimbourg, ligne 2 : prévision initiale 320 millions de livres ; la prévision par classe de référence donnait 357 millions au 50e centile et 400 millions au 80e centile ; ouverture avec 3 ans de retard en mai 2014, coût final 776 millions de livres (628 millions en prix 2004). La revue citée par la page estime que les prévisions par classe de référence étaient probablement trop basses, parce que les majorations avaient été appliquées trop tôt dans le projet. La page signale l'usage de la méthode au Royaume-Uni (guide 2004 du ministère des transports).
- Ce que ça établit : confirme les trois étapes et le principe vue intérieure contre vue extérieure ; sur ce cas, la prévision par classe de référence était plus proche du résultat que la prévision interne (320) mais restait en dessous (776 contre 400 au 80e centile).
- Règle pour la grille : confiance moyenne seulement (source secondaire) ; l'appui principal est W4-6.

### W4-8 : Mellers, Tetlock et al. 2014, formation, travail en équipe et suivi améliorent la précision
- Acteur / marché : recherche académique (Psychological Science 25(5)), tournoi de prévision géopolitique sur 2 ans
- Type : recherche académique
- Source : https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf (date : 2014 ; ouverte (PDF texte)) ; page : https://escholarship.org/uc/item/4rg4n9vr (non lisible en WebFetch)
- Citation : « Remarkably, a brief probabilistic training module paid off over an extended time »
- Chiffres / contenu : la formation aux probabilités conduit à considérer des classes de référence, à moyenner plusieurs estimations et à éviter « overconfidence, the confirmation bias, and base-rate neglect ». Le score de Brier va de 0 (meilleur) à 2 (pire), c'est une règle propre : les prévisionnistes sont incités à donner leur vraie probabilité. Exemple du texte : prévoir 90 % pour un événement qui a lieu donne 0,02, et 1,62 s'il n'a pas lieu. La calibration s'est améliorée avec la formation (années 1 et 2) ; les 2 % meilleurs de l'année 1, réunis en équipes, ont dépassé tous les autres groupes « by a wide margin » sans retour à la moyenne en année 2. Questions : 85 et 114 questions closes par année ; durée moyenne ouverte 102 jours.
- Ce que ça établit : la capacité à donner des probabilités calibrées s'apprend, se mesure (Brier, courbes de calibration) et s'améliore par la formation, la discussion en groupe et le suivi des résultats.
- Règle pour la grille : noter en probabilités, consigner les prévisions datées (ex. « cette piste passe la porte 2 : 30 % »), et calculer le score de Brier après résolution, pour apprendre si nos probabilités sont calibrées.

### W4-9 : Association for Psychological Science, résumé du tournoi Good Judgment
- Acteur / marché : APS, article de vulgarisation sur Mellers et al.
- Type : recherche académique (vulgarisation)
- Source : https://www.psychologicalscience.org/news/minds-business/superforecasters-the-art-of-accurate-predictions.html (date inconnue ; ouverte)
- Citation : « almost 30% more accurate than those of career intelligence agents »
- Chiffres : les 60 meilleurs prévisionnistes (superforecasters) sur un bassin d'environ 2 200 à 3 900 volontaires ; formation incluant « base-rate neglect » ; les superforecasters montrent plus de « willingness to change their minds in response to new evidence ».
- Ce que ça établit : deux traits mesurables du bon prévisionniste : ancrage sur les taux de base et mise à jour quand de nouvelles preuves arrivent.
- Règle pour la grille : à chaque porte, réviser la probabilité avec une règle écrite (preuve nouvelle donne une nouvelle probabilité datée), pas une nouvelle note.

### W4-10 : Lovallo et Kahneman 2003, « Delusions of Success » (Harvard Business Review)
- Acteur / marché : Harvard Business Review, juillet 2003
- Type : recherche académique (article de synthèse)
- Source : https://hbr.org/2003/07/delusions-of-success-how-optimism-undermines-executives-decisions (date : 2003-07 ; ouverte mais seul le résumé est lisible, article payant)
- Citation : « The evidence is disturbingly clear »
- Chiffres : aucun lisible. Le contenu (vue intérieure et vue extérieure) est confirmé par citation dans W4-6, pas par cette page.
- Ce que ça établit : l'article existe et est daté ; son contenu n'a pas été lu en entier.
- Règle pour la grille : ne pas citer de chiffre de cet article sans l'avoir lu.

## Lot 3 : causes d'échec (point 5) et pionniers (point 4), début

### W4-11 : CB Insights, raisons d'échec de 431 start-up financées par capital-risque (mars 2026)
- Acteur / marché : CB Insights, start-up soutenues par le capital-risque qui ont fermé publiquement depuis 2023 (périmètre géographique non précisé dans ce qui a été lu)
- Type : tendance (données déclaratives, post-mortems publics)
- Source : https://www.cbinsights.com/research/startup-failure-reasons-top/ (date : 2026-03-05 ; ouverte)
- Citation : « We analyzed public post-mortems, founder interviews, and shutdown announcements »
- Chiffres : 431 start-up, causes identifiables pour 385. Plusieurs causes possibles par start-up (total > 100 %). Capitaux épuisés 70 %, mauvaise adéquation produit-marché 43 %, mauvais timing ou contexte macro 29 %, économie unitaire non viable 19 %. Le rapport précise que le manque de trésorerie est souvent la cause finale, pas la cause racine.
- Ce que ça établit (citations et chiffres vérifiés dans le HTML de la page) : méthode déclarative (post-mortems publics et déclarations de fondateurs), échantillon limité aux start-up financées par capital-risque ayant fermé publiquement depuis 2023, période que la page décrit comme « the post-zero-interest-rate shakeout » (fin des taux zéro) ; la page est aussi une publicité pour un livre de post-mortems payant. CB Insights est un vendeur de données : confiance faible selon nos règles. Ce n'est ni un taux d'échec ni une distribution des causes pour des PME françaises. La page note elle-même que « Ran out of capital » est presque toujours la cause finale et non la cause racine.
- Règle pour la grille : n'utiliser la liste des causes que comme liste de questions de test (marché, timing, économie unitaire), jamais comme pondération. Contre-preuve de portée : le périmètre n'est pas celui d'un commerce ou d'un service local français.

### W4-12 : Tellis et Golder 1996, MIT Sloan Management Review, précurseurs et leaders durables
- Acteur / marché : recherche académique, MIT Sloan Management Review
- Type : recherche académique
- Source : https://sloanreview.mit.edu/article/first-to-market-first-to-fail-real-causes-of-enduring-market-leadership/ (date : 1996-01-15 ; ouverte)
- Citation : « many pioneers fail, while most current leaders are not pioneers »
- Chiffres : les études fondées sur les bases PIMS et ASSESSOR donnent aux pionniers une part moyenne d'environ 30 % (confirmé par W4-18) contre 19 % pour les suiveurs précoces et 13 % pour les entrants tardifs (lecture automatique, non confirmés ailleurs) ; ces bases viennent d'enquêtes sur des entreprises survivantes, donc sans les échecs ; analyse historique de catégories (couches jetables, ordinateurs personnels, magnétoscopes, bière légère, rasoirs). Facteurs de leadership durable : vision, persévérance, engagement, innovation, effet de levier sur les actifs.
- Ce que ça établit : le « avantage du pionnier » est en partie un biais de survivant ; les leaders durables sont souvent des entrants plus tardifs.
- Règle pour la grille : traiter « être premier » comme un indicateur non prédictif. Les 30 % de part de marché des pionniers sont le chiffre PIMS que Golder et Tellis 1993 contestent (W4-18).

## Lot 4 : point 2 (suite), points 3, 4 et 5

### W4-13 : Cooper, Woo et Dunkelberg 1988, l'optimisme des créateurs est détaché des taux de base
- Acteur / marché : recherche académique (Journal of Business Venturing 3(2), 97-108) ; 2 994 créateurs américains membres de la NFIB, enquête du printemps 1985, propriétaires depuis 1984-1985 (activité médiane de 12 mois)
- Type : recherche académique
- Source : https://gwern.net/doc/psychology/cognitive-bias/1988-cooper.pdf (date : 1988 ; ouverte (PDF texte), copie hébergée par gwern.net)
- Citation : « A remarkable 33% perceived their chances as "dead certain," 10 out of 10. »
- Chiffres : 95 % jugent leurs chances à 5 sur 10 ou plus, 81 % à 7 sur 10 ou plus, moyenne 8,1 sur 10. Pour « une entreprise comme la vôtre » : moyenne 5,9 ; 39 % donnent 7 sur 10 ou plus. Selon le résumé de l'article, les créateurs mal préparés sont aussi optimistes que les bien préparés.
- Ce que ça établit : l'estimation de leurs propres chances par les créateurs est « détachée » des statistiques, de la perception des pairs et de leurs caractéristiques ; l'optimisme est la norme, pas l'exception. Limites : échantillon américain de 1985, mesure d'opinion (pas de résultat observé).
- Règle pour la grille : une probabilité de réussite posée à l'intuition (par l'équipe ou par nous) est suspecte par défaut ; elle s'ancre sur le taux de base (W4-1) et ne s'en écarte que pour des raisons sourcées.

### W4-14 : Friedman et al. 2018, la précision des probabilités a de la valeur quand elles sont suivies
- Acteur / marché : recherche académique (International Studies Quarterly 62(2), 410-422), Good Judgment Project
- Type : recherche académique
- Source : https://academic.oup.com/isq/advance-article/doi/10.1093/isq/sqx078/4944059 (date : 2018-03-19 ; ouverte, 100 000 premiers caractères sur 161 000)
- Citation : « consistently sacrifices predictive accuracy » (à propos de l'arrondi des probabilités en catégories qualitatives)
- Chiffres : 888 328 prévisions ; arrondir en catégories grossières (échelle verbale) dégrade le score de Brier dans tous les sous-groupes testés ; arrondi en 2 classes : score de Brier moyen +31 % pour l'ensemble, plus de 500 % pour les superforecasters (lecture automatique, à revérifier). Les prévisionnistes formés et travaillant en groupe tirent plus de profit de la précision. Limites : volontaires, échelle de réponse non randomisée.
- Ce que ça établit : le défaut des notes « 7,35 contre 7,20 » n'est pas la précision en soi ; une probabilité fine est utile quand elle vient de prévisionnistes entraînés et dont les résultats sont suivis. Une somme de points subjectifs non calibrée avec des décimales ne porte pas cette information [INFÉRENCE].
- Règle pour la grille : exprimer les décisions de porte en probabilités datées et les scorer (W4-8) ; ne pas afficher de décimales sur un score qui n'a jamais été confronté à des résultats.

### W4-15 : Strategyzer, échelle de force de la preuve de 0 à 5
- Acteur / marché : Strategyzer (Osterwalder, Viki, Bostelaar), méthode « Testing Business Ideas »
- Type : praticiens reconnus
- Source : https://www.strategyzer.com/library/business-project-succcess (date : 2026-09-02 ; ouverte)
- Citation : « Five customer interviews and a million customer interviews score identically. »
- Chiffres : niveau 0 = pas une preuve (plans d'affaires, tableurs, études de marché générales) ; 1 = ce que les gens disent (entretiens, enquêtes) ; 2 = réaction à un artefact (fiche produit, brochure, maquette) ; 3 = action à faible enjeu (inscription à une page, rendez-vous commercial) ; 4 = action à enjeu significatif (lettre d'intention signée, précommande) ; 5 = comportement réel observé sans que le client sache qu'il est testé. Le seuil qui compte est entre 2 et 3 (dire contre faire). Autre phrase de la page : « If you have a thousand, it's still a 1. »
- Ce que ça établit (citations et date vérifiées dans le HTML de la page) : la force d'une preuve vient de la nature de l'engagement du client, jamais du nombre de réponses. Limite : page éditoriale d'un vendeur de formation qui promeut son propre abonnement ; l'échelle 0 à 5 est celle de Strategyzer, sans validation académique lue. Le niveau 4 est décrit par « Real skin in the game. A signed letter of intent, a full-day co-creation workshop, a pre-sale. »
- Règle pour la grille : étiqueter chaque ligne de la grille par un niveau de preuve ; seuls les niveaux 3 à 5 comptent comme engagement à la porte 2 (temps engagé = 3, précommande ou lettre d'intention = 4) ; niveaux 0 à 2 = hypothèses, non comptées dans le score. Le plafond chiffré à appliquer aux niveaux bas n'a pas de source : [HYPOTHÈSE].

### W4-16 : Cambridge Judge Business School, dix tests d'une opportunité (support de cours)
- Acteur / marché : Cambridge Judge Business School (Simon Stockley), support de cours « Is your idea an opportunity? »
- Type : praticiens reconnus (support pédagogique, source secondaire pour les critères de type Timmons)
- Source : https://www.jbs.cam.ac.uk/wp-content/uploads/2020/08/screening-opportunities.pdf (date : 2020 d'après l'URL ; ouverte (PDF texte))
- Citation : « Most fail because of poor opportunity evaluation »
- Chiffres / contenu : dix tests : conditions de marché ; conditions de secteur ; accès aux ressources ; technologie ; timing (marché, financement) ; scalabilité ; sortie ; adéquation personnelle ; équipe ; modèle de revenus. Entonnoir : 100 idées, 33 opportunités de marché, 10 opportunités d'affaires, 1 réalisée (non sourcé). Autres phrases : « Folklore says 80% but difficult to measure » ; « 65% of all failures are avoidable » (non sourcé). « Dream ticket » : marché supérieur à 100 m (monnaie non précisée), croissance 20 % par an, marge brute 40 % et plus, résultat net 10 à 15 %, rentabilité pour investisseurs supérieure à 30 % de TRI.
- Ce que ça établit : un support de formateur liste les critères d'une opportunité ; ses seuils de « ticket de rêve » visent des projets financés par des investisseurs, donc plus exigeants que nos seuils (50 M€ de marché, 8 % de croissance). L'entonnoir 100-33-10-1 et les 65 % ne sont pas sourcés. Les critères de Timmons d'origine n'ont pas été obtenus.
- Règle pour la grille : ne pas importer les seuils ; utiliser les dix tests comme liste de couverture : notre grille n'a pas de ligne pour le timing, l'économie unitaire (modèle de revenus) ni la scalabilité.

### W4-17 : Y Combinator (Kevin Hale, Startup School), critères pour évaluer une idée
- Acteur / marché : Y Combinator, billet de blog sur le cours de Kevin Hale
- Type : praticiens reconnus
- Source : https://www.ycombinator.com/blog/startup-school-podcast-preview-with-kevin-hale (date : 2019-07-31 ; ouverte)
- Citation : « A startup idea is basically a hypothesis »
- Chiffres / contenu : un bon problème est populaire, en croissance, urgent, coûteux, obligatoire et fréquent ; « You want to avoid problems that there's a small number of people that have it. » Marché en croissance d'environ 20 % par an (jugé l'un des avantages les plus faibles s'il est seul) ; produit 10 fois meilleur (2 ou 3 fois mieux = « nice » mais insuffisant) ; modèle d'acquisition (canaux gratuits préférés à l'acquisition payante) ; monopole ; « threshold belief » (peut-on le construire) et « miracle belief » (peut-il décoller), la seconde jugée la plus importante.
- Ce que ça établit : un praticien reconnu traite l'idée comme une hypothèse dont on cherche la croyance la plus fragile ; mais ses critères visent la croissance rapide financée par capital-risque.
- Règle pour la grille : cohérent avec l'étape `before-you-build` (croyance la plus fragile) ; ne pas importer les seuils « 20 % » et « 10 fois » : contre-preuve de portée, notre cible est une entreprise de 500 k€ de CA, pas une croissance de type capital-risque.

### W4-18 : Golder et Tellis 1993, 47 % des pionniers échouent, les leaders précoces gagnent
- Acteur / marché : recherche académique (Journal of Marketing Research 30(2), 158-170) ; environ 500 marques dans 50 catégories de produits, analyse historique incluant les marques disparues
- Type : recherche académique
- Source : https://people.duke.edu/~moorman/Marketing-Strategy-Seminar-2015/Session%205/Golder%20and%20Tellis.pdf (date : 1993-05 ; ouverte (PDF texte), copie JSTOR hébergée par Duke)
- Citation : « Forty-seven percent of market pioneers fail. » (conclusion 2 de l'article ; l'extraction PDF avait supprimé les espaces, rétablis ici)
- Chiffres : taux d'échec des pionniers 47 % ; part de marché moyenne des pionniers 10 % (contre 30 % dans les données PIMS ; l'article attribue environ la moitié de l'écart à l'inclusion des marques disparues) ; 11 % des pionniers sont leaders aujourd'hui ; « early leaders » : taux d'échec 8 %, part de marché 28 %, entrés en moyenne 13 ans après le pionnier. « Échec » = fin des ventes sous la marque d'entrée dans la catégorie. Taux d'échec plus de deux fois plus élevé pour les biens durables que non durables. Limites des auteurs : pas d'analyse du mix marketing, biais de survivant possible, « past success or failure does not automatically imply future outcomes ».
- Ce que ça établit : dans ces catégories de produits, ceux qui entrent après le pionnier mais tôt dans la croissance réussissent mieux que lui ; mais avec 13 ans de retard moyen, sur des catégories de produits (exemples cités : bière légère, fours à micro-ondes, Xerox, Polaroid), et pas pour la transposition d'un modèle de service dans un autre pays.
- Règle pour la grille : ne mettre aucun bonus ni malus d'ordre d'entrée dans la note ; ces chiffres ne se transposent pas tels quels à un modèle copié depuis l'étranger.

### W4-19 : VanderWerf et Mahon 1997, l'avantage du pionnier dépend de la méthode de mesure
- Acteur / marché : méta-analyse (Management Science 43(11), 1510-1519)
- Type : recherche académique (contre-preuve partielle à W4-18 sur le biais de survivant)
- Source : https://ideas.repec.org/a/inm/ormnsc/v43y1997i11p1510-1519.html (date : 1997-11 ; ouverte, résumé lu dans le HTML)
- Citation : « no more often than can be accounted for by random statistical error alone »
- Chiffres / contenu : les tests qui mesurent la performance par la part de marché trouvent beaucoup plus souvent un avantage du pionnier que ceux qui mesurent rentabilité ou survie ; l'échantillonnage par industries choisies et l'absence de mesure de la force concurrentielle des entrants augmentent aussi la probabilité d'en trouver un. Les auteurs trouvent « little evidence » que le biais de survivant change les résultats. Les tests sans aucune des pratiques mises en cause trouvent un avantage pas plus souvent que le hasard.
- Ce que ça établit : l'avantage du pionnier est surtout un effet de la mesure choisie (part de marché) ; sur rentabilité et survie, aucun avantage systématique. Contredit W4-18 sur l'importance du biais de survivant, mais pas sur la conclusion.
- Règle pour la grille : juger un suiveur sur la rentabilité et la survie de ses semblables, pas sur la part de marché.

### W4-20 : Shenkar 2010 (Harvard Business Review), l'imitation comme comprendre la cause du succès
- Acteur / marché : Harvard Business Review, avril 2010 ; livre Copycats (Harvard Business Press, 2010)
- Type : praticiens reconnus / recherche académique (résumé seul lisible)
- Source : https://hbr.org/2010/04/defend-your-research-imitation-is-more-valuable-than-innovation (date : 2010-04 ; ouverte, résumé seul, article payant)
- Citation : « Imitation is not mindless repetition; it's an intelligent search for cause and effect. »
- Chiffres : aucun lisible. Un résultat de recherche (extrait, non vérifié, source secondaire) attribue au livre : coût d'imitation de 65 à 75 % du coût d'innovation et délai d'environ 70 % ; confiance faible.
- Ce que ça établit : la thèse de l'auteur est que l'imitation efficace comprend la cause du succès au lieu de copier la forme ; aucune donnée de taux de succès des imitateurs n'a pu être lue.
- Règle pour la grille : la fiche d'un « modèle prouvé » doit écrire POURQUOI le modèle marche à l'étranger (la cause) avant de lui donner un niveau de preuve.

### W4-21 : Mehrotra et Velamuri 2021, copier un modèle étranger : copier les opérations, adapter client et prix
- Acteur / marché : recherche académique (Management and Organization Review 17, numéro spécial 2) ; deux chaînes de restauration rapide créées en Chine et en Inde
- Type : recherche académique (deux cas)
- Source : https://www.cambridge.org/core/product/3C7820E4DE1CAF6DF228A207A07197F9 (date : 2021-02-15 en ligne ; ouverte, 100 000 premiers caractères sur 126 000)
- Citation : « Inspired by the successful business models of international QSR brands »
- Chiffres : 1 400 points de vente en Chine et 300 en Inde (résumé de l'article, relu dans le HTML) ; répartition en 2019 : Chine environ 90 % franchisés, Inde 40 en propre et 260 franchisés (corps du texte, lecture automatique). Copié : chaîne de valeur et opérations (emplacements, format de magasin, personnel, logistique) et modèle de franchise. Adapté : produits (snacks régionaux), clients (actifs urbains de classe moyenne), prix (juste au-dessus des vendeurs de rue), niveau d'investissement des franchisés. Les auteurs écrivent que le petit échantillon limite la généralisation.
- Ce que ça établit : sur deux cas réussis, les opérations se copient, la cible et la monétisation s'adaptent au pays. Aucune étude à grand échantillon sur le taux de succès des transpositions de modèles d'un pays à un autre n'a été trouvée.
- Règle pour la grille : pour une piste « modèle étranger », séparer dans la fiche ce qui est copié (opérations) de ce qui doit être testé en France (cible, prix, offre) ; la porte 2 porte sur la partie adaptée.

### W4-22 : Cantamessa et al. 2018, post-mortems de start-up et stratégie de développement commercial
- Acteur / marché : recherche académique (Sustainability 10(7), 2346), Politecnico di Torino
- Type : recherche académique
- Source : https://ideas.repec.org/a/gam/jsusta/v10y2018i7p2346-d156535.html (date : 2018-07 ; ouverte, résumé seul ; texte intégral MDPI et IRIS Polito refusés en 403)
- Citation : « lack of a structured Business Development strategy »
- Chiffres (résumé relu dans le HTML de la page) : « a large database of 214 startup post-mortem reports » ; méthode de classification dérivée d'une taxonomie de facteurs d'échec ; le manque de stratégie de développement commercial structurée est un déterminant clé dans la majorité des cas. Pays et période des rapports non lus.
- Ce que ça établit : même limite que CB Insights (documents déclaratifs, non structurés) ; le facteur identifié rejoint la ligne « canal d'acquisition existant » de la grille. Résumé seul lu : ne pas en tirer de pondération.
- Règle pour la grille : conserver la ligne « segment accessible et canal d'acquisition » ; ne pas changer son poids sur cette seule source.

### W4-23 : Rogoff, Lee et Suh 2004, les entrepreneurs s'attribuent les succès et attribuent les échecs à l'extérieur
- Acteur / marché : recherche académique (Journal of Small Business Management 42(4), 364-376) ; pharmaciens indépendants, propriétaires de petites entreprises, experts
- Type : recherche académique (critique des post-mortems déclaratifs)
- Source : https://ideas.repec.org/a/taf/ujbmxx/v42y2004i4p364-376.html (date : 2004-10 ; ouverte, résumé)
- Citation : « The presence of a self‐serving attribution bias is shown in the two business owners' samples. »
- Chiffres (résumé vérifié dans le HTML de la page) : trois échantillons comparés (pharmaciens indépendants, propriétaires d'entreprises de secteurs variés, experts) ; biais d'auto-complaisance montré dans les deux échantillons de propriétaires ; « clear differences are shown between the entrepreneurs and the experts », ce que les auteurs lisent comme un biais acteur-observateur. Tailles d'échantillon non lues.
- Ce que ça établit : les explications d'échec données par les fondateurs sont biaisées en faveur de causes extérieures ; les experts extérieurs attribuent différemment. [INFÉRENCE] Les post-mortems publics et les interviews de fondateurs qui nourrissent CB Insights (W4-11) portent donc le même biais ; CB Insights le dit en partie lui-même (cause finale, pas cause racine).
- Règle pour la grille : ne jamais fonder un poids sur le classement des « raisons » d'échec déclarées ; utiliser les tests qui peuvent être mesurés avant lancement (preuve d'engagement, économie unitaire, timing).

### W4-24 : Kibler et al. 2017, raconter l'échec par des causes externes préserve la légitimité
- Acteur / marché : Journal of Business Venturing (2017), communiqué de l'université Anglia Ruskin relayé par Cambridge Network
- Type : recherche académique (source secondaire : communiqué)
- Source : https://www.cambridgenetwork.co.uk/news/failed-business-blame-perfect-storm (date : 2017-02-27 ; ouverte)
- Citation : « attributing the cause of failure to external circumstances beyond their control »
- Chiffres : enquête en ligne de 601 participants jugeant des profils d'entreprises défaillantes.
- Ce que ça établit : un fondateur a intérêt à présenter l'échec comme dû à des causes extérieures : incitation qui renforce le biais de W4-23 dans les post-mortems publics.
- Règle pour la grille : même règle que W4-23. Confiance moyenne (communiqué).

### W4-25 : Dawes 1979, des poids égaux prédisent presque aussi bien que des poids optimisés
- Acteur / marché : recherche académique (American Psychologist 34(7), 571-582)
- Type : recherche académique
- Source : https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf (date : 1979-07 ; ouverte (PDF texte))
- Citation : « unit (i.e., equal) weighting is quite robust for making such predictions »
- Chiffres / contenu : des modèles linéaires « impropres » (poids égaux, intuitifs ou issus de l'imitation d'un juge) battent l'intuition clinique pour prédire un critère numérique à partir de prédicteurs numériques ; le texte dit que les modèles linéaires sont « robust over deviations from optimal weighting » ; Dawes et Corrigan 1974 (cités) : l'essentiel est de savoir quelles variables regarder, puis de les additionner.
- Ce que ça établit : le choix des variables et du sens de leur effet compte plus que la précision des poids. Nos poids 25 / 25 / 20 / 15 / 15 n'ont aucune source dans le dépôt ; rien n'indique qu'ils classent mieux que des poids égaux. Limite : la source porte sur la prédiction de critères numériques ; notre grille mêle des seuils éliminatoires (non compensatoires) et un score, donc le transfert est une [INFÉRENCE].
- Règle pour la grille : soit poids égaux, soit calcul de la note avec plusieurs jeux de poids et affichage de l'intervalle ; ne pas départager deux pistes dont les intervalles se recouvrent.

## Contre-preuves et limites à garder

- W4-6 : l'auteur de la méthode écrit que la vue extérieure peut manquer les résultats extrêmes et que le choix de la classe est plus difficile sans précédents (idée neuve) ; une piste qui copie un modèle existant a des précédents, donc la méthode s'y applique bien.
- W4-2 : la hausse de la pérennité 2014 à 2018 vient en partie d'un changement de composition et d'aides Covid ; ne pas prendre 69 % comme norme durable.
- W4-5 : la Banque de France donne des nombres, pas des taux ; la conjoncture 2026 est dégradée (+19,3 % sur la moyenne 2010-2019).
- W4-11 : CB Insights concerne des start-up financées par capital-risque (périmètre géographique non précisé), pas des PME françaises.
- W4-17 et W4-16 : seuils pensés pour des projets finançables par investisseurs.
- W4-19 contredit W4-18 sur le poids du biais de survivant.
- W4-25 : transfert aux grilles à seuils éliminatoires non démontré.

## Sources non lues ou inutilisables

- https://pubsonline.informs.org/doi/10.1287/mnsc.39.1.17 (Kahneman et Lovallo 1993) : 403 ; l'article de 2003 (HBR) est payant ; leurs thèses ne sont lues que par citation dans W4-6.
- https://goodjudgment.com/philip-tetlocks-10-commandments-of-superforecasting/ : 403 (les dix commandements des superforecasters n'ont pas été lus).
- https://www.mdpi.com/2071-1050/10/7/2346 et le PDF IRIS Polito : 403 (Cantamessa : résumé seul via IDEAS).
- https://core.ac.uk/download/236084361.pdf : 403 (thèse citant les critères de Timmons) ; https://www.hufocw.org/Download/file/9436 : PDF d'images sans texte ; critères de Timmons d'origine non obtenus.
- https://www.insee.fr/fr/statistiques/fichier/8634190/IP2070.pdf : le fichier contient seulement la figure 1 ; texte lu sur la page https://www.insee.fr/fr/statistiques/8634190.
- https://www.cci-paris-idf.fr/fr/prospective/crocis/perennite-entreprises-covid19 : extrait de recherche seulement (pérennité à 5 ans et Covid), non ouvert.
- https://www.gsb.stanford.edu/faculty-research/case-studies/copycats-clones-fast-followers-note-replicating-business-models : note de cas réservée aux affiliés Stanford (extrait de recherche).
- Winter et Szulanski 2001, Meissner 2013 (Klarna), Jonsson et Foss (IKEA), Boulding et Christen 2003, Szymanski et al. 1995 : cités dans des résultats de recherche ou connus, non ouverts.
- https://wildfirelabs.substack.com/p/why-startups-fail-patterns-from-2 : ouvert, écarté (ne critique pas CB Insights, reprend ses chiffres sans méthode).
- https://en.wikipedia.org/wiki/Superforecasting : ouvert, contenu de la page du Good Judgment Project ; chiffres non repris (source secondaire, citation non copiée telle quelle).
- https://en.wikipedia.org/wiki/First-mover_advantage : ouvert, sans les chiffres empiriques cherchés (page signalée sans références suffisantes).

## Statut

Statut : partiel. Ce qui manque, liste exacte :
- taux de défaillance par secteur (stock d'entreprises et définition des procédures comptées par la Banque de France) ;
- probabilité d'atteindre 500 k€ de CA à 3 ans par secteur (Esane ou FARE non explorés) ;
- taux de succès des transpositions de modèles étrangers (aucune étude à grand échantillon trouvée) et chiffres de Shenkar ;
- textes non lus : Timmons d'origine, livre « Testing Business Ideas », Kahneman et Lovallo 1993 et 2003, dix commandements de Tetlock, Cantamessa en texte intégral, Boulding et Christen 2003, Szymanski et al. 1995, Winter et Szulanski 2001 ;
- lien empirique entre les cinq critères de la grille et la survie ou le CA d'une PME (aucun trouvé : les poids restent [HYPOTHÈSE]) ;
- critique méthodologique publiée visant CB Insights (aucune trouvée) ;
- relecture par le vérificateur : W4-14 (résumé automatique, 403 en téléchargement direct), W4-21 (corps du texte), W4-3 et W4-4 (secteurs, hors chiffres clés) restent à contrôler.
