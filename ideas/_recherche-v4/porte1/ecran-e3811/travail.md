# E3811 Collecte des déchets non dangereux : travail (2026-11-03)
Mission : comprendre la croissance, trouver 1 à 3 modèles qui encaissent, tester le meilleur. Biodéchets exclus.
Recherches web utilisées : 5 / 15 (REP PMCB, prix benne, Lemon Tri, prix papier ; ouverture ministère refusée par DNS). Preuves : 12. Domaines : eurostat, insee, recherche-entreprises.api.gouv.fr, data.economie.gouv.fr, hellopro, prix-travaux-m2.
Statut : partiel. Manque : ≥3 prix publics B2B (2 pages ouvertes, N4), REP PMCB (page ministère inaccessible), grille Smd3 (PDF illisible), économie unitaire, avis.

### E38-01 : Taille et croissance du code
- Acteur / marché : collecte de déchets non dangereux, France, valeur
- Type : tendance
- Source : https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=FR&geo=FR&nace_r2=E3811&indic_sbs=NETTUR_MEUR (date : 2026-11-03 ; N1 ; Eurostat)
- Citation : « 2024 : 3 989 M€ ; 1 913 entreprises »
- Chiffres : 2021 2 316 M€ / 1 140 entreprises, 2024 3 989 M€ / 1 913 ; +19,9 %/an
- Ce que ça dit pour nous : le nombre d'entreprises a grimpé de 68 % : la croissance Eurostat est en partie un effet de périmètre ou de déclaration.

### E38-02 : Croissance INSEE (contre-preuve à +20 %)
- Acteur / marché : idem, indice de CA en valeur (prix inclus)
- Type : contre-preuve
- Source : https://api.insee.fr/melodi/data/DS_ICA?ACTIVITY=38.11&FREQ=M&SEASONAL_ADJUST=Y&maxResult=5000 (date : 2026-11-03 ; N1 ; INSEE)
- Citation : « Croissance annuelle moyenne sur 3 ans (2022-2025) : +5.9 %/an »
- Chiffres : indice 100 (2021) à 129,1 (2025) ; 5 ans +7,6 %/an ; médiane des secteurs +3,0 %
- Ce que ça dit pour nous : croissance réelle probable 6-8 %/an en valeur, inflation et hausses de tarifs de traitement comprises : sous le seuil de 8 %. Effet prix non séparable [NON ÉTABLI].

### E38-03 : Fragmentation
- Acteur / marché : 38.11Z
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=38.11Z&etat_administratif=A&ca_min=100000000&per_page=25 (date : 2026-11-03 ; N1 ; Insee Sirene/RNE)
- Citation : « Part des 3 premières entités dans le CA du secteur E3811 (2024) : 29.9 % »
- Chiffres : 4 148 entreprises actives, 840 employeuses, 442 de 10 salariés ou plus ; 15 à 100 M€ ou plus (SEPUR 484,5 M€, COVED 434,3, Pizzorno 274,5) ; borne basse, par entité juridique
- Ce que ça dit pour nous : sous 40 % ; groupes (Suez RV x3, Nicollin x3) à regrouper, donc part réelle plus haute.

### E38-04 : Milieu de marché rentable (CA déposé)
- Acteur / marché : 144 entreprises 38.11Z de 3 à 40 M€ de CA
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=38.11Z&etat_administratif=A&ca_min=3000000&ca_max=40000000&per_page=25 (date : 2026-11-03 ; N1 ; Insee/RNE comptes déposés)
- Citation : « Part des 3 premières entités dans le CA du secteur E3811 (2024) : 29.9 % »
- Chiffres (CA ; résultat net) : Cedre 17,7 M€ ; +0,53 (2024) / Maine Collecte Valorisation 23,0 ; +0,48 (2024) / HC Environnement 22,2 ; +1,39 (2025) / Entreprise Bronzo 18,2 ; +2,89 (2025) / EDIB 9,9 ; +0,19 (2025) / Lemon Tri 12,4 ; +0,20 (2025) / Tribord 10,0 ; +0,03 (2025)
- Ce que ça dit pour nous : au moins 7 acteurs régionaux de 10 à 23 M€ encaissent, à l'équilibre ou légèrement bénéficiaires ; marges 1-5 % du CA (Bronzo 16 %).

### E38-05 : Acteurs en perte (faiblesse)
- Acteur / marché : même fichier, plus Recygo (38.32Z) et Ecodrop (82.99Z)
- Type : plainte
- Source : https://recherche-entreprises.api.gouv.fr/search?q=RECYGO&per_page=3 (date : 2026-11-03 ; N1 ; Insee/RNE comptes déposés)
- Citation : « Part des 3 premières entités dans le CA du secteur E3811 (2024) : 29.9 % »
- Chiffres : XL Recycling 17,1 M€ ; -3,37 M€ (2024) / ECT Collecte 10,3 M€ ; -1,35 M€ (2022) / Les Alchimistes 6,4 M€ ; -1,95 M€ (2024) / Recygo 19,4 M€ ; -0,83 M€ (2024) / Ecodrop 21,8 M€ ; -0,69 M€ (2024)
- Ce que ça dit pour nous : les acteurs à croissance rapide (Recygo, Ecodrop, Alchimistes) perdent de l'argent : contre-preuve du modèle « startup du tri ». Aucune procédure collective vue sur ces SIREN (BODACC : 5 premiers avis, dépôts de comptes et modifications seulement ; non exhaustif).

### E38-06 : Clients potentiels (artisans du bâtiment)
- Acteur / marché : électriciens 43.21A et finitions 43.39Z, cible des bennes de chantier
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=43.21A&etat_administratif=A&per_page=1 (date : 2026-11-03 ; N1 ; Insee)
- Citation : « Entreprises actives 43.21A : 124 938 »
- Chiffres : 43.21A 124 938 actives dont 25 524 employeuses ; 43.39Z 28 830 dont 2 327 employeuses
- Ce que ça dit pour nous : plus de 25 000 employeurs dans un seul code BTP : seuil de 3 000 clients largement franchi. Dépense annuelle par client : [HYPOTHÈSE].

### E38-07 : Marchés publics, location de benne
- Acteur / marché : collectivités, « location benne »
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22location+benne%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; N1 ; DECP)
- Citation : « plancher, pas un total »
- Chiffres : 2022 6 marchés 21,4 M€ ; 2023 40 / 33,0 ; 2024 107 / 128,1 ; 2025 185 / 100,8 ; 2026 83 / 103,9 (montant = valeur max des accords-cadres)
- Ce que ça dit pour nous : commande publique de bennes en forte hausse (x30 en 3 ans) mais accords-cadres lourds ; « collecte déchets entreprises » : 2-3 marchés par an ; « collecte papier bureau » : 14 en 2025 (0,4 M€).

### E38-08 : Prix public benne 10 m3 (prix 1)
- Acteur / marché : location benne avec traitement, B2B
- Type : argent dépensé (prix affiché, pas une dépense)
- Source : https://conseils.hellopro.fr/quel-est-le-prix-d-une-benne-a-dechet-grand-volume-1562.html (date : novembre 2026 selon la page ; N4 ; HelloPro, place de marché)
- Citation : « Ces montants sont donnés hors taxes et à titre indicatif. »
- Chiffres : 10 m3, 7 jours : 200 / 400 / 600 € HT (min / moyen / max)
- Ce que ça dit pour nous : ticket moyen ~400 € HT par rotation ; N4, inutilisable dans un score.

### E38-09 : Prix évacuation gravats (prix 2)
- Acteur / marché : évacuation de gravats de chantier
- Type : argent dépensé (prix affiché)
- Source : https://www.prix-travaux-m2.com/prix-evacuation-gravats.php (date : 2026-06-06 ; N4 ; site de prix indicatifs)
- Citation : « Généralement, le prix d'évacuation des gravats tourne autour de 35 euros à 70 euros HT / m3. »
- Chiffres : 35-70 € HT/m3 ; benne 200-700 € HT/jour
- Ce que ça dit pour nous : cohérent avec E38-08 (40 € HT/m3 en moyenne). Troisième prix : [NON OUVERT] (Smd3 : 235 € HT d'abonnement + 0,08-0,15 €/litre, extrait de recherche).

### E38-10 : REP bâtiment, moteur réglementaire (non ouvert)
- Acteur / marché : filière PMCB (produits et matériaux de construction du bâtiment)
- Type : obligation
- Source : [NON OUVERT] annonce de refondation du ministère, 2026-02-19 (DNS en échec deux fois). Piste N5 : plus de 6 000 points de reprise, quatre éco-organismes.
- Citation : aucune (non lue)
- Ce que ça dit pour nous : la REP PMCB peut créer de la collecte payée par éco-organisme ; non établi qu'elle explique la croissance du code 38.11.

### E38-11 : Obligation tri 5 flux
- Acteur / marché : producteurs de déchets non dangereux collectés par un prestataire privé
- Type : obligation
- Source : [NON OUVERT] plaquette du ministère (N5, extrait de recherche). Texte à citer : décret n°2016-288 du 10 mars 2016, Légifrance non ouvert.
- Citation : aucune (non lue)
- Ce que ça dit pour nous : moteur ancien (2016) : n'explique pas une accélération 2022-2024.

### E38-12 : Prix introuvables du tri 5 flux en abonnement
- Acteur / marché : Lemon Tri et prestataires de tri de bureaux
- Type : contre-preuve
- Source : [NON OUVERT] recherches web, aucun tarif publié trouvé (N5)
- Citation : aucune (non lue)
- Ce que ça dit pour nous : prix sur devis seulement : pas de prix public vérifiable pour ce segment.

## Conclusions
Modèle retenu (meilleur) : enlèvement de déchets de chantier par bennes pour artisans du BTP (clients E38-06, CA E38-04). Alternatives : tri 5 flux bureaux (concurrents en perte E38-05, prix non publics), collecte de papier de bureau (marché public minuscule).
Croyance la plus fragile : un entrant sans centre de tri ni camions peut marger au-dessus de 1-5 % (E38-04) en revendant l'enlèvement, face aux exploitants de plateformes de traitement. Test porte 2 sans entretien : page « réserver une benne 10 m3, créneau sous 48 h, dépôt remboursable de 100 € » (L.221-14, L.221-18), ciblée sur artisans d'une métropole ; seuil écrit avant, par exemple 15 dépôts pour 3 000 € de pub [HYPOTHÈSE à calibrer].
Probabilités (2026-11-03 ; taux de base SINE ensemble 69,0 % à 5 ans, classe exacte [HYPOTHÈSE]) : P(porte 2) 30 % ; P(vie à 3 ans) 60 % ; P(CA ≥ 500 k€ à 3 ans) 25 %. Aucune preuve N1-N2 sur l'économie unitaire ne déplace ces valeurs au-delà d'E38-04 et E38-05.

## Sources non lues
- https://www.ecologie.gouv.fr/presse/refondation-rep-pmcb-filiere-plus-efficace-plus-lisible-economiquement-soutenable : DNS en échec
- https://smd3.fr/wp-content/uploads/2022/12/grille-tarifaire-2023.pdf : PDF illisible
- https://www.occitanie.developpement-durable.gouv.fr/IMG/pdf/plaquette_ministere.pdf : non ouvert
