# Idées v2 : produits qui peuvent grandir

Date : 2026-10-14. Point de départ : les idées de la v1 (`ideas/_recherche/`) ont été jugées trop « petit service ».
Contraintes corrigées par l'équipe : on peut coder ou recruter un développeur, budget au-delà de 5 000 €, ambition startup (levée possible).
Recherche large, France d'abord. Méthode : skill `ai-startup-opportunity-generator` (score sur 10 : douleur 25 %, budget du client 20 %, adéquation logiciel/IA 20 %, simplicité du MVP 15 %, distribution 10 %, différenciation 10 %).

Niveau de preuve : [Certain] = source vérifiée, [Likely] = déduction solide, [Guessing] = à vérifier.

## Classement

| Rang | Idée | Client qui paie | Pourquoi maintenant | Score |
|------|------|-----------------|---------------------|-------|
| 1 | Copilote électricité pour PME | PME de 10 à 250 salariés, multi-sites | Fin de l'ARENH (1er janvier 2026), nouveau mécanisme de capacité sur les factures (1er novembre 2026), décret BACS (1er janvier 2027) | 7,6 |
| 2 | Logiciel de gestion de l'autoconsommation collective | Personnes morales organisatrices (PMO) : installateurs solaires, zones d'activités, collectivités | +129 % d'opérations en 2024, +133 % en 2025, 2 276 opérations fin juin 2026 | 7,2 |
| 3 | Taux EGalim automatique à partir des factures électroniques | Restauration collective privée et publique, sociétés de restauration | Réception des factures électroniques obligatoire depuis septembre 2026 ; seulement environ 30 % des cantines atteignent l'objectif | 7,0 |
| 4 | Conformité EUDR en libre-service pour petits importateurs | Torréfacteurs, chocolatiers, négociants bois et meubles, importateurs de cuir et caoutchouc | Application le 30 décembre 2026 (grandes et moyennes), le 30 juin 2027 (petites et micro) | 6,6 |
| 5 | Copilote de réponse aux appels d'offres pour PME du BTP | PME du BTP et des services | Outils d'IA générative mûrs, 34 % des startups ne répondent pas aux appels d'offres à cause de la complexité | 6,0 |

Écartées après recherche : agent vocal de présélection des candidats (36 solutions en Europe, Maki a levé 26 M€) ; analyse PFAS (métier de laboratoire, pas de logiciel).

## 1. Copilote électricité pour PME (7,6)

- **Problème** [Certain] : depuis la fin de l'ARENH au 1er janvier 2026, les PME sont plus exposées aux prix de marché ; le coût du mécanisme de capacité dépend de la consommation en heures de pointe et apparaît sur les factures à partir du 1er novembre 2026 ; les bâtiments tertiaires de plus de 70 kW doivent avoir une GTB au 1er janvier 2027.
- **Produit** : un logiciel branché sur les données du compteur (API Enedis) qui dit à la PME quoi changer : puissance souscrite, usages à décaler hors pointe, date et forme du prochain contrat, alerte facture anormale. Plus tard : vendre sa flexibilité via un agrégateur (Flexcity, Voltalis) et toucher une part du revenu.
- **Modèle** : abonnement de 30 à 150 € par site et par mois [Guessing], plus une part des économies ou du revenu de flexibilité.
- **Concurrence** [Likely] : courtiers gratuits payés par les fournisseurs (Opera Énergie, Selectra), qui vendent un contrat et pas un pilotage ; Advizeo et Deepki, faits pour les grands parcs immobiliers. Le créneau « PME de 10 à 250 salariés, sans gestionnaire énergie » paraît peu servi.
- **Avantage de l'équipe** : une alternance chez EDF sur les offres électricité pour TPE et PME.
- **Risque n°1** : conflit d'intérêts et clause d'exclusivité avec EDF ; à vérifier dans le contrat d'alternance avant tout. Risque n°2 : la PME ne voit pas l'économie assez vite pour payer un abonnement.

## 2. Logiciel de gestion de l'autoconsommation collective (7,2)

- **Problème** [Certain] : l'électricité solaire partagée entre voisins (entreprises, collectivités, immeubles) explose : 2 276 opérations et plus de 25 000 participants fin juin 2026, nombre d'opérations multiplié par plus de 2 chaque année. Chaque opération a besoin d'une PMO qui répartit l'énergie, facture les participants et gère les entrées et sorties.
- **Produit** : un logiciel tout-en-un pour la PMO : simulation, contrats, clés de répartition, facturation des participants, tableau de bord par participant, recrutement de nouveaux consommateurs dans le rayon autorisé.
- **Modèle** : prix par participant et par mois, ou par opération.
- **Concurrence** [Certain] : Enogrid (fondée en 2018, 2,7 M$ levés, logiciels EnoLab et EnoPower). Le marché est jeune et peu financé.
- **Risque n°1** [Likely] : marché encore petit (une opération moyenne compte 1 à 2 producteurs et environ 10 consommateurs, et la moitié est portée par des collectivités qui achètent lentement) ; il faut parier sur la croissance. Même risque EDF que l'idée 1.

## 3. Taux EGalim automatique à partir des factures électroniques (7,0)

- **Problème** [Certain] : la restauration collective doit servir 50 % de produits durables et de qualité, dont 20 % de bio ; le taux moyen est de 29,5 % et seulement environ 30 % des cantines qui déclarent atteignent le double objectif ; environ 40 % des sites seulement font leur télédéclaration sur « ma cantine ».
- **Produit** : depuis septembre 2026, toutes les entreprises reçoivent des factures électroniques structurées. Le logiciel lit les factures des fournisseurs, classe chaque ligne (bio, label, origine), calcule le taux EGalim en continu, prépare la télédéclaration et propose des substitutions de produits pour atteindre l'objectif.
- **Modèle** : abonnement par cuisine ou par repas servi ; à terme, commission sur les achats auprès de producteurs locaux (lien avec l'intérêt de l'équipe pour l'agroalimentaire).
- **Concurrence** [Guessing] : logiciels de gestion de cuisine (Easilys et d'autres) et outil public gratuit « ma cantine » ; à vérifier en priorité.
- **Risque n°1** : il n'y a pas de sanction, donc la cantine n'est peut-être pas prête à payer (même piège que les copropriétés en v1). Le levier d'achat est plutôt la baisse des coûts d'achat que la conformité.

## 4. Conformité EUDR en libre-service pour petits importateurs (6,6)

- **Problème** [Certain] : le règlement européen contre la déforestation s'applique le 30 décembre 2026 aux grandes et moyennes entreprises et le 30 juin 2027 aux petites et micro (hors bois) ; amende d'au moins 4 % du chiffre d'affaires européen ; la Commission a confirmé en mai 2026 qu'il n'y aurait pas de nouveau report.
- **Produit** : en ligne et en français, l'importateur ajoute ses fournisseurs et les coordonnées des parcelles, l'outil vérifie la déforestation par imagerie satellite et génère la déclaration de diligence raisonnable à déposer sur le système de l'UE.
- **Modèle** : forfait annuel selon le nombre de fournisseurs.
- **Concurrence** [Certain] : osapiens (offre PME « Easy Start », prix sur demande) et de nombreux éditeurs internationaux.
- **Risque n°1** [Likely] : le règlement a déjà été reporté deux fois et allégé (coûts réduits d'environ 75 %), et seul le premier opérateur qui met un produit sur le marché doit déclarer : la cible française est plus petite qu'elle n'en a l'air.

## 5. Copilote de réponse aux appels d'offres pour PME du BTP (6,0)

- **Problème** [Certain] : répondre à un appel d'offres public est long et complexe ; 34 % des startups interrogées en 2021 n'y répondaient pas pour cette raison.
- **Produit** : l'outil lit le dossier de consultation, extrait les exigences, dit s'il faut répondre ou non et rédige un premier jet du mémoire technique à partir des anciennes réponses.
- **Concurrence** [Likely] : déjà occupé (AITenders, Deepbloo et d'autres, dont un projet France 2030). Cette idée n'est gardée que si un membre de l'équipe a un accès privilégié au BTP.

## Ce qu'il faut faire avant de choisir

1. **Vérifier la clause EDF** (idées 1 et 2) : c'est le point qui peut tuer les deux meilleures idées.
2. **Appeler 10 clients par idée** avant d'écrire une ligne de code (skill `mom-test`) : 10 dirigeants de PME pour l'idée 1, 5 PMO et installateurs pour l'idée 2, 10 gérants de cantine pour l'idée 3.
3. Passer les 3 premières au conseil (skill `llm-council`) avec ces retours.

## Sources

- Fin de l'ARENH : [CCI Lyon Métropole](https://www.lyon-metropole.cci.fr/actualite/hausse-prix-electricite-la-fin-de-larenh-pour-les-entreprises), [Hellowatt](https://www.hellowatt.fr/blog/fin-arenh-impact-facture/)
- Mécanisme de capacité : [EDF Entreprises](https://www.edf.fr/entreprises/decryptages/normes-et-reglementations/comprendre-le-mecanisme-de-capacite) ; flexibilité : [baromètre RTE 2026](https://assets.rte-france.com/prod/public/2026-04/2026-04-17-barometre-flexibilite-consommation-principaux-enseignements.pdf), [Voltalis](https://group.voltalis.com/wp-content/uploads/2026/07/Communique-reserve-secondaire-Voltalis_02072026-1.pdf)
- Décret BACS : [CCI Paris Île-de-France](https://www.entreprises.cci-paris-idf.fr/web/transition-ecologique/decret-bacs-pour-des-batiments-tertiaires-plus-intelligents-et-plus-economes-en-energie)
- Autoconsommation collective : [Les Énergies Renouvelables, T1 2026](https://www.les-energies-renouvelables.eu/320-nouvelles-operations-autoconsommation-collective-au-premier-trimestre-2026/), [Conseil d'État et chiffres de juin 2026](https://www.les-energies-renouvelables.eu/article/actualites/reglementations/electricite-partagee-entre-voisins-le-conseil-detat-vient-de-changer-les-regles-1854/), [Enogrid sur CB Insights](https://www.cbinsights.com/company/enogrid)
- EGalim : [ministère de l'Agriculture](https://agriculture.gouv.fr/telecharger/152514), [Acteurs publics](https://acteurspublics.fr/articles/les-administrations-progressent-sur-la-restauration-collective-mais-ne-respectent-toujours-pas-la-loi/)
- EUDR : [Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-deforestation-regulation-commission-publishes-simplification-package-ahead-of-december-2026), [Mayer Brown](https://www.mayerbrown.com/ja/insights/publications/2026/02/eu-regulation-on-deforestation-free-products-eudr-what-lies-ahead-in-2026), [osapiens PME](https://osapiens.com/fr/eudr-for-sme/)
- Appels d'offres : [question parlementaire](https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE4188.pdf), [Deepbloo](https://www.lejournaldesentreprises.com/article/deepbloo-finance-son-pivot-vers-lia-generative-2098436), [Université de Montpellier](https://www.umontpellier.fr/en/articles/intelligence-artificielle-luniversite-de-montpellier-deepbloo-et-aitenders-lancent-une-solution-integree-de-gestion-des-appels-doffres-publics)
- Recrutement par agent vocal (écarté) : [Les Talents Narratifs](https://lestalentsnarratifs.substack.com/p/lia-vocale-une-claque)
