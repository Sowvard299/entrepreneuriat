# Index des signaux (phase 1, recherche v2)

Date : 13 octobre 2026. Option A (on repart de zéro). Consignes données aux chercheurs : [signaux/_consignes-communes.md](signaux/_consignes-communes.md).

## Bilan

| Famille | Fichier | Signaux | Domaines distincts (déclarés) | Recherches web |
|---------|---------|---------|-------------------------------|----------------|
| 1. Clients qui paient mais sont mécontents | [01-clients-mecontents.md](signaux/01-clients-mecontents.md) | 28 (dont 3 contre-signaux) | 13 | 5 + ~45 pages ouvertes |
| 2. Services locaux éparpillés sans marque | [02-services-locaux.md](signaux/02-services-locaux.md) | 27 | 26 | 22 |
| 3. Modèles qui marchent ailleurs | [03-modeles-ailleurs.md](signaux/03-modeles-ailleurs.md) | 25 | 29 | 25 |
| 4. Franchises, réseaux, cessions | [04-franchises-cessions.md](signaux/04-franchises-cessions.md) | 30 | 10 | 13 |
| 5. Argent qui circule et cimetière | [05-argent-et-cimetiere.md](signaux/05-argent-et-cimetiere.md) | 26 (19 + 7 échecs) | 22 | 13 |
| 6. Données publiques et timing | [06-donnees-et-timing.md](signaux/06-donnees-et-timing.md) | 27 | 34 | 21 |
| **Total** | | **163** | **135 domaines distincts** (comptage automatique des URL dans les 6 fichiers) | |

Objectif du prompt : au moins 80 sources distinctes et 8 secteurs. Atteint : 135 domaines, plus de 30 secteurs (services à domicile, propreté, immobilier et copropriété, location courte durée, automobile, dépannage, déménagement, seniors, garde d'enfants, animaux, marketing pour TPE, prospection B2B, vidéo, e-commerce, formation, comptabilité et création d'entreprise, énergie, déchets, réparation, vélo, seconde main, restauration, tourisme et puériculture, nuisibles).

## Domaines les plus cités

recherche-entreprises.api.gouv.fr (35 citations, comptes déposés et comptages Sirene), fr.trustpilot.com (30), comeup.com (16), fusacq.com (11), toute-la-franchise.com (10), observatoiredelafranchise.fr (7), franchise-magazine.com (6), economie.gouv.fr (6), puis des sources officielles (service-public, legifrance, insee, ecologie.gouv.fr, open.urssaf.fr, BODACC).

## Limites connues (à garder en tête pour la suite)

1. **Famille 1 trop dépendante de Trustpilot** : 25 signaux sur 28. Les avis Google et ceux des stores d'applications n'ont pas pu être lus. Trustpilot sur-représente les avis sollicités (5 étoiles) et les avis de colère (1 étoile).
2. **Reddit illisible** : WebFetch et navigateur intégré refusés. Aucune plainte Reddit n'est utilisée.
3. **Pappers et Societe.com bloqués (403)** : les CA viennent du champ `finances` de l'API officielle Recherche d'entreprises (mêmes comptes déposés). Un CA à 0 signifie souvent des comptes confidentiels.
4. **Malt, Cessionpme, fichier BMO 2026** : non lus ou lus seulement en extrait de recherche.
5. **Chiffres déclaratifs des franchiseurs** (« CA potentiel après 2 ans ») : promesses, pas des moyennes. Les CA réels de franchisés vérifiés dans l'API sont signalés comme tels et montrent une forte dispersion.
6. Certaines données viennent d'extraits de moteur de recherche (page non ouverte) : c'est indiqué signal par signal.

## Contre-signaux majeurs relevés

- Leaders bien notés : Wecasa (ménage et beauté, 4,7/5 sur 19 164 avis), Shiva (4,8/5 sur 69 385 avis, hébergés sur son site), Acadomia (6 % de 1-2 étoiles), Homebox.
- Cimetière : quick commerce (Getir, Flink, Cajoo), Frichti, Cityscoot, Lavoir Moderne, BnbSitter, Cyclofix, SoyezBCBG, Homejoy. Point commun : actifs lourds ou économie unitaire négative.
- Réglementation qui recule : CSRD pour PME (Omnibus), BACS reporté à 2030, ZFE instable.
- Marketplaces de freelances saturées (20 à 170 réponses par projet sur Codeur), sauf la téléprospection B2B (4 à 6 réponses).
