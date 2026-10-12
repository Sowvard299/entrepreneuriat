# Décision finale du 12/10/2026 : on part sur les Façonniers alimentaires

> **Contexte :** l'équipe doit choisir son idée finale aujourd'hui. Ce choix **remplace le gel
> du plan** décidé par le council n°3 (qui prévoyait de décider le 31 octobre). Le 31 octobre
> devient un **point de pilotage *à l'intérieur* de l'idée retenue** (on ajuste l'angle), plus
> un nouveau choix entre plusieurs idées.
>
> **Honnêteté :** c'est un choix fait **sans entretien client**. Il repose sur la veille web, les
> 3 councils et les 4 tours de challenge. Il est donc fiable sur ce qui *n'existe pas encore*
> (concurrents, obstacles juridiques), mais pas encore sur le fait que des clients paieront.

## 0. Niveau de confiance (règles de conseil du 12/10)

**L'essentiel de ce qui fait gagner cette idée est encore [Guessing].** Ce qui est solide, c'est
surtout ce qui élimine les autres idées.

| Affirmation | Confiance | Sur quoi elle repose |
|---|---|---|
| Aucun client n'a été interrogé, pour aucune des idées | [Certain] | Historique du projet |
| Aucune plateforme française de mise en relation entre marques et façonniers | [Likely] | 3 séries de recherches web sans résultat. Une absence de preuve n'est pas une preuve d'absence |
| PartnerSlate a levé 4 M$ en amorçage (2023) avec environ 6 000 fabricants | [Certain] | Presse spécialisée (FoodNavigator-USA, BevNET) |
| Le marché est modeste, même aux États-Unis (seulement 4 M$ levés) | [Likely] | Déduction à partir de la levée |
| Les jeunes marques souffrent assez pour payer environ 1 000 € | [Guessing] | Aucune donnée. C'est l'hypothèse n°1 à tester |
| Le prix de 900 à 1 500 € | [Guessing] | Aucun prix de référence trouvé |
| Un paiement d'avance par la marque évite le contournement | [Likely] | Logique du modèle, pas encore observée |
| Une partie des façonniers accepte les petits projets bien préparés | [Guessing] | Non testé : c'est la question qui peut tuer l'idée |
| La protection juridique de l'assurance professionnelle couvre souvent la défense des infirmiers face à un contrôle CPAM | [Likely] | Plusieurs sources disent « souvent ». Cela dépend des contrats |
| On ne sait pas si un CFA peut payer un prestataire au contrat signé | [Certain] | Aucune source trouvée. Question envoyée par écrit |
| Les compétences des 5 autres membres sont inconnues | [Certain] | Toujours « TODO » dans `CLAUDE.md` |

## 1. La grille de décision

Elle applique les « portes » du système décrit dans
[`../docs/multi-agent-idea-finder.md`](../docs/multi-agent-idea-finder.md), dans cet ordre :
concurrence → faits et obstacles → notation → testabilité → adéquation avec l'équipe.

| Critère | **Façonniers alimentaires** | Alterno (placement d'alternants) | Bouclier IDEL (contrôles CPAM des infirmiers libéraux) |
|---|---|---|---|
| **Concurrence** | ✅ **Ouvert.** Aucune plateforme française de mise en relation trouvée (3 séries de recherches). Les intermédiaires existants sont informels (ARIA), réservés aux adhérents et non outillés | ⚠️ Les logiciels pour CFA existent (Linkpick, Pyramide). Personne ne propose de placement payé au contrat signé, peut-être parce que c'est interdit | ❌ Le contrôle de cotation est déjà intégré aux logiciels de facturation (CareCare, Albus, Agathe YOU). La défense est souvent **déjà payée par la protection juridique de l'assurance professionnelle** (nouveau, vu le 12/10) |
| **Modèle qui a fait ses preuves ailleurs** | ✅ PartnerSlate (États-Unis) : 4 M$ levés, environ 6 000 fabricants référencés | ❌ Aucun | ❌ Aucun |
| **Obstacles juridiques** | 🟡 Faibles et gérables : statut d'apporteur d'affaires, accords de confidentialité, RC pro | ❌ **Non levé** : on ne sait pas si un CFA peut payer au contrat signé, et l'administration ne répondra pas aujourd'hui | ❌ Lourds : données de santé (hébergement HDS), consultation juridique réservée aux avocats, image d'« aide à la fraude » |
| **Conflit avec EDF ou devoir de loyauté** | ✅ Aucun | ✅ Aucun | ✅ Aucun |
| **Solvabilité de celui qui paie** | 🟡 Les jeunes marques sont souvent fauchées, mais les façonniers paient déjà pour trouver des clients (salons, commerciaux) | ❌ Les CFA voient leur marge chuter (5,1 % en 2024) | 🟡 Les infirmiers sont solvables, mais leur défense est déjà financée par l'assurance |
| **Accès de l'équipe aux clients** | 🟡 Pas de réseau direct, mais des listes publiques (exposants, ARIA, data.gouv) et des canaux (incubateurs, pépinières) | ✅ Les écoles des membres, mais il est interdit de démarcher son propre CFA, et cet avantage disparaît au diplôme | ❌ Aucun infirmier dans l'entourage |
| **Adéquation avec l'équipe** | ✅ **Agroalimentaire = intérêt déclaré.** Le marketing sert du côté des marques | 🟡 Vécu personnel, mais pas d'intérêt déclaré | ❌ Aucune |
| **Testable en 3 semaines sans code** | ✅ Oui (service fait à la main + appels) | ❌ Bloqué par la réponse juridique | 🟡 Oui, mais des entretiens délicats |
| **Potentiel** | ✅ Une base des capacités de production, puis des services, puis l'Europe | 🟡 Un cabinet de recrutement | 🟡 Une niche |
| **Verdict** | **✅ RETENU** | **⏸️ EN ATTENTE** (l'e-mail juridique part quand même, il ne coûte rien) | **❌ ABANDONNÉ** |

**Pourquoi le revirement « IDEL en tête » du council n°3 est définitivement écarté :** le
seul fait nouveau va **contre** IDEL. La protection juridique incluse dans l'assurance
professionnelle des infirmiers finance déjà l'avocat lors d'un contrôle.

## 2. L'idée retenue, en une phrase

> **« Une jeune marque alimentaire nous paie pour trouver, en 4 semaines, le bon fabricant
> pour produire ses premiers milliers d'unités, avec un dossier prêt à envoyer (cahier des
> charges, volumes, certifications) et des façonniers déjà qualifiés. »**

- **Qui paie :** la **jeune marque** qui sort de la pré-série (laboratoire d'école, CTCPA, atelier
  partagé, pépinière comme Ma Première Usine) et doit passer à une production régulière. C'est
  elle qui souffre le plus, et c'est elle qui paie. Ce choix répond à l'objection du Penseur des
  premiers principes.
- **Ce qu'elle achète :** du temps et un lancement qui n'est pas retardé. On lui livre une liste
  courte de 3 façonniers qualifiés, déjà contactés, avec un dossier projet propre.
- **Côté façonniers :** l'inscription est **gratuite** au début. Ils reçoivent des projets *préparés*,
  ce qui répond à leur crainte des petits projets flous. On les fera payer plus tard
  (abonnement ou commission), quand le volume de projets sera prouvé.
- **L'actif à long terme :** la **base des capacités de production** (qui fabrique quoi, à partir
  de quel volume minimum, avec quelles certifications). C'est la proposition de l'Expansionniste,
  mais on la construit **en faisant le service**, pas avant.
- **Prix de départ, à tester (hypothèse) :** un forfait de **900 à 1 500 €** par projet, avec un
  acompte. **Aucun prix de référence trouvé en ligne** pour ce service : c'est la première chose
  à valider.

**Pourquoi cet angle plutôt que la place de marché à commission :** il évite les trois
faiblesses relevées par les councils :
- la commission unique sur de petites séries ;
- le contournement (les deux parties traitent ensuite sans nous) ;
- le refus des petits projets par les façonniers.

En effet, la marque paie d'avance pour un travail qui a de la valeur même si elle traite ensuite
directement avec le façonnier.

## 3. Les risques qui restent (à tester en premier)

| # | Hypothèse | Si elle est fausse | Test |
|---|---|---|---|
| 1 | **Les jeunes marques souffrent assez pour payer environ 1 000 €** (temps perdu, lancement retardé, déjà payé un consultant ou un ingénieur) | On change de payeur : les façonniers (abonnement pour recevoir des projets) ou les structures (outil pour les ARIA) | 10 marques interrogées, et **2 acomptes** avant le 31 octobre |
| 2 | **Au moins une partie des façonniers accepte les petits projets bien préparés** | On ne peut rien livrer. Il faut alors viser les pépinières de production et les ateliers partagés | 8 façonniers interrogés : « votre dernier petit projet accepté ou refusé ? » |
| 3 | Les intermédiaires gratuits (ARIA, CCI, incubateurs) ne font pas déjà ce travail de façon satisfaisante | Ils deviennent le canal de distribution, ou le client (outil en marque blanche) | 3 appels avant le 23 octobre |
| 4 | Le besoin revient assez souvent pour faire vivre une entreprise | On élargit aux boissons, aux compléments alimentaires et aux cosmétiques, ou on passe à un abonnement | Compter les projets par marque sur 3 ans |

## 4. Plan des 3 prochaines semaines (les 6 membres sur une seule idée)

| Rôle | Nb | Livrable au 31 octobre |
|---|---|---|
| Base de façonniers : exposants du SIAL qui fabriquent pour d'autres marques (MDD, sous-traitance), annuaires des ARIA, pépinières, data.gouv filtré à la main | 1 | 60 façonniers qualifiés (catégorie, volume minimum, certifications, contact) |
| Entretiens et prévente auprès des jeunes marques (incubateurs, Shakeup Factory, Vitagora, Ma Première Usine, épiceries fines, LinkedIn) | 2 | 10 entretiens et **au moins 2 acomptes ou lettres d'intention** |
| Entretiens façonniers (e-mail ou LinkedIn d'abord, puis appel, uniquement sur des créneaux hors travail) | 2 | 8 entretiens, réponse à la question des petits projets |
| Structures (AgroAlia, ARIA, Vitagora ou Valorial) + e-mail Alterno + administratif (statut, accord de confidentialité type) | 1 | 3 appels, e-mail Alterno envoyé |

**Point de pilotage du 31 octobre** (on ne choisit pas une autre idée, on ajuste celle-ci) :

| Résultat | Action |
|---|---|
| Au moins 2 acomptes et au moins 3 façonniers sur 8 qui acceptent les petits projets | ✅ On continue : on livre les 2 projets à la main et on documente chaque étape (ce sera le futur produit) |
| Des marques intéressées mais 0 acompte | 🔄 On teste un prix plus bas ou un autre payeur (les façonniers paient pour recevoir des projets) |
| Les façonniers refusent les petits projets | 🔄 On cible les pépinières de production et ateliers partagés, et les marques qui en sortent |
| Les structures font déjà le travail | 🔄 Elles deviennent clientes ou canal (outil en marque blanche pour les ARIA) |
| Rien de tout cela | ❌ On revient à la grille « problèmes vus en alternance » (déjà prévue) |

## 5. Ce qui a été écarté, et pourquoi (pour ne pas y revenir)

- **Mémoire Gagnant :** marché saturé de logiciels (Tenderbolt, Maître AO, Olra...).
- **Foncier Solaire :** obligation réduite à 17,5 % par la loi Huwart, Cadastre solaire existe déjà, conflit avec EDF.
- **Bouclier IDEL :** déjà couvert par les logiciels de facturation et par la protection juridique des assurances professionnelles, données de santé.
- **Alterno :** en attente de la réponse juridique, jamais prioritaire. On le relance seulement si une réponse écrite favorable arrive **et** que les Façonniers échouent.
- Les 7 autres idées de la v2 : concurrents installés (voir `02-point-etape-affiner-ou-nouvelles-idees.md`).

## Sources nouvelles (12/10/2026)

- Protection juridique des infirmiers libéraux : [La Ruche CBA : indus CPAM](https://laruche.cbainfo.fr/gerer-cabinet-infirmier/facturation-idel/indus-cpam-idel/), [Le Quotidien du Médecin : panorama des protections juridiques](https://www.lequotidiendumedecin.fr/le-droit-et-vous/quel-est-le-panorama-des-protections-juridiques-des-liberaux), [MACSF : assurances de l'infirmier libéral](https://www.macsf.fr/exercice-liberal/exercer-au-quotidien/assurances-infirmier-liberal), [Caducée : les infirmiers face aux contrôles](https://www.caducee.net/actualite-medicale/16460/reduction-du-gaspillage-ou-facturation-abusive-les-infirmiers-liberaux-pris-au-piege-des-controles-de-la-cpam.html)
- Industrialisation des jeunes marques : [Le Journal des Entreprises : minimiil et Ma Première Usine](https://www.lejournaldesentreprises.com/article/le-clermontois-minimiil-installe-ses-cuves-en-provence-2143739), [LSA : les start-up de l'épicerie sucrée](https://www.lsa-conso.fr/la-course-effrenee-des-start-up-de-l-epicerie-sucree-pour-se-construire-rapidement,461953), [Ministère de l'Agriculture : accélérateur agroalimentaire avec Bpifrance](https://agriculture.gouv.fr/telecharger/96736)
