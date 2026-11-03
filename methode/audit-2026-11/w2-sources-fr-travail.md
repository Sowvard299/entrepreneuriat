# W2 : catalogue des sources françaises et européennes fiables (5 preuves)

- Mission : établir le catalogue des sources FIABLES (FR + UE) pour prouver (1) taille d'un marché français, (2) croissance (2 sources dont 1 institutionnelle), (3) concentration (part des 3 premiers), (4) argent réellement dépensé par un segment, (5) nombre de clients.
- Date : 2026-11-03
- Recherches web utilisées : 15 / 15 (budget épuisé)
- Preuves : 39 (W2-1 à W2-39) | Domaines distincts : 20, sous-domaines regroupés (ec.europa.eu, insee.fr, banque-france.fr, data.gouv.fr, inpi.fr, copeps.fr, service-public.gouv.fr, echodumardi.com, acteurspublics.fr, statista.com, xerfi.com, businesscoot.com, fevad.com, akto.fr, actuia.com, entreprises.gouv.fr, ademe.fr (data. et librairie.), carenews.com, autoritedelaconcurrence.fr, opendatasoft (BOAMP))
- Plus gros domaine : insee.fr, 5 preuves sur 39 (13 %) ; aucun domaine au-dessus de 40 %.
- Convention : « ouverte » = page lue avec WebFetch ; « extrait » = vue seulement dans un résultat de recherche. Les API ne sont pas testées (le coordinateur les teste).
- Statut : partiel (budget de 15 recherches épuisé ; voir « Manques » en fin de fichier)
- Format d'une fiche (adapté au catalogue) : Source (date, ouverte/extrait) | Citation ≤ 15 mots | Établit | Fiche (organisme, fraîcheur et fréquence, accès, fiabilité, piège, exemple). Les citations viennent du texte rendu par l'outil de lecture (modèle rapide) : à faire confirmer par le vérificateur avant usage chiffré.

---

## Lot 1 : INSEE, Eurostat, DECP

### W2-1 : Eurostat, statistiques structurelles d'entreprises (SBS), vue d'ensemble
- Source : https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Structural_business_statistics_overview (date : « Data extracted in September 2026 », prochaine mise à jour prévue septembre 2027 ; ouverte)
- Citation : « a comprehensive set of basic variables describing business demographics »
- Établit : l'UE publie, par activité NACE Rév. 2 (sections B à N, P à R, S95-S96), le nombre d'entreprises, le chiffre d'affaires, la valeur ajoutée, les personnes employées, les coûts de personnel et l'excédent brut d'exploitation ; ventilation par taille « mostly down to the three-digit (group) level of NACE » ; séries 2021-2024 sous le règlement (UE) 2019/2152.
- Fiche : Eurostat | annuelle, retard d'environ 20 mois (année de référence 2024 extraite en septembre 2026) | gratuit (connaissance générale, non lu sur la page) | officielle | pièges : emploi en nombre de personnes et non en équivalents temps plein ; entreprise classée sur son activité principale ; seules quelques variables ventilées par taille ; la page ne donne aucun chiffre France ; séries EBS démarrent en 2021 (rupture avec l'ancienne SBS : [HYPOTHÈSE], non confirmée par la page) | exemple : jeu de données `sbs_ovw_act` (cité par la page), filtre pays = FR.

### W2-2 : DECP consolidées sur data.gouv.fr (dépense publique par titulaire)
- Source : https://www.data.gouv.fr/fr/datasets/donnees-essentielles-de-la-commande-publique-fichiers-consolides/ (date : page mise à jour le 2026-11-02 ; ouverte)
- Citation : « un fichier unique agrégeant et retraitant les différentes sources »
- Établit : fichier consolidé des marchés publics issu de dix sources (DGFiP, AIFE, Atexo, Dematis...), produit par les ministères économiques et financiers (DAJ) ; depuis le 2024-01-01 les acheteurs publient directement sur data.gouv.fr.
- Fiche : DAJ Bercy | mise à jour très fréquente (la page affiche « Mis à jour hier ») | gratuit, Licence Ouverte 2.0, JSON, 43 fichiers principaux (quelques dizaines de Mo à plus de 1 Go) | officielle mais déclarative | pièges : la page ne documente ni le seuil, ni les champs, ni la qualité (renvoi au dépôt GitHub « decp-arr2022 ») ; seuil et absence de sanction : voir W2-10 | exemple : filtrer par code CPV et SIRET du titulaire pour sommer les montants d'un segment (montant déclaré = montant de marché, pas une facture : [HYPOTHÈSE], non lue sur la page).

### W2-3 : INSEE Ésane 2023, caractéristiques comptables, financières et d'emploi des entreprises
- Source : https://www.insee.fr/fr/statistiques/8611642 (date : 2025-09-18 ; ouverte)
- Citation : « Données 2022 pour comparaison »
- Établit : tableaux par section NAF (bilans, comptes de résultat, chiffres clés, ratios, branches) ; Ésane « disponible au niveau sous-classe (niveau 5) et groupe (niveau 3) » de la NAF rév. 2 ; micro-entrepreneurs 2023 : environ 1,9 million d'unités, 30,0 Md€ de chiffre d'affaires, 20,4 Md€ de valeur ajoutée (valeurs de la page).
- Fiche : INSEE | annuelle, millésime N publié en septembre N+2 (2023 publié le 2025-09-18, soit environ 20 mois) | gratuit (tableaux téléchargeables ; le format Excel n'est pas confirmé par la page lue) | officielle | pièges : « l'évolution du nombre d'entreprises entre 2022 et 2023 est fragile » à cause des micro-entrepreneurs (la page renvoie à la démographie des entreprises) ; comparer N et N-1 seulement avec l'onglet « Données 2022 pour comparaison » ; définition économique de l'entreprise depuis 2017 | exemple : Insee Résultats « Caractéristiques comptables, financières et d'emploi des entreprises en 2023 », tableau « Principales caractéristiques » par section.

### W2-4 : INSEE Ésane, fiches sectorielles 2019 (la maille la plus fine : NAF niveau 5)
- Source : https://www.insee.fr/fr/statistiques/6042002 (date : 2022-02-16 ; ouverte)
- Citation : « Fiches sectorielles - 2019 »
- Établit : une fiche par secteur (Commerce, Transport, Construction et promotion immobilière, Services) avec chiffre d'affaires hors taxes, effectifs en ETP et valeur ajoutée, aux niveaux groupe (3) et sous-classe (5) ; la page signale le secret statistique (« S ») et les données non disponibles (« N »).
- Fiche : INSEE | millésime 2019 publié en 2022, donc périmé pour une taille 2026 ; je n'ai pas trouvé de fiches sectorielles plus récentes (non cherché hors extrait de recherche) | gratuit | officielle | pièges : industrie et finance hors fiches ; cellules « S » (secret) fréquentes sur les petits secteurs ; rupture de définition en 2017 (données 2013-2016 limitées aux plus grands groupes) ; chiffres arrondis | exemple : fiche d'un secteur NAF à 5 caractères (ex. services) pour lire CA HT, ETP, VA.

### W2-5 : INSEE Ésane 2021, rupture de méthode à connaître
- Source : https://www.insee.fr/fr/statistiques/7651565 (date : 2023-09-25 ; ouverte)
- Citation : « cette méthode de calcul est remplacée par une somme simple de l'ensemble des données »
- Établit : au millésime 2021 le calcul des agrégats change ; l'INSEE demande de comparer 2021 avec l'onglet « Données 2020 pour comparaison » ; la forte hausse des prix (énergie, matières premières) combinée aux stocks de fin 2020 perturbe la valeur ajoutée 2021 ; l'emploi vient de la DSN depuis Ésane 2020.
- Fiche : INSEE | annuelle | gratuit | officielle | piège : un taux de croissance « sur 3 ans » calculé en collant des millésimes Ésane est faux ; il faut les couples N / N-1 recalculés par l'INSEE | exemple : onglet « Données 2020 pour comparaison ».

## Lot 2 : indices de CA, démographie, Banque de France, seuil DECP

### W2-6 : INSEE, indice de chiffre d'affaires dans les services (base 2021)
- Source : https://www.insee.fr/fr/metadonnees/source/indicateur/p1725/processus-statistique (date : « Paru le 03/11/2026 » ; ouverte)
- Citation : « Les principales données sources sont les déclarations fiscales mensuelles des entreprises assujetties à la TVA. »
- Établit : la croissance du chiffre d'affaires d'un secteur se lit sur un indice mensuel issu de la TVA, calculé au niveau sous-classe de la NACE sur l'unité légale ; l'indice est un rapport d'évolution sur le même mois de l'année précédente, pas un montant en euros.
- Fiche : INSEE | mensuelle | gratuit (séries BDM, le coordinateur teste l'API) | officielle | pièges : données désaisonnalisées révisées chaque mois depuis 2012 ; points de la crise 2020-2021 neutralisés à la main ; la page ne parle pas des micro-entrepreneurs (hors champ TVA : [HYPOTHÈSE], non confirmée) ; valeur ou volume à préciser (l'inflation gonfle la valeur) | exemple : séries « indice de chiffre d'affaires, services » par NAF dans BDM.

### W2-7 : INSEE, créations d'entreprises (flux, pas stock)
- Source : https://www.insee.fr/fr/statistiques/2015204 (date : « Paru le 16/10/2026 », données jusqu'au T3 2026 ; ouverte)
- Citation : « les créations d’entreprises sont en fait des créations d’unités légales. »
- Établit : sur 4 trimestres glissants (2025-T4 à 2026-T3), 1 278,6 milliers de créations y compris micro-entrepreneurs, dont 427,0 milliers hors micro-entrepreneurs ; champ « France, ensemble des activités marchandes non agricoles » ; source SIDE.
- Fiche : INSEE | trimestrielle (une note mensuelle « Informations rapides » existe selon un extrait de recherche, non ouverte) | gratuit | officielle | pièges : « données peu fiables en 2023 et du 1er au 3e trimestre 2024 » ; unités légales et non entreprises ; c'est un flux, pas le stock d'entreprises vivantes (le stock s'obtient par Sirene/REE) ; la part micro-entrepreneurs (environ 67 %) est un calcul de ma part, non publié | exemple : le tableau « Y compris / Hors micro-entrepreneurs » de la page.

### W2-8 : Banque de France, page « Connaître la situation économique de votre secteur ou région »
- Source : https://www.banque-france.fr/fr/a-votre-service/entreprises/connaitre-situation-economique-secteur-region (date inconnue ; ouverte)
- Citation : « élaborés chaque année à partir de données provenant du Fichier Bancaire des Entreprises (FIBEN) »
- Établit : défaillances d'entreprises mensuelles ventilées par secteur et par taille ; fascicules sectoriels (17 secteurs) ; base BACH (104 secteurs croisés avec 5 catégories de taille, harmonisée au niveau européen, accès par connexion) ; rapports de l'Observatoire des délais de paiement ; données granulaires via le CASD (chercheurs).
- Fiche : Banque de France | mensuelle (défaillances, crédit), annuelle (fascicules, BACH) | fascicules et statistiques en libre accès, BACH sur connexion | officielle | pièges : la page ne cite aucun jeu « chiffre d'affaires » ; fascicules sous forme de ratios, pas de volumes de marché ; aucune part de marché | exemple : lien « Défaillances d'entreprises » lu sur la page, non ouvert : https://www.banque-france.fr/fr/publications-et-statistiques/statistiques?theme%5B7154%5D=7154&sub_theme%5B7155%5D=7155&start-date=&end-date= ; et Webstat https://webstat.banque-france.fr/fr/ (lien lu sur la page, non ouvert).

### W2-9 : Banque de France, fascicules d'indicateurs sectoriels
- Source : https://www.banque-france.fr/fr/publications-et-statistiques/statistiques/fascicules-dindicateurs-sectoriels (date : mise en ligne 2025-11-27, mise à jour 2026-09-24 ; ouverte)
- Citation : « élaborés chaque année à partir de données provenant du Fichier Bancaire des Entreprises »
- Établit : 17 sections NAF (A à S), un fascicule « TOTAL » par section et des fascicules par division ; 30 ratios (activité, rentabilité, équilibre financier) en quartiles et médiane sur deux ans ; millésime majoritairement 2024.
- Fiche : Banque de France | annuelle | gratuit, PDF, aucun Excel mentionné | officielle | pièges : distributions de ratios, pas de montant total de marché ni de concentration ; fascicule par division (2 chiffres), pas par NAF 5 | exemple : fascicule « 75 » (activités vétérinaires, millésime 2025) cité par la page.

### W2-10 : Seuil de déclaration des DECP maintenu à 40 000 € HT, sans sanction
- Source : https://acteurspublics.fr/articles/bercy-clarifie-les-obligations-de-declarations-de-marches-publics-suite-a-la-hausse-des-seuils-marches-publics-bercy-preserve-la-transparence-malgre-le-relevement-des-seuils/ (date : 2026-04-07 ; ouverte)
- Citation : « les réflexions relatives à une éventuelle évolution de ce régime se poursuivront courant 2026 »
- Établit : la DAJ garde le seuil de déclaration à 40 000 € HT (régime normal) et 25 000 € HT (régime simplifié), malgré le relèvement à 60 000 € HT du seuil de dispense de publicité entré en vigueur le 2026-04-01 ; l'obligation est « théorique » faute de sanction ; l'article ne cite aucun article de code (l'article R. 2196-1 n'est donc pas confirmé par cette page).
- Fiche : Acteurs publics (presse spécialisée, cite la DAJ) | événementielle | article d'actualité (accès à vérifier) | professionnelle (presse) | pièges : tous les marchés sous 40 000 € HT sont invisibles ; pas de sanction donc sous-déclaration possible ; un régime pourrait changer en 2026 | exemple : à croiser avec W2-2.

## Lot 3 : comptes déposés (INPI / RNE) et confidentialité

### W2-11 : INPI, environ 45 % des dépôts de comptes avec déclaration de confidentialité
- Source : https://www.inpi.fr/ressources/propriete-intellectuelle/rechercher-une-entreprise-base-entreprises (date : « Publié le 13 mai 2025 », base « mise à jour quotidiennement » ; ouverte)
- Citation : « Environ 1,5 million d'inscriptions par an dont environ 45 % avec déclaration de confidentialité »
- Établit : le teneur officiel du RNE annonce qu'environ 45 % des dépôts annuels de comptes s'accompagnent d'une déclaration de confidentialité ; la base ne contient que les « Comptes annuels non confidentiels déposés » des entreprises commerciales. C'est le chiffre sourcé demandé par le coordinateur.
- Fiche : INPI | quotidienne | DATA INPI (data.inpi.fr renvoie 403 à notre lecteur ; compte requis pour les bilans selon l'extrait W2-16) | officielle | pièges : l'unité est l'« inscription » (un dépôt), pas la société ; ni l'année, ni la définition (confidentialité totale ou du seul compte de résultat) ne sont précisées ; la part varie très probablement avec la taille (voir W2-15) ; la page ne dit pas si l'accès est gratuit | exemple : sur un échantillon de SIREN d'un segment, compter la part sans champ `finances` dans recherche-entreprises.api.gouv.fr pour mesurer le taux de masquage du segment (méthode proposée, non testée ici).

### W2-12 : Copeps reprend la phrase de l'INPI (pas une 2e source)
- Source : https://copeps.fr/actualites/inpi-liste-entreprise/ (date inconnue ; ouverte)
- Citation : « Environ 1,5 million d’inscriptions par an dont environ 45 % avec déclaration de confidentialité. »
- Établit : mot pour mot la phrase de W2-11, sans date ni méthode ; ne compte pas comme source indépendante.
- Fiche : copeps.fr (site de prestataire) | non datée | gratuit | blog / commercial, confiance faible | piège : un chiffre recopié multiplie les URL sans multiplier les preuves.

### W2-13 : service-public, le RNE est le registre unique depuis 2023 et diffuse gratuitement via DATA INPI
- Source : https://entreprendre.service-public.gouv.fr/actualites/A15855?lang=fr&profil=tout (date : 2022-11-30 ; ouverte)
- Citation : « Ces informations seront disponibles en ligne gratuitement sur la plateforme DATA INPI »
- Établit : le RNE devient l'unique organisme d'immatriculation au 2023-01-01 ; droit de dépôt des comptes annuels des sociétés : 5,45 € ; textes cités : décret 2022-1014 du 19 juillet 2022, loi 2019-486 du 22 mai 2019 (PACTE) art. 2, ordonnance 2021-1189 du 15 septembre 2021.
- Fiche : service-public.fr (DILA) | ponctuelle | gratuit | officielle | piège : la page ne dit rien de la confidentialité des comptes (autre source nécessaire, voir W2-15).

### W2-14 : data.gouv.fr, « Comptes et bilans déposés aux greffes » est une archive périmée
- Source : https://www.data.gouv.fr/datasets/comptes-et-bilans-deposes-aux-greffes (date : dernière mise à jour 2023-10-19 ; ouverte)
- Citation : « une archive librement accessible des données opendata diffusées par l'INPI »
- Établit : jeu publié par un tiers (Christian Quest) et non par l'INPI ; la page signale que la fréquence de mise à jour n'est pas respectée (CSV du 2019-10-15, XML du 2023-10-19) ; licence « non spécifiée » dans les métadonnées ; deux fichiers de 34,9 Ko et 1,6 Ko.
- Fiche : data.gouv.fr | gelée | gratuit | non officielle | piège : ne pas s'en servir pour des chiffres d'affaires récents ; passer par DATA INPI ou par recherche-entreprises.api.gouv.fr.

### W2-15 : qui peut masquer ses comptes (article L. 232-25 du code de commerce)
- Source : https://echodumardi.com/juridique/confidentialite-des-comptes-precisions-sur-la-date-de-la-demande-et-les-societes-concernees (date : 2023-09-20 ; ouverte)
- Citation : « doit être effectuée au moment du dépôt des comptes au greffe »
- Établit : micro-entreprises : comptes annuels entiers non publics ; petites entreprises : compte de résultat confidentiel ; moyennes entreprises : bilan et annexe publiés sous forme simplifiée ; les sociétés appartenant à un groupe au sens de l'article L. 233-16 sont exclues de la confidentialité du compte de résultat ; demande impossible après le dépôt (cour d'appel de Paris, 2023-06-06, selon l'article).
- Fiche : L'Echo du Mardi (presse juridique régionale, cite le code de commerce) | ponctuelle | gratuit | professionnelle (le texte de loi est la source primaire : à ouvrir sur Légifrance, non fait ici) | pièges : le CA d'une petite entreprise peut manquer alors que son bilan est public ; les micro-entreprises n'ont aucun chiffre public ; un segment fait de petites structures aura beaucoup de « finances » vides.

### W2-16 : INPI, documentation API et SFTP des comptes annuels (codes de confidentialité)
- Source : https://www.inpi.fr/sites/default/files/2025-06/documentation%20technique%20API_comptes_annuels%20v5.pdf (date : version 5, juin 2025 ; extrait de recherche ; ouverture tentée : PDF compressé illisible)
- Citation : aucune citation vérifiable (PDF illisible) ; contenu rapporté par le résumé de recherche seulement
- Établit (à confirmer) : codes de confidentialité 0 = aucune déclaration, 1 = comptes entièrement confidentiels, 2 = seul le compte de résultat confidentiel, 3 = publication simplifiée, 4 = rapport du commissaire aux comptes confidentiel ; les PDF de comptes assortis d'une déclaration de confidentialité ne figurent pas dans le flux SFTP (doc SFTP v1.0 de mars 2023, https://www.inpi.fr/sites/default/files/Documentation%20technique%20SFTP%20Comptes-annuels%20v1.0%20mars%202023_0.pdf, extrait) ; bilans depuis 2017-01-01 accessibles après connexion ou création de compte (DATA INPI).
- Fiche : INPI | continue | gratuit avec compte (extrait) | officielle | piège : le résumé de recherche note qu'aucune répartition par code n'est publiée ; il faudra la calculer sur les données brutes.

## Lot 4 : classements de croissance, vendeurs d'études, fédération (Fevad)

### W2-17 : Les Echos / Statista, « Champions de la croissance » : conditions et vérification
- Source : https://rankings.statista.com/fr/entreprises-a-la-plus-forte-croissance/classements/entreprises-qui-croissent-le-plus-en-france/participation/ (date : édition à publier en février 2027 ; la page annonce aussi une fenêtre d'inscription du 2027-07-07 au 2027-11-06, dates contradictoires entre elles ; ouverte)
- Citation : « Les données de revenus sont vérifiées par un formulaire de confirmation signé »
- Établit : édition en cours : croissance du CA de 2022 à 2025, CA 2022 ≥ 100 k€ et CA 2025 ≥ 1,5 M€, entreprise indépendante, croissance principalement organique ; CA = chiffre d'affaires net hors TVA ; inscription et inclusion gratuites ; vérification = formulaire signé par le dirigeant, le directeur financier ou un membre du comité exécutif ; la page ne mentionne ni comptes déposés ni attestation d'expert-comptable.
- Fiche : Statista pour Les Echos | annuelle | inscription gratuite (lecture du classement final : non vérifiée) | commerciale (média + vendeur de données) | pièges : chiffres déclarés par les entreprises et contrôlés par une signature, pas par les comptes déposés ; classement fondé sur l'inscription, donc couverture non garantie exhaustive [HYPOTHÈSE, à confirmer dans la méthodologie] ; seuil ≥ 1,5 M€ en fin de période écarte les très petites ; la croissance d'une entreprise n'est pas celle de son marché | exemple : repérer des entreprises qui croissent vite dans un segment (signal de demande), jamais la taille ni la croissance du marché.

### W2-18 : Champions de la croissance, méthodologies 2023-2025 (extrait, PDF redirigés)
- Source : https://r.statista.com/wp-content/uploads/20250106_Champions-de-la-croissance_2025_Methodologie.pdf (date : 2025-01-06 d'après le nom du fichier ; extrait de recherche ; ouverture tentée : redirection 301 vers https://rankings.statista.com/en/, document non lu)
- Citation : aucune (document non lu)
- Établit (extrait, à confirmer) : édition 2025 : croissance annuelle moyenne du CA 2020-2023, entreprises indépendantes, seuil d'entrée 9,70 % ; édition 2024 : 2019-2022, seuil 9,35 % ; édition 2023 : CA ≥ 100 k€ en 2018, croissance surtout interne ; la FAQ 2025 (https://r.statista.com/wp-content/uploads/LesEchos_Champions2025_FAQ_FR.pdf, redirigée aussi) dirait que les organisateurs peuvent modifier les critères et faire des exceptions.
- Fiche : Statista | annuelle | PDF désormais inaccessibles au lecteur | commerciale | piège : les méthodologies des éditions passées ne s'ouvrent plus ; archiver le PDF de l'édition utilisée avant de citer.

### W2-19 : Xerfi, fiche d'étude « Marché nomenclaturé France » (prix et méthode visibles)
- Source : https://www.xerfi.com/presentationetude/Le-negoce-de-machines-outils_21NEG13 (date : « dernière mise à jour le 31/03/2026 » ; ouverte)
- Citation : « exploitent les derniers chiffres et enquêtes disponibles »
- Établit : 990 € HT, 199 pages (réf. 26NEG13), PDF ; taille du marché en valeur (1,66 Md€ en 2024) donnée comme « nos estimations » ; prévisions 2026-2027 ; données financières sur 170 opérateurs avec ratios « mis à jour chaque mois » ; ni Insee, ni enquête, ni panel nommés sur la page ; classements annoncés mais aucune part de marché chiffrée visible.
- Fiche : Xerfi (groupe privé) | mise à jour datée sur la fiche | payant, 990 € HT | commerciale, confiance faible pour une taille seule | pièges : estimations propriétaires non reproductibles ; méthode non publiée sur la page publique ; parts des 3 premiers non visibles avant achat | exemple : n'acheter que pour la liste d'opérateurs et leurs ratios, et recalculer la taille avec Ésane (W2-3).

### W2-20 : Xerfi, grille de prix des collections
- Source : https://xerfi.com/presentation-collections (date inconnue ; ouverte)
- Citation : « Avec notre méthode exclusive BMS© »
- Établit : prix HT : Focus marché 1 500 à 2 200 € ; Marché nomenclaturé France 990 € ; Étude stratégique 2 490 à 3 300 € ; Comex Briefing 6 200 € (cliniques vétérinaires, 39 pages) ; la méthode n'est décrite que pour les études sur mesure (BMS©) ; fréquence de mise à jour non indiquée.
- Fiche : Xerfi | non indiquée | payant | commerciale | piège : un chiffre de croissance Xerfi est une prévision de l'éditeur, pas une série observée.

### W2-21 : Xerfi, accueil et offre sur mesure (Precepta non confirmée)
- Source : https://www.xerfi.com/ et https://www.xerfi.com/en/xerfi-specific (date inconnue ; ouvertes)
- Citation : « plus de 1000 études actualisées et 30 ans d'expertise »
- Établit : abonnement « IA à toutes nos études » sans tarif affiché ; étude sur mesure sur devis (« Exprimez votre besoin ») ; ni Precepta, ni Previsis, ni MCI, ni Spécific ne sont nommées sur ces deux pages. Un profil tiers vu en extrait de recherche décrit Xerfi Precepta comme la marque d'analyse concurrentielle de Xerfi : non vérifié, URL du profil rouverte en 404.
- Fiche : Xerfi | non précisée | payant sur devis | commerciale | piège : « Precepta » ne se trouve pas comme offre autonome sur xerfi.com ; ne pas chiffrer son prix sans devis.

### W2-22 : Businesscoot, ressources déclarées pour ses études
- Source : https://www.businesscoot.com/en/page/the-resources-used-for-our-sector-studies (date inconnue ; ouverte)
- Citation : « The references in each study identify the evidence used. »
- Établit : sources déclarées : instituts statistiques nationaux, Eurostat, douanes, institutions internationales, presse professionnelle, rapports d'entreprises, associations professionnelles ; la page ne mentionne ni comptes déposés, ni panels, ni calcul des tailles et parts de marché (elle renvoie à une page « méthodologie » non lue).
- Fiche : Businesscoot (éditeur d'études en ligne) | mises à jour « en continu » selon l'éditeur (extrait de recherche, déclaration non vérifiée) | payant | commerciale, confiance faible | piège : sans acheter l'étude, on ne voit pas les références qui permettent de vérifier le chiffre.

### W2-23 : Businesscoot, prix d'un pack (extrait, page rouverte en 404)
- Source : https://www.businesscoot.com/en/study/le-marche-de-la-croisiere-france (extrait de recherche ; rouverte le 2026-11-03 : HTTP 404)
- Citation : « 5 études au prix de 75,6€HT par étude »
- Établit (extrait) : pack de 5 études à 75,60 € HT chacune, valable 12 mois, à choisir parmi environ 800 titres du catalogue France ; le nombre de titres varie selon les pages (800, 1 200, 1 500) ; pas d'abonnement mensuel trouvé ; à reconfirmer sur businesscoot.com.
- Fiche : Businesscoot | annuelle (crédits 12 mois) | payant, très bas prix | commerciale | piège : prix bas, mais études de 30 à 40 pages seulement (déclaration de l'éditeur) : à traiter comme une orientation, jamais comme une preuve de taille.

### W2-24 : Statista Market Insights, méthodologie officielle
- Source : https://statista.com/outlook/methodology (date inconnue ; ouverte)
- Citation : « approximates but does not reflect reality »
- Établit : chaque marché a son modèle (descendant, ascendant ou mixte) ; tailles en valeur et en prix courants (« Statista Market Insights data is presented in current, or nominal, prices ») ; prévisions sur 5 ans (ARIMA, courbe de Bass, lissage exponentiel) ; mises à jour au moins deux fois par an ; les séries passées peuvent changer d'une mise à jour à l'autre ; les tailles varient selon le périmètre.
- Fiche : Statista | au moins 2 fois par an | payant (grille tarifaire France introuvable en 15 recherches) | commerciale | pièges : croissance en prix courants, donc inflation incluse ; chiffre modélisé et non observé ; non reproductible sans l'accès ; le résumé de recherche note un recours à des sources tierces (Banque mondiale, YouGov, GfK, Kantar : extrait non vérifié) | exemple : n'utiliser qu'en contre-vérification d'un ordre de grandeur.

### W2-25 : Fevad, communiqué des chiffres clés 2026 (e-commerce France, données 2025)
- Source : https://www.fevad.com/ledition-2026-des-chiffres-cles-du-e-commerce/ (date : 2026-07-01 ; ouverte)
- Citation : « plusieurs instituts partenaires »
- Établit : 2025 : 196,4 Md€ (+7 %), ventes de produits +4 %, services +9 % ; 3,2 milliards de transactions (+11 %) ; plus de 158 000 sites marchands actifs ; 42,2 millions de cyberacheteurs ; part d'environ 12 % du commerce de détail ; sources : « principaux acteurs du marché », panels de consommateurs et instituts partenaires non nommés.
- Fiche : Fevad (fédération professionnelle) | annuelle (juillet) et bilans trimestriels | gratuit | professionnelle | pièges : méthode et périmètre « services » non définis ; la Banque de France et Médiamétrie ne sont pas citées par ce communiqué ; une fédération a intérêt à montrer la croissance de son secteur ; ne pas confondre l'Europe (911 Md€ en 2025, +7 %, titre de l'accueil fevad.com) et la France | exemple : bon pour le nombre de sites marchands actifs (clients B2B identifiables) et la tendance, à croiser avec Ésane / ICA pour la taille.

### W2-26 : Fevad, page « Chiffres clés du e-commerce 2026 »
- Source : https://www.fevad.com/chiffres-cles-ecommerce-2026/ (date : document daté du 2026-07-01 ; ouverte)
- Citation : « Chiffres Clés du e-commerce 2026 : les données de référence du marché en France »
- Établit : compilation (« best of ») de baromètres et d'études de la Fevad ; la page n'affiche aucun chiffre ; les chiffres viennent du service Études de la Fevad ou d'instituts partenaires non nommés ; téléchargement gratuit après formulaire ; les adhérents ont accès à l'ensemble des données.
- Fiche : Fevad | annuelle | gratuit avec formulaire, détail réservé aux adhérents | professionnelle | piège : le PDF n'a pas été ouvert ici ; le détail méthodologique reste à lire dans le document.

## Lot 5 : nombre de clients, observatoires de branche, études ministérielles, concentration, commande publique

### W2-27 : Urssaf, établissements employeurs et effectifs salariés (nombre de clients B2B)
- Source : https://www.data.gouv.fr/datasets/60ecd87888636149e7decb05 (date : dernière mise à jour 2026-05-29 ; ouverte)
- Citation : « Un établissement peut donc être dénombré avec 0 salarié »
- Établit : jeu « Nombre d'établissements employeurs et effectifs salariés du secteur privé, par département x grand secteur x tranche d'effectif (au 31/12 depuis 2006) » ; champ : établissements employeurs du secteur privé relevant du régime général ; annuel, mise à jour « fin d'année + ~150 jours » ; licence ODbL.
- Fiche : Urssaf | annuelle | gratuit (le coordinateur teste l'API Open Urssaf) | officielle | pièges documentés : apprentis inclus depuis la publication de juin 2023 (rupture) ; bascule vers la DSN 2015-2021 peut causer des révisions de niveau ; une entreprise individuelle n'est comptée que si elle verse une masse salariale (les micro-entrepreneurs sans salarié sont absents) ; données brutes non désaisonnalisées ; maille « grand secteur », pas NAF 5 ; compte des établissements et non des entreprises | exemple : dénombrer les établissements employeurs d'un grand secteur par tranche d'effectif et par département.

### W2-28 : API Recherche d'entreprises, limites documentées
- Source : https://www.data.gouv.fr/dataservices/672cf684c3488a0c533f7094 (date : RNE « mis à jour le 11 août 2026 », Sirene « mis à jour aujourd'hui » ; ouverte ; redirigée depuis api.gouv.fr)
- Citation : « ne permet pas d'accèder aux données complètes de la base Sirene »
- Établit : limite de débit « 7 appels / seconde » (réductible en cas de surcharge) ; exclus : prédécesseurs et successeurs d'établissements, entreprises non diffusibles, entreprises refusées au RCS ; la page ne mentionne ni les données financières, ni les comptes confidentiels, ni la pagination (renvoi à recherche-entreprises.api.gouv.fr/docs/, non ouvert).
- Fiche : DINUM / Insee / INPI | quotidienne | gratuit, sans clé | officielle | pièges : un décompte par API sous-estime les entreprises non diffusibles ; la présence ou non du champ `finances` dépend des comptes publics (voir W2-11, W2-15) | exemple : voir recette du chercheur.

### W2-29 : AKTO, observatoire de branche (exemple d'OPCO)
- Source : https://observatoire.akto.fr/ (date inconnue, publications 2024-2026 ; ouverte)
- Citation : aucune citation fiable (résumé de l'outil de lecture en anglais)
- Établit : l'observatoire couvre 20 branches (propreté, déchets, hôtels-cafés-restaurants, travail temporaire, enseignement privé...) avec portraits statistiques, panoramas, études prospectives ; sources : DSN déposée auprès de l'Urssaf et consolidée par France compétences, traitée par AKTO, plus les fichiers de formation d'AKTO ; exercice le plus récent : 2024, panorama 2025 (extraction juillet 2025) ; exemple de lien : https://observatoire.akto.fr/content/uploads/sites/3/2026/10/Panorama-statistique-Activite-Dechet-Excercie-2026.pdf (non ouvert).
- Fiche : OPCO AKTO | annuelle | gratuité non précisée sur la page (PDF en libre téléchargement) | professionnelle (OPCO, financé par les cotisations de branche) | pièges : les PDF testés (panorama propreté 2024) sont des fichiers à flux compressés illisibles par notre lecteur ; périmètre = branche conventionnelle (IDCC), pas secteur NAF ; ne donnent ni CA ni parts de marché.

### W2-30 : portraits de branche, nombre d'entreprises employeuses (extrait)
- Source : https://observatoire.akto.fr/content/uploads/sites/3/2026/02/Proprete-et-services-Panorama-statistique-Exercice-2024-Synthese.pdf (date : février 2026 d'après le chemin du fichier ; extrait de recherche ; ouverture tentée : PDF illisible)
- Citation : aucune vérifiable (extrait de recherche : « En 2023, la branche compte 14 680 entreprises employant au moins 1 salarié au 31/12 »)
- Établit (extrait, à confirmer) : le portrait de branche de la Dares comptait 14 680 entreprises employant au moins un salarié dans la propreté au 31/12/2023 (13 830 en 2022) ; le résumé de recherche note que les chiffres d'entreprises et d'effectifs varient selon la source (Dares, Acoss/Urssaf, fichier OPCO) et la date de référence (31/12 ou moyenne annuelle).
- Fiche : Dares / OPCO | annuelle | gratuit | officielle (Dares) et professionnelle (OPCO) | piège : trois sources donnent trois chiffres pour la même branche ; toujours citer source et date.

### W2-31 : Bpifrance Le Lab, enquêtes d'opinion de dirigeants (site illisible : 403)
- Source : https://www.actuia.com/actualite/etude-de-bpifrance-le-lab-lutilisation-des-ia-generatives-par-les-dirigeants-de-pme-tpe-est-encore-tres-limitee/ (date inconnue ; extrait de recherche) ; site d'origine https://lelab.bpifrance.fr (HTTP 403 à l'ouverture)
- Citation : aucune vérifiable (extrait de recherche)
- Établit (extrait) : Le Lab publie des enquêtes d'opinion auprès de dirigeants : IA générative (enquête en ligne du 2023-11-16 au 2023-12-05 auprès de 40 000 dirigeants de PME-TPE), « Climat des affaires ou affaire de climat » (1 006 dirigeants), inspiration (plus de 400 dirigeants) ; la méthode de l'édition 2026 sur la solitude des dirigeants n'a pas été trouvée.
- Fiche : Bpifrance (banque publique) | irrégulière | gratuit (PDF) | officielle / institutionnelle | piège : ce sont des opinions et des pratiques de dirigeants (signal de demande ou de douleur), pas des tailles de marché ni des dépenses ; échantillons auto-déclarés.

### W2-32 : DGE (entreprises.gouv.fr), page des publications : peu de tailles de marché
- Source : https://www.entreprises.gouv.fr/la-dge/publications (date : listing du 2026-10-12 au plus récent ; ouverte)
- Citation : aucune (résumé de l'outil de lecture)
- Établit : la DGE publie « Les Thémas de la DGE », rapports, guides pratiques, dossiers ; classement par secteur (Industrie, Numérique, Tourisme, Commerce-artisanat-restauration, Services marchands) ; la page ne contient aucun chiffre de taille de marché, seulement des parts et variations dans les résumés ; Pipame n'est pas une rubrique visible de cette page.
- Fiche : DGE (Bercy) | irrégulière | gratuit | officielle | piège : études de politique publique, rarement des tailles de marché chiffrées en euros ; chaque étude doit être ouverte pour sa note méthodologique.

### W2-33 : ADEME, jeu de données ouvert « Marchés et emplois concourant à la transition énergétique »
- Source : https://data.ademe.fr/datasets/etude-marches-et-emplois (date : jeu actualisé le 2025-11-03, étude parue en octobre 2025 ; ouverte)
- Citation : « Pour éviter les doubles comptes cinq filières sont à exclure du calcul »
- Établit : marchés en M€ et emplois directs en ETP par filière (29 filières, 630 enregistrements, série depuis 2006, situation 2021-2023 en « estimation préliminaire »), licence ouverte, mise à jour annuelle ; exploitation-maintenance des transports terrestres non estimée ; hypothèses par filière « disponibles sur demande ».
- Fiche : ADEME | annuelle | gratuit, licence ouverte | officielle (établissement public) | pièges : doubles comptes à éliminer à la main ; dernier millésime préliminaire ; limité aux filières de la transition énergétique ; méthode détaillée seulement sur demande.

### W2-34 : ADEME, librairie, étude édition 2025
- Source : https://librairie.ademe.fr/energies/8707-marches-et-emplois-concourant-a-la-transition-energetique-edition-2025.html (date : mise en ligne 2025-10-25 ; ouverte)
- Citation : « calculée sur la base des premières données et informations disponibles »
- Établit : étude suivie depuis 2008, plus de trente filières, trois secteurs ; sources citées : ADEME, SDES, Observ'ER, Uniclima, Eurostat, Insee, Enedis, CCFA, AVERE et fédérations professionnelles ; 8 PDF dont une méthodologie générale ; trajectoire à l'horizon 2028 alignée sur la PPE2 et la SNBC.
- Fiche : ADEME | annuelle | gratuit avec adresse courriel et lien de confirmation | officielle | piège : trajectoire 2028 = objectif de politique publique, pas une prévision de marché ; recouper avec des chiffres observés.

### W2-35 : ADEME 2022 : 113 Md€ et 421 300 emplois (relayé par la presse, communiqué ADEME en 403)
- Source : https://www.carenews.com/carenews-info/news/l-ademe-recense-421-000-emplois-lies-a-la-transition-energetique-en-france (date : 2024-09-25 ; ouverte) ; communiqué d'origine https://www.ademe.fr/presse/communique-national/transition-energetique-en-france-un-marche-qui-depasse-les-100-milliards-deuros (HTTP 403 à l'ouverture)
- Citation : « plus de 113 milliards d’euros »
- Établit : pour 2022, chiffre d'affaires de plus de 113 Md€ (+41 % par rapport à 2020) et 421 300 emplois directs en ETP (+24 %) ; transports terrestres 50,3 Md€, bâtiments résidentiels 16,7 Md€, énergies renouvelables et de récupération 34,2 Md€.
- Fiche : Carenews (média) relayant l'ADEME | annuelle | gratuit | presse (source primaire : ADEME) | piège : l'article ne renvoie pas à l'étude ; chiffre à reprendre depuis W2-33 / W2-34 plutôt que depuis la presse.

### W2-36 : Autorité de la concurrence, liste des décisions de contrôle des concentrations
- Source : https://www.autoritedelaconcurrence.fr/fr/liste-de-controle-des-concentrations (date : consultée le 2026-11-03, décisions publiées du 2026-10-07 au 2026-11-02 en première page ; ouverte)
- Citation : « Rechercher une décision de contrôle des concentrations rendue par l'Autorité de la concurrence depuis 2009 »
- Établit : 4 112 décisions depuis 2009 (206 pages de 20) ; filtres : 21 secteurs, type d'opération, sens de la décision, phase ; la page de liste n'affiche aucune part de marché ; numérotation 26-DCC-213 au 2026-11-02.
- Fiche : Autorité de la concurrence | continue | gratuit | officielle | piège : une décision ne porte que sur une opération notifiée ; le secteur affiché par le lecteur est déduit de la mise en page.

### W2-37 : Autorité de la concurrence, seuils et procédure de notification
- Source : https://www.autoritedelaconcurrence.fr/fr/controle-des-concentrations (date : 2026-11-03 ; ouverte)
- Citation : « 25 jours ouvrés maximum »
- Établit : conditions cumulatives : chiffre d'affaires mondial des parties supérieur à 250 M€, chiffre d'affaires France supérieur à 80 M€ pour au moins deux d'entre elles, pas de compétence UE (seuils plus bas pour le commerce de détail et l'outre-mer) ; environ 70 % des dossiers en procédure simplifiée (environ 3 semaines) ; la page ne dit rien de la publication des parts de marché ; un projet de loi de simplification 2026 relèverait les seuils.
- Fiche : Autorité de la concurrence | continue | gratuit | officielle | piège : un marché sans fusion importante n'a aucune décision ; les petits marchés (sous les seuils) sont invisibles ; seuils susceptibles de monter en 2026.

### W2-38 : Autorité de la concurrence, exemple de page de décision (26-DCC-209)
- Source : https://www.autoritedelaconcurrence.fr/fr/decision-de-controle-des-concentrations/relative-la-prise-de-controle-exclusif-des-societes-deret (date : 2026-10-28 ; ouverte)
- Citation : « Décision simplifiée : Oui »
- Établit : la page de décision est une fiche de synthèse (secteurs « Services » et « Transports », phase 1) sans part de marché, sans taille de marché et sans concurrents nommés ; le texte intégral n'y figure pas (autre document à chercher).
- Fiche : Autorité de la concurrence | continue | gratuit | officielle | piège : les parts de marché des 3 premiers ne se lisent pas sur la fiche ; elles se trouvent, s'il y en a, dans le texte intégral de la décision, souvent après coupe du secret des affaires [HYPOTHÈSE, non vérifiée dans ce travail].

### W2-39 : BOAMP, jeu de données ouvert des avis (annonces, pas dépenses)
- Source : https://boamp-datadila.opendatasoft.com/explore/dataset/boamp/information/ (date inconnue ; ouverte)
- Citation : « Le jeux de données des avis du boamp.fr »
- Établit : jeu ouvert des avis du BOAMP, licence etalab-2.0 ; la page rendue par notre lecteur ne donne ni nombre d'enregistrements, ni champs, ni fréquence, ni producteur explicite.
- Fiche : DILA (site de la DILA listé sur la page) | non indiquée | gratuit | officielle | piège : un avis d'appel d'offres prouve une intention d'achat, pas une dépense ; seuls les avis d'attribution portent un titulaire ; documentation à lire sur l'API avant usage.

---

## Sources non lues (URL + raison)
- https://lelab.bpifrance.fr : HTTP 403.
- https://data.inpi.fr : HTTP 403 (donc accès aux bilans non vérifié par nous).
- https://www.economie.gouv.fr/daj/observatoire-economique-de-la-commande-publique : HTTP 403 (recensement économique annuel de la commande publique non lu).
- https://www.ademe.fr/presse/communique-national/transition-energetique-en-france-un-marche-qui-depasse-les-100-milliards-deuros : HTTP 403.
- https://www.inpi.fr/sites/default/files/2025-06/documentation%20technique%20API_comptes_annuels%20v5.pdf et la documentation SFTP : PDF à flux compressés illisible.
- https://observatoire.akto.fr/content/uploads/sites/3/2026/02/Proprete-et-services-Panorama-statistique-Exercice-2024-Synthese.pdf : PDF illisible.
- https://www.francecompetences.fr/app/uploads/2026/09/Note-detude-N°14-OPMQ-VF-Copy.pdf : HTTP 404.
- https://r.statista.com/... (méthodologies 2024 et 2025, FAQ, page ranking 2024) : redirection 301 vers https://rankings.statista.com/en/.
- https://www.businesscoot.com/en/study/le-marche-de-la-croisiere-france et https://businesscoot.com/en/company/xerfi-groupe : HTTP 404 à la réouverture.
- https://www.insee.fr/fr/statistiques/documentation/imet143.pdf (Insee Méthodes n° 143, juin 2023) : vu en extrait, non ouvert.
- https://webstat.banque-france.fr/fr/ et https://www.bach.banque-france.fr/#/login : liens lus sur une page de la Banque de France, non ouverts (BACH demande une connexion).
- https://info.gouv.fr/upload/media/organization/0001/01/sites_default_files_contenu_piece-jointe_2016_09_dossier_de_synthese_-_etude_pipame.pdf : document Pipame de 2016 vu en extrait, trop ancien, non ouvert.
- Légifrance, article L. 232-25 du code de commerce : non ouvert (cité via W2-15).

## Manques (statut : partiel)
- Taux de confidentialité par secteur ou par taille : seule la moyenne INPI (environ 45 % des dépôts, W2-11) est sourcée ; la répartition par code (0 à 4) est dans une documentation illisible.
- Grille de prix Statista pour la France et définition de la marque Precepta : introuvables.
- Stock d'entreprises Insee (REE / démographie annuelle) : page non trouvée en budget.
- Pipame : aucune étude récente ouverte ; BOAMP : champs non documentés par la page lue.
- Recensement économique de la commande publique (OECP) : bloqué (403).
- Parts de marché d'une décision de concentration : non vérifiées dans un texte intégral.


