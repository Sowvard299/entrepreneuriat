# W4 : notation mieux calibrée, synthèse (2026-11-03)
Statut : partiel. 25 preuves (W4-1 à W4-25), 19 domaines, 15/15 recherches web. Détail : methode/audit-2026-11/w4-notation-travail.md. Chiffres Insee, Banque de France, Strategyzer, YC, CB Insights revérifiés dans le HTML ; W4-14 et le corps de W4-21 lus par résumé automatique.

## Modifications proposées de la grille et des portes
| # | Modification | Preuves | Confiance |
|---|---|---|---|
| 1 | Taux de base d'abord : avant toute note, écrire la classe de référence (secteur Insee × société / entreprise individuelle / micro) et son taux de survie. La note déplace cette probabilité, elle ne la remplace pas ; toute probabilité d'équipe au-dessus du taux de base cite une preuve. | W4-1 à W4-4, W4-6, W4-13 | forte pour les taux, moyenne pour la règle |
| 2 | Probabilités datées au lieu de points décimaux : P(passer la porte 2), P(survie à 3 ans), P(CA ≥ 500 k€ à 3 ans), par pas de 5 points [HYPOTHÈSE de pas], score de Brier après résolution, mise à jour par règle écrite. Le défaut de « 7,35 contre 7,20 » est l'absence de suivi, pas la précision. | W4-8, W4-9, W4-14 | moyenne |
| 3 | Niveau de preuve 0 à 5 sur chaque ligne. Un niveau 0 à 2 (dire, maquette) ne déplace pas la probabilité du taux de base (régression vers la moyenne de la classe) ; 3 à 5 (action du client : rendez-vous, précommande, lettre d'intention) peut la déplacer, d'un écart maximal par niveau à fixer avant la porte 2 [HYPOTHÈSE]. L'ordre argent > recherche > plainte > tendance reste cohérent avec dire / faire [INFÉRENCE]. | W4-15, W4-6 | moyenne (source de vendeur) |
| 4 | Poids égaux ou intervalle : rien ne justifie 25/25/20/15/15 ; calculer avec plusieurs jeux de poids, afficher l'intervalle, ne pas départager deux pistes dont les intervalles se recouvrent. | W4-25 | moyenne (seuils éliminatoires non testés) |
| 5 | Aucun bonus ni malus d'ordre d'entrée ; juger un suiveur sur la rentabilité et la survie de ses semblables, pas sur la part de marché. | W4-18, W4-19, W4-12 | moyenne |
| 6 | Modèle étranger : écrire la cause du succès, séparer opérations copiées et cible / prix / offre à tester en France ; la porte 2 porte sur la partie adaptée. | W4-20, W4-21 | faible (deux cas) |
| 7 | Porte 3 : deux lignes absentes de la grille, timing et économie unitaire, en questions de test sans poids tirés des classements de causes d'échec (déclaratifs, biaisés). | W4-11, W4-16, W4-22, W4-23, W4-24 | faible |
| 8 | Porte 4 : comparer le pilote à la courbe de survie de la classe (ensemble 94,6 / 88,0 / 81,3 / 74,1 / 69,0 % à 1-5 ans ; sociétés 83,4 % à 3 ans) et aux CA constatés (micro actifs : médiane 12 000 €). | W4-2, W4-3, W4-4 | moyenne |
| 9 | Ne pas importer les seuils du capital-risque (croissance du marché 20 %/an, produit 10 fois meilleur, marché > 100 m, marge brute 40 %) : portée différente de nos 500 k€. | W4-16, W4-17 | moyenne |

## Taux de base (Insee, survie à 5 ans, hors micro ; génération 2018, min-max 2010 / 2014 / 2018) [W4-1]
Commerce 63,9 (52,4-63,9) ; hébergement-restauration 64,0 (57,5-64,0) ; services admin. 65,6 (59,4-65,6) ; info-com 65,7 (59,6-65,7) ; construction 68,5 (54,7-68,5) ; transports 69,2 (67,5-69,2) ; autres services 69,5 (60,2-69,5) ; immobilier 69,8 (56,2-69,8) ; industrie 73,4 (64,2-73,4) ; spécialisées 73,8 (68,5-73,8) ; enseignement-santé 74,1 (74,1-74,8) ; finance 77,3 (67,0-77,3) ; ensemble 69,0 (60,4-69,0).
Sociétés 70,6 contre entreprises individuelles 63,3 [W4-2] ; micro-entrepreneurs 28 % [W4-4]. Des 8 points de hausse 2014-2018, 3 viennent d'un effet de structure et la Covid a joué : 2018 est un haut de fourchette [W4-2]. Défaillances fin août 2026 : 70 766 sur 12 mois, +19,3 % sur la moyenne 2010-2019 [W4-5].

## Contre-preuves
W4-6 : la vue extérieure rate les cas extrêmes. W4-19 contredit W4-18 sur le biais de survivant. W4-25 : transfert aux seuils éliminatoires non démontré. W4-11 : CB Insights, vendeur de données, start-up financées par capital-risque : confiance faible.

## Ce que je n'ai pas pu établir
- Taux de défaillance par secteur : la Banque de France publie des nombres, sans stock ni taux ; définition des procédures comptées non obtenue [W4-5].
- Probabilité d'atteindre 500 k€ de CA à 3 ans par secteur : aucune source (piste : Esane ou FARE) ; seul repère, CA des micro actifs [W4-4].
- Taux de succès des transpositions d'un modèle étranger : aucune étude à grand échantillon, deux cas seulement [W4-21] ; aucune donnée de taux de succès des imitateurs lue chez Shenkar [W4-20].
- Textes non lus (403 ou payants) : critères de Timmons d'origine, livre « Testing Business Ideas », Kahneman et Lovallo 1993 et 2003, dix commandements de Tetlock, Cantamessa en texte intégral [W4-22].
- Lien empirique entre nos cinq critères et la survie ou le CA d'une PME : aucun trouvé, les poids restent [HYPOTHÈSE].
- Critique méthodologique publiée de CB Insights : aucune trouvée ; seule la critique générale du biais d'attribution des fondateurs [W4-23, W4-24, INFÉRENCE].

## Conclusion
1. Correction la plus solide : ancrer chaque note sur le taux de survie Insee de la classe ; l'écart entre micro (28 %) et société (70,6 %), ou entre commerce (63,9 %) et finance (77,3 %), est mesuré, alors que 7,35 contre 7,20 ne repose sur aucune mesure.
2. Seconde correction : probabilités datées, scorées, avec niveau de preuve par ligne ; c'est ce qui rend les notes comparables et corrigeables.
3. À éviter : des poids tirés des classements de causes d'échec (déclaratifs, biaisés), un bonus d'ordre d'entrée, et lire 2018 (69 %) comme norme durable.
