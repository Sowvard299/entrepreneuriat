# 10 idées de startup (génération du 09/10/2026)

Généré avec le skill `ai-startup-opportunity-generator` (mode « découverte large »),
élargi au-delà de l'IA comme le demande `CLAUDE.md` : B2B, B2C, services, produit physique.

## Hypothèses de départ

- **Marché :** la France (le profil ne précise pas la géographie, mais l'équipe y est).
- **Équipe :** 6 personnes à temps partiel cette année. On ne connaît pas encore leurs
  compétences (TODO dans `CLAUDE.md`). Les notes « simplicité du MVP » supposent au moins
  une personne capable de coder ou d'utiliser du no-code. Si ce n'est pas le cas, les idées
  logicielles perdent 1 à 2 points.
- **Avantage fondateur :** le marketing et le métier de PM électricité pour TPE/PME comptent
  comme un bonus dans la note, jamais comme un filtre.
- **Chiffres :** ce sont des ordres de grandeur de mémoire, **à vérifier** avant toute décision.

## Grille de notation

Elle reprend celle du skill (notes de 1 à 10, moyenne pondérée). Une adaptation : comme toutes
les idées ne reposent pas sur l'IA, « Automation Fit » devient **« Faisabilité de la solution »**
(la solution règle-t-elle vraiment le problème avec la technologie d'aujourd'hui ?).

| Critère | Poids |
|---|---|
| Douleur | 25 % |
| Budget existant | 20 % |
| Faisabilité de la solution | 20 % |
| Simplicité du MVP | 15 % |
| Facilité de distribution | 10 % |
| Différenciation | 10 % |

Lecture : 8+ exceptionnel · 6,5–7,9 fort · 5–6,4 viable · < 5 faible.

## Tableau récapitulatif (classé)

| # | Idée | Secteur | Qui paie | MVP | Note | Survie |
|---|---|---|---|---|---|---|
| 1 | **FicheProd** : fiches techniques et étiquettes conformes pour PME agro | Agroalimentaire / réglementaire | Dirigeant ou responsable qualité de la PME agro | 6–8 sem. | **6,80** | Moyenne-haute |
| 2 | **AlternLink** : placement des alternants pour CFA et écoles | Éducation / RH | Directeur de CFA | 6–8 sem. | **6,50** | Moyenne |
| 3 | **RSE Réponse** : remplir les questionnaires RSE des clients | RSE / B2B | Dirigeant de PME sous-traitante | 4–6 sem. | **6,35** | Moyenne |
| 4 | **Dossier Rénov'** : copilote des dossiers d'aides pour artisans RGE | BTP / rénovation | Artisan RGE | 8–10 sem. | **6,35** | Moyenne-basse |
| 5 | **Watt Audit** : audit des contrats et factures d'électricité des TPE-PME | Énergie B2B | Gérant de TPE/PME | 4–6 sem. | **6,25** | Moyenne |
| 6 | **Après** : démarches après un décès, via assureurs et mutuelles | Services / assurance | Assureur obsèques, mutuelle, banque | 8–10 sem. | **6,20** | Moyenne |
| 7 | **FroidSûr** : capteurs pour chambres froides (HACCP + énergie) | IoT / commerce alimentaire | Restaurateur, boucher, supérette | 10–14 sem. | **5,85** | Moyenne-basse |
| 8 | **Relais Aidants** : coordination des aidants, payée par l'employeur | Santé / silver économie | DRH, mutuelle | 6–8 sem. | **5,30** | Basse |
| 9 | **Cantine Locale** : approvisionnement local et reporting EGalim | Agri / restauration collective | Commune, EHPAD, gestionnaire de cantine | 12+ sem. | **5,10** | Basse |
| 10 | **Drêche & Co** : marque de snacks upcyclés à partir de coproduits | Agroalimentaire B2C | Consommateur | 12+ sem. | **4,05** | Basse |

---

## Fiches détaillées

### 1. FicheProd : fiches techniques et étiquetage pour PME agroalimentaires — 6,80

- **Qui a le problème :** les artisans et PME agro (conserveries, biscuiteries, traiteurs,
  brasseries...). La France compte plus de 15 000 entreprises agroalimentaires, dont environ
  98 % de TPE/PME.
- **Ce qu'ils font aujourd'hui :** ils calculent les valeurs nutritionnelles à la main
  (table Ciqual, Excel) ou paient un laboratoire ou un consultant à la recette. Ils
  ressaisissent les allergènes et les ingrédients dans chaque fiche technique demandée par
  la GMS, les grossistes ou la restauration, chacun avec son propre format. Ils refont tout
  à chaque changement de recette ou de fournisseur.
- **Pourquoi ça coûte cher :** une erreur d'allergène peut entraîner un rappel produit. Une
  fiche manquante retarde un référencement. Il faut compter des heures par référence et
  par client.
- **Solution :** l'utilisateur saisit ou importe ses recettes et les fiches de ses
  fournisseurs. L'outil extrait les données (OCR + LLM), calcule la valeur nutritionnelle
  et le Nutri-Score, détecte les allergènes et génère l'étiquette INCO et les fiches
  techniques au format de chaque client. **Un humain valide** avant toute publication.
- **MVP :** une seule cible (biscuiteries et pâtisseries artisanales), recettes vers
  tableau nutritionnel, liste d'allergènes et fiche technique PDF.
- **Modèle :** abonnement de 49 à 199 €/mois selon le nombre de références. Option : revue
  par une diététicienne partenaire.
- **Concurrents :** des PIM pour grands comptes (Salsify, ex-Alkemics), des logiciels de
  calcul nutritionnel (Nutritics, Recipal, surtout anglo-saxons), des laboratoires et
  consultants qualité, et Excel. Le segment des petits acteurs francophones semble **mal servi**.
- **Pourquoi ça peut gagner :** un focus vertical sur la réglementation française et
  européenne, des formats de fiches propres aux distributeurs français, et un prix adapté
  aux TPE.
- **Risques :** le piège de la précision (d'où la validation humaine obligatoire), la
  responsabilité juridique (prévoir des CGU claires et une assurance RC pro), un marché de
  TPE sensible au prix.
- **Timing :** les LLM et l'OCR extraient désormais bien les fiches fournisseurs, et la
  pression réglementaire (évolutions du Nutri-Score, exigences des distributeurs) augmente.
- **Atout équipe :** l'intérêt pour l'agroalimentaire, et le marketing pour la distribution
  (salons, associations régionales des industries agroalimentaires, chambres de métiers).

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 7 | 6 | 8 | 7 | 6 | 6 |

### 2. AlternLink : outil de placement des alternants pour les CFA — 6,50

- **Qui a le problème :** les CFA et les écoles qui recrutent des alternants. Plus de
  850 000 contrats d'apprentissage sont signés chaque année. Le CFA n'est financé que si
  l'étudiant signe un contrat. Les chargés de relations entreprises prospectent à la main,
  par téléphone, sur LinkedIn et avec des tableurs.
- **Pourquoi ça coûte cher :** un étudiant sans entreprise représente un financement perdu
  et un abandon possible. Le CFA dispose aussi d'un délai légal limité pour trouver un
  contrat au jeune.
- **Solution :** un CRM spécialisé. Il cible les entreprises qui recrutent (offres
  publiées, historique des alternants), rapproche les CV des offres, prépare des messages
  de prospection personnalisés (à valider par le chargé) et suit chaque étudiant jusqu'à la
  signature du contrat.
- **MVP :** un tableau de suivi des étudiants sans contrat, plus un moteur de rapprochement
  entre ces étudiants et les offres publiques.
- **Modèle :** licence par CFA de 200 à 800 €/mois, ou facturation par étudiant suivi.
- **Concurrents :** les ERP de CFA comme Ypareo (gestion administrative, peu de
  prospection), les jobboards (Walt, Hellowork, JobTeaser) qui sont orientés étudiants et non
  CFA, et les CRM génériques.
- **Pourquoi ça peut gagner :** l'outil est pensé pour le chargé de relations entreprises,
  et l'équipe est **à l'intérieur du système** (étudiants en master en alternance, avec un
  accès direct aux écoles).
- **Risques :** le budget des CFA est sous tension depuis la baisse des niveaux de prise en
  charge et des aides à l'embauche en 2025. L'argument doit donc être le ROI : un contrat
  signé en plus paie l'abonnement. Les cycles de vente peuvent être lents dans les grands
  réseaux.
- **Timing :** moins d'aides à l'embauche signifie moins d'entreprises qui recrutent et donc
  plus de difficulté à placer les étudiants. La douleur augmente précisément maintenant.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 7 | 6 | 7 | 7 | 6 | 5 |

### 3. RSE Réponse : répondre aux questionnaires RSE des clients — 6,35

- **Qui a le problème :** les PME sous-traitantes de grands groupes. Elles reçoivent des
  questionnaires RSE (EcoVadis, formats maison, standard volontaire VSME) et y répondent à
  la main, souvent par le dirigeant, en cherchant les documents un par un.
- **Pourquoi ça coûte cher :** une note RSE faible peut faire perdre un contrat ou un appel
  d'offres. Chaque questionnaire prend des jours.
- **Solution :** l'entreprise charge ses documents (politiques, factures d'énergie,
  registres RH). L'outil pré-remplit les réponses en citant ses sources et liste les
  preuves manquantes. **Le dirigeant valide.** L'outil réutilise ensuite les réponses d'un
  questionnaire à l'autre.
- **MVP :** une base documentaire et un pré-remplissage pour **un** format (EcoVadis ou VSME).
- **Modèle :** 99 à 299 €/mois.
- **Concurrents :** les plateformes carbone et ESG (Greenly, Sweep, Carbo, Tennaxia) et les
  outils de réponse aux appels d'offres (Loopio, Responsive) : le marché est
  **assez encombré**. L'ouverture, c'est la réponse aux questionnaires pour les PME, pas le
  bilan carbone.
- **Risques :** le paquet Omnibus réduit fortement le périmètre de la CSRD, ce qui pourrait
  diminuer la pression. En revanche, les donneurs d'ordre continuent d'interroger leurs
  fournisseurs. Il faut aussi s'attendre à l'arrivée de fonctionnalités IA chez les acteurs
  existants.
- **Atout équipe :** les données d'énergie (scope 2) sont un sujet maîtrisé.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 6 | 6 | 8 | 7 | 5 | 5 |

### 4. Dossier Rénov' : copilote des dossiers d'aides pour artisans RGE — 6,35

- **Qui a le problème :** les artisans RGE (isolation, pompes à chaleur, menuiserie). Ils
  avancent le montant des aides (MaPrimeRénov', CEE) à leurs clients et montent des dossiers
  lourds. Un dossier refusé ou incomplet, c'est une créance qui n'est jamais payée.
- **Solution :** une checklist dynamique selon les travaux et le profil du ménage, un
  contrôle des pièces (devis, factures, photos, attestations) avant envoi, des alertes sur les
  incohérences et un suivi des paiements.
- **MVP :** un contrôle de conformité des dossiers CEE pour un seul type de geste (par
  exemple les pompes à chaleur).
- **Modèle :** un abonnement de 79 à 149 €/mois, ou un prix par dossier contrôlé.
- **Concurrents :** les délégataires et opérateurs CEE (Effy, Hellio), qui ont intérêt à
  capter le dossier, les logiciels de devis (Obat, Tolteck) et les cabinets de montage de
  dossiers.
- **Risques :** **très forte instabilité réglementaire** (le guichet MaPrimeRénov' a été
  suspendu à l'été 2025, et les règles changent souvent), un secteur gangrené par la
  fraude, des artisans réfractaires aux outils numériques.
- **Atout équipe :** la connaissance de l'énergie et des CEE (lien avec les fournisseurs
  d'énergie, qui sont des « obligés » CEE).

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 8 | 5 | 7 | 5 | 6 | 6 |

### 5. Watt Audit : audit des contrats et factures d'électricité des TPE-PME — 6,25

- **Qui a le problème :** les gérants de TPE/PME (restaurants, boulangeries, commerces,
  ateliers). Ils sont marqués par la crise de 2022-2023 et ne comprennent ni leur facture
  (puissance souscrite, TURPE, taxes) ni le nouveau cadre depuis la fin de l'ARENH au
  1er janvier 2026. Beaucoup ignorent s'ils ont encore droit au tarif réglementé (TPE de
  moins de 10 salariés et moins de 2 M€ de chiffre d'affaires).
- **Solution :** l'utilisateur dépose ses factures en PDF. L'outil extrait les données,
  détecte les erreurs et les puissances mal dimensionnées, compare avec le TRVE et les
  offres du marché, et alerte avant chaque échéance de contrat.
- **MVP :** un diagnostic gratuit à partir d'une facture, qui sert de produit d'appel,
  puis un rapport payant.
- **Modèle :** une commission sur les économies réalisées la première année, ou un
  abonnement de 15 à 40 €/mois. Canal privilégié : les experts-comptables.
- **Concurrents :** des courtiers (Opéra Énergie, Selectra), le comparateur public du
  médiateur de l'énergie, et des outils de suivi énergétique. Les courtiers sont rémunérés
  par les fournisseurs, d'où une **méfiance** des clients (démarchage abusif signalé par le
  médiateur).
- **Pourquoi ça peut gagner :** un positionnement indépendant, payé par le client.
  L'expertise métier du fondateur est **la plus forte des 10 idées**.
- **Risques :** ⚠️ **conflit d'intérêts avec l'emploi chez EDF**. Il faut vérifier la clause
  de loyauté ou de non-concurrence du contrat d'alternance avant d'avancer, et ne jamais
  utiliser d'information interne. Autres risques : la douleur baisse quand les prix baissent,
  et les TPE sont habituées au « gratuit » des courtiers.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 6 | 5 | 8 | 7 | 5 | 6 |

### 6. Après : les démarches après un décès, en marque blanche — 6,20

- **Qui a le problème :** les familles endeuillées. Il y a environ 640 000 décès par an en
  France, et chacun entraîne des dizaines de démarches (banques, caisses de retraite,
  résiliations d'abonnements, succession) à un moment d'épuisement.
- **Solution :** une liste de démarches personnalisée, des courriers pré-remplis, des
  résiliations en un clic et un suivi partagé entre les membres de la famille.
- **Modèle :** **B2B2C**, où l'assureur obsèques, la mutuelle ou la banque paie un service
  en marque blanche (licence ou prix par dossier). Une version B2C payante est possible en
  complément, via le référencement naturel.
- **Concurrents :** Simplifia (déjà positionné en marque blanche), les services des pompes
  funèbres et des notaires, et le guide de service-public.fr.
- **Risques :** un concurrent direct est déjà installé, et les partenariats avec les
  assureurs sont longs à signer. Il faut aussi des données sensibles (RGPD). Le sujet est
  difficile émotionnellement pour l'équipe.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 8 | 5 | 7 | 6 | 4 | 5 |

### 7. FroidSûr : capteurs connectés pour chambres froides (HACCP + énergie) — 5,85

- **Qui a le problème :** les restaurateurs, bouchers, traiteurs et supérettes. Une panne de
  chambre froide la nuit peut faire perdre des milliers d'euros de marchandise. Les
  relevés de température HACCP se font souvent sur papier, et le froid est leur premier poste
  de consommation d'électricité.
- **Solution :** des capteurs sans fil (LoRa) branchés en quelques minutes, avec une alerte
  SMS ou un appel en cas de dérive, des relevés HACCP automatiques prêts pour un contrôle
  sanitaire, et une détection des compresseurs qui surconsomment (avant la panne).
- **Modèle :** matériel vendu ou loué, plus un abonnement de 20 à 50 €/mois par site.
  Distribution par les installateurs frigoristes.
- **Concurrents :** les solutions HACCP (Octopus Lab, Traqfood), le suivi énergétique pour
  PME industrielles (Sensorfact, aux Pays-Bas) et la télésurveillance des frigoristes.
  L'ouverture : **combiner sécurité sanitaire et énergie** pour le petit commerce.
- **Risques :** du matériel (stock, service après-vente, certification), un MVP plus long,
  et des marges plus faibles que pour du logiciel pur.
- **Atout équipe :** l'énergie et l'intérêt pour la deeptech et l'agroalimentaire, tout en
  un.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 7 | 5 | 7 | 4 | 5 | 6 |

### 8. Relais Aidants : coordination des aidants, financée par l'employeur — 5,30

- **Qui a le problème :** environ 9 à 11 millions d'aidants en France, dont beaucoup sont
  salariés. Ils doivent coordonner les intervenants à domicile, les rendez-vous et les
  dossiers d'aide (APA, MDPH), ce qui entraîne absentéisme et épuisement.
- **Solution :** une application de coordination familiale (planning, documents partagés,
  liste des aides auxquelles on a droit), complétée par un accompagnement humain.
- **Modèle :** payé par l'employeur (dans le cadre de la qualité de vie au travail) ou la
  mutuelle, environ 2 à 5 € par salarié et par an.
- **Concurrents :** Responsage (accompagnement des aidants pour les entreprises), Ma
  Boussole Aidants (service public), Familéo. **Beaucoup d'applications B2C pour aidants
  ont disparu** faute de modèle économique, d'où le choix du B2B2C.
- **Risques :** des cycles de vente longs auprès des DRH, et une forte composante de service
  humain, difficile à faire tenir à une équipe à temps partiel.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 8 | 3 | 5 | 6 | 3 | 5 |

### 9. Cantine Locale : approvisionnement local et reporting EGalim — 5,10

- **Qui a le problème :** les cantines de petites communes et les EHPAD. La loi EGalim impose
  50 % de produits durables et de qualité, dont 20 % de bio, mais les petits producteurs
  n'arrivent pas à répondre aux marchés publics et les gestionnaires peinent à faire leur
  déclaration annuelle (sur « ma-cantine »).
- **Solution :** un catalogue de producteurs locaux, des commandes groupées, des livraisons
  mutualisées et un calcul automatique des taux EGalim.
- **Concurrents :** Agrilocal (plateforme publique départementale), Socleo et les
  grossistes de la restauration collective.
- **Risques :** une **marketplace à deux faces avec de la logistique**, qui mange la marge
  (plusieurs plateformes de circuits courts B2B ont fermé ou pivoté pour cette raison).
  S'y ajoutent les achats publics et l'absence de sanction réelle en cas de non-respect
  d'EGalim.
- **Pourquoi elle est gardée :** l'impact est fort, elle rejoint l'intérêt pour
  l'agroalimentaire, et une version « logiciel de reporting seul » serait bien plus simple
  à lancer.

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 6 | 4 | 6 | 4 | 4 | 6 |

### 10. Drêche & Co : marque de snacks upcyclés — 4,05

- **Concept :** transformer des coproduits agroalimentaires (drêche de brasserie, pulpe de
  fruits issue des jus, petit-lait) en crackers ou en biscuits, vendus en épiceries fines, en
  ligne et en entreprise.
- **Pourquoi la note est faible :** il n'y a pas de douleur client (c'est un achat plaisir),
  la grande distribution est difficile d'accès, les marges sont étroites et la fabrication
  (sous-traitance, normes d'hygiène) est longue à mettre en place. Quelques marques
  françaises existent déjà sur ce créneau, ainsi que tout l'écosystème anti-gaspillage
  (Too Good To Go, Phenix).
- **Pourquoi elle est gardée :** c'est la seule idée B2C de produit physique. Elle repose
  avant tout sur le **marketing et la marque** (le point fort du fondateur) et correspond à
  l'intérêt pour l'agroalimentaire. C'est aussi un projet concret et motivant pour une
  équipe de 6, testable rapidement (petite série, marché, précommandes).

| Douleur | Budget | Faisabilité | MVP | Distribution | Différenciation |
|---|---|---|---|---|---|
| 2 | 4 | 6 | 5 | 4 | 4 |

---

## Synthèse

- **Meilleure note globale :** #1 FicheProd (6,80). Douleur réglementaire réelle, segment
  mal servi, validation humaine naturelle.
- **La plus rapide à construire :** #3 RSE Réponse ou #5 Watt Audit (4–6 semaines,
  traitement de documents puis rapport).
- **Plus fort potentiel de revenus :** #4 Dossier Rénov' (la douleur se chiffre en créances
  impayées), à condition de supporter l'instabilité réglementaire.
- **La plus accessible pour l'équipe :** #2 AlternLink. L'équipe a un accès direct aux CFA
  et aux écoles, ce qui permet de faire 20 entretiens dès le mois prochain.
- **Par où commencer :** **#1 FicheProd** et **#2 AlternLink** en parallèle, avec des
  entretiens clients (skill `mom-test`) avant toute ligne de code. **#5 Watt Audit**
  reste l'idée où l'expertise est la plus forte, mais seulement après avoir réglé la
  question du conflit d'intérêts avec EDF.

## Prochaines étapes

1. Compléter les TODO de `CLAUDE.md` (compétences des 6 membres, budget, ambition). Plusieurs
   notes de cette liste en dépendent.
2. Lancer `llm-council` sur les 3 à 5 premières idées pour les confronter.
3. Pour l'idée favorite : `startup-design` (Fast Track), puis un script `mom-test`, et
   enregistrer le travail sous `ideas/<nom-idee>/`.
