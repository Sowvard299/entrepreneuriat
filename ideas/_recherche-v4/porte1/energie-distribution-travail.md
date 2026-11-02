# Énergie : voie distribution et reprise (porte 1) - fichier de travail
Mission : (a) produits/logiciels énergie prouvés à l'étranger, distribuables en France ; (b) petites entreprises énergie à reprendre.
Date : 2026-11-02. Recherches web utilisées : 11 / 15. WebFetch : 6 (2 en 403 Fusacq, 1 legalvision sans chiffre). API Sirene : 5 appels.
Preuves : 12. Domaines distincts : 9 (uimm, fusacq, fournisseurs-electricite, copeps, api.gouv, assemblee-nationale, jobijoba, les-energies-renouvelables, connaissancedesenergies). Plafond 40 % respecté (uimm 3/12 = 25 %).
Statut : partiel. Manque : programmes partenaires publics avec commissions affichées (non trouvés), annonces BPI Transmission/CRA (non ouvertes), TrustMRR/Acquire énergie (aucun résultat), CA vérifiables des vendeurs, marché plug-in solaire France.

### E-DIS-01 : Bureau d'études thermique à vendre, 746 k€ de CA
- Acteur / marché : bureau d'études ingénierie thermique/hydraulique/aéraulique, cédé par son dirigeant retraité
- Type : argent dépensé (prix affiché, non encore payé)
- Source : https://opportunites-industrielles.uimm.fr/imprimer-annonce-vente,88012-E (extrait de recherche ; l'ID exact de l'annonce n'est pas certain, à rouvrir) (date : inconnue, CA 2023)
- Citation : « le prix affiché est de 450 k€ (apport minimum de 150 k€ demandé à l'acquéreur) »
- Chiffres : CA 2023 746 k€, prix 450 k€ (0,6 x CA), apport 150 k€
- Ce que ça dit pour nous : reprise possible mais apport 150 k€ > budget 5 000 € ; hors piste rapide.

### E-DIS-02 : Bureau d'études thermique et énergétique, 490 k€
- Acteur / marché : bureau d'études, 100 % des actions, immobilier exclu
- Type : argent dépensé (prix affiché)
- Source : opportunites-industrielles.uimm.fr (extrait de recherche, URL précise non retenue) (date inconnue)
- Citation : « cession 100% des actions (prix cession hors réserves financières) »
- Chiffres : prix 490 k€, CA non vu
- Ce que ça dit pour nous : même ordre de grandeur, financement bancaire/vendeur obligatoire.

### E-DIS-03 : Installateur photovoltaïque B2B jeune, 300 k€
- Acteur / marché : installateur PV B2B, Auvergne-Rhône-Alpes/Sud-Est, moins de 5 ans
- Type : argent dépensé (prix souhaité)
- Source : fusacq.com (extrait de recherche ; page 403 à l'ouverture) (date : 2026)
- Citation : « Prix de cession souhaité : 300 k€ »
- Chiffres : 300 k€ ; CA non lu
- Ce que ça dit pour nous : prix demandé hors budget rapide ; CA à vérifier via API Sirene.

### E-DIS-04 : Électricité générale à 260 k€ pour 610 k€ de CA
- Acteur / marché : entreprise d'électricité générale
- Type : argent dépensé (prix fixé)
- Source : fusacq.com (extrait de recherche) (date inconnue)
- Citation : « Le prix de cession est fixé à 260 000 € »
- Chiffres : CA environ 610 k€, prix 260 k€ (0,43 x CA)
- Ce que ça dit pour nous : repère de multiple bas (0,4 à 0,6 x CA) ; activité artisanale, métier d'employeur.

### E-DIS-05 : Petit actif photovoltaïque IdF, 45 k€
- Acteur / marché : actif PV Île-de-France
- Type : argent dépensé (prix de cession)
- Source : fusacq.com (extrait de recherche) (date : T1 2024 pour le CA)
- Citation : « Le prix de cession est de 45 k€ »
- Chiffres : CA T1 2024 : 65 k€ ; prix 45 k€
- Ce que ça dit pour nous : seule reprise sous 50 k€ vue, mais nature de l'actif (centrale ou société) à confirmer.

### E-DIS-06 : Courtage en énergie, commission payée par le fournisseur
- Acteur / marché : courtier vend à TPE/PME, payé par le fournisseur
- Type : argent dépensé (modèle)
- Source : https://fournisseurs-electricite.com/contrat-electricite-gaz/comparatif/courtier-pro (ouverte) (date : MAJ 2026-05-07)
- Citation : « commission d'apport, intégrée à son coût d'acquisition global »
- Chiffres : pas de taux sur la page ; un comparateur évoque 2 à 5 % du contrat (extrait de recherche, confiance faible)
- Ce que ça dit pour nous : voie apporteur d'affaires = revenu récurrent sur contrats ; page écrite par Selectra, courtier (conflit d'intérêt, confiance faible).

### E-DIS-07 : Courtage, taux et nombre d'acteurs
- Acteur / marché : courtiers énergie PME
- Type : tendance
- Source : https://copeps.fr/actualites/courtage-en-energie-pme/ (ouverte) (date inconnue)
- Citation : « commission versée par le fournisseur d'électricité ou de gaz »
- Chiffres : aucun taux ni nombre de courtiers ; « -25 % » de facture non sourcé
- Ce que ça dit pour nous : 3 types d'acteurs (digitaux, cabinets, réseaux de proximité) ; taille de marché à calculer, pas publiée.

### E-DIS-08 : Concurrence courtage via Sirene
- Acteur / marché : entreprises actives dont le nom ou l'activité contient « courtage energie »
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?q=courtage%20energie&etat_administratif=A&per_page=1 (API ouverte) (date : 2026-11-02)
- Citation : « total_results »: 18 (recherche texte, très incomplète, pas de code NAF dédié)
- Chiffres : 18 résultats texte seulement ; NAF 43.21A (électricité) plafonné 10 000 ; NAF 35.14Z (commerce d'électricité) : 1 399 actives
- Ce que ça dit pour nous : le nombre de courtiers n'est pas mesurable par Sirene ; [HYPOTHÈSE] à tester via annuaire.

### E-DIS-09 : Apporteur d'affaires PV, barèmes affichés (foncier)
- Acteur / marché : développeurs ENR payant des apporteurs de sites
- Type : argent dépensé (offres)
- Source : jobijoba.com (offre, extrait de recherche) (date inconnue)
- Citation : « de 8 000 € (agrivoltaïque) à 13 000 € (flottant) » (paraphrase du résumé de recherche, non copiée de la page)
- Chiffres : 8 à 13 k€ par projet ; autre annonce : 1 000 à 3 000 € par MWc sécurisé
- Ce que ça dit pour nous : commissions visibles mais pour du foncier/MW, cycle long (> 6 mois) ; pas de contrat prouvé payé.

### E-DIS-10 : Plug-in solaire, 1,3 M d'unités en Allemagne
- Acteur / marché : kits balcon, Allemagne, distribués en France ?
- Type : tendance (Allemagne uniquement, ne se transpose pas)
- Source : https://www.les-energies-renouvelables.eu/article/actualites/energies/solaire-de-balcon-lessor-du-modele-plug-in-en-allemagne-533/ (extrait de recherche) (date inconnue)
- Citation : « plus de 1,3 million » (BVSS, relayé par la recherche ; formulation à rouvrir)
- Chiffres : Allemagne : 1 M enregistrés juin 2025 (BSW-Solar), >1,3 M (BVSS) ; Europe 4 à 5 M estimés. Rien sur la France.
- Ce que ça dit pour nous : produit prouvé à l'étranger, mais concurrents français (Sunology, vu en extrait) déjà présents : angle distribution non prouvé.

### E-DIS-11 : Kraken (logiciel utilitaire) licencié à EDF
- Acteur / marché : Octopus/Kraken, SaaS de facturation et relation client pour fournisseurs
- Type : argent dépensé (licence EDF, montant inconnu)
- Source : https://news.bloomberglaw.com/environment-and-energy/octopus-energy-plans-to-spin-off-technology-arm-kraken-3 (extrait de recherche) (date : inconnue)
- Citation : « already licensed to other energy providers such as Electricite de France » (paraphrase)
- Chiffres : 70 M de comptes gérés (extrait) ; aucun programme revendeur ou commission trouvé
- Ce que ça dit pour nous : pas de voie distribution accessible à 6 étudiants (vente aux grands fournisseurs). Piste écartée.

### E-DIS-12 : Contre-preuve : régulation du courtage et démarchage
- Acteur / marché : courtiers et démarcheurs énergie
- Type : contre-preuve (obligation réglementaire)
- Source : https://www.assemblee-nationale.fr/dyn/17/textes/l17b1845_proposition-loi.pdf (extrait de recherche) (date : XVIIe législature, 2025-2026 probable)
- Citation : « inscription obligatoire de tous les courtiers en énergie sur un registre national dédié »
- Chiffres : proposition de loi non vérifiée comme adoptée ; DGCCRF : « 140 procès-verbaux pénaux » (moneyvox, rénovation énergétique)
- Ce que ça dit pour nous : image dégradée du secteur, risque réglementaire (commissions, responsabilité du fournisseur) ; à vérifier avant tout lancement.

## Sources non lues
- https://www.fusacq.com/imprimer-annonce-vendeur-92747fr_fr_ et 92726 : 403.
- trustmrr.com, acquire.com : non ouverts, aucun résultat énergie en recherche.
- BPI Transmission, CRA : non consultés (budget).
- legalvision.fr apporteur PV : ouverte, aucun montant.
