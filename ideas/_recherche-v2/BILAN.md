# Bilan de la recherche v2 (13 octobre 2026) : arrêtée en phase 4

La v2 suivait `relancer-la-recherche.md` (option A, de zéro). Elle a été **arrêtée volontairement en
phase 4** : l'équipe a jugé les idées produites non viables. Le système a été refait (v3, voir
`relancer-la-recherche-v3.md`, `.claude/agents/`, `.claude/skills/market-segment-scanner/`).

## Ce qui a été produit

| Fichier | Contenu | Réutilisable ? |
|---------|---------|----------------|
| [signaux.md](signaux.md) et [signaux/](signaux/) | 163 signaux, 135 domaines distincts, 6 familles | Oui, comme base de données publiques : comptages Sirene par NAF en 75/92/93/94, CA vérifiés de nombreux acteurs (API `finances`), obligations datées et vérifiées (facturation électronique, DPE, loi Le Meur, biodéchets, audit énergétique, REP emballages), cimetière des échecs (BODACC) |
| [problemes.md](problemes.md) | 20 modèles existants classés, avec le job du client | Partiellement : classement biaisé vers les petites niches de services |
| [idees-classees.md](idees-classees.md) | 22 idées, 5 éliminées, top 8 | Non, sauf comme liste d'idées à éviter |
| [phase4/](phase4/) | 4 audits **incomplets** (coupés par la limite de session) | Les tableaux de concurrents déjà écrits sont exacts mais partiels |

## Pourquoi les idées ne sont pas viables

1. **Départ par les plaintes** (avis 1-2 étoiles) : on retrouve des marchés de services locaux
   (ménage, dépannage, garde d'enfants, déménagement, marketing pour artisans) où tout le monde peut
   entrer. Le top 8 était fait « d'agences locales de plus ».
2. **Grille de score** : la taille du marché ne pesait que 5 %, la rapidité et la facilité de test 25 %.
   Les micro-niches rapides à tester gagnaient.
3. **Métiers d'employeur à marge fine** : ménage, garde, dépannage, nettoyage reposent sur le recrutement
   d'intervenants (marges de 3 à 16 %), sans avantage pour une équipe marketing.
4. **Aucun avantage défendable** : rien n'empêchait un acteur en place de copier l'angle (« sans
   engagement », « remplaçant garanti »).
5. **Profil fondateur vague** (réseau « tout le monde », équipe non décrite) : impossible d'orienter
   vers un segment où l'équipe a un accès privilégié.

## Problèmes de fonctionnement du système

| Problème | Cause | Correction (v3) |
|----------|-------|-----------------|
| Limite de session atteinte, 4 auditeurs coupés en même temps | agents génériques sur le modèle le plus cher (environ 150 000 à 200 000 tokens chacun en phase 1) | agents dédiés en `sonnet` / `haiku`, vagues de 4 |
| Contexte du coordinateur saturé | il a relu les 6 fichiers de signaux en entier | fichier de synthèse de 40 lignes par agent, seul lu par le coordinateur |
| Famille 1 : 25 signaux sur 28 venant de Trustpilot, 5 recherches sur 25 utilisées | aucun quota de diversité | un site ≤ 40 % des preuves, une source officielle par marché |
| Reddit illisible (WebFetch et navigateur intégré refusés), Pappers, Malt, DGCCRF, Cessionpme bloqués | consigne « utilise le navigateur » inopérante | liste des sources bloquées et des API qui marchent dans `.claude/agents/chercheur.md` |
| Plusieurs règles juridiques laissées en [HYPOTHÈSE] jusqu'au classement | pas d'étape juridique sourcée | l'auditeur cite l'article pour chaque finaliste |
| Aucune vérification des citations | pas d'étape de contrôle | agent `verificateur` après chaque vague |
| Aucun point d'arrêt | autonomie totale demandée | 2 points d'arrêt en v3 |
