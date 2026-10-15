# Proposition de changements de seuils pour CLAUDE.md (non appliquée)

Date : 2026-10-14. Rien dans ce fichier n'est appliqué à `CLAUDE.md`. L'équipe décide ligne par ligne.
Sources : `methode/audit-systeme-v3.md` (section « Seuils à revoir ») et
`methode/veille-systeme.md` (section « Réglages de CLAUDE.md suggérés »).

## A. Déjà appliqués le 2026-10-13 (alors que l'audit disait « proposition, non appliquée »)

La session du 13 octobre a modifié ces lignes de `CLAUDE.md` en même temps qu'elle écrivait le workflow v4
(commit `2a5d668`). À confirmer ou à annuler :

| Ligne | Avant | Maintenant | Avis |
|-------|-------|------------|------|
| Taille (SAM ≥ 50 M€) | éliminatoire | éliminatoire à la porte 3 seulement | garder : la taille se calcule mieux avec des prix entendus |
| Croissance | ≥ 8 % ou moteur daté, éliminatoire | souhaité ; moteur compté seulement si la dépense continue après l'échéance ; éliminatoire pour la piste ambitieuse | garder : 0 marché sur 38 la prouvait |
| Argent déjà dépensé | prix et clients payants, ≥ 3 sources | ≥ 3 prix publics réellement payés, éliminatoire dès la porte 1 | garder, mais préciser « payé » (voir B2) |
| Accès | 10 clients joignables en une semaine | 20 clients nommés joignables, éliminatoire dès la porte 0 | garder |
| Engagement client | (absent) | 10 contacts, ≥ 3 engagements d'argent ou ≥ 5 de temps, porte 2 [HYPOTHÈSE] | garder tel quel jusqu'aux 10 premiers appels |

La grille de score a aussi été repondérée (engagement client 25 %). Avis : garder.

## B. Pas encore appliqués

| # | Ligne | Proposition | Pourquoi | Source |
|---|-------|-------------|----------|--------|
| B1 | nouvelle : « Part de la cible à signer » | clients nécessaires pour 500 k€ de CA ÷ clients identifiables du segment ; au-delà de 5 % à signer en 3 ans, la note de taille baisse. Souhaité, calculé dès la porte 1 | remplace la note « Valeur » qui saturait (> 3 M€ = 10 pour presque tout) dans `ideas/_archives/_recherche-v3/segments.md` | audit, 4e puce |
| B2 | Argent déjà dépensé | un prix compte comme « payé » s'il est public ET qu'on voit des clients qui le paient : CA déposé du vendeur (API recherche-entreprises), avis clients nombreux, clients cités, annonce de cession avec CA, revenus vérifiés (TrustMRR) | sans cette définition, une grille tarifaire sans client passe la porte 1 ; le cas Tolteck (P1-15 : 228 €/an, CA 6,79 M€) montre la bonne preuve | veille, réglage 3 |
| B3 | Premier client payant ≤ 3 mois | ajouter « mesuré par la porte 2 (engagement), confirmé par la porte 4 (pilote payant) » | aujourd'hui la ligne ne dit pas quand on la mesure | veille, réglage 2 |
| B4 | Croissance / Piste ambitieuse | une seule valeur : la ligne Croissance renvoie à la ligne « Piste ambitieuse » (≥ 10 %) au lieu de ≥ 8 % | les deux lignes se contredisent aujourd'hui (8 % et 10 % pour la même piste) | relecture du 2026-10-14 |
| B5 | Concentration, Clients identifiables | écrire la porte : clients identifiables à la porte 1 (comptage Sirene, gratuit), concentration à la porte 3 | les deux sont éliminatoires mais sans porte : on ne sait pas quand éliminer | relecture du 2026-10-14 |

## C. Ce que je ne propose pas de changer

- Le seuil d'engagement de la porte 2 (≥ 3 argent ou ≥ 5 temps sur 10) : il n'a jamais été testé. Le changer avant
  les 10 premiers appels serait une boucle de plus (règle anti-boucle de `CLAUDE.md`).
- Le seuil de 500 k€ de SOM : il dépend de l'ambition chiffrée du profil (☐ encore vide), pas d'une méthode.
