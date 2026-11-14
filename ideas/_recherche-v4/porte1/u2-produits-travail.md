# U2 produits physiques / e-commerce : fichier de travail
Mission : porte 1, produits physiques DTC, abonnements de consommables. Date : 2026-11-03. Recherches web : 9/15. Preuves : 12. Domaines distincts : 8 (ecommerce-nation, xerfi, recherche-entreprises.api.gouv.fr, frenchweb, ultrapremiumdirect, trustpilot, iqvia, lequotidiendupharmacien) + trustmrr.
Règle : chiffres issus de pages ouvertes (WebFetch ; comptes via l'API recherche-entreprises en curl, mention « API »). Les citations entre « » viennent des réponses de l'outil WebFetch (résumeur), pas d'un texte brut relu par moi. Statut : PARTIEL (2 modèles, pas 3).
Limite : Trustpilot = 4 preuves sur 12 (33 %).

### U2-PROD-01 : E-commerce de produits France 2024
- Acteur / marché : marché français, valeur, périmètre Fevad
- Type : tendance
- Source : https://www.ecommerce-nation.fr/e-commerce-france-2025-chiffres-cles-fevad/ (ouverte ; données 2024 relayées de la Fevad ; Fevad non ouverte)
- Citation : « volume d'affaires record » (produits 66,9 Md€, +6 % ; services 108,4 Md€)
- Chiffres : produits 66,9 Md€ +6 % en 2024 (valeur, France). Bilan 2025 (76,1 Md€ produits) vu seulement en extrait de recherche : [NON OUVERT]
- Ce que ça dit pour nous : le e-commerce de produits croît ~6 %/an (sous le seuil de 8 %) ; pas de 2e source institutionnelle.

### U2-PROD-02 : Petfood France 2024
- Acteur / marché : aliments pour animaux, France, valeur
- Type : tendance (contre-preuve partielle)
- Source : https://www.xerfi.com/presentationetude/L-alimentation-pour-animaux-de-compagnie_21IAA13 (ouverte, date 2025-2026)
- Citation : « reste globalement stable en 2025, malgré un léger recul des volumes. »
- Chiffres : > 6,3 Md€ en 2024 tous circuits ; Mars + Nestlé = 83 % du CA du panel fabricants 2023 ; ~50 % via grande distribution alimentaire. Vendeur de rapports : confiance faible.
- Ce que ça dit pour nous : très gros marché mais stable en volume, concentré côté fabricants.

### U2-PROD-03 : Ultra Premium Direct (N+U Pet Food), comptes
- Acteur / marché : croquettes premium en direct, abonnement, B2C
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=ULTRA%20PREMIUM%20DIRECT (API, vue 2026-11-03 ; siren 799071253)
- Citation : « ca »: 67346987, « resultat_net »: 3747254 (exercice 2024)
- Chiffres : CA 67,3 M€, résultat net 3,7 M€ (2024). Rattachement de la société « NATURA PLUS ULTRA PET FOOD » à la marque UPD : [HYPOTHÈSE].
- Ce que ça dit pour nous : un acteur DTC rentable à ~67 M€ existe déjà en France.

### U2-PROD-04 : UPD, trajectoire annoncée
- Acteur / marché : idem
- Type : argent dépensé
- Source : https://www.frenchweb.fr/pet-food-la-dnvb-ultra-premium-direct-passe-a-la-vitesse-superieure/424129 (ouverte ; 2021-06-14)
- Citation : tarifs « 30 % à 40 % » inférieurs à la moyenne (paraphrase du résumeur)
- Chiffres : prévision CA 2021 33,5 M€, levée 68 M€ (Eurazeo), 110 salariés, usine 4 M€, marketing 35-45 % du CA prévu 2022.
- Ce que ça dit pour nous : capital lourd, marketing ~40 % du CA.

### U2-PROD-05 : UPD, prix publics
- Acteur / marché : idem
- Type : argent dépensé
- Source : https://www.ultrapremiumdirect.com/ (ouverte, 2026-11-03)
- Citation : « Plus de 1,1 million de chiens et chats conquis »
- Chiffres : saumon frais chiot 12 kg « Dès €67.90 » (5,66 €/kg) ; Care digestion « Dès €66.90 » ; chiot super premium « Dès €47.90 » ; produit digestion 4,7/5, 4 916 avis ; abonnement -10 %.
- Ce que ça dit pour nous : ≥ 3 prix publics (OK) ; 1,1 M animaux (chiffre du vendeur).

### U2-PROD-06 : UPD, avis négatifs
- Acteur / marché : idem
- Type : plainte
- Source : https://fr.trustpilot.com/review/ultrapremiumdirect.com?stars=1&stars=2 (ouverte, 2026-11-03)
- Citation : « Après 7 livraisons ratés sur 12 j'abandonne... » (6 oct. 2026) ; « pour résilier c'est un vrai casse tête ils ne répondent plus » (29 sept. 2026)
- Chiffres : 4,0/5, 3 965 avis, 11 % de 1-2 étoiles.
- Ce que ça dit pour nous : faiblesse = livraison et résiliation (service), pas le produit.

### U2-PROD-07 : Japhy, avis et comptes
- Acteur / marché : croquettes sur-mesure en abonnement
- Type : plainte
- Source : https://fr.trustpilot.com/review/japhy.fr?stars=1&stars=2 (ouverte, 2026-11-03)
- Citation : « la marque vous harcèle littéralement » (17 oct. 2026)
- Chiffres : 4,7/5, 17 355 avis, ~7 % de 1-2 étoiles. API (siren 830695532) : CA 2025 = 0 (confidentiel), résultat net 497 262 €. CA 6,3 M€ (2022) : [NON OUVERT] (page Businesscoot 404).
- Ce que ça dit pour nous : Japhy bien noté, base clients large ; plainte = relances.

### U2-PROD-08 : Dog Chef, contre-preuve
- Acteur / marché : repas frais chien, Belgique/France
- Type : contre-preuve
- Source : https://www.trustpilot.com/review/dogchef.com?stars=1&stars=2 (ouverte, 2026-11-03)
- Citation : « We have found plastic pieces, some of them rather large inside the food » (27 août 2026)
- Chiffres : 4,7/5, 5 546 avis, ~3-4 % de 1-2 étoiles. CA et prix FR : [NON OUVERT] (page 404).
- Ce que ça dit pour nous : le frais est déjà servi, et bien noté.

### U2-PROD-09 : Compléments alimentaires France 2025
- Acteur / marché : compléments, France, valeur (pharmacie + parapharmacie + e-pharmacie + Amazon)
- Type : tendance
- Source : https://www.iqvia.com/locations/france/blogs/2026/04/complements-alimentaires-en-france (ouverte ; 2026-04)
- Citation : « Un marché de 2 milliards d'euros en pleine accélération »
- Chiffres : ~2 Md€ 2025, +4,7 % ; en ligne 8,3 % des ventes et 28 % de la croissance (13 % en 2024) ; Europe 19,9 Md€ (+5,9 %).
- Ce que ça dit pour nous : l'en ligne gagne du terrain, mais croissance < 8 % ; source privée, confiance moyenne.

### U2-PROD-10 : Compléments, circuit pharmacie
- Acteur / marché : idem
- Type : contre-preuve
- Source : https://www.lequotidiendupharmacien.fr/medicament-parapharmacie/lofficine-toujours-premier-lieu-de-vente-des-complements-alimentaires (ouverte, partielle ; 2025-03-28)
- Citation : « La croissance a été dynamique en 2024 »
- Chiffres : officine = 55 % de la valeur. Montant de l'article illisible : [NON UTILISÉ]. Synadiet non ouvert.
- Ce que ça dit pour nous : le DTC pèse peu face à la pharmacie.

### U2-PROD-11 : Nutri&Co, comptes et avis
- Acteur / marché : compléments DTC (collagène, magnésium, whey)
- Type : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/nutriandco.com (ouverte) ; API siren 825396492
- Citation : « Argent jeté à la poubelle. » (22 sept. 2026)
- Chiffres : 4,6/5, 5 674 avis (1 867 sur 12 mois), 6 % de 1-2 étoiles, réponse à 88 % des avis négatifs ; 2 852 avis sur le collagène marin ; comptes 2025 : CA 0 (confidentiel), résultat net +2,44 M€. Prix publics : [NON OUVERT] (page produit 404, accueil sans prix).
- Ce que ça dit pour nous : un DTC rentable existe déjà ; débit d'avis élevé.

### U2-PROD-12 : Piste étrangère (TrustMRR)
- Acteur / marché : e-commerce, TrustMRR
- Type : tendance
- Source : https://trustmrr.com/ (ouverte)
- Citation : « Supliful » MRR 177 843 $
- Chiffres : seul cas physique/CPG, plateforme B2B de marque blanche. Aucun modèle étranger absent de France démontré.
- Ce que ça dit pour nous : critère « absent en France » non prouvé dans cette session.

## Croyance la plus fragile et test (les deux modèles)
- Croyance : un entrant acquiert des clients à un coût inférieur à la marge de 12-24 mois face à UPD, Japhy, Nutri&Co. Test : fausse porte sur une niche (chiens seniors, nutrition sportive), 500 € de publicité, coût par précommande. Coût d'acquisition DNVB 32,4 € (PayPlug) : [NON OUVERT].

## Sources non lues
- Businesscoot Japhy (404) ; petfoodindustry.com (403) ; pepette.fr (domaine introuvable) ; dogchef.com/fr-fr (404) ; nutriandco.com produit (404) ; Fevad, Synadiet, Insee (non ouverts).
