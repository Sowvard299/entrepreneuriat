# entrepreneuriat

Un espace de travail Claude Code pour trouver et valider une idée d'entreprise.

## Skills installés

Ils vivent dans `.claude/skills/`. Claude Code les charge automatiquement à l'ouverture du dépôt,
en local ou dans une session cloud.

| Étape | Skill | Usage | Exemple de prompt |
|-------|-------|-------|-------------------|
| Cartographier | `market-segment-scanner` | Marchés en croissance → segments précis → angles « pareil mais mieux » | « Cartographie les marchés français en croissance et découpe-les en segments » |
| Creuser | `jobs-to-be-done` | Trouver les « jobs » mal servis d'un segment | « Quels jobs sont mal servis chez les restaurateurs pour leurs achats ? » |
| Creuser | `ai-startup-opportunity-generator` | Méthode d'idées ancrées dans le travail réel, scorées, vérifiées contre 10 échecs types (orientée logiciel : on saute son étape de stack) | « Donne 10 idées pour un segment de départ » |
| Décider | `llm-council` | 5 conseillers + relecture anonyme + verdict | « Council : laquelle de ces 3 idées donne des clients en 3 mois, laquelle fait vivre l'équipe à 3 ans ? » |
| Valider | `startup-design` | Recherche → stratégie → validation, ou Fast Track go/no-go | « Fast track : <idée> » |
| Valider | `market-sizing` | TAM / SAM / SOM, bottom-up puis top-down | `/market-sizing <idée> en France` |
| Valider | `beachhead-segment` | Choisir le premier marché gagnable | `/beachhead-segment <idée>` |
| Valider | `identify-assumptions-new` | Hypothèses risquées sur 8 catégories | `/identify-assumptions-new <idée>` |
| Valider | `lean-canvas` | Modèle économique en une page | `/lean-canvas <idée>` |
| Clients | `mom-test` | Scripts d'entretien qui évitent les faux positifs | « Script Mom Test pour <segment> » |
| MVP | `brainstorm-ideas-new` | Fonctionnalités d'un produit **déjà choisi** (PM / designer / ingénieur). Ne sert pas à trouver une entreprise | `/brainstorm-ideas-new <idée retenue>` |

Le tableau ne liste que les skills du parcours principal. Le dossier contient aussi les skills d'entretien
et d'analyse d'avis (`interview-script`, `summarize-interview`, `sentiment-analysis`, `competitor-analysis`,
`brainstorm-experiments-new`, `before-you-build`).

### Ajoutés le 2026-10-15 (50 skills, à appeler par leur nom, ex. `/pre-mortem <plan>`)

| Usage | Skills |
|-------|--------|
| Concurrents | `startup-competitors` (fiches de combat, carte des prix), `competitor-mapper`, `competitive-battlecard` |
| Positionnement et message | `startup-positioning` (méthode April Dunford), `positioning-ideas`, `value-proposition`, `value-prop-statements`, `product-name` |
| Prix et modèle économique | `pricing-strategy`, `pricing-and-wtp`, `monetization-strategy`, `business-model`, `startup-canvas`, `cac-modeler` |
| Marché et clients | `market-segments`, `ideal-customer-profile`, `user-personas`, `user-segmentation`, `customer-journey-map`, `tam-sam-som-builder`, `trend-analysis`, `trend-to-product-mapper` |
| Stratégie | `product-strategy`, `product-vision`, `swot-analysis`, `porters-five-forces`, `pestle-analysis`, `ansoff-matrix`, `north-star-metric` |
| Mise sur le marché | `gtm-strategy`, `gtm-motions`, `growth-loops`, `marketing-ideas`, `distribution-analysis` |
| Risques et décision | `pre-mortem`, `strategy-red-team`, `prioritize-assumptions`, `opportunity-solution-tree`, `idea-scoring`, `weakness-detection`, `pivot-engine`, `decision-memo`, `desire-evaluator`, `retention-predictor` |
| Profil fondateur | `user-background-interviewer`, `user-segmentation-profiler` |
| Lancement | `create-prd` (MVP), `startup-pitch` (investisseurs), `draft-nda`, `privacy-policy` (brouillons à faire relire par un juriste) |

Les skills de MaxKmet (`idea-scoring`, `pricing-and-wtp`, `cac-modeler`, `trend-analysis`...) visent les applis
mobiles B2C américaines et écrivent dans `memory/`. Leurs barèmes ne remplacent pas la grille de `CLAUDE.md`.

`market-segment-scanner` est fait maison : pas de source externe, pas de licence à suivre.
Les seuils et la grille de score sont dans `CLAUDE.md`, section « Critères de viabilité ».

## Sous-agents

Ils vivent dans `.claude/agents/`. La session principale les appelle pour la collecte et ne lit que
leurs fichiers de synthèse (règles dans `CLAUDE.md`, section « Sous-agents et coordination »).

| Agent | Modèle | Rôle |
|-------|--------|------|
| `chercheur` | sonnet | Collecte de preuves sourcées : règles de preuve, quota de diversité des sites, sources bloquées connues, API qui marchent |
| `auditeur` | sonnet | Concurrents réels, échecs passés, droit avec articles, économie unitaire, score recalculé |
| `verificateur` | haiku | Rouvre un échantillon d'URL et vérifie citations et chiffres |

## Outils externes (optionnels)

Voir l'étape 0.3 de `relancer-la-recherche-v3.md`. Lire le `SKILL.md` ou le README de chacun avant
installation. L'API `recherche-entreprises.api.gouv.fr` est sans clé et appelée directement.

## Recherches d'idées

- Première itération (octobre 2026) : recherche dans `ideas/_archives/_recherche/`, idée retenue dans `ideas/_archives/recrutement-garages/`.
- Deuxième itération (v2, octobre 2026) : `ideas/_archives/_recherche-v2/`, arrêtée en phase 4, idées jugées non
  viables. Leçons dans `ideas/_archives/_recherche-v2/BILAN.md`.
- Version 3 (marché → segment → angle) : suivre `relancer-la-recherche-v3.md` (guide pas à pas et prompt à
  coller, en français). Elle écrit dans `ideas/_archives/_recherche-v3/`.
- **Seul guide actif : `relancer-la-recherche-v4.md`.** Les autres guides et audits sont de l'historique.
- **Version 4, en cours (portes : accès → argent visible → engagement client → taille → pilote)** : suivre
  `relancer-la-recherche-v4.md`. Elle reprend les segments de la v3 et écrit dans `ideas/_recherche-v4/`.
  Pourquoi ce changement : `methode/audit-systeme-v3.md`.
- Remise à zéro des idées (2026-10-14) : méthode v4 gardée, recherches précédentes rangées dans
  `ideas/_archives/`, méthode dans `methode/`. État et prompt de reprise : `ideas/_recherche-v4/etat.md`.
- Ancienne méthode : `relancer-la-recherche.md` (v2), à garder pour comparer.

Les sources, commits et licences des skills tiers sont dans `.claude/skills/SOURCES.md`.
