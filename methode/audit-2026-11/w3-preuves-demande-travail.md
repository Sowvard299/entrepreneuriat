# W3 : preuves de chiffre d'affaires étranger (volet A) et de demande en ligne (volet B), fichier de travail

- Mission : A = sources fiables de CA d'entreprises étrangères (accès, limites) ; B = signaux de demande mesurables en ligne, tests de demande, cadre légal français d'une fausse porte / précommande.
- Date : 2026-11-03
- Recherches web (WebSearch) utilisées : 15 / 15 (budget épuisé)
- Pages ouvertes (WebFetch) : environ 70 appels, dont environ 20 en erreur (403, 404, redirection, rendu JavaScript : liste en fin de fichier)
- Preuves : 49 (W3-1 à W3-49) ; domaines distincts : 32 (codeur.com, comeup.com, sec.gov, cornell.edu, companieshouse.gov.uk, company-information.service.gov.uk, gov.uk, gesetze-im-internet.de, franchiselawsolutions.com, thrivepass.com, statista.com, deloitte.com, opencorporates.com, changelog.com, baremetrics.com, google.com, buffer.com, ppc.land, nber.org, github.com, jobspipe.dev, appfigures.com, appalize.com, repec.org, unbounce.com, strategyzer.com, dhinsights.org, pages.dev, wiley-vch.de, legifrance.gouv.fr, service-public.gouv.fr, cnil.fr). Part maximale d'un domaine : legifrance.gouv.fr, 10 preuves sur 49 (20 %).
- Statut : partiel (voir « Trous à combler »)
- Limite d'outil : un contrôle des citations par `curl` avec un agent utilisateur de navigateur a été refusé par le classificateur de permissions ; les citations viennent donc de WebFetch (demandées « mot pour mot »). Une citation reprise par un résumeur peut contenir une coquille : à re-contrôler par le vérificateur avant usage.
- Convention : « ouverte » = page lue en entier par WebFetch ; « extrait » = vu seulement dans un résultat de recherche. Les dates sont celles affichées par la page ; sinon « date inconnue (consultée 2026-11-03) ».

## Lot 1 (volet A : registres et dépôts officiels)

### W3-1 : SEC EDGAR, API de données financières (sans clé)
- Volet : A (États-Unis, entreprises cotées ou ayant fait une offre enregistrée)
- Source : https://www.sec.gov/search-filings/edgar-application-programming-interfaces (date : 2025-04-08, « Last Reviewed or Updated » ; ouverte)
- Citation : « These APIs do not require any authentication or API keys to access. »
- Ce que ça établit : accès gratuit, sans clé, à des données XBRL structurées (points d'accès `data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, `companyconcept`, `frames`) ; l'ensemble Zip `companyfacts.zip` existe pour le volume. Ces chiffres sont ceux des dépôts (10-K, 10-Q) : ils couvrent seulement les sociétés qui déposent à la SEC.

### W3-2 : SEC EDGAR, règle d'accès équitable
- Volet : A
- Source : https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data (date : 2024-06-26, « Last Reviewed or Updated » ; ouverte)
- Citation : « Current max request rate: 10 requests/second. »
- Ce que ça établit : limite de 10 requêtes par seconde ; la page demande aussi de déclarer un agent utilisateur dans les en-têtes (« Please declare your user agent in request headers. »). Piège : scripts sans identification = risque de blocage.

### W3-3 : SEC EDGAR, recherche plein texte
- Volet : A
- Source : https://www.sec.gov/search-filings (date inconnue, consultée 2026-11-03 ; ouverte) ; interface : https://www.sec.gov/edgar/search/
- Citation : « Find keywords and phrases in more than 20 years of EDGAR filings. »
- Ce que ça établit : on peut chercher une phrase (ex. « subscription revenue », « franchise ») dans 20 ans de dépôts, filtrer par date, société, catégorie. La page ne précise pas l'année de départ ni si les pièces jointes sont incluses : ne pas affirmer « depuis 2001 ».

### W3-4 : Financement participatif américain (Form C) : niveau de contrôle des comptes selon le montant levé
- Volet : A (petites sociétés américaines, dépôts gratuits sur EDGAR)
- Source : https://www.law.cornell.edu/cfr/text/17/227.201 (17 CFR 227.201(t) ; dernière modification citée : 87 FR 57398, 2022-09-20 ; ouverte)
- Citation : « More than $124,000, but not more than $618,000, financial statements of the issuer reviewed »
- Ce que ça établit : jusqu'à 124 000 $ levés, seuls des chiffres fiscaux certifiés par le dirigeant sont exigés (déclaratif) ; de 124 000 à 618 000 $, comptes « examinés » (revue limitée) par un comptable indépendant ; au-dessus de 618 000 $, comptes audités (exception : première offre jusqu'à 1 235 000 $, comptes examinés). Seuils lus sur la page ; un Form C n'est pas une preuve de CA audité pour les petites levées.

### W3-5 : Companies House (Royaume-Uni), produit « Accounts Data » : comptes iXBRL en téléchargement gratuit
- Volet : A (Royaume-Uni)
- Source : https://download.companieshouse.gov.uk/en_accountsdata.html (date : 2026-11-03, « Last Updated: 03/11/2026 » ; ouverte)
- Citation : « Each data file is provided free of charge and is not supported. »
- Ce que ça établit : fichiers quotidiens de comptes déposés en format iXBRL, gratuits ; la page indique « Data is only available for electronically filed accounts » (environ 75 % des 2,2 millions de comptes attendus par an) et chaque fichier quotidien n'est téléchargeable que 60 jours : il faut archiver soi-même. Les comptes déposés par les petites sociétés peuvent être réduits (voir W3-8).

## Lot 2 (volet A : Royaume-Uni et Allemagne, ce qui est publié ou non)

### W3-6 : Companies House, API : clé d'API obligatoire, inscription préalable
- Volet : A (Royaume-Uni)
- Source : https://developer-specs.company-information.service.gov.uk/guides/authorisation (date inconnue, consultée 2026-11-03 ; ouverte) ; et https://developer.company-information.service.gov.uk/get-started (date inconnue ; ouverte)
- Citation : « the Companies House API takes the username as the API key and ignores the password »
- Ce que ça établit : authentification HTTP Basic avec la clé d'API ; la page « get-started » dit « You must register a user account with Companies House to explore and perform tests ». Aucune des deux pages ne dit que l'accès est gratuit : la gratuité (affirmée dans la consigne de mission) reste [non confirmée par page ouverte].

### W3-7 : Companies House, API : limite de débit
- Volet : A
- Source : https://developer-specs.company-information.service.gov.uk/guides/rateLimiting (date inconnue, consultée 2026-11-03 ; ouverte)
- Citation : « You can make up to 600 requests within a five-minute period. »
- Ce que ça établit : 600 requêtes par fenêtre de 5 minutes, puis code 429 jusqu'à la fin de la fenêtre. Suffisant pour consulter quelques centaines de sociétés cibles, pas pour moissonner le registre (pour cela : le fichier en vrac de W3-5). L'API renvoie des informations d'enregistrement « en direct » (« The data returned is live and real-time ») ; la page d'accueil ne dit pas qu'elle renvoie des chiffres financiers : les chiffres sont dans les comptes déposés (PDF ou iXBRL).

### W3-8 : Royaume-Uni, ce que les petites sociétés déposent réellement (CA souvent invisible)
- Volet : A (Royaume-Uni) ; contre-preuve partielle à W3-5
- Source : https://www.gov.uk/annual-accounts/microentities-small-and-dormant-companies (date : non affichée, consultée 2026-11-03 ; ouverte)
- Citation : « You can only send abridged accounts if all your company members agree to it. »
- Ce que ça établit : une petite société peut déposer des comptes abrégés ; une micro-entité envoie « only your balance sheet with less information » (donc pas de compte de résultat, donc pas de CA). Seuils affichés (2 critères sur 3) : petite = CA ≤ 15 M£, bilan ≤ 7,5 M£, ≤ 50 salariés ; micro = CA ≤ 1 M£, bilan ≤ 500 k£, ≤ 10 salariés. Conséquence : une jeune société rentable de moins de 1 M£ de CA n'expose en général pas son CA à Companies House. Pas de mention d'un changement en 2027 sur cette page [à vérifier ailleurs].

### W3-9 : Allemagne, HGB § 326 : les petites sociétés ne publient pas leur compte de résultat
- Volet : A (Allemagne)
- Source : https://www.gesetze-im-internet.de/hgb/__326.html (date : aucune date « Stand » affichée, consultée 2026-11-03 ; ouverte)
- Citation : « Der Anhang braucht die die Gewinn- und Verlustrechnung betreffenden Angaben nicht zu enthalten. »
- Ce que ça établit : pour une petite société de capitaux (§ 326 Abs. 1) seuls bilan et annexe sont à transmettre, annexe sans les données du compte de résultat ; pour une micro-société (§ 326 Abs. 2) : « nur die Bilanz zu übermitteln ». Donc le CA d'une petite GmbH n'est en général pas public en Allemagne.

### W3-10 : Allemagne, HGB § 267 et § 316 : seuils de taille et audit
- Volet : A (Allemagne)
- Source : https://www.gesetze-im-internet.de/hgb/__267.html et https://www.gesetze-im-internet.de/hgb/__316.html (dates : aucune « Stand » affichée, consultées 2026-11-03 ; ouvertes)
- Citation : « 15 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag. » (§ 267 Abs. 1) ; « die nicht kleine im Sinne des § 267 Abs. 1 sind » (§ 316 Abs. 1)
- Ce que ça établit : une société est « petite » si elle reste sous 2 des 3 seuils : 7 500 000 € de total de bilan, 15 000 000 € de CA, 50 salariés en moyenne ; seules les sociétés qui ne sont pas petites doivent être auditées (« sind durch einen Abschlußprüfer zu prüfen »). Donc un CA allemand n'est audité qu'au-dessus de ces seuils ; en dessous, déclaratif et non publié (W3-9). La page § 267 ne mentionne pas de date de modification : ne pas dater les seuils.

## Lot 3 (volet A : franchises, classements, registres commerciaux)

### W3-11 : FDD américain, règle de la FTC : l'Item 19 est facultatif et non audité, l'Item 21 est audité
- Volet : A (franchises américaines)
- Source : https://www.law.cornell.edu/cfr/text/16/436.5 (16 CFR 436.5(s) et (u) ; date de mise à jour non affichée, consultée 2026-11-03 ; ouverte)
- Citation : « the franchisor must have a reasonable basis and written substantiation for the representation »
- Ce que ça établit : l'Item 19 (représentations de performance financière) est permis, non imposé ; à défaut, le franchiseur doit écrire « We do not make any representations about a franchisee's future financial performance ». Le texte exige une « base raisonnable » et une justification écrite (disponible sur demande des candidats), pas un audit. L'Item 21 : « these financial statements must be audited by an independent certified public accountant » (système de démarrage : audit progressif). Donc : CA du franchiseur = audité (Item 21) ; CA des unités franchisées (Item 19) = déclaratif, avec justificatif écrit, à lire avec ses notes (échantillon, période, exclusions).

### W3-12 : Inc. 5000, méthode : revenus fournis par l'entreprise, signés par le dirigeant et un tiers qualifié
- Volet : A (États-Unis, classement de croissance sur 3 ans)
- Source : https://www.thrivepass.com/awards/2025-inc-5000-award (page d'un lauréat qui reprend la méthode d'Inc. ; liste révélée le 2025-11-08 ; ouverte). La page de méthode d'Inc. (inc.com/inc-5000-methodology-how-we-selected-these-companies.html) renvoie 403 à WebFetch : non lue.
- Citation : « which must be signed by the CEO and a credentialed third party. »
- Ce que ça établit : conditions reprises : société privée, à but lucratif, basée aux États-Unis, indépendante ; au moins 100 000 $ de CA en 2021 et 2 M$ en 2024 ; classement au pourcentage de croissance sur 3 ans. Vérification = états financiers (ou déclarations fiscales) signés par le dirigeant et un tiers qualifié : contrôle documentaire, pas audit. Le classement donne le taux de croissance et le CA final, pas la marge. Source de seconde main (page d'entreprise lauréate) : confiance moyenne. Extrait de recherche complémentaire (non ouvert) : Inc. « reserves the right to decline applicants for subjective reasons » et fait des vérifications d'antécédents.

### W3-13 : FT 1000 (Europe), méthode Statista : formulaire de confirmation signé, pas d'audit
- Volet : A (Europe, classement de croissance 2022 à 2025)
- Source : https://rankings.statista.com/en/fastest-growing-companies/rankings/fastest-growing-companies-europe/participation/ (édition à publier en mars 2027, vérification ouverte du 2026-09-01 au 2026-11-30 ; ouverte)
- Citation : « a signed confirmation form by the managing director/CEO, finance director/CFO »
- Ce que ça établit : CA 2022 ≥ 100 000 € et CA 2025 ≥ 1,5 M€ ; croissance « primarily organic » ; indépendance ; la preuve demandée est un formulaire signé par un dirigeant ou le directeur financier : auto-certification encadrée, sans pièce comptable exigée sur cette page. Deux autres éditions confirment l'étape de vérification mais pas son contenu (extrait de recherche).

### W3-14 : Deloitte Technology Fast 500 : croissance seulement, « public company databases »
- Volet : A (États-Unis et Canada, technologie)
- Source : https://www.deloitte.com/us/en/industries/tmt/articles/fast500-apply.html (édition 2026 ; candidatures closes le 2026-07-01 ; ouverte)
- Citation : « researched by Deloitte LLP using public company databases »
- Ce que ça établit : formule de croissance sur 3 exercices (FY2022 → FY2025), seuil de 50 % ; CA minimal de 50 000 $ au départ et 5 M$ à l'arrivée. La page ne décrit pas de pièce justificative. Extrait de recherche (non ouvert, document de 2025) : « nominees must submit revenue amounts with supporting documentation » et le CA n'est pas publié : le classement donne un rang et un taux, pas le CA. Les cabinets de conseil, services professionnels et revendeurs sont exclus (extrait).

### W3-15 : OpenCorporates, API : payante, données d'enregistrement, accès gratuit réservé à l'intérêt public
- Volet : A (mondial)
- Source : https://opencorporates.com/pricing/ (© 2024 ; liens d'achat portant « 2022 » ; ouverte)
- Citation : « providing free at-scale access to our data »
- Ce que ça établit : pas d'offre gratuite en libre-service ; formules API de 2 250 £/an (500 appels/mois) à 12 000 £/an (5 000 appels/mois), Enterprise sur devis ; accès gratuit en volume pour journalistes d'investigation, ONG, universités, groupes anticorruption (formulaire). La page ne cite ni comptes annuels ni chiffre d'affaires : OpenCorporates sert à prouver l'existence, l'âge, la forme et les dirigeants d'une société, pas son CA (absence de mention, pas une preuve d'absence). Un extrait de recherche donne un autre prix d'entrée (6 600 £) : les chiffres de cette page priment, à reconfirmer.

## Lot 4 (volet A : franchises, revenus vérifiés par Stripe ; volet B : Google Trends, Keyword Planner)

### W3-16 : Bases publiques d'États américains pour lire les FDD (Californie, Wisconsin, Minnesota)
- Volet : A (franchises américaines)
- Source : https://www.franchiselawsolutions.com/learn/franchise-your-business/how-to-find-free-fdds (cabinet d'avocats, © 2026, pas de date d'article ; ouverte). Les sites officiels (apps.dfi.wi.gov, cards.web.commerce.state.mn.us, dfpi.ca.gov) renvoient 403 à WebFetch : non lus.
- Citation : « publicly available documents that are available for free download »
- Ce que ça établit : trois bases gratuites, d'après le cabinet : Californie (docqnet.dfpi.ca.gov, décrite comme la fonction de recherche du « Department of Business Oversight », ancien nom du DFPI), Wisconsin (apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx), Minnesota (cards.web.commerce.state.mn.us, choisir « Franchise Registrations »). Limite : un FDD n'apparaît que si le franchiseur est enregistré dans l'État (« the franchisor has not filed or registered its FDD with the particular state »). Extrait de recherche (non ouvert) : la Californie aurait remplacé DOCQNET par FRANSES en 2025 ; notre tentative sur docqnet.dfpi.ca.gov/search/ a bien redirigé vers une autre adresse du DFPI. Les URL de ce lot sont à re-tester par le vérificateur depuis un navigateur.

### W3-17 : Revenus « vérifiés par Stripe » sur Indie Hackers : l'échantillon vérifié est majoritairement à zéro (contre-preuve au récit « tout le monde gagne »)
- Volet : A (micro-entreprises logicielles, mondial)
- Source : https://changelog.com/news/9llJ (lien d'actualité daté 2022-07-19 qui cite l'analyse d'Indie Hackers ; ouverte). Les pages d'Indie Hackers renvoient 403 : non lues.
- Citation : « more than 54% of the products are not making any revenue at all »
- Ce que ça établit : l'analyse ne porte que sur « the 937 products that have their revenue verified by Stripe » ; plus de la moitié ne gagnent rien. Extrait de recherche (non ouvert, paraphrase d'un résumé, pas une citation) : la vérification ne fonctionne que pour les utilisateurs de Stripe (donc sous-estimation), les fondateurs choisissent d'afficher ou non, et des produits liés au même compte Stripe affichent des chiffres identiques. Verdict : « Stripe-vérifié » prouve des encaissements bruts passés par ce compte, pas un bénéfice, ni l'absence de ventes hors Stripe, ni qu'un succès moyen existe.

### W3-18 : Baremetrics Open Startups : revenus lus directement chez le processeur de paiement, mais instantané de 2015
- Volet : A
- Source : https://baremetrics.com/blog/open-startups (article du 2015-04-22, mention « Last updated on April 28, 2026 » ; ouverte)
- Citation : « Today, seven startups are part of this initiative. »
- Ce que ça établit : le mécanisme (« Baremetrics pulls directly from payment processors like Stripe, Braintree, and Recurly ») est de la donnée plateforme, non déclarative ; mais la page est un article de 2015 avec 7 participants ; la page d'accueil du programme (baremetrics.com/open-startups, ouverte) n'indique ni vérification ni fermeture. Je ne peux pas dire que le programme est actif en 2026 : ne pas le compter comme source vivante. Même mécanisme que TrustMRR (hors périmètre ici, déjà couvert).

### W3-19 : Google Trends : valeurs relatives, échantillon, termes rares à zéro
- Volet : B
- Source : https://support.google.com/trends/answer/4365533 (« FAQ about Google Trends data », © 2026, pas de date ; ouverte)
- Citation : « The resulting numbers are then scaled on a range of 0 to 100. »
- Ce que ça établit : indice 0 à 100 relatif à la zone et à la période ; la page dit aussi « Trends only shows data for popular terms » et que les termes à faible volume apparaissent à « 0 ». Il n'y a pas de volume absolu de requêtes. Bon pour comparer deux termes entre eux ou une saisonnalité, mauvais pour estimer un nombre de clients.

### W3-20 : Google Keyword Planner : compte Google Ads et facturation exigés
- Volet : B
- Source : https://support.google.com/google-ads/answer/7337243 (« Use Keyword Planner - Google Ads Help », © 2026, pas de date ; ouverte)
- Citation : « You must complete your account setup by entering your billing information »
- Ce que ça établit : accès par un compte Google Ads dont la configuration (carte de paiement) est finie ; la page liste idées de mots-clés, estimations mensuelles de recherches et de coûts, et dit que les mots-clés à très faible volume ne sont pas proposés. La page ne dit ni que l'outil est gratuit, ni qu'il faut avoir des campagnes actives, ni que le volume est affiché en tranches pour les petits comptes : ces trois points restent [non confirmés par page ouverte] (le recoupement n'a pas pu être fait, budget de recherche épuisé).

## Lot 5 (volet A : audit des comptes SEC ; volet B : bibliothèques de publicités et durée de diffusion)

### W3-21 : SEC, les états de résultat (donc le CA) des sociétés qui déposent un 10-K sont audités
- Volet : A (États-Unis)
- Source : https://www.law.cornell.edu/cfr/text/17/210.3-02 (17 CFR 210.3-02, règle S-X 3-02 ; date de mise à jour non affichée ; ouverte) et https://www.law.cornell.edu/cfr/text/17/210.8-02 (règle 8-02, petites sociétés cotées ; ouverte). La page investor.gov (« Form 10-K ») renvoie 403 : non lue.
- Citation : « audited statements of comprehensive income and cash flows for each of the three fiscal years » (règle 3-02) ; « Smaller reporting companies must file an audited balance sheet » (règle 8-02)
- Ce que ça établit : pour une société qui dépose à la SEC, le compte de résultat est audité sur trois exercices (deux pour une « emerging growth company » à son introduction). La règle 8-02 impose aux « smaller reporting companies » un bilan audité sur deux exercices (lecture résumée par l'outil : les états de résultat sont aussi couverts). Limite : seules les sociétés tenues de déposer (cotées, ou ayant fait une offre enregistrée) sont concernées ; les startups privées financées par investisseurs ne déposent rien.

### W3-22 : Meta Ad Library : pubs commerciales actives seulement, date de début visible, pas de dépenses
- Volet : B
- Source : https://buffer.com/resources/meta-ad-library/ (blog d'un éditeur d'outils, publié le 2024-10-30 ; ouverte). La page officielle transparency.meta.com/researchtools/ad-library-tools n'affiche que son titre (rendu JavaScript) : non lue.
- Citation : « only shows the ads that are currently running »
- Ce que ça établit : pour un annonceur commercial, le statut « actif », la date de début, les plateformes et la création sont visibles ; une estimation de dépense et de portée n'existe que pour les pubs politiques, électorales ou sociales. Dans l'UE s'ajoutent lieu, âge et sexe ciblés, portée totale, bénéficiaire et payeur, et « inactive ads in the EU also stay in the Facebook ad library for one year ». Donc la durée de diffusion est calculable pour les pubs actives (date de début → aujourd'hui), mais ni les dépenses ni les ventes ne le sont. Source secondaire : confiance moyenne ; un extrait de recherche (non ouvert) parle de 7 ans de conservation pour les pubs politiques.

### W3-23 : Google Ads Transparency Center : annonceur, pubs servies, données supplémentaires selon le pays
- Volet : B
- Source : https://support.google.com/adspolicy/answer/13733850 (« Ads transparency - France - Advertising Policies Help », © 2026, sans date ; ouverte)
- Citation : « a searchable repository of advertisers and the ads they've served »
- Ce que ça établit : nom de l'annonceur, localisation et payeur ; filtre par date et lieu ciblé ; pour certains pays : ciblage, « Total number of recipients for each ad » et libellé du sujet. La page ne donne aucune durée de conservation, aucun montant dépensé, aucune date de première diffusion.

### W3-24 : Durée de conservation des pubs dans le Google Ads Transparency Center : sources contradictoires
- Volet : B (contre-preuve de fiabilité de la source)
- Source : https://ppc.land/a-deep-dive-into-the-google-ads-transparency-center/ (blog spécialisé, 2024-04-01 ; ouverte)
- Citation : « Data on political ads goes back up to seven years. »
- Ce que ça établit : selon cet article, les pubs non politiques sont suivies 365 jours. Des extraits de recherche (non ouverts) avancent plutôt 30 jours, avec une date de première diffusion visible seulement dans l'Espace économique européen (loi sur les services numériques). La page officielle (W3-23) ne tranche pas : toute analyse de durée doit s'appuyer sur des captures datées faites par soi-même, pas sur une durée « affichée ».

### W3-25 : Étude d'eBay : une pub qui tourne n'est pas une pub qui rapporte (contre-preuve à l'heuristique « durée = rentabilité »)
- Volet : B
- Source : https://www.nber.org/papers/w20171 (Blake, Nosko, Tadelis, NBER Working Paper 20171, mai 2014 ; publié dans Econometrica 83, 155-174, 2015 ; ouverte)
- Citation : « we show that returns from paid search are a fraction of conventional non-experimental estimates »
- Ce que ça établit : à partir d'expériences de terrain à grande échelle chez eBay (« a series of large scale field experiments »), le rendement de la publicité par moteur de recherche est une fraction des estimations non expérimentales, et « brand-keyword ads have no measurable short-term benefits ». Conséquence : même un annonceur sophistiqué peut diffuser longtemps des pubs sans gain mesurable ; la durée de diffusion n'est qu'un indice faible que l'annonceur n'a pas coupé la campagne. Je n'ai trouvé aucune étude qui valide l'heuristique « durée longue = rentable » : [HYPOTHÈSE d'absence], aucune recherche dédiée faite (budget épuisé). Lewis et Rao (QJE 2015) non lue (SSRN 403).

## Lot 6 (volet B : offres d'emploi, applications, vitesse des avis)

### W3-26 : Indeed Hiring Lab : indices d'offres d'emploi en accès libre, France incluse
- Volet : B
- Source : https://github.com/hiring-lab/job_postings_tracker (pas de date de mise à jour affichée, © 2026 GitHub ; ouverte)
- Citation : « The frequency of the data is daily and it is refreshed each week. »
- Ce que ça établit : données sous licence CC BY 4.0, dossier France (FR), fichiers par secteur (« Occupational sector label ») et région française ; indice = variation en % des offres désaisonnalisées depuis le 2020-02-01 (moyenne mobile sur 7 jours). Source : offres d'Indeed uniquement. Signal de tendance de l'embauche d'un secteur, pas de chiffre d'affaires ni de prix.

### W3-27 : API Offres d'emploi de France Travail : compte gratuit, limites annoncées par un blog tiers
- Volet : B
- Source : https://jobspipe.dev/blog/france-travail-api (blog d'un vendeur de données concurrent, publié le 2026-09-01, modifié le 2026-09-26 ; ouverte). La documentation officielle (francetravail.io/data/api/offres-emploi) ne s'affiche pas à WebFetch (rendu JavaScript) : non lue.
- Citation : « Access starts with a free account on francetravail.io »
- Ce que ça établit (à confirmer sur la doc officielle) : identifiant et secret client (OAuth2, « client credentials »), point d'entrée `https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search`, paramètres `motsCles`, `codeROME`, `departement`, `range` ; selon le blog : au plus 150 résultats par page et 1 150 offres par requête, « the published rate limit is 10 calls per second ». Usage : compter les offres actives mentionnant un métier ou un mot-clé, découpé par département ou par code ROME, à date fixe. Une offre d'emploi est une dépense en préparation, pas un revenu.

### W3-28 : Appfigures : formule gratuite « Starter »
- Volet : B
- Source : https://appfigures.com/products/app-intelligence (page commerciale, sans date ; ouverte)
- Citation : « Try Appfigures with our free Starter plan and track up to 5 apps. »
- Ce que ça établit : suivi de 5 applications gratuit, sans autre détail sur la page ; la page promet des estimations quotidiennes de téléchargements et de revenus « with country-level accuracy » sans donner ni méthode ni taux d'erreur. La page de tarifs (www.appfigures.com/pricing) renvoie 403 : non lue. Sensor Tower : pas de formule gratuite d'après des fiches de comparateurs (Capterra, TrustRadius ; extrait de recherche, non ouvert) : [à confirmer sur sensortower.com].

### W3-29 : Estimations de téléchargements et de revenus d'applications : modèles, erreur annoncée de ±30 à 50 % par un concurrent
- Volet : B
- Source : https://www.appalize.com/blog/mobile-trends/app-download-and-revenue-estimation-tools-methods-and-accuracy (blog d'un vendeur concurrent, publié le 2026-03-18, « Updated Nov 3, 2026 » ; ouverte)
- Citation : « No estimation tool has access to actual download or revenue data from Apple or Google. »
- Ce que ça établit : les outils de tiers estiment à partir de panels d'utilisateurs, du rang dans les classements et de modèles ; le blog écrit que le CA estimé « can vary ±30-50% for individual apps » et que les outils ne sont pas comparables entre eux. Le blog ne dit pas comment ces plages ont été obtenues : confiance faible, aucun test indépendant trouvé. Usage prudent : classer des applications entre elles (ordre de grandeur), pas chiffrer un marché.

### W3-30 : Avis en ligne et ventes : la note pèse sur les ventes relatives, le nombre d'avis n'est pas calibré en ventes
- Volet : B
- Source : https://econpapers.repec.org/RePEc:nbr:nberwo:10148 (Chevalier et Mayzlin, NBER WP 10148, décembre 2003 ; publié au Journal of Marketing Research, août 2006 ; ouverte)
- Citation : « an improvement in a book's reviews leads to an increase in relative sales »
- Ce que ça établit : sur des livres, comparés entre Amazon.com et BarnesandNoble.com, une meilleure note des avis augmente les ventes relatives, et « the impact of 1-star reviews is greater than the impact of 5-star reviews ». L'étude porte sur l'effet de la note sur les ventes (via le rang), pas sur le comptage d'avis comme mesure des ventes : elle ne prouve pas qu'un nombre d'avis par mois égale un nombre de ventes. Aucune page ouverte ne donne un ratio « avis par vente » : [HYPOTHÈSE] à calibrer sur un produit dont on connaît les ventes.

## Lot 7 (volet B : repères de conversion et échelle de force des preuves)

### W3-31 : Unbounce, rapport 2024 : échelle de l'échantillon et médiane tous secteurs
- Volet : B
- Source : https://unbounce.com/conversion-benchmark-report/ (édition 2024, sans date de publication, © 2009-2026 ; ouverte)
- Citation : « The median conversion rate across all industries is 6.6%. »
- Ce que ça établit : « in the past year alone », 41 000+ pages de destination, 464 M+ visiteurs uniques, 57 M+ conversions ; neuf secteurs (dont SaaS, e-commerce, services financiers, juridique) avec des médianes de 3,8 % à 12,3 % d'après le texte (les valeurs par secteur sont dans des graphiques non lisibles). Limite écrite par Unbounce : « our data only looked at conversion events—not the value per conversion event » : une « conversion » est n'importe quel événement (formulaire, clic), pas un paiement. La page ne dit pas expressément que seuls les clients d'Unbounce sont mesurés (c'est sous-entendu : [HYPOTHÈSE]).

### W3-32 : Unbounce, méthode : les pages sans conversion sont exclues (biais vers le haut)
- Volet : B (contre-preuve : le repère est biaisé)
- Source : https://unbounce.com/conversion-benchmark-report/methodology/ (période 2023-07-23 au 2024-07-23 ; ouverte, relue deux fois)
- Citation : « Pages with fewer than 50 visitors or no conversions were excluded. »
- Ce que ça établit : un taux médian calculé sans les pages à zéro conversion est un taux de pages qui ont converti au moins une fois : trop optimiste pour juger une fausse porte. Aussi : « Industries were identified by using machine learning to sort pages into topics » (secteur attribué par modèle), secteurs ou sous-catégories de moins de 400 pages exclus, sous-catégories « political campaigns, religious topics, terms and conditions » exclues, moyennes et médianes mélangées selon les benchmarks, aucune formule du taux de conversion sur la page. Utiliser ces médianes comme ordre de grandeur de clic ou d'inscription, jamais comme seuil de succès d'une précommande.

### W3-33 : Strategyzer, Test Card : écrire le seuil de réussite avant le test
- Volet : B
- Source : https://www.strategyzer.com/blog/posts/2015/3/5/validate-your-ideas-with-the-test-card (Alex Osterwalder, 2015-03-05 ; ouverte)
- Citation : « How does success look like? What's the threshold? »
- Ce que ça établit : la fiche de test demande l'hypothèse, la mesure (« What are you going to measure to (in)validate your hypothesis? ») et le critère de réussite avant l'expérience. Cela fonde la règle « seuil écrit avant » de la porte 2. La page ne traite pas de la distinction « dire / faire » ni d'une échelle de force.

### W3-34 : Bland, « Say-Do gap » : ce que les gens disent n'est pas ce qu'ils font
- Volet : B
- Source : https://dhinsights.org/blog/risk-in-innovation (article de « Digital Health Insights », 2023-06-26, résumé de seconde main ; ouverte)
- Citation : « represents the discrepancy between what people claim they will do and what they actually do »
- Ce que ça établit : le cadre de Bland dans Testing Business Ideas sépare ce que les gens déclarent de ce qu'ils font, et préconise une suite de tests qui augmentent la preuve de désirabilité (« a sequence of tests that incrementally increase the evidence »). Source secondaire : le texte du livre n'a pas pu être lu.

### W3-35 : Testing Business Ideas : chaque expérience est cotée en « force de preuve » (échelle exacte non lue)
- Volet : B
- Source : https://business-idea-factory.pages.dev/resources/testing-business-ideas (résumé tiers, sans date ; ouverte) ; éditeur : https://www.wiley-vch.de/en/areas-interest/finance-economics-law/testing-business-ideas-978-1-119-55144-7 (« 1. Edition November 2019 », auteurs David J. Bland et Alex Osterwalder ; ouverte)
- Citation : « the relative strength of evidence it generates »
- Ce que ça établit : chaque fiche d'expérience de la bibliothèque (« over 40 distinct experiment types » selon le résumé) indique son coût, sa durée et la force relative de la preuve produite. Les niveaux exacts de l'échelle n'ont pas pu être lus : l'extrait gratuit du livre (e-bookshelf) est un PDF binaire illisible pour WebFetch, et la page éditeur n'en parle pas. Le classement général « faire > dire » vient donc de W3-34 (secondaire) ; l'échelle précise est [HYPOTHÈSE à confirmer dans le livre, chapitre « Experiment Library »].

## Lot 8 (volet B : droit français d'une fausse porte, pratiques commerciales trompeuses)

### W3-36 : Code de la consommation, L. 121-2 : tromper sur « l'existence, la disponibilité » du bien
- Volet : B (droit français)
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563114 (en vigueur depuis le 2022-05-28, version affichée au 2026-11-03 ; ouverte)
- Citation : « L'existence, la disponibilité ou la nature du bien ou du service ; » (2°, a) ; phrase d'ouverture : « Une pratique commerciale est trompeuse si elle est commise dans l'une des circonstances suivantes »
- Ce que ça établit : une page de vente qui laisse croire qu'un produit existe ou est disponible alors qu'il ne l'est pas relève du 2° a) si l'indication est fausse ou de nature à induire en erreur. Une fausse porte qui affiche « Acheter » ou « Disponible » sans le dire est donc exposée.

### W3-37 : Code de la consommation, L. 121-3 : l'omission d'une information substantielle
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563111 (en vigueur depuis le 2022-05-28 ; ouverte)
- Citation : « elle omet, dissimule ou fournit de façon inintelligible, ambiguë ou à contretemps une information substantielle »
- Ce que ça établit : ne pas écrire que le produit n'existe pas encore (ou qu'il s'agit d'une précommande avec livraison future) peut constituer une omission trompeuse. Remède pratique : écrire « bientôt disponible », « liste d'attente » ou « précommande, livraison prévue le ... » avant toute action de l'utilisateur.

### W3-38 : Code de la consommation, L. 121-4, 5° : prix affiché sans pouvoir fournir
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563107 (en vigueur depuis le 2022-05-28 ; ouverte) ; titre de la liste confirmé par la page de section https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220953/ (ouverte)
- Citation : « De proposer l'achat de produits ou la fourniture de services à un prix indiqué »
- Ce que ça établit : le point 5° (début de phrase lu ; la suite n'est pas reproduite par la page, la page de section la décrit comme l'absence de raisons plausibles signalées de ne pas pouvoir fournir au prix indiqué) est rangé parmi les pratiques « réputées trompeuses » : un prix affiché pour un produit que l'on n'est pas en mesure de livrer est le cas à éviter. La page de section dit que L. 121-4 en liste 28.

### W3-39 : Code de la consommation, L. 121-5 : s'applique aussi aux professionnels
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034072564 (en vigueur depuis le 2017-02-23 ; ouverte)
- Citation : « sont également applicables aux pratiques qui visent les professionnels et les non-professionnels »
- Ce que ça établit : les règles L. 121-2 à L. 121-4 valent aussi pour une fausse porte adressée à des entreprises (B2B), pas seulement aux particuliers.

### W3-40 : Code de la consommation, L. 132-2 : sanctions
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049532070 (en vigueur depuis le 2024-05-12 ; ouverte)
- Citation : « sont punies d'un emprisonnement de deux ans et d'une amende de 300 000 euros »
- Ce que ça établit : la pratique commerciale trompeuse est un délit : 2 ans d'emprisonnement et 300 000 € d'amende, montant pouvant être porté à « 10 % du chiffre d'affaires moyen annuel » ou à « 50 % des dépenses engagées pour la réalisation de la publicité ». Aucune de ces pages ne dit que la jurisprudence a déjà visé un test de demande : [non cherché, budget épuisé].

## Lot 9 (volet B : droit français d'une précommande, vente à distance)

### W3-41 : Code de la consommation, L. 221-5 : informer avant la commande, dont la date de livraison
- Volet : B (droit français)
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053310511 (version « en vigueur depuis le 2026-06-19 », modifiée par l'ordonnance n° 2026-2 du 5 janvier 2026, art. 2, selon la page ; ouverte)
- Citation : « La date à laquelle ou le délai dans lequel le professionnel s'engage à livrer » (I, 3°)
- Ce que ça établit : avant la conclusion d'un contrat de vente ou de services à distance avec un consommateur, le professionnel doit donner, lisiblement, la date ou le délai de livraison (I, 3°) et, quand il existe, les conditions, le délai et les modalités du droit de rétractation (I, 7°). Une précommande sans date de livraison ne respecte pas ce texte. La page note que les contrats en cours au 2026-06-19 restent sous l'ancienne rédaction.

### W3-42 : Code de la consommation, L. 221-14 : le bouton de commande
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226854 (en vigueur depuis le 2016-07-01, créé par l'ordonnance n° 2016-301 ; ouverte)
- Citation : « commande avec obligation de paiement » (libellé du bouton, relevé identique dans deux lectures de la page)
- Ce que ça établit : le professionnel veille à ce que le consommateur reconnaisse explicitement son obligation de paiement quand il commande (paraphrase de l'outil : le texte intégral n'a pas été reproduit mot à mot) et le bouton de validation porte la mention « commande avec obligation de paiement » ou une formule analogue. La conséquence d'un manquement n'est pas indiquée dans la version lue. Si la précommande demande une carte, ce libellé est exigé ; si la page ne prend aucun paiement (liste d'attente), il ne s'applique pas. Citation du texte intégral à faire reprendre par le vérificateur.

### W3-43 : Code de la consommation, L. 221-18 : 14 jours de rétractation
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842 (en vigueur depuis le 2016-07-01 ; ouverte) ; confirmation par https://entreprendre.service-public.gouv.fr/actualites/A18652?lang=en (« Publié le 13 novembre 2025 » ; ouverte)
- Citation : « Le consommateur dispose d'un délai de quatorze jours pour exercer son droit de rétractation »
- Ce que ça établit : un acheteur particulier peut renoncer dans les 14 jours sans motif (frais limités à ceux des articles L. 221-23 à L. 221-25). Pour une précommande, la somme encaissée est remboursable pendant ce délai : à budgéter, à ne pas compter comme CA acquis. L'article L. 221-28 (exceptions au droit de rétractation) n'a pas été lu.

### W3-44 : Code de la consommation, L. 216-1 : livraison à la date annoncée, sinon 30 jours
- Volet : B
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044142498 (en vigueur depuis le 2021-10-01 ; ouverte)
- Citation : « au plus tard trente jours après la conclusion du contrat »
- Ce que ça établit : le professionnel livre « à la date ou dans le délai indiqué au consommateur » ; à défaut d'indication, au plus tard 30 jours après la conclusion du contrat. Une précommande dont la livraison dépasse 30 jours exige donc une date ou un délai écrit. L. 216-2 (résolution en cas de retard) vue seulement en extrait de recherche : à lire avant de promettre une date.

### W3-45 : Code de la consommation, L. 221-3 : les règles de vente à distance ne s'étendent aux professionnels que hors établissement
- Volet : B (contre-preuve partielle : le droit de rétractation consommateur ne couvre pas la précommande B2B en ligne)
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882 (en vigueur depuis le 2016-07-01 ; ouverte)
- Citation : « sont étendues aux contrats conclus hors établissement entre deux professionnels »
- Ce que ça établit : l'extension aux professionnels vise les contrats « hors établissement » (démarchage), à condition que l'objet sorte de leur activité principale et que le sollicité ait au plus cinq salariés. Une précommande en ligne entre deux entreprises relève donc du droit commun des contrats, sauf qualification « hors établissement » : [HYPOTHÈSE à faire confirmer par l'auditeur, article cité mais jurisprudence non lue]. En revanche L. 121-2 à L. 121-4 s'appliquent bien au B2B (W3-39).

## Lot 10 (volet B : e-mails collectés, RGPD et prospection)

### W3-46 : CNIL, prospection par e-mail : consentement préalable pour les particuliers, intérêt légitime pour les professionnels
- Volet : B (droit français et européen)
- Source : https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique (page CNIL affichant « 10 juin 2026 », non libellée « mise à jour » ; ouverte)
- Citation : « les personnes aient donné leur consentement avant d'être démarchées » ; « lorsque l'objet de la sollicitation est en rapport avec la profession de la personne démarchée »
- Ce que ça établit : particuliers = e-mail, SMS et appel automatisé exigent un consentement préalable ; professionnels = possible sans consentement préalable si l'objet de la sollicitation est en rapport avec leur profession, avec information et « Opposition simple et gratuite ». Références citées par la page : article L. 34-5 du code des postes et des communications électroniques, RGPD articles 4.11 (consentement), 6 (bases légales), 7 (conditions du consentement), 21 (droit d'opposition). Une liste d'attente (l'internaute laisse son e-mail pour être prévenu) repose sur son consentement : texte clair, case non précochée, preuve conservée [lecture de l'exigence de l'article 7, non citée mot à mot par la page].

### W3-47 : RGPD, article 13 : ce qu'il faut dire à la personne quand on collecte son e-mail
- Volet : B
- Source : https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3 (texte du RGPD publié par la CNIL, « CHAPITRE III - Droits de la personne concernée » ; date non affichée ; ouverte)
- Citation : « les finalités du traitement auquel sont destinées les données »
- Ce que ça établit : à la collecte, la personne doit connaître « l'identité et les coordonnées du responsable du traitement » (art. 13 §1 a), les finalités (§1 c), « la durée de conservation des données à caractère personnel » (§2 a) et ses droits (§2 b). Pour un test de demande : mentionner qui collecte, pourquoi (« vous prévenir du lancement »), combien de temps, et offrir l'effacement. Le registre CNIL des durées de conservation des prospects n'a pas été lu.

## Lot 11 (volet B : places de marché françaises de freelances)

### W3-48 : Codeur.com, liste de projets : budget en tranches et nombre d'offres reçues
- Volet : B (France, services aux entreprises)
- Source : https://www.codeur.com/projects (instantané sans date absolue, consulté 2026-11-03 ; ouverte)
- Citation : « 1 000 € à 10 000 € » (tranche de budget de « Application mobile (ios/android) » avec « 74 Offres »)
- Ce que ça établit : chaque projet affiche un titre, un statut (« Ouvert », « En cours »), une tranche de budget (« Moins de 500 € », « 1 000 € à 10 000 € », « 10 000 € et plus »), le nombre d'« Offres » reçues et de « Vues ». C'est une recherche active d'une solution (un acheteur a publié un besoin), avec un prix en tranche déclaré par l'acheteur, pas un montant payé. Les offres mesurent la concurrence entre prestataires, pas le paiement. La page n'explique pas comment les budgets ni les offres sont comptés, et n'affiche que des dates relatives (« Il y a 1 heure »).

### W3-49 : ComeUp, page d'accueil : note et nombre d'avis par service, ventes par vendeur
- Volet : B (France, micro-services)
- Source : https://comeup.com/ (© 2026, sans date de publication ; ouverte)
- Citation : « 1 342 839 commandes effectuées » (chiffre global affiché par le site, sans date)
- Ce que ça établit : chaque fiche de service montre une note et un nombre d'avis entre parenthèses (exemples lus : « 5,0 (16) » et « 4,8 (66) »), un prix « À partir de » et parfois un budget moyen ; le nombre de ventes apparaît sur les cartes de vendeurs (exemples lus : « + 12 589 ventes »). La page ne définit pas ces compteurs : le nombre d'avis est au mieux un plancher des commandes terminées [HYPOTHÈSE]. Signal d'argent dépensé sur une place de marché, non audité, comparable d'un service à l'autre, cumulé depuis l'ouverture du compte (donc à dater par captures).

## Sources non lues (URL + raison)

- https://www.inc.com/inc-5000-methodology-how-we-selected-these-companies.html : 403. Méthode d'Inc. lue seulement en reprise par une page de lauréat (W3-12) ; https://www.pressreader.com/usa/inc-usa/20210301/282342567572492 : 403 ; archive https://webarchive.library.unt.edu/web/20161228220010/http://www.inc.com/inc5000apply/faqs.html : certificat rejeté.
- https://r.statista.com/wp-content/uploads/FT1000-Europes-Fastest-Growing-Companies-2024_Methodology.pdf : redirigé vers une page d'accueil, PDF non servi (méthode FT 1000 lue sur la page d'inscription, W3-13).
- https://www.deloitte.com/content/dam/Deloitte/us/Documents/technology-media-telecommunications/us-technology-fast-500-eligibility-requirements.pdf : 404 ; la FAQ du site slovaque de Deloitte redirige vers une page générique. La mention « supporting documentation » reste un extrait de recherche (W3-14).
- https://www.indiehackers.com/post/stripe-verified-revenue-de30646d2e et https://www.indiehackers.com/post/how-much-money-do-indie-hackers-products-make-74db9631f0 : 403. Remplacés par le relais de Changelog (W3-17).
- https://baremetrics.com/blog/storemapper-public-revenue-dashboard : ouverte, mais ne dit pas ce qu'un extrait de recherche lui attribuait (retrait du tableau de bord par Storemapper) : affirmation non vérifiée, non utilisée.
- https://opencorporates.com/plans : 404 (la page https://opencorporates.com/pricing/ a été lue à la place).
- ecfr.gov (17 CFR 227.201) : redirigé vers un écran anti-robot ; remplacé par Cornell LII. https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-k : 403 ; remplacé par les règles S-X 3-02 et 8-02.
- https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx, https://cards.web.commerce.state.mn.us/, https://www.cards.commerce.state.mn.us/, https://dfpi.ca.gov/regulated-industries/regulated-entities-list/?id= : 403 ; www.wdfi.org : domaine introuvable. Les trois bases ne sont connues que par le cabinet de W3-16.
- https://francetravail.io/data/api/offres-emploi : rendu JavaScript sans texte ; https://api.gouv.fr/les-api/api-offres-emploi : redirigé vers data.gouv.fr/dataservices.
- https://transparency.meta.com/researchtools/ad-library-tools (et variante zh-cn) : titre seul. https://ads.google.com/home/tools/keyword-planner/ : redirigé vers le mur de consentement de Google.
- https://www.appfigures.com/pricing : 403. https://sensortower.com/pricing : non tenté.
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2080235 (sonde pour Lewis et Rao) : 403, non lue ; https://www.nber.org/papers/w10148.pdf et https://content.e-bookshelf.de/media/reading/L-13331335-cf42c802cd.pdf : PDF binaires illisibles ; https://juststartwith-com.pages.dev/en/david-bland/testing-business-ideas et https://www.strategyzer.com/books/testing-business-ideas : 404. Un PDF intégral du livre hébergé sur un site universitaire est apparu dans une recherche : non ouvert volontairement (copie probablement non autorisée).
- https://www.unternehmensregister.de/de et https://www.bundesanzeiger.de/ : ouvertes, sans mention du coût d'accès aux comptes ; https://developer.company-information.service.gov.uk/ : ouverte, sans mention de gratuité ni de limite ; https://www.baremetrics.com/open-startups : ouverte, sans mention de vérification ni de fermeture.
- Extraits de recherche non ouverts : Inc. (« reserves the right to decline applicants »), Deloitte (« supporting documentation »), FT 1000 (étape de vérification), Sensor Tower (pas de formule gratuite), Google Ads Transparency Center (30 jours), Meta (7 ans pour les pubs politiques), France Travail (aucun quota officiel trouvé).

## Trous à combler (statut : partiel)

- Comptes déposés au Royaume-Uni : seuil d'exemption d'audit et changements annoncés pour 2027 non lus. Allemagne : coût d'accès aux comptes via Unternehmensregister non confirmé. Companies House API : gratuité non confirmée par une page.
- Keyword Planner : gratuité, tranches de volume pour les petits comptes, obligation d'avoir une campagne : non confirmés.
- Force de preuve de Bland et Osterwalder : niveaux exacts de l'échelle non lus (livre non accessible).
- Aucune recherche dédiée à des études favorables à l'heuristique « durée de pub = rentabilité » ; Lewis et Rao non lue.
- Aucun ratio « avis par vente » ni « téléchargements par avis » sourcé. Classements de ventes de grandes places de marché (Amazon Best Sellers Rank, Etsy) : non lus, aucune source ouverte sur leur lien avec les ventes réelles ; seules ComeUp et Codeur (W3-48, W3-49) ont été ouvertes.
- Jurisprudence ou position de la DGCCRF sur la fausse porte et la précommande : non cherchée (economie.gouv.fr/dgccrf bloqué, budget de recherche épuisé).
