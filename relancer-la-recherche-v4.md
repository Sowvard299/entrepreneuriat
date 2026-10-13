# Relancer la recherche d'idée, version 4 : par portes

La v3 cherchait sur le web une taille de marché que le web ne prouve presque jamais, et parlait aux clients à
la fin. La v4 inverse l'ordre : **une piste n'avance que si elle passe une porte**, et la preuve la plus forte
(un client qui s'engage) arrive en deuxième semaine, pas en quatrième session.
Pourquoi : `ideas/_recherche-v3/audit-systeme-v3.md`. D'où viennent les pièces : `ideas/_recherche-v3/veille-systeme.md`
et `.claude/skills/SOURCES.md`. Seuils : `CLAUDE.md`, section « Critères de viabilité ».

## Les portes

| Porte | Question | Preuve exigée | Outils (déjà dans le dépôt) | Durée, coût |
|-------|----------|---------------|------------------------------|-------------|
| 0. Accès | Peut-on parler à ces clients lundi ? | profil d'équipe rempli dans `CLAUDE.md` ; 20 clients nommés par piste | — | 1 h |
| 1. Argent visible | Le modèle encaisse-t-il déjà ? | ≥ 3 prix publics payés ; concurrents et leurs faiblesses citées ; croyance la plus fragile nommée | `chercheur`, `competitor-analysis`, `sentiment-analysis`, `before-you-build`, `verificateur` | 1 session, 1 agent par paire de pistes |
| 2. Engagement | Ces clients s'engagent-ils ? | 10 contacts en 1 semaine ; seuil d'engagement écrit avant (voir `CLAUDE.md`) | `interview-script`, `mom-test`, `summarize-interview` | 1 semaine, < 100 € |
| 3. Taille et choix | Peut-on en vivre à 3 ans ? | bottom-up avec les prix entendus ; SOM ≥ 500 k€ ou chemin d'expansion | `market-sizing`, `beachhead-segment`, `identify-assumptions-new`, `lean-canvas`, `llm-council` | 1 session |
| 4. Confirmation | Paient-ils vraiment ? | pilote payant ou précommandes, seuils écrits avant | `brainstorm-experiments-new`, puis `brainstorm-ideas-new` pour le MVP | 2 à 4 semaines, < 500 € |

Décision à chaque porte : **passe / à revoir / élimine**, écrite dans `ideas/_recherche-v4/portes.md` avec la preuve.

## Prompt à coller (reprend la v3)

```text
Lis CLAUDE.md (workflow v4 par portes, critères de viabilité) et relancer-la-recherche-v4.md.
Entrée : les 12 segments du Top 12 de ideas/_recherche-v3/segments.md et les signaux déjà collectés dans
ideas/_recherche-v3/signaux/ (P1 fini : facture électronique faible, panier 230-600 €/an).
Porte 0 : si le profil d'équipe de CLAUDE.md est vide, demande-le-moi d'abord (équipe, contacts nommés).
Porte 1 : en vagues de 4 « chercheur » au plus (une paire de segments chacun, 12 recherches web au plus,
fichiers dans ideas/_recherche-v4/porte1/ avec synthèse de 40 lignes), puis un « verificateur ». Pour chaque
segment : 3 prix publics payés, concurrents et faiblesses, croyance la plus fragile (skill before-you-build),
et 20 clients nommés joignables (où, comment). Élimine ce qui n'a pas 3 prix payés.
Puis arrête-toi : pour les 3 meilleurs segments, prépare le kit de la porte 2 (script interview-script + mom-test,
message d'approche, seuil d'engagement écrit, répartition des 10 contacts entre nous) et attends les comptes rendus.
Tiens ideas/_recherche-v4/etat.md à jour. Commite et pousse sur la branche claude/recherche-idee-v1 après chaque vague.
```

## Ce que l'équipe fait elle-même

- Remplir le profil de `CLAUDE.md` (porte 0) : c'est le levier le plus fort, aucun agent ne peut le faire.
- Passer les appels de la porte 2 et coller les comptes rendus dans `ideas/_recherche-v4/entretiens/`.
- Décider des seuils : ceux marqués [HYPOTHÈSE] dans `CLAUDE.md` se modifient une ligne à la fois, avec la raison.
