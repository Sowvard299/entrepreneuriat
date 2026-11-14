# Écran S9601 Blanchisserie-teinturerie (travail)
Mission : croissance réelle ou artefact, modèles qui encaissent, meilleur modèle. Date : 2026-11-03.
Recherches web utilisées : 5/15. Preuves : 15. Domaines distincts : 10. Statut : partiel (prix publics N2 B2B manquants ; avis du modèle retenu non trouvés).
Contrôle donnees.py : 15 preuves, 11 domaines, max 24 % (recherche-entreprises). verifier-citations RÉSUMÉ : OK=3, ABSENT=10, BLOQUE=1, EXTRAIT=1. Les 10 ABSENT sont des lignes de sortie de outils/donnees.py (S96-01 à S96-10), pas du texte de page : la citation vient du résultat de l'outil, le script lit le JSON brut. À rejouer par le vérificateur.

### S96-01 : Eurostat, CA du secteur
- Acteur / marché : S9601 France, CA net (valeur)
- Type : argent dépensé
- Source : https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=FR&geo=FR&nace_r2=S9601&indic_sbs=NETTUR_MEUR (2026-11-03 ; N1 ; Eurostat)
- Citation : « 2023 : 3 495 M€ ; 7 363 entreprises »
- Chiffres : 2021 1 640 ; 2022 1 937 ; 2023 3 495 ; 2024 3 925 M€ ; entreprises 7 267 puis 7 415 (stable)
- Ce que ça dit pour nous : saut de +80 % en 2023 avec le même nombre d'entreprises = probable rupture de série, pas croissance.

### S96-02 : INSEE, indice de CA (contre-preuve de la croissance +42 %/an)
- Acteur / marché : 96.01, indice en valeur
- Type : contre-preuve
- Source : https://api.insee.fr/melodi/data/DS_ICA?ACTIVITY=96.01&FREQ=M&SEASONAL_ADJUST=Y&maxResult=5000 (2026-11-03 ; N1 ; INSEE)
- Citation : « Croissance annuelle moyenne sur 3 ans (2022-2025) : +8.3 %/an »
- Chiffres : indice 2021=100 ; 2022 123,8 ; 2023 140,4 ; 2024 150,8 ; 2025 157,4 ; 5 ans +10,3 %/an, prix inclus
- Ce que ça dit pour nous : croissance réelle ~8 %/an en valeur (inflation incluse), pas 34-42 %. Eurostat 2023 = artefact probable.

### S96-03 : acteurs 96.01A (blanchisserie industrielle)
- Acteur / marché : blanchisseries industrielles B2B
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=96.01A&etat_administratif=A&ca_min=5000000&per_page=25 (2026-11-03 ; N1 ; Sirene/comptes déposés)
- Citation : « NETEXIAL (SIREN 343234142) : 308.6 M€ en 2025 »
- Chiffres : Netexial 308,6 ; Les Lavandières 227,7 ; MEWA 95,8 ; Kalhyge 65,7 ; Anett Deux 48,1 ; Bulle de Linge 40,1 M€ ; 45 acteurs >= 5 M€ ; 752 entreprises actives dont 161 de 10 salariés et plus ; part des 3 premiers 16,1 % (borne basse)
- Ce que ça dit pour nous : plus de 3 acteurs à CA déposé, fragmenté ; capital lourd.

### S96-04 : acteurs 96.01B (pressing, laverie)
- Acteur / marché : pressings et laveries
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=96.01B&etat_administratif=A&ca_min=1000000&per_page=25 (2026-11-03 ; N1 ; Sirene/comptes déposés)
- Citation : « 5ASEC R I F (SIREN 418782025) : 38.3 M€ en 2025 »
- Chiffres : 10 961 entreprises actives ; 8 475 non employeurs ; 30 avec CA >= 1 M€ ; 3 premiers 1,2 %
- Ce que ça dit pour nous : atomisé, micro-structures : peu d'entreprises passent 1 M€.

### S96-05 : marchés publics « blanchisserie »
- Acteur / marché : hôpitaux, EHPAD publics, collectivités
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22blanchisserie%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (2026-11-03 ; N1 ; DECP)
- Citation : « 2025 : 275 marchés  215.5 M€ »
- Chiffres : 2023 35 marchés 29,5 M€ ; 2024 233 marchés 797,8 M€ ; 2026 (en cours) 158 marchés 231,2 M€
- Ce que ça dit pour nous : le bond 2023-2024 vient en partie de la couverture déclarative DECP et d'accords-cadres (valeur maximale) ; plancher, pas total.

### S96-06 : marchés publics « entretien du linge »
- Acteur / marché : idem
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22entretien+du+linge%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (2026-11-03 ; N1 ; DECP)
- Citation : « 2025 : 118 marchés  980.3 M€ »
- Chiffres : 2024 104 marchés 787,6 M€ ; 2022 16 marchés 52,5 M€
- Ce que ça dit pour nous : quelques très gros accords-cadres hospitaliers ; inaccessibles sans usine.

### S96-07 : BODACC « blanchisserie »
- Acteur / marché : blanchisseries
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22blanchisserie%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (2026-11-03 ; N1 ; DILA)
- Citation : « 2025 : 311 »
- Chiffres : 2022 243 ; 2023 270 ; 2024 285 ; 2025 311 ; 2026 (en cours) 308 (annonces, pas entreprises)
- Ce que ça dit pour nous : les procédures collectives remontent depuis 2022 (+28 %), contre le récit de croissance.

### S96-08 : BODACC « pressing »
- Acteur / marché : pressings
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22pressing%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (2026-11-03 ; N1 ; DILA)
- Citation : « 2025 : 254 »
- Chiffres : 2008 268 ; 2022 229 ; 2025 254 (stable)
- Ce que ça dit pour nous : environ 250 annonces par an pour ~11 000 entreprises ; stable.

### S96-09 : EHPAD, clients identifiables
- Acteur / marché : hébergement personnes âgées (87.10A)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=87.10A&etat_administratif=A&per_page=1 (2026-11-03 ; N1 ; API Recherche d'entreprises)
- Citation : « Entreprises actives 87.10A : 3 195 »
- Chiffres : 3 195 (87.10A) + 325 (87.10B) ; 2 680 employeuses ; 1 656 de 50-99 salariés
- Ce que ça dit pour nous : ~3 500 clients B2B identifiables (seuil juste atteint), mais Bulle de Linge en sert déjà 950.

### S96-10 : locations saisonnières, clients identifiables
- Acteur / marché : hébergement touristique de courte durée (55.20Z)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=55.20Z&etat_administratif=A&per_page=1 (2026-11-03 ; N1 ; API Recherche d'entreprises)
- Citation : « Entreprises actives 55.20Z : 102 133 »
- Chiffres : 4 469 employeuses ; 97 107 non employeurs ou inconnus ; hôtels 55.10Z : 39 545 dont 15 081 employeuses
- Ce que ça dit pour nous : beaucoup de clients potentiels, mais la plupart sont des loueurs à très faible volume.

### S96-11 : Bulle de Linge, EHPAD
- Acteur / marché : linge des résidents d'EHPAD, 12 sites
- Type : argent dépensé
- Source : https://www.lejournaldesentreprises.com/article/le-groupe-normand-bulle-de-linge-lance-sa-douzieme-blanchisserie-en-sarthe-en-attendant-dautres-2110369 (2025-01-08 ; N3 ; Journal des Entreprises)
- Citation : « C'est une niche dans un marché très spécialisé de la blanchisserie »
- Chiffres : CA 2023 près de 32 M€, 650 salariés ; plus de 75 000 résidents, 950 établissements (déclaré) ; CA déposé 40,1 M€ en 2025 (S96-03, N1)
- Ce que ça dit pour nous : le modèle encaisse et croît, mais c'est un réseau d'usines : capital élevé.

### S96-12 : prix pressing 5àsec
- Acteur / marché : pressing en franchise, particuliers
- Type : argent dépensé
- Source : https://www.5asec.fr/fr/magasin/lyon-matagotte/ (date inconnue ; N2 ; 5àsec)
- Citation : « Shirt 5,50 € »
- Chiffres : chemise 5,50 ; chemise pliée 6,10 ; pantalon 9,25 ; veste 12,55 ; manteau 23,80 €
- Ce que ça dit pour nous : 3 prix publics B2C N2 existent.

### S96-13 : avis 5àsec
- Acteur / marché : pressing, B2C
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.5asec.fr?stars=1&stars=2 (2026-10-28 ; N3 ; Trustpilot)
- Citation : « Prix double par rapport à celui affiché sans explication »
- Chiffres : 447 avis, note 4,0/5 ; part 1-2 étoiles annoncée 41 % (incohérente avec 4,0 : à recouper) ; plaintes : frais non annoncés, taches, retards
- Ce que ça dit pour nous : faiblesse = prix opaque et délais ; canal unique (Trustpilot).

### S96-14 : prix B2B linge de locations saisonnières
- Acteur / marché : entretien externalisé du linge Airbnb
- Type : argent dépensé
- Source : https://rentaplus.immo/blog/blanchisserie-airbnb-prix/ (2026-10-19 ; N4 ; blog d'un vendeur de location de linge)
- Citation : « Le vrai prix d’une blanchisserie Airbnb se calcule par rotation »
- Chiffres : 26 € HT par rotation T2 (un prestataire francilien), location-entretien 47 € HT, lavage soi-même 22-33 € ; 260 € HT/mois pour 10 rotations
- Ce que ça dit pour nous : un seul prix de prestataire, source commerciale : pas de 3 prix N2 sur ce segment.

### S96-15 : prix au kilo B2B hôtellerie-restauration
- Acteur / marché : blanchisserie hôtelière
- Type : argent dépensé
- Source : https://kolonell.com/fr/blog/site-blanchisserie-industrielle-b2b-toulouse-devis-2026 (2026 ; N5 ; extrait de recherche, [NON OUVERT])
- Citation : « extrait non ouvert, non utilisable »
- Chiffres : aucun utilisable
- Ce que ça dit pour nous : les grilles B2B sont sur devis : prix publics N2 non établis.

## Analyse
- Croissance : en grande partie artefact. Eurostat +80 % en 2023 à nombre d'entreprises constant ; INSEE +8,3 %/an prix inclus (S96-02), juste au seuil ; en volume, plus bas [HYPOTHÈSE, pas de déflateur ouvert].
- Modèle le plus léger : entretien du linge des locations saisonnières et conciergeries, en sous-traitance par rotation. Contre-preuves : S96-07, S96-02, prix d'une seule source.
- Autre modèle : blanchisserie EHPAD (Bulle de Linge) : encaisse, mais capital d'usine.
- Croyance la plus fragile : des conciergeries et loueurs pro paient ~26 € HT par rotation pour la fiabilité plutôt que de laver eux-mêmes. Test porte 2 sans entretien : page « abonnement 10 rotations, prix, date du premier service » avec dépôt remboursable (L.221-14, L.221-18), pub ciblée conciergeries ; seuil écrit avant, calculé sur le coût du clic [HYPOTHÈSE].
- Probabilités datées 2026-11-03 (base SINE ensemble 69 % à 5 ans, classe exacte [HYPOTHÈSE]) : P(porte 2) 20 % ; P(en vie à 3 ans) 60 % ; P(CA >= 500 k€ à 3 ans) 10 %. Aucune n'est déplacée par une preuve N1-N2 sur le modèle lui-même.

## Sources non lues
- https://www.5asec.fr/wp-content/uploads/2025/08/d40198de-eb48-4c0c-8667-79d435589af1-Plaquette5secBusiness.pdf : PDF non ouvert.
- https://paca.ars.sante.fr/system/files/2024-07/Blanchisserie.pdf : non ouvert.
