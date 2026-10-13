# Analyse de marché et dimensionnement (TAM, SAM, SOM)

**Phase:** 3, Research (Wave 1, skill `market-sizing`)
**Project:** recrutement-garages
**Date:** 2026-10-12
**Confidence:** Medium (volumes sourcés ; part des TPE et taux d'embauche = hypothèses)

---

## 1. Définition du marché

- **Besoin** : un patron de garage ou de carrosserie qui n'arrive pas à pourvoir un poste de mécanicien, de carrossier-peintre ou de préparateur.
- **Unité vendue** : une **campagne de recrutement** pour un poste (forfait de 490 € HT) suivie, si elle aboutit, d'une **prime d'embauche** (990 € HT).
- **Périmètre** : France métropolitaine ; métiers « ouvriers mécaniciens de véhicules » et « carrossiers automobiles » de l'enquête BMO ; employeurs = entreprises de réparation automobile (NAF 45.20A, qui inclut la carrosserie).
- **Hors périmètre** : intérim, renfort freelance, poids lourds, autres métiers de l'artisanat (voir « marchés voisins »).

## 2. Données de base

| Donnée | Valeur | Source et date |
|--------|--------|----------------|
| Projets de recrutement, tous métiers, France | 2 274 951 (-6,5 %) | [Data] BMO 2026, France Travail, via La Finance pour tous (2026-04-24) |
| Projets « ouvriers mécaniciens de véhicules » | **19 495**, dont **72 %** difficiles (2025 : 21 557, 74 %) ; 5 % saisonniers | [Data] BMO 2026, open data France Travail, via https://travail-industrie.com/emploi/metiers-en-tension/ouvriers-mecaniciens-de-vehicules (consulté le 2026-10-12) |
| Projets « carrossiers automobiles » | **5 638**, dont **78 %** difficiles (2025 : 6 648, 80 %) ; 2 % saisonniers | [Data] même source : https://travail-industrie.com/emploi/metiers-en-tension/carrossiers-automobiles |
| Dont Île-de-France | mécaniciens 2 473 (67 % difficiles) ; carrossiers 1 046 (76 %) | [Data] mêmes pages, ventilation régionale |
| Entreprises de réparation automobile (NAF 45.20A) | 62 852 entreprises, 67 190 établissements (2023) | [Data] OBSA / ANFA, rapport des données sociales, édition 2025 (via [08-donnees-publiques.md](../../_recherche/signaux/08-donnees-publiques.md)) |
| Entreprises actives 45.20A par taille (France) | 6-9 salariés : 4 892 ; 10-19 : 2 250 ; 20-49 : 394 ; 1-2 et 3-5 : plus de 10 000 chacune (plafond de l'outil) | [Data] API Recherche d'entreprises (recherche-entreprises.api.gouv.fr), requête du 2026-10-12, tranches d'effectif INSEE 2024 |
| Entreprises actives 45.20A en Seine-et-Marne (77) | 1-2 salariés : 311 ; 3-5 : 269 ; 6-19 : 155 ; **total 1-19 : 735** (dont 3-19 : 424) | [Data] même API, 2026-10-12 |
| Entreprises actives 45.20A de 1 à 19 salariés, Île-de-France | 4 050 (75 : 288 ; 77 : 735 ; 78 : 563 ; 91 : 549 ; 92 : 336 ; 93 : 592 ; 94 : 406 ; 95 : 581) | [Data] même API, 2026-10-12 |
| Recrutements dans les services de l'automobile | 45 000 en 2022 (58 000 avec les alternants) ; 21 000 non aboutis (+43 % depuis 2019) ; 58 % des recrutements aboutis passent par une annonce, 42 % par le relationnel | [Data, ANCIENNE] ANFA Autofocus, via J2R Auto (2023-09-11) |
| Salaire moyen d'un mécanicien automobile | 2 401 € brut/mois, soit 28 812 €/an | [Data] INSEE 2023, via Journal du Net (consulté le 2026-10-12) |
| Honoraires d'un cabinet de recrutement | 15 à 30 % du salaire annuel brut | [Data, Tier 3] sources commerciales (optima-industrie.com, leonar.app, 2026) |

## 3. Estimation descendante (top-down)

1. 2 274 951 projets de recrutement en France en 2026 → **25 133 concernent les mécaniciens et les carrossiers** (1,1 %) [Data].
2. Dont **18 434 jugés difficiles** par l'employeur [CALCUL : 19 495 × 72 % + 5 638 × 78 %].
3. **Plafond théorique de dépense** si chaque recrutement difficile passait par un cabinet à 15 % du salaire moyen : 18 434 × 4 322 € = **79,7 M€ par an** [Estimate].
4. **Dépense réelle observée** : Mon Spécialiste Auto, un seul acteur de renfort freelance, réalise 10 M€ de CA auprès de plus de 1 000 garages [Data, J2R Auto, 2025-09-09] ; un réseau paie 5 850 €/mois de cabinet pour deux profils [Data, ANCIENNE]. Les garages dépensent donc déjà plusieurs dizaines de millions d'euros pour combler le manque de bras, mais surtout en renfort temporaire et en cabinets [Opinion].

## 4. Estimation ascendante (bottom-up)

1. Garages et carrosseries de **3 à 19 salariés** en France : 7 142 entreprises de 6 à 19 salariés [Data] + environ 12 400 de 3 à 5 salariés [CALCUL : même rapport 3-5 / 6-19 qu'en Seine-et-Marne, 269 / 155 = 1,74] = **environ 19 500 entreprises**.
2. Fréquence d'un recrutement difficile de mécanicien ou de carrossier : **une fois tous les deux ans** par entreprise [HYPOTHÈSE à valider en entretien].
3. **Environ 9 750 campagnes possibles par an** [CALCUL].

## 5. Réconciliation et tableau

- Descendant : 18 434 recrutements difficiles, dont **la moitié dans des indépendants de moins de 20 salariés** [HYPOTHÈSE], soit 9 217.
- Ascendant : environ 9 750.
- **Les deux approches convergent vers 9 200 à 9 800 campagnes par an.** On retient 9 217 (la plus prudente).

Valeur par campagne :
- **Prix plein** si l'embauche aboutit : 490 + 990 = **1 480 € HT** ;
- **Revenu moyen attendu** avec un taux d'embauche de 40 % [HYPOTHÈSE] : 490 + 0,4 × 990 = **886 € HT**.

| Indicateur | Volume (campagnes/an) | Valeur au prix plein | Valeur attendue (40 % d'embauches) | Projection 2-3 ans |
|------------|----------------------|----------------------|-------------------------------------|--------------------|
| **TAM** : tous les recrutements de mécaniciens et carrossiers en France | 25 133 | 37,2 M€ | 22,3 M€ | En baisse en volume (mécaniciens -9,6 %, carrossiers -15,2 % entre 2025 et 2026), stable en valeur si les salaires montent [Opinion] |
| **SAM** : recrutements difficiles dans les indépendants de 3 à 19 salariés | 9 217 | 13,6 M€ | 8,2 M€ | Idem ; + marchés voisins (autres métiers) |
| **SAM Île-de-France** | 1 226 [CALCUL : 3 519 × 69,7 % × 50 %] | 1,8 M€ | 1,1 M€ | |
| **SAM Seine-et-Marne (77)** | 222 [CALCUL : 3 519 × 18,1 % (part du 77 dans les petits garages franciliens) × 69,7 % × 50 %] | 0,33 M€ | 0,20 M€ | |
| **SOM 2027** (77, équipe à temps partiel puis 2 temps pleins) | 40 campagnes, 16 embauches | | **35 440 €** | 18 % du SAM du 77 |
| **SOM 2028** (Île-de-France) | 150 campagnes, 60 embauches | | **132 900 €** | 12 % du SAM francilien |
| **SOM 2029** (Île-de-France + une région ou un 2e métier) | 300 campagnes, 120 embauches | | **265 800 €** | 3,3 % du SAM national |

Lecture :
- **Le marché est petit mais réel.** Avec 8 à 14 M€ de SAM, c'est une entreprise de services rentable possible, pas une start-up à lever des fonds [Opinion].
- **Le SOM 2029 (environ 266 k€) fait vivre 6 personnes de façon modeste**, et seulement si le taux d'embauche atteint 40 % et si une campagne prend moins de 16 heures (voir [../05-financial/revenue-model.md](../05-financial/revenue-model.md)). Pour aller au-delà, il faut un 2e métier (bouchers, couvreurs, boulangers) ou une 2e région [Opinion].
- **Le marché se contracte en volume** : les projets de recrutement baissent de 10 à 15 % sur un an, même si la tension reste forte. C'est un signal à surveiller [Data].

## 6. Moteurs et freins

- **Moteurs** : départs en retraite, parc automobile vieillissant (11,8 ans en moyenne en 2026 selon Mobilians), technicité croissante (véhicules électriques et hybrides), annonces devenues le premier canal d'embauche (58 % des recrutements aboutis en 2022).
- **Freins** : baisse des projets de recrutement en 2026, alternatives gratuites, ciblage publicitaire bridé pour l'emploi, consolidation des garages en réseaux qui recrutent en interne (Speedy, First Stop).
- **Marchés voisins** (même format, mêmes prescripteurs) : bouchers (74 % de recrutements difficiles), couvreurs (82 %), boulangers, cuisiniers (57,6 %) [Data, signaux PT-13 et DP-06].

## 7. Hypothèses clés

| # | Hypothèse | Confiance | Comment la valider |
|---|------------|-----------|--------------------|
| 1 | La moitié des recrutements difficiles se fait dans des indépendants de moins de 20 salariés | Faible | Demander la répartition à l'ANFA ou à l'observatoire de la branche ; poser la question en entretien |
| 2 | Un garage de 3 à 19 salariés vit un recrutement difficile tous les deux ans | Faible | 10 entretiens : « Combien de personnes avez-vous embauchées ces 3 dernières années ? » |
| 3 | 40 % des campagnes aboutissent à une embauche | Très faible | 3 campagnes pilotes |
| 4 | La part du 77 dans les recrutements franciliens suit sa part dans les petits garages (18 %) | Moyenne | Tableau BMO 2026 par bassin d'emploi (open data) |
| 5 | Le prix de 490 € + 990 € est accepté | Faible | Préventes (voir [../07-terrain/experiences-validation.md](../07-terrain/experiences-validation.md)) |

---

## Flags

**Red Flags:**
- None identified.

**Yellow Flags:**
- Marché de niche (SAM national de 8 à 14 M€) : plafond bas sans extension à d'autres métiers.
- Volume de recrutements en baisse de 10 à 15 % entre 2025 et 2026.
- Les données BMO sont lues sur un site tiers qui reprend l'open data de France Travail : à recouper sur le fichier officiel (data.gouv.fr) avant toute présentation externe.

## Sources
- [Tier 1] Enquête BMO 2026, France Travail (open data), lue via travail-industrie.com, 2026-10-12.
- [Tier 1] API Recherche d'entreprises (DINUM / INSEE Sirene), requêtes du 2026-10-12.
- [Tier 1] OBSA / ANFA, rapport des données sociales, édition 2025.
- [Tier 2] J2R Auto (2023-09-11, 2024-06-10, 2025-09-09) ; Journal du Net (salaire INSEE 2023).
- [Tier 3] optima-industrie.com, leonar.app (honoraires des cabinets, 2026).
