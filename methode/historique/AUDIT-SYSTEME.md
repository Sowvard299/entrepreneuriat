# Audit du système de recherche d'idée (13 octobre 2026)

Périmètre : `CLAUDE.md`, les 12 skills de `.claude/skills/`, les 3 agents de `.claude/agents/`, les
guides `relancer-la-recherche.md` (v2) et `relancer-la-recherche-v3.md`, et les résultats des deux
itérations : v1 (`ideas/_recherche/`, gagnante `ideas/recrutement-garages/`) et v2
(`ideas/_recherche-v2/`, arrêtée en phase 4).

## 1. Le constat

Deux itérations, environ 340 signaux et 300 sites lus, et le même résultat : **une agence de services
pour une niche, dont le plafond est trop bas pour faire vivre 6 personnes.**

| Itération | Gagnante ou top | Plafond chiffré | Verdict |
|-----------|-----------------|-----------------|---------|
| v1 | Recrutement par vidéo pour garages et carrosseries | SAM France 8 à 14 M€, SOM à 3 ans ≈ 266 k€, revenu de 52 €/h qui casse sous 30 €/h | « Conditionnel 6/10 » ; scorecard : « trop peu pour une start-up » |
| v2 | Top 8 : marketing pour artisans, dépannage, ménage, déménagement, salons, vidéo, garde d'enfants, syndic | Agences locales, marges de 3 à 16 % pour les métiers d'employeur | Jugées non viables par l'équipe |

Ce n'est pas un manque de recherche. C'est la forme de l'entonnoir qui produit ce résultat.

## 2. Les causes profondes

### C1. Les contraintes ne laissent passer que des agences de main-d'œuvre
Pas de développeur, 5 000 €, temps partiel, premier euro en 3 mois, aucune licence, test à moins de
500 € : la seule chose qui passe tous ces filtres est un service vendu à l'heure. Or l'ambition
(500 k€ de CA récurrent, vivre à 6) exige alors des dizaines d'intervenants ou des centaines de
clients, avec des marges fines. **Les contraintes et l'ambition se contredisent, et aucun document ne
tranche cette contradiction.** La v3 la déplace (seuils de taille éliminatoires) sans la résoudre :
elle risque de finir par « aucune idée ne passe ».

### C2. Les seuls vrais avantages de l'équipe ne sont pas exploités
- **Le marketing** est noté 10 à 15 % comme « avantage », alors qu'il devrait choisir le **type
  d'entreprise** : celles où la réussite dépend d'abord de l'acquisition et de la marque (marque de
  produits, e-commerce de niche, média ou communauté monétisée, génération de leads). Le marketing est
  le métier du fondateur, mais ces catégories ont été écartées par réflexe (« stock », « pas de
  service ») ou jamais explorées.
- **La connaissance de l'intérieur** (offres d'électricité pour TPE/PME chez EDF) compte pour 10 %.
  `CLAUDE.md` interdit, à juste titre, d'en faire un filtre, mais ne la transforme pas non plus en
  lentille de recherche.
- **Le réseau des 6** est vide (« tout le monde »). Les deux runs ont donc choisi des segments où
  l'équipe n'a aucun accès privilégié : garages, artisans, syndics.

### C3. La viabilité se décide sur le terrain, mais le terrain arrive en dernier ou jamais
Chaque run se termine par « les 3 hypothèses qui peuvent tuer le projet » et un kit d'entretiens. Les
deux prompts demandent à `startup-design` de **sauter** sa phase Customer Discovery, que le skill
exige pourtant même en Fast Track (au moins 3 entretiens, section 3.7). Résultat : des semaines de
dossiers (Lean Canvas, pré-mortem, TAM/SAM/SOM) sur une idée qu'aucun client n'a confirmée.

### C4. Les scores sont des notes subjectives qui gonflent
- En v1, chaque audit a retiré 0,5 à 1,5 point (voir `ideas/_recherche/phase4/tournoi.md`) ; en v2, le
  même modèle notait puis classait ses propres idées.
- Une moyenne pondérée cache un défaut fatal : une idée notée 9 partout sauf « plafond » passe devant
  une idée solide.
- Les notes de 1 à 10 de la grille de `CLAUDE.md` n'ont pas de repères écrits (le scanner en a, la
  grille non).

### C5. Un méga-prompt en une seule session
Six phases, plusieurs dizaines d'agents et des dossiers complets dans une seule conversation. Les erreurs
du début se propagent, la limite de session coupe le travail (2 fois en v1, 1 fois en v2), et
l'équipe ne peut corriger le cap qu'à 2 points d'arrêt.

### C6. Des seuils difficiles à mesurer
« 3 premiers acteurs < 40 % du marché » et le SAM d'une niche ne sont presque jamais publiés gratuitement
(Xerfi et Statista sont payants). Sans règle claire pour l'inconnu, l'agent remplit de [HYPOTHÈSE] ou
élimine à tort.

### C7. Des skills mal ajustés à cette équipe
| Skill | Problème |
|-------|----------|
| `ai-startup-opportunity-generator` | pensé pour des SaaS d'IA codés en Laravel ; sa grille (« automation fit ») ne s'applique pas à une équipe qui ne code pas. Seule sa référence `failure-patterns.md` est vraiment utile. |
| `startup-design` | 476 lignes, beaucoup de phases (marque, produit, finances) inutiles avant validation ; on lui fait sauter la seule phase décisive (entretiens). |
| `llm-council` | 5 personas du même modèle : utile comme contradicteur, pas comme preuve. Il a validé à l'unanimité une idée à 266 k€ de SOM en v1. |
| `brainstorm-ideas-new` | correctement repositionné en v3 (fonctionnalités d'un produit choisi). |

### C8. Des chemins jamais explorés
- **Reprendre une petite entreprise rentable** au lieu de créer : les annonces DotMarket et Fusacq
  (v2, F4-22 à F4-30) montrent des sites et activités rentables de 25 000 à 330 000 €. Le budget de
  5 000 € l'exclut seul, mais pas avec un financement (voir P7).
- **Les dispositifs pour étudiants entrepreneurs** (statut national d'étudiant-entrepreneur via les
  PEPITE, prêts d'honneur, incubateurs d'école) changent les contraintes de temps et de budget.
  Aucun run ne les a regardés.

## 3. Ce qui fonctionne et doit être gardé

- Les règles de preuve (sources datées, citation courte, [HYPOTHÈSE], contre-preuve) et la
  vérification par l'API Recherche d'entreprises (CA réels de dizaines d'acteurs).
- Les audits concurrentiels : ils ont réellement fait tomber de mauvaises idées (facture électronique,
  copropriétés en v1).
- Les fichiers écrits au fil de l'eau, qui permettent de reprendre après une coupure.
- La v3 : marché d'abord, seuils de taille, 2 points d'arrêt, agents dédiés, vérificateur.

## 4. Propositions, par ordre d'impact

### P1. Trancher la contradiction contraintes / ambition en choisissant un archétype d'entreprise
Ajouter dans `CLAUDE.md` une étape 0 : l'équipe choisit 1 ou 2 archétypes compatibles avec 6 profils
marketing qui ne codent pas.

| Archétype | Pourquoi il colle | Point dur |
|-----------|-------------------|-----------|
| A. Marque de produits (DNVB, e-commerce de niche, agroalimentaire) | la réussite dépend d'abord du marketing et de l'acquisition ; marges brutes souvent supérieures à 50 % | stock et fabrication : sous-traitance, précommande, petites séries |
| B. Service productisé à forte marge, outillé (no-code, IA) | prix fixe, pas d'intervenants à embaucher, l'équipe vend et livre | le leader peut copier : il faut une niche verticale et une marque |
| C. Média ou communauté monétisée (contenu, affiliation, leads, événements) | 100 % compétences de l'équipe, coûts faibles | revenus lents la première année |
| D. Reprise d'une petite activité rentable | revenus dès le premier jour | financement à trouver (prêt d'honneur, prêt bancaire) |
| E. Agence de main-d'œuvre (ménage, dépannage…) | rapide à lancer | **déconseillé** : marges fines, plafond bas, aucun avantage ; seulement si les seuils de l'économie unitaire (P3) passent |

### P2. Mettre le terrain au milieu, pas à la fin
Nouveau point d'arrêt 1 bis, juste après le choix des marchés : un **sprint terrain d'une semaine**.
Chacun des 6 fait 5 conversations (Mom Test) avec des personnes des 3 à 5 marchés retenus, en partant
des contacts de l'équipe. Les notes vont dans `ideas/_recherche-v3/terrain/`. La phase 1 s'appuie
sur ce qu'ils ont entendu, pas seulement sur le web.
Règle de décision : **aucune idée n'est déclarée gagnante sans au moins 10 conversations et au moins un
signal d'engagement** (précommande, lettre d'intention, pilote payé, rendez-vous de suivi accepté).

### P3. Remplacer la moyenne pondérée par des portes, puis classer
1. **Portes éliminatoires chiffrées** (passe / ne passe pas) : seuils de `CLAUDE.md` + 3 nouvelles :
   - marge brute ≥ 50 % (sauf archétype D) ;
   - revenu ≥ 50 € par heure de travail de l'équipe au bout de 6 mois ;
   - coût d'acquisition d'un client remboursé en moins de 3 mois.
2. **Classement** des seules idées qui passent, avec la grille de `CLAUDE.md` et des repères 0 / 5 / 10
   écrits pour chaque critère, comme dans le scanner.
3. **Audit en aveugle** : l'auditeur ne voit pas le score initial (moins d'ancrage), et une seconde
   lecture « avocat du diable » cherche le défaut fatal.

### P4. Couper le méga-prompt en 4 sessions courtes
| Session | Contenu | Livrable | Durée |
|---------|---------|----------|-------|
| 1. Cartographie | archétypes choisis, 30 marchés → 8 | `marches.md` | 1 session |
| 2. Terrain (humains) | 30 conversations, notes | `terrain/` | 1 semaine |
| 3. Segments, angles, tournoi | segments, idées, portes, audits, conseil | `idees-classees.md`, `tournoi.md` | 1 à 2 sessions |
| 4. Dossier et test | dimensionnement, économie unitaire, expérience de prévente | `ideas/<idee>/` | 1 session, **seulement après un GO terrain** |

Chaque session a son propre prompt court et commence par lire `etat.md`. Le Lean Canvas, le pré-mortem
et le dossier complet ne sont produits qu'en session 4.

### P5. Rendre les seuils mesurables
- Concentration : « si mesurable, sinon donner les 3 premiers acteurs nommés et leur CA déposé ».
- Taille : calcul bottom-up obligatoire (clients identifiables × dépense constatée), le top-down sert
  seulement à recouper.
- Un seuil non mesurable n'élimine pas : il devient un risque à lever sur le terrain.

### P6. Alléger et réaligner les skills
- Retirer `ai-startup-opportunity-generator` du workflow ; garder seulement sa référence
  `failure-patterns.md`, citée par l'auditeur.
- `startup-design` : n'utiliser que la porte de recherche (3.5) et la découverte client (3.7), jamais en
  sautant les entretiens.
- `llm-council` : seulement comme « red team » sur les 3 finalistes, avec la consigne de chercher le
  défaut fatal ; il ne départage pas sans preuves de terrain.

### P7. Ajouter une fiche « ressources et financement »
Avant la session 1, un agent `chercheur` vérifie sur sources officielles : le statut national
d'étudiant-entrepreneur et le PEPITE de l'école, les prêts d'honneur accessibles en Île-de-France, les
incubateurs d'école, les concours. Il en tire le budget réel possible. Aucun chiffre à retenir
avant vérification.

### P8. Pistes concrètes à mettre dans la longue liste (hypothèses, pas des conclusions)
Elles découlent de P1. Chacune doit passer les portes comme les autres.
1. **Énergie pour TPE/PME** (avantage : connaissance de l'intérieur). Courtage ou achat groupé
   d'électricité et de gaz, service de suivi des contrats, mise en conformité énergie. Question
   préalable : la clause de non-concurrence ou d'exclusivité du contrat d'alternance chez EDF.
2. **Marque agroalimentaire ou boisson en DNVB** (avantage : marketing, intérêt agro). Fabrication
   sous-traitée (façonnier), précommande ou crowdfunding pour financer le stock.
3. **Média vertical + génération de leads B2B** sur un marché où les fournisseurs paient cher
   le contact (énergie, rénovation, logiciels pour TPE). Les signaux v2 montrent ~11 € par visiteur et
   par an dans l'affiliation de niche (F4-23).
4. **Reprise d'un petit e-commerce ou d'un site rentable** (DotMarket, de 25 000 à 85 000 € pour
   1 500 à 5 000 € de profit mensuel, F4-30), financée par prêt d'honneur, que l'équipe fait grandir
   par le marketing.

## 5. Plan de mise en œuvre proposé

| Ordre | Action | Qui | Effort |
|-------|--------|-----|--------|
| 1 | Compléter les ☐ de `CLAUDE.md` | l'équipe | 15 min |
| 2 | Choisir 1 ou 2 archétypes (P1) | l'équipe | 1 réunion |
| 3 | Mettre à jour `CLAUDE.md`, le scanner, les agents et le guide v3 : portes chiffrées, archétypes, audit en aveugle, 4 sessions, skills allégés (P1 à P6) | Claude | 1 session |
| 4 | Vérifier ressources et financement (P7) | Claude, agent `chercheur` | 1 agent |
| 5 | Lancer la session 1 (cartographie) | Claude | 1 session |
| 6 | Sprint terrain (P2) | l'équipe | 1 semaine |

Les étapes 1 et 2 ne peuvent pas être faites par Claude : ce sont elles qui feront la différence
avec les deux premiers runs.
