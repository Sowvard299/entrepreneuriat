# Piste : contrat d'électricité géré en continu, payé au résultat

Ouverte le 2026-11-14, à partir de CompareWatt (Yenka), vu par l'équipe. Statut : **porte 1 non passée**
(recherche web seule, `outils/donnees.py` pas encore lancé). Rien n'est publié ni dépensé.

## Le modèle
À partir de la courbe Linky (consentement Enedis), le service garde le foyer sur le bon fournisseur, la bonne
option (base, heures creuses, Tempo) et la bonne puissance, et change de contrat sous mandat.
Variante testée ici : **paiement au résultat** (25 à 30 % de l'économie mesurée face au Tarif Bleu), réservé
aux **foyers chauffés à l'électricité** ou à plus de 8 000 kWh/an. Pas de commission fournisseur (courtage
écarté le 2026-11-02).

## Chiffres (2026-11-14)
- 35,1 M de sites résidentiels électricité, 55,2 % au Tarif Bleu fin mars 2026 (CRE T1 2026, repris par un
  comparateur : N3 à relire dans le PDF).
- 30,9 M de résidences principales (SDES, 1er janvier 2025) ; 36-37 % chauffées à l'électricité (SDES 2020,
  JeChange 2022) → ≈ 11 M de foyers, ≈ 6 M encore au Tarif Bleu [HYPOTHÈSE : même part que l'ensemble].
- Gain de l'offre la moins chère face au Tarif Bleu : 2 à 3 c€/kWh (94 € pour 3 099 kWh, 186 € pour 5 700 kWh,
  344 € pour 10 800 kWh ; comparateurs, juillet à octobre 2026 ; remise max tombée à -10 % HT en octobre).
- Gain des changements suivants : 0,5 à 1 c€/kWh [HYPOTHÈSE] ; capture CompareWatt de l'équipe : 0,7 c€/kWh.
- Tempo, foyer 10 800 kWh (tarifs au 1er août 2026, profil supposé) : 2 179 € d'énergie sans effacement contre
  2 144 € en base ; 1 951 € si la moitié des heures pleines rouges est décalée. Le gain Tempo vient du
  comportement, pas du contrat.

## Économie unitaire (calcul, hypothèses entre crochets)
| Foyer | Commission | An 1 | An 2 | Total sur 3 ans [70 % restent après l'an 1] |
|-------|------------|------|------|------|
| 8 000 kWh | 25-30 % | 40-72 € | 10-24 € | 54-106 € |
| 11 000 kWh | 25-30 % | 55-99 € | 14-33 € | 74-145 € |

Coût d'acquisition [HYPOTHÈSE, CPC énergie non trouvé] : CPC 2 à 5 €, 2 à 5 % des visiteurs signent → 40 à 250 €.
Le modèle ne tient que si le coût d'acquisition reste sous ≈ 80 €. C'est la croyance la plus fragile.

## Concurrence et contre-preuves
- Gratuits : comparateur du médiateur (données Linky réelles), Selectra (106 M€ de CA 2024, commissions
  fournisseurs), Hello Watt, papernest. Aucun ne change de contrat seul en continu pour les ménages (non trouvé).
- Pilotage du chauffage : Voltalis, gratuit pour le foyer (payé par la flexibilité), ≈ 200 000 foyers
  (Que Choisir, non daté). Capte déjà le gain des jours rouges : ne pas en faire le cœur de l'offre.
- Royaume-Uni : auto-switching gratuit (Look After My Bills, Weflip, Migrate) et payant (Flipper, ≈ 25 £/an).
  Look After My Bills a cessé son activité (date et cause non établies ; crise 2021-2022 probable [HYPOTHÈSE]).
- Payer au pourcentage de l'économie : aucun service trouvé en France pour les ménages (trou ou impasse).
- Les remises se réduisent (jusqu'à 19 % HT en juillet, 10 % en octobre 2026) : si l'écart avec le Tarif Bleu
  disparaît, le revenu aussi.

## Droit (à faire citer par l'auditeur avant toute finale)
- Changement gratuit, sans coupure, sans limite de nombre (Médiateur, fiche pratique).
- Informations précontractuelles : C. conso. L.224-3 (17 mentions) et L.224-4 (support durable) : à faire
  parvenir au client malgré le mandat.
- PPL n° 1845 du 16/09/2025 (registre et obligations des courtiers en énergie) : statut non établi.
- Démarchage téléphonique interdit sans consentement depuis le 11/08/2026 (loi n° 2025-594).
- Non établi : régime du mandat de souscription, données Linky (consentement Enedis Data Connect).

## Probabilités (2026-11-14, preuves N3 au mieux : on reste près du taux de base)
Classe de référence : services d'information, société (survie à 5 ans 65,7 %, SINE 2018).
- P(passer la porte 2) = **15 %** : acquisition payante face à des concurrents gratuits très présents.
- P(en vie à 3 ans) = **50 %** : revenu lié à un écart de prix qui se réduit.
- P(CA ≥ 500 k€ à 3 ans) = **5 %** : il faut ≈ 5 000 à 9 000 foyers actifs à 55-100 €/an.

## Test porte 2 (prêt, pas lancé)
**Croyance testée** : des foyers chauffés à l'électricité confient leur contrat et versent un acompte
remboursable à un service qui n'existe pas encore, pour un coût d'acquisition sous 80 €.

- Page : analyse gratuite de la courbe Linky (ou saisie de la facture), puis offre « on gère votre contrat,
  30 % de l'économie mesurée, rien si pas d'économie », acompte de 19 € remboursable et déduit de la première
  commission.
- Mentions obligatoires (CLAUDE.md, porte 2) : service pas encore lancé + date de début (≤ 30 jours par défaut),
  bouton « commande avec obligation de paiement », rétractation 14 jours, informations RGPD art. 13.
- Trafic : Google Ads sur « tempo », « facture chauffage électrique », « changer fournisseur électricité
  maison » ; budget 1 000 €.
- **Seuil écrit avant** : ≥ 13 acomptes pour 1 000 € (coût par acompte ≤ 77 €), dont ≥ 70 % à plus de
  8 000 kWh/an. En dessous de 5 acomptes : STOP. Entre les deux : un second essai avec un autre message.
- Ressources : page + paiement (≈ 1 semaine), 1 000 € de publicité, société créée pour encaisser.
  À décider par l'équipe : rien n'est publié ni dépensé sans accord.

### Page de test prête (2026-11-14, `page-test/`)
Nom retenu : **Contrat Juste** (contratjuste.fr libre au registre AFNIC le 2026-11-14). Fichiers : `index.html`
(calculateur, prix, pour qui, questions, commande), `cgv.html`, `mentions-legales.html`, `confidentialite.html`,
`styles.css`, `DESIGN.md`, `og.png`, icônes, `annonces-google-ads.md` (mots-clés, annonces, seuil, suivi).
Vérifiée en local : ordinateur et mobile 375 px, mode sombre, console sans erreur, aucun débordement.

**À faire par l'équipe, dans l'ordre :**
1. Créer la micro-entreprise (guichet unique INPI) et obtenir le SIREN.
2. Désigner un médiateur de la consommation (obligatoire pour vendre aux particuliers).
3. Acheter contratjuste.fr ; héberger les fichiers de `page-test/` (sauf `outils/`) sur Netlify ou GitHub Pages, HTTPS.
4. Ouvrir Stripe au nom de la micro-entreprise ; créer un Payment Link de 19 € avec deux champs
   (chauffage électrique oui/non, consommation annuelle en kWh) et une redirection après paiement ;
   coller le lien dans `STRIPE_URL` (index.html).
5. Remplacer tous les `[À COMPLÉTER]` (date de lancement ≤ 30 jours après la mise en ligne, nom, adresse,
   SIREN, e-mail, hébergeur, TVA) et faire relire les CGV.
6. Ouvrir Google Ads et lancer la campagne de `annonces-google-ads.md` (1 000 €).
7. Avant tout lancement réel du service : faire citer par l'auditeur le régime du mandat et le statut de la
   PPL n° 1845, et prévoir le remboursement de tous les acomptes si le test échoue.

## Sources
- CRE, observatoire T1 2026 : https://www.cre.fr/fileadmin/Documents/Rapports_et_etudes/2026/Observatoire_T1_2026.pdf
- Kelwatt, Tarif Bleu au 1er août 2026 : https://www.kelwatt.fr/actu/tarif-edf-reglemente-1er-aout-2026
- Kelwatt, Tempo : https://www.kelwatt.fr/fournisseurs/edf/tempo/prix
- Hello Watt, octobre 2026 : https://www.hellowatt.fr/blog/meteo-energie-octobre-2026/
- Selectra, juillet 2026 : https://selectra.info/energie/electricite/moins-cher
- JeChange, 94 € d'écart : https://www.jechange.fr/energie/electricite/news/facture-electricite-94-euros-economie-tarif-reglemente
- SDES, chauffage des ménages : https://www.statistiques.developpement-durable.gouv.fr/les-energies-de-chauffage-des-menages-en-france-metropolitaine
- Selectra, groupe (CA 2024) : https://selectra.info/groupe
- Médiateur, changer de fournisseur : https://www.energie-info.fr/fiche_pratique/je-souhaite-changer-de-fournisseur-delectricite-ou-de-gaz-naturel/?pdf=225
- Légifrance, L.224-3 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051560284
- PPL n° 1845 : https://www.assemblee-nationale.fr/dyn/17/textes/l17b1845_proposition-loi.pdf
- ADIL, loi du 30 juin 2025 : https://www.anil.org/adil-44/les-info-semaines-de-ladil/200226-apports-loi-du-30-juin-2025-lutte-contre-les-fraudes-aux-aides-publiques-en-matiere-de-logement/
- Que Choisir, Voltalis : https://www.quechoisir.org/actualite-chauffage-que-cachent-les-thermostats-connectes-gratuits-n115646
- Which?, auto-switching : https://www.which.co.uk/news/2020/03/is-energy-autoswitching-right-for-you/
- Look After My Bills, fin d'activité : https://www.householdmoneysaving.com/look-after-my-bills-review/
