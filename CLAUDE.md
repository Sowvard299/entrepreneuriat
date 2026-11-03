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
| Argent déjà dépensé | CA du secteur (Eurostat) + ≥ 3 acteurs du modèle avec CA déposé (API) ou marchés publics notifiés (DECP), + ≥ 3 prix publics | éliminatoire dès la porte 1 (modifié 2026-11-03 : un prix affiché n'est pas une dépense) |
| Engagement client | précommande ou dépôt remboursable sur une page de test légale (voir porte 2) ; seuil écrit avant à partir du prix et du coût du trafic | éliminatoire à la porte 2 (modifié 2026-11-03 : pas d'entretiens) |
| Ressources nécessaires | capital avant le premier euro, compétences, licences, délai jusqu'au premier client | décrit et chiffré, jamais éliminatoire |

Taille, croissance, nombre de clients, concentration, marchés publics et échecs se mesurent avec
`outils/donnees.py` (sources et pièges : `methode/sources-fiables.md`), jamais par recherche web. La taille
d'un secteur est un plafond ; le marché adressable se calcule bottom-up : nombre de clients × dépense annuelle
constatée. La concentration calculée est une borne basse (≈ 45 % des comptes sont confidentiels).

**Un segment de départ peut être petit** s'il ouvre un chemin d'expansion vers des segments voisins dont
le total dépasse les seuils de taille. Le chemin doit être écrit et chiffré.

## Notation (modifiée le 2026-11-03, audit `methode/audit-2026-11/audit.md`)

Rien ne justifiait des poids fixes ni des notes à la décimale. Chaque piste reçoit des **probabilités datées**,
ancrées sur un taux de base, et déplacées seulement par des preuves fortes.

1. **Taux de base** : écrire la classe de référence (secteur INSEE × forme juridique) et son taux de survie à
   5 ans (SINE, génération 2018 : commerce 63,9 %, construction 68,5 %, info-com 65,7 %, industrie 73,4 %,
   finance 77,3 %, ensemble 69,0 % ; micro-entrepreneurs 28 % ; `methode/sources-fiables.md`).
2. **Niveau de preuve** sur chaque critère : N1 donnée officielle par l'outil, N2 page primaire, N3 étude à
   méthode, N4 déclaratif, N5 extrait. Seules les preuves N1-N2 et les actions de clients (précommande, dépôt)
   déplacent une probabilité ; N3-N4 restent des pistes.
3. **Trois probabilités**, par pas de 5 points : P(passer la porte 2), P(être en vie à 3 ans), P(CA ≥ 500 k€ à
   3 ans). Chacune cite les preuves qui l'écartent du taux de base. On les note avec leur date pour les comparer
   ensuite au résultat (score de Brier).
4. **Critères à renseigner** (sans poids) : argent déjà dépensé, taille et croissance, faiblesse des acteurs
   (avis, BODACC, prix), segment accessible, économie unitaire, timing. Deux pistes dont les probabilités sont
   à moins de 10 points l'une de l'autre ne se départagent pas : on teste les deux.
5. Pas de bonus d'ordre d'entrée ; pour un modèle étranger, écrire la cause de son succès et ce qui change en France.

## Workflow (par portes)

Une piste n'avance que si elle passe la porte. Guide pas à pas : `relancer-la-recherche-v4.md`.

0. **Écran** : `python outils/donnees.py ecran` classe les secteurs français par croissance ; on part des
   secteurs qui croissent plus vite que la médiane, sont fragmentés (CA moyen faible) et dont les échecs
   (`echecs`) ne s'emballent pas. Les exemples célèbres qu'un modèle « connaît » ne sont pas une source d'idées.
1. **Modèle prouvé et argent visible** : `fiche <NAF>` pour les chiffres standard ; le modèle encaisse déjà
   (comptes déposés en France, CA audité à l'étranger : SEC, Companies House ; annonces et classements =
   « déclaré ») ; ≥ 3 prix publics ; faiblesses des concurrents avec `competitor-analysis` et
   `sentiment-analysis` ; puis `before-you-build` pour la croyance la plus fragile et son test.
2. **Engagement, sans entretiens** : page de précommande ou de dépôt remboursable, trafic payant ciblé, seuil
   écrit avant. Cadre légal (vérifié sur Légifrance le 2026-11-03) : dire que le produit n'existe pas encore et
   donner une date de livraison (L.121-2 et L.121-3, L.221-5, L.216-1 : 30 jours par défaut), bouton « commande
   avec obligation de paiement » (L.221-14), rétractation de 14 jours (L.221-18) ; une pratique trompeuse coûte
   jusqu'à 2 ans et 300 000 € (L.132-2) ; e-mails : consentement et informations de l'article 13 du RGPD.
   Un clic, un e-mail, un volume de recherche ou une pub qui dure ne valent pas engagement.
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
- **Brief complet** : chaque mission donne objectif, format de sortie, sources à privilégier (l'outil d'abord),
  limites, budget, et autorise la sortie « non établi ». Une session = un sous-dossier de `porte1/` et une ligne
  dans `etat.md` : deux sessions n'écrivent jamais dans les mêmes fichiers.
- **Contrôle automatique d'abord** : `python outils/donnees.py controle <fichier>` et
  `python -I outils/verifier-citations.py <fichier>` sur chaque fichier de travail ; un fichier avec plus de
  20 % d'ABSENT ou d'EXTRAIT repart chez son chercheur avant tout vérificateur.
- **Vérification** : après chaque vague, un `verificateur` contrôle 10 preuves par fichier, en jugeant le
  soutien de l'énoncé et pas seulement la présence de la citation. Si plus de
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
- Niveaux de source N1 à N5 (`methode/sources-fiables.md`) : un extrait de recherche non ouvert n'est jamais
  une preuve ; un chiffre utilisé pour noter est N1 ou N2 ; trois sources = trois émetteurs (une reprise ou un
  communiqué recopié compte pour un).
- Ordre de force : argent déjà dépensé > recherche active d'une solution > plainte > tendance.
- Un marché dont le chiffre vient d'un vendeur de rapports ou d'un blog sans méthode est
  « confiance faible ».
- Une levée de fonds seule ne prouve pas qu'un modèle marche.
- Chaque marché ou idée finaliste a une contre-preuve notée.
- Aucun chiffre inventé. Source manquante = [HYPOTHÈSE].

## Dossiers

- Recherche en cours : `ideas/_recherche-v4/` (etat.md, porte1/). Méthode : `methode/` (registre des sources :
  `methode/sources-fiables.md` ; dernier audit : `methode/audit-2026-11/`). Outils : `outils/`.
- Une idée retenue : `ideas/<nom-de-l-idee>/`.
- Recherches précédentes : `ideas/_archives/`. Ce ne sont pas des entrées ni des exclusions.
- `memory/` : sorties des skills de MaxKmet, pensés pour les applis B2C américaines. Leurs barèmes ne
  remplacent ni les seuils ni la grille ci-dessus.
