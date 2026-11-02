# Entrepreneuriat : trouver une idée d'entreprise

Espace de travail pour trouver, valider et choisir une idée d'entreprise.
Les skills sont dans `.claude/skills/` (sources dans `.claude/skills/SOURCES.md`), les sous-agents dans
`.claude/agents/`. Réponds toujours en français. Ce fichier est lu en premier par tous les skills et
tous les sous-agents : il est la **source unique** des seuils et de la grille de score (section
« Critères de viabilité »).

## Point de départ neutre (2026-11-02)

La recherche part de zéro, sans aucune information sur les fondateurs : ni compétences, ni secteur connu,
ni réseau, ni budget, ni temps disponible, ni zone, ni exclusion. Aucune piste n'est favorisée ou écartée
parce qu'elle conviendrait ou non à l'équipe. Les ressources nécessaires (capital, compétences, licences,
délai) sont **décrites et chiffrées** pour chaque piste, jamais utilisées comme filtre. Le seul critère est
la viabilité de l'entreprise.

## Périmètre des idées

Tous les secteurs, modèles économiques et types de clients (B2B, B2C, services, produits physiques,
logiciels, industrie), en France comme point de départ du marché.

On ne cherche pas à innover. On cherche un modèle qui existe déjà et se vend, dans un marché qui grossit,
sur un segment précis, et un moyen de le faire mieux (service, délai, prix, cible négligée, marketing,
zone mal servie).

## Critères de viabilité (modifiables)

Ces seuils mesurent la viabilité du marché et du modèle, pas l'adéquation avec l'équipe. On peut les
changer ici, une ligne à la fois, en notant pourquoi. Tout chiffre utilisé doit être sourcé (URL, année,
périmètre) ou marqué [HYPOTHÈSE].

| Critère | Seuil par défaut | Effet |
|---------|------------------|-------|
| Taille du marché (SAM France) | ≥ 50 M€ / an | éliminatoire à la porte 3 |
| Croissance | ≥ 8 % / an sur 3 ans, ou moteur structurel daté | souhaité |
| Concentration | 3 premiers acteurs < 40 % du marché | éliminatoire, sauf angle crédible |
| Clients identifiables | ≥ 3 000 (B2B) ou ≥ 100 000 (B2C) | éliminatoire |
| SOM à 3 ans (calcul bottom-up) | ≥ 500 k€ de CA / an | éliminatoire, sauf chemin d'expansion démontré |
| Argent déjà dépensé | ≥ 3 prix publics réellement payés par le segment, clients payants identifiés | éliminatoire dès la porte 1 |
| Engagement client | sur 10 contacts : ≥ 3 engagements d'argent ou ≥ 5 de temps [HYPOTHÈSE de seuil, à écrire avant] | éliminatoire à la porte 2 |
| Ressources nécessaires | capital avant le premier euro, compétences, licences, délai jusqu'au premier client | décrit et chiffré, jamais éliminatoire |

Quand aucune taille de marché publiée n'est fiable, on calcule la taille bottom-up : nombre de clients
(Sirene, Urssaf, Insee) × dépense annuelle constatée (prix publics). La confiance est alors « moyenne » au mieux.

**Un segment de départ peut être petit** s'il ouvre un chemin d'expansion vers des segments voisins dont
le total dépasse les seuils de taille. Le chemin doit être écrit et chiffré.

## Grille de score (sur 10, pondérée)

Avant la porte 2, la ligne « Engagement client » vaut 0 et le score est provisoire.

- Engagement client mesuré à la porte 2 (argent > temps > réputation) : 25 %
- Argent déjà dépensé sur ce modèle (prix publics payés, clients identifiés) : 25 %
- Taille et croissance du marché (bottom-up avec les prix constatés) : 20 %
- Faiblesse prouvée des acteurs en place (avis, prix, délais) : 15 %
- Segment accessible (clients identifiables + canal d'acquisition existant) : 15 %

## Workflow (par portes)

Une piste n'avance que si elle passe la porte. Guide pas à pas : `relancer-la-recherche-v4.md`.

1. **Modèle prouvé et argent visible** : le modèle encaisse déjà en France ou ailleurs (TrustMRR, Acquire,
   Starter Story, annonces de cession comme source d'inspiration) ; ≥ 3 prix publics payés ; douleurs et
   faiblesses des concurrents avec `competitor-analysis` et `sentiment-analysis` ; puis `before-you-build`
   pour nommer la croyance la plus fragile et le test qui la lève. Sources d'idées : modèles étrangers
   rentables absents ou mal servis en France, `market-segment-scanner`, `ai-startup-opportunity-generator`.
2. **Engagement** : 10 contacts ou un test de demande (fausse porte, précommande) ; `interview-script` et
   `mom-test` ; seuil écrit avant.
3. **Taille et choix** : `market-sizing`, `beachhead-segment`, `identify-assumptions-new`, `lean-canvas`,
   puis `llm-council`.
4. **Confirmation** : `brainstorm-experiments-new`, pilote payant, puis GO / PIVOT / STOP.

## Sous-agents et coordination

La session principale coordonne ; la collecte se fait dans des sous-agents définis dans
`.claude/agents/` (on les appelle par leur nom avec l'outil Agent, `subagent_type`) :

| Agent | Modèle | Rôle |
|-------|--------|------|
| `chercheur` | sonnet | collecte de preuves (fiches marché, signaux par segment) |
| `auditeur` | sonnet | concurrents, échecs, droit, économie unitaire, score recalculé |
| `verificateur` | haiku | rouvre un échantillon d'URL et vérifie citations et chiffres |

Règles :
- **Vagues de 4 agents au plus.** Chaque agent reçoit son fichier de travail ET son fichier de
  synthèse ; il écrit au fil de l'eau.
- **Le coordinateur ne lit que les fichiers de synthèse** (40 lignes maximum chacun). Il ouvre un
  fichier de travail seulement pour une preuve précise (Grep sur l'ID).
- **`etat.md` tenu à jour après chaque vague** : agent, mission, fichier, statut (fini / partiel / coupé).
- **Vérification** : après chaque vague, un `verificateur` contrôle 10 preuves par fichier. Si plus de
  20 % sont en ✘ ou ≈ sur des chiffres utilisés, on relance le chercheur concerné ou on déclasse ses
  preuves. Toutes les preuves citées pour l'idée gagnante sont vérifiées.
- **`llm-council`** : les 5 conseillers et les 5 relecteurs tournent en `model: sonnet`, seul le
  président garde le modèle principal.
- Le droit n'est jamais laissé en [HYPOTHÈSE] pour une finaliste : l'auditeur cite l'article.
- **Budget d'usage du forfait Claude** : avant chaque vague, lire l'usage (`get_usage`). Au-delà de 85 % de la
  limite hebdomadaire : un seul agent à la fois, 12 recherches web au plus. À 95 % : plus d'agent, mettre à
  jour `etat.md` (section reprise), commiter et pousser.
- **Copier de l'existant avant d'écrire** : avant de créer un skill ou un agent, chercher un équivalent sous
  licence libre, le noter dans `.claude/skills/SOURCES.md`. Jamais de contenu sous licence non commerciale.

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

- Recherche en cours : `ideas/_recherche-v4/` (etat.md, porte1/). Méthode : `methode/`.
- Une idée retenue : `ideas/<nom-de-l-idee>/`.
- Recherches précédentes : `ideas/_archives/`. Ce ne sont pas des entrées ni des exclusions.
- `memory/` : sorties des skills de MaxKmet, pensés pour les applis B2C américaines. Leurs barèmes ne
  remplacent ni les seuils ni la grille ci-dessus.
