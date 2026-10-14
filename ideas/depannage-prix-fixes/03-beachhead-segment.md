# Premier segment (méthode beachhead-segment)

## Segments candidats

| Segment | Douleur brûlante | Capacité à payer | Part gagnable | Bouche-à-oreille | Total /20 |
|---------|------------------|------------------|---------------|------------------|-----------|
| **Particuliers de Paris 15e, Boulogne-Billancourt, Issy-les-Moulineaux** | 5 : immeubles anciens, urgences fréquentes, fraudeurs actifs dans les grandes villes ([DGCCRF](https://www.economie.gouv.fr/dgccrf/depannage-domicile-gare-aux-arnaques)) | 5 : revenus élevés, prêts à payer pour la confiance [HYPOTHÈSE] | 4 : zone contiguë, trajets courts entre interventions | 4 : gardiens d'immeuble, groupes de voisins | **18** |
| Particuliers de l'est parisien (11e, 12e, 20e) | 5 | 4 | 4 | 4 | 17 |
| Grande couronne pavillonnaire (Essonne) | 4 | 4 | 3 : trajets longs, moins d'interventions par jour | 3 | 14 |
| Bailleurs, syndics et gestionnaires (B2B) | 3 : ils ont déjà des artisans attitrés | 4 | 3 | 4 | 14 : **canal complémentaire** |

## Segment retenu

| Question | Réponse |
|----------|---------|
| **Qui** | Particuliers (locataires et propriétaires) confrontés à une urgence de plomberie ou de serrurerie : fuite, WC ou évier bouché, chasse d'eau, porte claquée ou serrure bloquée. Hors gaz et hors gros travaux |
| **Où** | Paris 15e (75015), Boulogne-Billancourt (92100), Issy-les-Moulineaux (92130) : zone contiguë, dense, beaucoup d'immeubles anciens [HYPOTHÈSE à confirmer par les données d'appels] |
| **Combien** | ~210 000 ménages [HYPOTHÈSE], ~39 000 interventions de plomberie-serrurerie par an (voir [02-market-sizing.md](02-market-sizing.md)) |
| **Côté techniciens** | 697 entreprises de plomberie-chauffage (43.22A) et de serrurerie-menuiserie métallique (43.32B) dans ces trois codes postaux ([API Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/search?activite_principale=43.22A,43.32B&code_postal=75015,92100,92130&etat_administratif=A&per_page=25), 14/10/2026) |
| **Comment les trouver** | Google Ads sur les recherches d'urgence de la zone ; affichettes chez les gardiens et dans les halls avec accord des syndics ; groupes de voisins ; agences de gestion locative de la zone |
| **Pourquoi eux d'abord** | Urgence forte, décision en minutes, un seul décideur ; zone compacte pour 3 à 4 interventions par technicien et par jour |

## Ce qui ferait changer de segment
- Coût par appel entrant au-dessus de 40 € sur Google Ads : passer en priorité au canal B2B (gestionnaires, syndics).
- Moins de 2 interventions par jour et par technicien après 4 semaines : resserrer la zone ou en tester une autre (est parisien).
