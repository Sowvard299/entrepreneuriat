# Consignes communes aux auditeurs (phase 4)

Contexte : 6 étudiants en master marketing, Paris / petite couronne, budget < 5 000 €, aucun développeur, temps partiel. Ils cherchent un modèle qui se vend déjà, à faire mieux. Lis d'abord :
- `C:\Users\fifla\OneDrive\Documents\CLAUDE\Entrepreunariat\CLAUDE.md`
- `C:\Users\fifla\OneDrive\Documents\CLAUDE\Entrepreunariat\ideas\_recherche-v2\idees-classees.md` (fiches des idées et grille de score)
- la section « Règles de preuve » de `C:\Users\fifla\OneDrive\Documents\CLAUDE\Entrepreunariat\ideas\_recherche-v2\signaux\_consignes-communes.md` (mêmes règles : URL, date, citation de 15 mots maximum, aucun chiffre inventé, [HYPOTHÈSE] sinon, garder les contradictions).

Ne lis pas `ideas/_recherche/` ni `ideas/recrutement-garages/`.

## Ce que doit contenir chaque audit (une section par idée)

1. **Concurrents réels** (5 à 10 par idée, directs et indirects) : nom, ce qu'ils vendent, **prix public** (ou « non publié »), taille (CA via l'API `https://recherche-entreprises.api.gouv.fr/search?q=<nom>` champ `finances`, nombre de clients, levées de fonds avec source), **avis clients** (note, nombre d'avis, plateforme) et **2 ou 3 faiblesses citées par leurs propres clients**, avec citation datée.
2. **Prédécesseurs qui ont échoué** : qui, quand, pourquoi (BODACC : `https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=...`, presse). Si rien n'est trouvé, dis-le.
3. **Cadre juridique vérifié sur une source officielle** (Légifrance, service-public, entreprendre.service-public, ministère, DGCCRF) : agréments, cartes, diplômes, règles de démarchage, responsabilité. Cite l'article.
4. **Économie unitaire, premiers éléments** : prix réaliste constaté, coût direct, heures de travail par vente ou par client et par mois, revenu par heure de travail. Distingue ce qui est sourcé de ce qui est [HYPOTHÈSE].
5. **Score recalculé** : reprends les 7 notes de la grille (Arg, Faib, Doul, Éq, Vit, Test, Tail) ; pour chaque note modifiée, une phrase d'explication avec l'ID de la preuve. Donne le nouveau score pondéré (0,25 × Arg + 0,15 × (Faib + Doul + Éq + Vit) + 0,10 × Test + 0,05 × Tail).
6. **Verdict** en 3 lignes : ce qui tient, ce qui casse, la meilleure variante de l'idée si l'audit en révèle une.

## Règles de fonctionnement
- Environ 25 recherches web (WebSearch mode "standard") au maximum, ouverture directe des pages (WebFetch) privilégiée.
- Écris dans ton fichier au fil de l'eau (au moins après chaque concurrent ou chaque bloc), pour survivre à une coupure. Si le fichier existe déjà, relis-le et continue sans doublon.
- Reddit, LinkedIn, Malt, Indeed bloquent souvent : essaie WebFetch ; sinon, si les outils `mcp__Claude_Browser__*` sont disponibles, ouvre TON propre onglet (`tabs_create`, passe le `tabId`, `get_page_text`, ferme l'onglet à la fin). Ne te connecte à rien, refuse les cookies non essentiels, ne remplis aucun formulaire. Liste les sources non lues en fin de fichier.
- Aucune question : prends une hypothèse et note-la.
- Ce que tu rends au coordinateur : 200 mots maximum, avec pour chaque idée l'ancien score, le nouveau, et la raison principale du changement.
