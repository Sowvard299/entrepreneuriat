# Segment de départ (beachhead)

**Phase:** 4, Strategy (skill `beachhead-segment`)
**Project:** recrutement-garages
**Date:** 2026-10-12
**Confidence:** Medium (comptages sourcés ; douleur et disposition à payer de ce segment précis à confirmer en entretien)

---

## Segments comparés

Notes de 1 à 5 sur les quatre critères du skill (douleur brûlante, disposition à payer, part de marché gagnable en 3 à 18 mois, potentiel de recommandation).

| Segment | Douleur | Payer | Gagnable | Recommandation | Total /20 | Commentaire |
|---------|---------|-------|----------|----------------|-----------|-------------|
| **A. Carrosseries indépendantes de 3 à 19 salariés en Seine-et-Marne** | 5 | 4 | 4 | 4 | **17** | Métier le plus tendu (78 % de recrutements difficiles en France, 76 % en Île-de-France) ; chaque poste vide = véhicules immobilisés et chiffre d'affaires perdu ; peu d'entreprises, donc une part élevée est atteignable |
| B. Garages mécaniques indépendants de 3 à 19 salariés en Seine-et-Marne | 4 | 3 | 3 | 3 | 13 | Tension un peu plus faible en Île-de-France (67 %) ; plus nombreux ; segment voisin naturel de A |
| C. Petits réseaux de 2 à 10 ateliers en Île-de-France | 4 | 5 | 2 | 3 | 14 | Ils paient déjà des cabinets (5 850 €/mois cité) mais décident plus lentement et internalisent (TikTok, cooptation) |
| D. Garages de 1 à 2 salariés en Seine-et-Marne | 3 | 2 | 3 | 3 | 11 | Embaucher le premier salarié est un saut ; budget faible |
| E. Boulangeries indépendantes en Seine-et-Marne | 4 | 2 | 3 | 3 | 12 | Dépense actuelle quasi nulle et fragilité financière documentées par l'audit |

## Segment retenu

**Les carrosseries indépendantes de 3 à 19 salariés de Seine-et-Marne qui cherchent un carrossier-peintre ou un préparateur depuis plus de 30 jours.**

- **Qui** : le patron (souvent ancien carrossier, 40 à 60 ans [HYPOTHÈSE]), qui décide seul ; il travaille lui-même à l'atelier.
- **Où** : Seine-et-Marne (77), en commençant par la moitié ouest, la plus dense (secteurs de Marne-la-Vallée, Meaux, Melun, Chelles) [HYPOTHÈSE : choix du département lié à la localisation de l'équipe, voir H11 dans [../../_recherche/hypotheses.md](../../_recherche/hypotheses.md)].
- **Combien** :
  - 735 entreprises de réparation automobile de 1 à 19 salariés dans le 77, dont 424 de 3 à 19 salariés [Data, API Recherche d'entreprises, 2026-10-12] ;
  - dont au moins **40 entreprises de 3 à 19 salariés avec « carrosserie » dans leur nom** [Data, même API, recherche par nom : sous-estimation, car beaucoup de garages font aussi de la carrosserie]. Fourchette retenue : **40 à 100 carrosseries** [Estimate].
  - Recrutements de carrossiers en Île-de-France : 1 046 projets en 2026, dont 76 % difficiles [Data, BMO 2026] ; part du 77 estimée à 18 %, soit **environ 190 projets par an** [CALCUL].
- **Pourquoi elles d'abord** :
  1. la douleur se chiffre (un poste vide = des véhicules qui attendent) ;
  2. le métier est précis (carrossier-peintre, préparateur), ce qui rend la vidéo et la grille de présélection plus simples ;
  3. le poste de **préparateur** s'ouvre aux reconversions, ce qui permet d'attirer de nouveaux candidats au lieu de vider la carrosserie voisine ;
  4. le segment est assez petit pour qu'une équipe de 6 en touche la plupart en 3 mois.

## Comment les trouver (liste concrète)

1. **Fichier des entreprises** : API Recherche d'entreprises (recherche-entreprises.api.gouv.fr), filtres : activité 45.20A, département 77, tranches d'effectif 3 à 19, mot-clé « carrosserie ». Gratuit, téléchargeable.
2. **Offres ouvertes** : recherche « carrossier », « peintre automobile », « préparateur carrosserie » sur France Travail, Indeed et Leboncoin, département 77. Une offre en ligne depuis plus de 30 jours = carrosserie prioritaire.
3. **Google Maps** : « carrosserie » commune par commune, pour les numéros et les avis (une carrosserie bien notée a de quoi vendre aux candidats).
4. **Prescripteurs** : chambre de métiers et de l'artisanat d'Île-de-France (délégation de Seine-et-Marne), Mobilians (syndicat des services de l'automobile), Fédération nationale de l'automobile (FNA), CFA et lycées professionnels de l'automobile du 77 (pour les candidats en fin de formation).
5. **Fournisseurs** : distributeurs de peinture automobile et de pièces qui visitent les carrosseries chaque semaine (à identifier lors des premiers entretiens).

## Prix et disposition à payer

- Prix de test : 490 € HT de campagne + 990 € HT à l'embauche (voir [../05-financial/revenue-model.md](../05-financial/revenue-model.md)).
- Repère pour le patron : un cabinet facture 15 à 30 % du salaire annuel, soit 4 300 à 8 600 € pour un salarié à 28 800 € brut par an [Estimate] ; le renfort freelance (Mon Spécialiste Auto) se paie à la journée.
- À tester en entretien : combien coûte au patron une semaine sans carrossier (chiffre d'affaires perdu) ? C'est l'argument de prix.

## Recommandation et extension

- **Recommandation** : un garage satisfait parle à ses fournisseurs, à son expert d'assurance et aux carrossiers voisins. Une vidéo réussie se montre (c'est la preuve la plus forte pour vendre la suivante).
- **Extension après le segment de départ** :
  1. garages mécaniques du 77 (même canal, même département) ;
  2. carrosseries et garages des autres départements de la grande couronne (78, 91, 95 : 1 693 entreprises de 1 à 19 salariés) [Data] ;
  3. autres métiers en tension avec les mêmes prescripteurs (bouchers, couvreurs, boulangers).
- **Règle** : un seul client par métier et par bassin à la fois, pour ne pas organiser le débauchage entre voisins.

## Plan d'acquisition sur 90 jours (segment de départ)

| Semaines | Objectif | Actions |
|----------|----------|---------|
| 1 à 2 | 10 entretiens de découverte | Liste de 60 carrosseries ; visites et appels (7 h 30-9 h, 12 h-14 h) ; guide d'entretien [../07-terrain/guide-entretien.md](../07-terrain/guide-entretien.md) |
| 3 à 6 | 3 pilotes payants | Proposition en fin de visite ; tournage, campagne, présélection ; mesure du coût par candidat et des heures passées |
| 7 à 12 | 10 campagnes signées dans le 77 | Études de cas des pilotes ; présentation à la chambre de métiers et aux fournisseurs ; extension aux garages mécaniques |

---

## Flags

**Red Flags:**
- None identified.

**Yellow Flags:**
- Le nombre exact de carrosseries de 3 à 19 salariés dans le 77 est inconnu (40 au minimum par le nom).
- Le choix du département dépend de la localisation réelle de l'équipe (hypothèse H11).

## Sources
- [Tier 1] API Recherche d'entreprises, 2026-10-12 ; BMO 2026 (France Travail, open data, via travail-industrie.com).
- [Tier 2] J2R Auto (2024-06-10, 2025-09-09, 2026-07-01).
- Audit : [../../_recherche/phase4/B-audit-recrutement-artisans.md](../../_recherche/phase4/B-audit-recrutement-artisans.md).
