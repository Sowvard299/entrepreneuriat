# Vérification de la vague agro A1 (porte 1)

- Date : 2026-11-02 | Vérificateur : haiku | Fichiers contrôlés (non modifiés) : agro-pme-travail.md, agro-restauration-travail.md, agro-reprise-travail.md
- Méthode : API Sirene (curl) pour les comptages ; WebFetch sur l'URL du fichier, puis sur une page publique du même éditeur quand la première était en 403 ou injoignable.

| ID | fichier | URL | verdict | note courte |
|----|---------|-----|---------|-------------|
| P1 | agro-pme | https://www.haccpaipro.com/ (capterra en 403) | ≈ | 19 € confirmé, mais la page dit « Starter à 19€/mois pour un établissement », pas « à partir de ». Clients payants non vus. |
| P2 | agro-pme | https://melba.io/fr/tarifs (lafabriquedunet en 403) | ✔ | 49 € HT (Simple) et 99 € HT (Premium) par mois, sur la page tarifs de l'éditeur. |
| P3 | agro-pme | https://www.epackpro.com/ (epackpro.fr injoignable) | ✘ | « 119 € HT par mois sur tablette » absent. Accueil tronqué, aucune page tarifs trouvée. |
| P4 | agro-pme | aidopms.com (domaine inexistant), vici.fr (domaine à vendre), lafabriquedunet en 403 | ? | Éditeur introuvable ; 29,99 € HT non vérifié. |
| A1 | agro-pme | API recherche-entreprises, codes 10.51C, 10.51A, 10.13A/B, 10.11Z, 10.72Z, 10.85Z, 10.89Z, 10.39B, 11.05Z, 11.02A/B, 11.03Z, 11.04Z | ✔ | Totaux exacts (ex. 10.51C = 919 ; 10.72Z = 4 571 ; 11.05Z = 2 919). Non revérifié : « dont 561 avec 1+ salarié ». |
| A2 | agro-pme | https://www.em-lyon.com/en/node/457 | ≈ | 18 000 entreprises, 98 % TPE/PME, 380 000 ETP, 167 Md€ : exacts. Document publié le 5 avril 2019 (mis à jour 2026) ; le fichier dit « date inconnue ». |
| F1 | agro-pme | https://www.appvizer.fr/biens/tracabilite-alimentaire | ✔ | HACCP Now 4,6/5 sur 7 avis ; Cashmere et Date Check Pro : aucun avis. « Tarif sur demande » est un libellé, pas une phrase. |
| F2 | agro-pme | https://www.logiciels.pro/comparateur-logiciels-pour-brasserie/ | ✔ | Phrase exacte : « Très puissant techniquement, il reste cependant limité sur la partie commerciale et douanière française. » Comparateur, confiance faible. |
| C1 | agro-pme | https://www.lhotellerie-restauration.fr/... (getapp en 403) | ≈ | Titre exact (réponse du 30 nov. 2022), mais le contenu dit l'inverse : « il n'existe pas, à ma connaissance, de logiciel gratuit permettant l'étiquetage des produits ». |
| P8 | agro-pme | https://foodlabelmaker.com/fr-ca/ ; getapp.co.nz en 403 ; resto-couts.fr injoignable | ✘ | Aucun montant 49 $ / 99 $ CAD sur la page lue (prix probablement absents ou rendus en JS). 29 €/mois (Resto Couts) non vérifié. |
| E01 | agro-restauration | https://koust.net/tarifs (lafabriquedunet en 403) | ✔ | Essentiel 80 €/mois/site (engagement annuel), 90 € en mensuel ; Professionnel 130 € ; Entreprise 180 €. |
| E02 | agro-restauration | https://melba.io/fr/tarifs ; appvizer.fr/operations/erp/melba | ≈ | Melba 49 / 99 € HT/mois confirmés. Appvizer parle « par utilisateur » et « Pro » ; l'éditeur ne donne « par utilisateur » que pour le module Core (15 €). Inpulse 159 € HT non vérifié. |
| E03 | agro-restauration | getapp.fr/software/2097488/ratiochef (403) ; capterra Ratatool (403) ; ratatool.fr injoignable ; ratiochef.com introuvable | ? | Aucun éditeur accessible ; 29 €/mois et « gratuit » non vérifiés. |
| E04 | agro-restauration | API recherche-entreprises, 56.10A | ✔ | total_results = 10 000 : c'est le plafond de l'API, donc un plancher (« plus de 10 000 »). |
| E05 | agro-restauration | https://kolonell.com/fr/blog/logiciel-cuisine-centrale-restauration-collective-lyon-2026 | ✔ | « Paramétrage figé, frais par site » (ligne offre complète) ; 200-350 et 400-600 € HT/mois ; 30 000-60 000 € en sur mesure ; publié le 8 oct. 2026. Source intéressée (vend du sur mesure). |
| E06 | agro-restauration | API 56.29A, 56.29B, 87.10A | ✔ | 556 ; 4 391 ; 3 195 exacts. Unités légales, pas sites. |
| E07 | agro-restauration | https://www.maire-info.com/restauration-scolaire/... | ✔ | 31,1 % durables, 12,1 % bio, près de 50 000 cantines (59 % des sites, +47 %), « plus de 90 000 cantines » : exacts. Article du 29 oct. 2026. |
| E08 | agro-restauration | https://agriculture.gouv.fr/telecharger/152514 | ? | PDF compressé illisible. 29,5 %, 11,8 %, 35 % et 30 % non vérifiés ; année des achats non lue. |
| V1 | agro-reprise | API recherche-entreprises, q=nutrimuscle | ≈ | N LAB (SIREN 845402494) : CA 2025 43 744 015 € et résultat 2 871 193 € exacts. Mais NAF 70.10Z (sièges sociaux) et lien N LAB = Nutrimuscle non établi (site éditeur bloqué 429, mentions légales 404). |
| V2 | agro-reprise | API recherche-entreprises, q=nutripure | ✔ | Nutripure (SIREN 833372212) : CA 2022 11 658 408 € et résultat 1 344 719 € exacts. Donnée de 2022 (4 ans). |

## Bilan

1. agro-pme-travail.md (10 vérifiées) : ✔ 4, ≈ 3, ✘ 2, ? 1. Taux ✘ + ≈ = 5/10 (50 %), soit 5/9 (56 %) hors ?.
2. agro-restauration-travail.md (8 vérifiées) : ✔ 5, ≈ 1, ✘ 0, ? 2. Taux ✘ + ≈ = 1/8 (12,5 %), soit 1/6 (17 %) hors ?.
3. agro-reprise-travail.md (2 vérifiées) : ✔ 1, ≈ 1, ✘ 0, ? 0. Taux ✘ + ≈ = 1/2 (50 %) ; échantillon trop petit pour conclure.
4. Chiffres à déclasser (non vérifiés ou faux) : P3 119 € HT/mois (✘) ; P4 29,99 € HT/mois (?) ; P8 29 €/mois et 49/99 $ CAD (✘ / ?) ; C1 « le gratuit suffit » (contredit par sa propre source) ; E02 Inpulse 159 € HT/site/mois et « par utilisateur » Melba ; E03 29 €/mois Ratatool et « gratuit » RatioChef (?) ; E08 29,5 %, 11,8 %, 35 %, 30 % (?, remplacés par E07 ✔ 31,1 % / 12,1 %) ; V1 attribution du CA à « Nutrimuscle » (chiffre exact, marque non établie). A2 : garder le chiffre, mais la date est 2019, pas « inconnue ».
5. Conséquence pour la porte 1 : après vérification, l'agro-PME n'a que 2 prix publics confirmés (P1 à 19 € et P2 à 49/99 € HT). Le seuil « 3 prix publics payés » n'est pas atteint sur ce fichier sans P3 ou P4. Aucun prix payé effectif (clients payants) n'est établi dans les deux fichiers.
