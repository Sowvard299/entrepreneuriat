# Relancer la recherche d'idée dans une nouvelle conversation

Ce guide explique, étape par étape, comment refaire tout le processus (scan du web → problèmes → idées → tournoi → validation → kit terrain) dans une nouvelle conversation Claude Code. Il intègre les leçons de la première itération (dossiers `ideas/_recherche/` et `ideas/recrutement-garages/`, octobre 2026).

La nouvelle version change d'angle : **pas besoin d'innover. On cherche ce qui existe déjà et se vend, puis une façon de le faire mieux** (meilleur service, meilleur marketing, cible négligée, meilleur prix, zone mal servie).

---

## Étape 0 : préparer le terrain (15 minutes, avant d'ouvrir la conversation)

### 0.1 Compléter `CLAUDE.md`

C'est le plus gros manque de la première itération : Claude a dû deviner votre localisation (hypothèse « Île-de-France, Seine-et-Marne ») et ne connaissait ni votre réseau ni vos compétences. Remplissez au minimum les lignes `_TODO_` de la section *Founder profile* :

| Ligne | Exemple de ce qu'il faut écrire |
|-------|---------------------------------|
| Geography / language of first market | « Lyon et le Rhône (69) ; on peut se déplacer dans un rayon de 50 km » |
| Team | une ligne par personne : « Léa : vente B2B, alternance chez X » ; « Tom : vidéo et réseaux sociaux » ; etc. |
| People I can easily reach | « parents artisans (2), oncle garagiste, 3 contacts en restauration, réseau de l'école » |
| Budget / runway | « 3 000 € au total, pas de salaire avant juin 2027 » |
| Ambition | « entreprise de services rentable vite, pas de levée de fonds au départ » |
| Things I do NOT want to do | « pas de stock, pas de santé, pas de porte-à-porte chez les particuliers » |
| Problems personally seen | ce que chacun a vu en stage ou en alternance |

Plus ce fichier est précis, plus le segment de départ et les entretiens seront concrets.

### 0.2 Choisir entre deux options

- **Option A, vraiment de zéro** : la nouvelle conversation ignore la première itération. Plus long, mais sans biais.
- **Option B, de zéro sur l'idée, pas sur les données** : la nouvelle conversation réutilise les 180 signaux déjà collectés et ne cherche que ce qui manque pour la nouvelle approche. Deux fois plus rapide. **Recommandé.**

### 0.3 Récupérer le bon état du dépôt

La première itération est sur la branche `claude/recherche-idee-v1`. Deux possibilités :
- fusionner cette branche dans `main` sur GitHub (pull request), puis partir de `main` ;
- ou ouvrir la nouvelle conversation directement sur la branche `claude/recherche-idee-v1`.

Dans les deux cas, la nouvelle itération écrit dans **`ideas/_recherche-v2/`** : rien de la première n'est écrasé.

---

## Étape 1 : ouvrir la conversation

1. Ouvrir l'application Claude, onglet **Code**, puis **nouvelle session**.
2. Choisir le dossier du projet : `Documents\CLAUDE\Entrepreunariat`.
3. Choisir la branche (`main` après fusion, ou `claude/recherche-idee-v1`).
4. Mode de permissions **auto** (sinon Claude demandera une autorisation à chaque recherche web) ; effort de réflexion élevé ; le modèle le plus capable disponible.

## Étape 2 : coller le prompt maître

Copier tout le bloc de la section « Le prompt maître » ci-dessous, supprimer la ligne de l'option non choisie (A ou B), puis envoyer.

## Étape 3 : laisser tourner, et savoir quoi faire en cas de coupure

- Le prompt interdit à Claude de vous poser des questions : vous n'avez rien à répondre.
- **Si un message « You've hit your session limit · resets HH:MM » apparaît**, c'est normal (c'est arrivé deux fois en première itération). Rien n'est perdu, car chaque chercheur écrit au fil de l'eau dans ses fichiers. Après l'heure indiquée, écrire dans la même conversation :
  > « Reprends là où tu t'es arrêté : relis les fichiers déjà écrits dans ideas/_recherche-v2/, relance les sous-agents interrompus avec la consigne de continuer sans doublon, puis continue la mission. »
- Si le dossier du projet change de place entre deux sessions, le préciser dans ce même message (les sous-agents gardent l'ancien chemin en mémoire).
- Compter **2 à 3 sessions** au total, sur une demi-journée à une journée.

## Étape 4 : vérifier le livrable

Le résumé final tient en 40 lignes dans la conversation. Avant de le croire, vérifier :

- [ ] `ideas/_recherche-v2/signaux.md` annonce au moins 80 sources distinctes, et chaque famille a son fichier ;
- [ ] chaque problème retenu dans `problemes.md` a au moins 3 sites différents ;
- [ ] `idees-classees.md` contient le tableau trié **et** la liste des idées éliminées avec leur motif ;
- [ ] les audits de la phase 4 nomment des concurrents réels avec prix et avis clients ;
- [ ] le dossier de l'idée gagnante contient le dimensionnement du marché, le segment de départ, les hypothèses, le Lean Canvas, le pré-mortem et le kit terrain ;
- [ ] les liens du résumé final s'ouvrent.

## Étape 5 : sauvegarder

Le prompt demande à Claude de créer une branche, de commiter et de pousser à la fin. S'il ne l'a pas fait, écrire : « Commit et push tout ça sur une nouvelle branche. »

---

## Le prompt maître

```text
# Mission
Trouve-nous UNE entreprise à lancer en reprenant un modèle qui existe déjà et qui se vend, et en le faisant mieux (meilleur service, meilleur marketing, cible négligée, meilleur prix ou zone mal servie). L'innovation n'est pas requise : la preuve que des clients paient déjà passe avant l'originalité. Nous sommes 6 étudiants en master marketing. Tous secteurs confondus.

Tu travailles en autonomie complète : ne nous pose AUCUNE question avant le livrable final. Si une info manque, prends une hypothèse raisonnable, note-la dans ideas/_recherche-v2/hypotheses.md et continue.

Contexte : lis d'abord CLAUDE.md (profil de l'équipe, localisation, réseau, budget). Ses informations priment sur les hypothèses par défaut ci-dessous.
[OPTION A] Ne lis pas ideas/_recherche/ ni ideas/recrutement-garages/ (première itération) : on repart de zéro.
[OPTION B] Lis d'abord ideas/_recherche/ (première itération). Réutilise ses signaux et ses données publiques, ne refais pas ce qui y est déjà prouvé, et concentre la collecte sur la nouvelle approche « existant à améliorer ». L'idée finale peut être différente de la première itération.

Hypothèses par défaut :
- équipe : 6 profils marketing (vente, contenu, acquisition, études de marché), aucun développeur, no-code possible ;
- temps : temps partiel cette année, temps plein possible après le diplôme ;
- budget de départ : moins de 5 000 € au total ;
- premier marché : la ville ou le département de l'équipe indiqué dans CLAUDE.md, sinon la France ;
- ambition : une entreprise rentable vite, autofinancée ; une levée de fonds reste possible plus tard.

Hors périmètre : site web, code, logo, identité de marque, prévisionnel financier détaillé. N'utilise pas les skills de création de site.

# Règles de preuve (non négociables)
- Chaque modèle ou problème retenu s'appuie sur au moins 3 sources indépendantes (sites différents), datées, idéalement de moins de 24 mois.
- Pour chaque preuve, note : URL, date, citation courte (15 mots maximum), type de signal (argent déjà dépensé, recherche active d'une solution, plainte, obligation réglementaire, tendance).
- Ordre de force des signaux : argent déjà dépensé > recherche active d'une solution > plainte > tendance.
- Un modèle « qui marche » se prouve par des clients payants identifiables : chiffre d'affaires publié, nombre de clients, avis clients nombreux et récents, réseau qui ouvre des unités. Une levée de fonds seule ne prouve rien.
- Aucun chiffre inventé. Toute donnée sans source est marquée [HYPOTHÈSE].
- Si une source contredit une idée, garde-la et dis-le.
- Interdit : les idées génériques sans cible précise, sans prix et sans canal d'acquisition concret.

# Règles de fonctionnement (leçons de la première itération)
- Sous-agents : au plus 6 en même temps. Le quota de recherches web est partagé : chacun se limite à environ 25 recherches et privilégie l'ouverture directe des pages utiles. Chacun écrit dans son propre fichier, par lots de 5 signaux, pour que le travail survive à une coupure.
- Si une limite de session coupe des sous-agents, relis leurs fichiers et relance-les avec la consigne de continuer sans doublon.
- Reddit, LinkedIn, Malt et Indeed bloquent souvent la lecture automatique : utilise le navigateur intégré pour ces sites. Signale toute source qui n'a pas pu être lue.
- Pour compter les entreprises d'un secteur par taille et par département, utilise l'API Recherche d'entreprises (recherche-entreprises.api.gouv.fr) : filtres activite_principale (code NAF), departement, tranche_effectif_salarie.
- Vérifie le cadre juridique de chaque idée (agrément, carte professionnelle, démarchage interdit, monopole d'une profession) dès la phase 3, pas à la fin.

# Méthode

## Phase 1 : trouver ce qui se vend déjà (6 sous-agents en parallèle)
Un sous-agent par famille ; chacun rapporte 15 à 30 signaux au format ci-dessus.
1. Clients qui paient mais sont mécontents : acteurs établis avec beaucoup d'avis (Trustpilot, Google, App Store, Play Store, Custplace, forum Que Choisir) et une part importante d'avis 1-2 étoiles récents. Pour chacun : prix, nombre d'avis, les 3 reproches les plus fréquents avec citations datées.
2. Services locaux éparpillés sans marque : métiers à demande forte et récurrente où l'offre est faite de petits indépendants mal notés, difficiles à joindre ou sans site (Google Maps, PagesJaunes, annuaires professionnels), et plateformes qui prennent une grosse commission.
3. Modèles qui marchent ailleurs : autres pays (États-Unis, Royaume-Uni, Allemagne, Pays-Bas, pays nordiques) et autres villes françaises, avec preuve de clients payants, mais absents ou faibles dans notre zone. Cherche activement l'équivalent local.
4. Franchises et réseaux en croissance, petites entreprises à vendre : réseaux qui ouvrent beaucoup d'unités (Toute la franchise, Observatoire de la franchise : droit d'entrée, CA moyen par unité) ; annonces de cession de petites activités (fonds de commerce, clientèles, sites e-commerce) avec CA public. But : comprendre ce qui se vend et ce qui rapporte, pas acheter une franchise.
5. Argent qui circule et cimetière : missions récurrentes sur Codeur, ComeUp, Malt (avec le nombre de ventes, pas seulement l'offre), revenus publiés (Indie Hackers, TrustMRR, Starter Story) ; copies d'un modèle qui marche qui ont échoué, et pourquoi.
6. Données publiques et timing : INSEE, Sirene, enquête BMO de France Travail, fédérations professionnelles, obligations réglementaires datées 2025-2028 (vérifie la date et le périmètre de chacune).
Couvre au moins 8 secteurs, en B2C comme en B2B, avec des produits physiques, des services et des logiciels. Vise au moins 80 sources distinctes au total. Enregistre tout au fil de l'eau dans ideas/_recherche-v2/signaux/ (un fichier par famille) avec un index ideas/_recherche-v2/signaux.md.

## Phase 2 : des signaux aux « modèles à améliorer »
Regroupe les signaux par modèle existant : qui vend quoi, à qui, à quel prix, et ce qui ne va pas. Classe les 20 premiers selon la preuve que l'argent circule, le nombre de sources indépendantes, la faiblesse prouvée des acteurs en place et la récence. Avec le skill jobs-to-be-done, formule pour chacun le job du client (fonctionnel, émotionnel, social), ce qu'il « embauche » aujourd'hui et le reproche principal fait à cette solution.
Livrable : ideas/_recherche-v2/problemes.md

## Phase 3 : idées « la même chose, en mieux »
Pour les 10 modèles les mieux prouvés, suis la méthode du skill ai-startup-opportunity-generator (travail réel → douleur → qui paie → solution → concurrents → échecs passés → MVP), sans l'étape 9 (stack Laravel). Propose 1 à 3 façons de faire mieux que l'existant (15 à 25 idées au total), en précisant sur quel point exact on bat l'acteur en place (service, délai, prix, cible négligée, marketing, zone géographique), à quel prix, par quel canal, et le MVP. Tout est permis : service, produit physique, abonnement, marketplace, prestation outillée, distribution.

Filtres éliminatoires (une ligne d'explication par idée éliminée, élimination définitive) :
- plus de 20 000 € nécessaires avant le premier euro de chiffre d'affaires (droit d'entrée de franchise compris) ;
- diplôme, agrément ou licence obligatoire qu'on n'a pas ;
- impossible à tester sans développement lourd ;
- leader déjà bien financé, sans angle d'attaque crédible ;
- impossible de joindre 10 clients potentiels en une semaine ;
- premier euro impossible en moins de 3 mois (décision collective, assemblée générale, saisonnalité, démarchage interdit).

Grille de score sur 10, pondérée :
- argent déjà dépensé sur ce modèle : 25 % ;
- faiblesse prouvée des acteurs en place (avis clients, prix, délais) : 15 % ;
- douleur prouvée par le web : 15 % ;
- avantage d'une équipe marketing (acquisition, contenu, vente) : 15 % ;
- vitesse jusqu'au premier client payant (nombre de personnes qui doivent dire oui × fréquence de l'occasion d'acheter) : 15 % ;
- testable en moins de 4 semaines, pour moins de 500 €, sans coder : 10 % ;
- taille du marché : 5 %.
Livrable : ideas/_recherche-v2/idees-classees.md (tableau trié, plus la liste des idées éliminées avec leur motif).

## Phase 4 : tournoi
- Pour les 8 meilleures idées : audit concurrentiel réel (noms, prix publics, levées de fonds, avis clients, faiblesses citées par leurs propres clients), prédécesseurs qui ont échoué, cadre juridique. Recalcule les scores après audit et explique chaque correction.
- Pour les 3 meilleures après audit : lance llm-council avec cette question : « Laquelle de ces idées une équipe de 6 étudiants en marketing a-t-elle le plus de chances de transformer en premiers clients payants en 3 mois ? » Demande aux relecteurs de vérifier l'économie unitaire de chaque idée (revenu par heure de travail).
- Choisis UNE gagnante et explique pourquoi les deux autres perdent.

## Phase 5 : valider la gagnante sur le papier
Dans ideas/<nom-de-l-idee>/ :
1. startup-design en Fast Track. Saute les questions d'intake (sers-toi de ce prompt et de CLAUDE.md), ainsi que les phases Brand et Product. Ne bloque pas sur la phase Customer Discovery : note-la « à faire sur le terrain » et continue.
2. market-sizing : TAM/SAM/SOM pour notre zone puis pour la France. Fais d'abord le calcul bottom-up (nombre de clients × prix), puis le top-down pour le recouper.
3. beachhead-segment : un premier segment ultra précis (qui, où, combien, comment les trouver).
4. identify-assumptions-new : hypothèses classées par impact × incertitude.
5. lean-canvas.
6. Économie unitaire : revenu moyen par vente, heures de travail par vente, revenu par heure, et le seuil en dessous duquel on arrête.
7. Pré-mortem : « On est dans 2 ans et c'est un échec. Pourquoi ? » Donne 5 causes probables et la parade à chacune.

## Phase 6 : kit terrain
Avec le skill mom-test, prépare :
- un guide d'entretien de 10 questions maximum, qui teste les 3 hypothèses les plus dangereuses ;
- les endroits précis où trouver 30 interlocuteurs (groupes, forums, annuaires, événements repérés pendant le scan, avec les liens vérifiés) et un message d'approche prêt à envoyer ;
- la répartition entre nous 6 (5 entretiens chacun), en tenant compte des compétences indiquées dans CLAUDE.md ;
- un modèle de compte rendu d'entretien ;
- 3 expériences de validation à moins de 500 € (préventes, MVP « concierge » où l'on rend le service à la main, fausse porte avec un formulaire, post ciblé…). Décris-les sans les construire, et fixe pour chacune un seuil de réussite chiffré à l'avance ;
- un critère clair GO / PIVOT / STOP à appliquer dans 4 semaines, avec la date.

# Livrable final
Dans le chat, en 40 lignes maximum :
- l'idée en 3 phrases (qui, quel modèle existant on améliore, sur quel point, quelle offre, quel prix) ;
- les 5 preuves les plus fortes, avec leur lien ;
- la taille du marché (SOM bottom-up) et le premier segment ;
- les 3 risques qui peuvent tuer le projet ;
- les 2 idées de réserve, une ligne chacune ;
- les 3 actions à faire la semaine prochaine.
Le détail va dans les fichiers. Sois franc : si aucune idée ne passe la barre, dis-le, et présente la meilleure piste en précisant ce qui lui manque.
Termine en créant une nouvelle branche, en commitant et en poussant ideas/_recherche-v2/ et le dossier de l'idée gagnante.

Commence maintenant par la phase 1.
```

---

## Ce qui a changé par rapport à la première itération, et pourquoi

| Constat de la première itération | Changement dans le prompt |
|----------------------------------|---------------------------|
| L'équipe veut un modèle éprouvé, pas forcément une innovation | Phase 1 orientée « ce qui se vend déjà » : clients mécontents, services locaux sans marque, modèles d'ailleurs, franchises, cessions |
| Claude a dû deviner la localisation et ignorait le réseau de l'équipe | Lecture obligatoire de `CLAUDE.md`, qui prime sur les hypothèses par défaut (étape 0.1) |
| 8 sous-agents en parallèle ont épuisé le quota de recherches et la limite de session (deux coupures) | 6 sous-agents au plus, environ 25 recherches chacun, écriture par lots, consigne de reprise |
| Reddit et LinkedIn n'ont presque pas pu être lus | Navigateur intégré pour les sites qui bloquent la lecture automatique |
| Les audits ont fait perdre 0,5 à 1,5 point à chaque idée, et le conseil a inversé le classement des scores | Audit des 8 meilleures au lieu de 5 ; nouveau critère « vitesse jusqu'au premier client payant » (15 %) |
| Une idée (compagnie de seniors) n'a été éliminée qu'en fin de phase 3 pour une question d'agrément | Vérification juridique dès la phase 3 ; nouveau filtre « premier euro impossible en moins de 3 mois » |
| L'économie unitaire n'est apparue qu'à la relecture du conseil | Étape « économie unitaire » obligatoire en phase 5, et vérification demandée aux relecteurs du conseil |
| Les résultats risquaient d'écraser la première itération | Tout s'écrit dans `ideas/_recherche-v2/` |
