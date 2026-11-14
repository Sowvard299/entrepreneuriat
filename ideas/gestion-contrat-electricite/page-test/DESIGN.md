# DESIGN.md : Contrat Juste (page de test, porte 2)

## Direction
Sobre et factuelle, « service public bien fait ». On demande un mandat et 19 € : chaque phrase doit être
vérifiable. Le visuel principal est un vrai calculateur, pas une image. Références d'esprit : energie-info.fr
(clarté), GOV.UK (hiérarchie simple). Réglages : variation 4, mouvement 2, densité 4.

## Couleurs (variables CSS dans styles.css, rien en dur)
| Rôle | Clair | Sombre |
|------|-------|--------|
| Fond | #f6f7f8 | #121417 |
| Surface (calculateur, commande) | #ffffff | #1b1e23 |
| Texte | #16191d | #e9ecef |
| Texte secondaire | #4a525c | #a9b1bb |
| Bordure | #d9dde2 | #2e333a |
| Accent (boutons, chiffres clés) | #0f6b47 | #4cc38a |
| Texte sur accent | #ffffff | #0b1a12 |

Une seule couleur d'accent, un vert sobre (économie), sur toute la page. Pas de dégradé.

## Typographie
Une seule famille : la police système (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`), rapide et
neutre, aucun téléchargement. Chiffres en `font-variant-numeric: tabular-nums`.
Échelle : 14 / 16 / 18 / 22 / 30 / 44 px. Graisses : 400 et 650.

## Formes et espacements
Un seul rayon : 6 px (boutons, champs, blocs). Grille de 8 px. Largeur max 1080 px, texte 65 caractères.
Un bouton principal (fond accent) et un secondaire (bordure). Pas d'ombre portée.

## Icônes
Aucune. Les listes sont numérotées par le texte, pas par des pictos. Zéro emoji.

## Mouvement
Uniquement le retour au survol et à l'appui des boutons, et l'ouverture des questions. Rien au défilement.
Coupé sous `prefers-reduced-motion`.

## Ton
Vouvoiement. Phrases courtes. Pas de tiret long. Chaque chiffre a sa source ou est marqué « estimation ».
Mots interdits : révolutionner, libérer, transformer, intelligent, sans effort, le meilleur.
On dit clairement que le service n'existe pas encore, et à qui il ne sert à rien.
