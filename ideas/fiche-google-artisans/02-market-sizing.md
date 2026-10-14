# Taille du marché (méthode market-sizing)

Prix de référence : 79 € HT/mois, soit **948 € HT/an** par client (hors frais de mise en route).
Comptages d'entreprises : API Recherche d'entreprises (données Sirene), interrogée le 14/10/2026, unités légales actives ayant au moins un établissement dans la zone (le filtre porte sur les établissements : une entreprise présente dans deux départements compte dans les deux, et la somme régionale est donc un plafond). Limite : la tranche d'effectif de Sirene peut dater de plusieurs années.

Codes d'activité retenus (« second œuvre ») : 43.21A électricité, 43.22A plomberie-chauffage, 43.29A isolation, 43.31Z plâtrerie, 43.32A menuiserie bois et PVC, 43.32B menuiserie métallique et serrurerie, 43.33Z revêtements de sols et murs, 43.34Z peinture et vitrerie, 43.91B couverture, 43.99C maçonnerie générale.

## 1. Bottom-up (nombre de clients × prix)

### Île-de-France (marché de départ)
| Département | Entreprises de second œuvre de 1 à 19 salariés |
|-------------|-----------------------------------------------|
| 75 Paris | 5 584 |
| 77 Seine-et-Marne | 4 147 |
| 78 Yvelines | 2 897 |
| 91 Essonne | 3 598 |
| 92 Hauts-de-Seine | 2 744 |
| 93 Seine-Saint-Denis | 6 976 |
| 94 Val-de-Marne | 3 887 |
| 95 Val-d'Oise | 4 208 |
| **Total** | **34 041** |

- **SAM Île-de-France** = 34 041 × 948 € = **32,3 M€ HT/an**.
- Sans salarié (micro-entrepreneurs) exclus : ils paient moins souvent [HYPOTHÈSE].

### France
- 557 306 entreprises artisanales du bâtiment de moins de 20 salariés, dont **182 329 employeuses** (CAPEB, chiffres 2021, [rapport CAPEB 79](https://www.capeb.fr/www/capeb/media//deuxsevres/document/Rapport%20moral%20et%20activites%202020.pdf)).
- **TAM France** (employeuses) = 182 329 × 948 € = **172,8 M€ HT/an**. Avec les non-employeuses : 528 M€, mais elles paieraient rarement.

### Segment de départ (Essonne)
- Plombiers-chauffagistes et électriciens de 1 à 9 salariés en Essonne : **984 entreprises** (API, 14/10/2026).
- Marché du segment = 984 × 948 € = **0,93 M€ HT/an**.

## 2. Top-down (recoupement)
- Solocal : 324,5 M€ de chiffre d'affaires 2025 pour 195 000 clients, toutes TPE confondues, soit ~1 660 € par client et par an ([résultats 2025](https://webdisclosure.com/press-release/solocal-group-epa-solocal-2025-annual-results-2hNhz7AVBdW), [Bourse Direct](https://www.boursedirect.fr/fr/actualites/categorie/divers/solocal-taux-de-marge-d-ebitda-a-18-5-en-2025-boursier-62282987696f84e2c1ca17af31d14369665b5db6)).
- Si 30 % de ces clients sont des entreprises du bâtiment [HYPOTHÈSE], cela fait ~58 500 artisans qui paient déjà ~1 660 €/an, soit environ un tiers des 182 329 artisans employeurs. **Notre prix (948 €/an) est inférieur à ce qu'ils paient déjà en moyenne.**
- Flux de départs : churn de 21 % → ~41 000 clients quittent Solocal chaque année en France. Avec 18 % des entreprises en Île-de-France et 30 % dans le bâtiment [HYPOTHÈSES], cela fait **~2 200 artisans franciliens qui quittent Solocal par an** : c'est le vivier de l'offre « Sortir de PagesJaunes ».
- Les deux approches donnent des ordres de grandeur cohérents (dizaines de M€ en IDF, une à quelques centaines de M€ en France).

## 3. SOM (ce qu'on peut réellement prendre en 3 ans)
Contrainte réelle : la capacité de l'équipe, pas la demande.

| Horizon | Clients actifs | Revenu récurrent annuel | Part du SAM IDF |
|---------|----------------|-------------------------|-----------------|
| Fin an 1 (été 2027, temps partiel) | 40 | 38 k€ | 0,1 % |
| Fin an 2 (temps plein possible) | 150 | 142 k€ | 0,4 % |
| Fin an 3 | 300 | 284 k€ | 0,9 % |

- 300 clients en 3 ans = capter ~5 % des artisans franciliens qui quittent Solocal chaque année [HYPOTHÈSE], ce qui reste prudent.
- **Lecture franche** : à 300 clients, le revenu (284 k€/an) paie 4 à 5 salaires modestes, pas 6. Le marché n'est pas la limite ; la limite est le temps passé par client (voir [06-economie-unitaire.md](06-economie-unitaire.md)).
