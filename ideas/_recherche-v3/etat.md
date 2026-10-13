# État de la recherche v3

Démarrée le 2026-10-13. Option A (de zéro : `_recherche/`, `_recherche-v2/`, `recrutement-garages/` non lus).
Mode : avec points d'arrêt. Profil : hypothèses par défaut (voir `hypotheses.md`).

## Phases

| Phase | Statut | Date |
|-------|--------|------|
| 0. Cartographie des marchés | ✔ (point d'arrêt 1 en attente) | 2026-10-13 |
| 1. Segments et signaux | à faire | |
| 2. Angles et idées | à faire | |
| 3. Tournoi | à faire | |
| 4. Validation de la gagnante | à faire | |
| 5. Kit terrain | à faire | |

## Sous-agents

| Vague | Agent | Mission | Fichier de travail | Statut |
|-------|-------|---------|--------------------|--------|
| 0.1 | chercheur A | lentilles 1 obligation datée + 2 transition | marches/obligation-transition.md | fini 2026-10-13 (10 marchés, 36 preuves ; tailles toutes bottom-up, Légifrance non ouvert) |
| 0.1 | chercheur B | lentilles 3 fragmentation + 6 capital et réseaux | marches/fragmentation-reseaux.md | fini 2026-10-13 (9 marchés, 39 preuves ; paraphrases d extraits à vérifier) |
| 0.1 | chercheur C | lentilles 4 modèle venu d'ailleurs + 5 demande en hausse | marches/ailleurs-demande.md | fini 2026-10-13 (9 marchés, 39 preuves ; 12 pages ouvertes seulement, Sirene en échec en fin de run) |
| 0.1 | chercheur D | lentille 7 dépense mal servie + B2C/produits physiques | marches/malservi-b2c.md | fini 2026-10-13 (10 marchés, 35 preuves, 30 domaines) |
| 0.2 | verificateur | taille/croissance des 8 marchés gardés (23 preuves) | verification.md | fini 2026-10-13 (8 ✔ / 8 ≈ / 1 ✘ / 4 ?) |

Note 2026-10-13 : marches.md écrit (38 marchés, 8 gardés, 30 éliminés avec motif). En attente de la vérification, puis point d'arrêt 1.

## Reprise dans une nouvelle session (sans le contexte de la conversation)

### Décisions déjà prises par l'utilisateur (2026-10-13)
- **Option A** : ne pas lire `ideas/_recherche/`, `ideas/_recherche-v2/`, `ideas/recrutement-garages/`.
- **Profil** : lignes ☐ de `CLAUDE.md` non remplies, lancer avec les hypothèses par défaut (`hypotheses.md`).
  Si l'utilisateur les a remplies depuis, `CLAUDE.md` prime.
- **Mode** : avec points d'arrêt (pas AUTO).
- Prompt suivi : « Le prompt maître v3 » en bas de `relancer-la-recherche-v3.md`, ligne [OPTION A].

### Où on en est
- Phase 0 finie : `marches.md` (38 marchés, 8 gardés, 30 éliminés avec motif) et `verification.md`.
- **Point d'arrêt 1 affiché, réponse de l'utilisateur en attente** : choisir 3 à 5 marchés parmi les 8.
  Recommandation du coordinateur : **A6 (bailleurs F 2028), A2 (tertiaire OPERAT/GTB), A1 (facturation
  électronique), C3 (batteries domestiques)**. Repêchables sous les seuils : D2 obsèques, B4 formation, B6 transmission.
- Prochaine étape après le choix : **phase 1** (segmentation, étape 4 du skill `market-segment-scanner`, puis
  chercheurs par paires de segments sur le Top 12, fichiers dans `signaux/`).

### Leçons de la phase 0 (à donner aux prochains agents)
- Une erreur API « SSL certificate hostname mismatch » a coupé les 4 chercheurs : relancés, ils ont repris
  leur fichier sans perte. En cas de récidive, vérifier VPN/proxy/antivirus.
- API recherche-entreprises : limite de débit (HTTP 429) au-delà de quelques requêtes rapprochées ; espacer
  les appels. Plafond de 10 000 résultats atteint sur la plupart des NAF : découper par département ou effectif.
- Inaccessibles en WebFetch : legifrance (pages vides), ADEME (403), ANIL (refus), impots.gouv (DNS),
  economie.gouv (403), Google Trends (429), PDF de fédérations (illisibles). Service-public.fr fonctionne.
- Les chercheurs paraphrasent souvent des extraits de recherche : exiger des citations verbatim de pages
  ouvertes pour les chiffres décisifs.
- Aucune croissance ≥ 8 % n'a été prouvée avec une source institutionnelle : les marchés passent par le
  « moteur structurel daté ». Les tailles sont bottom-up : la phase 1 doit trouver des prix réellement payés.

### Prompt à coller dans la nouvelle session
> Reprends la recherche v3 là où elle s'est arrêtée. Lis CLAUDE.md, puis ideas/_recherche-v3/etat.md
> (section « Reprise »), marches.md et verification.md. Ne lis pas les fichiers de travail en entier.
> Suis le prompt maître v3 de relancer-la-recherche-v3.md (option A, avec points d'arrêt) à partir de la
> phase 1. Pour le point d'arrêt 1, je garde les marchés : [ex. A6, A2, A1, C3].
