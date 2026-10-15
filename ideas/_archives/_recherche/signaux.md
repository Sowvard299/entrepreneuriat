# Signaux bruts : phase 1

Collecte lancée le 2026-10-12 par 8 chercheurs en parallèle, un par famille de sources.
Les signaux eux-mêmes sont dans `signaux/` (un fichier par famille, écrit au fil de l'eau).
Ce fichier sert d'index et de bilan ; il est complété à la fin de la phase 1.

## Fichiers

| # | Famille | Fichier | Préfixe |
|---|---------|---------|---------|
| 1 | Frustrations du grand public (Reddit, forums, avis 1-2 étoiles) | [signaux/01-grand-public.md](signaux/01-grand-public.md) | GP |
| 2a | Pros de terrain (artisans, CHR, commerces, e-commerce) | [signaux/02-pros-terrain.md](signaux/02-pros-terrain.md) | PT |
| 2b | Pros spécialisés (agri, libéraux de santé, immo, copro, assos, PME) | [signaux/03-pros-specialises.md](signaux/03-pros-specialises.md) | PS |
| 3a | Argent qui circule (Malt, Codeur, Fiverr, Indie Hackers, YC, levées FR) | [signaux/04-argent-qui-circule.md](signaux/04-argent-qui-circule.md) | AR |
| 3b | Modèles étrangers absents de France | [signaux/05-modeles-etrangers.md](signaux/05-modeles-etrangers.md) | ET |
| 4 | Timing (réglementation 2025-2028, tendances, démographie) | [signaux/06-timing-reglementation.md](signaux/06-timing-reglementation.md) | TM |
| 5 | Cimetière (startups fermées) | [signaux/07-cimetiere.md](signaux/07-cimetiere.md) | CI |
| 6 | Données publiques (dimensionnement) | [signaux/08-donnees-publiques.md](signaux/08-donnees-publiques.md) | DP |

## Format d'un signal

```
### <PRÉFIXE>-01 · <secteur> · <B2C|B2B|B2B2C> · <type de signal> (force N)
- **Problème** : une ligne, concrète
- **Qui** : cible précise
- **Source** : <site> : <URL précise>
- **Date** : AAAA-MM-JJ
- **Citation** : « 15 mots maximum »
- **Note** : contexte, chiffre sourcé, prix payé, contradiction, solution utilisée aujourd'hui
```

## Force des signaux

| Type | Force |
|------|-------|
| Argent déjà dépensé | 4 |
| Recherche active d'une solution | 3 |
| Obligation réglementaire | 3 (voir hypothèse H9) |
| Plainte | 2 |
| Tendance | 1 |
| Échec (cimetière) | 0 : sert d'avertissement, pas de preuve de douleur |

Marqueurs : `[HYPOTHÈSE]` chiffre non sourcé, `[CONTRADICTION]` source qui va contre un problème,
`[ANCIENNE]` source de plus de 24 mois, `[paraphrase]` texte non recopié mot pour mot.

## Bilan de la phase 1 (2026-10-12)

| Famille | Signaux | Remarque |
|---------|---------|----------|
| 1. Grand public | 24 | Trustpilot, Custplace, forum Que Choisir, Services Publics+, App Store, Assemblée nationale |
| 2a. Pros de terrain | 19 | CAPEB, Batiweb, presse pro, Codeur, Assemblée nationale |
| 2b. Pros spécialisés | 28 | Terre-net, Réussir, Cerfrance, FNO, CSMF, Fédésap, DREAL, Recherches & Solidarités |
| 3a. Argent qui circule | 26 | Codeur (11 signaux), TrustMRR, YC, FrenchWeb, Maddyness |
| 3b. Modèles étrangers | 22 | franchises et services américains et britanniques, avec recherche d'un équivalent français |
| 4. Timing | 27 | sources officielles (Légifrance, service-public, EUR-Lex, INSEE) + calendrier 2025-2028 |
| 5. Cimetière | 25 | Failory, CB Insights, FrenchWeb, Maddyness, TechCrunch |
| 6. Données publiques | 9 signaux + 111 chiffres | INSEE, Banque de France, DREES, CNSA, FFB, CAPEB, UNEC, MSA, FACCO, OBSA |
| **Total** | **180 signaux** | **302 URL distinctes, 176 sites distincts** |

Répartition par force : 24 signaux de force 4 (argent dépensé), 66 de force 3 (obligation, recherche active ou argent dépensé à l'étranger), 40 de force 2 (plainte), 25 de force 1 (tendance), 25 cas d'échec (force 0).

Secteurs couverts (plus de 20) : logement et copropriété, rénovation énergétique, bâtiment, restauration et hôtellerie, commerce de proximité, e-commerce, coiffure, automobile et auto-écoles, agriculture et viticulture, santé libérale, aide à domicile et EHPAD, seniors et aidants, petite enfance, éducation, animaux, associations et sport, tourisme et location courte durée, services aux PME (facturation, recouvrement, RSE, IA), mobilité, alimentation, seconde main, obsèques et succession.
Types de produits couverts : logiciels, services, prestations outillées, produits physiques (D2C, alimentation animale, scooters), abonnements, marketplaces, franchises.

### Limites de la collecte (à connaître avant de lire la suite)

- **Quota de recherche web épuisé à mi-parcours** : les 8 chercheurs partageaient un quota de recherches. Après épuisement, ils ont seulement ouvert des pages déjà repérées ou des sites officiels. Plusieurs pistes de la liste de départ n'ont donc pas été vérifiées (voir la fin de chaque fichier).
- **Reddit, LinkedIn, Malt, Upwork, Indie Hackers : peu ou pas couverts** (pages bloquées en 403 ou pas de résultats). Les frustrations du grand public viennent surtout de Trustpilot, Custplace, du forum Que Choisir et de Services Publics+. Reddit est réutilisé de façon ciblée en phase 4 sur les idées finalistes.
- **Pas de données Google Trends, Exploding Topics ni TikTok** : les tendances viennent de l'INSEE, de la DREES et de la presse.
- Certaines citations sont « vérifiées via extrait de recherche » (page non ouverte) ; elles sont signalées dans les notes.
- Beaucoup de chiffres viennent d'acteurs intéressés (éditeurs, franchiseurs, prestataires) ; ils sont signalés comme tels.
