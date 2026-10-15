# Phase 3 : idées « la même chose, en mieux »

Date : 13 octobre 2026. Entrée : les 10 premiers modèles de [problemes.md](problemes.md).

Méthode : skill `ai-startup-opportunity-generator`, étapes 1 à 8 et 10 à 12 (sans l'étape 9, stack Laravel). Pour chaque idée : travail réel → douleur → qui paie → solution → concurrents → échecs passés → MVP. On précise le point exact où l'on bat l'acteur en place, le prix, le canal et le cadre juridique. Les montants qui ne viennent pas d'un signal sont marqués [HYPOTHÈSE].

## Tableau trié (idées qui passent les filtres)

Grille du prompt, notes sur 10 : **Arg** argent déjà dépensé (25 %), **Faib** faiblesse prouvée des acteurs (15 %), **Doul** douleur prouvée par le web (15 %), **Éq** avantage d'une équipe marketing (15 %), **Vit** vitesse jusqu'au premier client payant (15 %), **Test** testable en moins de 4 semaines, pour moins de 500 €, sans coder (10 %), **Tail** taille du marché (5 %).

| Rang | Idée | Modèle | Arg | Faib | Doul | Éq | Vit | Test | Tail | **Score /10** |
|------|------|--------|-----|------|------|----|-----|------|------|---------------|
| 1 | I1. Visibilité locale sans engagement pour artisans du bâtiment | 1 | 9 | 6 | 7 | 10 | 7 | 9 | 7 | **8,00** |
| 2 | I10. Dépannage à prix fixe écrit, réseau d'artisans vérifiés | 4 | 8 | 9 | 9 | 8 | 7 | 6 | 8 | **7,95** |
| 3 | I5. Agence de ménage SAP « remplaçante garantie sous 48 h » | 2 | 10 | 6 | 7 | 6 | 7 | 6 | 10 | **7,50** |
| 4 | I19. Tiers de confiance du déménagement | 9 | 6 | 8 | 8 | 8 | 7 | 8 | 7 | **7,30** |
| 5 | I2. Sortir des commissions : marketing et réservation pour salons de beauté | 1 | 8 | 5 | 5 | 9 | 8 | 9 | 7 | **7,30** |
| 6 | I4. Vidéos courtes tournées sur place, à l'abonnement, pour commerces | 1 | 7 | 5 | 5 | 9 | 7 | 9 | 6 | **6,85** |
| 7 | I14. Garde d'enfants de plus de 3 ans en urgence et en sortie d'école | 6 | 9 | 6 | 6 | 6 | 6 | 6 | 8 | **6,85** |
| 8 | I12. Accompagnement au changement de syndic | 5 | 5 | 9 | 9 | 7 | 4 | 7 | 6 | **6,60** |
| 9 | I7. Ménage de petits bureaux et cabinets avec rapport photo | 3 | 9 | 4 | 4 | 7 | 7 | 6 | 8 | 6,55 |
| 10 | I17. Coordinateur de la transition de logement des seniors | 8 | 6 | 6 | 6 | 8 | 6 | 8 | 6 | 6,50 |
| 11 | I21. Rotations ménage + linge pour conciergeries (B2B) | 10 | 8 | 6 | 6 | 5 | 7 | 6 | 6 | 6,50 |
| 12 | I6. Ménage de fin de bail pour locataires sortants | 2 | 6 | 4 | 6 | 7 | 8 | 8 | 7 | 6,40 |
| 13 | I9. Nettoyage de fin de chantier pour entreprises de rénovation | 3 | 7 | 4 | 5 | 6 | 8 | 7 | 6 | 6,20 |
| 14 | I11. Maintenance à prix fixes des logements loués (petits bailleurs) | 4 | 6 | 6 | 6 | 7 | 6 | 6 | 7 | 6,20 |
| 15 | I8. « Gardien partagé » pour petites copropriétés sans gardien | 3 | 8 | 5 | 5 | 7 | 5 | 5 | 7 | 6,15 |
| 16 | I18. Paperasse des parents âgés, abonnement SAP | 8 | 5 | 6 | 5 | 7 | 6 | 7 | 7 | 5,90 |
| 17 | I13. Assistant outillé des syndics bénévoles | 5 | 5 | 7 | 6 | 5 | 6 | 6 | 4 | 5,65 |

Calcul : score = 0,25 × Arg + 0,15 × (Faib + Doul + Éq + Vit) + 0,10 × Test + 0,05 × Tail.

**Les 8 premières (I1, I10, I5, I19, I2, I4, I14, I12) passent en phase 4** (audit concurrentiel réel). Attention, I1, I2 et I4 sont trois variantes du même modèle (marketing pour commerces et artisans). L'audit dira si elles se renforcent ou se cannibalisent. I17 (seniors) arrive juste après la barre, à 6,50.

## Idées éliminées (élimination définitive)

| Idée | Filtre | Motif en une ligne |
|------|--------|--------------------|
| I3. Commande directe (click & collect) pour restaurants et traiteurs | Leader bien financé sans angle crédible | Le restaurateur achète un logiciel de commande, et plusieurs éditeurs financés l'occupent déjà [HYPOTHÈSE : noms à ne pas citer sans source] ; un service marketing par-dessus n'a pas d'angle qui tienne face aux 15 à 30 % d'Uber Eats, qui apportent aussi des clients (F2-13). |
| I15. Pack « je lance ma micro-entreprise » | Leader bien financé sans angle crédible | L'immatriculation d'une micro-entreprise est gratuite. Banques en ligne, legaltechs et logiciels de facturation offrent déjà le parcours, souvent gratuitement (F1-08, F6-21). Il reste un prix à payer pour l'accompagnement, mais aucun angle défendable. |
| I16. Marque commerciale d'un cabinet comptable sur une niche (apport d'affaires) | Profession réglementée | La tenue de comptabilité est réservée aux experts-comptables. Leur déontologie encadre strictement la rémunération des apporteurs d'affaires [HYPOTHÈSE juridique : interdiction probable, non vérifiée]. Le modèle repose donc sur une rémunération incertaine, voire interdite. |
| I20. « Jardin sans moustique tigre » (réserve, modèle 11) | Premier euro impossible en moins de 3 mois (saisonnalité) | Nous sommes mi-octobre : la saison commence en mai 2027. Il y a aussi le Certibiocide pour tout traitement insecticide (F3-08 à F3-10). À ressortir en février 2027 pour des préventes de printemps. |
| I22. Conciergerie Airbnb de quartier (variante du modèle 10) | Diplôme ou licence obligatoire qu'on n'a pas, et cimetière | Encaisser les loyers pour un propriétaire relève de la loi Hoguet (carte professionnelle) [HYPOTHÈSE juridique à vérifier]. BnbSitter a été liquidé (F5-24), la commission est à 20 % et la loi Le Meur réduit le marché (F2-18). Seule la sous-traitance du ménage (I21) est gardée. |

---

## Fiches des idées

### I1. Visibilité locale sans engagement pour artisans du bâtiment (8,00)
- **Travail réel** : un plombier, électricien ou menuisier de petite couronne trouve ses clients par le bouche-à-oreille, Google Maps et des plateformes de leads. Il n'a ni le temps ni l'envie de gérer sa fiche Google, ses avis et son site. Beaucoup ont signé un contrat de site « gratuit » à 170-180 €/mois sur 60 mois (F1-05).
- **Douleur** : engagement de 5 ans, conseiller qui disparaît, résiliation impossible même après cessation d'activité (F1-05). Payer environ 15 € par contact non qualifié (F2-20).
- **Qui paie** : l'artisan (TPE, décideur unique). Base de petite couronne : 17 027 entreprises d'installation électrique et 10 522 de plomberie (F6-16).
- **Solution, et le point exact où l'on bat l'acteur en place** : même service que Local.fr (site d'une page, fiche Google optimisée, demande d'avis après chaque chantier, rapport mensuel), mais **sans engagement**, résiliable en un clic, site et fiche **propriété de l'artisan**, et un rapport mensuel chiffré (appels reçus, demandes de devis). Prix : 99 à 149 €/mois [HYPOTHÈSE], plus 0 à 290 € de mise en place.
- **Canal** : terrain (négoces de matériaux comme Point.P ou Cedeo le matin, chantiers), réseaux d'affaires locaux, puis parrainage entre artisans. Aucune vente en ligne : les commerçants n'achètent pas ce service sur une marketplace (F5-04).
- **Concurrents** : Local.fr, Solocal / PagesJaunes, agences web locales, freelances (Codeur saturé : 80 à 170 offres par projet, F5-08). Audit à faire en phase 4.
- **Échecs passés** : à chercher en phase 4.
- **MVP** : 10 artisans en 4 semaines. Les fiches Google sont optimisées à la main, les sites faits en no-code. Le premier mois est facturé au prix plein, sans engagement.
- **Juridique** : aucune carte ni diplôme. Les contrats B2B entre professionnels « hors champ » (moins de 5 salariés) bénéficient de certaines protections du Code de la consommation [HYPOTHÈSE : article L221-3, à vérifier], ce qui sert notre argument contre l'engagement long.

### I10. Dépannage à prix fixe écrit, réseau d'artisans vérifiés (7,95)
- **Travail réel** : en urgence (porte claquée, fuite), le particulier tape « serrurier + ville » et appelle le premier résultat payant.
- **Douleur** : 60 % des dépanneurs contrôlés en infraction, 2 600 signalements en 2024 (F1-21, F2-06) ; facturé « au tarif maximum » chez MesDépanneurs (F1-11).
- **Qui paie** : le particulier ou son assurance, 100 à 800 € par intervention (F1-11).
- **Solution, point exact** : **prix fixe par intervention, écrit avant le déplacement** (et non une fourchette), facture et photos envoyées au client et à l'assureur, un humain qui suit le dossier, artisans vérifiés (qualification, assurance décennale, casier). Modèle à la commission (15 à 25 % [HYPOTHÈSE]) payée par l'artisan.
- **Canal** : SEO local et Google Ads, syndics et gestionnaires locatifs (B2B), affichage dans les halls d'immeubles.
- **Concurrents** : MesDépanneurs, Help Confort, réseaux d'assisteurs (Mondial Assistance, IMA [HYPOTHÈSE]), arnaqueurs très présents sur Google Ads.
- **Échecs passés** : à chercher (plateformes de dépannage fermées).
- **MVP** : 2 villes, 5 artisans, une page avec la grille des prix fixes, une ligne téléphonique tenue par l'équipe.
- **Juridique** : l'exécution est réservée à des professionnels qualifiés (loi du 5 juillet 1996) ; l'intermédiaire doit informer clairement sur les prix (arrêté sur l'information des consommateurs pour les dépannages à domicile [HYPOTHÈSE : référence exacte à vérifier]). **Risque majeur** : notre responsabilité en cas de malfaçon de l'artisan.

### I5. Agence de ménage SAP « remplaçante garantie sous 48 h » (7,50)
- **Travail réel** : un foyer actif emploie une aide ménagère 2 à 4 h par semaine, en direct (CESU) ou via une agence. Quand elle est absente, personne ne la remplace.
- **Douleur** : « 4 mois sans aucune prestation » chez O2 (F1-17), absences chez Helpling (F2-14). Contre-signal : Wecasa et Shiva très bien notés (F1-19, F5-14).
- **Qui paie** : le foyer, 13 à 15 €/h après crédit d'impôt [HYPOTHÈSE], avec l'avance immédiate. 244 000 foyers de petite couronne emploient déjà quelqu'un (F6-19).
- **Solution, point exact** : agence de quartier (une ou deux villes du 92) qui **garantit un remplacement sous 48 h, écrit au contrat**, avec un binôme d'intervenantes par client et des intervenantes mieux payées que le marché pour fidéliser.
- **Canal** : boîtes aux lettres, groupes Facebook de quartier, pharmacies et boulangeries, parrainage.
- **Concurrents** : O2, Shiva, Domi Ménage, Wecasa, Helpling, emploi direct.
- **Échecs passés** : Homejoy, Helpling Pays-Bas (F5-19) : le modèle plateforme échoue, l'agence déclarée gagne.
- **MVP** : en mode mandataire (le foyer reste employeur) pour démarrer sans masse salariale ; 10 clients et 6 intervenantes.
- **Juridique** : déclaration SAP (gratuite) pour le ménage, sans agrément si le public n'est pas fragile. Métier d'employeur (droit du travail, convention collective).

### I19. Tiers de confiance du déménagement (7,30)
- **Travail réel** : le particulier demande 3 devis, choisit le moins cher, signe la lettre de voiture le jour J sans rien vérifier, puis découvre la casse.
- **Douleur** : Demeco 28 % de 1-2 étoiles, indemnisation refusée grâce à la lettre de voiture (F1-01), même problème chez les petits déménageurs (F1-26).
- **Qui paie** : le particulier, forfait de 99 à 199 € [HYPOTHÈSE], plus une commission éventuelle du déménageur partenaire.
- **Solution, point exact** : nous ne déménageons pas. Nous **choisissons le déménageur** parmi des partenaires notés, faisons l'**inventaire vidéo**, sommes **présents au déchargement** pour le constat et les réserves écrites, et **gérons la réclamation**.
- **Canal** : SEO « déménagement Paris », agences immobilières et gestionnaires (locataires sortants), CSE.
- **Concurrents** : comparateurs de devis, déménageurs, assurances déménagement.
- **MVP** : 5 déménagements accompagnés en 4 semaines, payés.
- **Juridique** : en restant hors du contrat de transport (le client signe avec le déménageur), pas d'inscription au registre des commissionnaires de transport [HYPOTHÈSE juridique à vérifier en phase 4].

### I2. Sortir des commissions : marketing et réservation pour salons de beauté (7,30)
- **Travail réel** : un salon indépendant paie Treatwell (25 % sur les nouveaux clients, F2-03) ou Planity (88,80 €/mois, F1-18) pour remplir son agenda.
- **Douleur** : commissions, résiliation difficile, fichier client verrouillé (F1-18).
- **Qui paie** : le salon, décideur unique ; 21 600 salons de coiffure et de beauté en petite couronne (F6-16).
- **Solution, point exact** : récupération du fichier client, réservation sans commission via un outil existant moins cher, fiche Google, Instagram et campagnes SMS de relance, pour 99 à 149 €/mois sans engagement [HYPOTHÈSE].
- **Canal** : porte-à-porte des salons, fournisseurs de produits professionnels.
- **MVP** : 5 salons migrés en 4 semaines.
- **Juridique** : aucun.

### I4. Vidéos courtes tournées sur place, à l'abonnement, pour commerces (6,85)
- **Point exact** : les vendeurs de ComeUp travaillent à distance et à la pièce (F5-02). Nous tournons sur place, 4 vidéos par mois, pour 300 à 450 €/mois [HYPOTHÈSE], soit un prix entre le freelance à 406 €/jour (F5-26) et le budget d'un commerçant, souvent sous 500 € (F5-03).
- **Canal** : porte-à-porte de restaurants, boutiques et salons.
- **MVP** : 3 commerces, un mois de vidéos chacun.
- **Juridique** : droit à l'image des clients filmés, musique sous licence.

### I14. Garde d'enfants de plus de 3 ans en urgence et en sortie d'école (6,85)
- **Point exact** : la plateforme fait payer un abonnement pour simplement contacter des profils peu fiables (F1-02). Nous fournissons un vivier d'étudiants vérifiés (entretien, références, premiers secours) et **un remplaçant garanti le jour même**, facturé à l'heure, éligible au crédit d'impôt.
- **Qui paie** : les parents ; les CSE pour les urgences.
- **Concurrents** : Kinougarde (102 M€, F4-26), Babychou, Family Sphere, Yoopies.
- **Juridique** : déclaration SAP pour les plus de 3 ans ; **agrément préfectoral obligatoire pour les moins de 3 ans**, d'où la limite de l'offre.

### I12. Accompagnement au changement de syndic (6,60)
- **Point exact** : Foncia et Matera sont mal notés (27 % et 25 % de 1-2 étoiles, F1-04, F1-16), mais changer de syndic est un parcours obscur. Le conseil syndical paie un forfait de 600 à 1 500 € [HYPOTHÈSE] pour un cahier des charges, une mise en concurrence de 3 à 5 syndics, un comparatif, la préparation du vote en AG et le suivi de la passation.
- **Qui paie** : le conseil syndical, au nom du syndicat [HYPOTHÈSE juridique : la loi permet au conseil syndical de se faire assister à la charge du syndicat, à vérifier].
- **Vitesse** : les AG ont lieu surtout au printemps. La mission peut être signée maintenant, mais le résultat est collectif et lent, d'où la note de 4 en vitesse.
- **Juridique** : pas de carte G tant que nous ne gérons pas l'immeuble. Notre indépendance vis-à-vis des syndics doit être réelle (pas de commission versée par le syndic choisi, sinon conflit d'intérêts).

### Fiches courtes des idées classées de 9 à 17
- **I7. Petits bureaux et cabinets** (6,55) : nettoyage avec rapport photo et remplaçant garanti, 250 à 600 €/mois par client [HYPOTHÈSE] ; prix de marché 3 à 9 €/m² (F2-22). Faiblesse des acteurs peu prouvée.
- **I17. Transition de logement des seniors** (6,50) : un coordinateur unique (tri, désencombrement, déménageur partenaire, débarras, vente des objets, ménage, installation), forfait de 1 500 à 5 000 € [HYPOTHÈSE] payé par les enfants. Le modèle est prouvé aux États-Unis (F3-06) et absent en Île-de-France (F3-07). Les canaux passent par des prescripteurs (résidences seniors, EHPAD, notaires, agences) : plus lents.
- **I21. Rotations pour conciergeries** (6,50) : 25 à 90 € par rotation hors linge, 90 à 210 € tout compris (F2-17). Risque réglementaire (loi Le Meur, F2-18) et métier d'employeur pur.
- **I6. Ménage de fin de bail** (6,40) : forfait de 150 à 350 € [HYPOTHÈSE], prescrit par les agences. Peu de preuves directes.
- **I9. Fin de chantier** (6,20) : 20 à 35 €/m² (F2-22), clients pressés, mais il faut une main-d'œuvre disponible à la demande.
- **I11. Maintenance des logements loués** (6,20) : grille de prix fixes pour petits bailleurs et gestionnaires, avec des artisans partenaires. Recoupe I10.
- **I8. Gardien partagé** (6,15) : Planète Gardiens fait 2,77 M€ (F4-16). La vente passe par les syndics, ce qui est lent.
- **I18. Paperasse des parents âgés** (5,90) : l'assistance administrative à domicile est une activité SAP (crédit d'impôt de 50 %). Peu de preuves d'argent dépensé en France (F3-19).
- **I13. Assistant des syndics bénévoles** (5,65) : petit marché, et zone grise avec la loi Hoguet.

## Vérification juridique faite dès la phase 3 (à confirmer en phase 4 pour les 8 retenues)

| Idée | Agrément / carte / diplôme | Démarchage | Décision collective / saison |
|------|----------------------------|------------|------------------------------|
| I1, I2, I4 | Aucun | B2B : prospection téléphonique et physique autorisée | Décideur unique |
| I10 | Exécution par des artisans qualifiés (loi de 1996) ; obligations d'information sur les prix | B2C : la prospection téléphonique sans consentement préalable est interdite à partir d'août 2026 [HYPOTHÈSE : loi de 2025 contre la fraude aux aides publiques, date à vérifier] ; nous n'en faisons pas | Décideur unique, achat en urgence |
| I5 | Déclaration SAP (pas d'agrément pour le ménage) | Idem B2C | Décideur unique |
| I19 | À vérifier : commissionnaire de transport si nous contractons le transport | Idem B2C | Décideur unique, événement daté |
| I14 | Déclaration SAP pour les plus de 3 ans ; agrément pour les moins de 3 ans | Idem B2C | Décideur unique |
| I12 | Pas de carte G si nous ne gérons pas l'immeuble | B2C | **Conseil syndical (collectif) ; vote en AG (printemps)** |
