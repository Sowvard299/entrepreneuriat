---
name: market-segment-scanner
description: Trouve et classe des marchés français en croissance, les découpe en segments précis, puis propose pour chaque segment un angle « pareil que l'existant mais mieux », avant toute idée de produit. À utiliser dès que l'utilisateur cherche une idée d'entreprise, un marché porteur, une niche, un segment de départ ou un modèle à reprendre ; dès qu'il dit partir du marché plutôt que de l'idée, que les idées sont trop génériques ou que le marché est trop petit ; et dès qu'il demande de cartographier, segmenter ou comparer des marchés (market map, growth markets, segmentation, niche scan), même sans citer ce skill. Produit marches.md, segments.md et une short-list segment × angle prête pour llm-council, market-sizing et beachhead-segment.
---

# Market Segment Scanner

> **Rôle en v4 (2026-10-13)** : ce skill fournit la **liste d'entrée** de la porte 1 (marchés et segments
> candidats). Il ne décide plus : aucune piste n'est retenue sur sa taille ou sa croissance avant d'avoir passé
> les portes 1 (3 prix payés) et 2 (engagement client). Voir `CLAUDE.md`, section « Workflow ». Pour économiser,
> lancer seulement les étapes 1 à 4 avec 2 chercheurs au plus, et noter les segments sans recherche de signaux.

Inverse l'entonnoir habituel (plainte → idée → marché) en
**marché en croissance → segment précis → angle « pareil mais mieux »**.

Pourquoi : partir des plaintes clients visibles (avis Trustpilot, forums) conduit tout le monde
aux mêmes idées génériques, et à des niches trop petites pour faire vivre une équipe. La v2 de ce
dépôt l'a montré (`ideas/_recherche-v2/BILAN.md`). Un marché qui grossit fixe un plafond haut ; la
segmentation apporte ensuite la précision et l'avantage.

## Avant de commencer

1. Lis `CLAUDE.md` : profil, équipe, zone, budget, la section « Critères de viabilité », la grille
   de score et la section « Sous-agents et coordination ». Ses valeurs priment sur celles de ce skill.
   Si une information manque, prends une hypothèse raisonnable et note-la dans `hypotheses.md`.
2. Crée ou reprends `ideas/_recherche-v3/etat.md` : une ligne par étape (1 à 6) avec ✔ et la date
   quand elle est terminée, plus une ligne par sous-agent lancé (mission, fichier, statut). Si le
   fichier existe, relis les **fichiers de synthèse** déjà écrits et continue sans refaire ce qui est fait.
3. Écris au fil de l'eau (un marché ou un segment à la fois). Une coupure de session ne doit
   rien faire perdre.
4. Outils, dans cet ordre de préférence :
   - API `recherche-entreprises.api.gouv.fr` (sans clé) pour compter les entreprises ;
   - API Open Urssaf et pages Insee pour les particuliers employeurs, micro-entrepreneurs, démographie ;
   - un MCP Google Trends s'il est installé, sinon `web_search` et les pages publiques de tendances ;
   - `web_search` et `web_fetch` pour tout le reste.
   Les sources bloquées connues sont listées dans `.claude/agents/chercheur.md` : ne perds pas de
   recherches dessus. Si une source bloque, dis-le dans le fichier au lieu de l'ignorer.

## Répartition du travail (quand ce skill est lancé par un coordinateur)

Les étapes 1 et 2 demandent une centaine de recherches : elles se font avec des sous-agents
`chercheur`, en vagues de 4 au plus.
- Étape 1 + 2 : 4 chercheurs, chacun sur 2 lentilles (voir ci-dessous) et 8 à 10 marchés, au plus
  3 recherches web par marché. Fichiers : `marches/<lentilles>.md` (travail) et
  `marches/<lentilles>-synthese.md` (une ligne par marché au format du tableau de l'étape 3).
- Le coordinateur fusionne les synthèses dans `marches.md`, puis lance un `verificateur` sur les
  chiffres de taille et de croissance des 8 marchés gardés.
- Étape 4 (preuves par segment) : chercheurs par paires de segments, même principe.

## Étape 1 : longue liste de 30 à 40 marchés

Un marché = **un client qui paie + une dépense précise** (par exemple « entretien des
chaudières des petits commerces »), jamais une technologie (« l'IA »). Génère-les avec au
moins 5 de ces 7 lentilles, au moins 3 marchés par lentille utilisée :

1. **Obligation datée** : réglementation avec échéance 2026-2029. Vérifie la date et le périmètre
   sur une source officielle : beaucoup d'obligations ont été reportées ou réduites (CSRD des PME,
   décret BACS, ZFE, REP emballages professionnels…).
2. **Transition en cours** : énergie, numérique, vieillissement, normes, nouveaux usages.
3. **Fragmentation** : beaucoup d'établissements (codes NAF) et peu d'acteurs nationaux structurés.
4. **Modèle qui a grossi ailleurs** : États-Unis, Royaume-Uni, Allemagne, Pays-Bas, pays nordiques,
   pas encore mûr en France.
5. **Demande en hausse** : requêtes en croissance sur 5 ans (Google Trends, France).
6. **Capital et réseaux** : franchises qui ouvrent beaucoup d'unités, cessions de petites activités.
7. **Dépense déjà là mais mal servie** : indépendants peu joignables, plateformes qui prennent
   une grosse commission.

Couvre au moins 10 secteurs, en B2B et B2C, avec des services, des produits physiques et du logiciel.
Ne laisse pas le profil du fondateur réduire la liste : le secteur qu'il connaît compte plus tard
dans le score, pas ici.

## Étape 2 : fiche marché

Remplis une fiche par marché, dans `marches.md`. Ce gabarit est exact :

```
### [Marché : qui paie, pour quoi]
- Taille France : X M€/an. Source, année, périmètre. (ou calcul bottom-up : N clients × dépense, montré)
- Croissance : Y %/an sur [période]. Source(s). Valeur ou volume ?
- Moteur de croissance : [obligation, transition, usage...], daté si possible.
- Acteurs : nombre, 3 premiers et leur part (source).
- Clients identifiables : N (Sirene : NAF …, effectif …, zone …).
- Demande : tendance 5 ans sur [requêtes], hausse / stable / baisse.
- Modèle d'exécution : logiciel / service outillé / service à forte main-d'œuvre (employeur) / produit.
- Contre-preuve (obligatoire) : ce qui pourrait contredire la croissance ou la taille.
- Seuils CLAUDE.md : taille ✔/✘ | croissance ✔/✘ | concentration ✔/✘ | clients ✔/✘
- Confiance : forte / moyenne / faible (selon la qualité des sources)
```

Règles pour les chiffres :
- Préfère INSEE, Eurostat, ministères, fédérations professionnelles, Banque de France, Bpifrance,
  rapports annuels de sociétés cotées, comptes déposés (API Recherche d'entreprises, champ `finances`).
  Un chiffre venant d'un vendeur de rapports (Xerfi, Statista, Businesscoot…) ou d'un blog sans
  méthode est « confiance faible ».
- Pas de taille publiée fiable ? Calcule-la bottom-up (clients identifiables × dépense annuelle
  constatée sur des prix publics) et montre le calcul. Confiance « moyenne » au mieux.
- Distingue le marché mondial, européen et français. Ne mélange jamais les trois.
- Une croissance en valeur peut venir de l'inflation : cherche aussi le volume.
- Pour compter les entreprises : interroge l'API `recherche-entreprises.api.gouv.fr` avec
  `activite_principale` (NAF), `departement`, `tranche_effectif_salarie` et `etat_administratif=A`,
  et lis `total_results` (vérifie le nom exact du champ à la première requête). L'API plafonne à
  10 000 résultats : découpe par département. Si tu utilises la NAF 2025, note-le.
- Aucun chiffre inventé : source manquante = [HYPOTHÈSE].

## Étape 3 : filtre marché et premier point d'arrêt

Applique les seuils éliminatoires de `CLAUDE.md`. Classe les survivants avec un score marché :
taille 30 %, croissance 30 %, fragmentation 20 %, récurrence de la dépense 10 %, accès aux clients 10 %.
Garde les 8 meilleurs et écris dans `marches.md` le tableau classé, les fiches, puis la liste des
marchés éliminés avec leur motif (une ligne chacun).

**Point d'arrêt 1.** Affiche les 8 marchés (taille, croissance, confiance, modèle d'exécution,
contre-preuve en une ligne) et demande à l'utilisateur d'en choisir 3 à 5. S'il a écrit AUTO ou
demandé un run sans arrêt, garde les 5 premiers et continue.

## Étape 4 : segmentation

Pour chaque marché retenu, produis 10 à 15 segments en croisant **au moins 3 axes** :

1. taille ou profil du client (TPE 1-9 salariés, PME 10-49, foyers par type...) ;
2. sous-secteur fin (code NAF détaillé) ;
3. moment déclencheur d'achat (création, obligation, sinistre, recrutement, déménagement, saison) ;
4. besoin précis (le « job » à accomplir) ;
5. zone (région, ville, type de territoire) ;
6. canal d'achat (direct, via un prescripteur, via une plateforme).

Chaque segment tient en une phrase : *qui, où, quand ils achètent, ce qu'ils achètent aujourd'hui
et à quel prix.* « Les PME » n'est pas un segment ; « les restaurants de 3 à 20 salariés en
Île-de-France qui rouvrent après travaux » en est un.

Note chaque segment de 0 à 10 sur cinq critères, avec ces repères :

| Critère (poids) | 0 | 5 | 10 |
|-----------------|---|---|----|
| Valeur (30 %) | potentiel annuel du segment < 100 k€ | 300 k€ à 1 M€ | > 3 M€ |
| Accessibilité (25 %) | ni liste ni canal | liste constructible, canal à tester | liste gratuite (Sirene) + canal prouvé + contact dans l'équipe |
| Sous-servi (20 %) | leaders spécialisés bien notés | offre générique, avis moyens | personne ne s'adresse à lui, ou plaintes répétées et datées |
| Disposition à payer (15 %) | gratuit ou pas de dépense | dépense existante sur un autre budget | budget dédié, paiement récurrent prouvé |
| Avantage de l'équipe (10 %) | aucun | compétence marketing utile | compétence + secteur connu + contacts |

Le potentiel annuel du segment se calcule : nombre de clients × panier annuel × 10 % de
pénétration réaliste. Montre le calcul. Les bornes sont des repères à ajuster.

**Chemin d'expansion.** Un segment de départ petit est acceptable s'il ouvre 2 ou 3 segments
voisins (même client, même canal, besoin proche). Pour chaque segment finaliste, écris le chemin
(segment 1 → 2 → 3) et le potentiel cumulé. C'est ce qui évite à la fois la niche trop légère et
le marché trop vaste.

Écris dans `segments.md` : le tableau des segments classés par marché, puis le Top 12 global.

## Étape 5 : angles « pareil mais mieux »

Pour les 12 meilleurs segments, propose 1 à 2 angles. Un angle précise **le point exact** où l'on bat
l'acteur en place :

- spécialisation verticale (même service, conçu pour ce seul segment) ;
- délai ou qualité de service ;
- prix ou modèle de prix (abonnement plutôt que commission, forfait plutôt que devis) ;
- cible négligée ;
- confiance, marque ou marketing ;
- zone mal servie ;
- simplification ou regroupement de plusieurs prestataires.

Pour chaque angle, écris : l'offre, le prix, le canal d'acquisition, le MVP testable en moins de
4 semaines, la preuve de faiblesse de l'acteur en place (avec source), **pourquoi le leader ne
répond pas déjà** (ou ne peut pas copier facilement), et **l'économie unitaire en une ligne** (prix,
heures de travail par client et par mois, revenu par heure). Si tu n'as pas de réponse à la question
du leader, écris-le : c'est un risque, pas un détail.

Marque « besoin d'un associé tech » si l'angle exige un développement lourd. Ne l'élimine pas
automatiquement.

## Étape 6 : transmission

Termine `segments.md` par une short-list de 8 couples segment × angle, avec pour chacun le score
détaillé et la ligne « seuils CLAUDE.md » (taille, croissance, SOM, accès, budget). Propose ensuite :

1. `jobs-to-be-done` sur les 3 premiers segments pour formuler le besoin ;
2. `llm-council` avec deux questions : lequel donne des clients payants en 3 mois, et lequel peut
   faire vivre l'équipe à 3 ans ;
3. `market-sizing` (calcul bottom-up d'abord), puis `beachhead-segment` sur le favori.

## Pièges à éviter

- Marché défini par une technologie, ou segment défini par un seul axe.
- Taille du marché mondial présentée comme taille française.
- Plateforme de mise en relation sans plan pour attirer l'offre et la demande en même temps
  (cimetière v2 : Cyclofix, Homejoy, Helpling Pays-Bas, BnbSitter).
- « Une agence locale de plus » (ménage, dépannage, garde, marketing pour artisans) : métier
  d'employeur à marge fine, sans avantage défendable. Elle doit prouver qu'elle passe le seuil de SOM
  et pourquoi elle est difficile à copier, sinon elle reste en réserve de la piste rapide.
- Actifs lourds ou économie unitaire négative (cimetière v2 : quick commerce, Frichti, Cityscoot,
  Lavoir Moderne).
- Idée copiée d'un SaaS américain alors que l'équipe ne code pas : marque-la, ne la cache pas.
- Croissance annoncée sans moteur identifiable. Pas de moteur, pas de confiance forte.
- Obligation réglementaire non vérifiée sur source officielle (beaucoup sont reportées).
- Contre-preuve oubliée. Une fiche sans contre-preuve est incomplète.
