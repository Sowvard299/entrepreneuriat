# Entrepreneuriat : trouver une idée d'entreprise

Espace de travail pour trouver, valider et choisir une idée d'entreprise.
Les skills sont dans `.claude/skills/` (sources dans `.claude/skills/SOURCES.md`), les sous-agents dans
`.claude/agents/`. Réponds toujours en français. Ce fichier est lu en premier par tous les skills et
tous les sous-agents : il est la **source unique** des seuils et de la grille de score (section
« Critères de viabilité »).

## Profil fondateur

Les lignes marquées ☐ sont à compléter : tant qu'elles sont vagues, les segments
et les entretiens restent génériques.

- **Compétences :** Marketing. Fin de master, alternant Product Manager chez EDF
  (offres d'électricité pour TPE/PME).
- **Secteur connu de l'intérieur :** énergie / électricité B2B pour PME. C'est un
  avantage à scorer, jamais un filtre.
- **Intérêts :** IA, deeptech, agroalimentaire. Ouvert à tous les secteurs.
- **Problèmes vus au travail :** « l'innovation est trop lente dans un grand groupe ».
  ☐ C'est un constat, pas encore un problème de marché. Ajouter 2 ou 3 situations
  concrètes (quel client, quelle offre, quel blocage, quel prix) vues chez EDF ou ailleurs.
- **Réseau :** ☐ remplacer « tout le monde » par 3 à 5 contacts ou communautés nommés
  (secteur, taille d'entreprise, ville). C'est ce qui décide du segment de départ.
- **Équipe (6) :** ☐ une ligne par personne.

  | Prénom | Compétence principale | Heures/semaine | Contacts utiles |
  |--------|----------------------|----------------|-----------------|
  | ☐ | | | |

- **Temps :** temps partiel pendant l'année scolaire, puis projet à temps plein après
  le diplôme (☐ date : ______).
- **Budget :** 5 000 € autofinancés ; pré-amorçage possible si le projet est très solide.
- **Zone du premier marché :** Paris / Île-de-France, ou France entière.
- **Ambition :** vivre de l'entreprise.
  ☐ Chiffrer : revenu visé par personne et nombre de personnes à rémunérer.
  Formule : CA cible ≈ (rémunérations + charges) ÷ taux de marge brute.
  Hypothèse par défaut tant que ce n'est pas chiffré : **500 k€ de CA récurrent par an à 3 ans.**
- **À ne pas faire :** rien d'exclu. ☐ Préciser au moins ce qui ferait arrêter
  l'un de vous (stock, déplacements, démarchage à froid, métier réglementé, être employeur
  de nombreux intervenants...).

## Périmètre des idées

Ne pas se limiter à l'énergie, EDF, les TPE/PME, l'IA, la deeptech ou l'agro.
Explorer tous les secteurs, modèles économiques et types de clients (B2B, B2C,
services, produits physiques, logiciels). Le profil ci-dessus est du contexte :
il compte comme avantage dans le score, jamais comme condition.

On ne cherche pas à innover. On cherche un modèle qui existe déjà et se vend, dans
un marché qui grossit, sur un segment précis, et un moyen de le faire mieux
(service, délai, prix, cible négligée, marketing, zone mal servie).

Leçon de la v2 (octobre 2026, `ideas/_recherche-v2/BILAN.md`) : partir des avis négatifs a produit
des « agences locales de plus » (ménage, dépannage, garde d'enfants, marketing pour artisans), jugées
non viables : marges fines, métier d'employeur, aucun avantage défendable, plafond bas. Une idée de ce
type doit démontrer pourquoi elle dépasse le seuil de SOM et ce qui la rend difficile à copier ; sinon
elle reste au mieux une réserve de la piste rapide.

## Critères de viabilité (modifiables)

Ces seuils sont des hypothèses de départ. On peut les changer ici, une ligne à la fois,
en notant pourquoi. Tout chiffre utilisé doit être sourcé (URL, année, périmètre) ou
marqué [HYPOTHÈSE].

| Critère | Seuil par défaut | Effet |
|---------|------------------|-------|
| Taille du marché (SAM France) | ≥ 50 M€ / an | éliminatoire à la porte 3 seulement (modifié 2026-10-13 : la taille se mesure après un signal client, voir `ideas/_recherche-v3/audit-systeme-v3.md`) |
| Croissance | ≥ 8 % / an sur 3 ans, ou moteur structurel daté dont la dépense continue après l'échéance | souhaité ; éliminatoire pour la piste ambitieuse (modifié 2026-10-13 : 0 marché sur 38 la prouvait, aucune méthode de praticien ne l'exige) |
| Concentration | 3 premiers acteurs < 40 % du marché | éliminatoire, sauf angle crédible |
| Clients identifiables | ≥ 3 000 (B2B) ou ≥ 100 000 (B2C) | éliminatoire |
| SOM à 3 ans (calcul bottom-up) | ≥ 500 k€ de CA / an | éliminatoire, sauf chemin d'expansion démontré |
| Argent déjà dépensé | ≥ 3 prix publics réellement payés par le segment, clients payants identifiés | éliminatoire dès la porte 1 |
| Premier client payant | ≤ 3 mois (pilote ou précommande acceptés) | éliminatoire |
| Contrat récurrent | ≤ 6 mois | souhaité |
| Budget avant le premier euro | piste rapide ≤ 5 000 € ; piste ambitieuse ≤ 20 000 € | éliminatoire |
| Piste ambitieuse | seulement si SAM ≥ 200 M€ et croissance ≥ 10 % / an | condition d'accès |
| Droit | pas de diplôme, agrément ou licence qu'on n'a pas | éliminatoire |
| Accès | 20 clients potentiels nommés, joignables par l'équipe | éliminatoire dès la porte 0 (modifié 2026-10-13) |
| Engagement client | sur 10 contacts en 1 semaine : ≥ 3 engagements d'argent (acompte, précommande, lettre d'intention) ou ≥ 5 de temps (démo datée, présentation au décideur) [HYPOTHÈSE de seuil, à écrire avant d'appeler] | éliminatoire à la porte 2 (ajouté 2026-10-13) |
| Dépendance technique | développement lourd nécessaire | marquer « besoin d'un associé tech », pas éliminatoire |

Quand aucune taille de marché publiée n'est fiable (fréquent : les études Xerfi ou Statista sont
payantes), on calcule la taille bottom-up : nombre de clients (Sirene, Urssaf, Insee) × dépense
annuelle constatée (prix publics). La confiance est alors « moyenne » au mieux.

**Un segment de départ peut être petit** s'il ouvre un chemin d'expansion vers des segments
voisins dont le total dépasse les seuils de taille. Le chemin doit être écrit et chiffré.

**Deux pistes** à garder en parallèle : la piste rapide (autofinancée, premiers clients vite)
et la piste ambitieuse (marché plus grand, éventuel pré-amorçage). Le classement final
nomme une idée de réserve par piste.

## Grille de score (sur 10, pondérée)

Modifiée le 2026-10-13 pour la v4 : la preuve client pèse plus que la taille de marché, qui reste un plafond
vérifié à la porte 3. Avant la porte 2, la ligne « Engagement client » vaut 0 et le score est provisoire.

- Engagement client mesuré à la porte 2 (argent > temps > réputation) : 25 %
- Argent déjà dépensé sur ce modèle (prix publics payés, clients identifiés) : 20 %
- Segment accessible (clients nommés + canal d'acquisition testé) : 15 %
- Taille et croissance du marché (bottom-up avec les prix entendus) : 15 %
- Faiblesse prouvée des acteurs en place (avis, prix, délais) : 10 %
- Avantage de l'équipe (vente, contenu, acquisition, contacts, secteur connu) : 10 %
- Vitesse jusqu'au premier client payant : 5 %

## Workflow (v4, par portes : viable dès le début, puis confirmé)

Une piste n'avance que si elle passe la porte. Guide pas à pas : `relancer-la-recherche-v4.md`.
Pourquoi : audit `ideas/_recherche-v3/audit-systeme-v3.md` et veille `ideas/_recherche-v3/veille-systeme.md`.

0. **Accès** : profil de l'équipe rempli ; pour chaque piste, 20 clients nommés joignables. Sinon, pas de recherche.
1. **Modèle prouvé et argent visible** (1 `chercheur` par paire de pistes, budget court) : le modèle encaisse
   déjà en France ou ailleurs (TrustMRR, annonces de cession, Starter Story) ; ≥ 3 prix publics payés ; douleurs
   et faiblesses des concurrents avec `competitor-analysis` et `sentiment-analysis` ; puis `before-you-build`
   pour nommer la croyance la plus fragile et le test qui la lève. Les idées en entrée peuvent venir de
   `market-segment-scanner` (liste de marchés et segments), de `ai-startup-opportunity-generator` ou de l'équipe.
2. **Engagement** (terrain, 1 semaine, < 100 €) : `interview-script` et `mom-test` pour 10 conversations,
   `summarize-interview` après chacune ; seuil d'engagement écrit avant d'appeler.
3. **Taille et choix** : pour les pistes qui passent la porte 2 seulement : `market-sizing` (bottom-up avec les
   prix entendus), `beachhead-segment`, `identify-assumptions-new`, `lean-canvas`, puis `llm-council` avec deux
   questions : (a) clients payants en 3 mois ? (b) faire vivre l'équipe à 3 ans ?
4. **Confirmation** : `brainstorm-experiments-new` (précommande, MVP concierge, fausse porte, seuils écrits
   avant), pilote payant, puis GO / PIVOT / STOP. `brainstorm-ideas-new` sert ensuite à définir le MVP.

La recherche documentaire lourde (`market-segment-scanner` complet, vagues de chercheurs) est une option des
portes 1 et 3, jamais le point de départ.

## Sous-agents et coordination

La session principale coordonne ; la collecte se fait dans des sous-agents définis dans
`.claude/agents/` (on les appelle par leur nom avec l'outil Agent, `subagent_type`) :

| Agent | Modèle | Rôle |
|-------|--------|------|
| `chercheur` | sonnet | collecte de preuves (fiches marché, signaux par segment) |
| `auditeur` | sonnet | concurrents, échecs, droit, économie unitaire, score recalculé |
| `verificateur` | haiku | rouvre un échantillon d'URL et vérifie citations et chiffres |

Règles (leçons de la v2, où la limite de session a coupé 4 auditeurs d'un coup) :
- **Vagues de 4 agents au plus.** Chaque agent reçoit son fichier de travail ET son fichier de
  synthèse ; il écrit au fil de l'eau.
- **Le coordinateur ne lit que les fichiers de synthèse** (40 lignes maximum chacun), jamais les fichiers
  de travail en entier. Lire 6 fichiers complets coûtait environ 150 000 tokens en v2. Il ouvre un
  fichier de travail seulement pour une preuve précise (Grep sur l'ID).
- **`etat.md` tenu à jour après chaque vague** : agent, mission, fichier, statut (fini / partiel /
  coupé). Après une coupure, on relance seulement les agents « partiel » ou « coupé », avec la consigne
  de relire leur fichier et de continuer sans doublon.
- **Vérification** : après chaque vague, un `verificateur` contrôle 10 preuves par fichier. Si plus de
  20 % sont en ✘ ou ≈ sur des chiffres utilisés, on relance le chercheur concerné ou on déclasse ses
  preuves. Toutes les preuves citées pour l'idée gagnante sont vérifiées.
- **`llm-council`** : les 5 conseillers et les 5 relecteurs tournent en `model: sonnet`, seul le
  président garde le modèle principal.
- Le droit n'est jamais laissé en [HYPOTHÈSE] pour une finaliste : l'auditeur cite l'article.

## Règles de preuve

- Un modèle ou un marché retenu s'appuie sur au moins 3 sources indépendantes et datées
  (idéalement moins de 24 mois). Un chiffre de croissance demande 2 sources dont une
  institutionnelle (INSEE, Eurostat, ministère, fédération, Banque de France, Bpifrance).
- Un même site ne fournit pas plus de 40 % des preuves d'un fichier.
- Ordre de force : argent déjà dépensé > recherche active d'une solution > plainte > tendance.
- Un marché dont le chiffre vient d'un vendeur de rapports ou d'un blog sans méthode est
  « confiance faible ».
- Une levée de fonds seule ne prouve pas qu'un modèle marche.
- Chaque marché ou idée finaliste a une contre-preuve notée.
- Aucun chiffre inventé. Source manquante = [HYPOTHÈSE].

## Dossiers

- Recherche en cours (v4, par portes) : `ideas/_recherche-v4/` (etat.md, portes.md, porte1/, entretiens/).
  Entrée réutilisée : `ideas/_recherche-v3/` (marches.md, segments.md, signaux/), plus l'audit et la veille.
- Une idée retenue : `ideas/<nom-de-l-idee>/`.
- Les recherches précédentes (`_recherche/`, `_recherche-v2/`, `recrutement-garages/`) ne sont lues
  qu'en option B.
