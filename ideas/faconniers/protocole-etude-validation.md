# Façonniers alimentaires : protocole de l'étude de validation (12/10/2026)

> **Où on en est :** en **validation de l'idée**. Rien n'est vendu tant que l'étude n'a pas tranché :
> pas de prévente, pas d'acompte, pas de statut juridique. L'étude a un seul but : permettre à la
> porteuse de décider le **samedi 31/10** s'il faut continuer, changer d'angle ou abandonner.
>
> Ce protocole remplace la partie « prévente » du plan de la
> [décision du 12/10](../03-decision-finale-2026-10-12.md). Les faits de départ sont dans
> [`veille-marche.md`](veille-marche.md) (mise à jour du 12/10) et
> [`intermediaires-gratuits.md`](intermediaires-gratuits.md).

## 1. Les 5 hypothèses à trancher

| # | Hypothèse | Si elle est fausse | Méthode principale |
|---|---|---|---|
| H1 | Pour une jeune marque, trouver un fabricant est long, risqué et coûteux | Il n'y a pas de problème à résoudre | Entretiens marques, questionnaire |
| H2 | Des façonniers acceptent la première production d'une jeune marque | Il n'y a rien à proposer aux marques | Entretiens façonniers, codes de traçabilité |
| H3 | Les solutions existantes (réseau, ARIA, CCI, incubateurs, consultants, Torg) ne suffisent pas | Le besoin est déjà couvert | Étude documentaire, entretiens structures, questionnaire |
| H4 | Le besoin revient assez souvent et le marché est assez grand pour faire vivre une entreprise | C'est au mieux une activité de conseil | Dimensionnement à partir de données publiques |
| H5 | Les marques dépensent déjà de l'argent pour ce problème | Doute sur leur capacité à payer | Entretiens marques, questionnaire |

H5 remplace la prévente : sans rien vendre, **ce que les marques ont déjà dépensé** est le seul
indicateur honnête de ce qu'elles pourraient payer.

## 2. Critères de décision, fixés avant la collecte

On les fixe maintenant pour ne pas les adapter aux résultats (leçon n°3 de la passation). Les seuils
sont des **propositions [Guessing]** : la porteuse les valide avant le premier entretien, puis on n'y
touche plus.

| Hypothèse | Validée si… |
|---|---|
| H1 | Au moins la moitié des marques interrogées en entretien (8 au minimum) **et** au moins 40 % des répondants au questionnaire ont vécu une « recherche pénible » (définition en 4.5) |
| H2 | Au moins 3 façonniers sur 8 ont accepté un « petit projet » au cours des 12 derniers mois |
| H3 | Moins de 2 structures sur 3 traitent déjà ces demandes d'une façon que les marques jugent satisfaisante |
| H4 | Le scénario central du dimensionnement atteint **500 recherches de fabricant par an** en France. Raisonnement : environ 150 projets par an à environ 1 000 € font 150 k€ de chiffre d'affaires ; en captant au plus 30 % du marché accessible, il en faut au moins 500. Seuil à ajuster selon l'ambition de l'équipe (toujours « TODO » dans `CLAUDE.md`) |
| H5 | Au moins 30 % des marques (entretiens et questionnaire) ont déjà dépensé de l'argent pour trouver ou tester un fabricant |

**La décision du 31/10 :**

| Résultat | Décision |
|---|---|
| H1, H2, H4 et H5 validées, et H3 ne bloque pas | **Continuer.** Étape suivante : un premier test payant, avec un statut juridique |
| H1 validée, mais H2 ou H3 tombe | **Changer d'angle :** préparer les projets des marques (si H2 tombe), ou un outil pour les structures (si H3 tombe) |
| Seule H5 tombe | **Changer de payeur :** étudier les façonniers comme clients |
| H1 ou H4 tombe | **Abandonner.** On repart de la grille « problèmes vus en alternance » |

## 3. Étude documentaire (du 13 au 18/10)

**Déjà fait :** concurrents et substituts, prix de référence, contexte du secteur
([`veille-marche.md`](veille-marche.md)).

**Reste à faire :**
1. **Le dimensionnement du marché** (section 5.1).
2. **La mesure par les codes de traçabilité** (pour H2). Tout produit préemballé identifie son
   emballeur, son fabricant ou son importateur, en clair ou par un code « EMB ».
   [Open Food Facts](https://world.openfoodfacts.org/packager-codes) recense plus de 40 000 de ces
   codes, avec les produits associés.
   - Relever les codes d'au moins 30 produits de jeunes marques (en rayon ou sur Open Food Facts).
   - Compter les sites qui emballent pour au moins 3 marques différentes. Chacun est un façonnier qui
     **accepte déjà** de petites marques, et un contact pour les entretiens.
   - Que la méthode marche est [Likely] : la vérifier sur les 10 premiers produits avant d'aller plus loin.
3. **La fiche concurrent de Torg** : ce que le service promet, à qui, à quel prix, d'après ses pages
   publiques. Ne pas créer de compte en se faisant passer pour un acheteur.

## 4. Étude qualitative (du 13 au 27/10)

### 4.1 Méthode
Entretiens individuels semi-directifs de 20 à 30 minutes, au téléphone ou en visio, si possible en
binôme (l'un pose les questions, l'autre note). On parle de **leur passé**, jamais de notre idée.

### 4.2 Échantillon

| Population | Nombre | Critères |
|---|---|---|
| Jeunes marques | 8 à 10 | Marque alimentaire lancée en 2021 ou après, qui fait fabriquer par un tiers ou qui a cherché un fabricant depuis moins de 24 mois. Au moins 3 catégories et 2 régions, dont 2 marques qui ont renoncé au façonnage ou produisent elles-mêmes (comme minimiil) |
| Façonniers | 6 à 8 | Entreprise qui fabrique pour d'autres marques. Mélanger TPE et PME, exposants et non-exposants de salons (ceux qui exposent ont déjà un canal pour trouver des clients) |
| Structures et experts | 3 à 4 | Club AgroAlia, une ARIA, une pépinière (Ma Première Usine), le CTCPA ou un incubateur ; si possible un consultant indépendant |

On s'arrête quand deux entretiens de suite n'apportent plus rien de nouveau (saturation), mais jamais
sous le minimum. Les premiers contacts, déjà sourcés, sont dans [`suivi-entretiens.csv`](suivi-entretiens.csv).

### 4.3 Recrutement

| Population | Où trouver les contacts |
|---|---|
| Jeunes marques | Pépinières et ateliers partagés (Ma Première Usine à Carpentras, ateliers listés dans [`veille-marche.md`](veille-marche.md)) ; projets alimentaires de financement participatif (Miimosa, Ulule, KissKissBankBank) ; incubateurs (club AgroAlia, Shakeup Factory, Vitagora, Valorial) ; épiceries fines ; LinkedIn |
| Façonniers | Sites repérés par les codes de traçabilité (section 3) ; liste des exposants du SIAL (mots-clés : façonnage, private label, MDD, co-manufacturing) ; [annuaire des entreprises](https://annuaire-entreprises.data.gouv.fr/) (codes d'activité 10 et 11, à trier à la main) ; annuaires des ARIA |
| Structures | Les 3 appels de [`intermediaires-gratuits.md`](intermediaires-gratuits.md) |

**Règles de contact :**
- Se présenter comme étudiante ou étudiant, et ne rien présenter de l'idée. Ne jamais dire « plateforme » ni « startup ».
- Écrire quand on veut, mais **appeler seulement hors du temps de travail en entreprise** (7 h 30 - 9 h, 12 h - 14 h, jours d'école).
- Une seule relance. Un « non » ou un silence après la relance clôt le contact (droit d'opposition).
- Les modèles ci-dessous sont au féminin : adaptez-les.

**Jeune marque, e-mail.** Objet : *Comment avez-vous trouvé votre fabricant ? (question d'étudiante, 20 min)*

> Bonjour [Prénom],
>
> J'ai découvert [Marque] [chez X / sur Miimosa / sur LinkedIn]. Je suis étudiante en master à
> [école] et, avec cinq camarades, j'étudie comment les jeunes marques alimentaires passent de leurs
> premiers lots à une production régulière.
>
> Je ne vends rien. Accepteriez-vous de me raconter en 20 minutes, au téléphone ou en visio, comment
> vous avez trouvé votre fabricant, ou pourquoi vous produisez vous-même ? Je m'adapte à vos horaires,
> y compris tôt le matin ou à l'heure du déjeuner.
>
> Si vous préférez ne pas être recontacté(e), un simple « non merci » suffit.
>
> [Prénom Nom], étudiante en master [intitulé], [école] · [téléphone]

**Jeune marque, LinkedIn** (note de 300 caractères au maximum) :

> Bonjour [Prénom], étudiante en master, j'étudie comment les jeunes marques alimentaires trouvent
> leur fabricant. Le parcours de [Marque] m'intéresse : auriez-vous 20 min pour me le raconter ? Je ne
> vends rien.

**Façonnier, e-mail.** Objet : *Votre dernier client à façon : 15 minutes avec une étudiante ?*

> Bonjour [Prénom],
>
> Je suis étudiante en master à [école]. Avec cinq camarades, j'étudie comment les fabricants
> agroalimentaires trouvent leurs clients en fabrication à façon, et ce qu'ils font des demandes des
> jeunes marques.
>
> Je ne suis ni acheteuse ni commerciale. Auriez-vous 15 minutes pour me raconter comment est arrivé
> votre dernier client à façon ? Je peux vous appeler au créneau qui vous convient, dès 7 h 30.
>
> Si vous ne souhaitez pas être recontacté(e), dites-le-moi simplement.

**Façonnier, au téléphone** (20 secondes) :

> « Bonjour, [Prénom Nom], étudiante en master. Je ne vends rien et je ne suis pas acheteuse :
> j'étudie comment les fabricants trouvent leurs clients à façon. Vous avez deux minutes, ou je vous
> rappelle à un meilleur moment ? »

Au standard : « Qui s'occupe des demandes de fabrication à façon ou de marques de distributeur ? Quand
puis-je le ou la joindre ? »

**Structure, pépinière ou incubateur, e-mail.** Objet : *Les jeunes marques qui vous demandent un fabricant : 15 minutes ?*

> Bonjour [Prénom],
>
> Étudiante en master à [école], j'étudie comment les jeunes marques alimentaires trouvent un
> fabricant quand elles sortent de leurs premiers lots. [Structure] est souvent leur premier
> interlocuteur.
>
> Accepteriez-vous de me raconter en 15 minutes la dernière fois qu'une marque vous a demandé de l'aide
> sur ce point, et ce qui s'est passé ensuite ?

**Relance unique (4 jours après) :**

> Bonjour [Prénom], je me permets une seule relance : auriez-vous 20 minutes cette semaine ou la
> suivante, au créneau qui vous arrange ? Sinon, aucun souci, je ne vous relancerai pas.

### 4.4 Guide d'entretien
[`script-mom-test.md`](script-mom-test.md), mis à jour le 12/10 :
- plus aucune question d'argent ni de prévente ;
- côté marques, une question sur les moyens déjà essayés (annuaires, salons, plateformes) ;
- côté façonniers, la question sur le dernier petit projet, celle qui peut tuer l'idée.

### 4.5 Définitions communes
Sans elles, les six comptent différemment et le 31/10 ne tranche rien.

| Terme | Ce qui compte | Ce qui ne compte pas |
|---|---|---|
| Petit projet | La première production en usine d'une marque qui n'avait jamais produit en usine | Un nouveau produit d'un client déjà installé |
| Façonnier qui accepte | A accepté au moins un petit projet **au cours des 12 derniers mois** | « On pourrait », « ça dépend » |
| Recherche pénible | Une recherche commencée il y a moins de 24 mois, qui a pris plus d'un mois ou retardé un lancement, **et** qui a coûté de l'argent (consultant, échantillons, salon, essai raté) | « Ça a été un peu long », sans date ni dépense |
| Dépense | Une somme réellement payée, même approximative | « On aurait été prêts à payer » |

### 4.6 Éthique et RGPD
- Dire en début d'entretien qui on est, pourquoi on pose ces questions, et que l'on prend des notes.
- Pas d'enregistrement sans accord explicite.
- Ne demander ni le nom des clients ni les prix aux façonniers.
- Anonymiser les synthèses (M1, F1, S1…) et supprimer les données personnelles à la fin du projet.
- Rien pendant le temps de travail en entreprise, et rien qui concerne l'employeur d'un membre.

### 4.7 Notes et analyse
- **Après chaque entretien**, remplir [`suivi-entretiens.csv`](suivi-entretiens.csv) dans les 2 heures,
  avec au moins une citation exacte. Pour travailler à six, l'importer dans un tableur partagé.
  Valeurs de la colonne `statut` : a_contacter, contacte, relance, entretien_planifie, entretien_fait,
  refus, sans_reponse, opposition. Les colonnes `m_`, `f_` et `s_` concernent respectivement les
  marques, les façonniers et les structures.
- **Tous les 4 entretiens**, 10 minutes en binôme : ce qui confirme, ce qui contredit, ce qui surprend.
- **Analyse finale :** pour chaque hypothèse, compter les personnes qui remplissent la définition, et
  garder 2 ou 3 citations.

## 5. Étude quantitative

### 5.1 Dimensionnement à partir de données publiques
**Question :** combien de jeunes marques alimentaires cherchent un fabricant chaque année en France ?
On fait trois estimations indépendantes, puis on les compare (méthode du skill `market-sizing`).

| Approche | Calcul | Données de départ |
|---|---|---|
| Par le haut | Entreprises alimentaires × part qui fait fabriquer par un tiers × part qui cherche un fabricant dans l'année | 17 253 entreprises en 2016, hors artisanat commercial (ministère de l'Économie) ; « plus de 20 000 » selon l'ANIA (janvier 2026). Les parts viennent des entretiens et du questionnaire |
| Par le bas | Nouvelles marques par an × part qui fait fabriquer × nombre de recherches par marque | Créations d'entreprises par code d'activité ([annuaire des entreprises](https://annuaire-entreprises.data.gouv.fr/)) ; campagnes alimentaires de financement participatif (Miimosa : 736 projets accompagnés en 2023, exploitations agricoles comprises) ; promotions des incubateurs |
| Par comparaison | Volume de PartnerSlate × rapport de taille entre les marchés français et américain | PartnerSlate revendique plus de 100 marques qui publient un projet par mois (2023). Le rapport de taille reste à sourcer |

**Attention :** une marque qui fait tout fabriquer n'est souvent pas classée dans l'industrie
alimentaire (codes 10 et 11). L'approche par le haut risque donc de la manquer [Likely].

**Livrable :**
- trois scénarios (bas, central, haut), chaque chiffre avec sa source et son niveau de confiance ;
- le chiffre d'affaires possible aux prix observés : 199 $ par projet chez PartnerSlate, environ 440 €
  par jour pour un consultant indépendant.

C'est le scénario central qu'on compare au seuil de H4.

### 5.2 Questionnaire en ligne
- **Cible :** fondatrices et fondateurs de marques alimentaires lancées en 2021 ou après.
- **Échantillon non représentatif, et c'est assumé.** Il n'existe aucune liste de ces marques, donc
  aucun tirage au hasard n'est possible. On diffuse par les structures, les incubateurs, les
  pépinières, les groupes LinkedIn et Facebook de créateurs de marques alimentaires, les porteurs de
  projets de financement participatif et les personnes interrogées (bouche-à-oreille).
- **Objectif : au moins 30 réponses complètes** (faisabilité [Guessing]). Avec 30 réponses, un
  pourcentage de 50 % a une marge d'erreur d'environ ±18 points ; avec 50 réponses, d'environ
  ±14 points (intervalle de confiance à 95 %). On lit donc des **ordres de grandeur**, et on donne
  toujours les effectifs (« 12 sur 31 »).
- **Biais principal :** les marques qui ont souffert répondent plus volontiers [Likely]. Le
  questionnaire surestime donc probablement H1 ; les entretiens servent de contrôle.
- **Questions :** [`questionnaire-quanti.md`](questionnaire-quanti.md) (13 questions, 5 minutes,
  uniquement des faits passés).
- **Calendrier :** version 0 le 16/10, ajustée après les 6 premiers entretiens, testée sur
  3 personnes le 19/10, diffusée du 20 au 28/10.
- **Pas de questionnaire pour les façonniers :** trop peu de réponses à attendre [Likely]. Les
  entretiens et les codes de traçabilité suffisent.

## 6. Calendrier

| Quand | Quoi |
|---|---|
| Lundi 12/10 | Message d'équipe (section 9). La porteuse valide les seuils de la section 2 |
| Du mardi 13 au dimanche 18/10 | Recrutement et 6 premiers entretiens ; sources du dimensionnement ; codes de traçabilité ; questionnaire v0 le vendredi 16/10 |
| Mercredi 14/10 | Point de 20 minutes : messages envoyés, réponses reçues, accès au SIAL (oui ou non) |
| Du lundi 19 au dimanche 25/10 | Questionnaire testé le 19 et diffusé dès le 20 ; 14 entretiens au total ; 3 structures interrogées avant le 23 ; trois estimations du marché |
| Du lundi 26 au vendredi 30/10 | Questionnaire clos le 28 ; 18 à 20 entretiens au total ; analyse ; synthèse d'une page par hypothèse le 30 |
| Samedi 31/10 | Décision de la porteuse, avec la grille de la section 2 |

## 7. Rôles

| Rôle | Nb | Livrable au 30/10 |
|---|---|---|
| Étude documentaire, dimensionnement, analyse du questionnaire | 1 | Trois estimations sourcées, mesure des codes de traçabilité, résultats du questionnaire |
| Entretiens avec les jeunes marques | 2 | 8 à 10 entretiens notés |
| Entretiens avec les façonniers | 2 | 6 à 8 entretiens notés |
| Entretiens avec les structures, diffusion du questionnaire | 1 | 3 à 4 entretiens, au moins 30 réponses au questionnaire |

## 8. Ce que l'étude ne dira pas
- **Si les marques paieront notre prix.** On mesure ce qu'elles ont déjà dépensé, pas ce qu'elles
  achèteraient. Seul un test payant le dira, après une décision « continuer ».
- **Des pourcentages représentatifs.** Le questionnaire ne l'est pas.
- **Si les façonniers paieraient pour recevoir des projets.** On mesure seulement ce qu'ils dépensent
  déjà pour trouver des clients.

## 9. Message aux 5 autres membres (à envoyer aujourd'hui)

> Salut à tous. On part tous les 6 sur une seule idée, les **façonniers alimentaires** : aider les
> jeunes marques alimentaires à trouver le fabricant de leurs premiers milliers d'unités.
>
> On en est à la **validation** : on ne vend rien. D'ici le samedi 31/10, une étude documentaire,
> qualitative (18 à 20 entretiens) et quantitative (dimensionnement du marché et questionnaire) doit
> dire si on continue, si on change d'angle ou si on abandonne. Les critères sont fixés à l'avance.
>
> 4 rôles :
> 1. Étude documentaire, dimensionnement, analyse du questionnaire (1 personne, à l'aise avec les chiffres)
> 2. Entretiens avec des jeunes marques (2 personnes)
> 3. Entretiens avec des fabricants à façon (2 personnes)
> 4. Entretiens avec les structures (CCI, ARIA, pépinières) et diffusion du questionnaire (1 personne)
>
> J'ai besoin de 3 réponses de chacun **ce soir avant 20 h** :
> a) tes créneaux libres réels jusqu'au 31/10 (jamais pendant ton temps de travail en entreprise) ;
> b) ton rôle, en 1er et 2e choix ;
> c) appeler un inconnu, ça te va ? (oui / plutôt par écrit / non)
>
> Le protocole complet est dans le dépôt : `ideas/faconniers/protocole-etude-validation.md`.
> Point de 20 minutes mercredi soir.

## Sources
- Codes de traçabilité : [Justice.fr : le code emballeur EMB](https://www.justice.fr/fiche/se-procurer-code-emballeur-emb), [Open Food Facts : codes de traçabilité](https://world.openfoodfacts.org/packager-codes)
- Secteur : [Ministère de l'Économie : la filière agroalimentaire](https://www.entreprises.gouv.fr/secteurs-dactivite/industrie/les-comites-strategiques-de-filiere/la-filiere-agroalimentaire), [Terre-net : l'ANIA, janvier 2026](https://www.terre-net.fr/agroalimentaire/article/893139/l-agroalimentaire-a-bout-de-souffle-selon-l-ania), [Miimosa : rapport d'impact 2023](https://decouverte.miimosa.com/hubfs/MiiMOSA%20Rapport%20dimpact.pdf)
- Prix de référence et concurrents : voir la mise à jour du 12/10 dans [`veille-marche.md`](veille-marche.md)
