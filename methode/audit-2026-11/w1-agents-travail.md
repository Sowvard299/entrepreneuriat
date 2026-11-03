# W1 : recherche documentaire fiable avec des agents IA et vérification des sources (fichier de travail)

- Mission : ce que disent les sources de référence sur (a) la recherche documentaire par agents IA, (b) la vérification des sources. Méthode, pas marché.
- Date : 2026-11-03
- Recherches web (WebSearch) utilisées : 7 / 15. Pages ouvertes : environ 35 (WebFetch, et curl pour le texte brut).
- Preuves : 41 (39 sources externes W1-1 à W1-39, 2 observations de terrain W1-40 et W1-41, qui ne sont pas des sources).
- Domaines distincts : 13 (anthropic.com, platform.claude.com, code.claude.com, cdn.openai.com, github.com, arxiv.org, cjr.org, ebu.ch, communication.vrt.be, law.stanford.edu, hapgood.us, hendrix.edu, en.wikipedia.org). Part du plus gros : anthropic.com, 11 preuves sur 39 (28 %) ; arxiv.org, 9 sur 39 (23 %).
- Statut : partiel. Toutes les sources demandées ont été ouvertes. Manquent : l'article Nature Communications lui-même (contrôle anti-robot), la page HTML OpenAI et son centre d'aide (403), la version publiée 2019 de Wineburg et McGrew, et toute mesure du gain de nos règles (aucune source n'en publie).
- Contrôle des citations : chaque citation « ouverte » a été cherchée mot pour mot dans le texte brut de la page (HTML ou PDF) par un script (curl, retrait des balises, recherche exacte insensible à la casse et aux espaces). Ligne « Contrôle » de chaque preuve = résultat. Limite du script : une expression trouvée « quelque part sur la page » peut venir d'un commentaire (cas SIFT, voir W1-28).
- Vocabulaire : « primaire » = le document lui-même (étude, billet, documentation, politique) ; « secondaire » = quelqu'un d'autre qui le décrit ou le recopie. « Ouverte » = page lue en entier ou en partie ; « extrait » = vue seulement dans un résultat de recherche (aucune preuve de ce fichier n'est dans ce cas).
- [inférence] = règle que j'en déduis pour notre système, que la source ne dit pas telle quelle.

## Lot 1 : Anthropic, « How we built our multi-agent research system »

### W1-1 : Briefer chaque sous-agent
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « Each subagent needs an objective, an output format, guidance on the tools and sources »
- Chiffres clés : aucun. L'article raconte que des consignes courtes du type « research the semiconductor shortage » étaient trop vagues : sous-agents qui mal interprètent la tâche ou refont les mêmes recherches.
- Limites : système interne d'Anthropic (2025), évaluations internes non publiées ; pas de mesure isolée de l'effet de la consigne.
- Règle pour nous : chaque brief du coordinateur contient quatre choses écrites : objectif, format de sortie, sources et outils à privilégier (dont « ouvrir la page, ne jamais citer un extrait »), limites de la tâche. `chercheur.md` fixe déjà format et budget ; je n'ai pas vu les briefs réels, donc à vérifier : critère d'arrêt par sous-question et consigne d'ouverture de page [inférence].
- Contrôle : citation retrouvée mot pour mot (script).

### W1-2 : Sources de moindre qualité préférées par les agents
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources »
- Citation 2 : « source quality (did it use primary sources over lower-quality secondary sources?) »
- Chiffres clés : aucun. Le correctif est qualitatif : « Adding source quality heuristics to our prompts helped resolve this issue. » Les sources « faisant autorité » citées en exemple sont « academic PDFs or personal blogs » : l'autorité compte, pas le format.
- Limites : correctif décrit sans mesure ; c'est un critère de juge, pas une règle chiffrée.
- Règle pour nous : ajouter à `chercheur.md` un bloc d'heuristiques de qualité de source et exiger, à chaque page lue, une ligne « qui publie, primaire ou secondaire ». Ordre proposé : émetteur du chiffre (INSEE, comptes déposés, grille tarifaire du vendeur) > fédération > presse > blog ou vendeur de rapports > contenu optimisé SEO [ordre = inférence ; la source donne seulement le principe « primaire avant secondaire de moindre qualité »].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-3 : Effort proportionné et critère d'arrêt
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « Early agents made errors like spawning 50 subagents for simple queries »
- Citation 2 : « scouring the web endlessly for nonexistent sources »
- Chiffres clés : barème écrit dans le prompt : « Simple fact-finding requires just 1 agent with 3-10 tool calls » ; comparaisons directes 2 à 4 sous-agents de 10 à 15 appels ; recherche complexe plus de 10 sous-agents. Conseil de recherche : « Start wide, then narrow down. » car « Agents often default to overly long, specific queries that return few results. »
- Limites : valeurs propres à leur système ; corrigées par des règles dans le prompt, sans mesure publiée.
- Règle pour nous : chaque brief fixe un nombre d'ouvertures de pages par sous-question et une sortie « non établi » (pas de recherche sans fin d'une preuve qui n'existe peut-être pas) ; requêtes courtes et larges d'abord. Les valeurs du plafond sont à fixer par nous [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-4 : Passe de citation séparée
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « passes all findings to a CitationAgent, which processes the documents »
- Chiffres clés : aucun.
- Limites : l'article ne dit ni comment ce CitationAgent fonctionne ni son exactitude ; aucune mesure publiée.
- Règle pour nous : séparer produire et attribuer. Une étape dédiée, après la collecte, relit chaque énoncé contre la page source et fixe l'endroit exact de la citation. Chez nous : étape scriptée avant la fin de mission (voir W1-14), puis le vérificateur [inférence].
- Contrôle : citation retrouvée mot pour mot (script).

### W1-5 : Évaluer avec un petit jeu fixe, un juge LLM et un regard humain
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « We started with a set of about 20 queries representing real usage patterns. »
- Citation 2 : « citation accuracy (do the cited sources match the claims?) »
- Chiffres clés : environ 20 requêtes ; critères du juge LLM : exactitude factuelle, exactitude des citations, complétude, qualité des sources, efficacité des outils ; un seul appel avec un seul prompt, note de 0,0 à 1,0, jugé le plus cohérent avec les humains. « Human evaluation catches what automation misses » : les testeurs humains ont vu les agents choisir des fermes de contenu SEO, ce que les évaluations automatiques n'avaient pas vu.
- Limites : petit échantillon, évaluation interne ; les auteurs disent que le juge marche surtout quand la réponse attendue est claire.
- Règle pour nous : garder un jeu fixe d'environ 20 preuves déjà contrôlées (bonnes et mauvaises) à repasser après chaque modification de `chercheur.md` ou `verificateur.md` ; garder une relecture humaine d'un échantillon pour les biais de sélection des sources [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

## Lot 2 : Anthropic (suite) et « Building effective agents »

### W1-6 : Coût et domaine de validité du multi-agents
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « multi-agent systems use about 15× more tokens than chats. »
- Citation 2 : « multi-agent systems require tasks where the value of the task is high enough »
- Chiffres clés : +90,2 % face à un seul agent Claude Opus 4 sur leur évaluation interne ; « token usage by itself explains 80% of the variance » (évaluation BrowseComp) ; ces systèmes « excel especially for breadth-first queries » ; « LLM agents are not yet great at coordinating and delegating to other agents ».
- Limites : évaluations internes, tâche de recherche large ; les auteurs notent que le multi-agents convient mal quand les agents doivent partager le même contexte.
- Règle pour nous : ne pas augmenter le nombre d'agents pour corriger la qualité ; le balayage large (fiches marché) est le bon usage, la qualité vient des consignes et des contrôles. Notre plafond de 4 agents par vague est cohérent avec cette idée [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-7 : Reprise après coupure et descriptions d'outils
- Source : https://www.anthropic.com/engineering/multi-agent-research-system (date : 2025-06-13 ; primaire ; ouverte)
- Citation : « saving its plan to Memory to persist the context »
- Citation 2 : « Bad tool descriptions can send agents down completely wrong paths »
- Chiffres clés : un agent testeur d'outils a réécrit des descriptions défectueuses, d'où « a 40% decrease in task completion time for future agents using the new description » ; ils ont aussi bâti des systèmes capables de reprendre là où l'agent s'était arrêté.
- Limites : le 40 % mesure le temps de tâche, pas l'exactitude.
- Règle pour nous : le fichier de travail joue déjà le rôle du plan persistant ; y ajouter en tête ce qui est fait et ce qui reste. Décrire dans `chercheur.md` ce que fait chaque outil : WebFetch rend une réponse d'un petit modèle sur la page, pas son texte brut ; curl rend le texte brut (voir W1-40) [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-8 : Simplicité d'abord
- Source : https://www.anthropic.com/research/building-effective-agents (date : 2024-12-19 ; primaire ; ouverte)
- Citation : « This might mean not building agentic systems at all. »
- Citation 2 : « optimizing single LLM calls with retrieval and in-context examples is usually enough. »
- Chiffres clés : aucun.
- Limites : principes généraux de 2024, sans mesure ; la page signale elle-même que l'outillage a changé depuis.
- Règle pour nous : ce qui peut être fait par un script déterministe (compter des entreprises par l'API Sirene, retrouver une citation dans une page par recherche exacte) ne passe pas par un agent [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-9 : Vérité terrain à chaque étape, points de contrôle, arrêt
- Source : https://www.anthropic.com/research/building-effective-agents (date : 2024-12-19 ; primaire ; ouverte)
- Citation : « gain “ground truth” from the environment at each step »
- Citation 2 : « include stopping conditions (such as a maximum number of iterations) »
- Chiffres clés : aucun. Même page : les agents peuvent faire une pause pour un retour humain « at checkpoints or when encountering blockers » ; tests étendus en bac à sable.
- Limites : principes sans mesure.
- Règle pour nous : la vérité terrain d'une preuve est le texte de la page. Le contrôle doit se faire à chaque preuve, au moment de l'écrire, et pas seulement sur un échantillon de 10 en fin de vague. Chaque mission a un plafond d'itérations et une sortie « non établi » [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-10 : Rendre l'erreur difficile par la forme de l'outil
- Source : https://www.anthropic.com/research/building-effective-agents (date : 2024-12-19 ; primaire ; ouverte)
- Citation : « Poka-yoke your tools. Change the arguments so that it is harder to make mistakes. »
- Citation 2 : « we actually spent more time optimizing our tools than the overall prompt. »
- Chiffres clés : exemple de la page : l'agent se trompait avec des chemins de fichiers relatifs ; exiger des chemins absolus a supprimé l'erreur.
- Limites : exemple tiré de leur agent de code ; pas transposé à la recherche documentaire par les auteurs.
- Règle pour nous : un petit outil qui télécharge la page, enregistre le texte brut, le code HTTP et la date, puis refuse qu'une preuve soit déclarée « ouverte » si le texte n'est pas enregistré ; et un outil qui n'accepte une citation que si elle est retrouvée dans ce texte. Avec cela, « extrait de recherche » ne peut plus passer pour « ouverte » [inférence ; conception à tester].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-11 : Boucle évaluateur-optimiseur
- Source : https://www.anthropic.com/research/building-effective-agents (date : 2024-12-19 ; primaire ; ouverte)
- Citation : « clear evaluation criteria, and when iterative refinement provides measurable value »
- Chiffres clés : aucun.
- Limites : motif décrit, sans mesure.
- Règle pour nous : la boucle vérificateur vers chercheur n'a de valeur que si les critères sont écrits (✔ / ≈ / ✘ plus « la page soutient-elle l'énoncé tel qu'utilisé ? ») et si le chercheur corrige à partir du rapport. Aujourd'hui `CLAUDE.md` prévoit « relancer ou déclasser » après coup ; la correction ciblée des preuves en ✘ ou ≈ n'est pas prévue [inférence].
- Contrôle : citation retrouvée mot pour mot (script).

## Lot 3 : documentation Claude Code (sous-agents, mémoire, hooks) et OpenAI Deep Research

### W1-12 : Sous-agents Claude Code : isolement, reprise, bonnes pratiques
- Source : https://code.claude.com/docs/en/sub-agents (date inconnue, notes de version jusqu'à v2.1.304 ; primaire ; ouverte)
- Citation : « Each subagent invocation creates a new instance rather than continuing an earlier one. »
- Citation 2 : « Limit tool access: grant only necessary permissions for security and focus »
- Chiffres clés : aucun. Même page : « Each subagent runs in its own context window with a custom system prompt » ; bonnes pratiques listées : sous-agents ciblés (« each subagent should excel at one specific task »), descriptions précises, accès aux outils limité, versionnement.
- Limites : documentation de produit, pas une étude ; ne dit rien de la fiabilité des citations. Lue en entier par curl ; WebFetch n'en avait lu que les 100 000 premiers caractères.
- Règle pour nous : (1) une mission coupée n'a pas d'autre mémoire que le fichier de travail, ce qui justifie d'écrire au fil de l'eau. (2) `verificateur.md` liste ses outils (WebFetch, Read, Write, Grep, Glob, Bash) : il n'a pas WebSearch, donc ne peut pas faire de lecture latérale (W1-29) ; lui en donner un budget est un choix explicite à faire [déduction du fichier `verificateur.md` que j'ai lu et de la ligne de la doc sur le champ `tools`].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-13 : Mémoire persistante d'un sous-agent
- Source : https://code.claude.com/docs/en/sub-agents (date inconnue ; primaire ; ouverte)
- Citation : « The memory field gives the subagent a persistent directory that survives across conversations. »
- Chiffres clés : aucun.
- Limites : fonctionnalité de produit, jamais essayée ici ; la page précise que le champ est sans effet si la mémoire automatique est désactivée (réglage `autoMemoryEnabled`), ce que je n'ai pas contrôlé dans ce projet.
- Règle pour nous : donner au chercheur et au vérificateur un répertoire de mémoire pour y consigner les domaines qui répondent 403, la voie qui a marché (curl ou WebFetch) et les recettes d'API : on ne reteste pas les mêmes domaines à chaque vague (voir W1-41) [inférence].
- Contrôle : citation retrouvée mot pour mot (script).

### W1-14 : Hooks : une barrière mécanique avant la fin de mission
- Source : https://code.claude.com/docs/en/hooks (date inconnue ; primaire ; ouverte, texte intégral par curl)
- Citation : « exit code 2 on these events sends Claude back to keep working »
- Citation 2 : « Prevents the subagent from stopping »
- Chiffres clés : aucun. Même page : un hook défini dans un sous-agent ne tourne que pendant que ce sous-agent travaille ; un hook `Stop` y est converti en `SubagentStop`.
- Limites : mécanisme documenté, pas une preuve d'efficacité ; un hook exécute une commande sur la machine (à relire avant usage) ; sous Windows la doc exige Git Bash.
- Règle pour nous : un hook dans le frontmatter de `chercheur.md` lance un script qui relit le fichier de travail, retrouve chaque citation « ouverte » dans la page enregistrée, et sort avec le code 2 en listant les échecs ; le chercheur doit corriger avant de rendre. Les erreurs de citation tombent avant le coordinateur et avant le vérificateur [inférence ; conception non testée chez nous].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-15 : OpenAI Deep Research, fiche système : taux d'hallucination mesuré
- Source : https://cdn.openai.com/deep-research-system-card.pdf (date : 2025-02-25 ; primaire ; ouverte, PDF)
- Citation : « the hallucination rate noted above actually overstates how often deep research hallucinates »
- Citation 2 : « the information in our test set was out of date »
- Chiffres clés : test PersonQA (faits sur des personnes, 18 catégories) : précision 0,86 pour deep research contre 0,50 (GPT-4o), 0,55 (o1), 0,22 (o3-mini) ; taux d'hallucination 0,13 contre 0,30, 0,20 et 0,15.
- Limites : mesure du fournisseur sur son propre test ; les auteurs reconnaissent que la référence du test était périmée (il a pu donner plus d'enfants que la liste). Le chiffre de 13 % est donc un majorant dans leur test, pas une garantie.
- Règle pour nous : même le meilleur agent commercial publié garde un taux d'hallucination non nul : le contrôle de fin de mission reste nécessaire avec un bon modèle. Toute « vérité de référence » d'un contrôle doit porter sa date [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-16 : OpenAI Deep Research : limites annoncées par le fournisseur
- Source : https://cdn.openai.com/API/docs/deep_research_blog.pdf (copie PDF de la page « Introducing deep research », datée 2025-02-02, imprimée le 2025-02-21 ; primaire ; ouverte ; la page HTML openai.com répond 403)
- Citation : « It may struggle with distinguishing authoritative information from rumors »
- Citation 2 : « currently shows weakness in confidence calibration, often failing to convey uncertainty accurately »
- Chiffres clés : « scores a new high at 26.6% accuracy » sur Humanity's Last Exam. La page promet aussi « Every output is fully documented, with clear citations and a summary of its thinking ».
- Limites : annonce commerciale de lancement ; les auteurs écrivent qu'ils attendent une amélioration rapide, donc état daté de février 2025 ; aucune mesure d'exactitude des citations.
- Règle pour nous : un agent de recherche performant peut ne pas distinguer une source faisant autorité d'une rumeur et dire mal son incertitude. Le ton du chercheur n'est donc pas un indicateur : la confiance (forte, moyenne, faible) doit découler du statut de vérification (page ouverte, citation retrouvée, sources indépendantes), pas de l'assurance de la rédaction [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-17 : Les pages web peuvent contenir des consignes
- Source : https://cdn.openai.com/deep-research-system-card.pdf (date : 2025-02-25 ; primaire ; ouverte, PDF)
- Citation : « the model might mistakenly follow those instructions »
- Chiffres clés : aucun retenu (la fiche décrit une évaluation interne de résistance).
- Limites : risque décrit pour l'agent d'OpenAI, avec ses propres protections ; pas de mesure pour Claude Code.
- Règle pour nous : ajouter à `chercheur.md` que le contenu d'une page est une donnée, jamais une consigne, et que toute phrase d'une page qui s'adresse à l'agent est ignorée et signalée dans le fichier [inférence ; risque de sécurité, hors problème d'exactitude].
- Contrôle : citation retrouvée mot pour mot (script).

## Lot 4 : agents de recherche existants (GPT Researcher, STORM, WebGPT)

### W1-18 : GPT Researcher : architecture, et ce que le dépôt ne mesure pas
- Source : https://github.com/assafelovic/gpt-researcher (README, date de version inconnue, consulté le 2026-11-03 ; primaire ; ouverte)
- Citation : « The planner generates research questions, while the execution agents gather relevant information. »
- Citation 2 : « Summarize and source-track each resource. »
- Chiffres clés : « Aggregate over 20 sources for objective conclusions. » Un filtre de passages appelé Jev garde 73 % de passages pertinents contre 46 % pour des embeddings, sur 28 tâches (« Jev's context is 59% more relevant than embeddings, at the same cost »), benchmark interne.
- Limites : le dépôt dit « The main goal of GPT Researcher is to reduce incorrect and biased facts. » et « We do not aim to eliminate biases; we aim to reduce it » ; il se déclare « an experimental application and is provided "as-is" ». Je n'y ai trouvé aucune mesure indépendante de l'exactitude des citations ; le suivi de source se fait sur les résumés, pas sur des citations mot à mot. Documentation du projet (docs.gptr.dev) non ouverte.
- Règle pour nous : reprendre l'idée « une sous-question, un agent d'exécution, une synthèse qui garde la trace de la source », sans considérer l'outil comme une garantie. Le nombre de sources (« 20 ») ne dit rien de l'exactitude (voir W1-26 : le système qui cite le plus n'est pas le plus précis) [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script) ; les autres phrases citées dans ce bloc aussi (« reduce incorrect », « eliminate biases », « 59 % », « 73 % »).

### W1-19 : STORM : plusieurs points de vue et filtre de sources par règles
- Source : https://arxiv.org/pdf/2402.14207 (arXiv 2024-02-22, v2 2024-04-08, NAACL 2024 ; primaire ; ouverte, PDF) ; dépôt https://github.com/stanford-oval/storm (licence MIT, dernière nouvelle datée 2025-01)
- Citation : « rule-based filter according to the Wikipedia guideline »
- Citation 2 : « discovering diverse perspectives in researching the given topic »
- Chiffres clés : face à une base RAG guidée par un plan, davantage d'articles STORM jugés bien organisés (+25 % en absolu) et couvrants (+10 %) ; qualité des citations 84,83 (rappel) et 85,18 (précision), jugées par Mistral 7B-Instruct (Table 4) ; 10 éditeurs Wikipédia expérimentés consultés. Le filtre applique la page Wikipédia sur les sources fiables aux résultats de recherche pour exclure les sources peu fiables.
- Limites : articles encyclopédiques en anglais ; citations jugées par un petit modèle automatique, pas par des humains ; les auteurs écrivent que la qualité reste en deçà d'articles humains révisés en neutralité et vérifiabilité (voir W1-20).
- Règle pour nous : (1) un filtre par domaine, décidé avant lecture, qui écarte ou rétrograde les classes de sources peu fiables (inspiré de W1-37 et W1-39) ; (2) poser les questions depuis plusieurs points de vue (acheteur, vendeur, régulateur, concurrent déçu) avant de chercher, ce qui rejoint notre règle de diversité des domaines [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-20 : STORM : ce que les éditeurs ont trouvé qui reste faux
- Source : https://arxiv.org/pdf/2402.14207 (2024-04-08 pour la v2 ; primaire ; ouverte, PDF)
- Citation : « the collected information may still be biased towards dominant sources on the Internet »
- Citation 2 : « calls for high-level sensemaking rather than mere fact-level verification »
- Chiffres clés : aucun. Problèmes relevés par les éditeurs : ton promotionnel venant des sources, et « red herring » ou association abusive de faits sans lien.
- Limites : même cadre que W1-19.
- Règle pour nous : le contrôle « la phrase est-elle sur la page ? » ne détecte pas l'association abusive (un chiffre vrai attaché à un autre périmètre : autre pays, autre année, autre entreprise). Ajouter au contrôle : « ce fait prouve-t-il l'énoncé qu'on en tire ? ». Les sources de tête sont celles du web dominant (blogs optimisés SEO, vendeurs de rapports), donc à rétrograder [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

### W1-21 : WebGPT : la citation est une action de l'environnement ; le risque de choisir ce qui plaît
- Source : https://arxiv.org/pdf/2112.09332 (v3 : 2022-06-01 ; primaire ; ouverte, PDF)
- Citation : « page title, domain name and extract are recorded to be used later as a reference »
- Citation 2 : « incentivizes models to cherry-pick references that they expect labelers to find convincing »
- Chiffres clés : aucun retenu. Mécanisme : l'action « Quote » enregistre le titre, le domaine et l'extrait au moment où le modèle navigue ; la réponse finale est ensuite composée à partir de ces références. Les auteurs écrivent aussi « references are far from a panacea ».
- Limites : GPT-3 affiné en 2021, environnement texte, pas notre cas ; le risque de choix des références qui plaisent est présenté comme « early signs », pas comme un taux.
- Règle pour nous : (1) la citation vient d'une copie faite depuis la page, pas d'un texte retapé par le modèle ; (2) un agent récompensé pour trouver des preuves de la piste choisit celles qui conviennent : imposer une recherche active de ce qui contredit (la contre-preuve de `CLAUDE.md`) et faire chercher une contre-preuve par le vérificateur pour chaque chiffre décisif [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

## Lot 5 : exactitude des citations des moteurs de recherche et agents IA (études)

### W1-22 : Tow Center / CJR : taux d'erreur et assurance
- Source : https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php (date : 2025-03-06 ; primaire, étude ; ouverte)
- Citation : « Collectively, they provided incorrect answers to more than 60 percent of queries. »
- Citation 2 : « Most of the tools we tested presented inaccurate answers with alarming confidence. »
- Chiffres clés : 8 outils, 1 600 requêtes (20 éditeurs × 10 articles × 8 outils) ; Perplexity 37 % de réponses incorrectes ; Grok 3 94 % ; les versions payantes se trompent plus souvent avec assurance (« Premium models provided more confidently incorrect answers than their free counterparts. »).
- Limites : la tâche est d'identifier l'article d'origine d'un extrait de presse ; les auteurs écrivent « our findings are not intended to be extrapolated to all models or news organizations » et ne testent qu'une occurrence par extrait ; outils de début 2025.
- Règle pour nous : l'assurance d'un modèle n'est pas un signal, et un modèle plus cher ne dispense pas du contrôle. Notre taux d'erreur de 10 à 70 % selon les fichiers est dans la fourchette des taux publiés (voir W1-24 à W1-27), mais les tâches et les définitions d'erreur diffèrent : comparaison d'ordre de grandeur seulement.
- Contrôle : 3 citations retrouvées mot pour mot (script).

### W1-23 : Tow Center / CJR : URLs inventées, mauvais article, copies syndiquées
- Source : https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php (date : 2025-03-06 ; primaire ; ouverte)
- Citation : « More than half of responses from Gemini and Grok 3 cited fabricated or broken URLs. »
- Citation 2 : « The generative search tools we tested had a common tendency to cite the wrong article. »
- Chiffres clés : pour Grok 3, « 154 citations led to error pages » sur 200 requêtes ; Perplexity Pro a « cited syndicated versions of Tribune articles for three out of the ten queries », malgré un partenariat avec le Texas Tribune. « Content licensing deals with news sources provided no guarantee of accurate citation in chatbot responses. »
- Limites : mêmes que W1-22.
- Règle pour nous : une URL n'est écrite que si elle a été ouverte dans la session (code 200, texte lu) ; elle ne vient jamais de la mémoire du modèle. Citer l'émetteur d'origine plutôt qu'une copie ou un relais.
- Contrôle : 2 citations retrouvées mot pour mot (script) ; le chiffre « 154 » et la citation sur les copies aussi.

### W1-24 : EBU / BBC « News Integrity in AI Assistants » (2025)
- Source : https://www.ebu.ch/news/2025/10/ai-s-systemic-distortion-of-news-is-consistent-across-languages-and-territories-international-study-by-public-service-broadcaste (date : 2025-10-22 ; primaire ; ouverte via WebFetch seulement, curl répond 403) ; copie du communiqué par un partenaire : https://communication.vrt.be/largest-study-of-its-kind-shows-ai-assistants-misrepresent-news-content-45-of-the-time-regardless-of-language-or-territory (secondaire ; ouverte par curl ; citations ci-dessous contrôlées sur cette copie)
- Citation : « in 31% of cases, references were missing or misleading »
- Citation 2 : « 45% of all AI answers had at least one significant issue »
- Chiffres clés : plus de 3 000 réponses de ChatGPT, Copilot, Gemini et Perplexity évaluées par des journalistes ; 22 médias de service public, 18 pays (14 langues selon la page EBU, non revérifié par script) ; 45 % avec au moins un problème significatif ; 31 % avec un problème de sources ; 20 % avec une inexactitude majeure (« fabricated or outdated information ») ; Gemini 76 % de réponses avec problème significatif.
- Limites : questions d'actualité ; évaluateurs = journalistes des médias partenaires ; 4 assistants ; octobre 2025. La page EBU parle d'« some improvements » par rapport à l'étude BBC de février 2025 (WebFetch seul).
- Règle pour nous : les problèmes de source (31 %) sont plus fréquents que les inexactitudes majeures (20 %). Le contrôle doit viser l'attribution (« la source dit-elle ce qu'on lui fait dire ? ») et pas seulement la présence d'un chiffre.
- Contrôle : 2 citations retrouvées mot pour mot sur la copie VRT (script) ; ne sont PAS revérifiées sur la page EBU elle-même (403 en curl) : les autres phrases attribuées à l'EBU dans ce fichier viennent de WebFetch.

### W1-25 : Liu, Zhang et Liang (Stanford) : vérifiabilité des moteurs de recherche génératifs
- Source : https://arxiv.org/pdf/2304.09848 (arXiv, v2 : 2023-10-23 ; primaire, étude ; ouverte, PDF)
- Citation : « only 74.5% of citations support their associated sentence »
- Citation 2 : « the responses that seem more helpful are often those with inaccurate citations »
- Chiffres clés : Bing Chat, NeevaAI, perplexity.ai, YouChat ; en moyenne 51,5 % des phrases entièrement soutenues par leurs citations (rappel de citation) et 74,5 % des citations qui soutiennent leur phrase (précision de citation) ; corrélation précision de citation et utilité perçue r = -0,96 ; 34 annotateurs, accord par paires supérieur à 82 %.
- Limites : systèmes de mars 2023, dépassés ; requêtes grand public, pas des données d'entreprise ; évaluation humaine.
- Règle pour nous : suivre deux mesures dans l'audit. « Rappel de citation » : part des énoncés décisifs adossés à une source vérifiée. « Précision de citation » : part des sources citées qui soutiennent bien l'énoncé associé. Les preuves qui paraissent les plus utiles sont celles à vérifier en premier : l'utilité apparente est anti-corrélée à l'exactitude des citations dans cette étude [inférence sur la priorité de contrôle].
- Contrôle : 3 citations retrouvées mot pour mot (script) ; « a mere 51.5% of generated sentences are fully supported by citations ».

### W1-26 : DeepResearch Bench (cadre FACT) : exactitude des citations d'agents « deep research »
- Source : https://arxiv.org/pdf/2506.11763 (arXiv v1 : 2025-06-13 ; primaire, benchmark ; ouverte, PDF)
- Citation : « the Judge LLM assesses whether this content provides sufficient evidence to support the statement »
- Citation 2 : « We retrieve the textual content of the webpage using the Jina Reader API. »
- Chiffres clés : précision de citation (tableau 1) : Perplexity Deep Research 90,24 %, Grok Deeper Search 83,59 %, Gemini-2.5-Pro Deep Research 81,44 %, OpenAI Deep Research 77,96 % ; citations « effectives » par rapport : 31,26 ; 8,15 ; 111,21 ; 40,79. Sur les 16 systèmes du tableau, la précision va de 39,36 % à 94,04 %. Juge : Gemini 2.5 Flash.
- Limites : juge LLM, avec ses propres erreurs ; tâches = rapports de recherche ; d'après un résumé vu seulement en extrait de recherche (non vérifié), des versions ultérieures de l'article donnent d'autres valeurs : citer la version v1 avec sa date.
- Règle pour nous : une évaluation de citation robuste récupère le texte de la page citée, puis rend un verdict binaire « soutient / ne soutient pas » par énoncé : c'est la procédure à donner au vérificateur. Un juge économique y a suffi dans leur protocole. Dans ce tableau, le système qui cite le plus (Gemini, 111) n'est pas le plus précis (81 %) ; aucun lien de cause n'est établi, mais exiger « au moins 3 sources » sans contrôle proportionné peut augmenter le nombre de citations fausses [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script) ; chiffres du tableau lus dans le texte du PDF.

### W1-27 : SourceCheckup (Nature Communications, 2025) : recherche web activée, énoncés non soutenus
- Source : https://law.stanford.edu/publications/an-automated-framework-for-assessing-how-well-llms-cite-relevant-medical-references/ (notice Stanford Law reprenant le résumé de l'article paru dans Nature Communications 16, 3615, le 2025-04-16 ; secondaire ; ouverte) ; l'article lui-même (PMC) n'a pas pu être ouvert (contrôle anti-robot)
- Citation : « approximately 30% of individual statements are unsupported »
- Citation 2 : « between 50% and 90% of LLM responses are not fully supported »
- Chiffres clés : 7 LLM, 800 questions, 58 000 paires énoncé-source ; pour GPT-4o avec recherche web, environ 30 % d'énoncés non soutenus et presque la moitié des réponses non entièrement soutenues ; « Independent assessments by doctors further validate these results. »
- Limites : domaine médical ; vérificateur automatique validé contre des médecins mais je n'ai pas lu l'article ; résumé de seconde main.
- Règle pour nous : même avec la recherche web, une part importante des énoncés n'est pas soutenue par la source citée dans ce test : le contrôle se fait énoncé par énoncé, pas au niveau du fichier.
- Contrôle : 2 citations retrouvées mot pour mot sur la notice (script).

## Lot 6 : méthodes de vérification (SIFT, lecture latérale, Chain-of-Verification, SAFE, API de citations)

### W1-28 : SIFT (Caulfield) : quatre gestes avant de se servir d'une page
- Source : https://hapgood.us/2019/06/19/sift-the-four-moves/ (date : 2019-06-19 ; primaire, billet de l'auteur de la méthode ; ouverte)
- Citation : « trace the claim, quote, or media back to the source »
- Citation 2 : « look for trusted reporting or analysis on the claim »
- Chiffres clés : aucun. Les quatre gestes : Stop ; Investigate the source ; Find better coverage ; Trace claims, quotes, and media to the original context. Dosage : « Quick and shallow investigations will form most of what we do on the web. » Premier geste : « Don't read it or share media until you know what it is. »
- Limites : méthode d'éducation aux médias pour des humains, sans mesure d'efficacité dans ce billet. Le billet lui-même n'emploie pas l'expression « lecture latérale » : le script la trouve sur la page, mais seulement dans des commentaires de 2021 (positions 65 872 et suivantes sur 151 052 caractères, les commentaires commençant à 7 240). Ne pas lui attribuer ce terme.
- Règle pour nous : routine en quatre temps avant d'utiliser une page. (S) savoir ce que c'est : qui publie, quel type, quelle date. (I) qui est derrière et avec quel intérêt : vendeur de rapports, fédération, institution. (F) chercher une couverture indépendante du même chiffre. (T) remonter à l'original (tableau INSEE, comptes déposés, grille de prix du vendeur) et le citer à la place du relais. Approfondir seulement les chiffres décisifs [transposition aux agents : inférence].
- Contrôle : 4 citations retrouvées mot pour mot (script) ; le geste 4 est cité par WebFetch sous la forme « Trace claims, quotes, and media to the original context » (à contrôler, voir fin de fichier).

### W1-29 : Lecture latérale (Wineburg et McGrew) : sortir de la page pour la juger
- Source : https://www.hendrix.edu/uploadedFiles/Academics/Faculty_Resources/Teaching_and_Learning/EvaluatingDigitalInformation.pdf (copie hébergée par une université du document de travail SHEG n° 2017.A1, septembre 2017 ; primaire ; ouverte, PDF) ; la version publiée dans Teachers College Record (2019) n'a pas été lue ; résumé Stanford GSE du 2017-10-24 concordant
- Citation : « fact checkers read laterally, leaving a site after a quick scan »
- Citation 2 : « fact checkers arrived at more warranted conclusions in a fraction of the time »
- Chiffres clés : 45 participants (10 historiens docteurs, 10 vérificateurs professionnels, 25 étudiants de Stanford) ; accord entre codeurs 92 % (kappa 0,90). Tâche 1 (deux organisations de pédiatres, dont un groupe minoritaire) : score de conclusion de 0 à 2 sur le site du groupe minoritaire, vérificateurs 2 (écart-type 0), historiens 0,7, étudiants 0,16. Tâche 2 (trouver qui parraine un site) : vérificateurs 51 s en moyenne pour identifier l'organisme parent, historiens 3 min 40 s, étudiants 5 min 18 s ; « Every fact checker » a trouvé le parrain final, 6 historiens sur 10, 40 % des étudiants. Tâche 3 : conclusions notées 3,6 pour les vérificateurs contre 2,4 (historiens) et 2,3 (étudiants), mais les vérificateurs ont été plus lents (2 min 8 s contre 1 min 42 s pour les étudiants).
- Limites : « Small sample sizes exaggerate differences » ; tâche en laboratoire avec des chercheurs « peering over the shoulders » ; sites choisis par les auteurs ; humains, pas des agents ; seuls 2 historiens sur 10 se comportaient comme les vérificateurs. Le gain de temps ne vaut pas pour la tâche 3 (recherche d'une information, pas d'un jugement de crédibilité).
- Règle pour nous : pour juger une source, sortir de la page : ouvrir de nouvelles recherches sur son éditeur (qui est-ce, qui le finance, qu'en disent les autres) avant de lire le détail. Le vérificateur doit pouvoir le faire : lui donner un petit budget de WebSearch par preuve décisive (valeur à fixer : 2 ou 3 [HYPOTHÈSE]), et ne pas l'imposer pour les chiffres secondaires [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script) ; chiffres lus dans le texte du PDF.

### W1-30 : Lecture latérale : les extraits servent à trier, pas à prouver
- Source : même document que W1-29 (primaire ; ouverte)
- Citation : « They showed click restraint. »
- Citation 2 : « they mined Google's snippets for the wealth of information they contain »
- Citation 3 : « They knew that the first result was not necessarily the most authoritative »
- Chiffres clés : aucun. Les étudiants « often clicked on the first results » et allaient plus vite mais « their speed came at the expense of quality » ; les vérificateurs examinaient l'URL et la source de chaque résultat, parfois sur la 2e et la 3e page, avant d'ouvrir quoi que ce soit.
- Limites : mêmes que W1-29. Cet usage des extraits est un usage de tri (où cliquer), après lequel les vérificateurs ouvraient les pages pour conclure.
- Règle pour nous : un extrait de recherche sert à décider quelle page ouvrir (nom du site, URL, nature de l'émetteur), jamais de preuve. Parcourir toute la première page de résultats, ne pas prendre le rang 1 par défaut (le classement peut être manipulé par le référencement), juger le domaine avant d'ouvrir [inférence pour la règle ; le comportement observé est celui des vérificateurs humains].
- Contrôle : 3 citations retrouvées mot pour mot (script).

### W1-31 : Chain-of-Verification (Meta, 2023) : vérifier sans regarder la première réponse
- Source : https://arxiv.org/pdf/2309.11495 (arXiv v1 : 2023-09-20, v2 : 2023-09-25 ; primaire ; ouverte, PDF)
- Citation : « answers those questions independently so the answers are not biased by other responses »
- Citation 2 : « verifying questions should not attend to the original baseline response »
- Chiffres clés : modèle Llama 65B : précision sur des listes Wikidata 0,17 puis 0,36 avec CoVe en deux étapes ; F1 MultiSpanQA 0,39 puis 0,48 (« a 23% improvement in F1 over the few-shot baseline ») ; FACTSCORE de biographies 55,9 puis 71,4 (+28 %) avec la variante « factor+revise » ; les variantes « factored » battent la variante « joint » (par exemple 60,8 contre 63,7).
- Limites : voir W1-32.
- Règle pour nous : le vérificateur ne reçoit ni la conclusion du chercheur ni son raisonnement, seulement l'énoncé et l'URL. Il répond d'abord à une question simple (« que dit cette page sur X : valeur, date, périmètre ? »), puis seulement ensuite on compare à ce que le chercheur a écrit, de préférence par script. Transposition d'un protocole sans outil à notre cas, non démontrée chez nous [inférence].
- Contrôle : 3 citations retrouvées mot pour mot (script), dont « models that attend to existing hallucinations in the context from their own generations ».

### W1-32 : Chain-of-Verification : limites
- Source : https://arxiv.org/pdf/2309.11495 (v2 : 2023-09-25 ; primaire ; ouverte, PDF)
- Citation : « hence the model is used to check its own work »
- Citation 2 : « it does not remove them completely from generations »
- Chiffres clés : aucun. Les auteurs écrivent aussi « we do not explore tool-use » et proposent d'ajouter la recherche d'information comme extension.
- Limites : aucune lecture de document externe ; ne traite que les erreurs factuelles énoncées directement, pas les raisonnements ni les opinions ; un seul modèle ouvert (Llama).
- Règle pour nous : un modèle qui revérifie sa propre production sans accès à la source reste faillible : l'auto-vérification n'est pas une preuve. Le vérificateur doit relire la page (texte brut), pas « se souvenir » ni « raisonner ».
- Contrôle : 3 citations retrouvées mot pour mot (script).

### W1-33 : SAFE (Google DeepMind, 2024) : énoncés atomiques, recherche, verdict « soutenu ou non »
- Source : https://arxiv.org/pdf/2403.18802 (arXiv v1 : 2024-03-27, v4 : 2024-11-07, NeurIPS 2024 ; primaire ; ouverte, PDF)
- Citation : « revise each individual fact to be self-contained »
- Citation 2 : « SAFE agrees with crowdsourced human annotators 72% of the time »
- Chiffres clés : environ 16 000 faits individuels ; sur 100 désaccords tirés au hasard, « SAFE annotations were correct 76% of the time, whereas human annotations were correct only 19% » ; plus de 20 fois moins cher que des annotateurs ; chaque fait est vérifié par 5 étapes de recherche, 3 résultats par requête ; modèle utilisé : GPT-3.5-Turbo ; 13 modèles évalués sur 38 sujets.
- Limites : voir W1-34.
- Règle pour nous : (1) découper chaque preuve en énoncés atomiques et autonomes (remplacer « il », « ce marché » par l'entité) ; (2) pour chaque énoncé, requêtes de recherche indépendantes puis verdict « soutenu / non soutenu » ; (3) un juge économique avec accès à la recherche est viable (c'est un résultat de cette étude, avec les limites de W1-34).
- Contrôle : 3 citations retrouvées mot pour mot (script).

### W1-34 : SAFE : limites
- Source : https://arxiv.org/pdf/2403.18802 (v4 : 2024-11-07 ; primaire ; ouverte, PDF)
- Citation : « reporting our labels as "supported" or "not supported" by Google Search results »
- Citation 2 : « The largest cause of error was incorrect reasoning »
- Citation 3 : « Google Search may not easily find information about some fact »
- Chiffres clés : sur les 24 faits mal évalués par SAFE, la 1re cause est le raisonnement du modèle, la 2e l'absence de l'information dans les résultats de recherche, la 3e la reformulation ; les auteurs estiment que ces erreurs de raisonnement seraient en grande partie résolues par un modèle plus fort que GPT-3.5.
- Limites : le verdict est « soutenu par les résultats trouvés », pas « vrai » ; le droit et la médecine sont mal couverts par une recherche générale ; la référence humaine (annotateurs en ligne) est elle-même imparfaite (19 % de justesse sur les désaccords). Les auteurs notent que SAFE peut être restreint à des sites choisis en ajoutant « site:xxx » à la requête.
- Règle pour nous : le verdict du vérificateur est « soutenu par la page ouverte » ou « non soutenu », jamais « vrai ». Pour les points juridiques et techniques, limiter la recherche aux sites officiels. Un modèle économique doit recevoir le texte de la page, car c'est le raisonnement du modèle faible qui fait l'essentiel des erreurs restantes [inférence].
- Contrôle : 3 citations retrouvées mot pour mot (script) ; la remarque sur « site:xxx » aussi.

### W1-35 : API Citations d'Anthropic : la citation extraite plutôt que retapée
- Source : https://platform.claude.com/docs/en/build-with-claude/citations (date inconnue ; primaire, documentation ; ouverte par WebFetch, texte enregistré ; docs.claude.com redirige vers cette adresse)
- Citation : « citations are guaranteed to contain valid pointers to the provided documents »
- Citation 2 : « The API doesn’t guarantee either. »
- Chiffres clés : aucun. « In Anthropic’s evaluations, the citations feature is significantly more likely to cite the most relevant quotes » (sans chiffre) ; « cited_text does not count toward your output tokens ».
- Limites : un pointeur valide ne prouve pas que le passage soutient l'énoncé ; la phrase « The API doesn’t guarantee either » porte, dans l'exemple de la page, sur le fait que chaque champ ait une valeur et au moins une citation ; fonctionne sur des documents fournis à l'API, pas dans les sous-agents de Claude Code ; incompatible avec les sorties structurées.
- Règle pour nous : même principe d'architecture que W1-21 : la citation est extraite du texte de la page par l'outil, pas retapée par le modèle. Chez nous : un script qui copie le passage depuis le texte enregistré de la page ; le modèle ne fournit que le repère [inférence].
- Contrôle : 2 citations retrouvées mot pour mot dans le texte enregistré de la page (script).

## Lot 7 : hiérarchie et indépendance des sources (Wikipédia)

### W1-36 : Primaire, secondaire, tertiaire
- Source : https://en.wikipedia.org/wiki/Wikipedia:No_original_research (page de politique, version consultée le 2026-11-03, date de version inconnue ; primaire ; ouverte)
- Citation : « may be used on Wikipedia only to make straightforward, descriptive statements of facts »
- Citation 2 : « any interpretation needs a secondary source »
- Chiffres clés : aucun. Définitions de la page : « Primary sources are original materials that are close to an event » ; « A secondary source provides thought and reflection based on primary sources » ; « Reliable tertiary sources can help provide broad summaries of topics ».
- Limites : règles d'une encyclopédie anglophone, pas une norme d'étude de marché. Wikipédia demande des articles « based on reliable, published secondary sources », alors qu'Anthropic demande de préférer le primaire à du secondaire de moindre qualité (W1-2). Les deux se concilient ainsi : primaire pour les faits et chiffres bruts, secondaire fiable pour l'interprétation, tertiaire (encyclopédies, synthèses, agrégateurs) comme pointeur seulement.
- Règle pour nous : un chiffre brut (nombre d'entreprises, prix affiché, chiffre d'affaires déposé) se cite à l'émetteur ; une conclusion (« marché en croissance ») s'appuie sur une source secondaire fiable ; un blog ou un résumé n'est ni l'un ni l'autre, donc « confiance faible » comme le prévoit déjà `CLAUDE.md` [mise en correspondance : inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script), plus les 4 phrases entre guillemets de ce bloc.

### W1-37 : Fiabilité par usage, indépendance, relais et boucles de citation
- Source : https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources (page de politique ; primaire ; ouverte)
- Citation : « A source can be reliable or unreliable for the material it is meant to support. »
- Citation 2 : « Such sources are essentially a single source. »
- Chiffres clés : aucun. La phrase 2 vise les dépêches d'agence : « Multiple sources should not be asserted for any wire service article. » Sur les relais : « reliability should be judged based on the original source. » et « Direct links to the original source should be preferred over the aggregator's link. » Sur les boucles : « Editors should therefore beware of circular sourcing. » Sur les désaccords : « Material should be attributed in-text where sources disagree. »
- Limites : même cadre que W1-36 ; sur les statistiques, aucune règle spécifique trouvée dans la partie lue par WebFetch (100 000 premiers caractères sur 153 563).
- Règle pour nous : (1) la fiabilité se juge par usage (une page peut être fiable pour un prix affiché et pas pour une taille de marché) ; (2) « 3 sources indépendantes » : des copies d'une même dépêche, d'un même communiqué ou d'un même rapport comptent pour une seule ; (3) un relais ou un agrégateur se juge sur la source d'origine, et on cite l'original ; (4) quand deux sources divergent, le dire avec attribution plutôt que choisir.
- Contrôle : 2 citations retrouvées mot pour mot (script), plus les 5 phrases entre guillemets de ce bloc.

### W1-38 : Vérifiabilité : la charge de la preuve et le soutien de l'énoncé
- Source : https://en.wikipedia.org/wiki/Wikipedia:Verifiability (page de politique ; primaire ; ouverte)
- Citation : « The cited source must clearly support the material as presented in the article. »
- Citation 2 : « Do not reject reliable sources just because they are difficult or costly to access. »
- Chiffres clés : aucun. Sur la charge : « The burden to demonstrate verifiability lies with the editor who adds or restores material ».
- Limites : la page n'impose pas explicitement de consulter la source avant de la citer (WebFetch n'a trouvé aucune règle de ce type) ; principe de vérifiabilité, pas de vérité.
- Règle pour nous : (1) la charge de la preuve pèse sur celui qui avance le chiffre : le chercheur apporte la page et le passage, le vérificateur ne les cherche pas. (2) Une source difficile d'accès (403, payante) n'est pas écartée comme peu fiable, mais elle reste « non lue » tant qu'on ne l'a pas ouverte : ne pas la remplacer par un extrait, et ne pas lui faire porter un chiffre décisif.
- Contrôle : 3 citations retrouvées mot pour mot (script).

### W1-39 : Liste des sources « pérennes » de Wikipédia : l'exemple de Statista
- Source : https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources/Perennial_sources (liste communautaire, entrée Statista datée 2023 ; primaire ; ouverte)
- Citation : « It is not the source of the statistics it displays »
- Citation 2 : « It may be useful as a research tool to find sources of statistical information. »
- Chiffres clés : aucun. Même page, à propos d'un média dont le contenu est repris : « should be evaluated by the reliability of its original publisher ».
- Limites : consensus de rédacteurs anglophones ; je n'y ai trouvé aucune entrée pour Trustpilot (aucune occurrence dans la page) ; portée limitée à Wikipédia.
- Règle pour nous : classer les agrégateurs de statistiques et vendeurs de rapports comme « pointeur, pas source » : on s'en sert pour trouver l'émetteur d'origine, et on cite celui-ci. Cela prolonge notre règle « confiance faible » par l'étape « remonter à l'émetteur » [inférence].
- Contrôle : 2 citations retrouvées mot pour mot (script).

<!-- SUITE -->
