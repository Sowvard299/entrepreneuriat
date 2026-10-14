# Marchés v3, lentille 7 (dépense déjà là mais mal servie) + B2C et produits physiques

- Mission : phase 0 de la recherche v3, chercheur D. Date : 2026-10-13.
- Recherches web utilisées : 25 / 25 (WebFetch en plus : une vingtaine de pages). Appels API Sirene : une trentaine.
- Preuves : 35 (D1-p1 à D10-p4), 30 domaines distincts. Marchés : D1 à D10 (D1 déménagement, D2 obsèques, D3 bière et boissons sans alcool, D4 compléments alimentaires, D5 hébergeurs indépendants face aux OTA, D6 douche et salle de bain seniors, D7 mariage, D8 petfood, D9 cosmétique indie, D10 restaurants face aux plateformes de livraison).
- B2C : D1, D2, D3, D4, D6, D7, D8, D9. Produit physique : D3, D4, D8, D9.
- Légende : « ouverte » = page lue en entier par WebFetch ; « extrait de recherche » = vue seulement dans le résumé du moteur (les citations entre « » y sont celles du résumé, pas vérifiées sur la page).
- Sources bloquées rencontrées : economie.gouv.fr/dgccrf (403 connu, non tenté), hospitality-on.com (403), PDF compressés FACCO et FEBEA (illisibles), sénat ppr25-363.pdf (illisible), synadiet.org et insee.fr/8681093 (404 sur URL devinée, abandonnées).
- Les chiffres « Sirene » viennent de l'API recherche-entreprises.api.gouv.fr (état administratif actif, 2026-10-13). « emp ≥1 » = tranches d'effectif 01 à 53.

---

## D1 : Déménagement des ménages (B2C, service)

### D1-p1 : Taille du secteur, étude Xerfi
- Acteur / marché : entreprises de déménagement, clients ménages et entreprises
- Type : tendance
- Source : https://www.xerfi.com/presentationetude/le-marche-du-demenagement_STR13 (ouverte ; mise à jour de l'étude 2026-08-31)
- Citation : « environ 1,5 Md€ de chiffre d'affaires en France chaque année »
- Chiffres : 1,5 Md€/an, valeur, France ; secteur « Très atomisé », « essentiellement composé de TPE » ; près de la moitié des déménageurs dans un groupement (Demeco, Les Déménageurs Bretons...) ; Mobilitas et Hexvia en tête. Vendeur de rapports : confiance faible.
- Ce que ça dit pour nous : taille > 50 M€ mais chiffre non institutionnel ; marché fragmenté.

### D1-p2 : Parc d'entreprises et emploi en recul (OPTL/CSD via Selectra)
- Acteur / marché : établissements de déménagement employeurs
- Type : contre-preuve
- Source : https://selectra.info/demenagement/barometre (ouverte ; chiffres 2025, date de page inconnue)
- Citation : « La mobilité résidentielle recule sur dix ans »
- Chiffres : 1 219 établissements en 2025 contre 1 277 en 2024 ; 10 241 salariés contre 11 036 (-7,2 %) ; 389 créations et 295 défaillances en 2025 ; 5,9 M de personnes ont changé de résidence en 2023 (Insee), mobilité 8,8 % contre 10,8 % en 2013 ; dernier CA officiel OPTL : 1,2 Md€ (2015).
- Ce que ça dit pour nous : la demande baisse (mobilité -2 points en 10 ans) : la croissance ne passe pas ; 295 défaillances en un an.

### D1-p3 : Prix publics de la dépense
- Acteur / marché : ménages qui font appel à un déménageur
- Type : argent dépensé
- Source : https://selectra.info/demenagement/barometre (ouverte, fourchettes 2025 de La Cigogne et MyDéménageur)
- Citation : « Il n'existe pas de prix moyen officiel »
- Chiffres : local 2 pièces 500 à 1 200 € ; maison 4 pièces locale 1 500 à 3 000 € ; longue distance 4 pièces 2 500 à 5 000 € ; 35 à 90 €/m³.
- Ce que ça dit pour nous : panier de 500 à 3 000 € ; prix opaques (pas de prix officiel), donc comparateur crédible mais marché en recul.

### D1-p4 : Comptage Sirene
- Acteur / marché : entreprises NAF 49.42Z (services de déménagement)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=49.42Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : « total_results » : 3513 (champ de l'API, pas une phrase)
- Chiffres : 3 513 unités actives, dont 1 091 avec au moins 1 salarié.
- Ce que ça dit pour nous : plus de 3 000 prestataires joignables ; la moitié sont de très petites structures.

### Fiche D1
- Taille France : 1,5 Md€/an (Xerfi, D1-p1, confiance faible) ; 1,2 Md€ en 2015 (OPTL/CSD, D1-p2). Valeur, France.
- Croissance : négative en volume (mobilité 10,8 % → 8,8 % entre 2013 et 2023, Insee via Selectra, D1-p2) ; emploi -7,2 % en 2025. Pas de croissance en valeur sourcée.
- Moteur de croissance : aucun identifié. [HYPOTHÈSE] : l'inflation seule tire la valeur.
- Acteurs : 1 219 établissements employeurs (OPTL) ; top 3 : Mobilitas, Hexvia nommés (Xerfi), parts non publiées [HYPOTHÈSE] < 40 % car « très atomisé ».
- Clients identifiables : B2C : ~5,9 M de personnes/an changent de résidence (Insee 2023) ; B2B : 3 513 unités NAF 49.42Z (D1-p4).
- Demande : tendance 5 ans non mesurée (pas de Google Trends). Baisse de la mobilité = baisse.
- Modèle d'exécution : service à forte main-d'œuvre (employeur) ; ou plateforme de mise en relation (cimetière v2).
- Contre-preuve (obligatoire) : D1-p2 (mobilité en baisse, 295 défaillances, emploi -7,2 %).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : faible (taille Xerfi, pas de preuve de plainte dans mes recherches).

---

## D2 : Obsèques (B2C, service + produits funéraires)

### D2-p1 : Taille, concentration et opacité (question écrite à l'Assemblée)
- Acteur / marché : entreprises de pompes funèbres, familles
- Type : plainte
- Source : https://questions.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE12626 (ouverte ; question n° 12626, JO du 2026-02-03)
- Citation : « Deux grands opérateurs réaliseraient à eux seuls près d'un tiers des obsèques en France »
- Chiffres : ~3 Md€/an, ~650 000 décès/an ; coût moyen 3 000 à 4 500 € ; écarts de prix pouvant dépasser 100 % pour des prestations comparables ; « manque persistant de transparence dans le fonctionnement du marché funéraire ».
- Ce que ça dit pour nous : le marché existe (3 Md€), les prix sont opaques, mais deux groupes tiennent un tiers du marché.

### D2-p2 : Enquête Que Choisir sur les devis (ancienne)
- Acteur / marché : pompes funèbres (OGF/PFG, Roc'Eclerc, indépendants)
- Type : plainte
- Source : https://www.quechoisir.org/enquete-pompes-funebres-cout-des-obseques-le-devis-type-reste-lettre-morte-n10919/ (ouverte ; publiée 2011-10-20)
- Citation : « le manque de transparence dans les tarifs des obsèques »
- Chiffres : 821 devis dans 997 établissements, 97 % non conformes au devis type ; prix moyen d'une inhumation 3 098 € (1 300 à 6 101 €) ; OGF 3 552 € en moyenne, Roc'Eclerc 2 914 €, indépendants 2 986 €. Donnée de 2011 : contexte seulement.
- Ce que ça dit pour nous : l'opacité est ancienne et documentée ; les grands réseaux ne sont pas les moins chers.

### D2-p3 : DGCCRF, écarts entre prix affichés et facturés
- Acteur / marché : opérateurs funéraires
- Type : obligation
- Source : https://www.economie.gouv.fr/dgccrf/prestations-funeraires-etes-vous-bien-informes (extrait de recherche ; page non ouverte, 403 connu)
- Citation : « écarts significatifs entre le prix des cercueils affiché et celui facturé aux familles »
- Chiffres : enquête 2017-2018 : plus de 68 % d'établissements en anomalie ; nouvelle enquête nationale 2024-2025 (bilan non trouvé).
- Ce que ça dit pour nous : le contrôle public confirme l'opacité ; le cadre est l'arrêté du 11 janvier 1999 et le devis type (arrêté du 23 août 2010) selon le résumé : à faire vérifier par l'auditeur.

### D2-p4 : Décès en hausse
- Acteur / marché : volume de la demande
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/8721209 (page ouverte, sans chiffres ; chiffres lus dans l'extrait de recherche, bilan démographique publié le 2026-01-13)
- Citation : « Le nombre de décès augmente de 1,5 % en 2025 »
- Chiffres : 643 168 décès en 2024 (définitif) ; +1,5 % en 2025 (estimation) ; solde naturel négatif (-6 000) en 2025.
- Ce que ça dit pour nous : volume +1 à 2 %/an à court terme, très loin de 8 %.

### D2-p5 : Projection de long terme
- Acteur / marché : volume de la demande
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/2871833 (extrait de recherche ; projections 2005-2050, ancien ; rattachement exact du chiffre non garanti)
- Citation : aucune citation textuelle disponible ; paraphrase du résumé de recherche : les décès s'accélèrent à partir de 2030
- Chiffres : ~773 000 décès en 2049 contre ~531 000 en 2005 (scénario central ancien).
- Ce que ça dit pour nous : moteur structurel réel mais après 2030 ; hors fenêtre de 3 ans.

### D2-p6 : Sirene
- Acteur / marché : entreprises NAF 96.03Z (services funéraires)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=96.03Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : « total_results » : 6055 (champ de l'API)
- Chiffres : 6 055 unités actives, 2 491 avec au moins 1 salarié.
- Ce que ça dit pour nous : plus de 3 000 acteurs (B2B), donc un marché fragmenté dans le nombre.

### D2-p7 : Assurance obsèques, argent déjà prépayé
- Acteur / marché : assureurs obsèques, souscripteurs
- Type : argent dépensé
- Source : https://www.moneyvox.fr/assurance/actualites/100372/les-contrats-assurance-obseques-dans-le-viseur-de-la-repression-des-fraudes (extrait de recherche)
- Citation : « manque de lisibilité globale des informations précontractuelles » (formulation du résumé)
- Chiffres : 1,8 Md€ de cotisations en 2023, plus de 5,4 M de contrats ; un tiers des 69 professionnels contrôlés en 2022 présentaient des anomalies.
- Ce que ça dit pour nous : l'argent est dépensé en amont (prévoyance), canal de vente voisin.

### Fiche D2
- Taille France : ~3 Md€/an (D2-p1, ministère saisi, estimation parlementaire, année 2026). Bottom-up : 643 168 décès × 3 000 à 4 500 € = 1,9 à 2,9 Md€ (calcul, prix D2-p1) ; cohérent avec 3 Md€ (confiance moyenne).
- Croissance : décès +1,5 % en 2025, +0,3 % en 2024 (Insee, D2-p4), en volume. Valeur : [HYPOTHÈSE] 2 à 4 %/an (prix +35 % sur 10 ans citée par un site de business plans, faible). Pas 8 %.
- Moteur de croissance : arrivée des générations du baby-boom aux grands âges, accélération après 2030 (D2-p5, projection ancienne).
- Acteurs : ~4 000 à 6 055 entreprises (D2-p1, D2-p6) ; deux groupes ≈ 1/3 des obsèques (D2-p1). Parts de PFG 25 % et Roc'Eclerc 10 % lues dans un résumé sans source identifiée : confiance faible. Top 3 ≈ 35-40 %.
- Clients identifiables : ~643 000 familles/an (B2C, Insee) ; B2B : 6 055 entreprises (D2-p6).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : service outillé (comparateur, devis) ; opérateur funéraire = habilitation préfectorale [HYPOTHÈSE : à vérifier, article du CGCT à citer par l'auditeur]. Employeur si l'on exécute.
- Contre-preuve (obligatoire) : D2-p4 (volume +0,3 % à +1,5 %/an) et D2-p1 (deux groupes ≈ 1/3 ; habilitation).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (moteur structurel après 2030) | concentration ✔ limite | clients ✔
- Confiance : moyenne pour la taille (parlement + calcul), faible pour la croissance en valeur.

---

## D3 : Bière et boissons sans alcool (B2C, produit physique, brasseurs et marques)

### D3-p1 : Bilan 2025 des brasseurs
- Acteur / marché : brasseurs français, bière sans alcool en grande distribution
- Type : tendance
- Source : https://brasseurs-de-france.com/wp-content/uploads/2026/02/CP-eco-marche-bilan-2025-03022026.pdf (ouverte ; communiqué du 2026-02-03, données NielsenIQ)
- Citation : « un rôle moteur » (le sans alcool dans la catégorie)
- Chiffres : +11,5 % sur un an en grande distribution (volume), ~6 % des volumes ; marché de la bière total « atone » (-7 % cumulé 2022-2024) ; ~2 500 brasseries ; 209 fermetures et 213 ouvertures en 2025 ; 40 % des brasseurs interrogés produisent du sans alcool, 30 % ont un projet.
- Ce que ça dit pour nous : la hausse est réelle mais dans un marché total plat ; les petits brasseurs s'y mettent tous.

### D3-p2 : Kronenbourg, dix premiers mois 2025
- Acteur / marché : leader des bières sans alcool
- Type : contre-preuve
- Source : https://www.kronenbourg.com/media/25jpben3/cp-brasseries-kronenbourg-anime-le-dry-january-janvier-2026.pdf (extrait de recherche ; acteur du secteur)
- Citation : aucune phrase copiée ; le résumé dit que Tourtel Twist pèse 58 % du total des bières sans alcool
- Chiffres : 5,7 % du marché de la bière, +0,6 point de part, +12,8 % en volume (hors panachés) ; l'Allemagne et l'Espagne dépassent 15 %.
- Ce que ça dit pour nous : une marque tient 58 % ; le rattrapage vers 15 % est le moteur, mais l'entrée est difficile.

### D3-p3 : Valeur du segment (blog d'études)
- Acteur / marché : bière, vin, apéritifs sans alcool
- Type : tendance
- Source : https://www.intotheminds.com/blog/evolution-consommation-alcool-marche-desalcoolisation/ (ouverte ; date inconnue ; sources citées : « cabinets d'études » non nommés)
- Citation : aucune phrase copiée ; chiffres relevés dans un tableau
- Chiffres : bière sans alcool ~238 M€ en 2024, +5,4 % valeur, +3,9 % volume ; vin sans alcool ~36 M€ (+21,5 % valeur sur un an) ; apéritifs, cocktails et spiritueux sans alcool ~58 M€ (> +6 % valeur). Confiance faible (blog).
- Ce que ça dit pour nous : total ~330 M€ (somme, périmètres non datés) ; la valeur croît moins vite que le volume.

### D3-p4 : Sirene brasseries
- Acteur / marché : NAF 11.05Z (fabrication de bière)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=11.05Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 2932
- Chiffres : 2 932 unités actives, 931 avec au moins 1 salarié.
- Ce que ça dit pour nous : les brasseurs artisanaux sont nombreux et sans marque nationale : ils sont des clients B2B de fabrication ou de distribution.

### Fiche D3
- Taille France : bière sans alcool ~238 M€ (2024, blog, faible, D3-p3) ; avec vin et spiritueux sans alcool ~330 M€ (somme, faible). Valeur, France.
- Croissance : volume +11,5 % en 2025 en grande distribution (Brasseurs de France, fédération, D3-p1) et +12,8 % sur 10 mois (Kronenbourg, D3-p2). Valeur +5,4 % en 2024 (blog). Deux sources dont une fédération : volume ✔ ; valeur non confirmée.
- Moteur de croissance : désalcoolisation des consommations, Dry January, rattrapage vs Allemagne/Espagne (> 15 %) (D3-p2).
- Acteurs : Tourtel Twist = 58 % des bières sans alcool (D3-p2). Boissons sans alcool hors bière : part inconnue [HYPOTHÈSE].
- Clients identifiables : B2C, plusieurs millions de consommateurs [HYPOTHÈSE] ; B2B : 2 932 brasseries (D3-p4).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : produit (brassage en sous-traitance, distribution) ; stock et trésorerie.
- Contre-preuve (obligatoire) : D3-p2 (58 % pour une marque) et D3-p1 (marché de la bière total en baisse, 4 fermetures par semaine).
- Seuils CLAUDE.md : taille ✔ (bière seule ~238 M€, faible) | croissance ✔ en volume (valeur à confirmer) | concentration ✘ (bière) | clients ✔
- Confiance : faible à moyenne.

---

## D4 : Compléments alimentaires, santé et nutrition (B2C, produit physique)

### D4-p1 : Taille et croissance 2025 (IQVIA)
- Acteur / marché : marques de compléments, pharmacie, e-commerce
- Type : tendance
- Source : https://www.iqvia.com/locations/france/blogs/2026/04/complements-alimentaires-en-france (ouverte ; 2026-04-20)
- Citation : « 2 milliards d'euros en 2025 »
- Chiffres : 2 Md€ (pharmacie, parapharmacie, e-pharmacie, Amazon) ; +4,7 % ; +89 M€ entre 2024 et 2025 ; effet volume -35 M€, lancements et rénovations +96 M€ ; en ligne 8,3 % des ventes mais 28 % de la croissance (13 % en 2024) ; Amazon +19 % ; Europe 19,9 Md€ (+5,9 %).
- Ce que ça dit pour nous : le volume baisse ; la croissance vient de produits nouveaux et du canal en ligne.

### D4-p2 : Poids de la pharmacie
- Acteur / marché : circuits de vente
- Type : tendance
- Source : https://www.lequotidiendupharmacien.fr/medicament-parapharmacie/lofficine-toujours-premier-lieu-de-vente-des-complements-alimentaires (ouverte ; 2025-03-28)
- Citation : « la pharmacie représente 55 % des ventes en valeur de compléments alimentaires »
- Chiffres : 55 % en pharmacie (bilan 2024) ; croissance 2024 portée par « vitalité et immunité » et « stress et sommeil », minceur en baisse.
- Ce que ça dit pour nous : le canal dominant est tenu par les pharmaciens ; une marque en ligne vise les 8 % du web.

### D4-p3 : Santé mentale, moteur de 2025
- Acteur / marché : compléments stress, sommeil
- Type : recherche active
- Source : https://www.lequotidiendupharmacien.fr/medicament-parapharmacie/stress-fatigue-sommeil-la-sante-mentale-tire-le-marche-des-complements-alimentaires (extrait de recherche ; page payante)
- Citation : « la santé mentale tire le marché des compléments alimentaires » (titre de page)
- Chiffres : aucun dans l'extrait. Un site grand public (non identifié) cite 2,9 Md€ pour 2025 (+5,7 %) attribué au Synadiet : non vérifié, périmètre plus large.
- Ce que ça dit pour nous : la demande suit l'anxiété et le sommeil ; la nutrition sportive n'est chiffrée par aucune source trouvée.

### D4-p4 : Sirene
- Acteur / marché : NAF 10.89Z (fabrication d'autres produits alimentaires), proxy imparfait
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=10.89Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 2228
- Chiffres : 2 228 unités actives, 636 avec au moins 1 salarié. Code fourre-tout.
- Ce que ça dit pour nous : un vivier de fabricants à façon, mais le code ne sépare pas les compléments.

### Fiche D4
- Taille France : 2 Md€ en 2025 (IQVIA, D4-p1, circuits pharmacie/parapharmacie/e-commerce/Amazon, valeur) ; 2,9 Md€ (Synadiet via un site non identifié, périmètre plus large, faible).
- Croissance : +4,7 % en valeur en 2025 (IQVIA), volume négatif ; +5,7 % (non vérifié). En ligne : ~+18 %/an (calcul : 28 % × 89 M€ ≈ 25 M€ sur une base de 8,3 % × 2 000 M€ - 25 M€ ≈ 141 M€ ; [HYPOTHÈSE] sur l'assiette). Une seule source de panel : croissance non confirmée par une institution.
- Moteur de croissance : santé mentale, vitalité et immunité (D4-p2, D4-p3) ; pas de date d'obligation.
- Acteurs : parts non publiées [HYPOTHÈSE] ; la pharmacie vend 55 % (D4-p2).
- Clients identifiables : B2C, très large [HYPOTHÈSE sans chiffre sourcé] ; fabricants à façon : voir D4-p4.
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : produit (fabrication à façon, marque blanche) ; réglementation des allégations et déclaration DGCCRF [HYPOTHÈSE à vérifier].
- Contre-preuve (obligatoire) : D4-p1 (volume -35 M€ ; croissance venue des seuls lancements ; Amazon +19 %).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (4,7 %) sauf segment en ligne | concentration ? (inconnue) | clients ✔
- Confiance : moyenne pour la taille, faible pour la concentration.

---

## D5 : Hébergeurs indépendants face aux OTA (B2B, logiciel/service outillé)

### D5-p1 : Parc hôtelier indépendant (Insee)
- Acteur / marché : hôtels indépendants
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/2015412 (ouverte ; publiée 2026-07-23, données 2025)
- Citation : aucune phrase ; tableau de l'Insee
- Chiffres : 11 253 hôtels indépendants (3 634 de chaîne), 316 400 chambres, 111,0 M de nuitées en 2025, taux d'occupation 60,2 % (chaînes 64,4 %).
- Ce que ça dit pour nous : plus de 11 000 clients B2B identifiables avec un taux d'occupation plus faible que les chaînes.

### D5-p2 : Commissions et coût réel
- Acteur / marché : hôtels indépendants face à Booking.com
- Type : plainte
- Source : https://www.prostay.com/fr/blog/hotel-direct-booking-conversion-2026/ (extrait de recherche ; blog de prestataire, faible)
- Citation : « La commission affichée est de 15 % chez Booking.com et Expedia » (formulation du résumé)
- Chiffres : coût total 18 à 30 % avec Genius (10 %) et Visibility Booster (3 à 5 %).
- Ce que ça dit pour nous : la dépense existe et dépasse la commission affichée ; source commerciale.

### D5-p3 : Part des OTA en France
- Acteur / marché : distribution hôtelière en ligne
- Type : tendance
- Source : https://hospitality-on.com/fr/distribution/distribution-hoteliere-europeenne-le-duopole-booking-expedia-se-fige-les-rapports-de (extrait de recherche ; page non ouverte)
- Citation : « le duopole Booking-Expedia se fige » (titre de page)
- Chiffres (résumé du moteur, données D-EDGE et HOTREC 2026) : France : OTA ~70 % des réservations numériques en volume, direct ~25 % (33 % de la valeur) ; Booking = 65,4 % des réservations OTA en France ; Europe : 51,3 % en direct. Périmètres différents, ne pas les additionner.
- Ce que ça dit pour nous : Booking domine les OTA ; le direct plafonne.

### D5-p4 : Cadre juridique
- Acteur / marché : clauses de parité tarifaire
- Type : obligation
- Source : https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-09/cp240145fr.pdf (extrait de recherche ; CJUE C-264/23, 2024-09-19)
- Citation : aucune phrase copiée
- Chiffres : parité interdite en France depuis la loi du 6 août 2015 (art. 133), selon le résumé ; Booking a retiré les clauses dans l'UE après sa désignation comme contrôleur d'accès (DMA).
- Ce que ça dit pour nous : le moteur n'est pas nouveau : les hôteliers peuvent déjà vendre moins cher en direct.

### D5-p5 : Fréquentation
- Acteur / marché : hôtellerie
- Type : tendance
- Source : https://pro.normandie-tourisme.fr/app/uploads/sites/2/2026/04/la-frequentation-dans-lhotellerie-en-2025.pdf (extrait de recherche ; résumé reprenant l'Insee)
- Citation : aucune phrase copiée
- Chiffres : fréquentation +3 % en 2025, occupation 62 % (+1 point) ; tourisme d'affaires -9,9 % au 2e trimestre 2025.
- Ce que ça dit pour nous : croissance de l'activité ~3 %, bien sous 8 %.

### D5-p6 : Sirene hébergement
- Acteur / marché : NAF 55.20Z (hébergement touristique de courte durée) et 55.10Z (hôtels)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=55.20Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 10000 (plafond atteint)
- Chiffres : 55.20Z : plus de 10 000 actives, dont 4 420 avec au moins 1 salarié ; 55.10Z : plus de 10 000 actives ; 55.30Z (campings) : 6 897.
- Ce que ça dit pour nous : plusieurs dizaines de milliers de petits hébergeurs joignables.

### Fiche D5
- Taille France : bottom-up de la commission payée aux OTA = 111,0 M de nuitées (D5-p1, hôtels indépendants) × [HYPOTHÈSE] 70 € de recette par nuitée = ~7,8 Md€ × [HYPOTHÈSE] 30 à 60 % via OTA × 15 à 18 % = ~350 à 840 M€/an de commissions. Hypothèses fortes : confiance faible. Le marché vendable (logiciel de vente directe) est une fraction, non chiffrée.
- Croissance : fréquentation +3 % en 2025 (D5-p5) ; pas de croissance du marché des outils sourcée.
- Moteur de croissance : CJUE 2024 et DMA (D5-p4) ; déjà acquis depuis 2015 en France : moteur faible.
- Acteurs : Booking 65,4 % des réservations OTA en France (D5-p3). Concurrents du côté outils (SiteMinder, D-EDGE, Mews) présents, parts inconnues.
- Clients identifiables : 11 253 hôtels indépendants (D5-p1) + 4 420 hébergeurs employeurs 55.20Z (D5-p6).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : logiciel / service outillé (moteur de réservation, marketing direct) ; besoin d'un associé tech pour un produit propre.
- Contre-preuve (obligatoire) : D5-p4 (parité déjà interdite depuis 2015) et D5-p3 (direct qui stagne malgré l'interdiction ; outils concurrents installés).
- Seuils CLAUDE.md : taille ✔ (hypothèse) | croissance ✘ | concentration ✘ côté OTA, ? côté outils | clients ✔
- Confiance : faible.

---

## D6 : Douche et salle de bain adaptées aux seniors (B2C, produit + pose)

### D6-p1 : Volume de dossiers MaPrimeAdapt'
- Acteur / marché : propriétaires âgés finançant l'adaptation du logement
- Type : argent dépensé
- Source : https://informations.handicap.fr/a-handicap-tout-ce-qui-change-en-janvier-2026-38723.php (ouverte ; 2026-01-20)
- Citation : « près de 38 000 dossiers ont été enregistrés »
- Chiffres : 38 000 dossiers en 2025, aide moyenne 6 045 € ; objectif 2026 : 41 000 dossiers financés ; aide « reconduite en 2026 » mais « les nouvelles demandes sont temporairement suspendues » en attendant le budget.
- Ce que ça dit pour nous : 38 000 × 6 045 € = ~230 M€ d'aides publiques en 2025 (calcul) : de l'argent public déjà dépensé.

### D6-p2 : Prix de la douche senior
- Acteur / marché : remplacement baignoire par douche
- Type : argent dépensé
- Source : https://abctravaux.org/remplacement-baignoire-par-douche-senior-prix/ (extrait de recherche ; site commercial, faible)
- Citation : aucune phrase copiée
- Chiffres : 3 500 à 9 000 € posé selon les sources ; aide jusqu'à 70 % des travaux, plafond 22 000 € HT ; propriétaires de 70 ans et plus (ou 60-69 ans avec perte d'autonomie), logement de plus de 15 ans, sous conditions de ressources.
- Ce que ça dit pour nous : panier de 3 500 à 9 000 € ; le client paie le reste après aide.

### D6-p3 : Profil des bénéficiaires et files d'attente
- Acteur / marché : Anah, MaPrimeAdapt'
- Type : contre-preuve
- Source : https://edito.seloger.com/materiaux-equipements/travaux/maprimeadapt-2026-une-aide-cle-adapter-logement-bien-vieillir-chez (extrait de recherche ; publi-communiqué)
- Citation : aucune phrase copiée
- Chiffres : guichet opérationnel depuis le 2026-02-23 après deux mois de blocage, 83 000 dossiers en attente, délais d'instruction très allongés ; 82 % des dossiers engagés concernent une personne de 70 ans et plus (Selectra, extrait). 2026 : seuls les profils « Bleu » et « Jaune » sont éligibles (Hellio, extrait).
- Ce que ça dit pour nous : le marché dépend d'un budget d'État instable ; les ménages aisés restent hors aide.

### D6-p4 : Démarchage abusif dans les travaux
- Acteur / marché : entreprises de travaux auprès des personnes âgées
- Type : plainte
- Source : https://www.economie.gouv.fr/dgccrf/lutte-contre-les-arnaques-dans-le-secteur-des-travaux-de-renovation-0 (extrait de recherche ; non ouverte)
- Citation : aucune phrase copiée
- Chiffres : alertes sur devis gonflés, faux simulateurs d'aides, faux mandats Anah, personnes âgées ciblées ; délai de réflexion de 7 jours en vente à domicile. Pas de statistique propre aux douches.
- Ce que ça dit pour nous : la confiance est le point faible du secteur ; aucune plainte chiffrée par segment.

### D6-p5 : Sirene plomberie (proxy)
- Acteur / marché : NAF 43.22A (plomberie, chauffage)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=43.22A&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 10000 (plafond)
- Chiffres : plus de 10 000 entreprises actives.
- Ce que ça dit pour nous : offre très fragmentée ; poseurs nombreux, donc le client est difficile à orienter.

### Fiche D6
- Taille France : ~230 M€/an d'aides MaPrimeAdapt' en 2025 (38 000 × 6 045 €, handicap.fr, tous travaux d'adaptation, pas seulement les douches). Valeur des travaux aidés [HYPOTHÈSE] : 330 à 460 M€ (aide moyenne 6 045 € ÷ taux 50 à 70 %). Périmètre : France, dossiers financés ou enregistrés.
- Croissance : objectif 41 000 contre 38 000 dossiers (+8 %, cible et non constat) ; aucune série 2023-2025 sourcée. Une seule source : croissance non établie.
- Moteur de croissance : vieillissement (population 75 ans et plus en hausse, Insee, projection 2070 : 19,3 % de 75 ans et plus, extrait de recherche) et aide reconduite en 2026 (D6-p1).
- Acteurs : très fragmenté [HYPOTHÈSE], pas de chiffre de part de marché.
- Clients identifiables : propriétaires de 70 ans et plus ; effectif non sourcé [HYPOTHÈSE] > 1 M ; 38 000 dossiers/an en pratique.
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : service à forte main-d'œuvre (poseurs) ou intermédiation / accompagnement ; l'employeur n'est pas nécessaire en sous-traitant.
- Contre-preuve (obligatoire) : D6-p3 (guichet bloqué, 83 000 dossiers en attente, profils aisés exclus).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non prouvée) | concentration ✔ [HYPOTHÈSE] | clients ✔ [HYPOTHÈSE]
- Confiance : faible à moyenne.

---

## D7 : Mariage (B2C, prestataires et salles)

### D7-p1 : Nombre de mariages et budget moyen
- Acteur / marché : couples, prestataires de mariage
- Type : argent dépensé
- Source : https://www.economiematin.fr/?p=222519 (ouverte ; modifiée le 2026-05-27)
- Citation : « évalue à 19.293 euros le budget moyen d'un mariage en France en 2026 »
- Chiffres : 245 000 mariages en 2025 (Insee, métropole) contre 242 103 en 2024 ; budget moyen 19 293 € hors bague et voyage de noces (Mariages.net, vendeur d'annonces), 215 € par invité, en baisse sur un an ; budget « idéal » de 33 465 € (enquête, non dépensé).
- Ce que ça dit pour nous : calcul : 245 000 × 19 293 € = ~4,7 Md€/an, confiance moyenne.

### D7-p2 : Mariages en hausse légère (Insee)
- Acteur / marché : demande
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/8721209 (page ouverte, sans chiffres ; chiffres lus dans l'extrait de recherche ; bilan du 2026-01-13)
- Citation : « le nombre de mariages augmente de nouveau en 2025 »
- Chiffres : 251 000 célébrations en 2025 (estimation), 248 174 en 2024 (définitif), soit +1,1 % ; l'Economie Matin donne 245 000 pour la métropole seule.
- Ce que ça dit pour nous : volume stable ; pas de croissance de 8 %.

### D7-p3 : Plateformes d'annonces, plainte des prestataires
- Acteur / marché : Mariages.net, prestataires (photographes, événementiel)
- Type : plainte
- Source : https://de.trustpilot.com/review/mariages.net?stars=1&stars=2 (ouverte ; avis de 2026-02 à 2026-08)
- Citation : « Beaucoup de demandes ≠ beaucoup de clients. »
- Chiffres : 932 avis, note 4,4/5, 27 % d'avis à 1 ou 2 étoiles (24 % + 3 %) ; plaintes sur les tarifs d'abonnement, le renouvellement automatique, des hausses annuelles. Extrait de recherche complémentaire (non ouvert) : abonnements premium d'environ 1 700 €/an signalés sur forum.quechoisir.org, témoignages non vérifiés.
- Ce que ça dit pour nous : les prestataires paient cher une visibilité qui ne se convertit pas, mais la plateforme reste bien notée (4,4).

### D7-p4 : Acteurs marketplaces
- Acteur / marché : Zankyou, annuaires de salles
- Type : tendance
- Source : https://www.journaldunet.com/retail/1196466-zankyou-le-pure-player-qui-veut-organiser-les-mariages-de-a-a-z/ (extrait de recherche ; article ancien, ~2017)
- Citation : aucune phrase copiée
- Chiffres : 7 700 professionnels référencés en France chez Zankyou ; commission sur listes de mariage 1,65 % + 1 € par transaction (2017) ; l'annuaire Bridebook affiche 6 204 salles (fiches commerciales, pas un recensement).
- Ce que ça dit pour nous : l'offre est fragmentée (milliers de prestataires) et déjà intermédiée par des plateformes installées.

### Fiche D7
- Taille France : ~4,7 Md€/an (calcul : 245 000 mariages × 19 293 €, D7-p1 ; hors bague et voyage) ; Xerfi/sites : 3,5 à 4 Md€ (non sourcés, faible). Valeur, France.
- Croissance : mariages +1,1 % (248 174 → 251 000, Insee, D7-p2), volume ; budget moyen en baisse. Pas de 8 %.
- Moteur de croissance : aucun identifié.
- Acteurs : milliers de prestataires locaux (7 700 chez Zankyou, 6 204 salles Bridebook) ; top 3 non publiés [HYPOTHÈSE] < 40 %.
- Clients identifiables : ~245 000 à 251 000 couples/an ✔ (B2C, Insee).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : marketplace (cimetière v2 : attirer offre et demande) ou service d'organisation (agence locale).
- Contre-preuve (obligatoire) : D7-p2 (mariages stables, +1 %/an) et D7-p3 (Mariages.net noté 4,4/5 : l'acteur en place est apprécié).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ | concentration ✔ [HYPOTHÈSE] | clients ✔
- Confiance : moyenne pour la taille, faible pour l'angle.

---

## D8 : Aliments pour chiens et chats, premium et vente directe (B2C, produit physique)

### D8-p1 : Chiffre d'affaires et canaux 2025 (FACCO)
- Acteur / marché : industriels du petfood, propriétaires de chiens et chats
- Type : argent dépensé
- Source : https://globalpetindustry.com/news/french-pet-market-i-pet-food-holds-steady-at-e4-8bn-exports-drive-nearly-half-of-production/ (ouverte ; 2026-07-15, données FACCO 2025)
- Citation : « Digital channels hold steady at 28% for dog food and 21% for cat food. »
- Chiffres : 4,8 Md€ de chiffre d'affaires des industriels en 2025, inchangé vs 2024 ; 48 % de la production exportée ; grande distribution 51 % (chiens) et 68 % (chats) ; animaleries 34 % et 23 % ; en ligne 28 % et 21 %.
- Ce que ça dit pour nous : le marché est plat en 2025, mais plus d'un quart des chiens se nourrit par achats en ligne.

### D8-p2 : Foyers et parc d'animaux
- Acteur / marché : propriétaires d'animaux
- Type : tendance
- Source : https://www.facco.fr/wp-content/uploads/2025/06/2025-06-facco-chiffres-odoxa.pdf (extrait de recherche ; PDF illisible à l'ouverture ; baromètre FACCO-Odoxa 2025)
- Citation : « 60% des Français possèdent au moins un animal de compagnie » (formulation du résumé)
- Chiffres : 60 % (61 % en 2024) ; 53 % ont un chien et/ou un chat (55 % en 2024) ; 79 M d'animaux familiers ; 91 % des chiens et 96 % des chats mangent de l'alimentation industrielle.
- Ce que ça dit pour nous : la base de clients est immense mais le taux de possession recule d'un point.

### D8-p3 : Valeur au détail (vendeur de rapports)
- Acteur / marché : ventes d'aliments pour animaux tous circuits
- Type : tendance
- Source : https://www.xerfi.com/presentationetude/le-marche-du-petfood_IAA13 (extrait de recherche ; faible)
- Citation : aucune phrase copiée
- Chiffres : plus de 6,3 Md€ de ventes au détail en France en 2024 ; ~50 % via grandes surfaces alimentaires ; projection +3,5 %/an 2024-2029 (comdewouf.fr, blog, extrait, faible).
- Ce que ça dit pour nous : le détail pèse ~6,3 Md€ ; croissance annoncée autour de 3,5 %.

### D8-p4 : Évolution des prix et premiumisation
- Acteur / marché : marques de petfood
- Type : tendance
- Source : https://www.lsa-conso.fr/marche-du-petfood-comment-la-segmentation-repond-aux-attentes-des-pet-parents-exigeants,463055 (extrait de recherche)
- Citation : aucune phrase copiée
- Chiffres : hausse des prix de 2 % en 2024, stabilisation en 2025 ; 59 % des propriétaires interrogés (NielsenIQ) privilégient une alimentation adaptée aux bénéfices santé.
- Ce que ça dit pour nous : le segment premium existe mais le marché global ne croît plus par les prix.

### Fiche D8
- Taille France : 4,8 Md€ de CA des industriels en 2025 dont ~48 % exportés (FACCO, D8-p1) ; ventes au détail > 6,3 Md€ en 2024 (Xerfi, faible, D8-p3). Valeur ; périmètres différents, ne pas additionner. Marché domestique de l'industrie ≈ 52 % × 4,8 = ~2,5 Md€ [HYPOTHÈSE : 52 % est la part de la production vendue en France, appliquée à la valeur].
- Croissance : 0 % en valeur en 2025 (D8-p1) ; +3,5 %/an projeté (blog) ; volume 1 194 000 t. Pas de 8 %.
- Moteur de croissance : premiumisation et santé animale (D8-p4) ; pas de moteur daté.
- Acteurs : parts non publiées [HYPOTHÈSE] ; grandes multinationales dominantes dans la GMS ; la FACCO regroupe 32 à 34 adhérents pour 98 % du volume produit (extrait).
- Clients identifiables : 53 % des Français ont un chien et/ou un chat (D8-p2) : millions de foyers ✔.
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : produit (fabrication à façon, logistique de colis) ; stocks.
- Contre-preuve (obligatoire) : D8-p1 (marché inchangé en 2025, GMS 50 à 68 %) et D8-p2 (possession en baisse).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ | concentration ? [HYPOTHÈSE ✘ en GMS] | clients ✔
- Confiance : moyenne pour la taille, faible pour la concentration.

---

## D9 : Cosmétiques de marques indépendantes (B2C, produit physique)

### D9-p1 : Étude FEBEA sur les indie brands
- Acteur / marché : marques cosmétiques indépendantes françaises
- Type : tendance
- Source : https://www.febea.fr/sites/default/files/2024-10/FEBEA%20Communiqu%C3%A9%20de%20presse%20%C3%A9tude%20INDIE%20BRANDS%2011%20octobre%202024.pdf (extrait de recherche ; PDF illisible à l'ouverture ; communiqué du 2024-10-11)
- Citation : aucune phrase copiée
- Chiffres (résumé du moteur) : 158 marques interrogées en ligne et 34 en entretien ; 70 % ont moins de 9 salariés et moins de 1 M€ de CA ; 40 % des ventes à l'export ; 57 % omnicanal (web et pharmacies) ; aucun chiffre global sur le nombre de marques.
- Ce que ça dit pour nous : les marques indie sont minuscules et dispersées, mais le nombre exact n'existe pas.

### D9-p2 : Exportations 2025, contre-preuve
- Acteur / marché : filière cosmétique française
- Type : contre-preuve
- Source : https://www.linfodurable.fr/en-2025-les-exportations-francaises-de-cosmetiques-ont-recule-une-premiere-depuis-au-moins-20-ans (ouverte ; 2026-01-22, d'après l'AFP)
- Citation : « elles y reculent de 18% »
- Chiffres : exportations sur 10 mois 2025 : 18,75 Md€ (-1,16 %) ; États-Unis -18 % ; importations +6 % (4,46 Md€). Extrait de recherche FEBEA : exportations 2025 22,4 Md€ (-0,1 %) ; CA du secteur 2024 : 35,6 Md€ (production, pas consommation France).
- Ce que ça dit pour nous : la filière recule à l'export ; aucun chiffre de marché intérieur sourcé.

### D9-p3 : Sirene fabricants de parfums et cosmétiques
- Acteur / marché : NAF 20.42Z et 47.75Z
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=20.42Z&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 3218
- Chiffres : 20.42Z : 3 218 actives, 692 avec au moins 1 salarié ; 47.75Z (commerce de détail de parfumerie) : 9 162 actives, 2 286 employeurs.
- Ce que ça dit pour nous : un vivier de plus de 3 000 marques et fabricants, signe de fragmentation.

### Fiche D9
- Taille France : non publiée pour la consommation intérieure [HYPOTHÈSE à chiffrer]. CA du secteur 35,6 Md€ en 2024 (FEBEA, production mondiale vendue, extrait) : ne pas utiliser comme marché français. Marché des marques indie : inconnu.
- Croissance : exportations -0,1 % en 2025 (FEBEA, extrait) ; indie « en croissance exponentielle » depuis le Covid selon le communiqué, sans chiffre.
- Moteur de croissance : multiplication des marques indie ; aucun moteur daté.
- Acteurs : 3 218 unités NAF 20.42Z (D9-p3) ; part des 3 premiers inconnue [HYPOTHÈSE ✘ : groupes mondiaux dominants].
- Clients identifiables : B2C ✔ [HYPOTHÈSE] ; B2B : fabricants et marques (D9-p3).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : produit (fabrication à façon, responsabilité de mise sur le marché cosmétique) ; stock.
- Contre-preuve (obligatoire) : D9-p2 (première baisse des exportations depuis plus de 20 ans, États-Unis -18 %).
- Seuils CLAUDE.md : taille ? | croissance ✘ | concentration ? | clients ✔
- Confiance : faible (aucune taille France).

---

## D10 : Restaurants indépendants face aux plateformes de livraison (B2B, logiciel)

### D10-p1 : Valeur de la livraison de repas
- Acteur / marché : restaurants proposant la livraison
- Type : argent dépensé
- Source : https://www.republik-retail.fr/secteurs/food-et-restauration/restauration-les-10-chiffres-a-retenir-du-marche-de-la-livraison-en-france.html (extrait de recherche ; redirection à l'ouverture ; date de page inconnue)
- Citation : « Le chiffre d'affaires de la livraison s'élève aujourd'hui à 7 milliards d'euros » (formulation du résumé)
- Chiffres : 7 Md€ aujourd'hui, 9,2 Md€ prévus en 2026 (écart de +31 %, incohérent avec +7 %/an d'un site de business plans, faible) ; 41 % des consommateurs n'utilisent qu'une plateforme (30 % en 2020).
- Ce que ça dit pour nous : l'ordre de grandeur de 7 Md€ revient, la croissance est incertaine.

### D10-p2 : Commissions
- Acteur / marché : Uber Eats, Deliveroo
- Type : plainte
- Source : https://www.fooderise.com/en/blog/negocier-commission-uber-eats (extrait de recherche ; blog d'un prestataire, faible)
- Citation : « Uber Eats Direct » avec commission réduite de 3 % (formulation du résumé)
- Chiffres : commission 25 à 35 % de la commande selon ce blog ; 15 à 30 % (Uber Eats) et 14 à 30 % (Deliveroo) selon un comparatif 2026 (dineopen.com, extrait) ; pas de tarif officiel.
- Ce que ça dit pour nous : le coût est élevé mais déjà adressé par l'acteur lui-même (commande directe à 3 %).

### D10-p3 : Concentration
- Acteur / marché : plateformes de livraison
- Type : contre-preuve
- Source : étude Food Service Vision (2022-2023) rapportée dans un résumé de recherche, page exacte non identifiée : URL non citée
- Citation : aucune phrase copiée
- Chiffres : 88 % des restaurateurs livreurs passent par une société nationale, dont 60 % Uber Eats et 32 % Deliveroo ; marques proposant la livraison : 50 800 (octobre 2021) → 56 300 (janvier 2023), +10 % ; étude sur 160 restaurateurs.
- Ce que ça dit pour nous : deux plateformes captent l'essentiel ; ~56 000 marques sont des clients potentiels.

### D10-p4 : Sirene restaurants
- Acteur / marché : NAF 56.10A (restauration traditionnelle)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=56.10A&etat_administratif=A (ouverte via API, 2026-10-13)
- Citation : champ de l'API total_results = 10000 (plafond)
- Chiffres : plus de 10 000 restaurants traditionnels actifs, plus de 10 000 avec au moins 1 salarié (plafond).
- Ce que ça dit pour nous : clients très nombreux et joignables.

### Fiche D10
- Taille France : bottom-up de la commission pool = 7 Md€ (D10-p1) × 88 % via plateformes (D10-p3) × 15 à 30 % = ~0,9 à 1,8 Md€/an de commissions [HYPOTHÈSE sur le partage commissionné]. Le marché vendable (outil de commande directe) est une fraction, non chiffrée. Confiance faible.
- Croissance : +7 %/an (site de business plans, faible) ; +10 % de marques livrant en 15 mois (D10-p3). Aucune source institutionnelle.
- Moteur de croissance : aucun daté.
- Acteurs : Uber Eats 60 %, Deliveroo 32 % des restaurateurs livreurs (D10-p3) : top 2 > 90 %.
- Clients identifiables : ~56 300 marques livrant (D10-p3) ; plus de 10 000 restaurants NAF 56.10A (D10-p4).
- Demande : tendance 5 ans de requêtes non mesurée.
- Modèle d'exécution : logiciel ; besoin d'un associé tech.
- Contre-preuve (obligatoire) : D10-p3 (duopole) et D10-p2 (la commande directe à 3 % existe déjà chez Uber).
- Seuils CLAUDE.md : taille ✔ | croissance ✘ (non prouvée) | concentration ✘ | clients ✔
- Confiance : faible.

---

## Sources non lues
- https://www.economie.gouv.fr/dgccrf/prestations-funeraires-etes-vous-bien-informes : 403 connu, vu en extrait seulement.
- https://hospitality-on.com/fr/distribution/les-reservations-hotelieres-directes-ne-connaissent-pas-encore-lembellie-attendue-de : 403 à l'ouverture.
- https://www.facco.fr/wp-content/uploads/2025/06/2025-06-facco-chiffres-odoxa.pdf : PDF compressé illisible.
- https://www.febea.fr/sites/default/files/2024-10/FEBEA%20Communiqu%C3%A9%20de%20presse%20%C3%A9tude%20INDIE%20BRANDS%2011%20octobre%202024.pdf : PDF compressé illisible.
- https://www.senat.fr/leg/ppr25-363.pdf : PDF illisible (proposition de résolution sur le funéraire).
- https://www.republik-retail.fr/... : redirection vers une page d'accueil.
- https://www.teamfrance-export.fr/infos-sectorielles/21883/... : ouverte mais sans chiffre France (Espagne et monde), écartée.
- Synadiet (2,9 Md€) : chiffre vu seulement dans un résumé de recherche, page d'origine non identifiée.
- Mariages.net : tarifs d'abonnement non publics ; seuls des témoignages (Trustpilot ouvert, forum Que Choisir en extrait).
- Non cherché faute de budget : Google Trends, part de marché des 3 premiers pour D4, D8, D9 ; nutrition sportive ; plaintes sur les comparateurs de déménagement ; restauration hors domicile côté fournisseurs alimentaires (B2B).

## Contrôle de diversité des domaines (approximatif)
Domaines utilisés : recherche-entreprises.api.gouv.fr (8 preuves), insee.fr (4 : D2-p4, D2-p5, D5-p1, D7-p2), selectra.info (2), xerfi.com (2), quechoisir.org (1), questions.assemblee-nationale.fr (1), economie.gouv.fr (2), moneyvox.fr (1), brasseurs-de-france.com (1), kronenbourg.com (1), intotheminds.com (1), iqvia.com (1), lequotidiendupharmacien.fr (2), prostay.com (1), hospitality-on.com (1), curia.europa.eu (1), normandie-tourisme.fr (1), handicap.fr (1), abctravaux.org (1), edito.seloger.com (1), economiematin.fr (1), trustpilot.com (1), journaldunet.com (1), globalpetindustry.com (1), facco.fr (1), lsa-conso.fr (1), febea.fr (1), linfodurable.fr (1), republik-retail.fr (1), fooderise.com (1). Soit 30 domaines et 35 preuves ; aucun domaine au-dessus de 40 % (API Sirene : 8 sur 35, ~23 %).
Marchés à moins de 3 domaines distincts : aucun ; marchés sans source officielle ou fédération lue : D8 (FACCO en extrait), D9 (FEBEA en extrait), D10 (aucune, hors Sirene).
