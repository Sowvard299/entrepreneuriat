# Phase 2 : des signaux aux « modèles à améliorer »

Date : 13 octobre 2026. Sources : les 163 signaux de [signaux.md](signaux.md) (IDs F1 à F6).

## Méthode

1. Les signaux sont regroupés par **modèle existant** : qui vend quoi, à qui, à quel prix, et ce qui ne va pas.
2. Chaque modèle reçoit une note de 1 à 5 sur 4 critères du prompt :
   - **A, argent** : preuve que l'argent circule (CA publiés, nombre de clients, avis nombreux, réseaux qui ouvrent) ;
   - **S, sources** : nombre de sites indépendants (1 = un seul site, 5 = 6 sites ou plus) ;
   - **F, faiblesse** : faiblesse prouvée des acteurs en place (avis 1-2 étoiles récents, contrôles, échecs) ; une simple absence d'offre vaut 3 au plus ; un leader bien noté fait baisser la note ;
   - **R, récence** : part des preuves de moins de 24 mois.
3. Total sur 20, puis classement. Les modèles qui ne s'appuient pas sur 3 sites différents sont signalés « < 3 sources » et ne peuvent pas passer en phase 3 sans recherche complémentaire.
4. Pour chaque modèle du top 20 : le job du client avec le skill `jobs-to-be-done` (fonctionnel, émotionnel, social), ce qu'il « embauche » aujourd'hui, et le reproche principal fait à cette solution.

## Classement des 20 modèles les mieux prouvés

| Rang | Modèle existant | A | S | F | R | Total /20 | Signaux clés |
|------|-----------------|---|---|---|---|-----------|--------------|
| 1 | Marketing local par abonnement pour TPE (site, fiche Google, avis, réseaux) | 5 | 5 | 4 | 5 | **19** | F1-05, F1-18, F2-03, F2-13, F2-20, F4-29, F5-03, F5-04, F5-08, F5-26 |
| 2 | Ménage et repassage à domicile en agence déclarée SAP | 5 | 5 | 3 | 5 | **18** | F1-17, F1-19, F2-02, F2-14, F2-24, F4-03, F4-10, F4-28, F5-14, F5-19, F6-19 |
| 3 | Propreté B2B récurrente (petits bureaux, parties communes, fin de chantier) | 5 | 5 | 2 | 5 | **17** | F2-05, F2-22, F4-04, F4-05, F4-16, F4-21 |
| 4 | Dépannage à domicile (serrurerie, plomberie) via plateforme ou réseau | 4 | 4 | 5 | 4 | **17** | F1-11, F1-21, F2-06, F2-20, F4-17 |
| 5 | Syndic de copropriété (traditionnel ou en ligne) | 4 | 3 | 5 | 5 | **17** | F1-04, F1-16, F1-25, F6-07, F6-16 |
| 6 | Garde d'enfants à domicile (agence ou plateforme) | 5 | 3 | 4 | 5 | **17** | F1-02, F4-26, F6-19, F6-20 |
| 7 | Création d'entreprise, domiciliation, compta en ligne pour créateurs | 4 | 5 | 4 | 4 | **17** | F1-07, F1-08, F1-13, F4-22, F6-21, F6-22 |
| 8 | Services aux seniors : transition de logement (tri, déménagement, débarras) et paperasse | 4 | 5 | 3 | 4 | **16** | F3-06, F3-07, F3-18, F3-19, F3-20, F4-13, F4-14, F6-20, F6-23 |
| 9 | Déménagement de particuliers (réseaux et indépendants) | 4 | 3 | 4 | 5 | **16** | F1-01, F1-26 |
| 10 | Ménage + linge des locations courte durée (rotations) | 4 | 4 | 3 | 5 | **16** | F1-06, F2-01, F2-17, F2-18, F5-24 |
| 11 | Traitement anti-moustiques des jardins par abonnement (modèle US) | 4 | 3 | 4 | 5 | **16** | F3-08, F3-09, F3-10 |
| 12 | Prise de rendez-vous B2B externalisée (téléprospection, LinkedIn) | 4 | 3 | 3 | 5 | **15** | F5-07, F5-09 |
| 13 | Vidéo courte et contenu à l'abonnement pour commerces et marques | 4 | 3 | 3 | 5 | **15** | F5-02, F5-03, F5-10 |
| 14 | Entretien auto : plateformes de garages, centres auto, contrôle technique | 3 | 2 | 5 | 5 | **15** (< 3 sources) | F1-03, F1-12, F1-24, F6-09 |
| 15 | Contrats d'entretien chaudière et clim | 5 | 3 | 2 | 5 | **15** | F2-07, F2-16, F2-25 |
| 16 | Garde d'animaux et services animaliers | 3 | 4 | 3 | 5 | **15** | F1-15, F3-15, F3-16, F3-17, F4-11, F6-26 |
| 17 | Débarras et nettoyage extrême (succession, Diogène) | 3 | 4 | 3 | 4 | **14** | F2-12, F2-27, F4-20 |
| 18 | Mise en conformité des meublés de tourisme (loi Le Meur) | 3 | 4 | 2 | 5 | **14** | F6-06, F2-18, F4-08 |
| 19 | Bascule vers la facturation électronique (TPE, micro-entrepreneurs) | 2 | 5 | 2 | 5 | **14** | F6-01, F6-21, F6-22, F5-13 |
| 20 | Audit énergétique et déclaration OPERAT pour PME (apport d'affaires) | 3 | 4 | 2 | 5 | **14** | F6-12, F6-15 |

**Hors top 20** (13 et moins) : location de matériel bébé pour touristes à Paris (13 ; F3-11, F3-12), accompagnement CV et LinkedIn (13, < 3 sources ; F5-01, F5-23), réparation de proximité avec bonus réparation (13 ; F6-24, F6-27, contre-signal Cyclofix F2-08), nettoyage de canapés et matelas (11, < 3 sources ; F2-11), collecte de biodéchets (11 ; F6-04), SAV e-commerce externalisé (10, une seule source ; F5-06), friperie spécialisée (10 ; F6-25), ramassage de déjections canines (10 ; F3-01 à F3-03).

**Écartés dès la phase 1 par les chercheurs** (équivalent fort, actifs lourds ou échec avéré) : conciergerie Airbnb généraliste à Paris, quick commerce et livraison de repas en propre, laverie, pressing à domicile, lavage auto sans eau (CosmétiCar et DetailCar déjà installés), comptabilité en ligne façon Bench, box par abonnement, photographie immobilière, CSRD pour PME, diagnostics immobiliers (certification).

---

## Fiches des 20 modèles

Format : qui vend quoi, à qui, à quel prix → ce qui ne va pas → job du client (F = fonctionnel, E = émotionnel, S = social) → ce qu'il embauche aujourd'hui → reproche principal.

### 1. Marketing local par abonnement pour TPE (19/20)
- **Qui vend quoi** : Local.fr vend site + référencement aux artisans et commerçants, 170 à 180 €/mois avec 60 mois d'engagement, 6 855 avis Trustpilot (F1-05). Une agence de marketing local du sud-est a plus de 600 clients TPE, 1,4 M€ de CA et 250 k€ d'EBE (F4-29). Planity, 88,80 €/mois (F1-18). Les plateformes prennent leur part : Treatwell 25 % sur chaque nouveau client (F2-03), Uber Eats 15 à 30 % (F2-13), StarOfService environ 15 € par contact (F2-20).
- **Ce qui ne va pas** : vente trompeuse (« site gratuit »), engagement de 5 ans, conseiller qui disparaît après la signature, résiliation impossible même après cessation d'activité (F1-05). Codeur et ComeUp sont saturés (80 à 170 offres par projet de site, F5-08), et les commerçants n'achètent pas ces services en ligne (F5-04) : il faut aller les chercher.
- **Job** : F « quand mon carnet de commandes se vide ou que je paie 25 % à une plateforme, je veux que les clients du quartier me trouvent et me choisissent, pour remplir mon agenda sans dépendre d'un intermédiaire » ; E ne plus avoir l'impression de payer pour rien, ne plus se sentir piégé ; S avoir l'air aussi pro que la chaîne d'à côté.
- **Embauché aujourd'hui** : Local.fr, PagesJaunes, Planity ou Treatwell, le neveu qui fait le site, ou rien (non-consommation).
- **Reproche principal** : « je paie chaque mois, je suis engagé des années et je ne sais pas ce que ça me rapporte ».

### 2. Ménage et repassage à domicile en agence SAP (18/20)
- **Qui vend quoi** : O2, 72,5 M€ de CA (F2-24) ; Shiva, 700 agences, 200 000 clients, dès 140 €/mois (F5-14) ; un franchisé Domi Ménage du 92 fait 1,8 M€ et 16 % de marge nette (F4-10) ; Wecasa 12,7 M€ (F2-02). Les foyers de petite couronne versent 880 M€ de salaires nets par an en emploi direct (F6-19). Crédit d'impôt de 50 % avec avance immédiate.
- **Ce qui ne va pas** : intervenante absente des mois sans remplaçant (O2 : « 4 mois sans aucune prestation », F1-17, 17 % de 1-2 étoiles), facturation contestée, Helpling 2,5/5 sur Custplace (F2-14). **Contre-signal fort** : Wecasa 4,7/5 sur 19 164 avis (F1-19) et Shiva 4,8/5 (avis hébergés sur son site).
- **Job** : F « quand je rentre tard et que le ménage s'accumule, je veux que quelqu'un de fiable s'en occupe chaque semaine, pour retrouver mes soirées » ; E tranquillité (confiance pour laisser ses clés), ne pas culpabiliser ; S foyer présentable.
- **Embauché** : emploi direct déclaré en CESU (le plus fréquent), réseaux SAP, plateformes, travail non déclaré.
- **Reproche** : « quand mon intervenante est absente, personne ne la remplace ».

### 3. Propreté B2B récurrente (17/20)
- **Qui vend quoi** : 24 357 entreprises de nettoyage courant en petite couronne, dont 88 à 90 % sans salarié (F2-05) ; Planète Gardiens 2,77 M€ de CA (F4-16) ; 36 franchises de nettoyage à 17,8 k€ d'apport moyen (F4-04) ; prix : bureaux 3 à 9 €/m², parties communes 4 à 10 €/m², fin de chantier 20 à 35 €/m² (F2-22). Des repreneurs cherchent en Île-de-France « exclusivement » des sociétés à contrats récurrents (F4-21), valorisées 4 à 5 fois l'EBE.
- **Ce qui ne va pas** : offre atomisée, sans marque ; peu de preuves directes d'insatisfaction (Onet n'a pas d'avis Trustpilot exploitable).
- **Job** : F « quand mes locaux ou mes parties communes sont sales, je veux un prestataire qui passe à l'heure, sans que j'aie à le surveiller » ; E ne plus gérer les absences et les plaintes ; S image auprès des clients, des copropriétaires ou des salariés.
- **Embauché** : micro-entrepreneur du quartier, gros groupe (Onet, Atalian) pour les grands comptes, ménage fait par les salariés.
- **Reproche** : absences, qualité qui se dégrade après 3 mois, remplacement non assuré [en partie HYPOTHÈSE : peu de sources directes].

### 4. Dépannage à domicile (17/20)
- **Qui vend quoi** : MesDépanneurs, plus de 500 000 dépannages, 1 300 pros, prix en fourchette (débouchage 100 à 200 €, porte claquée 130 à 180 €) (F1-11) ; franchisés Help Confort de 265 à 515 k€ de CA (F4-17).
- **Ce qui ne va pas** : 60 % des professionnels contrôlés par la DGCCRF en infraction, 2 600 signalements en 2024 (F1-21, F2-06) ; MesDépanneurs 20 % de 1-2 étoiles, facturé « au tarif maximum » (F1-11) ; artisans indisponibles.
- **Job** : F « quand je suis bloqué dehors ou que l'eau coule, je veux quelqu'un en moins d'une heure, à un prix connu d'avance » ; E ne pas se faire arnaquer en situation de panique ; S ne pas passer pour un pigeon.
- **Embauché** : le premier résultat Google Ads, l'autocollant dans la boîte aux lettres, un voisin, MesDépanneurs.
- **Reproche** : « le prix final n'a rien à voir avec le prix annoncé ».

### 5. Syndic de copropriété (17/20)
- **Qui vend quoi** : Foncia, 17 500 avis (F1-04) ; Matera, plus de 10 000 copropriétés, 690 €/an cité par un client (F1-16) ; 11 894 structures d'administration d'immeubles en petite couronne (F6-16). Service obligatoire, payé chaque année.
- **Ce qui ne va pas** : Foncia 27 % et Matera 25 % de 1-2 étoiles ; 20 avis négatifs en 4 semaines chez Matera ; 38 % des résidents non satisfaits (Ipsos 2025 cité par la FNAIM, F1-25) ; reportage France 2 de janvier 2026.
- **Job** : F « quand l'immeuble a un dégât des eaux ou une AG, je veux un gestionnaire qui répond et des comptes justes, pour que l'immeuble soit entretenu sans que je m'en occupe » ; E ne plus être en colère à chaque AG ; S être un conseil syndical qui « tient » l'immeuble.
- **Embauché** : syndic pro (traditionnel ou en ligne), syndic bénévole, syndic coopératif.
- **Reproche** : « le gestionnaire est injoignable ».
- **Point dur dès maintenant** : être syndic professionnel exige la carte G (loi Hoguet), et changer de syndic se vote en AG (au mieux une fois par an).

### 6. Garde d'enfants à domicile (17/20)
- **Qui vend quoi** : Kinougarde 102 M€ de CA (F4-26) ; Yoopies 35 €/mois d'abonnement (F1-02) ; à Paris, 20 151 foyers emploient une garde à domicile (181 M€ de salaires nets, F6-19).
- **Ce qui ne va pas** : Yoopies 15 % de 1-2 étoiles (profils peu fiables, abonnement pour contacter) ; une agence Family Sphere du 92 en forte perte (contre-signal, F4-26).
- **Job** : F « quand l'école finit à 16 h 30 et que je travaille, je veux quelqu'un de sûr pour récupérer mes enfants, même quand la nounou est malade » ; E sécurité, culpabilité ; S être un parent organisé.
- **Embauché** : nounou en emploi direct (Pajemploi), agences, plateformes, grands-parents.
- **Reproche** : « personne pour remplacer au pied levé ».
- **Point dur** : la garde des moins de 3 ans exige un agrément préfectoral SAP.

### 7. Création d'entreprise, domiciliation, compta pour créateurs (17/20)
- **Qui vend quoi** : Legalstart, 7 608 avis, abonnements dès 29,90 € HT (F1-08) ; SeDomicilier 11 à 16 €/mois (F1-07) ; Dougs, 49 000 clients, 79 à 129 € HT/mois (F1-13) ; une formation en ligne pour freelances fait 2,2 M€ (F4-22). 333 500 créations en Île-de-France en 2025 (F6-21).
- **Ce qui ne va pas** : cases précochées, abonnements subis, prélèvements après résiliation, interlocuteurs qui changent, erreurs fiscales.
- **Job** : F « quand je lance mon activité, je veux que tout l'administratif soit en règle sans y passer mes soirées » ; E peur de l'erreur et du contrôle ; S être un « vrai » chef d'entreprise.
- **Embauché** : legaltechs, expert-comptable, tutoriels YouTube, faire seul.
- **Reproche** : « on m'a fait souscrire des abonnements que je n'ai pas voulus et personne ne répond ».
- **Point dur** : comptabilité (Ordre des experts-comptables), conseil juridique et domiciliation (agrément préfectoral) sont réglementés : l'équipe ne peut faire que la partie commerciale.

### 8. Services aux seniors : transition de logement et paperasse (16/20)
- **Qui vend quoi** : aux États-Unis, Caring Transitions, plus de 425 agences, 28 franchises vendues au 1er semestre 2026 (F3-06) ; « daily money managers » à 35 à 150 $/h (F3-18). En France : Petits-fils 31,9 M€ (F4-14), franchisés Senior Compagnie de 1,2 à 1,6 M€ (F4-13), home organizers à environ 70 €/h à Paris (F3-20).
- **Ce qui ne va pas** : **personne ne coordonne** le passage « maison familiale → résidence » (déménageur, débarras, brocanteur, ménage sont séparés, F3-07) ; l'assistance administrative n'existe qu'en complément, avec très peu d'avis (Vitalliance Paris Sud : 3 avis, F3-19). C'est une absence d'offre plutôt qu'une faiblesse prouvée par des avis.
- **Job** (celui de l'enfant de 45 à 60 ans) : F « quand mon parent doit quitter sa maison ou ne s'en sort plus avec ses papiers, je veux qu'une seule personne de confiance s'occupe de tout » ; E culpabilité, épuisement d'aidant ; S être un bon fils ou une bonne fille.
- **Embauché** : l'enfant lui-même (non-consommation, week-ends sacrifiés), déménageur + débarras séparés, notaire pour une partie.
- **Reproche** : « j'ai dû tout coordonner moi-même, à distance, en plus de mon travail » [HYPOTHÈSE à valider en entretien].

### 9. Déménagement de particuliers (16/20)
- **Qui vend quoi** : Demeco, « 100 000 déménagements chaque année », 500 à 900 € pour 15 m³ (F1-01) ; 1 051 déménageurs actifs en petite couronne (F1-26).
- **Ce qui ne va pas** : 28 % de 1-2 étoiles chez Demeco ; casse puis indemnisation refusée grâce à la lettre de voiture, problème de tout le secteur (F1-26).
- **Job** : F « quand je déménage, je veux que mes affaires arrivent intactes, à la date prévue, au prix annoncé » ; E stress du jour J ; S ne pas avoir à demander l'aide des amis.
- **Embauché** : déménageurs, location d'utilitaire + amis, plateformes de mise en relation.
- **Reproche** : « ils ont tout abîmé et refusent d'indemniser ».

### 10. Ménage + linge des locations courte durée (16/20)
- **Qui vend quoi** : forfaits Houst de 90 € (studio) à 210 € par rotation à Paris (F2-17) ; conciergeries à 20 % des revenus (F2-01, F1-06).
- **Ce qui ne va pas** : HostnFly 14 % de 1-2 étoiles, « ménage n'a pas été terminé » (F1-06) ; BnbSitter liquidé (F5-24) ; loi Le Meur et plafond de 90 jours possible (F2-18).
- **Job** (conciergerie ou hôte) : F « quand un voyageur part à 11 h et qu'un autre arrive à 15 h, je veux un logement impeccable et du linge propre, sans y aller » ; E peur de la mauvaise note ; S réputation « Superhost ».
- **Embauché** : femme de ménage indépendante, équipe salariée de la conciergerie, plateformes.
- **Reproche** : « ménage bâclé et personne à joindre en urgence ».

### 11. Anti-moustiques des jardins par abonnement (16/20)
- **Qui vend quoi** : Mosquito Squad (US), CA moyen 493 200 $ par territoire en 2025 (F3-08). En France, seulement des bornes à environ 600 € (F3-10).
- **Ce qui ne va pas** : en France on vend un produit, pas un service ; efficacité des bornes discutée ; 328 communes d'Île-de-France colonisées (F3-09).
- **Job** : F « quand je ne peux plus dîner dans mon jardin à cause du moustique tigre, je veux le récupérer sans y passer mes week-ends » ; E agacement, peur pour les enfants ; S recevoir dehors.
- **Embauché** : bornes, répulsifs, rien.
- **Reproche** : « j'ai acheté une borne, elle ne suffit pas ».
- **Point dur** : saisonnier (mai à octobre) et biocides encadrés (Certibiocide).

### 12. Prise de rendez-vous B2B externalisée (15/20)
- **Qui vend quoi** : sur ComeUp, prospection LinkedIn 33 € avec 377 avis, budget moyen 350 € (F5-07) ; sur Codeur, projets de téléprospection de 1 000 à 10 000 € (F5-07) ; aux US, agence productisée à 3 999 $/mois, 80 clients (F5-09).
- **Ce qui ne va pas** : c'est le seul type de projet où l'offre manque (4 à 6 réponses contre 20 à 170 ailleurs) ; les prestataires vendent du volume plutôt que des rendez-vous qualifiés.
- **Job** : F « quand mon agenda commercial est vide, je veux des rendez-vous avec des décideurs qualifiés, sans recruter un commercial » ; E angoisse du pipeline vide ; S montrer de la croissance aux associés.
- **Embauché** : le dirigeant prospecte lui-même, outil d'automatisation (Waalaxy), freelance, agence d'appels.
- **Reproche** : « beaucoup de messages envoyés, peu de rendez-vous utiles » [HYPOTHÈSE partielle].

### 13. Vidéo courte et contenu à l'abonnement (15/20)
- **Qui vend quoi** : sur ComeUp, pub UGC avec un budget moyen de 1 110 € et montage YouTube à 1 735 € (F5-02) ; White Glove Content (US), 611 abonnés (F5-10) ; community managers sur Malt à 406 €/jour (F5-26).
- **Ce qui ne va pas** : vendeurs à distance, à la pièce, sans tournage réel ; trou de prix entre le freelance à 400 €/jour et les budgets de commerçants sous 500 €/mois (F5-03).
- **Job** : F « quand je dois publier chaque semaine pour exister, je veux des vidéos qui donnent envie, sans y passer mes soirées » ; E fatigue, peur d'être ridicule ; S paraître moderne.
- **Embauché** : le commerçant filme lui-même, freelance, rien.
- **Reproche** : « trop cher pour mon budget, ou trop générique ».

### 14. Entretien auto (15/20, moins de 3 sites indépendants)
- **Qui vend quoi** : Vroomly (660 avis, 34 % de 1-2 étoiles), Speedy (64 %), Autosur (74 %) (F1-03, F1-12, F1-24) ; contrôle technique des deux-roues obligatoire (F6-09).
- **Ce qui ne va pas** : prix affichés non tenus, ventes additionnelles, rendez-vous fantômes.
- **Job** : F « quand ma voiture doit passer au garage, je veux un prix juste et ne pas perdre ma journée » ; E méfiance envers les garagistes ; S ne pas se faire avoir.
- **Embauché** : garage habituel, centres auto, plateformes.
- **Reproche** : « le devis final double ».
- **Limite** : les preuves viennent toutes de Trustpilot, plus service-public : il manque un 3e site indépendant.

### 15. Contrats d'entretien chaudière et clim (15/20)
- **Qui vend quoi** : Proxiserve 302 M€ (F2-16) ; contrats de 114 à 305 €/an (F2-07) ; ventes de clim record en septembre 2026 (F2-25).
- **Ce qui ne va pas** : rien de prouvé par des avis (HYPOTHÈSE de service pensé pour les grands comptes).
- **Job** : F « chaque année, je veux être en règle (attestation) sans courir après un chauffagiste » ; E éviter la panne en hiver ; S propriétaire responsable.
- **Embauché** : contrat Proxiserve, Savelys ou Engie, chauffagiste du coin, rien.
- **Reproche** : non documenté.
- **Point dur** : intervention réservée aux professionnels qualifiés.

### 16. Garde d'animaux et services animaliers (15/20)
- **Qui vend quoi** : Rover, 35 876 avis, 15 % de frais ajoutés (F1-15) ; Dogtopia (US) environ 300 sites (F3-15) ; franchises animalières françaises à 55-100 k€ de CA par unité (F4-11).
- **Ce qui ne va pas** : support Rover injoignable et en anglais, pas de contrôle des gardiens ; CA unitaires faibles en France.
- **Job** : F « quand je pars, je veux que mon animal soit gardé par quelqu'un de sûr » ; E inquiétude ; S bon maître.
- **Embauché** : voisins, famille, Rover, pensions.
- **Reproche** : « aucun contrôle des gardiens, et personne à appeler ».

### 17. Débarras et nettoyage extrême (14/20)
- **Qui vend quoi** : franchise Les Débarrasseurs de l'Extrême, 8 000 € d'apport pour 200 k€ de CA déclaré (F4-20) ; Les Débarrasseurs Bretons 258 k€ de CA (F4-20) ; Lebontri publie des demandes de nettoyage Diogène à Paris (F2-27).
- **Ce qui ne va pas** : fiches d'annuaire avec très peu d'avis, aucune marque de référence (F2-12).
- **Job** : F « quand je dois vider le logement d'un parent décédé avant la vente, je veux que ce soit fait vite et proprement » ; E deuil, honte (Diogène) ; S respect du défunt.
- **Embauché** : famille, brocanteurs, entreprises de débarras trouvées sur Google.
- **Reproche** : « devis opaque, peur d'être arnaqué ».

### 18. Mise en conformité des meublés de tourisme (14/20)
- **Qui vend quoi** : organismes de classement, diagnostiqueurs, conciergeries (F6-06) ; enregistrement national au 4e trimestre 2026, amendes jusqu'à 50 000 €, abattement de 30 % au lieu de 50 % si le meublé n'est pas classé.
- **Ce qui ne va pas** : règles qui changent chaque année ; pas d'offre « coordination » identifiée.
- **Job** : F « je veux continuer à louer légalement en payant le moins d'impôts possible » ; E peur de l'amende ; S propriétaire en règle.
- **Embauché** : conciergerie, expert-comptable LMNP, faire seul.
- **Reproche** : non documenté.

### 19. Bascule vers la facturation électronique (14/20)
- **Qui vend quoi** : plateformes agréées et logiciels (Pennylane, Qonto, Tiime…), souvent gratuits ou presque (F6-01). Réception obligatoire depuis le 1er septembre 2026, émission le 1er septembre 2027 pour TPE et micro-entrepreneurs. 205 000 micro-entrepreneurs économiquement actifs en petite couronne (F6-22).
- **Ce qui ne va pas** : aucune preuve d'argent dépensé pour l'accompagnement ; ComeUp montre que la saisie comptable ne se vend pas en ligne (F5-13).
- **Job** : F « je veux être en règle avant septembre 2027 sans y passer un week-end » ; E peur de l'amende ; S « ne pas être largué ».
- **Embauché** : banque, logiciel gratuit, expert-comptable.
- **Reproche** : non documenté.

### 20. Audit énergétique et déclaration OPERAT pour PME (14/20)
- **Qui vend quoi** : bureaux d'études et fournisseurs d'énergie (F6-12, F6-15). Nouveau critère : 2,75 GWh consommés, échéance du 11 octobre 2026 dépassée.
- **Ce qui ne va pas** : des PME ignorent qu'elles sont désormais concernées [HYPOTHÈSE].
- **Job** : F « je veux être en conformité sans mobiliser un ingénieur » ; E peur de la sanction ; S image RSE.
- **Embauché** : fournisseur d'énergie, bureau d'études.
- **Point dur** : conflit d'intérêts possible avec l'alternance du fondateur chez EDF.

---

## Ce que montre le regroupement

1. **Les mêmes trois reproches reviennent partout** : personne à joindre, engagement ou abonnement subi, prix final différent du prix annoncé. Ce sont des défauts d'organisation et de relation client, pas de technologie.
2. **L'argent est le mieux prouvé dans les services récurrents**, à domicile ou aux bâtiments (ménage SAP, propreté B2B, garde d'enfants), où une seule agence de petite couronne dépasse 0,5 à 1,8 M€ de CA. Ce sont aussi des métiers d'employeur.
3. **Le métier natif de l'équipe (marketing pour TPE) est le mieux noté**, mais c'est aussi le plus encombré : la différence doit venir de la verticalisation (un seul métier de client) et de la vente en direct.
4. **Les plateformes nationales financées par levée de fonds perdent de l'argent** (Treatwell FR -7,6 M€, Wecasa en perte, Cyclofix et Homejoy disparus). Le bon gabarit est la marque locale de service géré, pas une plateforme de plus.
5. Les modèles 5, 6, 7, 11, 15 et 20 ont un point juridique ou de calendrier qui sera vérifié dès la phase 3.

Les 10 premiers modèles (rangs 1 à 10) passent en phase 3 : [idees-classees.md](idees-classees.md). La vidéo à l'abonnement (rang 13) n'a pas de fiche propre en phase 3 : elle y apparaît comme une variante du modèle 1, car c'est le même client (commerce de quartier) et le même budget marketing. Les modèles 11 et 12 (anti-moustiques, prise de rendez-vous B2B) restent en réserve. Ils seraient repris si le top 10 ne produisait aucune idée qui passe les filtres.
