# Porte 1 : agroalimentaire TPE/PME, logiciels et services déjà payés (travail)

- Mission : argent visible, logiciels/services payés par TPE/PME agro en France (recherche de zéro)
- Date : 2026-11-02 | Recherches web : 12/12 | WebFetch : 8 (4 en 403) | API Sirene : 1 série de comptages
- Preuves : 14 | Domaines distincts : 10 (recherche-entreprises.api.gouv.fr, comeup.com, appvizer.fr, capterra.fr/.com, getapp.co.nz, lafabriquedunet.fr, logiciels.pro, agriculture.gouv.fr/info.agriculture.gouv.fr, orne.gouv.fr, em-lyon.com/Bpifrance-ministère)
- Statut : partiel (voir fin). Vérification archives : Grep par mots-clés, 14 occurrences dans 7 fichiers (v1/v2/v3), non lus ; aucune piste agro dédiée repérée par le nom de fichier. [HYPOTHÈSE] pas d'élimination antérieure, à confirmer par un Grep ciblé si une piste avance.

## Comptage cible (API Sirene, unités actives, toutes tailles dont non-employeurs ; ce n'est pas Esane)

### A1 : Entreprises actives par code NAF (Sirene)
- Acteur / marché : cibles des logiciels de traçabilité/PMS/étiquetage
- Type : tendance (comptage)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=<NAF>&etat_administratif=A&per_page=1 (API ouverte, date : 2026-11-02)
- Citation : « total_results » (champ de l'API, pas de citation textuelle)
- Chiffres : fromageries 10.51C 919 (dont 561 avec 1+ salarié, tranches 01 à 22) ; laiteries 10.51A 250 ; viandes transformées 10.13A 939 ; charcuterie 10.13B 2 962 ; boucherie-abattage 10.11Z 2 645 ; biscuits/pâtisserie de conservation 10.72Z 4 571 ; plats préparés 10.85Z 2 869 ; autres produits alim. 10.89Z 2 249 ; conserves fruits/légumes 10.39B 1 725 ; chocolat/confiserie 10.82Z non relevé ; brasseries 11.05Z 2 919 ; cidre/vins/spiritueux 11.01Z non relevé, 11.02B 1 315, 11.02A 406, 11.03Z 236, 11.04Z 157. Somme des codes relevés, hors boulangerie-pâtisserie (10.71C/D, plus de 19 000 unités) : environ 31 800 unités.
- Ce que ça dit pour nous : le nombre de cibles dépasse largement 3 000 ; mais beaucoup sont des non-employeurs ou sans atelier, donc le vrai SAM payant est inférieur (non chiffré).

### A2 : Tissu agro national
- Acteur / marché : filière agroalimentaire France
- Type : tendance
- Source : https://em-lyon.com/en/node/457 (extrait de recherche, fiche ministère Agriculture - Bpifrance ; date inconnue)
- Citation : « près de 18 000 entreprises agroalimentaires, dont 98% sont des TPE/PME »
- Chiffres : 18 000 entreprises, 380 000 ETP, 167 Md€ de CA (volume France). Unités de comptage différentes de Sirene (A1) : ne pas additionner.
- Ce que ça dit pour nous : plafond institutionnel du nombre de clients, environ 17 600 TPE/PME hors artisanat de bouche.

## Prix publics payés

### P1 : HACCP AI Pro, 19 €/mois
- Acteur / marché : HACCP AI Pro vend relevés température, nettoyage, traçabilité aux artisans de bouche
- Type : argent dépensé (prix public ; clients payants non vus)
- Source : https://www.capterra.com/p/10047830/haccpaipro/ (extrait de recherche ; page en 403 ; date inconnue)
- Citation : « à partir de 19€/mois » (synthèse du moteur, non copiée du site)
- Chiffres : 19 €/mois ; nombre de clients inconnu
- Ce que ça dit pour nous : prix plancher très bas ; le PMS numérique pour artisan est une commodité.

### P2 : Melba (FoodMeUp), traçabilité
- Acteur / marché : FoodMeUp vend recettes, production, traçabilité aux restaurateurs, traiteurs, boulangers-pâtissiers
- Type : argent dépensé (prix public)
- Source : https://www.lafabriquedunet.fr/logiciel/melba (extrait de recherche ; 403) ; https://www.cbinsights.com/compare/foodmeup-vs-kitchen-data-systems (extrait ; 72 $/mois de départ)
- Citation : « 49 € HT par mois (Simple) ou 99 € HT par mois (Premium) » (synthèse du moteur, non confirmée par une 2e source)
- Chiffres : 49 / 99 € HT par mois selon l'extrait lafabriquedunet ; autre agrégateur : 72 $/mois de départ. Contradiction de prix : confiance faible.
- Ce que ça dit pour nous : fourchette 50 à 100 €/mois pour un acteur français établi (2016).

### P3 : ePackPro, matériel inclus
- Acteur / marché : ePackPro (ex-ePack Hygiène), formule tout compris avec tablette
- Type : argent dépensé (prix public)
- Source : https://www.lafabriquedunet.fr/logiciel/epackpro (extrait de recherche ; 403)
- Citation : « démarre à 119 € HT par mois sur tablette » (synthèse du moteur)
- Chiffres : 119 € HT/mois
- Ce que ça dit pour nous : le prix monte à 119 € quand le matériel est inclus.

### P4 : AidoPMS (VICI), 29,99 €/mois
- Acteur / marché : AidoPMS, surtout restauration collective
- Type : argent dépensé (prix public)
- Source : https://www.lafabriquedunet.fr/logiciel/aidopms (extrait de recherche)
- Citation : « à partir de 29,99 € HT par mois » (synthèse du moteur)
- Chiffres : 29,99 € HT/mois
- Ce que ça dit pour nous : 4 prix publics HACCP/traçabilité entre 19 et 119 €/mois ; seuil « 3 prix » atteint pour ce marché, mais clients payants non identifiés.

### P5 : Services freelances ComeUp, fiche technique + étiquette INCO
- Acteur / marché : freelance « Fourtservives » vend fiches techniques et étiquettes INCO à des producteurs
- Type : argent dépensé (prix public, 1 vente seulement)
- Source : https://comeup.com/fr/service/504282/creer-vos-fiches-techniques-alimentaires-et-vos-etiquettes-inco-conformes (ouverte, date : 2026-11-02)
- Citation : « Travail sérieux et consciencieux, à l'écoute des attentes du client. »
- Chiffres : 15 € (1 fiche ou 1 étiquette), 35 € (fiche + étiquette), 80 € (jusqu'à 5 produits, vérification de conformité) ; note 5,0, 1 avis, 1 vente
- Ce que ça dit pour nous : le besoin existe mais la demande observée est quasi nulle (1 vente) ; prix par produit de 15 à 80 €.

### P6 : Services freelances ComeUp, PMS HACCP
- Acteur / marché : consultante QHSE vend un PMS à restaurants, boulangeries, petits fabricants
- Type : argent dépensé (prix public ; vendeuse inscrite depuis mai 2026)
- Source : https://comeup.com/fr/service/535788/creer-un-pms-plan-de-maitrise-sanitaire-haccp (ouverte, 2026-11-02)
- Citation : « Je vous fournis un dossier professionnel au format numérique. »
- Chiffres : 35 € (base), options +44 € (allergènes), +66 € (guide bonnes pratiques), +110 € (PMS complet) ; 1 vente
- Ce que ça dit pour nous : un PMS complet se vend 35 à 145 € en freelance : prix d'ancrage très bas face au consultant.

### P7 : Consultant hygiène et formation PMS
- Acteur / marché : consultant freelance et formation inter-entreprises
- Type : argent dépensé (prix public)
- Source : https://www.malt.fr/profile/rachidaitlasri (extrait de recherche ; malt bloqué) ; https://labo.lozere.fr/sites/default/files/upload/planning_de_formation_2024.pdf (extrait de recherche)
- Citation : « 246,71 € par stagiaire » (formation PMS/HACCP 7 h, planning 2024, synthèse du moteur)
- Chiffres : 200 €/jour (un consultant, annonce unique) ; 246,71 € par stagiaire pour 7 h
- Ce que ça dit pour nous : le conseil hygiène se vend 200 €/jour ; des formations sont déjà payées (financées souvent par OPCO : [HYPOTHÈSE]).

### P8 : Étiquetage nutrition, outils étrangers
- Acteur / marché : Food Label Maker (Canada) et Resto Couts (France) vendent recettes, allergènes, coûts
- Type : argent dépensé (prix public)
- Source : https://foodlabelmaker.com/fr-ca/ et https://www.getapp.co.nz/software/2113631/resto-couts (extraits de recherche)
- Citation : « 29 €/mois » (Resto Couts, fiches et recettes illimitées, synthèse du moteur)
- Chiffres : Resto Couts 29 €/mois ; Food Label Maker 49 $ CAD et 99 $ CAD/mois (règles canadiennes CFIA, non INCO)
- Ce que ça dit pour nous : aucun éditeur INCO français pour producteur n'a de prix affiché dans mes résultats ; trou ou simple défaut de recherche.

## Faiblesses des acteurs

### F1 : Prix cachés, peu d'avis
- Acteur / marché : HACCP Now, Cashmere, Date Check Pro (Appvizer)
- Type : plainte (faible)
- Source : https://www.appvizer.fr/biens/tracabilite-alimentaire (ouverte, 2026-11-02)
- Citation : « Tarif sur demande »
- Chiffres : HACCP Now 4,6/5 sur 7 avis ; Cashmere et Date Check Pro 0 avis ; 3 sur 3 sans prix
- Ce que ça dit pour nous : opacité tarifaire et quasi-absence d'avis : acteurs peu visibles auprès des TPE.

### F2 : Logiciels de brasserie inadaptés à la douane française
- Acteur / marché : BeerSmith, ERP pour brasseries
- Type : plainte (comparatif éditorial)
- Source : https://www.logiciels.pro/comparateur-logiciels-pour-brasserie/ (ouverte, date inconnue)
- Citation : « limité sur la partie commerciale et douanière française »
- Chiffres : aucun prix lu ; ERP complets décrits comme « usines à gaz »
- Ce que ça dit pour nous : angle douane (DRM, DAE) pour brasseries, mais comparateur à liens d'affiliation probable : confiance faible.

### F3 : Notes Capterra sur petits volumes
- Acteur / marché : MRPeasy, Stocksmith, Ollie, Vicinity (fabricants/brasseurs)
- Type : plainte (absence d'offre française)
- Source : https://www.capterra.fr/directory/30563/food-traceability/software (extrait de recherche ; non ouverte)
- Citation : « 4.5/5 sur 168 avis » (MRPeasy, synthèse du moteur)
- Chiffres : MRPeasy 4,5 sur 168 avis ; Stocksmith 4,6 sur 245 ; Ollie 3,6 sur 5 avis. Outils majoritairement étrangers, prix non lus.
- Ce que ça dit pour nous : les outils qui ont des avis sont étrangers ; place pour un outil francisé (INCO, DLC, RappelConso, douane).

## Obligation réglementaire et rappels

### R1 : Traçabilité obligatoire
- Acteur / marché : tout exploitant alimentaire, y compris remise directe
- Type : obligation
- Source : https://www.orne.gouv.fr/contenu/telechargement/10316/92764/file/20200115_notice-remise-directe_cle7c2b7e.pdf (extrait de recherche, 2020) ; note régionale sur art. 18 du règlement (CE) 178/2002 (extrait)
- Citation : « application de l'article 18 du règlement (CE) n° 178/2002 »
- Chiffres : sans objet
- Ce que ça dit pour nous : obligation ancienne et stable (non lié à une échéance) ; sert de fondation, pas de moteur de croissance.

### R2 : Rappels produits en hausse
- Acteur / marché : producteurs alimentaires (RappelConso)
- Type : tendance
- Source : https://www.slate.fr/boire-manger/cinq-six-rappels-produits-alimentaires-jour-peur-assiettes-rappel-conso-contamination-bacterie-listeria-e-coli-inquietude-sante (extrait de recherche ; 403 à l'ouverture ; date inconnue)
- Citation : « 2.151 rappels alimentaires en 2024, contre 2.025 en 2023 » (synthèse du moteur)
- Chiffres : 2 151 (2024) vs 2 025 (2023), +6 % en volume ; le même extrait donne aussi 2 087 : écart non résolu. Source média, pas DGAL.
- Ce que ça dit pour nous : croissance +6 % en nombre de rappels, une seule source non institutionnelle : ne vaut pas preuve de croissance du marché.

## Contre-preuves

### C1 : Le papier et le gratuit suffisent
- Acteur / marché : petits producteurs
- Type : contre-preuve
- Source : https://www.getapp.fr/directory/193/food-traceability/pricing/free/software (extrait de recherche) ; https://www.lhotellerie-restauration.fr/sos-experts/question-reponse/etiquetage-ou-trouver-un-logiciel-gratuit-49724 (extrait)
- Citation : « Étiquetage : où trouver un logiciel gratuit ? » (titre de page)
- Chiffres : offres gratuites existantes (Wherefour, source US, non confirmé en France)
- Ce que ça dit pour nous : la disposition à payer d'un artisan est tirée vers le bas : 0 à 30 €/mois ; un logiciel seul ne passe pas le SOM de 500 k€ sans milliers de clients.

### C2 : Les chambres d'agriculture et Eurofins font le PMS
- Acteur / marché : conseil PMS pour producteurs fermiers
- Type : contre-preuve
- Source : https://www.eurofins.com/fr-fr/analyses-agro-alimentaires/hygiene-alimentaire/conseil/redaction-plan-maitrise-sanitaire/ (extrait) ; https://ardennes.chambre-agriculture.fr/fileadmin/user_upload/Grand-Est/045_Inst_Ardennes/RUB_Techniques/Circuits_courts/Fiche_Produit_-_Ecriture_PMS.pdf (extrait)
- Citation : « tarifs et conditions de vente sur demande » (chambre d'agriculture, synthèse du moteur)
- Chiffres : aucun prix
- Ce que ça dit pour nous : institutions subventionnées occupent déjà la rédaction de PMS ; prix publics absents.

### C3 : Certifications, aucun prix trouvé
- Acteur / marché : IFS, BRC, bio
- Type : contre-preuve (absence de prix)
- Source : https://www.dqsglobal.com/fr/certifier/certification-ifs-food (extrait)
- Citation : « dépend de la taille de l'entreprise et de la complexité des processus » (synthèse du moteur)
- Chiffres : seul chiffre vu = forum UK ancien, environ 1 000 £ (BRC) et 2 500 £ (IFS), rejeté (hors France, daté)
- Ce que ça dit pour nous : zéro prix public pour IFS/BRC/bio en France ; piste non validée à la porte 1.

## Sources non lues
- capterra.com haccpaipro, lafabriquedunet.fr (melba, epackpro, aidopms), getapp (resto-couts), slate.fr : 403 en WebFetch, utilisés en extrait de recherche seulement.
- Pages éditeur (melba/foodmeup.io, ePackPro, Breww, Ekos, Apicbase) : non ouvertes faute de budget ; prix à confirmer.
- Tarifs organismes certificateurs (Ecocert, Kiwa, SGS, DQS) : non trouvés.
- Trustpilot, forums : non cherchés (budget de recherche épuisé).

## Ce qui manque (statut partiel)
- Prix publics affichés des éditeurs de traçabilité/étiquetage pour producteurs (Melba confirmé sur le site, Apicbase, Agrap, etc.).
- Prix des certifications IFS/BRC/bio en France (grilles des organismes).
- Avis négatifs Trustpilot/Capterra FR détaillés avec citations ; EGalim, Nutri-Score, export non couverts.
- Nombre d'entreprises Esane/Insee par taille (seulement Sirene et Bpifrance).
- Aucun client payant identifié nommément.
