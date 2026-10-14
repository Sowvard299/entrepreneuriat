# Segments (phase 1, étape 1) : recherche v3

Date : 2026-10-13. Marchés retenus au point d'arrêt 1 : **A6, A2, A1, C3** (recommandation du coordinateur ;
l'utilisateur a répondu « continue » sans choisir, voir `etat.md`).
Méthode : skill `market-segment-scanner`, étape 4. Faite par le coordinateur **sans nouvelle recherche web**
(budget épuisé), à partir des synthèses de la phase 0. Conséquence : presque tous les comptages et tous les paniers
sont des [HYPOTHÈSE] à confirmer par les chercheurs de l'étape 2. Les notes sont provisoires.

Potentiel annuel = clients × panier annuel × 10 % de pénétration.
Score = Valeur 30 % + Accessibilité 25 % + Sous-servi 20 % + Disposition à payer 15 % + Avantage équipe 10 % (0-10).
Axes : P = profil du client, N = sous-secteur, D = déclencheur, B = besoin, Z = zone, C = canal.

## A6 : Bailleurs privés, logements F interdits à la location au 01/01/2028

Base : 720 000 logements F en location privée (A6-p1 ✔). Panier d'un accompagnement (audit, devis, aides, suivi) :
1 500 à 5 000 € par logement [HYPOTHÈSE], ponctuel. Marché ponctuel jusqu'en 2028, puis classe E en 2034.

| ID | Segment (qui, où, quand, ce qu'ils achètent aujourd'hui) | Axes | Calcul du potentiel | V | A | S | P | Av | Score |
|----|------|------|------|---|---|---|---|----|-------|
| A6-S1 | Bailleurs de 1-2 logements F en Île-de-France, à la relocation ou au renouvellement de bail ; achètent un DPE (100-250 €) puis des devis d'artisans en direct | P, Z, D | 100 000 [H] × 2 000 € × 10 % = 20 M€ (≈ 7 M€/an jusqu'en 2028) | 10 | 5 | 8 | 6 | 4 | 7,15 |
| A6-S2 | SCI familiales de 3 à 10 logements dont au moins un F, France ; gèrent en direct ou via un comptable | P, N, C | 60 000 [H] × 5 000 € × 10 % = 30 M€ | 10 | 6 | 7 | 7 | 4 | 7,35 |
| A6-S3 | Agences de gestion locative (NAF 68.31Z) qui gèrent des mandats F : plan de mise en conformité payé par l'agence ou le bailleur | P, C, B | 8 000 agences [H] × 3 000 €/an × 10 % = 2,4 M€/an | 6 | 8 | 7 | 5 | 5 | 6,45 |
| A6-S4 | Propriétaires de studios ≤ 30 m² à Paris (DPE défavorable aux petites surfaces) | P, Z, B | 40 000 [H] × 1 500 € × 10 % = 6 M€ | 8 | 5 | 6 | 6 | 3 | 6,05 |
| A6-S5 | Bailleurs qui préfèrent vendre leur F plutôt que rénover | D, B | 200 000 [H] ; activité réglementée (carte T, loi Hoguet) | 8 | 5 | 5 | 6 | 3 | 5,85 |
| A6-S6 | Bailleurs d'un F en copropriété dont l'isolation dépend d'un vote en assemblée | P, D, C | 400 000 [H] × 1 000 € × 10 % = 40 M€ | 10 | 4 | 7 | 4 | 3 | 6,30 |
| A6-S7 | Bailleurs de maisons F en villes moyennes et zones rurales, peu d'artisans RGE | P, Z | 200 000 [H] × 2 500 € × 10 % = 50 M€ | 10 | 3 | 8 | 5 | 3 | 6,40 |
| A6-S8 | Investisseurs LMNP (meublé) avec un F, joignables via CGP et comptables LMNP | P, N, C | 100 000 [H] × 2 000 € × 10 % = 20 M€ | 10 | 6 | 7 | 6 | 4 | 7,20 |
| A6-S9 | Bailleurs non-résidents (expatriés) avec un F en France, gestion à distance | P, Z, B | 30 000 [H] × 3 500 € × 10 % = 10,5 M€ | 10 | 4 | 8 | 8 | 3 | 7,10 |
| A6-S10 | Petites foncières et investisseurs de 10 à 50 logements | P, N, B | 5 000 [H] × 15 000 € × 10 % = 7,5 M€ | 10 | 6 | 5 | 8 | 4 | 7,10 |

## A2 : Tertiaire > 1 000 m² (déclaration OPERAT annuelle, GTB obligatoire au 01/01/2027)

Base : environ 340 000 entités assujetties (A2-p2, ≈ non vérifié). Panier : déclaration et suivi OPERAT plus
assistance GTB, 2 000 à 4 000 €/an [HYPOTHÈSE], récurrent. Avantage équipe : énergie B2B (EDF).

| ID | Segment | Axes | Calcul du potentiel | V | A | S | P | Av | Score |
|----|------|------|------|---|---|---|---|----|-------|
| A2-S1 | Supermarchés indépendants adhérents (Leclerc, Intermarché, Système U…) > 1 000 m², France | P, N, C | 6 000 [H] × 3 000 € × 10 % = 1,8 M€/an | 6 | 8 | 6 | 7 | 8 | 6,85 |
| A2-S2 | PME propriétaires-occupantes de bureaux de 1 000 à 5 000 m² | P, N, B | 15 000 [H] × 2 500 € × 10 % = 3,75 M€/an | 8 | 6 | 7 | 5 | 7 | 6,75 |
| A2-S3 | Hôtels indépendants > 1 000 m² (11 253 hôtels indépendants, D5-p1) | P, N | 4 000 [H] × 2 500 € × 10 % = 1 M€/an | 6 | 8 | 7 | 5 | 6 | 6,55 |
| A2-S4 | EHPAD et cliniques privés indépendants | N, B | 3 500 [H] × 4 000 € × 10 % = 1,4 M€/an | 6 | 7 | 5 | 7 | 6 | 6,20 |
| A2-S5 | Établissements scolaires privés (gérés par des bénévoles) | N, P | 7 000 [H] × 2 000 € × 10 % = 1,4 M€/an | 6 | 7 | 8 | 4 | 5 | 6,25 |
| A2-S6 | Entrepôts et sites logistiques chauffés | N | 5 000 [H] × 4 000 € × 10 % = 2 M€/an | 6 | 5 | 5 | 6 | 6 | 5,55 |
| A2-S7 | Concessions automobiles > 1 000 m² | N, P | 4 000 [H] × 2 500 € × 10 % = 1 M€/an | 6 | 7 | 7 | 6 | 6 | 6,45 |
| A2-S8 | Salles de sport et centres de loisirs > 1 000 m² | N | 2 000 [H] × 2 500 € × 10 % = 0,5 M€/an | 5 | 7 | 7 | 5 | 5 | 5,90 |
| A2-S9 | Petits bailleurs de bureaux (immeuble loué), obligation partagée avec le locataire | P, B | 10 000 [H] × 3 000 € × 10 % = 3 M€/an | 8 | 5 | 7 | 5 | 6 | 6,40 |
| A2-S10 | Grandes surfaces spécialisées indépendantes (bricolage, jardinerie) | N, P | 3 000 [H] × 2 500 € × 10 % = 0,75 M€/an | 5 | 7 | 7 | 5 | 6 | 6,00 |

## A1 : TPE/PME, facturation électronique (émission obligatoire au 01/09/2027 ✔)

Base : environ 10 M d'assujettis à la TVA (A1-p3, non vérifié). Panier : mise en place 300 à 3 000 € et/ou
abonnement 10 à 30 €/mois [HYPOTHÈSE]. Fenêtre qui se ferme après septembre 2027 sauf abonnement.

| ID | Segment | Axes | Calcul du potentiel | V | A | S | P | Av | Score |
|----|------|------|------|---|---|---|---|----|-------|
| A1-S1 | TPE du bâtiment (1-9 salariés, NAF 43) qui facturent sur Word ou Excel | P, N, B | 150 000 [H] × 580 € × 10 % = 8,7 M€ | 10 | 8 | 6 | 5 | 4 | 7,35 |
| A1-S2 | Cabinets d'expertise comptable (23 827, API NAF 69.20Z) : migration de leur portefeuille de TPE en marque blanche | P, C, B | 23 827 × 3 000 € × 10 % = 7,1 M€ | 10 | 8 | 6 | 6 | 5 | 7,60 |
| A1-S3 | Associations assujetties à la TVA | P, N | 50 000 [H] × 300 € × 10 % = 1,5 M€ | 7 | 6 | 8 | 3 | 4 | 6,05 |
| A1-S4 | Micro-entrepreneurs B2B (consultants, freelances) | P, D | 1 000 000 [H] × 100 € × 10 % = 10 M€ | 10 | 7 | 3 | 2 | 4 | 6,05 |
| A1-S5 | PME de 10 à 49 salariés sur un logiciel de gestion ancien à migrer | P, B, D | 60 000 [H] × 2 000 € × 10 % = 12 M€ | 10 | 7 | 5 | 7 | 4 | 7,20 |
| A1-S6 | Exploitations agricoles assujetties à la TVA | N, P | 250 000 [H] × 300 € × 10 % = 7,5 M€ | 10 | 5 | 7 | 4 | 5 | 6,75 |
| A1-S7 | Négoces et grossistes B2B de 1 à 49 salariés (gros volumes de factures) | N, P, B | 40 000 [H] × 1 500 € × 10 % = 6 M€ | 10 | 7 | 5 | 7 | 4 | 7,20 |
| A1-S8 | Professions libérales assujetties (architectes, géomètres, conseils) | P, N | 100 000 [H] × 300 € × 10 % = 3 M€ | 10 | 6 | 5 | 4 | 3 | 6,40 |
| A1-S9 | Restaurants (réception des factures fournisseurs, e-reporting) ; 114 659 actifs (API, A7) | N | 114 659 × 200 € × 10 % = 2,3 M€ | 9 | 8 | 4 | 3 | 3 | 6,25 |
| A1-S10 | Transporteurs routiers TPE (NAF 49.41) | N, P | 30 000 [H] × 800 € × 10 % = 2,4 M€ | 9 | 7 | 6 | 5 | 3 | 6,70 |

## C3 : Batteries domestiques (volume ×2 en 2025 ✔, rachat du surplus à 4 c€/kWh)

Base : 10 209 installations en 2025 ✔ ; prix d'une batterie 3 500 à 15 000 € ✔ (C3-p5 corrigé) ; parc solaire
d'environ 1,3 M de foyers (non vérifié). L'équipe ne pose pas : rôle de génération de demande ou de vente.

| ID | Segment | Axes | Calcul du potentiel | V | A | S | P | Av | Score |
|----|------|------|------|---|---|---|---|----|-------|
| C3-S1 | Foyers solaires équipés de 2017 à 2024 qui vendent leur surplus, Sud de la France (rénovation) | P, Z, D | 400 000 [H] × 7 000 € × 10 % = 280 M€ (vente de matériel, pas notre CA) | 10 | 4 | 6 | 6 | 3 | 6,40 |
| C3-S2 | Installateurs RGE photovoltaïque qui achètent des contacts qualifiés pour vendre des batteries | P, C, B | 5 000 [H] × 6 000 €/an × 10 % = 3 M€/an | 8 | 8 | 6 | 7 | 7 | 7,35 |
| C3-S3 | Foyers avec voiture électrique et panneaux | P, B | 150 000 [H] × 8 000 € × 10 % = 120 M€ (matériel) | 10 | 3 | 6 | 7 | 3 | 6,30 |
| C3-S4 | Nouveaux acheteurs de solaire (offre panneau + batterie) | D, B | 50 000 [H] × 3 000 € × 10 % = 15 M€ | 10 | 4 | 4 | 6 | 3 | 6,00 |
| C3-S5 | Agriculteurs avec hangar photovoltaïque en autoconsommation | N, P | 30 000 [H] × 20 000 € × 10 % = 60 M€ (matériel) | 10 | 5 | 6 | 5 | 5 | 6,70 |
| C3-S6 | Petits commerces et artisans avec panneaux en toiture (autoconsommation B2B) | P, N, B | 20 000 [H] × 15 000 € × 10 % = 30 M€ (matériel) | 10 | 6 | 7 | 5 | 7 | 7,35 |
| C3-S7 | Maisons en zones à coupures fréquentes (secours) | Z, B | 50 000 [H] × 8 000 € × 10 % = 40 M€ (matériel) | 10 | 3 | 7 | 5 | 3 | 6,20 |
| C3-S8 | Foyers en option Tempo ou heures creuses qui veulent optimiser leur facture | P, B | 100 000 [H] × 6 000 € × 10 % = 60 M€ (matériel) | 10 | 4 | 7 | 4 | 7 | 6,70 |
| C3-S9 | Résidences secondaires équipées de panneaux | P, Z | non calculé | 8 | 3 | 6 | 3 | 3 | 5,10 |
| C3-S10 | Copropriétés et lotissements en autoconsommation collective | P, B, C | 2 000 [H] × 30 000 € × 10 % = 6 M€ | 10 | 5 | 8 | 4 | 6 | 7,05 |

## Top 12 global (provisoire)

| Rang | ID | Segment | Score |
|------|----|---------|-------|
| 1 | A1-S2 | Experts-comptables : migration de leurs TPE à la facture électronique | 7,60 |
| 2 | A6-S2 | SCI familiales de 3 à 10 logements avec un F | 7,35 |
| 3 | A1-S1 | TPE du bâtiment qui facturent sur Word/Excel | 7,35 |
| 4 | C3-S2 | Installateurs RGE : contacts qualifiés pour batteries | 7,35 |
| 5 | C3-S6 | Commerces et artisans avec panneaux en toiture | 7,35 |
| 6 | A6-S8 | Investisseurs LMNP avec un F, via CGP et comptables | 7,20 |
| 7 | A1-S5 | PME 10-49 sur logiciel ancien | 7,20 |
| 8 | A1-S7 | Négoces et grossistes B2B | 7,20 |
| 9 | A6-S1 | Bailleurs de 1-2 F en Île-de-France | 7,15 |
| 10 | A6-S9 | Bailleurs non-résidents | 7,10 |
| 11 | A6-S10 | Petites foncières de 10 à 50 logements | 7,10 |
| 12 | C3-S10 | Autoconsommation collective | 7,05 |
| (13) | A2-S1 | Supermarchés indépendants (OPERAT + GTB) | 6,85 |

A2 n'a aucun segment dans le Top 12 : clients peu nombreux, donc valeur plus faible. A2-S1 est signalé en 13e
parce qu'il combine récurrence et avantage énergie de l'équipe ; à substituer à C3-S10 si l'utilisateur le souhaite.

## Chemins d'expansion (finalistes)

- **A1** : experts-comptables (S2) → leurs TPE du bâtiment et négoces (S1, S7) → abonnement de suivi après
  septembre 2027 (e-reporting, relances, rapprochement). Risque : fenêtre ponctuelle, éditeurs gratuits.
- **A6** : SCI familiales et LMNP (S2, S8) → petites foncières (S10) → classe E en 2034 → copropriétés (A10).
  Risque : agrément « Mon Accompagnateur Rénov' » et projet d'assouplissement de la loi.
- **C3** : installateurs RGE (S2, contacts batteries) → mêmes installateurs pour pompes à chaleur et
  rénovation → commerces avec panneaux (S6). Risque : plateformes de génération de contacts déjà présentes.

## Étape 2 à faire (chercheurs par paires de segments, vagues de 4 au plus)

Voir `etat.md`, section « Reprise », pour les missions exactes.
