# P1 : A1 facturation électronique, segments A1-S2 (cabinets) et A1-S1 (TPE du bâtiment)

- Mission : signaux par segment (argent dépensé, faiblesse, recherche active, étranger, comptages, accès, droit)
- Date : 2026-10-13
- Recherches web utilisées : voir ligne « Compteur » en bas de fichier
- Convention : « ouverte » = page lue en WebFetch ; « extrait » = vue seulement dans un résultat de recherche.

## Lot 1

### P1-1 : Comptage API, TPE du bâtiment (NAF 43.xx) employeuses de 1 à 9 salariés
- Acteur / marché : entreprises actives de NAF 43.11Z à 43.99E, tranche d'effectif 01+02+03 (1-2, 3-5, 6-9 salariés)
- Type : tendance (donnée publique de comptage)
- Source : https://recherche-entreprises.api.gouv.fr/search (24 codes 43.xx, tranche_effectif_salarie=01,02,03, etat_administratif=A, un appel par département, 101 départements) (date : 2026-10-13, API ouverte)
- Citation : « total_results » additionné sur 101 départements = 177 400 (maximum 7 540 pour le 93)
- Chiffres : 177 400 unités légales actives, employeurs de 1 à 9 salariés, NAF 43. Hypothèse de segments.md (150 000) : confirmée et dépassée de 18 %. Cela inclut toutes les TPE du 43 (électriciens, plombiers, peintres...), pas seulement celles « sur Word/Excel » : cette part reste [HYPOTHÈSE]. Non-employeurs : voir P1-3.
- Ce que ça dit pour nous : le nombre de clients (>= 3 000) est largement atteint ; la vraie question est le prix payé, pas le nombre.

### P1-2 : Comptage API, cabinets 69.20Z
- Acteur / marché : activités comptables NAF 69.20Z
- Type : tendance (comptage)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=69.20Z&etat_administratif=A (date : 2026-10-13, API ouverte)
- Citation : « total_results »:10000 (plafond de l'API)
- Chiffres : plafond atteint, le 23 827 de segments.md n'est pas revérifiable sans découpage par département (voir lot suivant si fait). 69.20Z contient aussi des comptables non experts et des commissaires aux comptes.
- Ce que ça dit pour nous : ne pas citer 23 827 comme confirmé sans découpage.

### P1-4 : Obat, prix publics (devis-facture BTP, plateforme agréée via Iopole)
- Acteur / marché : Obat vend un logiciel devis-facture à des artisans du bâtiment
- Type : argent dépensé (prix public ; nombre de payants inconnu)
- Source : https://www.obat.fr/tarifs (date : consultée 2026-10-13, date de page inconnue ; ouverte)
- Citation : « Conforme à la réforme via Iopole, plateforme agréée »
- Chiffres : HT/mois, TPE/PME : Pro 49 € (39 € annuel), Croissance 79 € (69 €), Booster 129 € (109 €). Artisan seul : mêmes montants. Micro : 32/52/95 € (25/45/85 € annuel). Facturation électronique incluse dans chaque offre.
- Ce que ça dit pour nous : les TPE du bâtiment paient 470 à 1 560 €/an HT un logiciel qui inclut la facture électronique : le panier de 580 € est cohérent, mais c'est le prix d'un logiciel, pas d'un service de migration.

### P1-5 : Tolteck, prix publics
- Acteur / marché : Tolteck, devis-facture BTP
- Type : argent dépensé (prix public)
- Source : https://www.tolteck.com/tarifs (date : consultée 2026-10-13, date de page inconnue ; ouverte)
- Citation : « À payer pour 12 mois, soit 228€ pour un an »
- Chiffres : 25 € HT/mois, ou 19 € HT/mois en annuel (228 €/an) ; réduction de plus de 35 % pour les entreprises de moins de 5 ans ; la page dit que Tolteck permet d'être conforme (pas de mention explicite « plateforme agréée »).
- Ce que ça dit pour nous : un acteur BTP vend à 228 €/an : le plancher payé par les TPE du bâtiment est de l'ordre de 230 à 600 €/an.

### P1-6 : Indy, plateforme agréée gratuite (contre-preuve prix)
- Acteur / marché : Indy, indépendants et petites entreprises, offre pour cabinets
- Type : contre-preuve
- Source : https://www.indy.fr/guide/facturation/electronique/gratuit/expert-comptable/ (date : 2026-06-25 selon la page ; ouverte)
- Citation : « permet aux indépendants, auto-entrepreneurs et petites entreprises de gérer leur facturation électronique gratuitement »
- Chiffres : gratuit pour la base ; prix cabinet non indiqué ; marque blanche non mentionnée.
- Ce que ça dit pour nous : la facturation électronique de base est gratuite chez Indy et Tiime (P1-7) : la valeur monnayable est l'accompagnement humain, pas l'outil.

### P1-7 : Tiime Free et Pennylane, prix publics
- Acteur / marché : Tiime (indépendants, TPE, 3 000 cabinets partenaires), Pennylane
- Type : contre-preuve (prix bas) et argent dépensé
- Source : https://www.tiime.fr/tarifs et https://www.pennylane.com/fr/tarifs (date : consultées 2026-10-13 ; ouvertes)
- Citation : « Facturation électronique 100% gratuite. Conformité garantie. » (Tiime) ; « la facturation électronique est incluse dans tous les plans Pennylane, sans surcoût. » (Pennylane)
- Chiffres : Tiime Free 0 € ; Initial 9,99 €/mois ; Smart 17,99 à 49,99 €/mois ; Business 24,99 à 65,99 €/mois (HT). Pennylane indépendants : 7, 14, 24, 79 €/mois HT. Tiime : « choisir parmi nos 3 000 cabinets partenaires ».
- Ce que ça dit pour nous : le logiciel coûte 0 à 24 €/mois pour une TPE ; Tiime est déjà branché sur 3 000 cabinets : le canal cabinet est occupé par des plateformes qui donnent l'outil.

### P1-8 : EBP Bâtiment, aucun prix public
- Acteur / marché : EBP Bâtiment ACTIV / PRO / ELITE
- Type : tendance (aucun prix publié)
- Source : https://www.ebp.com/logiciel-devis-facture-batiment (date : consultée 2026-10-13 ; ouverte)
- Citation : « Devis et factures conformes avec la facturation électronique. »
- Chiffres : les 3 offres sont « Sur devis » : aucun prix public.
- Ce que ça dit pour nous : opacité des prix des éditeurs historiques, mais aucun prix payé vérifiable.

## Lot 2

### P1-9 : Obat sur Trustpilot (peu de faiblesse chez le leader)
- Acteur / marché : Obat
- Type : plainte (et contre-preuve : peu de plaintes)
- Source : https://fr.trustpilot.com/review/obat.fr?stars=1&stars=2 (date : consultée 2026-10-13 ; ouverte)
- Citation : « Aucun suivi client » (2026-05-31) ; « je paie 38.40 euros aujourd'hui 58.80 euros » (2025-11-25)
- Chiffres : note 4,5/5, 696 avis, 5 % de 1-2 étoiles (4 % 1 étoile, 1 % 2 étoiles). Plaintes : support injoignable, hausse de prix.
- Ce que ça dit pour nous : le leader BTP est bien noté ; la faiblesse (support, prix) existe mais est marginale : l'angle « meilleur outil » est faible.

### P1-10 : CAPEB, atelier et afterwork facture électronique (accès + recherche active)
- Acteur / marché : sections CAPEB locales (artisans du bâtiment)
- Type : recherche active (événements de la fédération)
- Source : https://www.capeb.fr/actualites/facturation-electronique-ce-qui-change-pour-les-entreprises-du-batiment-hellip-et-pourquoi-il-faut-s-y-preparer-des-maintenant (date : 2026-05-04 ; ouverte)
- Citation : « L'objectif n'est pas de vendre une plateforme »
- Chiffres : afterwork CAPEB Bas-Rhin le 2026-05-21 avec MAS INFORMATIQUE. Atelier CAPEB Gironde le 2026-02-05 avec In Extenso (https://www.capeb.fr/actualites/facture-electronique-reunion-le-05-02-2026-a-la-capeb-gironde, ouverte).
- Ce que ça dit pour nous : les CAPEB départementales organisent déjà des réunions avec un prestataire (éditeur, cabinet) : canal d'accès réel, mais place déjà prise par des acteurs locaux.

### P1-11 : Un tiers des professionnels pas prêts (confiance faible) et partenariat CAPEB-Costructor
- Acteur / marché : TPE du bâtiment ; CAPEB national et Costructor (logiciel BTP)
- Type : tendance
- Source : https://www.futura-sciences.com/maison/questions-reponses/batiment-facturation-electronique-2026-votre-entreprise-btp-elle-prete-reforme-24760/ (date : 2026-04-01 ; extrait de recherche, non ouverte) ; PDF CAPEB « cp-capeb-costructor-partenariat-facturation-electronique » (illisible)
- Citation : extrait paraphrasé par le moteur, pas verbatim : « un tiers des professionnels ne se sentent pas encore prêts » (source primaire non nommée)
- Chiffres : un tiers pas prêt (confiance faible).
- Ce que ça dit pour nous : la part de TPE pas prêtes n'est pas quantifiée par une source institutionnelle ; la CAPEB a déjà un partenaire logiciel national.

### P1-12 : Droit, périmètre réservé (ordonnance du 19 septembre 1945, art. 2 et 20)
- Acteur / marché : monopole de l'expert-comptable
- Type : obligation (réglementaire)
- Source : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032364676 (version en vigueur depuis 2017-05-08 ; ouverte, texte partiel) ; https://bpifrance-creation.fr/activites-reglementees/expert-comptable (ouverte) ; https://www.eurojuris.fr/articles/monopole-experts-comptables-interdiction-montage-mise-a-disposition-43629.htm (2026-02-27 ; ouverte)
- Citation : « L'expert-comptable fait aussi profession de tenir, centraliser, ouvrir, arrêter, surveiller »
- Chiffres : réservé : tenue, centralisation, arrêté, surveillance des comptabilités de tiers (art. 2) ; exercice illégal : art. 20 ; arrêt Cass. crim. 21 janvier 2026, n° 24-81.008 (condamnation pour mise à disposition de salariés comptables, d'après Eurojuris).
- Ce que ça dit pour nous : migrer un client vers un outil, le former, le paramétrer ne correspond à aucun verbe de l'art. 2 ; saisir ou tenir des écritures le serait. Je n'ai trouvé aucun texte traitant spécifiquement de l'accompagnement à la facture électronique : [HYPOTHÈSE : onboarding, formation et paramétrage hors périmètre réservé], à faire valider par l'Ordre ou un avocat.

### P1-13 : Service-public, calendrier et plateformes agréées
- Acteur / marché : obligation de facturation électronique
- Type : obligation
- Source : https://entreprendre.service-public.gouv.fr/actualites/A15683 (publié 2026-01-19, mis à jour 2026-02-27 ; ouverte)
- Citation : « il est impératif de choisir une plateforme agréée par l'État »
- Chiffres : émission PME et micro : 2027-09-01 ; réception pour tous : 2026-09-01. L'entreprise passe « directement ou au travers d'une solution compatible ».
- Ce que ça dit pour nous : un accompagnateur n'a pas à être plateforme agréée, c'est l'entreprise qui choisit sa plateforme ; un prestataire qui transmettrait lui-même les factures pour le compte d'un client devrait passer par une PA [HYPOTHÈSE à vérifier].

### P1-14 : Italie, la facture électronique obligatoire a produit des services à bas prix
- Acteur / marché : Italie, TPE et artisans (obligation B2B au 2019-01-01)
- Type : argent dépensé (prix) et contre-preuve
- Source : https://quifinanza.it/fisco-tasse/quanto-costa-fattura-elettronica/356738/ (2020-02-28 ; ouverte) ; https://www.fiscozen.it/guide/migliori-software-fatturazione-elettronica-2026/ (tarifs « vérifiés en août 2026 » ; ouverte)
- Citation : « Fatture in Cloud : 48 € + TVA/an » (reformulé du plan Forfettari, cf. Fiscozen)
- Chiffres : Italie, portail officiel gratuit ; logiciels 29 à 49 €/an (2020) ; Fatture in Cloud 48 € HT/an, Aruba 29,90 €/an (2026) ; commercialisti « quelques centaines d'euros » à plus de 1 000 €/an pour une petite entreprise (2020, indicatif) ; Fiscozen (service avec commercialiste) 499 €/an TTC forfettari et 599 €/an artisans et commerçants.
- Ce que ça dit pour nous : en Italie l'outil coûte 30 à 50 €/an ; l'argent est allé à un abonnement récurrent avec comptable (499 à 599 €/an), pas à une migration ponctuelle.

## Lot 3

### P1-3 : Comptage API, BTP non employeur (complément de P1-1)
- Acteur / marché : NAF 43.xx, tranche « NN » ou « 00 » (non employeur, inconnu ou 0 salarié)
- Type : tendance (comptage)
- Source : https://recherche-entreprises.api.gouv.fr/search (même méthode que P1-1, 101 départements) (date : 2026-10-13, API ouverte)
- Citation : « total_results » additionné = 533 437
- Chiffres : 533 437 unités actives de NAF 43 sans salarié (ou effectif inconnu) : surtout micro-entrepreneurs et sociétés unipersonnelles du bâtiment. En plus des 177 400 employeuses de 1 à 9 salariés (P1-1).
- Ce que ça dit pour nous : le vivier brut est de l'ordre de 710 000 entités, mais les 533 k sans salarié paient le plus petit panier (logiciel gratuit ou 7 à 25 €/mois, P1-4 à P1-7).

### P1-15 : Tolteck, CA publié (argent réellement dépensé)
- Acteur / marché : TOLTECK SAS (SIREN 820833028, NAF 58.29C, effectif tranche 12)
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=820833028 (exercice 2025, consulté 2026-10-13 ; API ouverte)
- Citation : « 2025 {'ca': 6793687, 'resultat_net': 2043510} »
- Chiffres : CA 2025 = 6 793 687 € ; résultat net 2 043 510 € (marge nette ~30 %). Au prix de 228 à 300 €/an, ordre de grandeur de 23 000 à 30 000 clients [HYPOTHÈSE de calcul, pas un chiffre publié].
- Ce que ça dit pour nous : un éditeur BTP à 228 €/an réalise 6,8 M€ très rentables : le marché paie, mais un logiciel à bas prix et forte marge.

### P1-16 : Obat, Tiime, Pennylane, CA publiés (contexte)
- Acteur / marché : OBAT (SIREN 852304229), TIIME (831280680 et 823811278), PENNYLANE (880265921)
- Type : argent dépensé (partiel)
- Source : https://recherche-entreprises.api.gouv.fr/search?q=852304229 ; ?q=tiime ; ?q=pennylane (consulté 2026-10-13 ; API ouverte)
- Citation : « 2022 {'ca': 0, 'resultat_net': -2616141} » (Obat) ; « 2025 {'ca': 9711920, 'resultat_net': 476273} » (TIIME)
- Chiffres : Obat : CA à 0 (comptes confidentiels ou non renseignés), résultat 2022 : -2,6 M€. TIIME 2025 : CA 9,71 M€ (entité TIIME SOFTWARE : 9,86 M€, résultat net 2,04 M€). Pennylane 2022 : CA 3,9 M€, résultat -20,4 M€ (non comparable à 2025).
- Ce que ça dit pour nous : les éditeurs vivent d'abonnements logiciels ; aucune donnée publiée sur le CA d'un service d'onboarding.

### P1-17 : Tolteck sur Trustpilot (contre-preuve : très bien noté)
- Acteur / marché : Tolteck
- Type : contre-preuve
- Source : https://fr.trustpilot.com/review/tolteck.com?stars=1&stars=2 (consultée 2026-10-13 ; ouverte)
- Citation : « logiciel non conforme avec les obligations fiscales » (2024-09-26, un expert-comptable)
- Chiffres : note 4,9/5 ; 961 avis ; moins de 2 % de 1-2 étoiles. Plaintes : suspension immédiate du compte en cas d'échec de paiement (2026-01-02), adresse no-reply (2024-09-03).
- Ce que ça dit pour nous : les deux logiciels BTP principaux (Obat 4,5 ; Tolteck 4,9) sont très bien notés : faiblesse des acteurs faible dans le BTP (voir P1-9).

### P1-18 : CAPEB Aube, réunion du 7 avril 2026 (prix, partenaires, canal d'accès)
- Acteur / marché : CAPEB et CNATP de l'Aube, DGFIP, In Extenso, 4 éditeurs
- Type : recherche active (une centaine d'artisans en salle) et contre-preuve (canal déjà occupé)
- Source : https://www.capeb.fr/actualites/facturation-electronique-tout-ce-que-les-artisans-du-btp-doivent-savoir (publié 2026-04-10 ; ouverte)
- Citation : « Personne ne peut vous imposer sa plateforme. »
- Chiffres : « plus de 140 plateformes agréées » à 0,05 à 1,50 € par facture ; une centaine d'artisans de l'Aube ; offres partenaires CAPEB : EBP -25 % la première année, Notim tarif préférentiel ; Kolecto (Crédit Agricole) et Sage Batigest cités.
- Ce que ça dit pour nous : les CAPEB locales réunissent des artisans avec un cabinet et des éditeurs : accès possible, mais la fédération a déjà ses partenaires et dit de « consulter votre expert-comptable ».

### P1-19 : FFB, 50 000 adhérents, E-BTP, offres gratuites
- Acteur / marché : FFB, fédération d'Ille-et-Vilaine
- Type : tendance / contre-preuve
- Source : https://www.ffbatiment.fr/actualites-batiment/actualite/fd35-facturation-electronique-changements-pour-les-entreprises-du-btp (date inconnue ; ouverte)
- Citation : « une plateforme agréée est obligatoire pour toutes les entreprises »
- Chiffres : réseau de 50 000 entreprises, environ deux tiers artisanales ; partenaire E-BTP négocie des conditions préférentielles ; la page dit (paraphrase) que beaucoup de plateformes proposent une offre gratuite ou peu coûteuse et que de nombreux éditeurs BTP intègrent la facturation électronique sans surcoût.
- Ce que ça dit pour nous : l'outil est gratuit ou inclus ; la FFB renvoie vers l'éditeur ou l'expert-comptable ; peu de place pour un intermédiaire à fort panier.

### P1-20 : Baromètre OpinionWay / CNOEC / ECMA 2026 (préparation entreprises et cabinets)
- Acteur / marché : entreprises et cabinets d'expertise comptable
- Type : recherche active / tendance (baromètre d'une instance professionnelle, relayé par Sage)
- Source : https://www.sage.com/fr-fr/blog/expert-comptable-desamorcer-embouteillage-septembre-facture-electronique/ (article du 2026-06-25, baromètre de mai 2026 ; ouverte)
- Citation : « Ce décalage de perception crée un risque d’embouteillage. »
- Chiffres : 35 % des entreprises ont choisi leur plateforme agréée (environ 65 % non) ; 42 % ne connaissent aucune plateforme agréée ; cabinets : 92 % se déclarent engagés, mais 45 % seulement jugent leurs clients réellement engagés.
- Ce que ça dit pour nous : la non-préparation des TPE est mesurée (65 % sans plateforme en mai 2026) ; les cabinets se disent engagés (92 %) : leur besoin de renfort externe n'est pas prouvé.

### P1-21 : Prix d'un accompagnement facturé par un cabinet (confiance faible)
- Acteur / marché : cabinets d'expertise comptable, mission de transition facture électronique
- Type : argent dépensé (prix annoncé, page sponsorisée)
- Source : https://ma-facture-electronique.org/mise-en-conformite/accompagnement-expert-comptable/ (page publiée 2026-06-27, mise à jour 2026-05-29 : dates incohérentes ; ouverte)
- Citation : « Comptez 300 à 500€ HT pour le diagnostic seul »
- Chiffres : diagnostic seul 300 à 500 € HT ; accompagnement complet (diagnostic, mandat opt-in, choix de la PA, tests pilotes) 800 à 2 000 € HT ; forfait comptable 70 à 250 € HT/mois. Page sponsorisée, ni Ordre ni DGFiP : confiance faible. Aucun prix relevé directement chez un cabinet.
- Ce que ça dit pour nous : un panier de 800 à 2 000 € existe sur le papier, mais aucun prix réellement payé n'est prouvé : [HYPOTHÈSE].

### P1-22 : Cegid/Shine, offre PA pour cabinets
- Acteur / marché : Cegid (devenu Shine pour les experts-comptables), plateforme agréée pour cabinets
- Type : argent dépensé (offre existante, prix non publié)
- Source : https://www.cegid.com/fr/blog/ec-imposer-pdp-clients/ (publié 2025-06-12, modifié 2025-10-23 ; ouverte)
- Citation : « Le client reste décisionnaire, même s'il délègue ce choix. »
- Chiffres : aucun prix ; PA pour cabinets ; mandat « opt-in » ; modèles de mandat de l'Ordre annoncés « prochainement » à la date de la page.
- Ce que ça dit pour nous : les gros éditeurs de cabinets (Cegid/Shine, Sage, Pennylane, Tiime avec 3 000 cabinets, Indy) offrent déjà l'infrastructure et le mandat.

### P1-23 : B2Brouter et IOPOLE, plateforme agréée en marque blanche
- Acteur / marché : plateformes proposant la marque blanche à des éditeurs ou cabinets
- Type : argent dépensé (offre existante)
- Source : https://www.b2brouter.net/fr/edocsync-pdp/ (date inconnue ; extrait de recherche, non ouverte)
- Citation : extrait paraphrasé par le moteur, pas verbatim : l'éditeur opère en « Solution Compatible » par API, la plateforme reste invisible
- Chiffres : aucun prix ; IOPOLE propose aussi marque blanche ou solution compatible (via munci.org, extrait).
- Ce que ça dit pour nous : la brique technique en marque blanche est déjà vendue ; notre différence ne pourrait être que l'accompagnement humain.

### P1-24 : Freelance Malt « marque blanche cabinets » (signal faible)
- Acteur / marché : freelance Malt (profil maxenceprouteau) : déploiement en marque blanche de la facture électronique sur le portefeuille d'un cabinet
- Type : argent dépensé (offre existante, prix inconnu)
- Source : https://www.malt.fr/profile/maxenceprouteau (extrait de recherche uniquement ; page en 403, non ouverte)
- Citation : extrait paraphrasé par le moteur : tâches « non réglementées » uniquement
- Chiffres : aucun prix ni avis lisible.
- Ce que ça dit pour nous : le service « onboarding marque blanche » est déjà proposé par au moins un freelance ; rappelle la limite du périmètre réglementé (cohérent avec P1-12).

### P1-25 : Belgique, la transition a été « plus simple que prévu » (contre-preuve)
- Acteur / marché : Belgique, facturation électronique B2B obligatoire depuis 2026-01-01 (Peppol)
- Type : contre-preuve
- Source : https://www.lalibre.be/economie/2026/06/11/peppol-pourquoi-la-facturation-electronique-sest-revelee-plus-simple-que-prevu-en-belgique-JYI5ATRJVJCUNIMIJVIUP6IOJY/ (2026-06-11 ; ouverte) ; enquête ITAA/Banqup : https://www.banqup.com/fr-be/resources/blog/accountants-and-tax-advisers-prepare-businesses-for-e-invoicing-but-75-still-need-to-take-steps (extrait de recherche, non ouverte)
- Citation : « adaptés par leurs éditeurs » (logiciels WinBooks, Exact Online, Odoo, selon La Libre)
- Chiffres : une simple mise à jour a suffi dans de nombreux cas (paraphrase) ; extrait ITAA : 70 % des comptables disent que moins d'un quart de leurs clients étaient prêts (confiance faible, éditeur).
- Ce que ça dit pour nous : en Belgique l'accompagnement est venu du comptable habituel et de l'éditeur, pas de prestataires tiers payants (aucun service tiers payant identifié).

### P1-26 : Allemagne, enquête ZDH sur l'artisanat (coût d'introduction moyen ~3 000 €)
- Acteur / marché : artisanat allemand (ZDH, fédération) ; réception obligatoire 2025, émission 2027-2028
- Type : argent dépensé (coût déclaré) / tendance
- Source : https://www.handwerksblatt.de/betriebsfuehrung/themen-specials/die-e-rechnung-wird-pflicht-tipps-fuer-handwerksbetriebe/zdh-umfrage-im-handwerk-noch-mehr-aufwand-mit-der-e-rechnung (article du 2026-05-18, enquête janvier-février 2026 ; ouverte)
- Citation : « Statt spürbarer Entlastung erleben viele Handwerksbetriebe aktuell vor allem mehr Aufwand »
- Chiffres : près de 2 000 entreprises ; coûts d'introduction « un peu moins de 3 000 € » en moyenne et environ 800 €/an ; 47,4 % jugent la charge plus lourde ; un tiers a des problèmes de lecture des données ; 56 % ont moins de 800 000 € de CA ; près de la moitié des non-émetteurs comptent commencer au 2e semestre 2027.
- Ce que ça dit pour nous : coût d'introduction déclaré proche de 3 000 € (échantillon à CA plus élevé que nos TPE de 1 à 9 salariés ; ~1 200 factures d'achat par an) : le panier français observé via les prix publics est plutôt de 230 à 1 560 €/an.

### P1-27 : Ordre des experts-comptables, taille de la profession
- Acteur / marché : cabinets d'expertise comptable
- Type : tendance
- Source : https://www.experts-comptables.fr/evenement/692fd1d4-9d0e-11f0-8902-00155d038b20 (événement du 2025-10-14 ; ouverte)
- Citation : « plus de 22 000 experts-comptables »
- Chiffres : plus de 22 000 experts-comptables ; partenaires de plus de 7 entreprises sur 10, soit environ 3,5 millions de structures, surtout petites (paraphrase de la page).
- Ce que ça dit pour nous : environ 3,5 M de clients de cabinets, surtout petits ; le besoin d'accompagnement est large, mais les cabinets sont déjà équipés par les gros éditeurs (P1-22).

