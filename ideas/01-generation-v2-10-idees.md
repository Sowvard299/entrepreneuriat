# 10 idées de startup, v2 : des remix ciblés (09/10/2026)

Cette v2 remplace `00-generation-10-idees.md`. Le reproche fait à la v1 (« des idées au
hasard ») était juste : elle partait de secteurs pris un par un, sans méthode pour qu'une idée
soit *forte*. Ici, chaque idée est **construite** pour cocher les critères qui font monter la
note, puis vérifiée par quelques recherches web.

## La méthode : 3 leviers de remix + 1 filtre équipe

Chaque idée combine au moins deux leviers :

1. **Un modèle qui a fait ses preuves ailleurs**, transposé à un marché français qui n'en
   bénéficie pas encore (autre pays, autre taille de client, autre secteur).
2. **Un déclencheur 2025-2026** qui crée une douleur *maintenant* : échéance légale déjà
   passée, baisse de subventions, nouveau risque de contrôle.
3. **Un modèle économique au résultat** (commission sur l'argent récupéré, prix au contrat
   signé, prix au lead) : le client n'a pas besoin de budget pour dire oui, ce qui fait monter
   les notes de budget et de distribution.

Le **filtre équipe** : un accès direct aux clients (alternance, énergie), le marketing comme
moteur de distribution, et un MVP faisable « à la main » par 6 personnes à temps partiel
avant d'écrire du code.

Même grille que la v1 (douleur 25 %, budget 20 %, faisabilité 20 %, MVP 15 %,
distribution 10 %, différenciation 10 %).

## Classement

| # | Idée | Formule du remix | Note |
|---|---|---|---|
| 1 | **Mémoire Gagnant** : IA qui rédige les mémoires techniques des PME à partir de *leurs* chantiers | Outils américains de réponse aux appels d'offres (Loopio, Responsive) × marchés publics français × jurisprudence contre les mémoires génériques | **7,55** |
| 2 | **Alterno** : placement d'alternants payé au contrat signé, avec le logement inclus | Recrutement au succès × crise de financement des CFA × bail mobilité | **7,50** |
| 3 | **Foncier Solaire** : détection par satellite des parkings non conformes à la loi APER, vendue aux développeurs solaires | Prospection immobilière par données satellite × échéance légale passée en juillet 2026 | **7,45** |
| 4 | **Récup'** : récupération de l'argent trop payé par les TPE, rémunérée au succès | Cabinets d'optimisation des coûts pour grands comptes (Ayming, Lowendalmasaï) × IA pour descendre aux TPE | **7,30** |
| 5 | **Fissure** : défenseur des sinistrés de la sécheresse face aux assureurs | « Public adjusters » américains (payés au % de l'indemnité) × catastrophes naturelles sécheresse en France | **7,05** |
| 6 | **FicheNet** : réseau partagé des fiches techniques agroalimentaires | FicheProd (v1) + effet de réseau fournisseurs → fabricants → distributeurs | **7,05** |
| 7 | **Bouclier IDEL** : pré-contrôle CPAM pour infirmiers libéraux | Audit de facturation médicale (AKASA, Fathom aux États-Unis) × peur des indus par extrapolation | **7,00** |
| 8 | **Fournée** : prévision de production pour boulangeries, distribuée par les meuniers | Outils anti-gaspillage existants × canal B2B2B des meuniers, qui paient pour fidéliser leurs boulangers | **6,95** |
| 9 | **PMO Express** : gestion clé en main de l'autoconsommation collective | Énergie communautaire × communes et bailleurs sociaux | **6,65** |
| 10 | **(bonus audacieux) Flex TPE** : un « Voltalis » pour commerces | Effacement électrique (Voltalis chez les particuliers, Flexcity pour l'industrie) × segment TPE délaissé × heures creuses déplacées en journée | **6,15** |

La moyenne passe de **5,9 (v1) à 7,1**, et la meilleure idée de 6,80 à 7,55.

**Pourquoi aucune idée ne dépasse 8 :** sur cette grille, 8+ suppose une douleur
« prête à payer aujourd'hui » *prouvée*. Une note supérieure à 8 sur le papier serait gonflée. Les
notes montent pour de vrai avec des preuves terrain : 10 entretiens qui confirment la douleur
et un client qui paie une version faite à la main valent +1 à +1,5 point sur la douleur et le
budget.

---

## 1. Mémoire Gagnant : 7,55

> 🔄 **Mise à jour du 09/10 (veille) :** le marché du logiciel est encombré (Tenderbolt, Maître AO, Olra, Remporte, Smart BTP...). Seul angle restant : un service « fait pour vous » dans un secteur précis, face à des consultants à 2 500–4 000 €. Voir [`memoire-gagnant/veille-marche.md`](memoire-gagnant/veille-marche.md).

- **Problème :** dans un appel d'offres public, le mémoire technique pèse souvent le plus
  dans la note. Les PME (BTP, nettoyage, espaces verts, informatique) le rédigent dans
  l'urgence ou paient un consultant ou un freelance. Les juges sanctionnent désormais les
  mémoires génériques : le TA de Paris (5 janvier 2024) a jugé que même une forte expérience
  ne compense pas un mémoire imprécis.
- **Le remix :** les outils de réponse aux appels d'offres des grandes entreprises
  américaines (Loopio, Responsive) n'ont pas d'équivalent pour les PME françaises.
  **L'angle qui le rend défendable :** l'outil se nourrit des données *propres* à la PME
  (références de chantiers, photos, CV, moyens matériels, mémoires gagnants et perdants avec
  les notes obtenues), ce qui est exactement l'inverse du « générique » sanctionné par les
  juges.
- **Fonctionnement :** l'outil lit le dossier de consultation et ses critères de notation,
  puis produit un plan calqué sur ces critères et une première version à partir des données
  de la PME. **Un humain valide.** Après la décision, l'outil analyse les notes obtenues pour
  améliorer les mémoires suivants.
- **MVP :** une seule cible (second œuvre BTP ou propreté), un mémoire produit en 48 h,
  **à la main avec assistance IA** au début (service), puis automatisé.
- **Modèle :** 300 à 900 € par mémoire, ou un abonnement de 150 à 400 €/mois. Les
  consultants facturent ce travail plusieurs centaines à quelques milliers d'euros.
- **Concurrence :** des freelances (Malt, ComeUp), des cabinets de conseil, des formations,
  des logiciels de mémoire pour le BTP et de l'IA sur mesure (Tensoria). La recherche n'a
  pas trouvé de produit PME dominant.
- **Ce qui pourrait faire chuter la note :** une concurrence IA qui arrive vite, et des
  plateformes de veille d'appels d'offres qui ajoutent la rédaction.

| Douleur 8 | Budget 8 | Faisabilité 8 | MVP 7 | Distribution 6 | Différenciation 7 |
|---|---|---|---|---|---|

## 2. Alterno : placement d'alternants au succès, logement inclus — 7,50

> 🔄 **Mise à jour du 09/10 (veille) :** les logiciels de placement pour CFA existent (Linkpick, Pyramide, OSCAR). En revanche, aucun placement payé au contrat signé ni aucune colocation alternée n'ont été trouvés. La règle des 3 mois sans contrat rend la douleur maximale de décembre à janvier. Voir [`alterno/veille-marche.md`](alterno/veille-marche.md).

- **Déclencheur 2026 :** depuis mars 2026, l'aide à l'embauche est limitée à 2 000 € en PME
  et 750 € en grande entreprise pour les licences et masters. France compétences a révisé
  les niveaux de prise en charge des CFA en avril 2026 (baisse de 8 à 20 % pour de nombreux
  métiers). Les contrats ont reculé d'environ 5 % en 2025. **Moins d'entreprises recrutent,
  alors que chaque contrat non signé est un financement perdu pour le CFA.** (Attention :
  un communiqué du Medef de juillet 2026 annonce un maintien des aides ; c'est à vérifier.)
- **Le remix :**
  1. **Prix au contrat signé**, payé par le CFA : l'outil est payé seulement si le contrat
     est signé, ce qui revient à un tarif de cabinet de recrutement au succès. Comme le CFA
     n'est financé que si le contrat existe, le ROI est évident. Le placement est gratuit
     pour l'étudiant, comme la loi l'impose.
  2. **Logement en rythme alterné :** un alternant au rythme « 1 semaine école / 3 semaines
     entreprise » paie souvent deux logements. Alterno associe deux alternants aux rythmes
     opposés sur un même logement (bail mobilité de la loi ELAN, ouvert aux apprentis), en
     complément de l'aide Mobili-Jeune d'Action Logement. Le logement est une raison majeure
     de refuser une offre éloignée : c'est **le différenciateur que personne d'autre n'a**.
- **MVP :** **sans code**. Les 6 membres de l'équipe font eux-mêmes le placement pour 1 ou 2
  CFA partenaires (tableur, LinkedIn, offres publiques), puis automatisent ce qui se répète.
- **Atout équipe :** vous êtes **vous-mêmes des alternants en master** : accès direct aux
  écoles, crédibilité et connaissance des souffrances de l'intérieur.
- **Concurrence :** les jobboards (Walt, Hellowork, JobTeaser), qui ne garantissent rien au
  CFA, les ERP de CFA (Ypareo), qui ne prospectent pas, et les chargés de relations
  entreprises en interne.
- **Ce qui pourrait faire chuter la note :** les CFA, dont la trésorerie est sous tension
  (marge passée de 11 % en 2021 à 5,1 % en 2024), pourraient négocier le prix. La partie
  logement ajoute aussi un risque juridique et de confiance (cautions, assurances).

| Douleur 8 | Budget 7 | Faisabilité 7 | MVP 8 | Distribution 8 | Différenciation 7 |
|---|---|---|---|---|---|

## 3. Foncier Solaire : la loi APER vue par satellite — 7,45

> ⚠️ **Correction du 09/10 (veille) :** la loi Huwart (26/11/2025) a ramené l'obligation à **17,5 %** de panneaux solaires, et des reports d'échéance existent. Des outils de prospection avec les propriétaires existent déjà (module Prospection de Cadastre solaire). Note réestimée : **environ 6,0**. Voir [`foncier-solaire/veille-marche.md`](foncier-solaire/veille-marche.md).

- **Déclencheur :** la loi APER (10 mars 2023, décret 2024-1023) impose de couvrir **au
  moins 50 %** des parkings extérieurs de plus de 1 500 m² avec des ombrières solaires. Les
  échéances sont **le 1er juillet 2026** pour ceux de plus de 10 000 m² (**déjà passée**) et le
  1er juillet 2028 pour ceux de 1 500 à 10 000 m². Selon une source, seuls 10 à 15 % des
  grands parkings étaient équipés ou en cours d'équipement. Les sanctions annoncées vont
  jusqu'à 20 000 € par an et par tranche de 500 m² non couverte (montant à vérifier sur
  Légifrance).
- **Le remix :** la prospection immobilière par données (orthophotos IGN et cadastre, en
  données ouvertes) appliquée à une obligation légale. Un modèle de vision par ordinateur
  détecte les parkings, mesure leur surface et vérifie s'ils sont déjà équipés. L'outil
  croise ensuite avec le propriétaire, la distance au réseau électrique et les exemptions.
- **Qui paie :** **les développeurs solaires**, pour qui trouver du foncier est le premier
  goulot d'étranglement. Ils achètent des listes de sites qualifiés ou paient une commission
  par projet signé. Les propriétaires reçoivent gratuitement un diagnostic de conformité, ce
  qui sert de produit d'appel.
- **Extension :** les toitures, puis les **terres agricoles en agrivoltaïsme** (les mêmes
  développeurs achètent), pour devenir *la* place de marché du foncier solaire.
- **MVP :** une région, une liste qualifiée de 200 parkings non conformes, vendue à 3
  développeurs. Faisable en quelques semaines avec des outils de géomatique ouverts (QGIS) et
  un modèle de détection pré-entraîné.
- **Atout équipe :** l'énergie, et le côté technologique et « deeptech légère ».
- **Ce qui pourrait faire chuter la note :** un report ou un assouplissement de la loi (la
  grande distribution le demande), des développeurs qui ont déjà ce type de données en
  interne ou par des prestataires de géodonnées, et la nécessité de vérifier le conflit
  d'intérêts avec EDF (EDF Renouvelables est un développeur).

| Douleur 8 | Budget 8 | Faisabilité 8 | MVP 7 | Distribution 6 | Différenciation 6 |
|---|---|---|---|---|---|

## 4. Récup' : l'argent que les TPE paient en trop — 7,30

- **Le remix :** Ayming ou Lowendalmasaï récupèrent les trop-payés des grandes entreprises
  (énergie, taxes, télécoms, achats) contre un pourcentage. Les TPE ne sont pas servies, car
  l'audit humain coûte trop cher pour les petits montants. **L'IA rend l'audit quasi gratuit**,
  ce qui permet de descendre jusqu'aux 4 millions de TPE.
- **Ce qu'on audite :** les factures d'énergie (puissance souscrite surdimensionnée, erreurs
  d'acheminement, éligibilité au tarif réglementé), les télécoms (lignes fantômes), les frais
  bancaires, la CFE (dégrèvements) et les assurances en doublon.
- **Modèle :** **0 € d'avance, 30 à 50 % des sommes récupérées ou économisées** la première
  année. Le « oui » est facile.
- **Distribution :** les experts-comptables (qui ont les factures et cherchent des services à
  valeur ajoutée), plus le bouche-à-oreille entre commerçants.
- **Atout équipe :** l'audit énergie, le métier du fondateur. ⚠️ Il faut vérifier les
  clauses du contrat chez EDF (loyauté, non-concurrence) et ne jamais utiliser d'information
  interne.
- **Ce qui pourrait faire chuter la note :** des petits montants par client (il faut un
  traitement très automatisé), et l'image des « chasseurs de primes » qu'il faudra éviter
  (transparence totale).

| Douleur 7 | Budget 7 | Faisabilité 8 | MVP 7 | Distribution 8 | Différenciation 7 |
|---|---|---|---|---|---|

## 5. Fissure : défendre les sinistrés de la sécheresse — 7,05 (B2C)

- **Problème :** environ 10 millions de maisons sont exposées au retrait-gonflement des
  argiles. Après une sécheresse, les façades se fissurent (des dizaines de milliers d'euros
  de réparations). Mais il faut un arrêté de catastrophe naturelle pour la commune, puis une
  expertise contradictoire face à l'expert de l'assureur. Les refus sont fréquents, et les
  particuliers sont seuls et démunis.
- **Le remix :** aux États-Unis, les « public adjusters » défendent l'assuré contre un
  pourcentage de l'indemnité. En France, les « experts d'assurés » existent mais sont
  artisanaux et invisibles en ligne. Fissure ajoute l'IA (analyse des photos de fissures,
  vérification des arrêtés, données météo et géologiques, constitution du dossier) et un
  **réseau d'experts partenaires**.
- **Modèle :** un dossier de pré-analyse à 49–99 €, puis 8 à 12 % de l'indemnité obtenue.
- **Distribution :** le référencement naturel sur des recherches désespérées (« fissure
  sécheresse refus assurance »), les groupes et associations de sinistrés, les mairies.
- **Ce qui pourrait faire chuter la note :** les délais longs (des mois avant d'être payé),
  le besoin de vrais experts du bâtiment, et la réglementation (il faut vérifier le cadre
  juridique des honoraires de résultat et de la représentation de l'assuré).

| Douleur 9 | Budget 7 | Faisabilité 6 | MVP 6 | Distribution 7 | Différenciation 6 |
|---|---|---|---|---|---|

## 6. FicheNet : le réseau des fiches techniques agro — 7,05

- **Évolution de FicheProd (v1) :** le même problème (fiches techniques, allergènes,
  étiquetage INCO), mais avec un **effet de réseau**. Un fournisseur publie sa fiche une
  seule fois, et tous ses clients fabricants la reçoivent à jour. Le fabricant génère ses
  propres fiches, qu'il partage à ses distributeurs (épiceries fines, grossistes,
  restauration). Chaque demande de fiche envoie une **invitation** sur la plateforme.
- **Le remix :** Alkemics (devenu Salsify) l'a fait pour les grandes marques et la grande
  distribution, mais personne ne l'a fait pour les TPE et PME, ni pour leurs petits clients.
- **Pourquoi la note monte par rapport à la v1 :** distribution 6 → 8 (boucle d'invitation
  virale) et différenciation 6 → 8 (le réseau est difficile à copier).
- **Ce qui pourrait faire chuter la note :** un MVP plus dur (il faut que l'outil soit utile
  même pour un seul utilisateur au départ), et la responsabilité juridique sur les allergènes
  (validation humaine obligatoire).

| Douleur 7 | Budget 6 | Faisabilité 8 | MVP 6 | Distribution 8 | Différenciation 8 |
|---|---|---|---|---|---|

## 7. Bouclier IDEL : pré-contrôle CPAM pour infirmiers libéraux — 7,00

- **Déclencheur :** l'article 102 de la loi de financement de la Sécurité sociale (LFSS) pour
  2023 permet à la CPAM de réclamer des **trop-perçus (indus) par extrapolation** sur toute
  l'activité, à partir des anomalies relevées lors d'un contrôle (état d'application à
  vérifier). Les infirmiers libéraux le vivent comme une menace sur leur cabinet. Les
  cotations de la nomenclature (NGAP) changent avec les avenants 2025-2027, et une cotation
  non justifiée dans le dossier de soins suffit à faire rejeter une facture.
- **Le remix :** l'audit de facturation médicale par IA est un marché en forte croissance
  aux États-Unis (AKASA, Fathom), mais personne ne vise les libéraux français. Fonctionnement :
  l'infirmier importe ses exports de facturation et les retours de rejets, l'outil détecte les
  cotations à risque, les justificatifs manquants et les actes sous-cotés (de l'argent
  perdu), puis prépare un dossier en cas de contrôle.
- **Modèle :** 29 à 49 €/mois. C'est une « assurance tranquillité », vendable par la peur et
  par l'argent récupéré.
- **Distribution :** les infirmiers libéraux ont des communautés en ligne très actives
  (groupes Facebook, forums), ce qui permet une croissance par bouche-à-oreille.
- **Ce qui pourrait faire chuter la note :** données de santé (hébergement certifié HDS
  obligatoire, ce qui alourdit le MVP), éditeurs de logiciels de facturation qui ajoutent ce
  contrôle, et le risque d'être perçu comme une aide à la « sur-cotation » (il faut un
  positionnement conformité strict).

| Douleur 9 | Budget 6 | Faisabilité 7 | MVP 5 | Distribution 8 | Différenciation 6 |
|---|---|---|---|---|---|

## 8. Fournée : prévision de production pour boulangeries, via les meuniers — 6,95

- **Constat de la recherche :** la prévision anti-gaspillage pour boulangeries **existe
  déjà** : Inpulse (utilisé par L'Atelier Papilles, 28 boulangeries), Fullsoon, Helean (réseau
  Ange) et Go Nina en Suisse. Une idée « logiciel de plus » plafonnerait vers 6.
- **Le remix qui change la note :** les ~30 000 boulangeries artisanales ne sont pas
  équipées, et le canal idéal, ce sont **les meuniers**. Ils se battent pour la fidélité des
  boulangers et financent déjà des services (formation, marketing, aide à l'installation).
  Fournée est vendue **au meunier** en marque blanche, et le meunier l'offre à ses clients
  boulangers. Un contrat signé donne accès à des centaines ou des milliers de boulangeries.
- **Ce qui pourrait faire chuter la note :** les meuniers pourraient préférer un partenariat
  avec Inpulse ou Fullsoon, il faut une intégration avec les caisses enregistreuses, et
  certains boulangers se méfient de l'IA (23 % des franchisés Ange la voient comme une
  menace).

| Douleur 7 | Budget 7 | Faisabilité 8 | MVP 6 | Distribution 8 | Différenciation 5 |
|---|---|---|---|---|---|

## 9. PMO Express : l'autoconsommation collective clé en main — 6,65

- **Problème :** les communes, les bailleurs sociaux et les zones d'activité montent des
  opérations d'autoconsommation collective (des panneaux solaires partagés entre voisins).
  Mais la « personne morale organisatrice » (PMO) doit gérer les conventions avec Enedis, la
  répartition de l'énergie produite entre les membres, les entrées et sorties des
  participants et la facturation. Ce travail repose souvent sur des bénévoles et fait échouer
  des projets.
- **Le remix :** un « syndic » de l'énergie partagée. Le service gère tout pour un forfait par
  participant ou un pourcentage des flux d'énergie.
- **Concurrence :** des acteurs spécialisés existent déjà (Enogrid, par exemple). L'angle
  serait les petites opérations rurales, mal servies.
- **Atout équipe :** l'expertise énergie. Le conflit d'intérêts avec EDF est plus faible,
  mais reste à vérifier.

| Douleur 7 | Budget 6 | Faisabilité 7 | MVP 6 | Distribution 7 | Différenciation 6 |
|---|---|---|---|---|---|

## 10. (Bonus audacieux) Flex TPE : un Voltalis pour commerces — 6,15

- **Idée :** un boîtier pilote le froid, les chauffe-eau et le chauffage des commerces pour
  déplacer la consommation vers les nouvelles heures creuses en journée (le TURPE 7, le tarif
  d'acheminement, déplace progressivement une partie des heures creuses l'après-midi) et
  vendre de l'effacement sur les marchés. C'est **gratuit pour le commerçant**, la
  rémunération vient du marché de la flexibilité.
- **Pourquoi la note est plus basse :** du matériel, un accès aux marchés de l'électricité et
  un MVP long (MVP 3/10). C'est le pari « deeptech à fort potentiel » de la liste, et
  l'idée la plus exposée au conflit d'intérêts avec EDF.

| Douleur 6 | Budget 7 | Faisabilité 7 | MVP 3 | Distribution 6 | Différenciation 8 |
|---|---|---|---|---|---|

---

## Synthèse

- **Meilleure note :** #1 Mémoire Gagnant (7,55).
- **Meilleur avantage équipe :** #2 Alterno. Vous êtes la cible, le MVP est faisable sans
  code dès ce mois-ci, et le logement en rythme alterné est un vrai différenciateur.
- **La plus innovante :** #3 Foncier Solaire. Elle utilise la donnée satellite face à une
  obligation légale dont l'échéance est déjà passée, et le marché qui paie (les développeurs)
  a de gros budgets.
- **Le meilleur oui facile :** #4 Récup' (0 € d'avance).
- **La meilleure idée grand public :** #5 Fissure.

**Recommandation :** pré-sélectionner **#2 Alterno, #1 Mémoire Gagnant et #3 Foncier
Solaire**, puis les confronter avec `llm-council`. Ensuite, faire 10 entretiens `mom-test`
sur la gagnante avant toute ligne de code.

## Sources consultées (recherche du 09/10/2026)

- Mémoire technique : [Tensoria](https://tensoria.fr/blog/logiciel-memoire-technique-vs-ia-sur-mesure), [marche-public.fr (jurisprudence sur la notation)](https://www.marche-public.fr/contrats-publics/memoire-technique-jp-notation-acheteurs.htm)
- Loi APER : [photovoltaique.info](https://www.photovoltaique.info/fr/preparer-un-projet/quel-type-de-projet/obligations-de-solarisation/obligation-de-solarisation-des-parcs-de-stationnement-exterieurs/), [Connaissance des énergies](https://www.connaissancedesenergies.org/afp/ombrieres-photovoltaiques-sur-les-parkings-la-grande-distribution-demande-une-reglementation-realiste-260702), [swim.legal](https://www.swim.legal/blog/ombriere-solaire-parking-obligations-entreprises)
- Apprentissage : [L'Essentiel de l'éco](https://lessentieldeleco.fr/8060-coup-de-rabot-sur-lapprentissage-un-freinage-budgetaire-au-pire-moment/), [Assemblée nationale, compte rendu](https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion_fin/l17cion_fin2526116_compte-rendu.pdf), [Medef Gard](https://www.gard.territoriaux.medef.com/communiques-de-presse-download/apprentissage-un-dispositif-essentiel-pour-les-competences-des-jeunes-est-preserve)
- Boulangerie : [Inpulse (presseagence)](https://presseagence.fr/paris-inpulse-la-startup-qui-aide-les-restaurants-et-les-boulangeries-a-reduire-le-gaspillage-alimentaire/), [L'Express Franchise (Ange)](https://lexpress-franchise.com/articles/de-lia-dans-vos-baguettes-les-boulangeries-ange-innovent/), [Swissinfo (Go Nina)](https://www.swissinfo.ch/fre/le-meilleur-du-contenu-ssr/une-ia-r%c3%a9duit-le-gaspillage-alimentaire-dans-les-boulangeries-suisses/91230416)
- Infirmiers libéraux : [Question parlementaire sur les indus](https://www2.assemblee-nationale.fr/questions/detail/16/qe/8500/(vue)/pdf), [La Ruche (CBA), erreurs de facturation](https://laruche.cbainfo.fr/gerer-cabinet-infirmier/facturation-idel/erreurs-facturation-idel/)
- Saisonniers agricoles (idée écartée : WiziFarm gratuit et soutenu par l'État, Ohmyseason) : [Terre-net](https://www.terre-net.fr/actualite-agricole/economie-social/article/moins-de-900-missions-pour-plus-de-300-000-candidats-202-168698.html), [L'Essentiel de l'éco](https://lessentieldeleco.fr/4491-ohmyseason/)

Les autres chiffres (nombre de TPE, de maisons exposées aux argiles, de boulangeries) sont
des ordres de grandeur de mémoire, **à vérifier**.
