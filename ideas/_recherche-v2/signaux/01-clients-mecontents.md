# Famille 1 : clients qui paient mais sont mécontents

- Chercheur : n°1
- Date : 2026-10-13
- Recherches web utilisées : 5 / 25 (le reste en ouverture directe WebFetch, environ 45 pages)
- Nombre de signaux : 28 (dont 3 contre-signaux : F1-19, F1-27, F1-28)
- Sources distinctes (domaines) : 13 (fr.trustpilot.com, demeco.fr, hostnfly.com, sedomicilier.fr, legalstart.fr, ornikar.com, dougs.fr, mesdepanneurs.fr, matera.eu, consoglobe.com, fnaim.fr, forum.quechoisir.org, recherche-entreprises.api.gouv.fr)
- Limite : 25 signaux sur 28 reposent sur Trustpilot. Les avis Google et des stores d'applications n'ont pas pu être lus automatiquement.

Méthode : pour chaque acteur, ouverture de la page Trustpilot globale (note, nombre d'avis, répartition des étoiles) puis de la page filtrée 1-2 étoiles (`?stars=1&stars=2`, 20 avis les plus récents). Les « 3 reproches » sont un classement fait à la main sur ces 20 avis récents ; la part de 1-2 étoiles est celle affichée par Trustpilot sur l'ensemble des avis. Biais connu : Trustpilot sur-représente les avis sollicités par l'entreprise (souvent 5 étoiles) et les avis de colère (1 étoile). Une part de 1-2 étoiles de 15 % ou plus sur un acteur qui sollicite ses avis est donc un signal fort.

---

## Signaux

### F1-01 : Déménagement (Demeco) : casse et litiges d'indemnisation
- Modèle / acteur : Demeco, réseau de déménageurs (franchisés indépendants), déménagement particuliers sur devis
- Secteur : déménagement | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.demeco.fr?stars=1&stars=2 (date : avis de 2025-11 à 2026-09) ; https://www.demeco.fr/ (date inconnue)
- Citation : « Prix remis en cause à la livraison malgré facture émise 48h plus tôt » (JYP, 2026-05-05)
- Chiffres : 511 avis Trustpilot, note 4,1/5 ; 1 étoile 25 %, 2 étoiles 3 % (soit 28 % de 1-2 étoiles). Prix : aucun tarif public ; le site cite seulement une fourchette de « 500 à 900 euros » pour 15 m³. Volume revendiqué : « 100 000 déménagements chaque année » (page d'accueil ; un autre article du même site dit « plus de 70 000 foyers », chiffres non réconciliés).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Casse et dégâts (environ 15 avis) : « Ils nous ont tout abîmé, aucune precotion de prise » (Viviani Damien, 2026-07-24)
  2. Indemnisation refusée ou sans réponse, la lettre de voiture signée sert à rejeter la réclamation (environ 15 avis) : « La lettre de voiture se signe pour attester que tout a été livré sans dommage » (David, 2026-06-01)
  3. Organisation (retards, sous-effectif, sous-traitance, annulation la veille) (environ 9 avis) : « Déménagement annulé la veille alors que la date avait été confirmée par téléphone » (F. Grumblatt, 2026-06-22)
- Angle d'amélioration : un déménageur ou courtier de déménagement à Paris / petite couronne qui vend la transparence : prix ferme au m³ affiché en ligne, inventaire vidéo, photos avant / après de chaque meuble, constat contradictoire au déchargement, procédure de réclamation en 72 h écrite d'avance. Le réseau « marque nationale + franchisés » crée un flou de responsabilité (« n'est en fait qu'un réseau d'indépendants », J. Lancery, 2025-12-17) : une marque unique avec un seul interlocuteur répond directement à ce reproche. Modèle possible sans camion : courtier qui sous-traite à des déménageurs notés et garantit lui-même le suivi.

### F1-02 : Plateforme de garde d'enfants (Yoopies) : payer pour parler, profils peu fiables
- Modèle / acteur : Yoopies, place de marché de baby-sitters / nounous / aide à domicile, abonnement payant côté parents
- Secteur : garde d'enfants | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.yoopies.fr?stars=1&stars=2 (date : avis de 2025-10 à 2026-10)
- Citation : « Ils forcent un abonnement hors de prix (35e par mois) » (Paul, 2026-01-23)
- Chiffres : 1 162 avis Trustpilot, note 3,2/5 ; 1 étoile 13 %, 2 étoiles 2 % (15 % de 1-2 étoiles). Prix : 35 €/mois selon plusieurs avis (pauline conti, 2026-09-25 ; Paul, 2026-01-23) ; page tarifs publique non trouvée (https://www.yoopies.fr/tarifs renvoie 404).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Profils datés, faux ou peu fiables, absences et annulations (environ 8 avis) : « le taux d'annulation étant très élevé ce service n'est pas fiable » (Jipp, 2026-07-24)
  2. Abonnement obligatoire pour simplement contacter quelqu'un (environ 7 avis) : « Il faut payer une blinde pour devoir parler aux gens ! » (Nobody, 2026-10-08)
  3. Renouvellement sans consentement, résiliation difficile (environ 7 avis) : « il est pratiquement impossible de se désabonner » (Tiny, 2026-07-08)
- Angle d'amélioration : une agence ou un collectif de garde d'enfants / baby-sitting local (un arrondissement ou une ville de petite couronne) qui vérifie les profils en vrai (entretien, références appelées), garantit un remplaçant en cas d'absence et facture à la prestation, pas à l'abonnement. Le crédit d'impôt de 50 % (service à la personne) rend le prix acceptable pour les familles. Différenciation marketing simple : « zéro abonnement, remplaçant garanti sous 24 h ».

### F1-03 : Plateforme de réservation de garages (Vroomly) : prix affichés non tenus, rendez-vous fantômes
- Modèle / acteur : Vroomly, comparateur et prise de rendez-vous en ligne avec des garages partenaires (entretien, freins, courroie...)
- Secteur : auto (entretien) | Cible : B2C
- Type de signal : plainte (+ argent dépensé chez les garages)
- Source : https://fr.trustpilot.com/review/www.vroomly.com?stars=1&stars=2 (date : avis de 2026-06 à 2026-09)
- Citation : « Le devis du garage est le double de celui annoncé sur le site » (serge pico, 2026-09-30)
- Chiffres : 660 avis Trustpilot, note 2,3/5 ; 1 étoile 31 %, 2 étoiles 3 % (34 % de 1-2 étoiles). Prix : service gratuit pour le client, la plateforme se rémunère sur les garages [HYPOTHÈSE : modèle de commission, non vérifié sur une page tarifs] ; écart de prix cité : « le montant réel était de 149 euros et non 69 euros » (Tony Rodrigues, 2026-06-14).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Rendez-vous non transmis, non confirmés ou annulés, garage pas au courant (environ 10 avis) : « Fixe des rdv alors que le garage n'est même pas au courant » (Amelie B, 2026-06-27)
  2. Prix réel très supérieur au prix affiché (environ 5 avis) : « Tarifs mensongers ne correspondant pas au prix pratiqué » (Isabelle Aslanian, 2026-06-26)
  3. Garages inadaptés ou réparations mal faites (environ 4 avis) : « un garage qui ne fait que du remplacement de vitres » (Jo, 2026-09-03)
- Angle d'amélioration : le besoin (devis comparés, rendez-vous rapide) est réel mais la promesse « prix en ligne » n'est pas tenue. Une petite équipe peut faire mieux sur une zone réduite : sélection de 15 à 30 garages partenaires en petite couronne, rendez-vous confirmé par téléphone par un humain, prix garanti ou différence remboursée. Variante : service de convoyage « on prend votre voiture, on la ramène » (jockeying) pour actifs parisiens sans voiture de remplacement.

### F1-04 : Syndic et gestion locative (Foncia) : injoignable, comptes faux
- Modèle / acteur : Foncia, premier administrateur de biens en France (syndic de copropriété, gestion locative, location)
- Secteur : immobilier (syndic de copropriété, gestion locative) | Cible : B2C (copropriétaires, bailleurs, locataires)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.foncia.com?stars=1&stars=2 (date : avis de 2025-10 à 2026-10)
- Citation : « Il faut appeler 20 fois, attendre des heures au téléphone » (avis gestion locative, 2026-09-01)
- Chiffres : 17 500 avis Trustpilot (« 18 k » dans le résumé), note 4,1/5 ; 1 étoile 24 %, 2 étoiles 3 % (27 % de 1-2 étoiles). Prix : honoraires de syndic non publiés sur la page lue (date inconnue) [HYPOTHÈSE : forfait annuel par lot, fixé au contrat de syndic].
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Gestionnaire injoignable, relances sans réponse (environ 11 avis) : « Le gestionnaire est injoignable. » (syndic, 2026-10-02)
  2. Sinistres et dossiers qui traînent (dégât des eaux, dépôt de garantie, état des lieux) (environ 6 avis) : « inertie totale pendant 11 mois » (gestion locative, 2025-10-10)
  3. Comptes, frais et paiements contestés (environ 5 avis) : « Les comptes ne sont pas bons en fin d'exercice » (syndic, 2026-10-11)
- Angle d'amélioration : le syndic est obligatoire pour toute copropriété (loi de 1965) et le changement de syndic se vote en assemblée générale : la douleur est forte et le client peut partir. Une équipe sans carte professionnelle ne peut pas être syndic professionnel elle-même [HYPOTHÈSE : carte G loi Hoguet requise]. Angles possibles : (a) accompagner les petites copropriétés à passer en syndic bénévole ou coopératif, avec un service outillé (assistant AG, compta, suivi des sinistres) ; (b) un service de « mise en concurrence de syndic » pour conseils syndicaux mécontents ; (c) s'associer à un titulaire de carte G et vendre un syndic « réactivité garantie » (réponse sous 48 h écrite au contrat).

### F1-05 : Site internet « gratuit » pour TPE avec engagement long (Local.fr) : vente forcée et contrat de 5 ans
- Modèle / acteur : Local.fr, création de site internet et référencement pour artisans et commerçants, vendu en démarchage avec abonnement mensuel et engagement long
- Secteur : agence web / marketing digital pour TPE | Cible : B2B (artisans, commerçants, indépendants)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.local.fr?stars=1&stars=2 (date : avis de 2026-08 à 2026-10)
- Citation : « Je paie environ 170 à 180 € par mois avec un engagement de 60 mois » (florian, 2026-09-11)
- Chiffres : 6 855 avis Trustpilot (environ 2 048 sur les 12 derniers mois), note 4,5/5 ; 1 étoile 11 %, 2 étoiles < 1 % (environ 12 % de 1-2 étoiles). Prix : 170 à 180 €/mois sur 60 mois selon un client, soit environ 10 000 € au total (Jean AL REZEK, 2026-08-28, cite « ~10 000 € ») ; un autre client dit qu'on lui réclame « environ 11 000 € » après fermeture de son activité (Dani, 2026-09-23).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Discours commercial trompeur (site « gratuit », durée d'engagement découverte après) : « il n'a jamais été question de 24 ou 36 mois » (Daugas, 2026-09-23)
  2. Plus aucun suivi après la signature, résultats SEO faibles : « conseillé fantôme qui disparait dès la signature du contrat » (Mouloud Chemoun, 2026-10-03)
  3. Résiliation impossible, même en cas de cessation d'activité : « Refus de reconsidérer le contrat en cas de cessation d'activité » (Guil07, 2026-09-04)
- Angle d'amélioration : très adapté à une équipe marketing. Les TPE paient déjà 170-180 €/mois pour un site + visibilité locale. Offre concurrente : site vitrine + fiche Google Business Profile + gestion des avis, sans engagement (mensuel résiliable) ou à prix fixe, site propriété du client, compte rendu mensuel chiffré. Outils no-code (Webflow, Framer, WordPress) suffisent, pas besoin de développeur. Cible de départ : artisans du bâtiment et commerces de petite couronne. Message : « votre site vous appartient, résiliable en 1 clic ».

### F1-06 : Conciergerie Airbnb (HostnFly) : ménage non fait, injoignable, cautions retenues
- Modèle / acteur : HostnFly, conciergerie de location courte durée (annonce, voyageurs, ménage, linge, clés) payée à la commission
- Secteur : conciergerie location courte durée | Cible : B2C (propriétaires) + voyageurs
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/hostnfly.com?stars=1&stars=2 (date : avis de 2026-07 à 2026-10) ; https://www.hostnfly.com/ (date inconnue)
- Citation : « Le ménage n'a pas été terminé, le linge a simplement été déplacé chez moi. » (2026-09-14)
- Chiffres : 2 313 avis Trustpilot, note 4,1/5 ; 1 étoile 13 %, 2 étoiles < 1 % (environ 14 % de 1-2 étoiles). Prix : commission « à partir de 20% » des revenus locatifs (page d'accueil). Taille : « 5000 hôtes » / « plusieurs milliers d'hôtes », 18 villes dont Paris.
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Ménage bâclé, logement sale ou abîmé : « L'appartement a été dégradé. Des affaires volées » (2026-08-31)
  2. Réactivité nulle, pas de numéro d'urgence : « aucun numéro d'urgence n'était disponible pour obtenir une assistance immédiate » (2026-07-09)
  3. Remboursements et cautions contestés : « Cette societe nous retient une caution de 250 euros » (2026-10-01)
- Angle d'amélioration : conciergerie de quartier (un ou deux arrondissements, ou une ville de petite couronne proche de Paris) avec une équipe ménage salariée ou fidélisée, photos datées après chaque ménage envoyées au propriétaire, astreinte téléphonique humaine. La réglementation parisienne sur les meublés de tourisme [HYPOTHÈSE : plafond de nuitées pour les résidences principales abaissé par la loi Le Meur fin 2024, à vérifier] réduit le marché à Paris intra-muros ; la petite couronne et la location moyenne durée (bail mobilité) sont des alternatives. Entrée possible avec très peu de capital.

### F1-07 : Domiciliation d'entreprise (SeDomicilier) : prélèvements après résiliation, courrier perdu
- Modèle / acteur : SeDomicilier, domiciliation d'entreprise en ligne (adresse de siège + scan du courrier), avec création de société en option
- Secteur : services aux entreprises (domiciliation) | Cible : B2B (créateurs, TPE, indépendants)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.sedomicilier.fr?stars=1&stars=2 (date : avis de 2025-12 à 2026-10) ; https://www.sedomicilier.fr/tarifs (date : promo affichée jusqu'au 2026-10-31)
- Citation : « SeDomicilier a continué à me prélever malgré la fermeture de mon entreprise » (Erik VD, 2025-12-26)
- Chiffres : 1 229 avis Trustpilot, note 4,3/5 ; 1 étoile 14 %, 2 étoiles 2 % (16 % de 1-2 étoiles). Prix : de 11 à 16 €/mois HT selon la durée d'engagement (jusqu'à 3 ans) en micro-entreprise ; options courrier Business +10 €/mois et Premium +40 €/mois ; 14 adresses à Paris, 11 en Île-de-France.
- 3 reproches les plus fréquents (sur 21 avis 1 étoile récents) :
  1. Résiliation ignorée, prélèvements qui continuent, engagement de 3 ans regretté (environ 9 avis) : « J'ai malheureusement souscris à un contrat multi-années (3 ans) » (Léo L., 2026-09-30)
  2. Service client injoignable, traitements lents (environ 6 avis) : « Ils sont totalement injoignables, je multiplie les demandes de rappel » (Kilian Fossier, 2026-07-03)
  3. Courrier détruit ou perdu, documents refusés (environ 6 avis) : « ils vous les détruisent sans mail de rappel avant » (Ayoub Merzak, 2026-01-21)
- Angle d'amélioration : la domiciliation demande un agrément préfectoral [HYPOTHÈSE : agrément obligatoire, art. L123-11-3 du Code de commerce] et un local. Angle réaliste : centre de domiciliation de proximité (petite couronne, par exemple adossé à un coworking existant) ou partenariat avec un domiciliataire agréé, vendu avec un vrai humain, engagement mensuel, résiliation en un clic et alerte courrier par SMS. Différenciation surtout sur le service ; prix de marché bas (11-16 €/mois).

### F1-08 : Création de société en ligne (Legalstart) : abonnements cochés par défaut, formalistes injoignables
- Modèle / acteur : Legalstart, création d'entreprise et formalités juridiques en ligne, avec abonnements (juridique, compta « LS Compta »)
- Secteur : legaltech / formalités d'entreprise | Cible : B2B (créateurs, TPE)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.legalstart.fr?stars=1&stars=2 (date : avis de 2026-04 à 2026-10) ; https://www.legalstart.fr/tarifs/ (date inconnue)
- Citation : « une case est cochée qui vous fait souscrire à un abonnement à 35.88€ par mois » (2026-07-09)
- Chiffres : 7 608 avis Trustpilot, note 4,5/5 ; 1 étoile 12 %, 2 étoiles 1 % (13 % de 1-2 étoiles). Prix : création « à partir de 0€ » ; comptabilité « à partir de 29€ HT/mois » ; abonnements « à partir de 29,90€ HT » (soit 35,88 € TTC, montant cité dans les avis).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Abonnements non voulus ou renouvelés automatiquement, remboursements refusés (environ 9 avis) : « 4 abonnements que je n'ai jamais signé » (2026-10-12)
  2. Documents génériques ou conseils inadaptés (environ 6 avis) : « Le même texte pour toutes société avec des éléments qui ne sont reels. » (2026-09-25)
  3. Injoignable et délais, même avec option payante (environ 5 avis) : « formaliste injoignable malgré option premium payé » (2026-10-12)
- Angle d'amélioration : le prix d'appel à 0 € est financé par des abonnements subis. Une offre « création + premier an » à prix fixe tout compris, sans abonnement caché, avec un interlocuteur nommé, est simple à vendre. Le juridique nécessite un avocat ou un expert-comptable partenaire ; la valeur de l'équipe est l'acquisition, l'accompagnement et le suivi. Proche de F1-07 (même cible de créateurs) : un bouquet « je crée ma boîte à Paris » (statuts via partenaire, domiciliation, banque, compta) pourrait réunir les deux.

### F1-09 : Auto-école en ligne (Ornikar) : leçons annulées, pas de créneaux, heures non remboursées
- Modèle / acteur : Ornikar, auto-école en ligne (code + forfaits de conduite avec moniteurs indépendants), aussi assureur auto
- Secteur : auto-école / permis de conduire | Cible : B2C (jeunes, parents payeurs)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.ornikar.com?stars=1&stars=2 (date : avis de 2026-06 à 2026-10, 18 sur 20 en auto-école) ; https://www.ornikar.com/permis (date : prix 2026)
- Citation : « Les rendez-vous étaient systématiquement annulés la veille » (2026-07-17)
- Chiffres : 29 907 avis Trustpilot, note 4,3/5 ; 1 étoile 11 %, 2 étoiles 2 % (13 % de 1-2 étoiles). Prix : Pack Permis dès 459,99 € (12 h), conduite accompagnée dès 569,99 €, permis accéléré dès 1 709,99 € ; code dès 2,99 €/mois ; « + 1 800 moniteurs ».
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Annulations et manque de moniteurs / de créneaux : « Un seul moniteur pour tout une commune » (2026-10-09)
  2. Service client lent ou injoignable : « Plus de 25 minute avant d'avoir un conseiller.. » (2026-10-09)
  3. Heures non remboursées, coûts supplémentaires après échec : « après un échec, 8 h à repayer même quand l'élève sait conduire » (2026-10-10)
- Angle d'amélioration : le goulot est la disponibilité des moniteurs, pas le logiciel. Une auto-école locale ou un réseau de moniteurs indépendants coordonné sur une zone dense (93/94) qui garantit un nombre de créneaux par semaine ferait mieux [HYPOTHÈSE : agrément préfectoral et moniteurs diplômés requis]. Variante plus légère : service de « coaching permis » (planification, examens blancs, location de voiture double commande) pour candidats libres. Contrainte : plus capitalistique et réglementé que d'autres pistes.

### F1-10 : Salle de sport low-cost (Fitness Park) : prélèvements tous les 28 jours, résiliation difficile, machines en panne
- Modèle / acteur : Fitness Park, réseau de salles de sport low-cost en franchise
- Secteur : sport / fitness | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.fitnesspark.fr?stars=1&stars=2 (date : avis de 2025-09 à 2026-10)
- Citation : « Le piège de la facturation tous les 28 jours » (2026-09-29)
- Chiffres : 924 avis Trustpilot, note 2,0/5 ; 1 étoile 68 %, 2 étoiles 5 % (73 % de 1-2 étoiles). Prix : abonnement affiché « 30€/mois » selon un avis (2026-10-11) ; prix officiel non vérifié sur le site. Point de comparaison : Basic-Fit, 109 192 avis, note 4,2/5, 19 % de 1-2 étoiles (https://fr.trustpilot.com/review/www.basic-fit.com, page lue le 2026-10-13, seulement 3 avis négatifs visibles, tous du 2026-10-12, dont « L'application fait tout pour vous arnaquer »).
- 3 reproches les plus fréquents (sur 22 avis 1-2 étoiles récents) :
  1. Facturation et résiliation (cycle de 28 jours, prélèvements pendant une suspension, recommandé obligatoire) : « elle a été prélevée induement pendant 2 ans » (2026-10-05)
  2. Machines en panne non réparées : « Les machines tombent en panne les unes après les autres. » (2026-09-01)
  3. Accueil et service client : « Impossible de les joindre par téléphone » (2026-08-26)
- Angle d'amélioration : ouvrir une salle demande trop de capital pour l'équipe. Angles accessibles : petits groupes de coaching (extérieur ou salles louées à l'heure) avec abonnement mensuel sans engagement et résiliation en ligne ; ou sport en entreprise. Le signal montre surtout que « sans engagement, sans piège » est un argument marketing qui porte dans ce secteur.

### F1-11 : Plateforme de dépannage à domicile (MesDépanneurs) : prix opaques, artisans indisponibles
- Modèle / acteur : MesDépanneurs, plateforme qui envoie des artisans partenaires (plomberie, serrurerie, électricité, chauffage) en urgence, avec prix annoncés en fourchette
- Secteur : dépannage / artisans à domicile | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.mesdepanneurs.fr?stars=1&stars=2 (date : avis de 2025-11 à 2026-10) ; https://www.mesdepanneurs.fr/ (date inconnue)
- Citation : « facturé directement au tarif maximum (242€ TTC avec déplacement) » (2026-09-16)
- Chiffres : 7 095 avis Trustpilot, note 4,0/5 ; 1 étoile 16 %, 2 étoiles 4 % (20 % de 1-2 étoiles). Prix publics en fourchette : débouchage WC 100-200 €, ouverture de porte claquée 130-180 €, serrure 3 points 400-800 €, entretien chaudière 150-180 €. Revendique « +500 000 dépannages depuis 2013 », « 1300 pros », 48 villes.
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Prix jugés excessifs ou facturés au maximum de la fourchette (environ 9 avis) : « le prix demandè pour 25 minutes de travail est un VOL » (2026-08-20)
  2. Délai d'intervention non tenu, pas de rappel, pas d'artisan disponible (environ 7 avis) : « Demande d'intervention annulée car aucuns dépanneurs dispos!!! » (2026-09-18)
  3. Compétence ou honnêteté de l'artisan, garantie non appliquée (environ 6 avis) : « la garantie mise en avant n'a apporté aucune prise en charge » (2026-02-20)
- Angle d'amélioration : le dépannage d'urgence est un marché où la confiance manque (arnaques de serruriers connues). Un réseau local de 10 à 20 artisans vérifiés en petite couronne, prix fixes par intervention (pas de fourchette), photo et facture envoyées au client et à son assurance, et un humain qui suit le dossier. L'équipe fait le marketing (SEO local, Google Ads) et la relation client, les artisans font le travail : modèle de commission sans capital. Le reproche « pas de facture pour l'assurance » (9 mois d'attente, 2025-11-16) montre que la gestion administrative est elle-même une valeur.

### F1-12 : Centres auto (Speedy) : devis gonflés, ventes additionnelles, travail mal fait
- Modèle / acteur : Speedy, réseau de centres d'entretien rapide (pneus, freins, vidange, batterie) en propre et franchise
- Secteur : auto (entretien rapide, pneus) | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.speedy.fr?stars=1&stars=2 (date : avis de 2026-01 à 2026-10)
- Citation : « Des frais cachés pour un simple changement de pneu 280 euros » (Moithe legend, 2026-09-14)
- Chiffres : 798 avis Trustpilot (334 sur les 12 derniers mois), note 3,5/5 ; 1 étoile 59 %, 2 étoiles 5 % (64 % de 1-2 étoiles). Prix : pas de page tarifs lue ; montants cités dans les avis : 280 € pour un pneu, devis de 966 € et de plus de 1 800 €.
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Prix, frais cachés et ventes additionnelles (environ 9 avis) : « ils faut changer les disques en plus des plaquettes » (Mr L, 2026-10-05)
  2. Erreurs de montage et dégâts sur le véhicule (environ 5 avis) : « le filtre à huile a été mal vissé » (Alain M., 2026-07-10)
  3. Remboursements et factures qui tardent (environ 4 avis) : « je réclame la facture de deux pneus achetés et payés sur Speedy.fr » (Florence C., 2026-05-18)
- Angle d'amélioration : à rapprocher de F1-03 (Vroomly). Le client veut un prix connu d'avance et ne pas se faire vendre de pièces inutiles. Service « tiers de confiance » : diagnostic photo / vidéo, second avis sur devis de garage (« ce devis est-il justifié ? ») payant à petit prix, puis réservation chez un garage partenaire à prix garanti. Faisable par une équipe sans mécanicien en s'appuyant sur un mécanicien conseil rémunéré à l'acte [HYPOTHÈSE].

### F1-13 : Expert-comptable en ligne (Dougs) : erreurs fiscales, interlocuteurs qui changent
- Modèle / acteur : Dougs, cabinet d'expertise comptable en ligne pour indépendants et TPE, abonnement mensuel
- Secteur : expertise comptable | Cible : B2B (TPE, indépendants, SAS / EURL)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.dougs.fr?stars=1&stars=2 (date : avis de 2026-08 à 2026-10) ; https://www.dougs.fr/tarifs/ (date inconnue)
- Citation : « personne ne porte un dossier dans la durée » (Pierre Toussaint, 2026-09-09)
- Chiffres : 3 641 avis Trustpilot, note 4,7/5 ; 1 étoile 8 %, 2 étoiles 2 % (10 % de 1-2 étoiles, mais 19 avis négatifs en 2 mois). Prix : Pack Liberté dès 79 € HT/mois, Sérénité dès 99 €, Exclusivité dès 129 € ; formalités annuelles 300 € HT en Liberté ; « + 49 000 entrepreneurs ».
- 3 reproches les plus fréquents (sur 19 avis 1-2 étoiles récents) :
  1. Service lent, interlocuteurs multiples, pas de suivi (majorité des avis) : « multiplie les interlocuteurs sans cohésion entre eux » (Nicolas André, 2026-10-05)
  2. Erreurs comptables ou fiscales qui coûtent des pénalités : « Nous devons payer des pénalités pour un oubli de formalité » (Isabelle Tourtoulon, 2026-10-11)
  3. Prélèvements et remboursements : « Très déçu par la gestion d'un double prélèvement » (Aurélien Lavayssière, 2026-08-01)
- Angle d'amélioration : l'équipe ne peut pas tenir la comptabilité elle-même (profession réglementée [HYPOTHÈSE : inscription à l'Ordre requise pour la tenue et la révision]). Angle accessible : apporteur d'affaires ou marque commerciale spécialisée pour un cabinet partenaire, sur une niche (restaurateurs, artisans du bâtiment, professions de santé, créateurs de contenu) avec un comptable dédié nommé. La plainte n° 1 n'est pas le prix, c'est l'absence d'un interlocuteur stable.

### F1-14 : Réparation de smartphones en boutique (Save) : réparations ratées, boutiques fermées
- Modèle / acteur : Save, réseau de boutiques de réparation de smartphones et de vente de reconditionnés (franchise)
- Secteur : réparation smartphone | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/save.co?stars=1&stars=2 (date : avis de 2025-10 à 2026-09)
- Citation : « Boutique fermée aux horaires d'ouverture » (Eleonore Petitgas, 2026-08-25)
- Chiffres : 204 avis Trustpilot, note 2,2/5 ; 1 étoile 67 %, 2 étoiles 5 % (72 % de 1-2 étoiles). Prix : non relevés (pas de page tarifs lue) ; un avis cite un devis de réparation jugé excessif sur un Samsung Z Fold 5 (2026-09-23).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Réparation ratée, nouvelle panne, pièces de mauvaise qualité (environ 8 avis) : « Travail bâclé et téléphone gardé une semaine » (2026-07-09)
  2. Boutiques fermées sans prévenir, injoignables (environ 7 avis) : « Magasin souvent fermé sans mentionner l'heure de réouverture. » (2026-08-28)
  3. Devis, remises ou remboursements non honorés (environ 5 avis) : « Refus d'honorer le devis officiel » (Fernanda P, 2026-05-07)
- Angle d'amélioration : le volume d'avis est faible (204), le signal porte donc sur la qualité d'un réseau plus que sur la taille du marché. Une offre de réparation à domicile ou au bureau (technicien qui vient, réparation en 30 min devant le client) avec prix fixe affiché et garantie, en B2B pour les flottes de téléphones de PME, serait un angle différenciant. Le bonus réparation de l'État (fonds réparation) aide à vendre [HYPOTHÈSE : montant et éligibilité à vérifier].

### F1-15 : Garde d'animaux entre particuliers (Rover) : support injoignable, frais des deux côtés
- Modèle / acteur : Rover, place de marché de pet-sitting (garde à domicile, promenade, hébergement), commission côté propriétaire et côté gardien
- Secteur : garde d'animaux | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.rover.com?stars=1&stars=2 (date : avis de 2026-07 à 2026-10, 19 sur 20 venant de France)
- Citation : « Au prix affiché Rover ajoute 15% pour celui qui réserve » (2026-09-14)
- Chiffres : 35 876 avis Trustpilot (environ 6 457 sur 12 mois, toutes langues), note 4,5/5 ; 1 étoile 7 %, 2 étoiles 2 % (9 % de 1-2 étoiles). Prix : frais de 15 % ajoutés côté réservant selon l'avis cité ; frais d'inscription côté gardien cités (2026-09-09).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Support client injoignable, chat en anglais, réponses automatiques (environ 9 avis) : « aucun numéro de téléphone à appeler ni adresse postale » (2026-09-21)
  2. Frais jugés élevés des deux côtés : « Frais très importants déductibles de vos gains. » (2026-08-06)
  3. Incidents de garde mal gérés, aucun contrôle des gardiens : « Aucun contrôle. » (2026-09-10)
- Angle d'amélioration : part de 1-2 étoiles modérée, mais les avis négatifs récents sont presque tous français, signe d'un service mal adapté au marché français. Une agence locale de pet-sitting (Paris / petite couronne) avec gardiens rencontrés en vrai, numéro de téléphone français, assurance claire et rapport photo après chaque visite. Peu de capital, forte récurrence (promenades quotidiennes, vacances). Statut à vérifier : la garde d'animaux à domicile peut relever des services à la personne [HYPOTHÈSE : éligibilité au crédit d'impôt à vérifier, probablement non].

### F1-16 : Syndic de copropriété en ligne / coopératif (Matera) : abandon des copropriétés, comptes en retard
- Modèle / acteur : Matera, syndic en ligne (offre coopérative où le conseil syndical gère avec la plateforme, et offre « syndic local » déléguée)
- Secteur : immobilier (syndic de copropriété) | Cible : B2C (copropriétés, conseils syndicaux)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/matera.eu?stars=1&stars=2 (date : avis de 2026-09 à 2026-10, 20 avis en 4 semaines) ; https://www.matera.eu/fr/tarifs (date inconnue)
- Citation : « Nous payons 690€ par an pour que Matera mette en paiement 4 factures ! » (braceschi, 2026-10-08)
- Chiffres : 1 592 avis Trustpilot, note 3,7/5 ; 1 étoile 23 %, 2 étoiles 2 % (25 % de 1-2 étoiles). Prix : pas de grille publique (« Devis sur-mesure et gratuit ») ; 690 €/an cité par un client. Taille revendiquée : « +10 000 copropriétés clientes », environ 150 000 copropriétaires ; 4,4/5 sur plus de 1 000 avis Google (chiffre de la page Matera, non vérifié).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Injoignable, pas de téléphone, mails sans réponse : « ne pas pouvoir appeler le support client au téléphone est un inconvénient MAJEUR » (Jean-Etienne Joullié, 2026-09-30)
  2. Erreurs financières (factures fournisseurs impayées, appels de fonds faux) : « plus d'une cinquantaine de factures emises par le même fournisseur » (Francois Wartelle, 2026-09-30)
  3. AG non tenues, comptes non présentés, passation au syndic suivant bloquée : « Matera n'a toujours pas fait la passation » (Mosbacher, 2026-09-21)
- Angle d'amélioration : avec F1-04 (Foncia), cela montre que ni le syndic traditionnel ni le syndic en ligne ne satisfont. La vague d'avis négatifs groupés (20 en 4 semaines, plusieurs copropriétés qui partent) suggère une crise de service en cours chez Matera : des centaines de conseils syndicaux cherchent un nouveau syndic maintenant. Angles pour l'équipe : (a) service d'accompagnement au changement de syndic (comparatif, cahier des charges, vote en AG, suivi de la passation) facturé au conseil syndical ; (b) assistance « syndic bénévole » outillée pour petites copropriétés (moins de 10 lots), sans carte professionnelle [HYPOTHÈSE : un syndic bénévole copropriétaire n'a pas besoin de carte G ; un prestataire d'assistance non plus tant qu'il n'est pas mandataire].

### F1-17 : Services à la personne en réseau (O2) : 4 mois sans ménage, pas de remplaçant
- Modèle / acteur : O2, réseau national de services à domicile (ménage, repassage, garde d'enfants, aide aux seniors, jardinage), éligible au crédit d'impôt de 50 %
- Secteur : ménage / services à domicile | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.o2.fr?stars=1&stars=2 (date : avis de 2026-04 à 2026-10)
- Citation : « 4 MOIS SANS AUCUNE PRESTATION DE MÉNAGE » (2026-09-02)
- Chiffres : 3 469 avis Trustpilot (858 sur 12 mois), note 4,2/5 ; 1 étoile 13 %, 2 étoiles 4 % (17 % de 1-2 étoiles). Prix : non relevé sur le site [HYPOTHÈSE : tarif horaire de ménage de l'ordre de 25-30 € avant crédit d'impôt, à vérifier] ; montants contestés cités : « surfacturation de 1200 euros » (garde d'enfants, 2026-08-11), « 1000 euros » réclamés (seniors, 2026-07-28).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Pénurie d'intervenants, interruptions longues, pas de remplaçant (environ 10 avis) : « Aucune prestation de service depuis 4 mois et demi » (2026-09-21)
  2. Facturation et gestion administrative (environ 7 avis) : « le montant prélevé ne correspond pas à ce qui m'avait été expliqué » (2026-08-25)
  3. Qualité du travail (environ 6 avis) : « elle ne nettoyait pas correctement elle passe autour des objets » (2026-08-07)
- Angle d'amélioration : le problème n° 1 est le recrutement et la fidélisation des intervenantes, pas la demande. Une petite structure de ménage locale (une ou deux villes de petite couronne) qui paie mieux ses intervenantes et garantit un remplacement, en mandataire ou prestataire [HYPOTHÈSE : déclaration SAP simple pour le ménage, agrément seulement pour publics fragiles]. Le crédit d'impôt de 50 % et l'avance immédiate URSSAF rendent l'offre facile à vendre. Contre-signal : voir F1-19, Wecasa obtient 4,7/5 sur plus de 19 000 avis avec un modèle de plateforme, la concurrence « bien notée » existe.

### F1-18 : Logiciel de réservation pour salons de beauté (Planity) : abonnement difficile à résilier, données clients bloquées
- Modèle / acteur : Planity, logiciel de prise de rendez-vous et de caisse pour coiffeurs, instituts, barbiers, avec place de marché côté clients
- Secteur : logiciel pour TPE (prise de rendez-vous) | Cible : B2B (salons) + B2C (clients des salons)
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.planity.com?stars=1&stars=2 (date : avis de 2026-07 à 2026-10)
- Citation : « je n'ai pas pu résilier ce contrat qui me prélève 88,80 euros par mois » (thérapeute, 2026-09-01)
- Chiffres : 3 599 avis Trustpilot (612 sur 12 mois), note 4,5/5 ; 1 étoile 8 %, 2 étoiles < 1 % (environ 9 % de 1-2 étoiles). Prix : 88,80 €/mois cité par un professionnel ; page tarifs pro non trouvée (https://www.planity.com/pro renvoie 404).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents, mélange clients et pros) :
  1. Remboursements, facturation et résiliation : « faites opposition sur les prélèvements quand vous résiliez » (2026-09-09)
  2. Réservations dans des salons fermés ou défaillants : « Un site de voleur qui laisse réserver dans des salons qui sont fermés » (2026-07-23)
  3. Côté pros, support et données verrouillées : « je souhaitais simplement extraire la liste de mes clientes » (salon, 2026-07-28)
- Angle d'amélioration : signal modéré (9 %). Pour une équipe sans développeur, refaire un logiciel n'est pas réaliste. Angle plus réaliste : service de migration et de paramétrage pour salons qui veulent quitter (récupération du fichier client, mise en place d'un outil moins cher, fiche Google, campagne SMS de relance) ; ou agence marketing spécialisée salons de beauté. À rapprocher de F1-05 : les TPE paient 80-180 €/mois pour des outils de visibilité dont elles ne sont pas satisfaites.

### F1-19 : Ménage à domicile en plateforme (Helpling vs Wecasa) : contre-signal, le leader est bien noté
- Modèle / acteur : Helpling (plateforme de ménage à domicile) comparé à Wecasa (plateforme de ménage, beauté, massage à domicile)
- Secteur : ménage / services à domicile | Cible : B2C
- Type de signal : plainte (Helpling) ; contre-signal (Wecasa)
- Source : https://fr.trustpilot.com/review/www.helpling.fr?stars=1&stars=2 (date : avis de 2021-11 à 2026-05) ; https://fr.trustpilot.com/review/www.wecasa.fr (date : avis du 2026-10-09 et 2026-10-12)
- Citation : « Si aucune aide-ménagère ne se présente, vous êtes tout de même prélevé. » (Helpling, URBILLAC, 2024-02-16)
- Chiffres : Helpling 930 avis, note 4,5/5, 10 % de 1-2 étoiles, la plupart des avis négatifs ont plus de 24 mois (Trustpilot signale qu'Helpling ne sollicite plus d'avis ni ne répond). Wecasa : 19 164 avis, note 4,7/5, 1 étoile 6 %, 2 étoiles < 1 %, aucun avis 1-2 étoiles sur la première page. Prix : non relevés.
- 3 reproches les plus fréquents chez Helpling (20 avis 1-2 étoiles) :
  1. Absences sans prévenir, intervenantes qui changent : « Vous n'êtes pas avertis de l'absence de l'intervenant » (2024-10-31)
  2. Double facturation, prélèvement pour une prestation non faite : « préstations prélevées deux fois sous pretexte de bug informatique » (2025-09-09)
  3. Qualité et casse : « Zéro suivi, aucun geste en cas de casse (reconnue par l'intervenante) » (2025-06-16)
- Angle d'amélioration : ce signal CONTREDIT en partie F1-17 : sur le ménage, le leader plateforme (Wecasa) satisfait très largement ses clients. Un nouvel entrant ne gagnera pas sur « l'expérience de réservation ». Il ne reste de place que sur la régularité (même intervenante chaque semaine, remplacement garanti) face aux réseaux type O2, ou sur des cibles négligées (seniors, bureaux de TPE, fin de bail / état des lieux).

### F1-20 : Encaissement par carte pour TPE (SumUp) : fonds bloqués, aucun humain au téléphone
- Modèle / acteur : SumUp, terminaux de paiement et caisse pour petits commerçants et indépendants (commission par transaction + abonnements)
- Secteur : logiciel / fintech pour TPE (encaissement, caisse) | Cible : B2B
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.sumup.fr?stars=1&stars=2 (date : avis de 2026-09 à 2026-10)
- Citation : « Pas d humains au téléphone. » (2026-09-30)
- Chiffres : 59 340 avis Trustpilot (25 591 sur 12 mois), note 4,2/5 ; 1 étoile 17 %, 2 étoiles 3 % (20 % de 1-2 étoiles, soit environ 11 800 avis négatifs). Prix : non relevés (pas de page tarifs lue).
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Support inaccessible (chatbot, répondeur) (environ 9 avis) : « Assistance inexistante » (2026-09-27)
  2. Comptes bloqués, virements non reçus (environ 9 avis) : « Ils m'ont bloqué mon compte et mes ponts, aucune raison » (2026-09-26)
  3. Frais trop élevés, abonnement plus cher que promis (environ 5 avis) : « on m'a tout simplement menti pour me faire payer un abonnement plus cher » (2026-09-30)
- Angle d'amélioration : l'équipe ne peut pas devenir établissement de paiement. Angle indirect : courtage / conseil en solutions d'encaissement pour commerçants (comparer SumUp, Zettle, Stripe, banques, négocier les taux), payé à la commission par les fournisseurs ou au forfait. Signal surtout utile comme preuve que les TPE souffrent d'un support absent chez leurs fournisseurs numériques (même constat en F1-05, F1-08, F1-13, F1-18).

### F1-21 : Dépannage à domicile, preuve réglementaire : 60 % des professionnels contrôlés en infraction
- Modèle / acteur : secteur du dépannage à domicile (plomberie, serrurerie, électricité, chauffage), contrôles DGCCRF
- Secteur : dépannage / artisans à domicile | Cible : B2C
- Type de signal : obligation réglementaire + plainte
- Source : https://www.consoglobe.com/depannage-a-domicile-arnaques-infractions-cg (date : 2025-07-10), qui reprend la publication DGCCRF du 2025-07-08 (https://www.economie.gouv.fr/dgccrf/depannage-domicile-gare-aux-arnaques, page non lisible : erreur 403, extrait vu via le moteur de recherche seulement)
- Citation : « 60 % d'entre eux se sont révélés en infraction. » (Consoglobe, 2025-07-10)
- Chiffres : plus de 600 professionnels contrôlés selon l'article (548 selon le message DGCCRF cité dans le même article ; chiffres non réconciliés), contrôles 2024 ; près de 2 600 signalements sur SignalConso en 2024. Infractions : pas de devis ni de facture écrits, prix abusifs profitant de l'urgence, pratiques déloyales surtout en zone urbaine. Selon l'extrait du moteur de recherche (non lu en entier) : 189 avertissements, 195 injonctions, 67 amendes administratives, 64 procès-verbaux pénaux en 2024.
- Angle d'amélioration : confirme F1-11. Dans un marché où le client a peur de se faire arnaquer, la marque de confiance (prix fixe écrit avant intervention, facture systématique, artisans vérifiés) est l'argument principal, et c'est un travail de marketing et d'organisation, pas de technique. Paris est explicitement une zone à problèmes (« zones urbaines »).

### F1-22 : Box repas (HelloFresh) : livraisons ratées, prélèvements non voulus
- Modèle / acteur : HelloFresh, box de recettes avec ingrédients livrées à domicile, sur abonnement
- Secteur : box et abonnements alimentaires | Cible : B2C
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.hellofresh.fr?stars=1&stars=2 (date : avis de 2026-06 à 2026-10)
- Citation : « continue de me prélever l'argent et de m'envoyer des colis » (Armelle, 2026-10-05)
- Chiffres : 41 013 avis Trustpilot, note 4,1/5 ; 1 étoile 12 %, 2 étoiles 6 % (18 % de 1-2 étoiles, soit environ 7 400 avis négatifs). Prix : 45,96 € pour une box selon un avis (Patrick Bouaillon, 2026-09-04) ; grille officielle non lue.
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Livraison (retard, mauvaise adresse, colis resté au dépôt) (environ 10 avis) : « à chaque fois même problème de livraison à mauvaise adresse » (Sakura, 2026-09-10)
  2. Service client injoignable ou inutile (environ 6 avis) : « Le service client est injoignable à l'écrit. » (Gilles, 2026-06-09)
  3. Abonnement subi, prélèvements après résiliation, livraisons non voulues (environ 6 avis) : « Ça enchaîne des livraisons non désirées dans un rythme très court » (2026-09-14)
- Angle d'amélioration : une box repas nationale est hors budget. Angle local : box ou plats préparés livrés par un acteur de quartier (traiteur, producteur IDF, circuit court) avec livraison maîtrisée sur une petite zone et commande à l'unité sans abonnement forcé. Lien possible avec l'intérêt agroalimentaire du fondateur. Signal modéré (la note globale reste 4,1).

### F1-23 : Formation en ligne financée (Studi) : aucun suivi, contenus obsolètes, garantie « diplômé ou remboursé » contestée
- Modèle / acteur : Studi, école en ligne (diplômes, titres RNCP, formations financées par CPF, France Travail ou alternance)
- Secteur : formation en ligne | Cible : B2C (adultes en reconversion) + financeurs publics
- Type de signal : argent dépensé + plainte
- Source : https://fr.trustpilot.com/review/www.studi.com?stars=1&stars=2 (date : avis de 2026-01 à 2026-10)
- Citation : « Aucun suivi pédagogique, aucune réponse du support » (Redouane Bensedira, 2026-10-06)
- Chiffres : 9 538 avis Trustpilot (« 10 k »), note 4,5/5 ; 1 étoile 8 %, 2 étoiles 1 % (9 % de 1-2 étoiles). Prix : non relevés.
- 3 reproches les plus fréquents (sur 20 avis 1-2 étoiles récents) :
  1. Pas de suivi, support qui ne répond pas (environ 14 avis) : « personne ne te répond ni par mail ni au téléphone » (Ambre Billaud, 2026-09-11)
  2. Contenus obsolètes ou mal expliqués (environ 7 avis) : « les cours ne sont pas à jour » (Maï Le Borgne, 2026-09-21)
  3. Erreurs administratives et pression commerciale (environ 8 avis) : « leur politique de réussi ou remboursé est un pure MENSONGE. » (Lory Bellardant, 2026-09-02)
- Angle d'amélioration : créer un organisme de formation certifié Qualiopi est long [HYPOTHÈSE : certification Qualiopi nécessaire pour être financé par le CPF]. Angle plus rapide : tutorat / coaching humain d'apprenants en formation à distance (suivi hebdomadaire, préparation aux examens) vendu aux apprenants ou aux organismes qui sous-traitent le suivi. Signal modéré en pourcentage, mais la plainte (« personne ne suit ») est très homogène.

### F1-24 : Contrôle technique (Autosur) : contre-visites contestées, accueil désagréable
- Modèle / acteur : Autosur, réseau de centres de contrôle technique automobile (franchise)
- Secteur : auto (contrôle technique) | Cible : B2C
- Type de signal : obligation réglementaire (contrôle obligatoire) + plainte
- Source : https://fr.trustpilot.com/review/www.autosur.fr?stars=1&stars=2 (date : avis de 2025-10 à 2026-09)
- Citation : « allégations non vérifiables conduisant à une contre-visite » (Patrick, 2026-07-17)
- Chiffres : 133 avis Trustpilot, note 1,9/5 ; 1 étoile 71 %, 2 étoiles 3 % (74 % de 1-2 étoiles). Prix : « 72€ » débités selon un avis (2025-12-29) ; grille officielle non lue. Faible volume d'avis : signal de mécontentement net mais base étroite (les avis des centres sont surtout sur Google).
- 3 reproches les plus fréquents (sur 21 avis 1-2 étoiles récents) :
  1. Défauts contestés, contre-visites payantes jugées abusives : « pour des tolérances acceptées par les autres enseignes » (Mehdi Ben-khalifa, 2025-12-02)
  2. Personnel désagréable, pas d'explication : « aucune explications d'aucunes sortes sur les raisons » (2026-06-01)
  3. Réservation et prix (RDV disparu, facture supérieure au prix en ligne) : « une facture bien plus élevée que le prix » (2026-02-14)
- Angle d'amélioration : le contrôle technique est obligatoire et réglementé (agrément de centre et de contrôleur [HYPOTHÈSE]). L'équipe ne peut pas ouvrir de centre facilement. Angle : service de « pré-contrôle + convoyage » pour actifs parisiens (on prend la voiture, on la passe au CT, on gère la contre-visite chez un garage partenaire, on la ramène), à combiner avec F1-03 et F1-12 dans une offre « conciergerie auto ».

### F1-25 : Syndics, preuve d'insatisfaction à l'échelle du secteur
- Modèle / acteur : ensemble des syndics professionnels (FNAIM, grands réseaux), copropriétaires
- Secteur : immobilier (syndic de copropriété) | Cible : B2C (copropriétaires)
- Type de signal : tendance + plainte
- Source : https://www.fnaim.fr/communiquepresse/1951/10-syndics-de-copropriete-stop-au-syndic-bashing.htm (date : 2026-01-09)
- Citation : « 62 % des résidents se déclarent satisfaits de la gestion de leur copropriété » (FNAIM, 2026-01-09, citant Ipsos 2025)
- Chiffres : selon Ipsos 2025 cité par la FNAIM, 62 % des résidents satisfaits dont 10 % très satisfaits (donc environ 38 % non satisfaits), 66 % des propriétaires satisfaits. Contexte : reportage France 2 « Envoyé spécial » du 2026-01-08 « Syndics de copropriété : gare aux abus », auquel la FNAIM répond.
- Angle d'amélioration : c'est le syndicat professionnel lui-même qui affiche qu'un tiers des copropriétaires ne sont pas satisfaits, alors que le service est obligatoire et payé chaque année. Avec F1-04 (Foncia, 27 % de 1-2 étoiles) et F1-16 (Matera, 25 %), le syndic est le marché le plus constamment mal noté de cette recherche. Le reportage TV de janvier 2026 crée un moment médiatique favorable à une offre « syndic transparent » ou « accompagnement au changement de syndic ». Taille du vivier : 8 285 établissements actifs en NAF 68.32A (administration d'immeubles, inclut syndics et gestion locative) à Paris, 1 805 dans le 92, 692 dans le 93, 1 112 dans le 94 (API Recherche d'entreprises, interrogée le 2026-10-13, `activite_principale=68.32A&etat_administratif=A`).

### F1-26 : Déménageurs indépendants : litiges de casse sans réponse (forum Que Choisir)
- Modèle / acteur : petits et moyens déménageurs (Servidem, Demefrance, L'Officiel du déménagement, Biard...) cités sur le forum Que Choisir
- Secteur : déménagement | Cible : B2C
- Type de signal : plainte
- Source : https://forum.quechoisir.org/post1278864.html (date : 2025-01-23) ; autres fils vus seulement en extrait de recherche (Demefrance, fil mis à jour en 2024-11 ; L'Officiel du déménagement, 2022-2024)
- Citation : « Cette entreprise n'assume pas ses incompétences et laisse le client sans réponse ni indemnisation » (Karen D, fil « Déménageurs SERVIDEM à fuir », 2025-01-23)
- Chiffres : 2 messages dans ce fil. Nombre de déménageurs actifs (NAF 49.42Z, API Recherche d'entreprises, 2026-10-13) : 411 à Paris, 168 dans le 92, 300 dans le 93, 172 dans le 94, soit 1 051 en petite couronne.
- Reproche principal : le même que chez Demeco (F1-01), la réclamation de casse est rejetée faute de réserves détaillées sur la lettre de voiture ou laissée sans réponse jusqu'à la prescription (extrait de recherche du fil Demefrance, non lu en entier).
- Angle d'amélioration : confirme que le problème n'est pas propre à Demeco : c'est un problème de secteur (lettre de voiture, franchise d'assurance, délai de 10 jours). Un tiers de confiance qui accompagne le client le jour J (check-list, photos horodatées, réserves bien écrites) et choisit le déménageur parmi des partenaires notés aurait un argument clair. Base de 1 051 déménageurs en petite couronne pour recruter des partenaires.

### F1-27 : Soutien scolaire (Acadomia) : contre-signal, leader bien noté
- Modèle / acteur : Acadomia, cours particuliers à domicile et stages (services à la personne, crédit d'impôt 50 %)
- Secteur : soutien scolaire | Cible : B2C (parents)
- Type de signal : plainte (faible) ; contre-signal
- Source : https://fr.trustpilot.com/review/www.acadomia.fr?stars=1&stars=2 (date : avis de 2026-02 à 2026-07)
- Citation : « Elle a eu 3 professeurs différents et je n'ai reçu aucune évaluation. » (Fontaine, 2026-03-31)
- Chiffres : 8 063 avis Trustpilot, note 4,4/5 ; 1 étoile 4 %, 2 étoiles 2 % (6 % de 1-2 étoiles seulement). Prix : non relevés.
- 3 reproches (19 avis 1-2 étoiles, faible fréquence : environ 19 en 8 mois) :
  1. Stages multi-niveaux et qualité inégale : « au bout de 4 jours j'apprends que c'est un stage multiniveaux » (Malau, 2026-04-23)
  2. Service administratif : « Très déçue par le service administratif. » (Florence, 2026-04-22)
  3. Facturation : « Double Facturation d'heure et délais inacceptables pour corriger l'erreur » (Dolcenea, 2026-07-20)
- Angle d'amélioration : ce signal CONTREDIT l'idée d'un marché mal servi : le leader du soutien scolaire satisfait la grande majorité. Un nouvel entrant devrait viser une niche (élèves « dys », préparation de concours spécifiques, lycées d'un quartier) plutôt qu'un meilleur service généraliste. À ne pas prioriser.

### F1-28 : Garde-meubles / self-stockage (Homebox) : contre-signal, prix cachés mais clients satisfaits
- Modèle / acteur : Homebox, réseau de centres de self-stockage (box à louer au mois) et location de camions
- Secteur : garde-meubles / stockage | Cible : B2C + B2B (TPE, e-commerçants)
- Type de signal : plainte (faible) ; contre-signal
- Source : https://fr.trustpilot.com/review/www.homebox.fr?stars=1&stars=2 (date : avis de 2023-12 à 2026-09)
- Citation : « Impossible de voir les tarifs simplement, sans être contacté » (V D, 2026-06-26)
- Chiffres : 298 avis Trustpilot (289 sur 12 mois), note 4,7/5 ; 1 étoile 4 %, 2 étoiles 2 % (6 % de 1-2 étoiles). Prix : non publiés sans laisser ses coordonnées (reproche récurrent).
- 3 reproches (17 avis 1-2 étoiles, faible fréquence) :
  1. Prix cachés et hausses sans préavis : « Prix augmentant sans préavis ou explication. » (Quentin Desvalois, 2026-07-02)
  2. Accès au box (code inactif, étage sans ascenseur) : « Impossible d'accéder au box loué car le code donné n'a jamais pu être activé. » (2026-07-21)
  3. Remboursements et dépôts lents : « rembourser l'acompte ou un virement effectué par erreur, cela peut prendre des jours » (2026-09-10)
- Angle d'amélioration : marché capitalistique (bâtiments) et clients globalement satisfaits : à écarter pour cette équipe. Seule leçon utile : l'affichage des prix sans formulaire est un argument différenciant dans plusieurs secteurs (déménagement, stockage, syndic).

---

## Synthèse

Constat transversal : dans presque tous les secteurs, les 3 mêmes reproches reviennent : (1) personne à joindre, (2) abonnement ou engagement subi et résiliation difficile, (3) prix final différent du prix annoncé. Ce sont des défauts d'organisation et de relation client, pas de technologie : exactement ce qu'une équipe marketing peut corriger. Les secteurs où le leader est bien noté (ménage en plateforme avec Wecasa, soutien scolaire avec Acadomia, garde-meubles avec Homebox, réparation d'électroménager avec Murfy) sont à écarter.

1. **Accompagnement des copropriétés mécontentes de leur syndic** (F1-04, F1-16, F1-25). Qui paie : les copropriétés (conseil syndical), plusieurs centaines à quelques milliers d'euros par an d'honoraires de syndic (690 €/an cité pour une petite copropriété chez Matera). Ce qui ne va pas : gestionnaire injoignable, comptes faux, AG non tenues, passation bloquée. Foncia 27 % et Matera 25 % de 1-2 étoiles, 38 % des résidents non satisfaits selon Ipsos 2025 cité par la FNAIM. Offre possible sans carte G : service payant de changement de syndic (appel d'offres, vote, suivi de passation) et assistance outillée aux syndics bénévoles de petites copropriétés. Le plus fort de la famille.

2. **Site + visibilité locale pour TPE, sans engagement** (F1-05, F1-18, F1-20). Qui paie : artisans et commerçants, 80 à 180 €/mois (Local.fr 170-180 €/mois sur 60 mois, Planity 88,80 €/mois). Ce qui ne va pas : vente trompeuse (« site gratuit »), engagement de 5 ans, conseiller qui disparaît, résiliation impossible. Offre : site no-code + fiche Google + gestion des avis, mensuel résiliable, site propriété du client. Colle parfaitement à des profils marketing sans développeur.

3. **Dépannage à domicile de confiance à prix fixe** (F1-11, F1-21). Qui paie : particuliers en urgence, 100 à 800 € par intervention (grille MesDépanneurs). Ce qui ne va pas : prix au maximum de la fourchette, artisans indisponibles, garanties non tenues ; 60 % des dépanneurs contrôlés en infraction (DGCCRF 2024, via Consoglobe). Offre : réseau local d'artisans vérifiés, prix fixe écrit avant intervention, facture envoyée à l'assurance ; l'équipe fait le marketing local et la relation client, modèle à la commission.

4. **Déménagement transparent / tiers de confiance le jour J** (F1-01, F1-26). Qui paie : particuliers, 500 à 900 € pour 15 m³ (fourchette Demeco). Ce qui ne va pas : casse puis indemnisation refusée grâce à la lettre de voiture, franchisés qui se renvoient la responsabilité, annulations la veille. Demeco 28 % de 1-2 étoiles ; 1 051 déménageurs actifs en petite couronne pour recruter des partenaires. Offre : courtier avec prix ferme affiché, inventaire vidéo, constat photo et réclamation gérée par nous.

5. **Conciergerie auto pour citadins (devis vérifié, contrôle technique, convoyage)** (F1-03, F1-12, F1-24). Qui paie : automobilistes, de 72 € (CT) à plus de 1 000 € (réparations). Ce qui ne va pas : prix affichés non tenus, rendez-vous fantômes, ventes additionnelles, contre-visites contestées. Vroomly 34 %, Speedy 64 %, Autosur 74 % de 1-2 étoiles. Offre : un humain qui gère la voiture de A à Z avec garages partenaires à prix garanti.

6. **Garde d'enfants / ménage local avec remplaçant garanti** (F1-02, F1-17 ; contre-signal F1-19). Qui paie : familles, 35 €/mois d'abonnement Yoopies ou prestations O2 avec crédit d'impôt de 50 %. Ce qui ne va pas : profils non fiables, abonnement pour simplement contacter, intervenante absente 4 mois sans remplaçant. Yoopies 15 %, O2 17 % de 1-2 étoiles. Attention : Wecasa (4,7/5 sur 19 164 avis) montre qu'un acteur bien organisé satisfait ce marché ; il faut se battre sur la régularité et le remplacement, pas sur la réservation.

7. **Kit « je crée ma boîte » humain et sans abonnement caché** (F1-07, F1-08, F1-13). Qui paie : créateurs et TPE, 11-16 €/mois de domiciliation, 29,90 € HT/mois d'abonnements Legalstart, 79-129 € HT/mois de compta Dougs. Ce qui ne va pas : cases précochées, prélèvements après résiliation, interlocuteurs qui changent, erreurs fiscales. Offre : prix fixe tout compris avec avocat ou expert-comptable partenaire et un interlocuteur nommé ; l'équipe porte l'acquisition et le suivi. Contraintes réglementaires (agrément domiciliation, Ordre des experts-comptables) à traiter par partenariat.

8. **Conciergerie de quartier (location courte ou moyenne durée) et pet-sitting local** (F1-06, F1-15). Qui paie : propriétaires (commission dès 20 % chez HostnFly), propriétaires d'animaux (15 % de frais Rover côté réservant). Ce qui ne va pas : ménage bâclé, aucun numéro d'urgence, support en anglais ou automatique. Entrée sans capital mais risque réglementaire sur la location courte durée à Paris.

## Sources non lues ou inexploitables

- https://www.economie.gouv.fr/dgccrf/depannage-domicile-gare-aux-arnaques et https://www.economie.gouv.fr/dgccrf/secteur-du-depannage-domicile-64-des-entreprises-controlees-par-les-services-de-la-dgccrf : erreur 403 (seul l'extrait du moteur de recherche a été vu).
- https://www.yoopies.fr/tarifs : 404. https://www.ornikar.com/permis/tarifs : 404 (prix pris sur /permis). https://www.planity.com/pro : 404.
- https://fr.trustpilot.com/review/www.peopleandbaby.com : 404 (crèches non couvertes).
- https://fr.trustpilot.com/review/www.complete-formation.fr : 404.
- Pages Trustpilot sans avis (secteur non mesurable sur Trustpilot) : popchef.com (repas d'entreprise), www.onet.fr (nettoyage de bureaux), www.babilou.fr (crèches). Foodles (www.foodles.co) n'a que 9 avis : trop peu pour un signal, non retenu (7 avis négatifs dont hygiène et contamination signalées en 2026-04).
- https://fr.custplace.com/nexity : lu, 1 012 avis, note 4,0/5, un seul avis négatif visible (2026-08-12) : inexploitable, non retenu.
- Fils du forum Que Choisir sur Demefrance, Daba'Dem, Biard, L'Officiel du déménagement : vus en extrait de recherche seulement.
- Non couverts faute de temps : avis Google Maps et App Store / Play Store (non lisibles par WebFetch), traiteurs d'entreprise, nettoyage de bureaux, toilettage, crèches privées.

