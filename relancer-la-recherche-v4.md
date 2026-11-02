# Relancer la recherche d'idée, version 4 : par portes

La v3 cherchait sur le web une taille de marché que le web ne prouve presque jamais, et parlait aux clients à
la fin. La v4 inverse l'ordre : **une piste n'avance que si elle passe une porte**, et la preuve la plus forte
(un client qui s'engage) arrive en deuxième semaine, pas en quatrième session.
Pourquoi : `methode/audit-systeme-v3.md`. D'où viennent les pièces : `methode/veille-systeme.md`
et `.claude/skills/SOURCES.md`. Seuils : `CLAUDE.md`, section « Critères de viabilité ».

## Les portes

| Porte | Question | Preuve exigée | Outils (déjà dans le dépôt) | Durée, coût |
|-------|----------|---------------|------------------------------|-------------|
| 1. Argent visible | Le modèle encaisse-t-il déjà ? | ≥ 3 prix publics payés ; concurrents et leurs faiblesses citées ; croyance la plus fragile nommée | `chercheur`, `competitor-analysis`, `sentiment-analysis`, `before-you-build`, `verificateur` | 1 session, 1 agent par paire de pistes |
| 2. Engagement | Ces clients s'engagent-ils ? | 10 contacts en 1 semaine ; seuil d'engagement écrit avant (voir `CLAUDE.md`) | `interview-script`, `mom-test`, `summarize-interview` | 1 semaine, < 100 € |
| 3. Taille et choix | Peut-on en vivre à 3 ans ? | bottom-up avec les prix entendus ; SOM ≥ 500 k€ ou chemin d'expansion | `market-sizing`, `beachhead-segment`, `identify-assumptions-new`, `lean-canvas`, `llm-council` | 1 session |
| 4. Confirmation | Paient-ils vraiment ? | pilote payant ou précommandes, seuils écrits avant | `brainstorm-experiments-new`, puis `brainstorm-ideas-new` pour le MVP | 2 à 4 semaines, < 500 € |

Décision à chaque porte : **passe / à revoir / élimine**, écrite dans `ideas/_recherche-v4/portes.md` avec la preuve.

## Prompt à coller (remise à zéro du 2026-10-14)

Le prompt à jour est dans `ideas/_recherche-v4/etat.md`, section « Reprise ».
Aucune idée, aucun segment ni signal des recherches précédentes (`ideas/_archives/`) n'est une entrée.

## Ce qui reste humain

- Passer les appels de la porte 2 et coller les comptes rendus dans `ideas/_recherche-v4/entretiens/`.
- Décider des seuils : ceux marqués [HYPOTHÈSE] dans `CLAUDE.md` se modifient une ligne à la fois, avec la raison.
