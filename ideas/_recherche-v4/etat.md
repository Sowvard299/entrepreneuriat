# État de la recherche v4 (par portes)

Créé le 2026-10-13. **Remis à zéro le 2026-10-14** : la méthode v4 reste, mais aucune idée, aucun segment ni
signal des recherches précédentes n'est une entrée. Elles sont rangées dans `ideas/_archives/`, la méthode
(audit, veille) dans `methode/`. Guide : `relancer-la-recherche-v4.md`.

| Porte | Statut | Date |
|-------|--------|------|
| 0. Accès (profil, 2-3 porteurs datés, 30 conversations réseau, 20 clients nommés par piste) | kit prêt : `kit-porte0.md` ; ☐ profil de CLAUDE.md et 30 conversations à faire par l'équipe | 2026-10-13 |
| 1. Argent visible | fait (web seul) : `pistes-web.md` ; 1 piste avec argent vérifié (reprise micro-SaaS), budget non résolu | 2026-11-02 |
| 2. Engagement | à faire | |
| 3. Taille et choix | à faire | |
| 4. Confirmation | à faire | |

## À éviter (idées déjà étudiées, archivées)

Une piste neuve qui recoupe l'une de ces idées est signalée et mise de côté, pas creusée.

- v1 : recrutement pour les garages automobiles.
- v2 : agences locales de services (ménage, dépannage, garde d'enfants, déménagement, marketing pour artisans)
  et les 22 idées de `ideas/_archives/_recherche-v2/idees-classees.md`.
- v3 : facture électronique (experts-comptables, TPE du bâtiment, PME, négoces) ; bailleurs, SCI, LMNP et
  petites foncières face au DPE ; installateurs RGE, batteries, panneaux en toiture, autoconsommation
  collective ; supermarchés indépendants (OPERAT).

## Sous-agents

| Vague | Agent | Mission | Fichier | Statut |
|-------|-------|---------|---------|--------|
| 1 | chercheur | voie distribution | porte1/distribution-*.md | partiel (preuves déclassées, 6/10 ≈/✘) |
| 1 | chercheur | reprise | porte1/reprise-*.md | partiel (2/10 ≈) |
| 1 | verificateur | 20 preuves | porte1/verification.md | fini |
| 2 | chercheur | modèles Acquire.com à copier | porte1/modeles-acquire-*.md | partiel (1/10 ≈) |
| 2 | chercheur | modèles TrustMRR/Starter Story | porte1/modeles-mrr-*.md | partiel (7/10 ≈/✘, déclassé) |
| 2 | verificateur | 20 preuves | porte1/verification-modeles.md | fini |

## Journal

- 2026-10-14 (matin) : pièces du système v4 revérifiées (6 skills identiques à la source, scout non copiable : voir
  `.claude/skills/SOURCES.md`).
- 2026-10-14 (matin) : `methode/proposition-seuils.md` écrit (changements de seuils proposés, non appliqués ;
  5 lignes déjà modifiées le 13/10 à confirmer).
- 2026-10-14 (matin) : portes 1 et 2 appliquées aux 12 segments v3 avec les preuves existantes (aucun agent, aucune
  recherche web) : 1 éliminé, 11 à revoir, 0 passe. Fichier archivé après la remise à zéro :
  `ideas/_archives/_recherche-v3/tri-sans-recherche.md`.
- 2026-10-14 (après-midi) : remise à zéro des idées (voir en-tête et « À éviter »).
- 2026-10-15 : 50 skills ajoutés (`.claude/skills/SOURCES.md`) ; branche réconciliée avec les commits du matin du 14.

- 2026-11-02 : l'équipe choisit la recherche seule, sans entretiens réseau (porte 0 non faite). Porte 1 lancée (forfait à 34 %).

- 2026-11-02 (après-midi) : relance de zéro limitée à l'énergie (CLAUDE.md modifié). Pistes v3 rouvrables avec
  un angle nouveau. Vague E1 : 4 chercheurs, fichiers `porte1/energie-*`. Forfait à 34 %.

| Vague | Agent | Mission | Fichier | Statut |
|-------|-------|---------|---------|--------|
| E1 | chercheur | achat et facture d'énergie des TPE/PME/collectivités | porte1/energie-achat-* | partiel (11/15, courtage seul a de l argent) |
| E1 | chercheur | efficacité, rénovation, conformité (DPE, décret tertiaire, audits) | porte1/energie-efficacite-* | partiel (11/15, prix affichés seulement) |
| E1 | chercheur | production locale, stockage, IRVE, flexibilité | porte1/energie-production-* | partiel (9/15, preuves surtout en extraits) |
| E1 | chercheur | voie distribution et reprise dans l'énergie | porte1/energie-distribution-* | partiel (11/15 recherches, Fusacq bloqué) |
| E1 | verificateur | 10 preuves x 4 fichiers | porte1/energie-verification.md | fini : alerte achat 22 %, efficacité 50 %, production 57 %, distribution 67 % |
- 2026-11-02 : l'équipe refuse la reprise ; nouvelle voie = copier en France un modèle étranger rentable. Classement dans `pistes-web.md`.

## Reprise

Le 2026-10-14, le forfait hebdomadaire était à 99 % (remise à zéro le 2026-10-15 à 11 h 59, heure de Paris).
Aucun agent n'a été lancé. Le ménage est fait et commité. Pendant ce temps, l'équipe peut commencer la porte 0
(`kit-porte0.md`) : les 30 conversations restent la première source d'idées.

Prompt à coller dans une nouvelle session, après la remise à zéro du forfait :

```text
Lis CLAUDE.md (workflow v4 par portes, critères de viabilité), relancer-la-recherche-v4.md et
ideas/_recherche-v4/etat.md. Remise à zéro du 2026-10-14 : aucune idée des recherches précédentes n'est une
entrée ; ne lis pas ideas/_archives/, sauf un Grep pour vérifier qu'une piste n'y figure pas déjà.
1. Lis l'usage du forfait (get_usage). Au-delà de 85 % : un seul agent à la fois, 12 recherches web au plus.
   À 95 % : arrête-toi, mets à jour la section Reprise d'etat.md, commite et pousse.
2. Porte 1, pistes neuves sur le web : 2 agents « chercheur », 12 recherches web chacun, chacun avec un
   fichier de travail et une synthèse de 40 lignes dans ideas/_recherche-v4/porte1/ :
   a. Voie distribution : 8 produits ou services qui encaissent déjà à l'étranger (Europe, Royaume-Uni,
      États-Unis), absents ou mal servis en France, achetés par des particuliers, des indépendants ou des TPE,
      et où l'on peut être agent commercial, distributeur, revendeur ou apporteur d'affaires. Pour chacun :
      preuve d'argent encaissé, 3 prix publics, présence actuelle en France, commission ou marge connue,
      contrat type.
   b. Reprise : 8 types de petites entreprises à céder en France, sites et logiciels en ligne compris
      (annonces de cession : CRA, Fusacq, Bpifrance Transmission, places de marché de sites). Pour chacun :
      prix, CA, raison de la vente, financement possible avec 5 000 € d'apport et un prêt.
   Exclure ce qui recoupe la liste « À éviter » d'etat.md, et tout métier d'employeur à marge fine.
3. Un « verificateur » contrôle 10 preuves par fichier.
4. Écris ideas/_recherche-v4/pistes-web.md : pistes classées avec la grille de CLAUDE.md (score provisoire,
   engagement = 0), la croyance la plus fragile (skill before-you-build) et, pour chacune, où trouver
   20 clients nommés joignables. Puis arrête-toi et attends les comptes rendus de la porte 0.
Tiens etat.md à jour. Commite et pousse sur la branche claude/recherche-idee-v1 après chaque étape.
```

- 2026-11-02 (après-midi) : demande de l'équipe « trouver une idée en partant de zéro pour l'agroalimentaire ».
  Piste agro ouverte à côté de l'énergie (le périmètre énergie de CLAUDE.md n'est pas modifié). Vague A1 :
  4 chercheurs, 12 recherches web chacun, fichiers `porte1/agro-*`. Forfait à 35 %.

| Vague | Agent | Mission | Fichier | Statut |
|-------|-------|---------|---------|--------|
| A1 | chercheur | logiciels et services payés par les TPE/PME agro (traçabilité, étiquetage, HACCP, certifications) | porte1/agro-pme-* | partiel (12/12 ; 4 pages en 403, prix surtout tirés d extraits) |
| A1 | chercheur | restauration commerciale et collective (EGalim, biodéchets, gaspillage, achats locaux) | porte1/agro-restauration-* | partiel (11/12 recherches ; Capterra bloqué, prix gaspillage non publiés) |
| A1 | chercheur | voie distribution agro (produits prouvés à l'étranger, absents en France) | porte1/agro-distribution-* | partiel (12/12 ; Brewbound 403) |
| A1 | chercheur | reprise et modèles B2C/e-commerce agro qui encaissent | porte1/agro-reprise-* | partiel (11/12 ; Fusacq 403, Starter Story non suivi) |
