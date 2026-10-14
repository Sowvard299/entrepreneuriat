# Audit C : ménage SAP (I5) et garde d'enfants d'urgence (I14)

Date : 2026-10-13. Auditeur C, phase 4. Règles de preuve de `signaux/_consignes-communes.md`. IDs de preuve : C-xx.

---

## I5. Agence de ménage SAP « remplaçante garantie sous 48 h » (score phase 3 : 7,50)

### 1. Concurrents réels

Source commune des CA : API Recherche d'entreprises, `https://recherche-entreprises.api.gouv.fr/search?q=<nom>` et filtres `activite_principale` + `code_commune` (consultée le 2026-10-13).

**C-01. Densité locale (API).** Entreprises actives en NAF 88.10A (aide à domicile, où se classent la plupart des agences SAP) : 564 dans le 92, 1 177 à Paris ; en 81.21Z (nettoyage courant, mélange B2B et SAP) : 3 559 dans le 92, 9 283 à Paris. Marché très encombré : la question n'est pas « y a-t-il de la place » mais « pourquoi nous plutôt que l'agence O2 à 500 m ».

**C-02. O2 (réseau Oui Care, mode prestataire).**
- Vend : ménage, repassage, garde d'enfants, seniors ; intervenants en CDI, l'agence est employeur.
- Prix : **non publié** sur https://www.o2.fr/tarifs (consulté le 2026-10-13) : « Nos tarifs sont calculés au plus juste en fonction des prestations souhaitées et de la localisation. » Garantie affichée : « satisfait, refait ou remboursé » (qualité), **aucune garantie de remplacement écrite**. Service « sous réserve [...] de disponibilité d'un intervenant ».
- Taille locale (API, CA 2025) : O2 Boulogne-Billancourt (SIREN 500547757) 1 391 572 € ; O2 Issy-les-Moulineaux (479205544) 1 175 305 € ; O2 Neuilly-Levallois (820625382) 1 202 345 € ; O2 Châtillon (511303323) 1 044 534 €. Une agence O2 de ville du 92 fait donc environ 1 à 1,4 M€ avec un résultat de 5 à 10 %.
- Avis : 3 469 avis Trustpilot, 4,2/5, 17 % de 1-2 étoiles (F1-17).
- Faiblesses citées : « 4 MOIS SANS AUCUNE PRESTATION DE MÉNAGE » (Trustpilot, 2026-09-02) ; « Aucune prestation de service depuis 4 mois et demi » (2026-09-21) (F1-17). La pénurie d'intervenants est le reproche n° 1 (environ 10 avis sur 20).

**C-03. Shiva (réseau Acadomia, mode mandataire : le client est employeur).**
- Vend : ménage et repassage. Prix public (https://www.shiva.fr/, consulté le 2026-10-13) : **16 €/h après crédit d'impôt, 32 €/h avant**, « minimum national » ; « à partir de 140 €/mois » pour 2 h/semaine ; **frais de gestion « en moyenne de 25 € » par mois**, dus même sans intervention ; **dépôt de garantie de 100 €** ; « Sans engagement, aucun frais d'annulation ». Promet un « remplacement temporaire de votre intervenant » **sans délai ni conditions écrites**.
- Taille : « 700 agences en France » (la méta-description dit « Plus de 620 agences »), « 200 000 clients actifs », « 3,5 ans d'ancienneté en moyenne ». Tête de groupe SHIVA GROUPE (SIREN 443977871, nom d'usage Acadomia) : CA 2025 63 820 120 €, résultat 1 338 261 € (API).
- Avis : 4,8/5 sur 69 385 avis **hébergés par Shiva** ; mais **Trustpilot : 3,7/5 sur 1 158 avis, 25 % de 1 étoile + 4 % de 2 étoiles** (https://fr.trustpilot.com/review/www.shiva.fr?stars=1&stars=2, consulté le 2026-10-13). Contradiction à garder : la note maison est bien plus flatteuse.
- Faiblesses citées (Trustpilot) : remplacement subi : « un coup je suis remplacé sans être prévenu » (2026-10-09) ; absence : « Personne ne s'est présenté » (2026-10-01) ; frais cachés : « les 100€ de frais de garantie ne l'ont en aucun cas été mentionné » (2026-10-03) ; préavis en mandataire : « Un préavis de 1 mois m'a été appliqué. » (2026-09-29) ; côté salariés : « nous sommes payés que 15 à 16 € de l'heure » (2026-10-06, se présente comme salarié).

**C-04. Helpling France (plateforme, intervenants salariés d'agences partenaires).**
- Prix public (https://www.helpling.fr/, consulté le 2026-10-13) : **28 €/h TTC régulier (14 €/h après crédit d'impôt), 33 €/h ponctuel (16,50 €)**. Avance immédiate « optionnel, gratuit ». « Déjà 80 000 clients satisfaits », « >20 villes ».
- Taille : HELPING FRANCE (SIREN 803290444) CA 2019 872 520 €, perte 354 869 € ; plus de comptes publiés depuis (API). Helpling Pays-Bas en faillite en 2023 (F5-19).
- Aucune politique de remplacement publiée : si personne n'est dispo, Helpling « recontactera » le client pour un autre créneau.
- Faiblesses citées : « Si aucune aide-ménagère ne se présente, vous êtes tout de même prélevé. » (Trustpilot, 2024-02-16, F1-19) ; « Vous n'êtes pas avertis de l'absence de l'intervenant » (2024-10-31, F1-19). Avis négatifs anciens : Helpling ne sollicite plus d'avis (F1-19).

**C-05. Wecasa (plateforme d'indépendants, multi-services).**
- Prix : **non lu sur le site** (wecasa.fr renvoie 403 à la lecture automatique). Un guide tiers indique 28,90 €/h, soit 14,45 € après crédit d'impôt (https://abby.fr/guide/micro-entreprise/tarif-auto-entrepreneur-menage, date inconnue) [à vérifier].
- Taille : WECASA (SIREN 822686788) CA 2024 12 742 185 €, perte 1 850 379 € (API) ; Trustpilot 4,7/5 sur 19 164 avis, 7 % de 1-2 étoiles (F1-19). **Contre-signal fort** : le leader plateforme est très bien noté, la douleur « fiabilité » n'est pas universelle.
- Risque réglementaire : un amendement à l'Assemblée nationale vise la captation du crédit d'impôt par les plateformes (https://www.assemblee-nationale.fr/dyn/17/amendements/1906A/AN/1142.pdf, extrait de recherche seulement, non ouvert).

**C-06. Gros acteurs SAP présents dans le 92 (API, sièges ou établissements à Boulogne, Issy, Levallois, Neuilly, Courbevoie, Rueil)** : Vitalliance (160,7 M€ en 2023, surtout seniors), Onela / Bien à la Maison (57,0 M€ en 2025), Domaliance / A2micile (38,9 M€ en 2024), Ouihelp (23,9 M€ en 2024, **perte de 11,2 M€**), Amelis (14,9 M€ en 2025, perte de 1,9 M€), Domidom (17,4 M€ en 2022, perte de 2,1 M€). Ils visent surtout la dépendance (plus rentable avec l'APA), mais font aussi du ménage. Leçon : même avec des dizaines de millions de CA, plusieurs perdent de l'argent.

**C-07. Petites agences indépendantes du 92 (API)** : Casa Services (Issy/Boulogne, 411 480 € en 2024, **perte de 97 326 €**) ; Vivaservices Levallois / ASSL Services (280 460 € en 2023, résultat 16 538 €) ; Home Privilèges / Les Menus Services (987 137 € en 2024, perte de 16 726 €) ; Tilia (408 483 € en 2025, **perte de 216 599 €**). Taille typique d'une agence indépendante : 0,3 à 1 M€, souvent à perte ou à marge très fine.

**C-08. Domi Ménage (franchise née à Boulogne-Billancourt, prestataire).**
- Prix public (https://www.domi-menage.fr/, consulté le 2026-10-13) : **31,90 €/h, 15,95 €/h avec avance immédiate**, tarif « tout compris », « sans frais cachés ». « Domi Ménage est prestataire de service et non mandataire. » 12 agences, dont **Boulogne-Billancourt et Levallois-Perret**, c'est-à-dire exactement nos villes cibles.
- Remplacement : « nous vous proposons et organisons son remplacement par une autre professionnelle » (sans délai chiffré).
- Avis : 4,9 sur Google (widget Trustindex, nombre non affiché). Tête de réseau DOMI MENAGE DEVELOPPEMENT (SIREN 835115627, Boulogne) : CA 2023 70 417 € (redevances, API). Article franchise : « CA potentiel » de 250 000 € après 2 ans (https://www.toute-la-franchise.com/news-domi-menage-specialiste-menage-repassage-domicile-paris, 2021-05-18).
- Faiblesses clients : non trouvées (pas de page d'avis négatifs lue) [lacune].

**C-09. Centre Services (réseau, agences Paris 14, Clamart, Malakoff).** Fiche Aladom : « En cas d'absence de votre intervenant, nous garantissons son remplacement » (https://www.aladom.fr/annuaire/pro/595444/centreservicesparis14, date inconnue, page © 2026). Prix non publié, aucun avis. **Le mot « garantissons » est déjà employé par un concurrent du sud du 92**, sans délai chiffré.

**C-10. Ménage.fr (réseau historique).** MENAGE.FR PARIS (SIREN 480589290, 93200) CA 2023 351 708 €, résultat -475 € ; Ménage.fr PO (78) 247 818 €, perte 43 836 € ; Ménage.fr Lyon 660 323 €, perte 106 531 € en 2024 (API). Réseau qui stagne et perd de l'argent. « Free Ménage » : aucune entreprise trouvée dans l'API.

**Un concurrent promet-il déjà le remplacement garanti ?** Oui, en mots, pas en délai. Shiva : « remplacement temporaire de votre intervenant » ; Domi Ménage : « nous vous proposons et organisons son remplacement » ; Centre Services : « nous garantissons son remplacement ». O2 et Helpling n'en parlent pas. **Aucune des pages lues n'écrit un délai chiffré (48 h) ni une pénalité si le remplacement n'a pas lieu.** Notre différence se réduit donc à « délai écrit + compensation », ce qui est copiable en une ligne par Domi Ménage ou Shiva si ça marche, et qui ne se prouve qu'au bout de plusieurs mois de service. Les plaintes (O2, Shiva) montrent que la promesse existe déjà chez certains et n'est pas tenue faute d'intervenantes : **le vrai goulot est le recrutement, pas la promesse.**

---

## I14. Garde d'enfants de plus de 3 ans en urgence et en sortie d'école (score phase 3 : 6,85)

### 1. Concurrents réels

(en cours)

---

## Cadre juridique commun (SAP), vérifié sur sources officielles

**C-20. Liste des activités et régimes (Code du travail, art. D7231-1, version en vigueur depuis le 2023-07-17).** Source : Légifrance, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000018500042/ (consulté le 2026-10-13).
- **I. Agrément (art. L7232-1)** : garde d'enfants à domicile « en dessous d'un âge fixé par arrêté » (3 ans) ; accompagnement des jeunes enfants hors du domicile ; et, pour les personnes âgées ou handicapées, assistance aux actes quotidiens, conduite du véhicule, accompagnement.
- **II. Déclaration facultative (art. L7232-1-1)** : point 1 « Entretien de la maison et travaux ménagers » ; point 4 garde d'enfants à domicile « au-dessus d'un âge fixé par arrêté » ; point 15 accompagnement « des enfants de plus de trois ans » hors du domicile.
- Donc : **I5 (ménage) et I14 (garde des plus de 3 ans, sortie d'école) relèvent de la seule déclaration**. Toute garde d'un enfant de moins de 3 ans, même une fois, exige l'agrément (y compris en mandataire).

**C-21. Déclaration, agrément, autorisation (DGE, https://www.servicesalapersonne.gouv.fr/espace-pro/obligations-reglementaires/declaration-agrement-autorisation-dans-quel-cas, mise à jour 2025-12-18).**
- La déclaration se fait sur l'extranet NOVA. Elle est gratuite [HYPOTHÈSE : aucun coût mentionné nulle part]. Sans elle, pas d'avantage : « Les organismes non déclarés (et leurs clients) ne peuvent pas bénéficier des avantages fiscaux et sociaux ».
- Agrément (État, instruit par les DDETS) : « valable cinq ans sur un territoire déterminé » ; délai d'instruction de 3 mois maximum une fois le dossier complet (extrait de recherche servicesalapersonne.gouv.fr, non relu en page) ; cahier des charges avec obligations de continuité de service et de qualification.
- Autorisation (conseil départemental) : uniquement pour l'aide aux personnes âgées ou handicapées en prestataire, par appel à projets depuis 2023, valable 15 ans. Non concerné.
- Devis et factures doivent mentionner le numéro de déclaration.

**C-22. Condition d'activité exclusive (art. R7232-17 et R7232-20 du Code du travail, même page Légifrance).** Le dirigeant s'engage à exercer les SAP « à titre exclusif » ; sinon, comptabilité séparée pour les structures dispensées. Non-respect = perte des avantages fiscaux après un délai de 15 jours d'observations. **Assouplissement depuis le 2025-01-01** (décret n° 2024-851 du 25 juillet 2024) : micro-entrepreneurs et entreprises de moins de 11 salariés exerçant à titre principal des SAP peuvent avoir une activité accessoire, sur demande dans NOVA (FAQ DGE, https://www.servicesalapersonne.gouv.fr/files/sap/files/documents/2025/faq-osp-amenagement-dispense-cae.pdf, extrait de recherche, non ouvert). Conséquence : **la société SAP doit être une structure dédiée** ; I5 et I14 peuvent cohabiter dans la même société (deux activités SAP), mais pas avec du ménage de bureaux (I7) sans la dispense.

**C-23. Récépissé (art. R7232-18).** Pas de délai fixé : le préfet enregistre la déclaration « dès réception du dossier de déclaration complet » ; les exonérations sociales s'appliquent « à compter du premier jour du mois qui suit la publication du récépissé ». [HYPOTHÈSE : 2 à 4 semaines en pratique, aucune source officielle sur le délai réel.]

**C-24. Avance immédiate du crédit d'impôt : la vraie barrière d'entrée en 2026.**
- Pour proposer l'avance immédiate, l'organisme doit être **habilité à l'API Tiers de prestation (prestataire) ou à l'API Tierce déclaration CESU (mandataire)** de l'Urssaf, en général via un logiciel métier partenaire. Après habilitation, chaque client est inscrit, l'administration fiscale vérifie qu'il a une déclaration de revenus N-1 ou N-2, le client active son compte (lien valable 7 jours) ; seules les prestations postérieures à l'activation sont couvertes ; l'Urssaf verse le montant total au prestataire 4 jours ouvrés après validation (extraits de recherche des pages urssaf.fr ; les pages elles-mêmes renvoient ECONNRESET à la lecture automatique). Délai d'habilitation : « quelques semaines » selon une page Urssaf ancienne [non vérifié].
- **Garantie financière obligatoire** (art. D133-22 du Code de la sécurité sociale) : attestation d'une banque ou d'un assureur, **15 000 € minimum** pour moins de 500 000 € déclarés ; date limite **31 octobre 2026**, faute de quoi l'accès à l'avance immédiate est suspendu ; le ministère indique qu'« aucun nouveau report ne sera accordé » (https://www.aladom.fr/actualites/secteur-service/11232/avance-immediate-du-credit-dimpot-la-date-limite-pour-lattestation-de-garantie-repoussee-au-31-octobre-2026/, 2026-07-15, mis à jour 2026-08-04). La Fédésap juge l'obligation « matériellement impossible à satisfaire », les assureurs refusant de couvrir le risque (https://www.fedesap.org/wp-content/uploads/2025/12/CP-Fedesap-%E2%80%93-AiCi-031225.pdf, 2025-12-03, extrait de recherche, non ouvert).
- **Conséquence pour une équipe à moins de 5 000 €** : obtenir une garantie de 15 000 € d'un assureur sans historique est incertain [HYPOTHÈSE : caution bancaire probablement adossée à un dépôt ou à une caution personnelle]. Sans avance immédiate, le client paie 28 à 32 €/h et attend son crédit d'impôt l'année suivante, alors que tous les concurrents (Shiva, Domi Ménage, Helpling) affichent 14 à 16 €/h. **Démarrage commercial réaliste : 2 à 4 mois après la création de la société** [HYPOTHÈSE construite sur C-23 et C-24]. Point à vérifier en priorité : la garantie s'applique-t-elle aussi en mode mandataire (API Tierce déclaration CESU) ? Non tranché par les sources lues.

**C-25. Mandataire ou prestataire.** En mandataire, le particulier est l'employeur légal ; il applique la convention collective des particuliers employeurs (IDCC 3239) et supporte la rupture du contrat (préavis, indemnités) ; l'organisme facture des frais de gestion (Shiva : environ 25 €/mois, C-03). En prestataire, l'organisme est employeur (IDCC 3127) et responsable de la prestation. Les plaintes Shiva sur le préavis imposé (« Un préavis de 1 mois m'a été appliqué », 2026-09-29) illustrent le risque du mandataire : **le client découvre qu'il est employeur**. [La page DGCCRF sur les modes d'intervention renvoie 403 : https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques-et-les-faq/services-la-personne-modes-dintervention-activites, non lue.] **Problème pour la promesse I5** : en mandataire, l'agence ne peut pas « garantir » un remplaçant, puisque le remplaçant serait un second salarié du client, avec un second contrat. La garantie de 48 h n'est crédible qu'en prestataire.

**C-26. Salaires (code.travail.gouv.fr et Légisocial).** SMIC au 2026-06-01 : « le SMIC est fixé à 12,31 € brut de l'heure » (https://www.legisocial.fr/reperes-sociaux/montant-smic-2026-taux-horaire-net-brut.html, mis à jour 2026-10-07). Les minima de la convention IDCC 3127 (avenant n° 11 du 22 janvier 2024, cité par https://code.travail.gouv.fr/contribution/3127-quel-est-le-salaire-minimum, mis à jour 2026-06-01) sont de 11,68 à 12,11 €/h selon des sites tiers, donc **rattrapés par le SMIC : le plancher réel est 12,31 € brut**. Un salarié Shiva dit être payé « 15 à 16 € de l'heure » (C-03, 2026-10-06 ; brut ou net non précisé).

**C-27. Recrutement (BMO 2026, France Travail, via https://travail-industrie.com/emploi/metiers-en-tension/..., open data, consulté le 2026-10-13).**
- Personnels de ménage chez des particuliers : 38 839 projets de recrutement en France, **52 % jugés difficiles** (moyenne 43 %) ; **Île-de-France : 8 318 projets, 34 % difficiles**. Contradiction à garder : en IDF, le ménage est jugé moins difficile à recruter qu'en moyenne nationale.
- Aides à domicile et auxiliaires de vie : environ 69 400 projets, 62 % difficiles, 5e métier le plus recherché (extraits de recherche).
- Gardes d'enfants à domicile et assistants maternels : 23 609 projets, 49 % difficiles ; IDF 5 894 projets, 36 % difficiles.
- Turnover : aucune donnée sourcée trouvée [lacune ; HYPOTHÈSE : élevé, les plaintes « remplacé sans être prévenu » en sont un indice].

---

## Sources non lues

(en cours)
