# Validation rapide (startup-design, Fast Track)

Intake sauté : le contexte vient du prompt de recherche, de `CLAUDE.md` et de [../_recherche-v2/hypotheses.md](../_recherche-v2/hypotheses.md). Phases Marque et Produit sautées.

## Phase 0.5 : pré-vol

| Vérification | Résultat | Conséquence |
|--------------|----------|-------------|
| Solution dominante ? | **Oui** : Solocal / PagesJaunes, 195 000 clients fin 2025, churn 21 %/an ([résultats 2025](https://webdisclosure.com/press-release/solocal-group-epa-solocal-2025-annual-results-2hNhz7AVBdW)) ; Simplébo, plus de 6 000 clients annoncés, partenaire CAPEB ; Malou sur les restaurants | On ne crée pas un marché, on en prend une part à un leader qui recule. Éviter les restaurants (Malou) |
| Échec public d'un prédécesseur ? | Aucun trouvé sur ce créneau précis | Pas de mine connue, mais l'absence de preuve n'est pas une preuve |
| Interdiction juridique ? | Non. Points de vigilance : rétractation de 14 jours pour les entreprises de 5 salariés ou moins démarchées hors établissement ; interdiction des faux avis | Contrat et charte d'avis à rédiger avant le premier client |

## Phase 2 : trois variations

| Variation | Pour | Contre | Retenue ? |
|-----------|------|--------|-----------|
| I1. Artisans du bâtiment, abonnement sans engagement | Marché large (34 000 entreprises de second œuvre de 1 à 19 salariés en IDF), leader en recul, aucun concurrent financé dédié | Artisans difficiles à joindre et méfiants | **Oui, cœur de l'offre** |
| I2. Restaurants et commerces de bouche | Avis encore plus décisifs | Malou : 10 M€ levés, plus de 2 000 restaurants | Non (concurrent financé) |
| I3. « Sortir de PagesJaunes » au succès | Transforme la plainte principale en offre | Revenu ponctuel, dépend des dates de reconduction | **Oui, comme accroche commerciale d'I1** |

## Phase 3 : recherche (vagues 1 et 2)
- **Marché** : voir [02-market-sizing.md](02-market-sizing.md). Les TPE paient déjà : 324,5 M€ de chiffre d'affaires pour Solocal en 2025, soit environ 1 660 € par client et par an [calcul : 324,5 M€ ÷ 195 000].
- **Concurrents** : voir l'audit [A](../_recherche-v2/phase4/A-audit-visibilite-tpe.md).
- **Timing** : activité des artisans du bâtiment −1,5 % sur un an au T2 2026, carnets des plus petites entreprises en légère baisse ([CAPEB T2 2026](https://www.capeb.fr/www/capeb/media/national/note-conjoncture-capeb-t2-2026.pdf)) : les artisans cherchent des clients.

## Phase 3.5 : porte de recherche
**GO conditionnel.** L'argent dépensé et le recul du leader sont prouvés. Ce qui n'est pas prouvé : que des artisans paieront **nous**, et qu'ils verront assez d'appels en plus pour rester. Ces deux points ne se règlent que sur le terrain.

## Phase 3.7 : découverte client
**À faire sur le terrain.** Aucun entretien n'a eu lieu. Minimum Fast Track : 3 entretiens avant d'aller plus loin ; le kit prévoit 30 ([terrain/](terrain/)).

## Phase 7 : modèle de revenus (hypothèses, étape A)
| Élément | Hypothèse |
|---------|-----------|
| Abonnement | 79 € HT/mois, sans engagement |
| Mise en route | 149 € HT, une fois |
| Option « avis seuls » | 39 € HT/mois |
| Offre « Sortir de PagesJaunes » | gratuite si l'artisan prend l'abonnement ; sinon 50 % de l'économie de la première année |
| Objectif an 1 | 40 clients actifs, environ 3 200 € de revenu mensuel récurrent |
Détail et seuils : [06-economie-unitaire.md](06-economie-unitaire.md).

## Phase 8 : tableau de bord

| Dimension | Note /10 | Justification |
|-----------|----------|---------------|
| Gravité du problème | 6 | Besoin réel (81 % des clients lisent les avis avant de choisir), mais pas une urgence vitale pour un artisan au carnet plein |
| Taille du marché | 7 | 32 M€/an en Île-de-France au prix visé ; plus de 170 M€/an en France (voir 02) |
| Avantage concurrentiel | **4** | Aucun avantage durable aujourd'hui : le service est copiable, Google automatise une partie des tâches |
| Faisabilité | 9 | Aucun code, aucune licence, outils gratuits ou peu chers |
| Clarté du modèle économique | 7 | Abonnement simple ; churn inconnu |
| Adéquation équipe-marché | 6 | Compétences marketing en plein dans le livrable ; aucune connaissance du bâtiment ; une connaissance des TPE via l'alternance |
| Timing | 7 | Leader en recul, artisans qui cherchent des clients, mais IA de Google qui progresse |
| **Global** | **6,6** | |

**Verdict** : idée **prometteuse à tester pour pas cher, pas encore une entreprise.** Elle est faisable dès la semaine prochaine sans argent, et le marché paie déjà. Sa faiblesse est l'avantage concurrentiel : n'importe qui peut vendre la même chose. Elle ne vaut que si, en 60 jours, les artisans pilotes voient plus d'appels et restent. Lancer les 3 expériences de [terrain/experiences-validation.md](terrain/experiences-validation.md) et décider le 16 novembre 2026.
