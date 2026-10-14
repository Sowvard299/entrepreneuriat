# Hypothèses de travail (recherche v2, octobre 2026)

Recherche repartie de zéro : les dossiers `ideas/_recherche/` et `ideas/recrutement-garages/`
(première itération) n'ont pas été lus. Si une idée de la première itération réapparaît
d'elle-même à partir des nouvelles preuves, elle est signalée comme telle.

## Réponses de l'équipe (14 octobre 2026)

| Sujet | Réponse | Comment on l'applique |
|-------|---------|-----------------------|
| Marché de départ | Pas de préférence entre en ligne et local ; si local, Île-de-France | Les idées locales sont testées sur l'Île-de-France ; les idées en ligne sur la France francophone |
| Angle | Reprendre un modèle qui se vend déjà et le faire mieux | La preuve que des clients paient passe avant l'originalité |
| Équipe | Compétences non contraignantes : on recrute | Critère « avantage de l'équipe » supprimé de la grille (deuxième version du classement) |
| Budget | « On s'en fiche » (pas de plafond fixé) | Pas de filtre éliminatoire sur le budget ; le capital nécessaire avant le premier euro reste un critère de score, car l'ambition est l'autofinancement |
| Ambition | Rentable vite, autofinancé | Vitesse jusqu'au premier client payant fortement pondérée |

## Hypothèses par défaut (non confirmées par l'équipe)

- Équipe (consigne de l'équipe, 14/10/2026) : 6 associés ; **les compétences de l'équipe ne sont pas une contrainte**, toute compétence nécessaire sera recrutée. Aucune idée n'est notée ni filtrée sur l'adéquation avec l'équipe.
- [HYPOTHÈSE] Réseau : réseau d'école, entourage, et l'alternance chez EDF (TPE / PME, énergie). Aucun réseau sectoriel confirmé.
- [HYPOTHÈSE] Exclusions : aucune exclusion de secteur fournie. Une activité réglementée n'est écartée que si l'autorisation ne peut pas être obtenue en recrutant une personne qualifiée (ex. expertise comptable, dont le capital doit être détenu par des professionnels).
- [HYPOTHÈSE] Le budget « libre » ne signifie pas des fonds illimités : on suppose quelques milliers d'euros mobilisables, et on pénalise les idées qui demandent plus de 20 000 € avant le premier euro.

## Limites techniques de cette session

- Recherche faite dans une session cloud sans sous-agents (non demandés), donc séquentielle.
- `recherche-entreprises.api.gouv.fr` coupe la connexion en ligne de commande depuis cette session, mais répond via l'outil de lecture web : les comptages d'entreprises des dossiers d'idée viennent de cette API (14/10/2026).
- Trustpilot renvoie une erreur 403 aux lectures automatiques : les avis Trustpilot sont cités via les extraits des moteurs de recherche ou d'autres sites d'avis quand c'est possible, et signalés comme tels.
