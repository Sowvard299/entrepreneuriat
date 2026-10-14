# Porte 1 sur les 12 segments : tri avec les seules preuves déjà dans le dépôt

Date : 2026-10-14. **Aucune nouvelle recherche web, aucun agent.** Sources lues : `ideas/_recherche-v3/segments.md`,
les synthèses `marches/obligation-transition-synthese.md`, `marches/ailleurs-demande-synthese.md`,
`signaux/p1-factur-ec-btp-synthese.md`, `verification.md`, et la fiche A6 de `marches/obligation-transition.md` (Grep).
Pourquoi sans recherche : la porte 0 n'est pas passée (profil vide, 0 conversation), et `CLAUDE.md` dit « Sinon,
pas de recherche » ; la règle de budget impose aussi de lire l'usage du forfait avant toute vague.

Critère de la porte 1 (`CLAUDE.md`) : ≥ 3 prix publics réellement payés par le segment ; concurrents et faiblesses ;
croyance la plus fragile (format `before-you-build`). Décision : passe / à revoir / élimine.

| Rang v3 | Segment | Prix payés connus (preuve) | Concurrents, faiblesse | Croyance la plus fragile → test qui la lève | Décision |
|---|---|---|---|---|---|
| 1 | A1-S2 cabinets d'expertise comptable, migration en marque blanche | 0 prix payé ; 800-2 000 € annoncés sur une page sponsorisée (P1-21) | Cegid/Shine, Sage, Tiime, Indy offrent PA et mandat, souvent gratuits (P1-6, P1-7, P1-22) ; en Belgique comptable + éditeur ont suffi (P1-25) | « un cabinet paiera un tiers pour ce que son éditeur donne » → 5 appels à des cabinets : ont-ils déjà payé un prestataire pour ça ? | **élimine** (angle migration ponctuelle : recherche P1 faite, aucun achat prouvé en France, Italie, Belgique). L'angle « suivi récurrent vendu via les cabinets » devient une nouvelle piste à présenter à la porte 1 |
| 3 | A1-S1 TPE du bâtiment sur Word/Excel | 2 prix avec clients payants : Tolteck 228 €/an, CA 2025 6,79 M€ (P1-15) ; Obat 39-129 €/mois HT (P1-4), 21 000 clients (C4) ; 3e (EBP via CAPEB, -25 %, P1-18) sans prix lu | leaders notés 4,5/5 (696 avis) et 4,9/5 (961 avis) (P1-9, P1-17) : faiblesse non prouvée ; CAPEB et FFB déjà partenaires | « une TPE paiera un nouveau venu plutôt que l'outil gratuit ou le partenaire de sa fédération » → seul angle restant : voie distribution (revendre ou apporter Tolteck/Obat, commission) ; demander les conditions de leurs programmes partenaires | **à revoir** : l'argent circule pour le logiciel, mais rien ne prouve une faiblesse des acteurs ; à rouvrir seulement comme piste de distribution |
| 2 | A6-S2 SCI familiales 3-10 logements avec un F | 0 (panier 1 500-5 000 € [HYPOTHÈSE]) | non étudiés | « une SCI paie un coordinateur au lieu d'aller en direct chez l'artisan ou son comptable » → 3 prix d'accompagnement payés + agrément « Mon Accompagnateur Rénov' » requis ou non | **à revoir** (aucune preuve) |
| 6 | A6-S8 LMNP via CGP et comptables | 0 | non étudiés | « les CGP recommandent un tiers payant pour la mise aux normes » → prix d'un apport d'affaires CGP | **à revoir** (aucune preuve) |
| 9 | A6-S1 bailleurs 1-2 F en Île-de-France | DPE 100-250 € (segments.md, non sourcé ; diagnostic réservé à un certifié) ; aucun prix d'accompagnement | non étudiés | « le bailleur achète autre chose qu'un DPE et des devis directs » → 3 prix d'accompagnement payés | **à revoir** (aucune preuve) |
| 10 | A6-S9 bailleurs non-résidents | 0 | non étudiés | « l'expatrié paie plus cher pour tout déléguer » → prix d'offres de gestion à distance existantes | **à revoir** (aucune preuve) |
| 11 | A6-S10 petites foncières 10-50 logements | 0 (15 000 € [HYPOTHÈSE]) | non étudiés | « elles n'ont pas déjà un maître d'œuvre ou un bureau d'études » → 3 contrats publics | **à revoir** (aucune preuve) |
| 4 | C3-S2 installateurs RGE qui achètent des contacts batteries | 0 prix de contact lu | plateformes de génération de contacts déjà présentes (segments.md, sans ID) ; solaire résidentiel -26 % (C3-p3) | « un installateur paie des contacts batterie alors que son marché recule » → 3 grilles de prix de contacts PV/batterie payées | **à revoir** (aucune preuve) |
| 5 | C3-S6 commerces et artisans avec panneaux | 0 ; prix batterie 3 500-15 000 € côté particulier seulement (C3-p5 corrigé) | non étudiés | « 20 000 [HYPOTHÈSE] sites existent et achètent une batterie B2B » → comptage + 3 devis payés | **à revoir** (aucune preuve) |
| 12 | C3-S10 autoconsommation collective | 0 | non étudiés | « une copropriété ou un lotissement paie un organisateur » → 3 opérations avec prix | **à revoir** (aucune preuve) |
| 7 | A1-S5 PME 10-49 sur logiciel ancien | 0 | non étudiés ; P1 montre que les éditeurs donnent la PA (P1-6, P1-7) | « la PME migre avec un tiers et non avec son revendeur actuel » → 3 prix de migration payés à des intégrateurs | **à revoir**, avec un a priori négatif (même mécanisme que A1-S2) |
| 8 | A1-S7 négoces et grossistes B2B | 0 | idem | idem | **à revoir**, a priori négatif |

## Bilan

- **1 élimine, 11 à revoir, 0 passe.** Les preuves existantes ne suffisent à faire passer aucun segment : 10 des 12 n'ont
  jamais eu de recherche de prix (la v3 s'est arrêtée après la paire P1).
- Les 12 viennent de 4 marchés de conformité choisis sans décision de l'utilisateur (`ideas/_recherche-v3/etat.md`),
  le biais n° 2 de l'audit. A1 cumule : P1 a montré que l'argent va aux abonnements gratuits ou bon marché des éditeurs.
- **Porte 2 : non commencée pour les 12.** Elle exige 10 contacts réels par segment et un seuil écrit avant les appels ;
  aucun agent ne peut la faire. Elle ne s'ouvre qu'aux segments qui passent la porte 1.

## Si l'équipe décide quand même de lancer la vraie porte 1 avant la porte 0

Coût estimé : 5 « chercheur » (paires A6-S2+S8, A6-S1+S9, A6-S10+C3-S10, C3-S2+S6, A1-S5+S7), 12 recherches web
chacun, plus 1 « verificateur », en 2 vagues. Je propose de retirer d'abord A1-S5 et A1-S7 (a priori négatif) : 4 chercheurs,
une seule vague. Pré-requis de `CLAUDE.md` : lire l'usage du forfait avant la vague.
