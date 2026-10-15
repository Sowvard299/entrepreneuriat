# Relancer la recherche d'idée, version 3 : du marché au segment

Cette version change l'ordre de la recherche. La v2 partait des plaintes clients, puis cherchait une idée,
puis mesurait le marché. Elle produisait des idées génériques et des marchés trop petits. La v3 fait
l'inverse : **marché qui grossit → segment précis → angle « pareil mais mieux » → preuve que l'argent circule.**

Les seuils (taille, croissance, SOM, budget) et la grille de score sont dans `CLAUDE.md`, section
« Critères de viabilité ». Ils s'y modifient en une ligne ; ce guide n'a rien à changer.

Le travail de collecte est confié à trois sous-agents définis dans `.claude/agents/` : `chercheur`,
`auditeur` et `verificateur` (voir `CLAUDE.md`, section « Sous-agents et coordination »).

---

## Ce qui n'allait pas dans la v2

| Constat | Effet | Correction en v3 |
|---------|-------|------------------|
| Taille du marché = 5 % du score | les micro-niches gagnent | taille et croissance = 25 % |
| Filtres « premier euro en 3 mois » et « moins de 20 000 € » | tout le B2B à cycle long est éliminé | premier client payant (pilote ou précommande) en 3 mois, contrat récurrent en 6 mois ; deux pistes (rapide / ambitieuse) |
| Départ par les avis négatifs | tout le monde trouve les mêmes plaintes, d'où des idées bateau (ménage, dépannage, garde d'enfants, marketing pour artisans) | départ par les marchés qui grossissent, avec moteur daté ; piège « agence locale de plus » écrit dans le skill |
| `market-sizing` et `beachhead-segment` en phase 5 | la taille est mesurée après le choix | segmentation et calcul de potentiel avant les idées |
| Aucune mesure de croissance | un marché stable ou en baisse passe | croissance sourcée (2 sources dont 1 institutionnelle) + contre-preuve obligatoire |
| Autonomie totale, aucune question | un mauvais départ se propage jusqu'au bout | 2 points d'arrêt (après les marchés, après les idées) |
| Conseil qui répond « premiers clients en 3 mois » | on optimise la vitesse, pas la taille | deux questions : clients en 3 mois, et vivre de l'entreprise à 3 ans |
| `brainstorm-ideas-new` cité pour trouver des idées | il génère des fonctionnalités de produit, pas des entreprises | déplacé après le choix, pour le MVP |
| Sous-agents génériques sur le modèle le plus cher, 6 en parallèle | limite de session atteinte : les 4 auditeurs de la phase 4 coupés d'un coup | agents dédiés en `sonnet` (vérificateur en `haiku`), vagues de 4, conseil en `sonnet` |
| Le coordinateur relisait les 6 fichiers de signaux en entier (~150 000 tokens) | contexte saturé, session épuisée plus vite | chaque agent écrit un fichier de synthèse de 40 lignes ; le coordinateur ne lit que ces synthèses |
| 25 signaux sur 28 d'une famille venaient de Trustpilot | preuves peu diverses | quota : un site ≤ 40 % des preuves d'un fichier, une source officielle par marché |
| Reddit illisible même avec le navigateur intégré ; Pappers, Malt, DGCCRF bloqués | recherches gaspillées | liste des sources bloquées et des recettes qui marchent dans `.claude/agents/chercheur.md` |
| Règles juridiques laissées en [HYPOTHÈSE] jusqu'au classement | idées classées sur un droit non vérifié | l'auditeur cite l'article (Légifrance, service-public) pour chaque finaliste |
| Aucune vérification des citations et des chiffres | impossible de savoir si une preuve est exacte | agent `verificateur` après chaque vague, et sur toutes les preuves de la gagnante |
| Section 0.2 : l'option B était absente | on ne pouvait pas choisir | corrigé ci-dessous |

---

## Étape 0 : préparer le terrain (30 minutes)

### 0.1 Remplir `CLAUDE.md`

Complétez les lignes marquées ☐ de `CLAUDE.md` :
- le tableau de l'équipe (prénom, compétence, heures par semaine, contacts) ;
- 3 à 5 contacts ou communautés nommés à la place de « tout le monde » ;
- 2 ou 3 situations concrètes vues chez EDF (quel client, quelle offre, quel blocage) ;
- l'ambition chiffrée (revenu visé, nombre de personnes à rémunérer) ;
- ce qui ferait arrêter l'un de vous (par exemple : être employeur de 20 intervenants à domicile).

Sans ces informations, Claude choisit des segments au hasard. C'est le levier le plus fort sur la
qualité du résultat, devant tout réglage du prompt.

### 0.2 Choisir entre deux options

- **Option A, de zéro** : la conversation ignore `ideas/_recherche/`, `ideas/_recherche-v2/` et
  `ideas/recrutement-garages/`. Sans biais.
- **Option B, en réutilisant les itérations précédentes** : Claude relit `ideas/_recherche-v2/BILAN.md`
  et peut réutiliser les données publiques déjà collectées (comptages Sirene, CA vérifiés, obligations
  datées) de `ideas/_recherche-v2/signaux/` et `ideas/_recherche/`, sans refaire ce qui est prouvé.
  L'idée finale peut être différente.

Supprimez la ligne de l'option non choisie dans le prompt.

### 0.3 Outils

Rien à installer : le skill `market-segment-scanner` et les trois agents sont déjà dans le dépôt
(`.claude/skills/` et `.claude/agents/`). L'API `recherche-entreprises.api.gouv.fr` ne demande aucune clé.

Optionnel, à n'installer qu'après avoir lu le README ou le `SKILL.md` (un skill ou un serveur MCP peut
lancer des commandes sur votre machine). Les noms de paquets ci-dessous n'ont pas été vérifiés :
vérifiez-les sur npm ou GitHub avant toute commande.
- Tendances de recherche (mesurer la croissance de la demande) : un serveur MCP Google Trends.
- Skill d'étude de marché `market-research` du dépôt `affaan-m/everything-claude-code` (dépôt très gros :
  n'installez que ce skill).
- Recherche approfondie `assafelovic/gpt-researcher` (clés API, coût par recherche).

### 0.4 Récupérer le bon état du dépôt

Partez de la branche qui contient ce fichier et le dossier `.claude/agents/`. La v3 écrit dans
**`ideas/_recherche-v3/`** : rien de ce qui existe n'est écrasé.

---

## Étape 1 : ouvrir la conversation

1. Application Claude, onglet **Code**, nouvelle session.
2. Dossier du projet : `Documents\CLAUDE\Entrepreunariat`.
3. Branche : celle qui contient `.claude/agents/`.
4. Permissions en **auto**, effort de réflexion élevé, modèle le plus capable (il ne sert qu'à la
   coordination ; les agents tournent sur des modèles plus légers).
5. Démarrez la session juste après une remise à zéro de votre limite d'usage si possible : un run
   complet en consomme plusieurs.

## Étape 2 : coller le prompt maître

Copiez le bloc « Le prompt maître v3 » en bas de ce fichier, supprimez la ligne de l'option non choisie,
envoyez. Pour un run sans surveillance, ajoutez le mot **AUTO** à la fin : Claude ne s'arrêtera alors
à aucun point d'arrêt (déconseillé pour le premier essai).

## Étape 3 : points d'arrêt et reprise

- **Point d'arrêt 1**, après la cartographie : Claude affiche 8 marchés avec taille, croissance, confiance,
  modèle d'exécution et contre-preuve. Choisissez 3 à 5 marchés (par exemple : « garde 2, 5 et 7, ajoute le
  marché de ... »). Vous pouvez aussi écrire « go ».
- **Point d'arrêt 2**, après le classement des idées : Claude affiche le Top 8 avec le tableau des seuils.
  Écrivez « go » pour lancer le tournoi, ou demandez de corriger (« élimine 3, ajoute le segment ... »).
- Si le message « You've hit your session limit · resets HH:MM » apparaît, rien n'est perdu : tout est écrit
  dans `etat.md` et les fichiers. Après l'heure indiquée, écrivez dans la même conversation :
  > « Reprends là où tu t'es arrêté : lis ideas/_recherche-v3/etat.md et les fichiers de synthèse déjà
  > écrits, relance seulement les agents marqués partiel ou coupé (même agent, même fichier, consigne de
  > relire le fichier et de continuer sans doublon), puis continue. »
- Si le dossier du projet change de place entre deux sessions, précisez le nouveau chemin dans ce message.
- Comptez 3 à 4 sessions sur une journée.

## Étape 4 : vérifier le livrable

- [ ] `marches.md` contient au moins 30 marchés évalués, chaque marché gardé a une contre-preuve, un niveau
      de confiance et un modèle d'exécution, et la liste des marchés éliminés indique le motif ;
- [ ] chaque chiffre de croissance cite 2 sources dont 1 institutionnelle, ou est marqué [HYPOTHÈSE] ;
- [ ] `segments.md` a 10 à 15 segments par marché retenu, chacun défini par au moins 3 axes, avec le calcul de
      potentiel visible et un chemin d'expansion pour les finalistes ;
- [ ] `signaux.md` annonce au moins 80 sources distinctes, aucun site au-dessus de 40 % des preuves d'un
      fichier, et chaque segment du Top 12 a ses 6 types de signaux ;
- [ ] `verification.md` existe : taux de ✔ par fichier, et 100 % des preuves de la gagnante contrôlées ;
- [ ] `idees-classees.md` contient le tableau trié, la liste des idées éliminées avec leur motif, et une
      idée de réserve par piste ;
- [ ] les audits de la phase 3 nomment de vrais concurrents avec prix et avis, et citent les articles de loi ;
- [ ] le dossier de l'idée gagnante contient dimensionnement bottom-up et top-down, segment de départ, chemin
      d'expansion, hypothèses, Lean Canvas, économie unitaire, pré-mortem et kit terrain ;
- [ ] le résumé final contient le tableau « seuils de CLAUDE.md : réussi / raté » et ses liens s'ouvrent.

## Étape 5 : si aucune idée ne passe les seuils

C'est un résultat valable. Ne baissez pas tous les seuils d'un coup. Dans l'ordre :
1. relancez les phases 0 à 2 avec d'autres marchés (demandez à Claude de ne pas reprendre ceux déjà vus) ;
2. relâchez **un seul** seuil dans `CLAUDE.md` (par exemple SOM 500 k€ → 300 k€, ou croissance 8 % → 5 %)
   et notez la raison à côté ;
3. relancez à partir de la phase 2, pas depuis le début.

## Étape 6 : sauvegarder

Le prompt demande une nouvelle branche, un commit et un push. Sinon, écrivez :
« Commit et push tout ça sur une nouvelle branche. »

---

## Le prompt maître v3

```text
# Mission
Trouve-nous UNE entreprise à lancer en suivant cet ordre : un MARCHÉ qui grossit, puis un SEGMENT précis
de ce marché, puis un modèle existant qui se vend déjà, que nous ferons mieux (meilleur service, meilleur
prix, cible négligée, meilleur marketing, zone mal servie). L'innovation n'est pas requise. La preuve que
des clients paient déjà passe avant l'originalité, et un marché trop petit pour faire vivre l'équipe est
éliminé quelle que soit la qualité de l'idée. Nous sommes 6 étudiants en master marketing. Tous secteurs.

Contexte : lis d'abord CLAUDE.md (profil, équipe, réseau, budget, ambition, « Critères de viabilité »,
grille de score, « Sous-agents et coordination »). Ses informations priment sur les hypothèses par
défaut ci-dessous.
[OPTION A] Ne lis pas ideas/_recherche/, ideas/_recherche-v2/ ni ideas/recrutement-garages/ : on repart de zéro.
[OPTION B] Lis d'abord ideas/_recherche-v2/BILAN.md. Réutilise les données publiques déjà collectées dans
ideas/_recherche-v2/signaux/ et ideas/_recherche/ (comptages Sirene, CA vérifiés, obligations datées) sans
refaire ce qui y est prouvé. L'idée finale peut être différente.

Fonctionnement : tu travailles en autonomie, SAUF aux deux points d'arrêt ci-dessous où tu t'arrêtes
et attends ma réponse. Si j'ai écrit AUTO à la fin de ce message, ne t'arrête à aucun point d'arrêt.
Hors points d'arrêt, ne me pose pas de question : si une information manque, prends une hypothèse
raisonnable, note-la dans ideas/_recherche-v3/hypotheses.md et continue. Tiens à jour
ideas/_recherche-v3/etat.md (une ligne par phase, ✔ et date quand elle est finie, et une ligne par
sous-agent : mission, fichier, statut fini / partiel / coupé) pour qu'on puisse reprendre après une coupure.

Hypothèses par défaut (si CLAUDE.md est muet) :
- équipe : 6 profils marketing (vente, contenu, acquisition, études), aucun développeur, no-code possible ;
- temps : partiel cette année, plein temps possible après le diplôme ;
- budget : moins de 5 000 € autofinancés ; pré-amorçage possible pour une piste ambitieuse ;
- premier marché : la zone indiquée dans CLAUDE.md, sinon la France.

Hors périmètre : site web, code, logo, identité de marque, prévisionnel financier détaillé.

# Règles de preuve (non négociables)
- Chaque marché ou modèle retenu s'appuie sur au moins 3 sources indépendantes et datées, idéalement de
  moins de 24 mois. Pour chaque preuve : URL, date, citation de 15 mots maximum, type de signal.
- Un même site ne fournit pas plus de 40 % des preuves d'un fichier.
- Un chiffre de croissance cite 2 sources dont 1 institutionnelle (INSEE, Eurostat, ministère, fédération,
  Banque de France, Bpifrance). Précise valeur ou volume, France ou monde, période.
- Ordre de force : argent déjà dépensé > recherche active d'une solution > plainte > tendance.
- Un modèle « qui marche » se prouve par des clients payants identifiables (CA publié, nombre de clients,
  avis nombreux et récents, réseau qui ouvre des unités). Une levée de fonds seule ne prouve rien.
- Chaque marché et chaque idée finaliste a une contre-preuve. Garde toute source qui contredit une idée.
- Aucun chiffre inventé : toute donnée sans source est marquée [HYPOTHÈSE].
- Interdit : les idées sans segment précis, sans prix et sans canal d'acquisition concret.

# Règles de fonctionnement
- Toute collecte passe par les sous-agents de .claude/agents/ (outil Agent, subagent_type) :
  « chercheur » pour la collecte, « auditeur » pour le tournoi, « verificateur » pour le contrôle.
  N'utilise pas d'agent générique pour ces tâches.
- Vagues de 4 agents au plus. Donne à chacun : sa mission, la liste précise de ce qu'il couvre, le
  chemin de son fichier de travail ET de son fichier de synthèse (même nom suffixé -synthese.md).
- Tu ne lis QUE les fichiers de synthèse. Tu n'ouvres un fichier de travail que pour une preuve précise
  (Grep sur son ID).
- Après chaque vague : mets à jour etat.md, puis lance un « verificateur » sur 10 preuves par fichier
  (rapport dans ideas/_recherche-v3/verification.md). Au-delà de 20 % de ✘ ou ≈ sur des chiffres
  utilisés, relance le chercheur concerné ou déclasse ses preuves.
- Si une limite de session coupe des agents, relance seulement ceux marqués partiel ou coupé, avec la
  consigne de relire leur fichier et de continuer sans doublon.
- Les sources bloquées connues (Reddit, Pappers, Malt, DGCCRF…) et les API qui marchent sont listées dans
  .claude/agents/chercheur.md : ne perds pas de recherches dessus.
- Vérifie le cadre juridique de chaque idée dès la phase 2 (agrément, carte professionnelle, démarchage
  interdit, monopole d'une profession). Pour les finalistes, l'article de loi est cité.

# Méthode

## Phase 0 : cartographier les marchés en croissance
Utilise le skill market-segment-scanner, étapes 1 à 3, avec 4 « chercheur » (2 lentilles chacun,
8 à 10 marchés, 3 recherches par marché au plus). Longue liste de 30 à 40 marchés par lentilles
(obligation datée, transition, fragmentation, modèle venu d'ailleurs, demande en hausse, franchises et
cessions, dépense mal servie), au moins 10 secteurs, B2B et B2C, services, produits et logiciels.
Fiche par marché (avec le modèle d'exécution : logiciel, service outillé, service à forte main-d'œuvre,
produit), filtre selon les seuils de CLAUDE.md, top 8, puis « verificateur » sur les chiffres de taille
et de croissance des 8.
Livrable : ideas/_recherche-v3/marches.md (tableau classé, fiches, marchés éliminés avec motif).
>>> POINT D'ARRÊT 1 : affiche les 8 marchés (taille, croissance, confiance, modèle d'exécution,
contre-preuve en une ligne) et demande-moi d'en choisir 3 à 5. Attends.

## Phase 1 : segmenter et prouver que l'argent circule
1. Segmentation (market-segment-scanner, étape 4) des marchés choisis : 10 à 15 segments chacun, définis
   par au moins 3 axes, scorés, avec chemin d'expansion pour les finalistes. Garde le Top 12 global.
2. Pour les 12 segments, des « chercheur » (2 segments chacun, en vagues de 4) cherchent ces signaux :
   a) argent déjà dépensé : prix publics des offres existantes, CA publiés (API Recherche d'entreprises,
      TrustMRR), annonces de cession, unités de franchise ;
   b) faiblesse des acteurs en place : avis (Trustpilot, Custplace, forums Que Choisir), prix, délais,
      avec citations datées ;
   c) recherche active : tendances de recherche, questions en forum, missions Codeur, ComeUp ;
   d) équivalent à l'étranger ou dans une autre ville française, et copies qui ont échoué (pourquoi) ;
   e) données publiques : nombre de cibles (Sirene, Urssaf), BMO France Travail, fédérations,
      obligations datées ;
   f) accès : où trouver les 10 premiers clients (groupes, annuaires, événements, liens vérifiés).
Vise au moins 80 sources distinctes. Écris dans ideas/_recherche-v3/signaux/ (un fichier de travail et
un fichier de synthèse par agent) avec un index signaux.md, et dans segments.md.

## Phase 2 : angles et idées « pareil mais mieux »
Pour les 12 segments : formule avec le skill jobs-to-be-done le besoin du client (fonctionnel,
émotionnel, social), ce qu'il « embauche » aujourd'hui et le reproche principal. Puis, avec la méthode
du skill ai-startup-opportunity-generator (sans son étape de stack technique), propose 1 à 2 angles par
segment (15 à 25 idées). Chaque idée précise : le segment, l'offre, le prix, le canal d'acquisition,
le point exact où on bat l'acteur en place, la preuve de sa faiblesse, pourquoi le leader ne répond pas
déjà, l'économie unitaire en une ligne (prix, heures par client et par mois, revenu par heure), le MVP,
et « besoin d'un associé tech » si c'est le cas.
Filtres éliminatoires : ceux de CLAUDE.md (une ligne de motif par idée éliminée, élimination définitive).
Score : la grille de CLAUDE.md. Classe aussi chaque idée dans la piste rapide ou la piste ambitieuse.
Livrable : ideas/_recherche-v3/idees-classees.md (tableau trié, idées éliminées avec motif, ligne
« seuils de CLAUDE.md » pour chacune).
>>> POINT D'ARRÊT 2 : affiche le Top 8 avec le tableau des seuils. Attends mon « go » ou mes corrections.

## Phase 3 : tournoi
- Pour les 8 meilleures : 4 « auditeur » (2 idées chacun, une seule vague) font l'audit concurrentiel
  réel (noms, prix publics, levées de fonds, avis clients, faiblesses citées par leurs propres clients),
  les prédécesseurs qui ont échoué, le cadre juridique avec articles, l'économie unitaire et le score
  recalculé. Puis un « verificateur » sur leurs chiffres décisifs. Explique chaque correction de score.
- Pour les 3 meilleures après audit : llm-council (conseillers et relecteurs en model sonnet, président
  sur le modèle principal) avec DEUX questions. (a) Laquelle donne le plus de chances de premiers clients
  payants en 3 mois ? (b) Laquelle peut faire vivre l'équipe à 3 ans, au vu du chemin d'expansion ?
  Demande aux relecteurs de vérifier l'économie unitaire (revenu par heure de travail, coût d'acquisition
  d'un client estimé) et de jouer l'avocat du diable (« pourquoi un leader écrase ça en 6 mois »).
  Sauve le verdict dans ideas/_recherche-v3/conseil.md.
- Choisis UNE gagnante, explique pourquoi les deux autres perdent, et désigne une réserve par piste.

## Phase 4 : valider la gagnante sur le papier
Dans ideas/<nom-de-l-idee>/ :
1. startup-design en Fast Track (saute l'intake, la phase Brand et la phase Product ; note la Customer
   Discovery « à faire sur le terrain »).
2. market-sizing : bottom-up d'abord (clients × prix), puis top-down pour recouper, en 3 scénarios
   (prudent, central, ambitieux), pour notre zone puis pour la France.
3. beachhead-segment : le premier segment (qui, où, combien, comment les trouver) et le chemin
   d'expansion chiffré : segment 1 → 2 → 3, avec le potentiel cumulé comparé au seuil de CLAUDE.md.
4. identify-assumptions-new : hypothèses classées par impact × incertitude.
5. lean-canvas.
6. Économie unitaire : revenu par vente, heures de travail par vente, revenu par heure, coût
   d'acquisition estimé, et le seuil en dessous duquel on arrête.
7. Pré-mortem : « dans 2 ans c'est un échec : pourquoi ? » 5 causes probables et une parade chacune.
8. brainstorm-ideas-new, uniquement pour définir le MVP de l'idée gagnante.
9. « verificateur » sur 100 % des preuves citées dans le dossier de la gagnante.

## Phase 5 : kit terrain
Avec le skill mom-test :
- guide d'entretien de 10 questions maximum qui teste les 3 hypothèses les plus dangereuses ;
- où trouver 30 interlocuteurs (liens vérifiés issus de la phase 1, point f) et un message d'approche ;
- répartition entre nous 6 (5 entretiens chacun) selon les compétences de CLAUDE.md ;
- modèle de compte rendu d'entretien ;
- 3 expériences de validation à moins de 500 € (précommande, MVP « concierge », fausse porte, post ciblé),
  décrites sans les construire, avec un seuil de réussite chiffré à l'avance ;
- critère GO / PIVOT / STOP à appliquer dans 4 semaines, avec la date.

# Livrable final
Dans le chat, en 40 lignes maximum :
- l'idée en 3 phrases (qui, quel modèle existant on améliore, sur quel point, quelle offre, quel prix) ;
- le marché (taille, croissance, sources), le segment de départ et le chemin d'expansion ;
- le tableau des seuils de CLAUDE.md : réussi / raté, avec le chiffre ;
- les 5 preuves les plus fortes, avec leur lien et leur verdict de vérification ;
- les 3 risques qui peuvent tuer le projet ;
- les 2 idées de réserve (une par piste), une ligne chacune ;
- les 3 actions de la semaine prochaine.
Le détail va dans les fichiers. Sois franc : si aucune idée ne passe les seuils, dis-le, présente la
meilleure piste et ce qui lui manque.
Termine en créant une nouvelle branche, en commitant et en poussant ideas/_recherche-v3/ et le dossier
de l'idée gagnante.

Commence maintenant par la phase 0.
```
