# Audit A : marketing pour TPE (I1 artisans, I2 salons de beauté, I4 vidéos courtes)

Date : 13 octobre 2026. Auditeur A, phase 4. Règles de preuve de `signaux/_consignes-communes.md` : URL, date, citation de 15 mots maximum, [HYPOTHÈSE] sinon.
IDs de preuve de cet audit : A-xx. Les IDs F-xx renvoient aux signaux de phase 2.

## Données registre (API Recherche d'entreprises, consultée le 2026-10-13)

### A-01 : tailles des acteurs (API `recherche-entreprises.api.gouv.fr/search?q=<nom>`, champ `finances`)
| Acteur | SIREN | Effectif (tranche) | CA | Résultat net |
|---|---|---|---|---|
| LOCAL.FR (Rueil-Malmaison 92100, créée 1984, NAF 62.01Z) | 331221150 | 250 à 499 salariés (code 32) | 51 128 553 € (2024) | -75 784 € (2024) |
| SOLOCAL (PagesJaunes, 92100) | 444212955 | 1 000 à 1 999 (code 42) | 265 148 000 € (2024) | -18 072 000 € (2024) |
| SOLOCAL MARKETING SERVICES | 422041426 | 250 à 499 (code 32) | 64 216 000 € (2025) | 15 181 000 € (2025) |
| PLANITY (Paris 2e, créée 2016) | 821511128 | 250 à 499 (code 32) | non publié (finances nulles) | non publié |
| Treatwell FR (F2-03) | 752044503 | - | 11 585 554 € (2024) | -7 564 796 € (2024) |
| FRESHA.COM SV IRELAND LIMITED (établissement français, créé 2024) | 932393929 | non déclaré | non publié | non publié |
| HABITATPRESTO (Paris 15e, 2005) | 483343356 | 20 à 49 (code 12) | 4 829 532 € (2024) | -62 083 € (2024) |
| TRAVAUX.COM (13290, 2006) | 489170001 | 6 à 9 (code 11) | 23 084 379 € (2024) | 1 740 472 € (2024) |
| OBAT (logiciel devis-factures artisans, Nantes, 2019) | 852304229 | 100 à 199 (code 22) | 0 € déclaré (2022, comptes probablement non détaillés) | -2 616 141 € (2022) |
| SYSTEM LOG (éditeur probable de Batappli, 60000) [HYPOTHÈSE : rapprochement par nom] | 422467621 | 20 à 49 | 2 214 710 € (2023) | -302 638 € (2023) |

Lecture : Local.fr est une grosse PME rentable à l'équilibre (51 M€), pas une start-up fragile. Le modèle « site + visibilité à l'abonnement pour TPE » fait donc au moins 51 M€ de CA chez un seul acteur, et environ 330 M€ chez Solocal (deux entités). Travaux.com fait 23 M€ de CA avec moins de 10 salariés : la vente de leads aux artisans est très rentable.

---

# I1. Visibilité locale sans engagement pour artisans du bâtiment

## 1. Concurrents réels

### A-02 : Local.fr (concurrent direct n°1)
- **Qui** : LOCAL.FR SA/SAS, SIREN 331221150, siège Rueil-Malmaison (92), créée en 1984, 250 à 499 salariés (A-01).
- **Ce qu'ils vendent** : sites vitrine, e-commerce, réservation, Click&Collect, référencement SEO/SEA, Google Ads, présence annuaires et GPS, logo. Cibles affichées : bâtiment, commerce, restauration, beauté, taxi, auto, agriculture.
- **Taille** : CA 2024 = 51 128 553 €, résultat net 2024 = -75 784 € (API, A-01). Page d'accueil : « 25 000 professionnels qui nous font confiance », « 800 sites créés par mois », « 21 agences » (https://www.local.fr/, consulté le 2026-10-13). Recoupement : 51,1 M€ / 25 000 clients = environ 2 045 € par client et par an, soit environ 170 €/mois, cohérent avec les prix cités par les clients (calcul, pas une donnée publiée).
- **Prix public** : non publié sur le site (aucune page tarif ni CGV liée en pied de page). Prix constatés dans les avis : « Je règle 142,80 € par mois pour mon site internet. » (Chris, Trustpilot, 2026-09-29) ; 170 à 180 €/mois sur 60 mois (F1-05).
- **Durées d'engagement** : avis et réponses de l'entreprise citent des options de 24, 36, 48 ou 60 mois. Réclamation de « environ 11 000 € » après cessation d'activité (Dani, 2026-09-23).
- **Avis clients** : Trustpilot 4,5/5 sur 6 855 avis, 2 048 sur les 12 derniers mois ; l'entreprise répond à 98 % des avis négatifs, avec des réponses quasi identiques (https://fr.trustpilot.com/review/www.local.fr?stars=1, consulté le 2026-10-13). **Contradiction à garder** : la grande majorité des clients notent bien. L'insatisfaction concerne une minorité (environ 12 % de 1-2 étoiles, F1-05), mais elle porte exactement sur notre angle (engagement, résiliation).
- **Faiblesses citées par leurs clients** :
  1. Engagement long découvert après coup : « il n'a jamais été question de 24 ou 36 mois » (Daugas, Trustpilot, 2026-09-23).
  2. Suivi qui disparaît : « conseillé fantôme qui disparait dès la signature du contrat » (Mouloud CHEMOUN, 2026-10-03).
  3. Discours « gratuit » au rendez-vous : « il m'a été indiqué que le développement de mon site serait gratuit » (Fabien, 2026-09-23). Résultats promis non tenus (« 2 à 3 appels par jour » promis, résumé d'un avis).
- **Mode de vente** : rendez-vous commercial chez le client (« rendez-vous avec leur commercial », un avis). C'est un point juridique clé (A-03).
- **Décisions DGCCRF ou tribunaux visant nommément Local.fr** : aucune trouvée (2 recherches web, 0 résultat nommant Local.fr). Judilibre / Légifrance non interrogés nommément (recherche plein texte non fonctionnelle sans navigateur). À noter comme « non trouvé », pas comme « inexistant ».

### A-03 : cadre juridique de l'argument « contre l'engagement long » (vérifié)
- **Texte officiel** : article L221-3 du Code de la consommation, version en vigueur depuis le 1er juillet 2016 (ordonnance 2016-301), lu sur Légifrance (https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221319/, consulté le 2026-10-13). Il étend les sections 2, 3 et 6 du chapitre (information précontractuelle, formalisme du contrat hors établissement, droit de rétractation) « aux contrats conclus hors établissement entre deux professionnels » si l'objet du contrat n'entre pas dans le champ de l'activité principale du professionnel sollicité et si celui-ci emploie « inférieur ou égal à cinq » salariés.
- **Droit de rétractation** : 14 jours (article L221-18, version du 1er juillet 2016) ; si l'information sur la rétractation n'a pas été fournie, le délai « est prolongé de douze mois » (article L221-20, version du 28 mai 2022). Les deux lus sur Légifrance (https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221365/, consulté le 2026-10-13).
- **S'applique-t-il aux contrats de site web ? Oui, en principe** : Cass. civ. 1re, 12 septembre 2018, n° 17-17.319 (Cometik c/ une architecte) : un contrat de création et licence de site signé hors établissement ; la Cour retient que « la communication commerciale et la publicité via un site Internet n'entraient pas dans le champ » de l'activité principale (commentaire Eurojuris, 2018-09-28, https://www.eurojuris.fr/articles/creation-site-web-professionnel-et-retractation-37762.htm). Critère confirmé par Cass. civ. 1re, 31 août 2022, n° 21-11.455 : seule compte l'inclusion dans les activités habituelles, pas l'utilité du contrat (Centre Inffo, 2026-06-04, https://www.centre-inffo.fr/site-droit-formation/actualites-droit/contrat-entre-professionnels-le-code-de-la-consommation-peut-aussi-proteger-certains-clients-professionnels). Arrêt récent : Cass., 28 mai 2026, n° 25-14.507 : pour un site personnalisé, le délai de rétractation « se situait au jour de la conclusion du contrat » (Le Monde du Droit, 2026-06-04, https://www.lemondedudroit.fr/affaires/295-consommation/104561-creation-de-site-internet-sur-mesure-quelle-qualification-juridique.html). Texte des arrêts non lu sur Légifrance (sources secondaires).
- **Limites importantes** (ce qui affaiblit l'argument) :
  1. Ne joue que pour un contrat **conclu hors établissement** (chez l'artisan, sur un chantier). Un contrat signé à distance (téléphone, signature électronique) n'est pas visé par L221-3.
  2. Ne joue que pour **5 salariés ou moins**. Un artisan à 6 salariés n'est pas protégé.
  3. Ne donne surtout qu'un droit de rétractation de 14 jours (ou prolongé si mal informé) et la nullité pour défaut de formalisme. **Il n'interdit pas un engagement de 60 mois** signé dans les règles. L'appréciation de « l'activité principale » relève des juges du fond (procès long et incertain pour un artisan).
- **Conséquences pour I1** : (a) nos propres contrats, vendus au négoce ou sur chantier, sont aussi des contrats hors établissement : nous devons fournir le formulaire de rétractation et l'information précontractuelle (sections 2 et 3), sinon nullité. Ce n'est pas un problème avec une offre sans engagement, mais c'est une obligation de forme. (b) L'argument marketing honnête est « résiliable chaque mois », pas « vous pouvez sortir de votre contrat Local.fr » : aider un artisan à sortir d'un contrat existant ressemble à du conseil juridique [HYPOTHÈSE : à éviter, renvoyer vers une association de consommateurs ou un avocat]. (c) Démarchage B2B : pas de règle spécifique trouvée en plus de L221-3 ; Bloctel ne protège que les consommateurs [HYPOTHÈSE, non vérifié sur source officielle dans cet audit].

### A-04 : Solocal / PagesJaunes (concurrent direct n°2, en déclin)
- **Ce qu'ils vendent** : trois lignes. Connect (présence en ligne, fiches), Booster (publicité, dont « Référencement Prioritaire » sur PagesJaunes = 64 % de Booster), Sites Internet.
- **Taille et tendance** (communiqué résultats annuels 2025, 17 février 2026, https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2026/02/FCECO080966_20260217.pdf, lu le 2026-10-13) :
  - CA groupe 2025 = 324,5 M€ (-3,0 % sur 2024) ; T4 2025 = 79,0 M€ (-9,1 %). Connect 77,1 M€ (-15 %), Booster 189,1 M€ (+1 %), Sites Internet 58,3 M€ (+2 %, 18 % du CA, « gains de temps de production notamment grâce à l'IA »).
  - **Parc clients : 251 000 début 2024, 227 000 fin 2024, 195 000 fin 2025.** En 2025 : 16 000 acquisitions, **48 000 clients perdus**, churn 21 % stable. Cause citée : « un record de faillites ».
  - ARPA (revenu moyen par client) environ 1 550 €/an fin 2025 (environ 1 420 € fin 2024), soit environ 129 €/mois (calcul).
  - Prises de commande 2025 : 362 M€ (+18 %) ; carnet de commandes 246,3 M€, dont environ 32 % à verser en 2027 et au-delà : signe de contrats pluriannuels.
  - Tendance 2026 (résumé de recherche, rapport semestriel non ouvert) : T1 2026 = 74 M€ (-10,7 %) [à vérifier].
  - Entités juridiques (API, A-01) : SOLOCAL 265,1 M€ de CA 2024 (perte de 18,1 M€) ; SOLOCAL MARKETING SERVICES 64,2 M€ (2025, bénéfice 15,2 M€).
- **Prix public** : non relevé dans cet audit. Prix cités par des clients : « Je règle normalement 180 € par mois. » (Chris, Trustpilot, 2026-09-29 ; même prénom et même date qu'un avis Local.fr, possible confusion de l'outil de lecture, à recouper) ; « Il était prévu que je paie moins de 60€ par mois » (Soon, 2026-09-28).
- **Avis clients** : Trustpilot 4,3/5 sur 12 272 avis, 1 382 sur 12 mois ; **32 % d'avis 1 étoile**, 60 % 5 étoiles (https://fr.trustpilot.com/review/www.solocal.com, consulté le 2026-10-13). Distribution très polarisée.
- **Faiblesses citées par leurs clients** (https://fr.trustpilot.com/review/www.solocal.com?stars=1, consulté le 2026-10-13) :
  1. Tacite reconduction : « ils établissent votre contrat pour 2 ans, avec tacite reconduction. » (Eric Dienot, 2026-09-24).
  2. Rétractation refusée : « Même si vous demandez votre résiliation durant les 14 jours de réflexion il la refuse » (M. Bresson Fabien, 2026-09-30).
  3. Prélèvements après fermeture : « Ils m'ont prélevés alors que mon entreprise était fermé » (Papillon Fermetures, 2026-09-11).
- **Lecture pour I1** : le marché « présence en ligne TPE à l'abonnement » est grand (Solocal + Local.fr = environ 375 M€ de CA, 220 000 clients) mais **il se contracte** chez l'acteur historique (-32 000 clients nets en 2025). Bon signe (48 000 TPE par an sortent de Solocal et cherchent autre chose) et mauvais signe (le besoin perçu baisse, ou il est capté par Google directement / par des outils moins chers).

### A-05 : plateformes de leads (concurrents indirects : l'artisan paie déjà pour des contacts)
**Travaux.com** (SIREN 489170001, CA 2024 = 23,1 M€, bénéfice 1,7 M€, 6 à 9 salariés, A-01)
- Modèle : l'artisan paie pour accéder aux coordonnées d'un particulier ; selon les réponses de l'entreprise, facturation seulement à l'accès, prix affiché avant, certains plans avec engagement annuel.
- Avis : Trustpilot 4,0/5 sur 10 855 avis, 1 223 sur 12 mois, 16 % de 1 étoile (https://fr.trustpilot.com/review/www.travaux.com?stars=1, consulté le 2026-10-13). Les avis positifs viennent surtout des particuliers ; les avis 1 étoile cités ci-dessous viennent d'artisans (rôle déduit du contenu).
- **Prix par contact constatés (avis d'artisans, septembre-octobre 2026)** : 55 € (flouchippe henri, 2026-09-18), 58,80 € (Cleannt, 2026-10-05), 71 € pour un contact téléphonique (Alain ROUSSEL, 2026-09-21), « 89 € pour un simple clic sur un contact » (Manola ML Conception, 2026-09-25), « 50 ou 60€ pour des mises en relation » (WAVELEC, 2026-09-22), « 60€ voir plus » (Guillaume, 2026-10-03), 50 à 200 € selon un autre artisan (STEVEN NGUYEN, 2026-09-15). Abonnements cités : 180 €/mois avec engagement (avis « cliente », 2026-09-22), environ 200 €/mois (Fumeron Nicolas, 2026-10-03).
- Faiblesses citées : contacts vendus à plusieurs artisans et payés même sans chantier (« travaux.com se rémunère sur le dos des artisans », Elie Karame, 2026-09-18) ; faux numéros (« les numéro qui vous donne es bidon », D G, 2026-09-23) ; engagement annuel malgré résiliation (« cliente », 2026-09-22).

**Habitatpresto** (SIREN 483343356, CA 2024 = 4,8 M€, perte de 62 k€, 20 à 49 salariés, A-01)
- Modèle : abonnement mensuel avec un nombre de contacts, engagement minimum de 6 mois (réponses de l'entreprise et avis).
- Avis : Trustpilot 4,4/5 sur 2 012 avis, 426 sur 12 mois (https://fr.trustpilot.com/review/www.habitatpresto.com?stars=1, consulté le 2026-10-13).
- **Prix constatés** : « j ai payé 210 euros en un mois 10 contacts seulement 8 bidons » (Patrick Bernard, artisan, 2026-08-06), soit environ 21 € par contact (calcul) ; 192 €/mois (jardiseb, 2026-07-19) ; 576 € pour un abonnement de 6 mois sans chantier (oualid merghem, 2026-06-09).
- Faiblesses citées : contact envoyé à beaucoup de professionnels (« le même contact a été envoyé à des dizaines », MTS Solaire Service, 2026-08-07) ; engagement de 6 mois difficile à résilier (« l'abonnement de 6 mois MINIMUM validé », Marina RAJCIC, 2026-05-25) ; qualité des leads (« Les leads sont de très mauvaise qualité. », S.T, artisan BTP, 2026-06-08).

**StarOfService** : environ 15 € par réponse à une demande, données anciennes de 2017-2018 (F2-20). Pas de mise à jour dans cet audit.

**Lecture pour I1** : un artisan qui achète des leads dépense **environ 120 à 210 €/mois** (Habitatpresto, Travaux.com), ou **50 à 90 € par contact** chez Travaux.com, pour des contacts partagés. Une offre à 99-149 €/mois qui produit des appels **exclusifs** (fiche Google, avis, site à son nom) est dans le même budget. C'est le meilleur argument de prix d'I1 : se comparer au prix d'un lead, pas au prix d'un site. Limite : Travaux.com est rentable (1,7 M€ de bénéfice) et très noté par les particuliers, donc l'achat de leads continue malgré les plaintes.

