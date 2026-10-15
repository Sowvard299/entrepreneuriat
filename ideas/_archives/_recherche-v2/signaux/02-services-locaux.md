# Famille 2 : services locaux éparpillés sans marque (Paris + petite couronne)

- Chercheur : n°2
- Date : 2026-10-13
- Recherches web utilisées : 22 / 25 (plus environ 25 ouvertures directes de pages et des requêtes à l'API Recherche d'entreprises)
- Signaux : 27 (F2-01 à F2-27)
- Sources distinctes (domaines) : 26 (recherche-entreprises.api.gouv.fr, guestready.com, maddyness.com, copeps.fr, journaldeleconomie.fr, futura-sciences.com, consoglobe.com, selectra.info, gravelpassion.fr, reporterre.net, jds.fr, edito.seloger.com, fooderise.com, fr.custplace.com, toute-la-franchise.com, parrainduweb.fr, houst.com, ulysse.com, franchise-magazine.com, largus.fr, forum.quechoisir.org, aladom.fr, travaux.obat.fr, sudradio.fr, questions.assemblee-nationale.fr, lebontri.fr)
- Métiers couverts : conciergerie et ménage Airbnb, ménage à domicile, coiffure / beauté, désinsectisation, nettoyage de bureaux / copropriétés / fin de chantier, serrurerie et dépannage, entretien chaudière, climatisation, réparation de vélos, cordonnerie, nettoyage de canapés, débarras, traiteurs / restauration, lavage auto sans eau, pressing, photographie immobilière, jardinage, nettoyage après décès / Diogène

Note de méthode sur les comptages d'entreprises : API Recherche d'entreprises (`recherche-entreprises.api.gouv.fr`), interrogée le 2026-10-13, filtre `etat_administratif=A` (actives), départements 75 / 92 / 93 / 94. « NN » = tranche d'effectif « unité non employeuse ou effectif inconnu » ; « 00 » = 0 salarié au 31/12. NN + 00 sert d'approximation de « sans salarié ». Le plafond d'affichage de l'API est de 10 000 résultats (un code atteint ce plafond dans le 75). Les codes NAF ne correspondent pas parfaitement aux métiers (une conciergerie Airbnb peut être en 68.32A ou 68.31Z, un laveur de canapé en 81.21Z, 81.29B ou 96.01B).

Les CA cités « via API » viennent du champ `finances` de la même API (comptes publiés au greffe) ; un CA à 0 signifie souvent comptes déposés en mode confidentiel, pas un CA nul.

---

### F2-01 : Conciergeries Airbnb à Paris, commission standard de 20 % ou plus
- Modèle / acteur : GuestReady, HostnFly, WeHost, Checkmyguest gèrent des locations courte durée pour le compte de propriétaires (annonce, check-in, ménage, linge)
- Secteur : immobilier / services aux hôtes | Cible : B2C (propriétaires particuliers)
- Type de signal : argent dépensé
- Source : https://www.guestready.com/fr/blog/comparaison-meilleure-conciergerie-airbnb/ (date : 2025-03-10, mise à jour 2026-08-28)
- Citation : « 20 % TTC des revenus locatifs, hors frais prélevés par les plateformes » (à propos de WeHost)
- Chiffres : HostnFly « à partir de 20 % des revenus générés » ; GuestReady à partir de 20 % + frais d'intégration ; Checkmyguest 20 % courte durée. Ménage facturé en plus, montant non publié. Source rédigée par un concurrent (GuestReady). Comptages API : 68.32A (administration de biens) = 8 285 entreprises actives dans le 75, 1 805 dans le 92, 692 dans le 93, 1 112 dans le 94, dont 85 à 87 % sans salarié déclaré (NN).
- Angle d'amélioration : marché très concurrentiel à Paris et freiné par la réglementation (plafond de nuitées des résidences principales à Paris, loi Le Meur de novembre 2024 [HYPOTHÈSE : effet exact à vérifier]). Angle plus sûr : sous-traiter le ménage et le linge aux conciergeries et aux hôtes autonomes (B2B), plutôt que devenir une conciergerie de plus.

### F2-02 : Wecasa, plateforme de ménage et coiffure à domicile, 12,7 M€ de CA en 2024
- Modèle / acteur : Wecasa met en relation des particuliers avec des indépendants (ménage, coiffure, garde d'enfants, bien-être) et prend une commission
- Secteur : services à domicile | Cible : B2C
- Type de signal : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=wecasa (date : consulté le 2026-10-13, comptes 2024) et https://www.maddyness.com/2025/04/17/wecasa-part-a-la-conquete-de-leurope/ (date : 2025-04-17)
- Citation : « la rentabilité dans les deux pays en 2024 » (Maddyness, France et Royaume-Uni)
- Chiffres : SAS Wecasa (SIREN 822686788), CA 2024 = 12 742 185 €, résultat net 2024 = -1 850 379 € (API). Le CA d'une place de marché correspond en général aux commissions, pas au volume total [HYPOTHÈSE]. Taux de commission cité par des tiers : 20 % (2021) à 25 % (2024), non confirmé par Wecasa. Le Royaume-Uni pèse 15 % du CA (Maddyness).
- Angle d'amélioration : la demande de beauté et ménage à domicile est prouvée et monétisée. Une petite équipe ne battra pas Wecasa sur le généraliste ; elle peut prendre un créneau (ex. une seule prestation très standardisée, une zone, ou une clientèle B2B comme les hôtels sans spa ou les entreprises) avec une marque propre et des intervenants fidélisés.

### F2-03 : Treatwell prend 25 % sur chaque nouveau client des salons, et perd de l'argent
- Modèle / acteur : Treatwell (réservation en ligne coiffure / beauté) facture aux salons un abonnement et une commission d'apport
- Secteur : coiffure / beauté | Cible : B2B (salons) et B2C (clients finaux)
- Type de signal : argent dépensé
- Source : https://copeps.fr/actualites/treatwell-statut-juridique/ (date inconnue) et https://recherche-entreprises.api.gouv.fr/search?q=treatwell (consulté le 2026-10-13)
- Citation : « une commission de 25 % sur les nouveaux clients »
- Chiffres : plan Starter 29 €/mois, 0 % sur les clients fidélisés, 2 % sur les prépaiements en ligne (copeps, non daté). Treatwell FR (SIREN 752044503) : CA 2024 = 11 585 554 €, résultat net 2024 = -7 564 796 € (API). Planity : abonnement fixe sans commission (montant non publié, d'après une recherche web, page source non ouverte). Comptages API coiffure 96.02A : 5 298 entreprises actives (75), 1 866 (92), 2 194 (93), 1 695 (94), dont 54 à 65 % sans salarié déclaré (NN + 00).
- Angle d'amélioration : les salons paient déjà pour être trouvés. Une agence marketing locale spécialisée (fiche Google, Instagram, avis, réservation sans commission) pour salons indépendants peut se vendre contre ces 25 %. Réglementation : coiffure = CAP ou BP obligatoire pour exercer, mais une offre marketing aux salons n'en a pas besoin.

### F2-04 : Punaises de lit, tarifs abusifs dénoncés par le ministre de la Santé
- Modèle / acteur : entreprises de désinsectisation (traitement chimique, vapeur, cryogénie, canon à chaleur, détection canine)
- Secteur : hygiène / nuisibles | Cible : B2C et B2B (bailleurs, hôtels, syndics)
- Type de signal : plainte (et obligation réglementaire)
- Source : https://www.journaldeleconomie.fr/?p=29708 (date : 2023-10-04, plus de 24 mois)
- Citation : « des boites qui leur font payer 2.000 ou 3.000 euros » (Aurélien Rousseau, ministre)
- Chiffres : coût moyen d'environ 1 250 € (chiffre Badbugs) ; insecticide ≈ 400 € pour 50 m² en 2 à 3 passages ; vapeur ou cryogénie ≈ 1 000 € ; canon à chaleur ≈ 2 000 €. Seulement 450 à 480 professionnels agréés selon le ministère (listes publiques). Comptages API 81.29A (désinfection, désinsectisation, dératisation) : 385 (75), 145 (92), 263 (93), 186 (94), dont 75 à 78 % sans salarié déclaré. Un article sponsorisé de mai 2025 (futura-sciences.com, partenaire Sanipure) cite des interventions en hausse de 65 % depuis l'été 2022 (titre d'article lié, non ouvert).
- Angle d'amélioration : marché de confiance (panique, arnaques, garanties non tenues). Une marque transparente (prix publiés, garantie écrite, suivi) a de la place. Réglementation lourde : le Certibiocide est obligatoire pour appliquer des biocides professionnels, ce qui impose soit de se former, soit de sous-traiter à des applicateurs certifiés et de ne faire que la marque et la vente.

### F2-05 : Nettoyage courant des bâtiments, plus de 24 000 entreprises en petite couronne, très majoritairement sans salarié
- Modèle / acteur : ménage de bureaux, parties communes d'immeubles, commerces, logements (NAF 81.21Z), et nettoyage spécialisé (81.22Z : vitres, fin de chantier, industriel)
- Secteur : propreté | Cible : B2B (bureaux, syndics, commerces) et B2C
- Type de signal : tendance (structure de l'offre)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=81.21Z&departement=93&etat_administratif=A&per_page=1 (consulté le 2026-10-13 ; même requête pour 75, 92, 94 et pour 81.22Z)
- Citation : « "total_results":7374 » (81.21Z actives dans le 93)
- Chiffres : 81.21Z = 9 283 (75), 3 559 (92), 7 374 (93), 4 141 (94), soit 24 357 entreprises actives, dont 88 à 90 % sans salarié déclaré (NN) et très peu à « 0 salarié ». 81.22Z = 1 190 (75), 432 (92), 866 (93), 500 (94), dont 62 à 75 % NN. 81.10Z (activités combinées de soutien aux bâtiments) = plus de 10 000 dans le 75 (plafond de l'API), 9 706 (92), 4 293 (93), 5 758 (94).
- Angle d'amélioration : offre ultra-fragmentée faite de micro-entrepreneurs, à côté de quelques grands groupes. Une marque qui agrège des indépendants vérifiés, avec contrat clair, remplacement garanti en cas d'absence et reporting photo, peut viser les petits clients B2B (cabinets, commerces, petites copropriétés) que les grands groupes négligent. Aucune carte professionnelle requise pour le nettoyage courant.

### F2-06 : Dépannage à domicile (serrurerie en tête), 60 % des professionnels contrôlés en infraction
- Modèle / acteur : serruriers, plombiers, chauffagistes, électriciens de dépannage d'urgence
- Secteur : dépannage / bâtiment | Cible : B2C (et B2B : syndics, commerces)
- Type de signal : plainte
- Source : https://www.consoglobe.com/depannage-a-domicile-arnaques-infractions-cg (date : 2025-07-10), qui reprend l'enquête DGCCRF (page officielle economie.gouv.fr bloquée en lecture, voir « Sources non lues »)
- Citation : « 60 % d'entre eux se sont révélés en infraction »
- Chiffres : plus de 600 professionnels contrôlés selon l'article, « près de 548 » selon le tweet DGCCRF cité ; près de 2 600 signalements SignalConso en 2024. D'après un résumé de recherche (page non ouverte), la serrurerie serait le métier du dépannage le plus générateur de plaintes ; non vérifié. Comptages API 43.32B (menuiserie métallique et serrurerie) : 1 579 (75), 599 (92), 1 205 (93), 769 (94), dont 68 à 77 % sans salarié déclaré.
- Angle d'amélioration : le problème central est la confiance (prix annoncé, devis avant travaux, pas de surfacturation). Une marque « dépannage honnête » à prix fixes publiés, avec un réseau d'artisans vérifiés et une garantie, s'attaque à une plainte massive et documentée. Réglementation : pas de carte professionnelle spécifique pour la serrurerie [HYPOTHÈSE : la loi du 5 juillet 1996 impose une qualification pour certains métiers du bâtiment, à vérifier pour la serrurerie] ; le gaz exige une qualification. Risque : l'acquisition se fait sur Google Ads, où les arnaqueurs enchérissent fort.

### F2-07 : Entretien annuel de chaudière, obligation légale, 95 à 300 € par an
- Modèle / acteur : chauffagistes indépendants et réseaux de contrats d'entretien (Savelys, Proxiserve, Garanka)
- Secteur : chauffage / énergie | Cible : B2C (propriétaires, locataires) et B2B (bailleurs, syndics)
- Type de signal : obligation réglementaire (et argent dépensé)
- Source : https://selectra.info/energie/renovation-energetique/chaudiere/gaz/entretien (date : mise à jour 2026-06-12)
- Citation : « l'entretien de la chaudière gaz est une obligation légale »
- Chiffres : décret n° 2009-649 du 9 juin 2009 (chaudières de 4 à 400 kW), attestation remise sous 15 jours. Visite ponctuelle 95 à 110 € (prix-pose.com, septembre 2025) ; contrats annuels : Proxiserve 114 à 276 €/an, Savelys 120 à 298,81 €/an, Garanka 119 à 305 €/an. Pas de sanction directe, mais l'assureur peut réduire l'indemnisation. Comptages API 43.22B (installation thermique et climatisation) : 2 051 (75), 1 020 (92), 1 863 (93), 1 270 (94), dont 57 à 75 % sans salarié déclaré.
- Angle d'amélioration : revenu récurrent et prévisible (abonnement annuel). Une marque locale qui gère la relation client (rappel automatique, prise de rendez-vous en ligne, attestation numérique) et sous-traite la visite à des chauffagistes qualifiés pourrait vendre aux bailleurs particuliers et petits syndics. Réglementation : intervention réservée à un professionnel qualifié ; la climatisation exige en plus une attestation de capacité pour manipuler les fluides frigorigènes [HYPOTHÈSE : détail non vérifié dans cette recherche]. L'équipe ne peut donc pas faire la prestation elle-même.

### F2-08 : Cyclofix, réparation de vélos à domicile, liquidée malgré une forte notoriété (contre-signal)
- Modèle / acteur : Cyclofix, place de marché de réparateurs de vélos indépendants qui se déplacent (Paris et grandes villes)
- Secteur : mobilité / réparation | Cible : B2C et B2B (flottes)
- Type de signal : tendance (contre-signal : modèle qui a échoué)
- Source : https://www.gravelpassion.fr/notre-avis-sur-cyclofix-2/ (date : mise à jour 2024-07-18) et https://recherche-entreprises.api.gouv.fr/search?q=cyclofix (consulté le 2026-10-13)
- Citation : « semble avoir cessé son activité »
- Chiffres : liquidation judiciaire depuis juillet 2023 selon l'article. Cyclofix SAS (SIREN 814300034) : CA 2021 = 1 925 990 €, résultat net 2021 = -2 864 011 € (API), soit une perte supérieure au CA. L'entreprise revendiquait 350 000 vélos réparés en trois ans et 180 réparateurs (déclaratif).
- Angle d'amélioration : la demande existe, mais le modèle « place de marché nationale financée par levée de fonds » a brûlé plus qu'il ne gagnait. Une version locale, rentable dès le départ (B2B : flottes de vélos d'entreprise, résidences, hôtels ; abonnement d'entretien) serait l'angle, à valider. Réglementation : aucun diplôme obligatoire pour réparer des vélos.

### F2-09 : Réparateurs de vélos ambulants, environ 100 créations en 2022
- Modèle / acteur : micro-entrepreneurs réparateurs de vélos mobiles (camionnette ou vélo-cargo)
- Secteur : mobilité / réparation | Cible : B2C
- Type de signal : tendance
- Source : https://reporterre.net/Reparateurs-de-velo-ambulant-un-metier-en-plein-boom (date : 2023-01-05, plus de 24 mois)
- Citation : pas de citation chiffrée retenue ; l'article rapporte environ 100 réparateurs ambulants créés en 2022 (estimation Union sport et cycles)
- Chiffres : environ 300 réparateurs ambulants en France (estimation) ; 2,8 millions de vélos neufs achetés en 2021 ; environ 10 millions de vélos inutilisés sur un parc de 30 millions ; plus de 1 000 offres d'emploi sur Emploi Vélo. Aucun prix ni revenu publié dans l'article.
- Angle d'amélioration : offre éparpillée et sans marque, mais source ancienne et marché post-Covid peut-être retombé [HYPOTHÈSE]. À croiser avec F2-08 : ne pas reproduire le modèle Cyclofix. Comptage API 95.29Z (réparation d'autres biens personnels, dont vélos) : 1 462 (75), 499 (92), 554 (93), 369 (94), dont 82 à 89 % sans salarié déclaré (code large, pas seulement le vélo).

### F2-10 : Minit France (Mister Minit), cordonnerie et clés en réseau, 33,9 M€ de CA
- Modèle / acteur : Minit France, réseau de kiosques de cordonnerie, double de clés, gravure, petites réparations
- Secteur : cordonnerie / réparation | Cible : B2C
- Type de signal : argent dépensé (exemple de métier local « marqué »)
- Source : https://recherche-entreprises.api.gouv.fr/search?q=mister+minit (consulté le 2026-10-13)
- Citation : « "ca": 33885958 » (Minit France, exercice 2024)
- Chiffres : Minit France (SIREN 582120267, NAF 95.29Z, tranche d'effectif 32 = 250 à 499 salariés) : CA 2024 = 33 885 958 €, résultat net 2024 = -1 114 169 €. Comptages API cordonnerie 95.23Z : 349 (75), 130 (92), 115 (93), 110 (94), dont 72 à 73 % sans salarié déclaré.
- Angle d'amélioration : preuve qu'un métier artisanal éparpillé peut être « marqué » à grande échelle, mais la marque perd de l'argent et le modèle exige des emplacements physiques (galeries commerciales) : capital et savoir-faire artisanal hors de portée de l'équipe. Angle plus léger : service de collecte / livraison de réparations (chaussures, maroquinerie) en entreprise, sous-traité à des cordonniers indépendants. Réglementation : pas de diplôme obligatoire, mais immatriculation au répertoire des métiers (artisan).

### F2-11 : Nettoyage de canapés, tapis et matelas à domicile, prix forfaitaires publiés de 59 à 159 €
- Modèle / acteur : Wecleaned (Paris 8e), Éclatys Paris et des dizaines de micro-entreprises : nettoyage par injection-extraction au domicile du client
- Secteur : nettoyage spécialisé | Cible : B2C (et B2B : hôtels, bureaux, locations meublées)
- Type de signal : argent dépensé (prix publiés)
- Source : https://www.jds.fr/paris/immobilier-maison-et-decoration/wecleaned-24075_L (date inconnue)
- Citation : « Canapé 2 – 3 places : Nettoyage complet + détachage 99€ »
- Chiffres : canapé 99 € (2-3 places), 129 € (4-5 places), 159 € (plus de 5) ; matelas 69 € (1 place), 99 € (2 places) ; tapis 59 € (1-2 m²), 89 € (3-4 m²). Une page promotionnelle non datée (copeps.fr, actualites/entreprise-nettoyage-canape) cite 40 à 110 € par canapé en France et revendique l'éligibilité au crédit d'impôt de 50 % des services à la personne [à vérifier]. Une recherche Google sur ce métier remonte surtout des fiches d'annuaire et une page Trustpilot rédigée par l'entreprise elle-même, sans avis clients.
- Angle d'amélioration : prestation courte, standardisable, à panier moyen d'environ 100 € et sans réglementation (pas de diplôme). Le matériel (injecteur-extracteur) est accessible [HYPOTHÈSE : quelques centaines à 2 000 € l'appareil, prix non vérifié]. Une marque claire avec prix fixes, photos avant / après, réservation en ligne et offres groupées (hôtes Airbnb, fin de bail, crèches, bureaux) pourrait se démarquer d'une offre sans visibilité. Récurrence faible chez les particuliers (une fois par an au mieux) [HYPOTHÈSE] : le B2B récurrent est le vrai levier.

### F2-12 : Débarras d'appartements à Paris, successions et départs en EHPAD
- Modèle / acteur : entreprises de débarras (ex. Les Compagnons Débarrasseurs cité en lien), modèle « gratuit si les objets revendables couvrent le coût »
- Secteur : débarras / réemploi | Cible : B2C (héritiers, familles) et B2B (notaires, agences, bailleurs)
- Type de signal : argent dépensé
- Source : https://edito.seloger.com/conseils-d-experts/demenager/debarras-d-appartement-paris-profiter-d-un-service-gratuit-conditions (date : 2025-06-27, publi-communiqué)
- Citation : « Si la valeur estimée couvre le coût de l'intervention »
- Chiffres : un débarras complet coûte « de plusieurs centaines à plusieurs milliers d'euros » selon la surface et le volume. Déclencheurs cités : décès, entrée en maison de retraite, contraintes de délai à Paris, parc ancien. Les fiches d'annuaire observées (PagesJaunes, Cylex) montrent peu d'avis (ex. 9 avis pour une note de 4,3 ; une fiche sans aucun avis), d'après le résumé de recherche.
- Angle d'amélioration : marché de moment de vie (succession, déménagement senior) où le client est pressé, peu informé et méfiant. Une marque de confiance, avec devis sur photos, prix fixe garanti, traçabilité du réemploi (dons, recyclage) et partenariats prescripteurs (notaires, agences immobilières, EHPAD), est faisable sans diplôme. Logistique lourde (camion, déchetterie, main-d'œuvre) à sous-traiter au départ. Aucun comptage NAF fiable (activité dispersée entre collecte de déchets, déménagement et brocante).

### F2-13 : Uber Eats et Deliveroo prennent 15 à 35 % aux restaurants et traiteurs
- Modèle / acteur : plateformes de livraison de repas (Uber Eats, Deliveroo, Just Eat) qui facturent une commission par commande
- Secteur : restauration / traiteur | Cible : B2B (restaurants, traiteurs de quartier)
- Type de signal : argent dépensé
- Source : https://www.fooderise.com/en/platform-fees (date : grilles 2026, jour inconnu ; site qui vend des services aux restaurateurs)
- Citation : « Click & collect at only 7-10% commission. » (Just Eat)
- Chiffres : Uber Eats Lite 15 %, Plus 25 %, Premium 30 % ; Deliveroo 25 à 35 % avec livreur de la plateforme, 15 à 20 % si le restaurant livre ; Just Eat 25 à 30 %, 13 à 14 % en livraison propre, 7 à 10 % en retrait. Comptages API traiteurs 56.21Z : 3 042 (75), 1 104 (92), 1 226 (93), 876 (94), dont 81 à 87 % sans salarié déclaré.
- Angle d'amélioration : les restaurateurs paient très cher l'accès aux clients. Pour une équipe marketing : service de commande directe pour traiteurs et restaurants de quartier (site, Google, fichier clients, commandes de bureaux et d'événements), facturé au forfait plutôt qu'en pourcentage. Concurrence d'outils existants (Zelty, Sunday, etc.) [HYPOTHÈSE : non vérifié ici]. Réglementation : hygiène alimentaire (formation HACCP) pour qui cuisine, pas pour qui fait le marketing.

### F2-14 : Helpling France, plateforme de ménage, plaintes sur les absences et la facturation
- Modèle / acteur : Helpling, plateforme de réservation d'aides ménagères indépendantes ; en France, développement en agences sous licence (2020)
- Secteur : ménage à domicile | Cible : B2C
- Type de signal : plainte
- Source : https://fr.custplace.com/helping (date : avis de 2019 à 2025, le plus récent sur une expérience du 2025-03-25)
- Citation : « Plateforme malhonnête, affiche un tarif et en prélève un autre. » (avis de 2021)
- Chiffres : note 2,5 / 5 sur 38 avis Custplace ; plaintes récurrentes : aide ménagère absente ou en retard, service client injoignable, écarts de facturation. Helpling France (SIREN 803290444) : CA 2019 = 872 520 €, résultat net 2019 = -354 869 € (API). En 2020, Helpling recrutait des porteurs de projet pour ouvrir des « agences digitales » avec un « CA potentiel après 2 ans » de 250 000 € (https://www.toute-la-franchise.com/news-helpling-agence-digitale-menage-repassage-nouveaux-porteurs-projet, date : 2020-07-30). Une enquête journalistique de 2022 sur Helpling en Allemagne et ailleurs évoquait 25 à 41,5 % de commission (source non ouverte).
- Angle d'amélioration : la plainte principale n'est pas le prix mais la fiabilité (absence, remplacement, joignabilité). Une agence de ménage de quartier avec un vrai remplaçant garanti et un interlocuteur joignable répond à cette douleur. Réglementation : ménage à domicile = services à la personne ; la déclaration SAP (gratuite) ouvre le crédit d'impôt de 50 % au client ; pas de diplôme exigé pour le ménage.

### F2-15 : Yoojo, frais de service client de 15 à 20 %, prix horaires publiés par métier
- Modèle / acteur : Yoojo, place de marché de « jobbers » (ménage, bricolage, jardinage, montage de meubles, déménagement)
- Secteur : services à domicile multi-métiers | Cible : B2C
- Type de signal : argent dépensé
- Source : https://parrainduweb.fr/blog/yoojo-tarif (date : 2026-05-19, mise à jour 2026-08-15 ; site de parrainage, fiabilité moyenne)
- Citation : « frais de service Yoojo côté client se situent généralement entre 15 et 20 % »
- Chiffres : tarifs horaires avant frais : ménage / repassage 11 à 28 €/h (moyenne 18 €/h), bricolage 20 à 50 €/h (moyenne 28 €/h), jardinage 15 à 35 €/h (moyenne 22 €/h). La page revendique 384 000 prestataires en France (chiffre non vérifié). Un avis de prestataire sur gowork.fr parle de 20 % de commission (non ouvert). Yoojo SAS (SIREN 821085560) : derniers comptes publiés dans l'API = 2017 (CA 67 496 €), comptes récents non publics.
- Angle d'amélioration : ces prix horaires très bas (ménage à 18 €/h moyen) montrent une offre abondante mais non différenciée. La place est sur le service « géré » à prix plus élevé (sélection, assurance, remplacement), pas sur une place de marché de plus. Réglementation : jardinage et petit bricolage éligibles aux services à la personne dans certaines limites [HYPOTHÈSE : plafonds non vérifiés ici] ; pas de diplôme requis.

### F2-16 : Contrats d'entretien chaudière, Proxiserve pèse 302 M€ de CA
- Modèle / acteur : Proxiserve, Garanka (et Savelys, cité en F2-07) vendent des contrats annuels d'entretien de chaudières, surtout aux bailleurs et aux particuliers
- Secteur : chauffage / maintenance | Cible : B2B (bailleurs sociaux, syndics) et B2C
- Type de signal : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=proxiserve et https://recherche-entreprises.api.gouv.fr/search?q=garanka (consultés le 2026-10-13)
- Citation : « "ca": 302360919 » (Proxiserve, exercice 2025)
- Chiffres : Proxiserve (SIREN 334873726, siège 92300, tranche 51 = 2 000 à 4 999 salariés) : CA 2025 = 302 360 919 €, résultat net = 3 542 565 €. Garanka Nord Ouest : CA 2024 = 18 376 725 € ; Garanka Sud Est : CA 2024 = 12 980 057 € (perte de 1,49 M€) ; Garanka Holding : CA 2024 = 12 421 118 € (perte de 4,62 M€).
- Angle d'amélioration : l'obligation annuelle (F2-07) fait vivre de gros acteurs, ce qui prouve la dépense récurrente. Les petits bailleurs particuliers (quelques logements) et les copropriétés à chauffage individuel sont probablement mal servis par ces groupes orientés grands comptes [HYPOTHÈSE]. Une équipe marketing ne peut pas faire la visite (qualification obligatoire) : le modèle serait un courtier / gestionnaire de rappels qui sous-traite à des chauffagistes partenaires, à marge mince [HYPOTHÈSE].

### F2-17 : Ménage de locations courte durée à Paris, 90 à 210 € par rotation tout compris
- Modèle / acteur : Houst (conciergerie) et prestataires de ménage + linge pour hôtes Airbnb et conciergeries
- Secteur : nettoyage / hébergement | Cible : B2B (conciergeries, hôtes multi-logements) et B2C (hôtes particuliers)
- Type de signal : argent dépensé (prix publiés)
- Source : https://www.houst.com/blog/menage-airbnb-tarifs (date : mise à jour 2026-09-09)
- Citation : « une majoration courante de 20 à 40 pour cent à Paris »
- Chiffres : marché France : studio / T1 25 à 45 € par intervention, T2 / T3 40 à 90 €, maison 90 à 150 € ; linge (lavage, repassage) + 10 à 30 € ; forfaits Houst Paris ménage + linge + produits d'accueil : studio 90 €, 1 chambre 104 €, 2 chambres 128 €, 3 chambres 148 €, 4 chambres 186 €, 5 chambres 210 €. Une offre France Travail d'avril 2025 (non ouverte, résumé de recherche) mentionne une société gérant près de 300 Airbnb à Paris qui recrute des agents de linge.
- Angle d'amélioration : chaque rotation est un achat récurrent, planifié par calendrier, payé par des professionnels. Une offre B2B « rotation + linge hôtelier » fiable (photo-rapport, créneaux garantis le jour même, gestion des imprévus) pour les conciergeries qui sous-traitent est un modèle simple sans diplôme. Risque majeur : voir F2-18 (réglementation qui réduit le nombre de nuits louées).

### F2-18 : Locations meublées à Paris, volume énorme mais réglementation qui se durcit (signal mixte)
- Modèle / acteur : Airbnb et hôtes de meublés de tourisme à Paris
- Secteur : hébergement courte durée | Cible : B2C (hôtes) / B2B (conciergeries)
- Type de signal : obligation réglementaire (contre-signal pour F2-01 et F2-17)
- Source : https://ulysse.com/news/paris-taxe-sejour-airbnb-2026-hausse (date : 2026-05-12)
- Citation : « Le tarif n'est pas forfaitaire : il dépend du prix de la nuit. » (taxe de séjour)
- Chiffres : Airbnb a reversé 26,8 M€ de taxe de séjour à la Ville de Paris en 2025 (selon l'article), ce qui indique un volume de nuitées très important. Loi Le Meur du 19 novembre 2024 : les communes peuvent limiter à 90 jours par an la location de la résidence principale ; numéro d'enregistrement obligatoire à 13 chiffres ; abattement micro-BIC des meublés non classés ramené à 30 % dans la limite de 15 000 €. Taxe de séjour parisienne jusqu'à 15,93 € par personne et par nuit.
- Angle d'amélioration : le marché reste gros, mais la pression réglementaire et fiscale réduit les marges des hôtes et pousse une partie des logements vers la location moyenne durée (bail mobilité) [HYPOTHÈSE]. Une offre de services aux hôtes doit fonctionner aussi pour la moyenne durée (ménage de sortie, linge, état des lieux).

### F2-19 : Lavage automobile sans eau sur parkings, réseaux de franchise orientés B2B (sources anciennes)
- Modèle / acteur : Sineo, Ecolave : lavage de véhicules sur site (parkings d'entreprises, concessions, flottes), sans station
- Secteur : entretien automobile | Cible : B2B (90 % des interventions selon Sineo) et B2C
- Type de signal : argent dépensé (sources de plus de 24 mois)
- Source : https://www.franchise-magazine.com/news-franchise/sineo-redemarre-sur-de-nouvelles-bases (date : 2014-01-16) et https://www.largus.fr/pros/actualite-automobile/ecolave-ouvre-une-master-franchise-en-suisse-4212379.html (date : 2014-06-02)
- Citation : « le droit d'entrée est, en France, de 5 500 euros » (Ecolave)
- Chiffres : Sineo : 25 centres en 2014 ; 70 % du CA avec les professionnels de l'automobile, 20 % collectivités et entreprises, 10 % particuliers ; redevance fixe de 250 à 1 000 €/mois. Ecolave : une quarantaine d'agences en France en 2014, CA annuel moyen de 100 000 € communiqué par le dirigeant (sans préciser s'il s'agit d'un CA par agence). Aucune donnée récente trouvée.
- Angle d'amélioration : modèle à faible investissement (droit d'entrée de quelques milliers d'euros en 2014), B2B récurrent (flottes, concessions, parkings de bureaux, loueurs, autopartage). Données trop anciennes pour conclure : il faudrait vérifier si ces réseaux existent encore et ce que paient aujourd'hui les gestionnaires de flottes. Réglementation : aucun diplôme ; à Paris, usage de l'espace public et rejets d'eau à vérifier [HYPOTHÈSE].

### F2-20 : StarOfService, les artisans se plaignent de payer des mises en relation sans garantie
- Modèle / acteur : StarOfService, annuaire / place de marché qui fait payer les professionnels par crédits à chaque réponse à une demande client
- Secteur : mise en relation multi-métiers (artisans, coachs, photographes...) | Cible : B2B (indépendants) et B2C (demandeurs)
- Type de signal : plainte (sources de plus de 24 mois)
- Source : https://forum.quechoisir.org/starofservice-t121276.html (date : messages du 2017-10-20 au 2018-10-14)
- Citation : « vous ponctionnent automatiquement 15 € » (message du 2018-10-14)
- Chiffres : débit d'environ 15 € par réponse à un client, sans garantie d'obtenir le contrat ; hausses successives du prix de mise en relation après l'activation obligatoire de l'« Autopilot » (réponses automatiques) en 2017-2018. D'après un résumé de recherche (autres fils non ouverts), un abonnement premium de 342 € pour 3 mois aurait été prélevé à un professionnel. StarOfService SAS (SIREN 751713215) : comptes 2023 publiés sans CA (confidentiels), résultat net -18 329 € (API).
- Angle d'amélioration : les indépendants paient déjà pour trouver des clients, mais détestent payer des contacts non qualifiés. Pour une équipe marketing, deux pistes : (1) vendre aux artisans d'un métier précis un service de visibilité locale à forfait (fiche Google, avis, site simple) plutôt qu'au contact ; (2) monter sa propre marque de services et garder les clients au lieu de louer l'accès. Données anciennes, à recouper avec des avis récents.

### F2-21 : Photographie immobilière à Paris, offre pléthorique d'indépendants, tarifs de 80 €/h à 450 €/jour
- Modèle / acteur : photographes indépendants qui vendent aux agences immobilières, hôtes Airbnb et conciergeries (photos, visite virtuelle 360°, drone)
- Secteur : photographie / immobilier | Cible : B2B (agences, conciergeries) et B2C (vendeurs particuliers, hôtes)
- Type de signal : argent dépensé (prix publiés)
- Source : https://www.aladom.fr/photographe/paris_18eme-75/photographe-immobilier-et-architecture-6lv8 (date inconnue)
- Citation : « Tarif : 80,00 € / heure » (photographe immobilier, Paris 18e)
- Chiffres : comptages API 74.20Z (activités photographiques) : 7 371 (75), 2 223 (92), 1 653 (93), 1 629 (94), dont 96 à 97 % sans salarié déclaré, soit l'offre la plus atomisée de cette recherche. D'après un résumé de recherche sur des profils Malt (pages non ouvertes, Malt bloque la lecture), les tarifs iraient d'environ 125 €/jour à 449 €/jour, avec des formules à 200 € (25 photos) et 380 € (50 photos).
- Angle d'amélioration : offre surabondante et peu chère : difficile d'en faire une marque rentable, sauf en vendant un paquet complet aux conciergeries et agences (photos + annonce optimisée + visite virtuelle + home staging léger) à prix fixe. Pas de diplôme requis ; le drone exige une formation et un enregistrement de télépilote [HYPOTHÈSE : règles exactes non vérifiées]. Signal plutôt négatif (saturation).

### F2-22 : Grille de prix du nettoyage professionnel en 2026 : fin de chantier 20 à 35 €/m²
- Modèle / acteur : entreprises de propreté (bureaux, parties communes de copropriété, vitres, fin de chantier)
- Secteur : propreté B2B | Cible : B2B (bureaux, syndics, commerces, entreprises du bâtiment, promoteurs)
- Type de signal : argent dépensé (prix publiés)
- Source : https://travaux.obat.fr/guides/tarif-nettoyage-m2/ (date : 2026-06-04, mise à jour 2026-06-09)
- Citation : « Le tarif de nettoyage varie entre 20 et 35 €/m2 selon l'ampleur du chantier. »
- Chiffres : bureaux 3 à 9 €/m² ; parties communes de copropriété 4 à 10 €/m² en moyenne (forfaits mensuels possibles) ; vitres 20 à 40 €/h ou 3 à 8 €/m² ; nettoyage courant 20 à 40 €/h ; fin de chantier 20 à 35 €/m². Moyennes nationales, non spécifiques à Paris. Le nettoyage des parties communes relève du syndic, qui signe le contrat et peut réclamer une indemnisation si le cahier des charges n'est pas respecté (bailfacile.fr, résumé de recherche, page non ouverte).
- Angle d'amélioration : la fin de chantier est le segment le mieux payé au m², avec des clients professionnels (artisans, entreprises de rénovation, promoteurs, particuliers en fin de travaux) qui ont une échéance (livraison, état des lieux). Une offre fiable « chantier rendu propre sous 48 h » vendue aux entreprises de rénovation parisiennes est simple à tester. Aucune carte professionnelle ; assurance responsabilité civile professionnelle indispensable.

### F2-23 : SoyezBCBG, pressing et cordonnerie à domicile à Paris, fermé après des pertes (contre-signal)
- Modèle / acteur : SoyezBCBG collectait vêtements et chaussures à domicile ou au bureau, les confiait à des pressings et cordonniers partenaires, puis les livrait sous 48 h
- Secteur : pressing / cordonnerie | Cible : B2C (actifs parisiens) et B2B (conciergeries d'entreprise)
- Type de signal : tendance (contre-signal : modèle qui a échoué)
- Source : https://recherche-entreprises.api.gouv.fr/search?q=soyezbcbg (consulté le 2026-10-13) ; contexte : levée de 400 000 € en 2016 selon un résumé de recherche (article maddyness.com du 2016-09-22, non ouvert)
- Citation : « "etat_administratif": "C" » (entreprise cessée)
- Chiffres : SoyezBCBG (SIREN 807557210, Paris 1er) : CA 2019 = 657 042 €, résultat net 2019 = -468 941 € ; entreprise cessée. Comptages API 96.01B (blanchisserie-teinturerie de détail, dont pressings) : 1 132 (75), 482 (92), 468 (93), 393 (94), dont 67 à 74 % sans salarié déclaré.
- Angle d'amélioration : la collecte-livraison à l'unité coûte plus cher que la marge du pressing. Si le modèle est repris, ce doit être en tournées groupées (entreprises, résidences, hôtels, hôtes Airbnb) et non en B2C à la demande. Pas de diplôme pour le pressing, mais réglementation sur les installations classées et les solvants pour qui exploite un atelier [HYPOTHÈSE : détail non vérifié].

### F2-24 : O2 et Shiva, réseaux qui ont « marqué » le ménage à domicile, 60 à 70 M€ de CA chacun
- Modèle / acteur : O2 Care Services (ménage, garde d'enfants, aide aux seniors, jardinage) et Shiva (ménage et repassage, groupe Acadomia), réseaux d'agences en propre et en franchise
- Secteur : services à la personne | Cible : B2C
- Type de signal : argent dépensé (exemple de métier éparpillé « marqué »)
- Source : https://recherche-entreprises.api.gouv.fr/search?q=o2+developpement et https://recherche-entreprises.api.gouv.fr/search?q=shiva+menage+repassage (consultés le 2026-10-13)
- Citation : « "ca": 72483289 » (O2 Développement, exercice 2025)
- Chiffres : O2 Développement (SIREN 452022858, Le Mans, tranche 32 = 250 à 499 salariés) : CA 2025 = 72 483 289 €, résultat net = 5 918 120 €. Shiva Groupe (SIREN 443977871, Paris 8e, entité qui porte aussi Acadomia d'après son nom) : CA 2025 = 63 820 120 €, résultat net = 1 338 261 €. Ces CA ne couvrent qu'une partie des réseaux (les franchisés ont leurs propres comptes) [HYPOTHÈSE sur le périmètre].
- Angle d'amélioration : preuve que le ménage à domicile, métier très éparpillé, peut porter des marques rentables grâce au crédit d'impôt de 50 % et à la récurrence (client hebdomadaire). Entrer face à eux en généraliste est difficile ; un créneau peut marcher (ex. ménage + linge pour petites surfaces locatives, ménage de bureaux de moins de 10 personnes, villes de petite couronne peu couvertes). Réglementation : déclaration SAP pour le crédit d'impôt ; agrément SAP seulement pour les publics fragiles (enfants de moins de 3 ans, seniors) [HYPOTHÈSE : règle à vérifier].

### F2-25 : Climatisation, ventes « jamais vues » en septembre 2026 après six semaines de canicule
- Modèle / acteur : installateurs et vendeurs de climatisation réversible pour particuliers
- Secteur : climatisation / génie thermique | Cible : B2C (et B2B : commerces, bureaux)
- Type de signal : argent dépensé (et tendance)
- Source : https://www.sudradio.fr/sud-radio/la-vente-de-climatisation-explose-en-septembre-avec-la-chaleur-qui-persiste (date : 2026-09-22)
- Citation : « pour être sûrs d'être servis » (clients prêts à faire poser pendant l'année)
- Chiffres : six semaines de canicule, températures moyennes autour de 30 °C ; une cliente a fait réaliser environ 4 000 € de travaux. Pas de chiffre de ventes global dans l'article. D'après un résumé de recherche (pages non ouvertes : selectra.info, labomaison.com, capeb.fr), l'entretien d'une clim réversible coûte 100 à 300 €, une installation 2 000 à 15 000 €, et l'attestation de capacité « fluides frigorigènes » est obligatoire depuis le 4 juillet 2009 pour toute entreprise qui intervient sur ces équipements.
- Angle d'amélioration : demande forte, saisonnière et en croissance, avec des installateurs saturés l'été. Mais métier réglementé (attestation de capacité, RGE pour les aides) : l'équipe ne peut pas poser elle-même. Angle possible : contrats d'entretien annuels clim + chaudière (voir F2-07) vendus hors saison, exécutés par des partenaires certifiés.

### F2-26 : Jardinage à domicile, crédit d'impôt de 50 % jusqu'à 5 000 €, mais activité en baisse et dispositif menacé
- Modèle / acteur : entreprises de « petits travaux de jardinage » déclarées services à la personne (tonte, taille de haies, désherbage)
- Secteur : jardinage / espaces verts | Cible : B2C (maisons avec jardin de la petite couronne) et B2B (copropriétés)
- Type de signal : obligation réglementaire (cadre fiscal) et plainte des professionnels
- Source : https://questions.assemblee-nationale.fr/q17/17-18071QE.htm (date : 2026-09-08, question écrite de Mme Anne-Sophie Ronceret)
- Citation : « forte diminution de l'activité » (après canicules et sécheresse depuis le printemps 2026)
- Chiffres : crédit d'impôt de 50 % dans la limite de 5 000 € de dépenses par an et par foyer pour le jardinage (soit 2 500 € d'avantage maximal, d'après un résumé de recherche citant l'article D7233-5 du Code du travail). Les professionnels demandent le maintien du taux de 50 % et du plafond de 5 000 € dans le projet de loi de finances 2027 ; pas de réponse du gouvernement à la date de lecture. Comptages API 81.30Z (aménagement paysager) : 816 (75), 440 (92), 429 (93), 451 (94), dont 63 à 83 % sans salarié déclaré.
- Angle d'amélioration : modèle fortement dépendant de la niche fiscale et de la météo ; pas prioritaire. Utile seulement comme service complémentaire (ex. entretien de petites cours et terrasses, copropriétés). Pas de diplôme requis pour les petits travaux ; l'usage de produits phytosanitaires est encadré [HYPOTHÈSE : non vérifié].

### F2-27 : Nettoyage après décès et syndrome de Diogène, une place de marché dédiée à Paris
- Modèle / acteur : Lebontri, plateforme qui publie des demandes de nettoyage extrême (Diogène, après décès, débarras) et les fait chiffrer par des entreprises spécialisées
- Secteur : nettoyage extrême / hygiène | Cible : B2B (bailleurs sociaux, mandataires judiciaires, notaires, services sociaux) et B2C (familles)
- Type de signal : recherche active (des clients publient des demandes)
- Source : https://lebontri.fr/nettoyage-syndrome-diogene/paris (date : contenu le plus récent du 2026-02-26)
- Citation : « Annonce réservée aux professionnels spécialisés »
- Chiffres : aucun tarif publié ; estimation gratuite sur photo, acompte de 10 % à la publication de l'annonce, déduit du devis retenu. Clients ciblés : familles, tuteurs, mandataires judiciaires, bailleurs et bailleurs sociaux, services sociaux, notaires. D'après un résumé de recherche (guide national non ouvert), ces interventions coûteraient 25 à 60 €/m² selon l'insalubrité.
- Angle d'amélioration : prestation chère, urgente, peu comparée, avec des prescripteurs professionnels identifiables (bailleurs sociaux, mandataires, notaires) : un bon terrain pour une marque de confiance qui coordonne débarras + nettoyage + désinsectisation + petite remise en état. Contraintes : risques biologiques (formation, équipements de protection), désinsectisation soumise au Certibiocide (voir F2-04) ; la coordination peut être faite par l'équipe, l'exécution sous-traitée au départ.

---

## Synthèse

Lecture d'ensemble : les comptages API confirment une offre très éparpillée (de 54 % à 97 % d'entreprises sans salarié déclaré selon le métier). Deux familles de modèles ressortent. (a) Les métiers « marqués » qui marchent sont récurrents et soutenus par une obligation ou une niche fiscale (ménage SAP, entretien chaudière). (b) Les places de marché nationales financées par levée de fonds perdent souvent de l'argent (Treatwell FR, Cyclofix, SoyezBCBG, Helpling France) : le bon angle pour l'équipe est une marque locale de service géré, pas une plateforme de plus.

1. **Ménage + linge pour locations meublées (rotations B2B)**. Qui paie : conciergeries et hôtes multi-logements. Combien : 25 à 90 € par rotation hors linge, 90 à 210 € tout compris à Paris. Ce qui ne va pas : fiabilité des prestataires, conciergeries qui prennent 20 % ou plus et margent sur le ménage. Risque : réglementation (loi Le Meur, 90 jours). Signaux : F2-01, F2-17, F2-18, F2-05.

2. **Nettoyage de fin de chantier pour entreprises de rénovation**. Qui paie : artisans, entreprises de rénovation, promoteurs, particuliers en fin de travaux. Combien : 20 à 35 €/m², le prix au m² le plus élevé de la propreté. Ce qui ne va pas : offre atomisée (plus de 3 000 entreprises 81.22Z en petite couronne, majoritairement sans salarié), peu de marques. Signaux : F2-22, F2-05.

3. **Nettoyage de canapés, tapis et matelas à prix fixes**. Qui paie : particuliers, hôtes, bureaux, hôtels. Combien : 59 à 159 € par pièce. Ce qui ne va pas : aucune marque visible, des fiches d'annuaire sans avis. Pas de diplôme, matériel accessible. Limite : récurrence faible en B2C, d'où l'intérêt de paquets B2B. Signaux : F2-11, F2-17.

4. **Dépannage « honnête » à prix fixes publiés (serrurerie, plomberie)**. Qui paie : particuliers en urgence, syndics, commerces. Ce qui ne va pas : 60 % des dépanneurs contrôlés en infraction, 2 600 signalements en 2024. Limites : métiers techniques (l'équipe ne fait que la marque et la sélection), acquisition coûteuse sur Google. Signaux : F2-06, F2-20.

5. **Contrats d'entretien chaudière + clim pour petits bailleurs et copropriétés**. Qui paie : propriétaires, locataires, bailleurs. Combien : 95 à 300 € par an et par équipement ; Proxiserve fait 302 M€ de CA. Ce qui ne va pas : services pensés pour les grands comptes, prise de rendez-vous pénible [HYPOTHÈSE]. Limite : qualification obligatoire, donc sous-traitance. Signaux : F2-07, F2-16, F2-25.

6. **Débarras + nettoyage extrême (succession, Diogène, après décès)**. Qui paie : héritiers, bailleurs sociaux, mandataires, notaires. Combien : de plusieurs centaines à plusieurs milliers d'euros par intervention. Ce qui ne va pas : client pressé et méfiant, peu d'avis, aucune marque de référence. Signaux : F2-12, F2-27, F2-04.

7. **Marketing local à forfait pour indépendants qui paient des commissions** (salons de coiffure, traiteurs, artisans). Qui paie : salons (25 % par nouveau client chez Treatwell), restaurants (15 à 35 % chez Uber Eats / Deliveroo), artisans (environ 15 € par contact chez StarOfService). Ce qui ne va pas : commissions jugées trop lourdes, contacts non qualifiés. C'est le modèle le plus proche du profil marketing de l'équipe, sans réglementation. Signaux : F2-03, F2-13, F2-20.

8. **Ménage à domicile de créneau (petites surfaces, petits bureaux, villes de petite couronne)**. Qui paie : particuliers (crédit d'impôt de 50 %), petites entreprises. Preuve : O2 (72,5 M€) et Shiva (63,8 M€) rentables, Wecasa 12,7 M€. Ce qui ne va pas : absences, remplacements, joignabilité (Helpling 2,5/5). Limite : marché très concurrentiel. Signaux : F2-02, F2-14, F2-15, F2-24.

Modèles écartés ou contre-signaux : réparation de vélos à domicile (F2-08, F2-09 : Cyclofix liquidé), pressing à domicile (F2-23 : SoyezBCBG cessé), photographie immobilière (F2-21 : saturation), jardinage (F2-26 : activité en baisse et niche fiscale menacée), désinsectisation en direct (F2-04 : Certibiocide), lavage auto sans eau (F2-19 : données trop anciennes pour conclure), conciergerie Airbnb généraliste (F2-01 : concurrence et réglementation).

## Sources non lues

- https://old.reddit.com/r/paris/search?q=plombier... : WebFetch refusé (« unable to fetch from old.reddit.com ») et navigateur intégré bloqué (« not allowed due to safety restrictions »). Aucune plainte Reddit n'a donc été relevée.
- https://www.economie.gouv.fr/dgccrf/secteur-du-depannage-domicile-64-des-entreprises-controlees-par-les-services-de-la-dgccrf : 403 (chiffres repris via consoglobe.com).
- https://www.pappers.fr : 403 (CA obtenus via le champ `finances` de l'API Recherche d'entreprises).
- https://www.frenchweb.fr/planity-treatwell-ou-fresha-quelle-plateforme-choisir-pour-son-salon-de-coiffure-ou-de-soins-esthetiques/463489 : 404.
- https://www.ootravaux.fr/installation-entretien/chauffage/chaudiere/prix-entretenir-chaudiere.html : 403.
- https://www.travaux.com/blog/penurie-main-oeuvre-metiers-du-batiment : 403 (étude 2025 sur la pénurie d'artisans non lue).
- Infographie Ipsos « Métiers du bâtiment » (2024-04-16, ipsos.com) : PDF téléchargé mais illisible (texte compressé, pas d'outil de rendu).
- https://labomaison.com/maison/ventilateur/penurie-installateurs-climatisation-delais/ : 403.
- https://www.helpling.fr/prix : 404.
- Profils Malt (photographes immobiliers) : non ouverts, Malt bloque la lecture automatique.
- Non trouvé : taux de commission officiel publié par Yoojo, Helpling, Wecasa (seulement des sources tierces) ; chiffres récents sur le lavage auto sans eau et sur la réparation de vélos.
