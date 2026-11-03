# S2 : 88.10 aide à domicile et 38.11 collecte de déchets non dangereux (porte 1)

- Mission : moteur de croissance, sous-segments qui encaissent, faiblesses, modèle étranger, angle et test de précommande.
- Date : 2026-11-03. Recherches web utilisées : 10 sur 12.
- Preuves : 24. Domaines distincts : 14 (data.economie.gouv.fr, bodacc, recherche-entreprises.api.gouv.fr, ec.europa.eu, sec.gov, solidarites.gouv.fr, legifrance.gouv.fr, ecologie.gouv.fr, nievre.fr, weka.fr, trustpilot.com, buurtzorgnederland.com, 3rdanjou.fr, linfodurable.fr). Aucun domaine au-dessus de 40 % (trustpilot 4/24).
- Citations (verifier-citations.py, après correction de S2-5) : RÉSUMÉ final OK=9, ABSENT=1 (S2-5 : l'expression « tarif plancher de 22 € par heure » est bien sur la page lue par curl et WebFetch, mais le script ne la retrouve pas à cause d'espaces insécables mal décodés ; faux négatif probable), BLOQUE=2 (S2-9 et S2-18 : Trustpilot renvoie 403 au script, mais les pages ont été lues par WebFetch le 2026-11-03 ; non rejouable par script). Les autres preuves sont des données outil sans citation.
- Statut : partiel. Manque : CA sur plusieurs années par acteur (l'API ne renvoie que la dernière année déposée), donc croissance des acteurs non mesurée, seule la croissance sectorielle (fiches) l'est ; 3 prix publics N2 en collecte non atteints (2 prix N2 + 1 N3) ; CA audité Buurtzorg non trouvé (« déclaré » absent) ; plancher national 2026 non lu sur page ouverte (sources CNSA en erreur de certificat).

## Chiffres de cadrage (outil, N1)
Fiches : `fiche-88.10.md` (4 482 M€ en 2024, +13,9 %/an 2021-2024, top 3 12,3 %) et `fiche-38.11.md` (3 989 M€, INSEE +5,9 %/an 2022-2025, top 3 29,9 %). Non refaits.

## A. 88.10 Aide à domicile

### S2-1 : Marchés publics « aide à domicile » (DECP)
- Acteur / marché : collectivités qui achètent de l'aide à domicile
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22aide+%C3%A0+domicile%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DECP, data.economie.gouv.fr)
- Citation : aucune (donnée outil)
- Chiffres : 2023 : 39 marchés 14,7 M€ ; 2024 : 40, 14,9 M€ ; 2025 : 80, 16,8 M€ ; 2026 : 14, 3,4 M€ (plancher, ≥ 40 000 € HT)
- Ce que ça dit pour nous : le marché public direct est petit (≈ 17 M€) ; le payeur dominant passe par l'APA, pas par appels d'offres.

### S2-2 : Acteurs 88.10A avec CA déposé
- Acteur / marché : SAAD prestataires seniors, payeurs ménages + départements (APA)
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=88.10A&etat_administratif=A&ca_min=20000000&per_page=25 (date : 2026-11-03 ; niveau N1 ; émetteur : Insee Sirene / comptes déposés)
- Citation : aucune (donnée outil)
- Chiffres : Accès SAP 298,1 M€ (2024, résultat net 0,13 M€) ; Vitalliance 160,7 M€ (2023, résultat 7,3 M€) ; Unipros 90,7 M€ (2024, 0,28 M€) ; Domusvi Domicile 71,4 M€ (2025, 1,4 M€) ; Bien à la Maison (Onela) 57,0 M€ (2025, 0,16 M€) ; Domalliance 38,9 M€ (2024, 0,37 M€). Marges nettes 0,04 % à 4,5 %. Une seule année par acteur : croissance par acteur non mesurée.
- Ce que ça dit pour nous : ≥ 3 acteurs avec CA déposé, mais rentabilité très faible chez les gros.

### S2-3 : Acteur en perte, AVS Besançon
- Acteur / marché : aide à domicile (88.10A)
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=750510075 (date : 2026-11-03 ; niveau N1 ; émetteur : comptes déposés)
- Citation : aucune (donnée outil)
- Chiffres : CA 38,0 M€ (2024), résultat net -8,0 M€
- Ce que ça dit pour nous : un acteur de 38 M€ perd 21 % de son CA ; l'échelle ne protège pas.

### S2-4 : Procédures collectives liées à l'aide à domicile (BODACC)
- Acteur / marché : services d'aide à domicile
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22aide+%C3%A0+domicile%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : BODACC, DILA)
- Citation : aucune (donnée outil)
- Chiffres : 252 annonces en 2022 ; 327 en 2023 ; 436 en 2024 ; 428 en 2025 ; 347 sur 2026 en cours. Plein texte, annonces multiples par entreprise. Hausse de 70 % 2022-2024 pendant que le CA sectoriel monte.
- Ce que ça dit pour nous : le secteur croît mais les défaillances aussi ; le moteur n'enrichit pas les petits acteurs.

### S2-5 : Moteur 1, tarif plancher national et financement départemental
- Acteur / marché : départements (APA/PCH) paient les SAAD ; tarif plancher national
- Type : obligation
- Source : https://solidarites.gouv.fr/financement-des-services-domicile-de-nouveaux-outils-pour-les-gestionnaires-et-les-departements (date : 2022 ; niveau N2 ; émetteur : ministère des Solidarités)
- Citation : « tarif plancher »
- Chiffres : 22 €/h au 1er janvier 2022, dotation qualité par CPOM, LFSS 2022 ; décret n° 2022-735 du 28 avril 2022
- Ce que ça dit pour nous : cause datée de la hausse du CA : plancher national et dotation payés par les départements. Valeur 2026 (25,00 €) vue seulement dans l'arrêté Nièvre/Savoie (voir S2-6).

### S2-6 : Prix publics 2026 fixés par arrêté départemental (Nièvre)
- Acteur / marché : SAAD habilités, tarif horaire APA, département de la Nièvre
- Type : argent dépensé
- Source : https://nievre.fr/shared-files/56913/ (date : 2026-07-17 ; niveau N2 ; émetteur : conseil départemental de la Nièvre) ; https://nievre.fr/shared-files/57565/ ; https://nievre.fr/shared-files/57564/
- Citation : « Tarif horaire moyen annuel »
- Chiffres : 26,35 €/h (SAAD Cœur de Nièvre), 25,40 €/h (Morvan), 25,59 €/h (Lucenay-les-Aix), exercice 2026. Trois prix publics. Coût de revient estimé à 25 € en 2022 par le ministère (non relu sur page ouverte, donc non retenu).
- Ce que ça dit pour nous : prix administré à ≈ 25-26 €/h ; la marge se fait sur le coût salarial, pas sur le prix.

### S2-7 : Plafond de hausse des prix 2026 pour les services non habilités
- Acteur / marché : services autonomie à domicile non habilités à l'aide sociale
- Type : obligation
- Source : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053228211 (date : 2025-12-23 ; niveau N1 ; émetteur : JORF, Légifrance)
- Citation : « ne peuvent augmenter de plus de 2 % en 2026 »
- Chiffres : plafond +2 % en 2026, art. L. 347-1 CASF ; arrêté du 23 décembre 2025
- Ce que ça dit pour nous : le prix est encadré par la loi ; un angle « prix » est impossible, l'angle est le service et la dotation qualité.

### S2-8 : Autorisation obligatoire des SAAD
- Acteur / marché : création d'un SAAD intervenant auprès de bénéficiaires APA/PCH
- Type : obligation
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049392047 (date : 2024-04-10 ; niveau N1 ; émetteur : Légifrance, art. L313-1 CASF)
- Citation : « l'autorisation est accordée pour une durée de quinze ans »
- Chiffres : autorisation du président du conseil départemental (art. L. 313-1-1 et L. 313-1, loi 2024-317 du 8 avril 2024) ; décret 2025-747 du 1er août 2025 sur les conditions techniques. Délai : non établi.
- Ce que ça dit pour nous : sans autorisation, pas d'accès aux financements APA ; le mode mandataire/déclaré (sans APA) reste possible mais n'est pas lu ici [HYPOTHÈSE].

### S2-9 : Avis négatifs Petits-fils (aide à domicile, payeur ménages)
- Acteur / marché : agence mandataire, seniors, ménages (crédit d'impôt 50 %)
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.petits-fils.com (date : 2026-09-30 ; niveau N3 ; émetteur : Trustpilot)
- Citation : « Les heures durent 40 minutes et certaines auxiliaires ne viennent pas en l'annonçant »
- Chiffres : note 3,4/5, 213 avis, 56 % de 1-2 étoiles (page filtrée) ; autres avis 2026 : « Gros turn over, beaucoup d'absences, souvent de dernière minute. » (2026-08-30)
- Ce que ça dit pour nous : plaintes sur absences, turn-over, durée réelle : canal unique (Trustpilot), à croiser.

### S2-10 : Plaintes publiques, Cour des comptes juillet 2026
- Acteur / marché : SAAD, offre et qualité
- Type : plainte
- Source : https://www.weka.fr/actualite/aide-a-domicile/article/aide-a-domicile-la-cour-des-comptes-invite-a-simplifier-la-reforme-des-sad-217750/ (date : 2026-08-03 ; niveau N3 ; émetteur : WEKA, commentant la Cour des comptes du 2026-07-08)
- Citation : « imparfaitement »
- Chiffres : ≈ 9 000 SAAD ; listes d'attente, refus, ruptures, plans d'aide partiellement réalisés ; contrôles publics jugés insuffisants ; recommande d'abandonner la tarification administrée (délégation aux départements dès 2027)
- Ce que ça dit pour nous : l'offre est rationnée par le recrutement : la demande dépasse l'offre. Risque : changement de régime de tarification en 2027 (contre-preuve).

### S2-11 : Modèle étranger, Buurtzorg (Pays-Bas)
- Acteur / marché : soins et aide à domicile par équipes autogérées, payeur assurance
- Type : tendance
- Source : https://www.buurtzorgnederland.com/assets/Bestanden/d1741ff61f/2025-Kwaliteitsbeeld-Buurtzorg-Nederland-1.pdf (date : 2025 ; niveau N2 ; émetteur : Buurtzorg Nederland)
- Citation : « zelfsturende teams die zelf verantwoordelijkheid nemen »
- Chiffres : overhead 6,7 % des coûts contre 16,9 % en benchmark ; NPS clients 83,8 % contre 54,8 % (déclaré par l'entreprise) ; > 70 000 clients (extrait de recherche non ouvert, non retenu). CA audité : non établi.
- Ce que ça dit pour nous : cause de succès = équipes de quartier autogérées, peu d'encadrement ; en France l'autorisation et le tarif départemental imposent d'autres règles.

## B. 38.11 Collecte de déchets non dangereux

### S2-12 : Acteurs 38.11Z avec CA déposé (grands)
- Acteur / marché : collecte DNDAE et ménagers, payeurs collectivités et entreprises
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=38.11Z&etat_administratif=A&ca_min=100000000&per_page=25 (date : 2026-11-03 ; niveau N1 ; émetteur : comptes déposés)
- Citation : aucune (donnée outil)
- Chiffres : Sepur 484,5 M€ (2025, résultat 7,1 M€) ; Coved 434,3 M€ (2024, 9,3 M€) ; Pizzorno 274,5 M€ (2025, 23,8 M€) ; Nicollin 225,0 M€ (2025, 10,6 M€) ; Grandjouan 188,5 M€ (2024, 1,0 M€). Une année par acteur.
- Ce que ça dit pour nous : marché de gros acteurs rentables (2 à 9 %) ; les nouveaux entrants se placent sur des niches.

### S2-13 : Marchés publics « collecte déchets » et « biodéchets » (DECP)
- Acteur / marché : collectivités acheteuses de collecte
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22collecte+d%C3%A9chets%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DECP)
- Citation : aucune (donnée outil)
- Chiffres : « collecte déchets » : 2022 130 marchés 368,7 M€ ; 2023 257, 746,8 M€ ; 2024 1 044, 1 924,3 M€ ; 2025 1 420, 4 401,2 M€ (valeur maximale des accords-cadres, pas des factures). « biodéchets » : 2023 48 marchés 142,6 M€ ; 2024 247, 377,7 M€ ; 2025 230, 172,8 M€.
- Ce que ça dit pour nous : le payeur public est massif (centaines de marchés) ; la hausse vient aussi d'une meilleure déclaration, à prendre avec prudence.

### S2-14 : Moteur 2, obligation de tri à la source des biodéchets
- Acteur / marché : tous les producteurs ou détenteurs de biodéchets (restaurants, commerces, entreprises, collectivités)
- Type : obligation
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041627130 (date : version en vigueur 2026-11-03 ; niveau N1 ; émetteur : Légifrance, art. L541-21-1 Code de l'environnement)
- Citation : « Au plus tard le 31 décembre 2023, cette obligation s'applique à tous les producteurs ou détenteurs de biodéchets »
- Chiffres : généralisation au 1er janvier 2024 (confirmé par https://www.ecologie.gouv.fr/biodechets, N2, « tous les professionnels et particuliers »). Sanction : non trouvée sur la page ministère.
- Ce que ça dit pour nous : cause datée et légale de la demande en collecte de biodéchets ; l'application réelle par contrôle reste à établir.

### S2-15 : Acteurs spécialisés biodéchets, CA déposé et pertes
- Acteur / marché : collecte de biodéchets restaurateurs et professionnels, vélo ou camion
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=moulinot%20compost%20biogaz (date : 2026-11-03 ; niveau N1 ; émetteur : comptes déposés) ; https://recherche-entreprises.api.gouv.fr/search?q=les%20alchimistes
- Citation : aucune (donnée outil)
- Chiffres : Moulinot Compost & Biogaz 10,9 M€ (2024), résultat -2,4 M€ ; Moulinot Nouvelle-Aquitaine 1,4 M€, -1,0 M€ ; Moulinot Pays de la Loire 0,27 M€, -1,0 M€ ; Les Alchimistes 6,4 M€ (2024), -1,9 M€ ; Recygo (38.32Z, tri bureaux) 19,4 M€ (2024), -0,8 M€
- Ce que ça dit pour nous : la demande existe (≥ 3 acteurs avec 6 à 19 M€) mais tous perdent de l'argent : la collecte spécialisée n'est pas encore rentable. Contre-preuve forte.

### S2-16 : Prix public, collecte biodéchets professionnels (3RD'Anjou, prestataire Les Alchimistes)
- Acteur / marché : biodéchets professionnels, bac 120 L
- Type : argent dépensé
- Source : https://www.3rdanjou.fr/media/guide-des-pro-2-plis-roules-a4-v2026.pdf (date : 2026 ; niveau N2 ; émetteur : communauté de communes 3RD'Anjou)
- Citation : « Forfait annuel pour un bac 120L »
- Chiffres : forfait annuel bac 120 L 35 € si déjà client du service, +92 € sinon ; coût par échange de bac 23 € (15 € dès le 2e bac) ; engagement 3 mois minimum. Symbole € absent de l'extraction PDF, montants lus en clair.
- Ce que ça dit pour nous : 23 € l'échange est un prix public réel ; à 1 échange par semaine ≈ 1 200 €/an/bac [calcul à partir de 52 × 23, non sourcé comme usage].

### S2-17 : Prix payé par un restaurateur parisien
- Acteur / marché : Moulinot, restaurants Paris
- Type : argent dépensé
- Source : https://www.linfodurable.fr/conso/des-dechets-des-restaurants-parisiens-transformes-en-compost-et-en-methane-29719 (date : 2021-11-24 ; niveau N3 ; émetteur : L'Info durable)
- Citation : « 17 euros la collecte par semaine »
- Chiffres : 17 €/semaine (témoignage d'un chef) ; environ 1 600 restaurants clients en Île-de-France (2021, déclaré)
- Ce que ça dit pour nous : second prix de marché : 17 à 23 € par collecte, soit 900 à 1 200 €/an par site.

### S2-18 : Avis négatifs Paprec (collecte pro)
- Acteur / marché : gros collecteur, clients professionnels
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.paprec.com (date : 2026-04-29 ; niveau N3 ; émetteur : Trustpilot)
- Citation : « Celles ci n’étant pas du tout bachées, de nombreux papiers et cartons s’envolaient »
- Chiffres : note 2,6/5 sur 9 avis seulement, 78 % de 1 étoile ; Veolia : 3,9/5, 3 738 avis, ≈ 30 % de 1-2 étoiles (https://fr.trustpilot.com/review/www.veolia.com, 2025-11-28)
- Ce que ça dit pour nous : échantillon trop petit (9 avis) pour conclure ; faiblesse non prouvée en collecte pro. Canal unique.

### S2-19 : Procédures collectives liées à la collecte de déchets (BODACC)
- Acteur / marché : collecte de déchets
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22collecte+d%C3%A9chets%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : BODACC, DILA)
- Citation : aucune (donnée outil)
- Chiffres : 263 annonces en 2021 ; 314 en 2022 ; 346 en 2023 ; 414 en 2024 ; 464 en 2025 ; 447 sur 2026 en cours. Plein texte, annonces multiples ; « biodéchets » : 1 annonce en 2023.
- Ce que ça dit pour nous : défaillances en hausse de 76 % entre 2021 et 2025 malgré la croissance du CA.

### S2-20 : Modèle étranger, Rubicon (États-Unis), place de marché de collecte
- Acteur / marché : plateforme numérique reliant clients et transporteurs de déchets
- Type : contre-preuve
- Source : https://data.sec.gov/api/xbrl/companyfacts/CIK0001862068.json (date : 2023-03-23 ; niveau N1 ; émetteur : SEC EDGAR, 10-K Rubicon Technologies)
- Citation : aucune (donnée outil)
- Chiffres : revenus 583,1 M$ (2021), 675,4 M$ (2022) ; résultat net -73,2 M$ (2021), -281,8 M$ (2022) (audité)
- Ce que ça dit pour nous : un modèle numérique de collecte a atteint 675 M$ de CA mais perd plus de 40 % ; la plateforme seule ne crée pas de marge.

### S2-21 : Taille et croissance, double source
- Acteur / marché : 88.10 et 38.11
- Type : tendance
- Source : https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=FR&geo=FR&nace_r2=Q8810&indic_sbs=NETTUR_MEUR (date : 2026-11-03 ; niveau N1 ; émetteur : Eurostat)
- Citation : aucune (donnée outil)
- Chiffres : 88.10 : 3 032 M€ (2021) à 4 482 M€ (2024), +13,9 %/an, valeur, inflation comprise. 38.11 : Eurostat +19,9 %/an 2021-2024 (3 989 M€), INSEE ICA +5,9 %/an 2022-2025 (fiche). Pour 88.10 aucune série INSEE : un seul chiffre institutionnel (Eurostat).
- Ce que ça dit pour nous : 88.10 : croissance à 2 sources non remplie ; 38.11 : deux sources institutionnelles concordent sur > 5 %.

## C. Angles, croyance fragile, test de précommande (non des preuves, des propositions)

### S2-22 : Angle 88.10, équipes de quartier autogérées pour seniors payeurs ménages [HYPOTHÈSE]
- Acteur / marché : aide à domicile prestataire privée, ménages avec crédit d'impôt 50 % (S2-9)
- Type : tendance
- Source : voir S2-9, S2-10, S2-11
- Citation : aucune
- Chiffres : Pareil que Petits-fils/Shiva/Domidom (ménages, prix libre mais plafonné +2 % si non habilité, S2-7), mais équipes fixes de 6 à 10 auxiliaires par quartier (continuité, cf. Buurtzorg). Ressources : autorisation CASF art. L. 313-1 si APA visée (15 ans, appel à projet : délai et coût non établis) ; capital de démarrage [HYPOTHÈSE] : trésorerie salariale 2 à 3 mois, soit ≈ 30 000 à 60 000 € pour 10 auxiliaires ; compétences : encadrement médico-social.
- Croyance la plus fragile : les familles paieront plus (ou resteront) pour la continuité des intervenants, alors que le prix est encadré et le recrutement rationné (S2-10).
- Test légal : page « liste d'attente avec dépôt remboursable de 50 € » pour un quartier précis, avec mention que le service n'est pas encore ouvert et une date d'ouverture (L.121-2, L.221-5) ; seuil écrit avant : ≥ 20 dépôts sur 1 000 visiteurs ciblés (2 %) en 30 jours, ou ≥ 10 dépôts pour un budget pub ≤ 1 500 € [HYPOTHÈSE de seuil].
- Ce que ça dit pour nous : angle sérieux seulement si le recrutement d'auxiliaires peut être résolu ; sinon le goulot est l'offre, pas la demande.

### S2-23 : Angle 38.11, collecte de biodéchets de petits producteurs en zone mal couverte [HYPOTHÈSE]
- Acteur / marché : restaurants, traiteurs, petits commerces non desservis par un service public ; Moulinot, Alchimistes, services publics (S2-15, S2-16, S2-17)
- Type : tendance
- Source : voir S2-14 à S2-17
- Citation : aucune
- Chiffres : prix de marché 17 à 23 € par collecte, soit ≈ 900 à 1 200 €/an par site ; hypothèse de 150 sites pour couvrir un camion → CA ≈ 135 000 à 180 000 € [calcul à partir de S2-16/17, nombre de sites HYPOTHÈSE]. Ressources : véhicule de collecte, contrat avec une installation de compostage ou méthanisation, déclaration de transporteur de déchets (code de l'environnement, art. R. 541-50 et s., non relu) ; capital ≈ 50 000 à 150 000 € [HYPOTHÈSE].
- Croyance la plus fragile : un collecteur peut faire un résultat positif alors que les trois acteurs spécialisés perdent 1 à 2,4 M€ (S2-15).
- Test légal : page de précommande « service non ouvert, démarrage à 60 jours dans la ville X » avec acompte remboursable de 25 € et rétractation de 14 jours (L.221-18) ; seuil : ≥ 15 acomptes sur 100 restaurateurs ciblés par courrier, [HYPOTHÈSE de seuil].
- Ce que ça dit pour nous : l'obligation légale crée la demande ; les comptes des acteurs montrent que le prix actuel ne couvre pas les coûts. Piste à prudence élevée.

### S2-24 : Qualité des preuves de prix en collecte
- Acteur / marché : 38.11
- Type : contre-preuve
- Source : https://conseils.hellopro.fr/quel-est-le-prix-d-une-benne-a-dechet-grand-volume-1562.html (date : 2026-11 ; niveau N4 ; émetteur : Hellopro, annonceur B2B)
- Citation : « se situe souvent entre 500 et 1 200 € »
- Chiffres : location benne 8 m3 : 150 / 250 / 400 € (min/moyen/max) ; 15 m3 : 300 / 550 / 800 € (HT, 7 jours, indicatif, N4)
- Ce que ça dit pour nous : seule fourchette trouvée pour les bennes, niveau N4 : ne sert pas à un score ; segment bennes de chantier non couvert en N2.

## Sources non lues
- https://www.cnsa.fr/sites/default/files/2026-01/Tarifs-APA-1er-janvier-2026.pdf : erreur de certificat ; la valeur 25,00 € du plancher 2026 n'est donc pas retenue.
- https://www.cnsa.fr/sites/default/files/2026-06/PUB-CNSA-CC2026-WEB-ACCESS.pdf : idem (832 100 bénéficiaires APA à domicile lus localement, non vérifiable).
- https://www.apef.fr (grilles tarifaires agences 2026) : URL avec espaces renvoyant 404.
- https://www.savoie.fr/web/sw_171309/... : scan OCR, illisible.
- https://www.fhf.fr/sites/default/files/2026-08/Synth%C3%A8seFHF-RapportCCptesSAD_juillet2026.pdf et rapport Cour des comptes : non ouverts.
- Trustpilot Domidom (3 avis) : échantillon trop petit ; Trustpilot Moulinot : 404.
- Prix de bennes de chantier : seulement N4.
