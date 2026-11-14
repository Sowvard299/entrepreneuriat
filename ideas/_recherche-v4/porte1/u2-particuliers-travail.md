# U2 particuliers : travail (porte 1)
Mission : services/abonnements aux particuliers, croissance structurelle datée, modèle scalable. Date : 2026-11-03.
Recherches web : 9 sur 15 (arrêt volontaire : sources officielles lisibles épuisées). Preuves : 18. Domaines : insee.fr, drees.solidarites-sante.gouv.fr, service-public.gouv.fr, education.gouv.fr, facco.fr, moneyvox.fr, hellosafe.fr, lessentieldeleco.fr, echosdunet.net, acadomia.fr, trustpilot.com, recherche-entreprises.api.gouv.fr (12).
Règle : toutes les pages ci-dessous ont été ouvertes avec WebFetch (ou API curl) ; sinon [NON OUVERT].
Modèles : A téléassistance/maintien à domicile seniors ; B assurance santé animale (assurtech) ; C soutien scolaire (abonnement en ligne).

## Modèle A : téléassistance seniors

### U2-PART-01 : population 75 ans et plus
- Acteur / marché : seniors, France
- Type : tendance (source institutionnelle)
- Source : https://www.insee.fr/fr/statistiques/5893969 (ouverte, projections 2021-2070, scénario central)
- Citation : « Le nombre d'habitants de 75 ans ou plus devrait croître de 5,7 millions sur cette période »
- Chiffres : 75+ = 6,41 M en 2021, 11,33 M en 2050 (calcul de l'outil de lecture sur les tableaux : +77 %, ≈ +2,3 %/an). La date de la page est antérieure à juin 2026 (nouvelle projection Insee citée en extrait de recherche, [NON OUVERT]).
- Ce que ça dit pour nous : moteur structurel daté fort, volume (personnes), France.

### U2-PART-02 : bénéficiaires APA
- Type : tendance (institutionnelle)
- Source : https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse-documents-de-reference/panoramas-de-la-drees/251001-Panoramas-aide-sociale-personnes-%C3%A2g%C3%A9es-ou-handicap%C3%A9es (ouverte, 2025)
- Citation : « Fin 2023, 1,36 million de personnes de 60 ans ou plus la perçoivent, soit 7,2 % »
- Chiffres : +2,1 % de bénéficiaires en un an (2023). PDF Drees fiche APA illisible.
- Ce que ça dit pour nous : 2 sources institutionnelles (Insee + Drees) pour la demande ; la croissance en valeur du marché téléassistance reste non sourcée.

### U2-PART-03 : prix publics téléassistance (3 prix)
- Acteur / marché : Redion, Nexecur, vendus aux seniors
- Type : argent dépensé (prix publics)
- Source : https://www.echosdunet.net/domotique/teleassistance-seniors (ouverte, prix datés oct. 2026, issus du comparateur Selectra)
- Citation : « C'est un crédit, pas une réduction »
- Chiffres : Redion Domveil Plus 25,90 €/mois (12,95 € après crédit d'impôt) ; Nexecur Formule Domicile 29,90 € ; Nexecur Formule Aidant 42,90 € ; Redion Géoveille 33,90 €. Installation Nexecur à domicile 149 €. Nombre d'abonnés : non donné.
- Ce que ça dit pour nous : 4 prix publics 26 à 43 €/mois, soit 310 à 515 €/an par client.

### U2-PART-04 : crédit d'impôt 50 % (moteur de solvabilité)
- Type : obligation/réglementaire (aide)
- Source : https://www.service-public.gouv.fr/particuliers/vosdroits/F12 (ouverte)
- Citation : « Téléassistance et visio-assistance, si elles permettent le maintien à domicile d'une personne fragile »
- Chiffres : crédit 50 %, plafond 12 000 € de dépenses (+1 500 € si membre du foyer > 65 ans) ; la page 2026 liste aussi la livraison de repas.
- Ce que ça dit pour nous : le prix net payé est divisé par deux ; vaut aussi pour soutien scolaire à domicile (modèle C).

### U2-PART-05 : CA des acteurs en place
- Type : argent dépensé (comptes déposés)
- Source : https://recherche-entreprises.api.gouv.fr/search?q=NEXECUR (et REDION, FILIEN, ASSYSTEL) (API ouverte via curl, 2026-11-03)
- Citation : « ca » 102917897 (Nexecur Protection, 2024) ; champ JSON, pas de texte
- Chiffres : Nexecur Assistance 4,65 M€ (2024, +0,19 M€ résultat) ; Redion Téléassistance 9,26 M€ (2025, résultat 0,39 M€) ; Filien Écoute ADMR 12,25 M€ (2024, résultat 0,78 M€) ; Assystel 4,75 M€ (2024, résultat −0,04 M€). Nexecur Protection (alarme, pas seulement seniors) 102,9 M€.
- Ce que ça dit pour nous : acteurs rentables mais petits (4 à 12 M€) : marché fragmenté, mais aussi faible taille unitaire. Total de ces 4 : ≈ 31 M€.

### U2-PART-06 : avis négatifs Nexecur
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.nexecur.fr?stars=1&stars=2 (ouverte, avis oct. 2026)
- Citation : « Pas de réponse a la demande de résiliation faite en ligne début septembre 2026 »
- Chiffres : 4,8/5, 7 615 avis, 6 % de 1-2 étoiles ; les avis négatifs portent sur fin de la 2G, matériel, service client (pas sur téléassistance).
- Ce que ça dit pour nous : contre-preuve partielle, satisfaction forte chez le leader : faiblesse faible (résiliation, obsolescence 2G).

### U2-PART-07 : Présence Verte sans avis
- Type : contre-preuve / manque
- Source : https://fr.trustpilot.com/review/www.presenceverte.fr?stars=1&stars=2 (ouverte)
- Citation : « Cette entreprise n'a pas encore reçu d'avis. »
- Chiffres : 0 avis. Le canal d'acquisition passe par mairies/CCAS/départements (extrait de recherche, [NON OUVERT] : listes Isère, Aix).
- Ce que ça dit pour nous : peu de signal en ligne ; vente par prescripteurs publics.

## Modèle B : assurance santé animale (assurtech)

### U2-PART-08 : taille et croissance du marché
- Type : tendance (confiance faible : sites de comparateurs)
- Source : https://hellosafe.fr/assurance-animaux/marche (ouverte, 2026)
- Citation : « 600 millions € de primes annuelles en 2025 »
- Chiffres : 400 M€ en 2020, +8 %/an attendu jusqu'en 2030 ; 5 % d'animaux assurés (~1,1 M) ; chiens 7 %, chats 4 % ; 52 % des foyers ont un animal. Incohérence interne (80 M vs 22,6 M animaux). Pas de source institutionnelle lue : croissance = confiance faible.
- Ce que ça dit pour nous : valeur France, ≈ +8 %/an (400 → 600 M€ en 5 ans = +8,4 %/an calculé).

### U2-PART-09 : contradiction sur la pénétration
- Type : contre-preuve (données)
- Source : https://lessentieldeleco.fr/2175-assurance-sante-animale-la-france-a-la-traine-malgre-un-marche-en-plein-boom/ (ouverte, 2025-05-16)
- Citation : « seuls 35% des propriétaires ont souscrit une assurance santé animale. »
- Chiffres : SantéVet = 189 000 contrats, 69 M€ de CA, « presque la moitié du marché » selon l'article ; Dalma 65 000 animaux, levée 20 M€ (2025). Moneyvox (U2-PART-10) donne 5-6 %. L'écart (5 % à 35 %) est inexpliqué.
- Ce que ça dit pour nous : leader dominant (concentration élevée, 3 premiers acteurs probablement > 40 %), à vérifier ; 69 M€ ≠ moitié de 600 M€ : chiffres incompatibles.

### U2-PART-10 : prix publics assurance
- Type : argent dépensé
- Source : https://www.moneyvox.fr/assurance/actualites/110075/faut-il-assurer-son-animal-de-compagnie-et-a-quel-prix-en-2026 (ouverte, 2026)
- Citation : « Entre 1,5 million et 3,2 millions d'animaux sont assurés en France »
- Chiffres : médiane chien 1 an 11 € (base) à 38 € (premium) /mois ; chat 8 à 26 € ; chien 2 ans premium 45,40 € ; « frais vétérinaires +20 % en 10 ans ». Ce sont des médianes de simulations Meilleurtaux, non des prix d'un assureur.
- Ce que ça dit pour nous : prix payés 100 à 450 €/an ; ≥ 3 prix publics de marché, pas par assureur.

### U2-PART-11 : budget alimentaire (taille du segment animal)
- Type : tendance
- Source : https://www.facco.fr/combien-depensons-nous-pour-nos-chiens-et-chats/ (ouverte, 2026) et https://www.facco.fr/chiffres-cles/les-chiffres-de-la-population-animale-2/ (ouverte)
- Citation : « 73,4M animaux de compagnie en France »
- Chiffres : alimentation 517 €/an/chien, 339 €/an/chat. Population : % foyers non lus (PDF illisible). Facco = fédération.
- Ce que ça dit pour nous : source fédérale pour la dépense animale ; croissance du nombre d'animaux [NON OUVERT].

### U2-PART-12 : avis négatifs Santévet
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.santevet.com?stars=1&stars=2 (ouverte, nov. 2026)
- Citation : « La mensualité à doublée du jour au lendemain, en plein milieu de l'année. »
- Chiffres : 4,2/5, 27 828 avis, 16 % de 1-2 étoiles. Autres : « Ne m'ont pas été remboursés malgré mes nombreuses relances. » (28 oct. 2026) ; vaccins promis remboursés puis non (2 nov. 2026).
- Ce que ça dit pour nous : plaintes précises (hausse de prime, remboursement, promesse commerciale) : angle transparence/prix fixe.

### U2-PART-13 : contre-preuve Manypets
- Type : plainte (concurrent étranger)
- Source : https://fr.trustpilot.com/review/www.manypets.com?stars=1&stars=2 (ouverte)
- Citation : « Claim times are ridicluously long. »
- Chiffres : 4,3/5, 2 454 avis, 8 % de 1-2 étoiles (page FR de Trustpilot, avis en anglais, Royaume-Uni probable).
- Ce que ça dit pour nous : le même défaut (délais de remboursement) existe à l'étranger : modèle réglementé, pas de croissance sans capital et agrément. CA des acteurs français : API sans résultat pour Santévet SAS, Dalma, Assur O'Poil ; SantéVet Holdings CA 0 (comptes holding). CA 2 acteurs : NON OBTENU.

## Modèle C : soutien scolaire en ligne (abonnement)

### U2-PART-14 : demande en baisse (contre-preuve forte)
- Type : contre-preuve (institutionnelle)
- Source : https://www.education.gouv.fr/depp/previsions-d-effectifs-d-eleves-du-premier-degre-la-baisse-devrait-se-poursuivre-jusqu-en-2029-452706 (ouverte, DEPP mars 2025)
- Citation : « La baisse des effectifs devrait se poursuivre aux rentrées suivantes »
- Chiffres : 6 169 800 élèves en 2025, 5 699 800 prévus en 2029 (premier degré, −560 800 vs 2024).
- Ce que ça dit pour nous : pas de croissance démographique ; moteur = intensité de dépense, non démontré.

### U2-PART-15 : prix publics Acadomia
- Type : argent dépensé
- Source : https://www.acadomia.fr/tarifs (ouverte, tarifs 2026/2027)
- Citation : « Le paiement est effectué mensuellement, à la séance consommée »
- Chiffres : cours collectifs en ligne 69 à 114 €/mois TTC ; en centre 76 à 145 €/mois ; à domicile maths 25 à 50 €/h (fourchettes générales de l'article). Collectif non éligible au crédit d'impôt.
- Ce que ça dit pour nous : 3 prix publics (69, 114, 145 €).

### U2-PART-16 : CA Acadomia/Domia
- Type : argent dépensé (comptes)
- Source : API recherche-entreprises, q=ACADOMIA (ouverte via curl)
- Citation : champ « ca » 104147000 (Domia Group, 2023, résultat 6,74 M€)
- Chiffres : Junior Kid (Acadomia) 5,66 M€ (2025, résultat −0,31 M€) ; Acadomia Pro 3,32 M€ (2025, −0,10 M€).
- Ce que ça dit pour nous : acteur historique à ~104 M€ : marché installé, filiales déficitaires.

### U2-PART-17 : avis négatifs Acadomia
- Type : plainte
- Source : https://fr.trustpilot.com/review/www.acadomia.fr?stars=1&stars=2 (ouverte, 2026)
- Citation : « Une fois le RIB fourni, prélèvement sans avertissement »
- Chiffres : 4,4/5, 8 067 avis, 6 % de 1-2 étoiles ; « Très déçue par le service administratif. » (22 avr. 2026).
- Ce que ça dit pour nous : faiblesse faible, satisfaction élevée.

### U2-PART-18 : Wamiz (pet média) sans signal
- Type : contre-preuve
- Source : https://fr.trustpilot.com/review/wamiz.com?stars=1&stars=2 (ouverte)
- Citation : « Aucun résultat »
- Chiffres : 1 avis. API : Wamiz 2025 CA = 0 (confidentiel), résultat 184 007 €.
- Ce que ça dit pour nous : aucune donnée exploitable.

## Sources non lues
- https://www.facco.fr/wp-content/uploads/2025/06/2025-06-facco-chiffres-odoxa.pdf : PDF illisible.
- Drees fiche APA PDF : illisible. Insee projection 2026 (Insee Première 2108) : extrait seulement.
- https://www.isere.fr/sites/default/files/2025-11/liste-telealarme-isere.pdf : contenu vide.
- trustpilot dalma.fr : 404. Listes Pays d'Aix et catalogues Présence Verte : extraits seulement.
