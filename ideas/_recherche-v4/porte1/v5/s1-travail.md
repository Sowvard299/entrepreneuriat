# S1 : 96.01 Blanchisserie-teinturerie et 33.12 Réparation de machines (porte 1)

Date : 2026-11-03. Recherches web utilisées : 12 sur 12 (3 de ces 12 sans résultat exploitable). Statut : partiel.
Chiffres de taille, croissance, effectifs, top 3 : voir `fiche-96.01.md` et `fiche-33.12.md` (N1, non refaits).
Limite API : `recherche-entreprises` ne renvoie que le dernier exercice déposé dans `finances` : pas de CA par année
pour les acteurs (impossible d'établir qui croît acteur par acteur). Voir « Manques ».
Preuves : 24 ; domaines distincts : 14 (Trustpilot 3 preuves sur 24, 12 %).
RÉSUMÉ du vérificateur de citations : OK=9, ABSENT=0, BLOQUE=3, EXTRAIT=0. Les 3 BLOQUE (S1-6, S1-9, S1-24) sont des pages Trustpilot en 403 pour curl ; elles ont été lues par WebFetch le 2026-11-03, citations copiées de cette lecture.

## Partie A : 96.01 Blanchisserie-teinturerie

### S1-1 : Location-entretien de linge et vêtements (acteurs)
- Acteur / marché : Netexial, Les Lavandières, Mewa, Bardusch ; location-entretien de linge plat et vêtements, B2B
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=343234142 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API, pas de texte)
- Chiffres : CA déposé Netexial 308,6 M€ (2025, résultat 21,9 M€) ; Les Lavandières 227,7 M€ (2025, résultat 27,7 M€) ; Mewa 95,8 M€ (2025, résultat 17,1 M€) ; Bardusch 27,4 M€ (2025, résultat -1,0 M€). Un seul exercice par entité.
- Ce que ça dit pour nous : le modèle encaisse à grande échelle, mais les trois premiers sont des groupes industriels hors de portée directe.

### S1-2 : Linge des résidents d'EHPAD (Bulle de Linge)
- Acteur / marché : Bulle de Linge, entretien du linge personnel des résidents, structures d'hébergement de personnes fragiles
- Type : argent dépensé
- Source : https://www.bulledelinge.com (date : 2026-11-03 ; niveau N2 ; émetteur : Bulle de Linge) ; CA : https://recherche-entreprises.api.gouv.fr/search?q=493485924 (N1)
- Citation : « plus de 75.000 résidents dans 950 établissements »
- Chiffres : CA 40,1 M€ (2025), résultat 3,3 M€ ; 12 unités de production ; aucun tarif ni délai publié.
- Ce que ça dit pour nous : un sous-segment B2B récurrent existe et est rentable ; prix non publics, donc prix publics à trouver ailleurs.

### S1-3 : Autres acteurs du linge de santé (segment non vérifié)
- Acteur / marché : Kalhyge 1, Anett Deux, AD3 ; activité 96.01A, segment client [HYPOTHÈSE : santé et collectivités, non ouvert]
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=971503578 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : Kalhyge 1 65,7 M€ (2024, résultat -1,3 M€) ; Anett Deux 48,1 M€ (2025, résultat 4,5 M€) ; AD3 33,1 M€ (2024, résultat 3,1 M€).
- Ce que ça dit pour nous : au moins 3 acteurs à 30-65 M€ en 96.01A ; leur segment exact reste à confirmer.

### S1-4 : Pressing grand public : 5àsec, CA et résultat
- Acteur / marché : 5ASEC R I F, pressing B2C, Île-de-France
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=418782025 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : CA 38,3 M€ (2025), résultat net -4,8 M€.
- Ce que ça dit pour nous : le plus connu des pressings perd de l'argent sur son entité franciliennne : le B2C pressing est fragile.

### S1-5 : Prix publics 5àsec
- Acteur / marché : 5àsec, magasin Paris Vaugirard
- Type : argent dépensé (prix affichés)
- Source : https://www.5asec.fr/fr/magasin/paris-vaugirard-falguiere/ (date : 2026-11-03 ; niveau N2 ; émetteur : 5àsec)
- Citation : aucune (prix lus dans la page ouverte, pas de citation textuelle conservée)
- Chiffres : chemise 4,70 € ; manteau 14,60 € ; couette synthétique 25,50 € ; linge au kilo lavé-repassé-plié 14,60 €.
- Ce que ça dit pour nous : un prix public N2 pour le linge au kilo : 14,60 € le kilo repassé.

### S1-6 : Avis 5àsec
- Acteur / marché : 5àsec, B2C
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.5asec.fr (date : 2026-10-31 ; niveau N2 ; émetteur : Trustpilot)
- Citation : « Ma parka a été abimé lors du nettoyage, elle m’a coûté 495€ ! »
- Chiffres : 446 avis ; 41 % de 1-2 étoiles (37 % + 4 %). Autre avis : « 25€ la couette, avec EN PLUS la facturation du sac plastique »
- Ce que ça dit pour nous : dommages et prix mal perçus chez le leader B2C ; canal unique (Trustpilot).

### S1-7 : Laundryheap France, prix et délais (location de linge court séjour)
- Acteur / marché : Laundryheap, location de draps et serviettes pour hôtes
- Type : argent dépensé (prix affichés)
- Source : https://www.laundryheap.com/fr-fr/linen (date : 2026-11-03 ; niveau N2 ; émetteur : Laundryheap)
- Citation : « livraison le lendemain dans la plupart des régions »
- Chiffres : jeu draps et serviettes à partir de 14,95 € + TVA par jeu ; livraison gratuite dans tout Paris.
- Ce que ça dit pour nous : prix public N2 par rotation ; J+1 est la norme à battre.

### S1-8 : Laundryheap France perd de l'argent (contre-preuve) et maison mère britannique
- Acteur / marché : Laundryheap France (WAST), 62.01Z au registre ; Laundryheap Limited (Royaume-Uni)
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=laundryheap (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE) ; https://find-and-update.company-information.service.gov.uk/search/companies?q=laundryheap (N1)
- Citation : « Incorporated on 29 August 2014 »
- Chiffres : France : CA 2,2 M€ (2025), résultat -0,3 M€, créée 2023-05-25. Royaume-Uni : société n° 09193151, comptes consolidés 2025 déposés le 2026-10-02 (CA non lu : document non ouvert).
- Ce que ça dit pour nous : le modèle logistique à la demande n'est pas rentable à Paris au bout de 2 ans ; CA audité étranger non établi.

### S1-9 : Avis Laundryheap (Royaume-Uni)
- Acteur / marché : Laundryheap, B2C et B2B
- Type : plainte
- Source : https://www.trustpilot.com/review/laundryheap.com (date : 2026-11-02 ; niveau N2 ; émetteur : Trustpilot)
- Citation : « There is literally NO CUSTOMER SUPPORT processes. »
- Chiffres : 14 453 avis ; 16 % de 1-2 étoiles ; plaintes : chauffeurs indisponibles, articles perdus ou abîmés.
- Ce que ça dit pour nous : la faiblesse type est la fiabilité logistique et le support.

### S1-10 : Prix de location de linge court séjour (comparatif)
- Acteur / marché : Elis, LocLinge, Easy Linge pour hôtes Airbnb
- Type : argent dépensé (prix déclarés)
- Source : https://www.minut.com/fr/blog/prix-location-draps-airbnb-quelles-solutions (date : 2026-01-26 ; niveau N4 ; émetteur : Minut, blog)
- Citation : « contactez leur service client pour demander un devis »
- Chiffres : Elis 25-40 € par séjour (estimation) ; LocLinge 25-35 € ; Easy Linge 20-30 € (non sourcés).
- Ce que ça dit pour nous : fourchette 20-40 € par séjour, confiance faible (N4).

### S1-11 : Prix d'un prestataire francilien (Buanderie Saisonnière)
- Acteur / marché : Buanderie Saisonnière, entretien de linge d'hôtes
- Type : argent dépensé (prix déclarés)
- Source : https://rentaplus.immo/blog/blanchisserie-airbnb-prix/ (date : 2026-09 ; niveau N4 ; émetteur : Rentaplus, blog)
- Citation : « 26 € HT par rotation »
- Chiffres : entretien 26 € HT par rotation ; location avec entretien 47 € HT par rotation ; « à confirmer par devis ».
- Ce que ça dit pour nous : prix par rotation 26 à 47 € HT, mais N4 et prestataire absent du registre Sirene (recherche par nom).

### S1-12 : Marchés publics de blanchisserie et de linge (DECP)
- Acteur / marché : collectivités, hôpitaux, EHPAD
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22blanchisserie%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DECP)
- Citation : aucune (donnée API)
- Chiffres : « blanchisserie » : 20 marchés en 2022, 233 en 2024 (797,8 M€, valeur maximale d'accords-cadres, probable valeur aberrante), 275 en 2025 (215,5 M€) ; « linge » : 514 marchés en 2025 (1 580 M€). Hausse en partie due à une meilleure déclaration [HYPOTHÈSE].
- Ce que ça dit pour nous : la commande publique de blanchisserie est réelle ; les montants sont des plafonds.

### S1-13 : Procédures collectives, blanchisserie et pressing (BODACC)
- Acteur / marché : secteur
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22blanchisserie%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DILA)
- Citation : aucune (donnée API)
- Chiffres : « blanchisserie » : 243 annonces en 2022, 270 en 2023, 285 en 2024, 311 en 2025 ; « pressing » : 229 en 2022, 254 en 2025. Plein texte, plusieurs annonces par entreprise.
- Ce que ça dit pour nous : les annonces remontent depuis 2022 : le secteur croît en valeur mais des entreprises tombent.

### S1-14 : Le leader Elis grandit moins vite que l'indice du secteur
- Acteur / marché : Elis (groupe), location-entretien
- Type : contre-preuve
- Source : https://bourse.fortuneo.fr/actualites/elis-confirmation-des-objectifs-2026-8415332 (date : 2026-07-29 ; niveau N3 ; émetteur : Fortuneo, reprise du communiqué Elis)
- Citation : « Au 1er semestre 2026, le chiffre d'affaires ressort à 2,457 MdsE (+4,9% dont +3,2% en organique) »
- Chiffres : groupe +3,2 % en organique au S1 2026 ; détail France et par marché non lu (rapport en PDF illisible).
- Ce que ça dit pour nous : l'indice INSEE +8,3 %/an inclut les prix ; la croissance en volume du leader est bien plus faible.

### S1-15 : Moteur hôtelier : fréquentation en hausse modérée
- Acteur / marché : hôtels, clients des blanchisseries
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/8739138 (date : 2026 ; niveau N1 ; émetteur : INSEE)
- Citation : « Au quatrième trimestre 2025, la fréquentation des hébergements collectifs touristiques hors campings est en hausse de 2,2 % »
- Chiffres : hôtels T4 2025 : 48,7 M de nuitées, +2,1 % ; 2025 : 220,2 M de nuitées, 14 886 hôtels (https://www.insee.fr/fr/statistiques/2015412). Aucune donnée sur les meublés de tourisme obtenue.
- Ce que ça dit pour nous : la demande hôtelière progresse de 2 % ; l'écart avec +8,3 % est probablement du prix [inférence non démontrée].

### S1-16 : Easy Linge existe mais sans comptes déposés
- Acteur / marché : Easy Linge, location de linge
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=easy%20linge (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : SIREN 824360275, 96.01B, créée 2016-11-30, pas de CA déposé.
- Ce que ça dit pour nous : les petits acteurs de la location courte durée n'ont pas de CA lisible : la preuve d'argent y reste à N4.

## Partie B : 33.12 Réparation de machines et équipements mécaniques

### S1-17 : Froid commercial et cuisine : acteurs avec CA
- Acteur / marché : Paris Froid Services, Froid & Services Méditerranée, Azur Trucks Froid, BV Services (BV Froid), Froid Equipement Service ; dépannage et maintenance du froid, B2B
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=33.12Z&etat_administratif=A&ca_min=5000000&ca_max=100000000&per_page=25&page=1 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : Paris Froid Services 20,3 M€ (2025, +0,5 M€) ; Froid & Services Méditerranée 13,2 M€ (2024, +1,0 M€) ; Azur Trucks Froid 11,5 M€ (2025, -1,3 M€) ; BV Services 7,6 M€ (2024) ; Froid Equipement Service 6,2 M€ (2024). Dalkia Froid Solutions 226,6 M€ (fiche).
- Ce que ça dit pour nous : au moins 5 acteurs régionaux à 6-20 M€ avec résultat faible mais positif : marché fragmenté.

### S1-18 : Hydraulique et flexibles : acteurs avec CA
- Acteur / marché : Chrono Flex, Hydro Maintenance, Hydro Europe Service, Hydrofluid Technologies, Technic Hydro ; B2B BTP, agricole, industrie
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=33.12Z&etat_administratif=A&ca_min=5000000&ca_max=100000000&per_page=25&page=1 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : Chrono Flex 67,1 M€ (2025, +3,5 M€) ; Hydro Maintenance 19,3 M€ (2025) ; Hydro Europe Service 10,5 M€ (2025) ; Hydrofluid Technologies 9,1 M€ (2025) ; Technic Hydro 6,7 M€ (2025).
- Ce que ça dit pour nous : 5 acteurs avec CA ; Chrono Flex rentable à 5 % de marge.

### S1-19 : Manutention et pesage : acteurs avec CA
- Acteur / marché : Bretagne Manutention, Accu Manutention Services, Precia Molen Service, Ademi Pesage
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=33.12Z&etat_administratif=A&ca_min=5000000&ca_max=100000000&per_page=25&page=1 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : Bretagne Manutention 114,4 M€ (2024, fiche) ; Precia Molen Service 61,4 M€ (2025) ; Ademi Pesage 15,2 M€ (2025) ; Accu Manutention Services 10,3 M€ (2024).
- Ce que ça dit pour nous : sous-segments rentables et régionaux ; prix publics absents.

### S1-20 : Pénurie de frigoristes (recherche active de main-d'œuvre)
- Acteur / marché : installation et maintenance en froid, employeurs
- Type : recherche active
- Source : https://travail-industrie.com/emploi/metiers-en-tension/techniciens-et-agents-de-maitrise-en-installation-et-maintenance-en-froid-et-conditionnement-d-air (date : 2026 ; niveau N3 ; émetteur : travail-industrie.com, reprise de l'enquête BMO France Travail)
- Citation : « 81 % jugés difficiles »
- Chiffres : 2 950 projets de recrutement en 2026 ; 81 % jugés difficiles contre 43 % tous métiers ; Île-de-France 516 projets, 84 %.
- Ce que ça dit pour nous : la rareté de techniciens est la cause plausible de délais longs ; à confirmer sur la source France Travail.

### S1-21 : Prix déclarés d'intervention hydraulique
- Acteur / marché : dépannage de flexibles hydrauliques sur site
- Type : argent dépensé (prix déclarés)
- Source : https://conseils.hellopro.fr/combien-coute-la-reparation-de-flexible-hydraulique-4832.html (date : 2026-11 ; niveau N4 ; émetteur : Hellopro, marketplace)
- Citation : « Le tarif horaire se situe généralement entre 72 € et 83 € »
- Chiffres : atelier 60-240 € ; sur site 180-420 € ; avec recherche de panne 360-720 € ; astreinte 348-840 € ; HT.
- Ce que ça dit pour nous : fourchettes de prix, confiance faible ; ce ne sont pas 3 prix publics de vendeurs N2.

### S1-22 : Commande publique de maintenance
- Acteur / marché : collectivités, cantines, établissements
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22maintenance+%C3%A9quipements+de+cuisine%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DECP)
- Citation : aucune (donnée API)
- Chiffres : maintenance équipements de cuisine : 7 marchés en 2022, 163 en 2025 (41,1 M€) ; maintenance chambres froides : 23 marchés en 2025 (9,5 M€), 18 en 2026 (20,4 M€) ; maintenance chariots élévateurs : 11 marchés en 2025 (2,6 M€) ; flexibles hydrauliques : 14 marchés en 2025 (1,5 M€). Hausse en partie due à une meilleure déclaration [HYPOTHÈSE].
- Ce que ça dit pour nous : le froid et la cuisine collective achètent de la maintenance, en volume croissant.

### S1-23 : Procédures collectives, maintenance industrielle et froid (BODACC)
- Acteur / marché : secteur
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22maintenance+industrielle%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DILA)
- Citation : aucune (donnée API)
- Chiffres : « maintenance industrielle » : 287 annonces en 2020, 343 en 2023, 458 en 2025 ; « froid commercial » : 168 en 2022, 325 en 2025 ; « frigoriste » : 14 à 18 par an.
- Ce que ça dit pour nous : les annonces montent en 2024-2025 : signal de défaillances à surveiller.

### S1-24 : Avis d'un frigoriste (contre-preuve de faiblesse)
- Acteur / marché : Azur Froid, dépannage climatisation et froid
- Type : contre-preuve
- Source : https://fr.trustpilot.com/review/www.azur-froid.fr (date : 2026-06-26 ; niveau N2 ; émetteur : Trustpilot)
- Citation : « Excellente réactivité suite à panne de climatisation en pleine période de canicule. »
- Chiffres : note 4,0 ; 5 avis, tous à 5 étoiles ; l'entreprise n'a pas invité ses clients à noter.
- Ce que ça dit pour nous : Trustpilot ne documente pas les faiblesses du B2B de réparation : aucune plainte trouvée.

## Questions de la mission

### 1. Moteur de la croissance
- 96.01 : indice INSEE +8,3 %/an (fiche, N1). Le leader Elis fait +3,2 % en organique (S1-14) et les nuitées hôtelières +2,1 % (S1-15) : la croissance du secteur est surtout en valeur (prix), cause non démontrée. Segments qui tirent : non établi ; les pistes sont l'hébergement de résidents (S1-2) et la commande publique (S1-12). CA par année par acteur : non établi (API).
- 33.12 : indice INSEE +5,0 %/an (fiche). Tirage plausible : maintenance externalisée dans le froid et la cuisine collective (S1-22) avec pénurie de techniciens (S1-20). Cause datée par un texte de loi (règlement UE sur les gaz fluorés) : non établie, page EUR-Lex et Légifrance non lues.

### 2. Sous-segments × modèles
- 96.01 : location-entretien B2B (S1-1) ; linge de résidents (S1-2, S1-3) ; linge de location courte durée (S1-7, S1-10, S1-11) ; pressing B2C (S1-4 à S1-6).
- 33.12 : froid commercial et cuisine (S1-17) ; hydraulique et flexibles (S1-18) ; manutention et pesage (S1-19).
- Prix publics N2 trouvés : 96.01 : 5àsec (S1-5) et Laundryheap (S1-7) seulement 2 ; 33.12 : aucun (S1-21 est N4).

### 3. Faiblesses
- 96.01 : dommages et prix (S1-6, 41 % de 1-2 étoiles), fiabilité logistique (S1-9), BODACC en hausse (S1-13).
- 33.12 : pénurie de techniciens (S1-20), BODACC en hausse (S1-23) ; avis non exploitables (S1-24). Délais : non établis.

### 4. Modèle étranger
- 96.01 : Laundryheap (Royaume-Uni), CA audité non lu (comptes déposés, document non ouvert) ; la filiale française perd de l'argent (S1-8). Ne « fait pas mieux » : contre-preuve.
- 33.12 : non établi (une recherche, uniquement des annuaires et annonces de cession, N5 écartés).

### 5. Angles, croyance, test, ressources
- Angle 96.01 : linge de rotation pour hôtes et conciergeries hors Paris, J+1, prix fixe par rotation (26-47 € HT, S1-11, N4).
  - Croyance la plus fragile : une densité de clients suffisante par tournée pour couvrir la logistique (c'est ce qui perd de l'argent chez Laundryheap, S1-8).
  - Test : page de précommande avec date de livraison et dépôt remboursable (cadre légal du CLAUDE.md : L.221-14, L.221-18). Seuil à écrire avant : sur 10 conciergeries ou hôtels ciblés par trafic payant ou démarchage, au moins 3 précommandes payées d'un mois [HYPOTHÈSE de seuil, à recalculer avec le prix et le coût par contact].
  - Ressources : capital avant le premier euro, sous-traitance du lavage à une blanchisserie existante : [HYPOTHÈSE] quelques milliers d'euros (véhicule, contenants) ; atelier propre : rubrique ICPE de blanchisserie, seuil à vérifier [HYPOTHÈSE] ; compétences : logistique de tournée ; délai : [HYPOTHÈSE] 2 à 3 mois.
- Angle 33.12 : abonnement de maintenance préventive du froid pour restaurants et commerces indépendants avec délai d'intervention garanti, en s'appuyant sur des techniciens indépendants.
  - Croyance la plus fragile : des restaurateurs paient un forfait annuel pour un délai garanti ; et la capacité à recruter ou sous-traiter des frigoristes (S1-20).
  - Test : dépôt remboursable sur contrat annuel, seuil écrit avant : au moins 3 contrats sur 10 restaurants contactés [HYPOTHÈSE de seuil].
  - Ressources : attestation de capacité pour fluides frigorigènes et assurance professionnelle (article de loi à citer par l'auditeur, non lu) ; véhicule et outillage [HYPOTHÈSE de coût non chiffrée, aucune source] ; capital non établi.

## Manques (Statut : partiel)
- CA par année des acteurs (API limitée au dernier exercice) : non établi.
- Prix publics N2 : 96.01 deux sur trois ; 33.12 zéro.
- Segment exact de Kalhyge, Anett, AD3 ; CA audité Laundryheap UK ; modèle étranger en 33.12.
- Texte de loi gaz fluorés et obligations de froid : EUR-Lex vide, Légifrance 404.
- Délais constatés des acteurs : aucune source.

## Sources non lues
- https://fr.elis.com/sites/fr.elis.com/files/2026/07/30/Elis%20-%20Rapport%20financier%20semestriel%202026.pdf : PDF compressé illisible
- https://www.optionfinance.fr/info-financiere-en-continu/d/2026-07-29-elis-confirme-ses-objectifs-2026-apres-un-bon-premier-semestre.html : 403
- https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R0573 : contenu vide
- https://find-and-update.company-information.service.gov.uk/company/09193151/filing-history : comptes non ouverts (CA non lu)
- https://annuaire-entreprises.data.gouv.fr/entreprise/493485924 : tableau des comptes non rendu
