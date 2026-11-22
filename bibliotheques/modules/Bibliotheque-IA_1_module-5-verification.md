# Bibliothèque IA 1 — module « Vérification et livraison » — v1

Édition du 22 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale et de sections de la Bibliothèque IA 2 par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : contrôles sur le rendu, grille de relecture, rapport de conformité, partie enseignant·e, repli sans Word.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# ÉTAPE 0 — LE CONTRAT

## 0.5 Si l'outil ne peut pas produire un fichier .docx structuré

Si l'IA ne peut pas créer de tableaux, de hauteurs de ligne exactes ou de tabulations dans un vrai fichier .docx, elle DOIT **le dire avant de produire**. Elle livre alors :

1. le cadrage et la fiche technique complète (Étapes 1 et 2) ;
2. le contenu de la fiche, balisé rôle par rôle (`[CONSIGNE]`, `[DONNÉES]`, `[ZONE : 2 lignes de 16 cm]`, `[SAUT DE PAGE]`) ;
3. la liste des réglages à appliquer dans Word (Étape 4) ;
4. la mention explicite : « Mise en page à réaliser ; ce texte n'est pas une ressource prête à imprimer. »

Elle ne présente jamais un texte avec des tirets bas comme une fiche prête à imprimer.


# ÉTAPE 4 — CONSTRUIRE : STYLES ET RECETTES TECHNIQUES

## 4.3 Partie enseignant·e : structure fixe

La partie enseignant·e est un fichier séparé. Elle DOIT contenir, dans cet ordre :

1. **En bref** : objectif, indices de réussite, moment de la séquence, durée, matériel, avec une solution de rechange pour ce qui pourrait manquer (par exemple, sans dé : la roue de tirage J20 ; sans jetons : des cases à cocher).
2. **Choix pédagogiques** : codes F, P, MF, G mobilisés, en une ligne chacun.
3. **Ancrage PER** : texte consulté et date, ou **[À VÉRIFIER dans le PER]** ; constat d'adéquation (§ 1.2).
4. **Hypothèses annoncées** (§ 1.1).
5. **Déroulement conseillé** (par exemple lancement oral 5 min, travail 20 min, mise en commun 5 min).
6. **Différenciation** : dispositif (MP-D-02), attribution, extension éventuelle ; pour une classe multi-âges, l'entrée de chaque degré ou niveau (MP-D-05).
7. **Corrigé expliqué** : réponse et « Pourquoi » pour chaque item ; quand la tâche admet plusieurs réponses, toutes les réponses acceptables (l'unicité reste exigée pour les jeux d'appariement, MP-J-01).
8. **Barème indicatif** ou grille formative sans note.
9. **Erreurs typiques** : erreur → hypothèse → rétroaction actionnable → tâche de reprise.
10. **Ticket de sortie et décision** (MF44) : résultat → suite proposée.
11. **Rapport de conformité** (Étape 5).
12. **Statut des informations** : vérifié dans la session / non vérifié / inférence de conception.

**Pour un jeu (GF-F)**, la partie enseignant·e ajoute :

- dans « En bref », un **tableau d'impression** : page, contenu, quantité, papier, découpe ; Sous le tableau, des **astuces pratiques** : faire lancer le dé dans une boîte ou un couvercle (ou dé en mousse, tapis de feutrine) ; cacher la réponse des cartes question-réponse (pochette, rabat, carte tenue par le camarade qui interroge) ; un sablier par groupe ; un sachet étiqueté par jeu, avec la règle et le corrigé ; un essai recto-verso sur une seule feuille ; le jeu laissé en libre accès après la séance.
- dans « En bref », **ce qui fait apprendre** dans ce jeu, en une ou deux phrases, en partant de la ligne « Fait apprendre si… / N'apprend rien si… » de sa section : le mécanisme qui fait travailler l'objectif (rappel actif, retour immédiat, nombre de réponses par élève et par partie, verbalisation), et ce qui ferait perdre l'apprentissage (attente, hasard dominant, réponse visible) ;
- dans « Déroulement conseillé », une **mise en commun** après la partie : ce qu'on a appris, les erreurs fréquentes, la règle ou la procédure à retenir ;
- dans « Corrigé expliqué », la **solution du jeu** (ordre de la boucle, paires ou familles), avec un « Pourquoi » pour chaque pièce ;
- dans « Différenciation », les **variantes de jeu** : solo, à trois, mélange des lots ; Pour tout jeu de parcours ou de compétition, proposer aussi une **variante coopérative**, fondée sur l'interdépendance positive et la responsabilité individuelle (Johnson & Johnson, 2009) : un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance seul ; un but commun chiffré (tous les pions arrivés en moins de dix tours, vingt cartes réussies) ; des rôles tournants (J13) ; l'aide qui rapporte (si l'explication d'un camarade permet de répondre, les deux avancent) ; l'erreur sans recul (le groupe explique, puis l'élève rejoue) ; des binômes par pion ; un bilan de fin de partie (« qu'est-ce qui nous a aidés ? »).
- dans le rapport de conformité, les contrôles **V11 à V13** (et V14 si le fichier est produit par du code ; V15 à V19 selon le gabarit ; V20 et V21 toujours).

**Pour un jeu ou une dictée**, la partie enseignant·e est une page à part entière, jamais oubliée (V21) : pour un jeu, la règle complète, la solution et le débriefing ; pour une dictée (G20), le texte à dicter en entier. La règle destinée aux élèves est imprimée avec le matériel, en étapes numérotées (MP-J-07), en planche A5 si elle tient sur une demi-page (R15). Avant le test en classe, elle renvoie à la grille « utile, utilisable, acceptable » (Tricot et al., 2003 ; Bibliothèque IA 2).

# ÉTAPE 5 — VÉRIFIER SUR LE RENDU

## 5.1 Obligation (MP-V-01)

La vérification porte sur **ce qui s'imprimera**, pas sur le texte du fichier. L'IA DOIT convertir la fiche en PDF (ou en afficher l'aperçu avant impression) et examiner **chaque page**. Si elle ne peut pas produire ou regarder ce rendu, elle DOIT écrire dans le rapport : « Rendu non contrôlé », puis donner à l'enseignant·e la liste des contrôles du § 5.2 (V1 à V10 pour une fiche ; V11 à V13 en plus pour un jeu), réalisables en quelques minutes sur l'aperçu avant impression.

Lors des essais qui ont conduit à cette version, un audit fondé sur le seul texte du fichier avait estimé une fiche conforme à environ 80 %. Le rendu PDF montrait pourtant quatre pages au lieu de deux, deux exercices coupés et des lignes d'écriture fusionnées.

## 5.2 Contrôle visuel en dix points, et contrôles complémentaires V11 à V21

| N° | Contrôle | Référence |
|---|---|---|
| V1 | Le nombre de pages est celui de la fiche technique ; aucune page remplie partiellement (mesure : V20). | MP-O-11, MP-O-14 |
| V2 | Aucun exercice, consigne, tableau ou encadré n'est coupé entre deux pages. | X-03, MP-O-06 |
| V3 | Chaque zone d'écriture affiche **le nombre de lignes prévu**, à la hauteur prévue. | X-02, MP-E-10 |
| V4 | Chaque lacune a la longueur prévue (comparer à la largeur de la page : 6 cm ≈ un peu plus d'un tiers de la ligne). | MP-E-11, X-10 |
| V5 | Le texte lu par l'élève a la taille du degré ; une seule police. | MP-T |
| V6 | Symboles et cases lisibles et de taille homogène ; aucune information portée par la seule couleur. | R6, MP-C-02 |
| V7 | Rien d'essentiel près des bords ; lignes et tableaux dans la largeur utile. | MP-F-04, MP-F-06 |
| V8 | Aucune trace de la partie enseignant·e (corrigé, barème, niveaux) sur la fiche élève. | X-05, X-11 |
| V9 | En-tête dans l'ordre : Prénom et Date tout en haut, puis titre centré avec un espace avant et après, puis objectif en langage élève, sans étiquette « Mon objectif ». | X-14, MP-O-12 |
| V10 | Relecture orthographique de tout le texte élève : aucune forme fautive ou inexistante, ni dans les consignes, ni dans les exemples, items, distracteurs, banques de mots ou textes d'images ; si l'enseignant·e a demandé une analyse d'erreurs (§ 3.7), chaque forme fautive est marquée, corrigée et justifiée, une seule fois, et les quatre conditions sont vérifiées. | X-13, MP-CC-11, MP-I-05 |
| V11 | **Jeu — unicité et fermeture** : chaque question a une seule réponse dans le lot ; la boucle se ferme (ou chaque paire, chaque famille est complète). Contrôle par programme (Annexe I-C) ou à la main, pièce par pièce. | MP-J-01, X-15 |
| V12 | **Jeu — pièces** : dimensions prévues ; aucune pièce coupée entre deux pages ; traits de coupe (pointillés) distincts des séparations internes (trait plein épais) ; ordre d'impression mélangé ; chaque case d'accueil dépasse la pièce mobile d'au moins 0,5 cm par côté (`verifier_case_piece`) ; la planche occupe toute la surface utile, texte et images centrés ; repères de coupe présents au bord de la feuille pour chaque ligne de coupe. | R8, MP-J-03, MP-J-05, MP-J-10, MP-J-11, MP-J-12 |
| V13 | **Jeu recto-verso** : alignement du recto et du verso contrôlé sur une impression test (le PDF ne suffit pas), si le jeu est imprimé recto-verso. | J4 |
| V14 | **Schéma** : validation OOXML du fichier quand il est produit par du code (facultatif, mais recommandé). | Annexe I-C |
| V15 | **Cursive** : GE Typo Libre est incorporée au PDF ; aucun point médian ; aucune écriture liée en image générée. | R10, MP-CC-11 |
| V16 | **Tracé** : largeur du couloir conforme ; deux portions non voisines séparées d'au moins la largeur + 2 mm ; labyrinthe à chemin unique ; aucun angle vif. | R11, G19 |
| V17 | **Affiche** : corps de la table 2.5 ; au plus six étapes ; lecture réelle depuis la place la plus éloignée ; impression à 100 %. | R9, GF-V |
| V18 | **Montage** : chaque texte tient dans sa fenêtre (calcul), puis un exemplaire est réellement monté et manipulé avant la classe. | R11, J11, J6 |
| V19 | **Combinatoire** : fréquence exacte de chaque élément, aucun doublon, cartes toutes différentes ; un seul symbole commun par paire de cartes. | R13, J7, J8 |
| V20 | **Page pleine** : sur le rendu, chaque page élève atteint au moins 90 % du budget de hauteur (position du dernier élément visible, mesurée sur l'image de la page ; `verifier_remplissage`) et ne déborde pas ; sinon aérer, compléter ou passer en planche A5. Exceptions déclarées : partie enseignant·e, dernière planche d'un jeu à nombre de pièces fixé. | MP-O-14, R15 |
| V21 | **Cohérence didactique** : chaque mot contient le graphème étudié (`verifier_graphemes`) ; chaque réponse d'énigme est calculée et vaut un chiffre de 0 à 9 (`verifier_code`) ; aucune case d'autoévaluation ou de réussite pré-remplie ; chaque question a sa zone de réponse ; un schéma correspond au texte qui le commente ; la consigne d'une grille croisée indique le sens de lecture ; les termes grammaticaux sont complets ; la partie enseignant·e accompagne tout jeu (règle, solution, débriefing) et toute dictée (texte à dicter) ; nombres et notions adaptés à la progression du degré. | MP-CC-11, MP-J-01, MP-P-09 |

V1 à V10 et V12 se contrôlent sur le PDF ou l'aperçu ; V11 sur les données du jeu ; V13 sur papier ; V14 avec un validateur ; V15 sur le PDF ; V16 et V19 par calcul ; V17 dans la classe ; V18 par calcul, puis à la main ; V20 sur le PDF, par mesure ; V21 sur les données et le texte, avant la mise en page, puis sur le PDF.

## 5.3 Grille de relecture courte

À appliquer après le contrôle visuel, avant chaque livraison.

| N° | Question | Référence |
|---|---|---|
| 1 | Public, contexte d'usage et objectif identifiés ; hypothèses annoncées ; adéquation PER examinée ? | Étape 1, MP-P-09 |
| 2 | Fiche technique produite ; budget ≤ 22 cm par page respecté ? | Étape 2, MP-O-11 |
| 3 | A4, marges de 2,5 cm, largeur utile de 16 cm ? | MP-F-01 à MP-F-06 |
| 4 | Une police, taille conforme au degré, texte aligné à gauche, pas de majuscules continues ? | MP-T |
| 5 | Structure numéro → consigne → données → réponse identique ; un rôle, un style ? | MP-O-01, MP-O-09, MP-S-01 |
| 6 | Consignes directes, courtes, sans titre, sans négation, une action par phrase ? | MP-CO-01 à MP-CO-05 |
| 7 | Zones d'écriture construites avec R1 (jamais de tirets bas pour une phrase), en nombre suffisant ? | MP-E-05, MP-E-10, X-01, X-02 |
| 8 | Lacunes calibrées (R2) et cohérentes avec la réponse attendue ? | MP-E-11, MP-CO-07 |
| 9 | 3-5 exercices courts ou 1-2 longs par page ; au plus 4 éléments principaux par exercice ? | MP-O-04, MP-CI-02 |
| 10 | Exemple résolu pour toute tâche nouvelle ; aides placées au-dessus de l'exercice ; pré-training ≤ ¼ de page ? | MP-CC-04, MP-CC-06, MP-PT |
| 11 | Différenciation sans étiquette évaluative ; chaque version dans son budget ; en classe multi-âges, une entrée par degré ou niveau, sans repère visible ? | MP-D-01, MP-D-03, MP-D-05 |
| 12 | Partie enseignant·e séparée et complète (structure § 4.3) ? | Étape 4 |
| 13 | Contrôle visuel V1-V10 effectué (ou impossibilité déclarée) ; V20 (page pleine) et V21 (cohérence didactique) ; pour un jeu, V11 à V13 ; pour un fichier produit par du code, V14 ? | MP-V-01, MP-O-14 |
| 14 | En-tête conforme : Prénom et Date en première ligne, titre centré entre deux espaces, objectif en langage élève sans étiquette ? | MP-O-12, R7 |
| 15 | Aucune forme écrite fautive ou inexistante montrée à l'élève, y compris dans les exercices de jugement, hors analyse d'erreurs demandée et conforme aux quatre conditions du § 3.7 ? | MP-CC-11, X-13 |
| 16 | Jeu : une seule pièce correcte par question, aucun indice non visé, ordre mélangé, autocorrection intégrée, règle en étapes avec un exemple hors lot, qui dit qui commence, la disposition, qui vérifie et ce que fait l'élève qui s'est trompé ; réponse écrite ou épelée quand l'exactitude ne s'entend pas ; modalité adaptée à la notion, cases d'accueil plus grandes que les pièces mobiles ? | MP-J-01 à MP-J-08, MP-J-10, X-15 à X-17 |
| 17 | Contextes, rôles et récompenses sans stéréotype et compatibles avec les valeurs de l'école (pas de rôle de voleur pour s'exercer à la soustraction) ; matériel sobre : pas plus de pages, de couleur ni de plastification que l'apprentissage n'en demande ? | Annexe I-B |

La grille détaillée (audit ou transformation d'une fiche existante) figure en Annexe I-B.

## 5.4 Rapport de conformité (MP-V-02)

L'IA DOIT livrer un rapport court, dans ce format :

| Contrôle | Constat | Statut |
|---|---|---|
| V1 Pages | 2 pages, conforme à la fiche technique | conforme |
| V3 Lignes | ex. 4 : 4 lignes visibles sur 4 prévues | conforme |
| G9 colonnes | colonnes de réponse de 4,2 cm au lieu de 5 cm (5 colonnes sur 16 cm) | **écart déclaré** |
| V6 Symboles | ☐ affiché par substitution de police | **à vérifier sur l'ordinateur de l'école** |
| V11 Unicité (jeu) | 16 réponses distinctes ; chaque question a une seule réponse ; boucle fermée (vérification par programme) | conforme |
| V20 Page pleine | p1 95 %, p2 92 % du budget (mesure du rendu) | conforme |

Puis : **Écarts assumés** (du plus important au plus mineur, avec leur justification) et **Statut des informations** (MP-V-03) : ce qui a été vérifié dans la session (avec la source), ce qui ne l'a pas été, ce qui relève d'une inférence de conception.

# ÉTAPE 6 — LIVRER

# ANNEXE I-B — GRILLE DE RELECTURE DÉTAILLÉE

À utiliser pour auditer une fiche existante ou pour transformer une fiche d'une autre source. Chaque écart est référencé par son code ; le relevé est présenté du plus grave au plus mineur, en commençant par les écarts aux règles DOIT.

## Grille détaillée (évaluation ou transformation d'une fiche existante)

À utiliser pour auditer une fiche existante (prompt G) ou transformer une fiche d'une autre source (prompt B). Chaque écart constaté est référencé par son identifiant.

#### Contenu didactique (en premier pour analyser une ressource existante, § 0.6)
- Objectif probable et alignement : chaque item fait-il travailler cet objectif ? Les écarts sont signalés, item par item.
- Prérequis implicites : ce que la ressource suppose acquis sans le dire.
- Progression : ordre des items, sauts de difficulté, étapes intermédiaires qui manquent.
- Structure des tâches : types de problèmes ou d'exercices présents (par exemple une ou deux étapes, recherche du tout ou d'une partie) et leur variété.
- Erreurs probables et obstacles prévisibles pour les élèves du degré.
- Données superflues, pièges, difficultés : les signaler et demander s'il s'agit d'un choix didactique.
- Biais possibles et valeurs véhiculées : contextes, prénoms, références culturelles ou sociales ; stéréotypes ; situations, rôles ou récompenses contraires aux valeurs de l'école (par exemple, jouer les voleurs pour s'exercer à la soustraction).
- Réponses et corrigé : présence, exactitude ; une seule réponse ou plusieurs réponses acceptables.
- Usage prévu : moment de la séquence, travail individuel ou collectif, part d'autonomie.
- Sobriété : nombre de pages, couleur et plastification proportionnés à l'usage ; matériel réutilisable.

#### Rendu imprimé (à faire en premier pour un fichier produit, sur le PDF)
- Contrôle visuel V1-V10 (§ 5.2) : pages, coupures, nombre réel de lignes, longueur des lacunes, tailles, symboles, bords, absence de la partie enseignant·e, ordre de l'en-tête, orthographe.
- Budget de page de la fiche technique cohérent avec le rendu (MP-O-11) ; aucune page élève remplie partiellement (MP-O-14, V20).
- Cohérence didactique : graphème présent dans chaque mot, réponses d'énigme calculées, cases de réussite vides, zone de réponse pour chaque question, partie enseignant·e des jeux et des dictées (V21).
- Fichier produit par du code : validation au schéma OOXML (V14).

#### Jeux imprimés (si la ressource est un jeu)
- Unicité de chaque réponse dans le lot et fermeture de la boucle, ou complétude des paires et des familles (V11, MP-J-01, X-15).
- Aucun indice non visé : radical, longueur, position, ordre d'impression (MP-J-02, MP-J-03, X-16).
- Pièces aux dimensions prévues, non coupées ; traits de coupe en pointillés, séparations internes en trait plein épais (V12, MP-J-05) ; chaque case d'accueil dépasse la pièce mobile d'au moins 0,5 cm par côté (MP-J-10) ; planche qui occupe toute la page, repères de coupe au bord de la feuille (MP-J-11, MP-J-12).
- Recto-verso aligné sur une impression test (V13).
- Règle en étapes avec un exemple hors lot ; carte-mémoire pour vérifier ; aucun repère de niveau (MP-J-06 à MP-J-08).
- Modalité adaptée à la notion : pas de jeu uniquement oral pour une notion orthographique (X-17).

#### Contexte et adéquation
- Public cible identifié ; vocabulaire, syntaxe, structure et densité adaptés (MP-P-04).
- Contexte d'usage pris en compte ; durée estimée réaliste (MP-P-05).
- Type d'objectif (comprendre, agir, explorer) et format d'exercice cohérents (MP-P-06).
- Terminologie suisse respectée (1P-8P et 9S-11S, cycles 1 à 3, disciplines romandes).
- Adéquation de la demande à la progression PER examinée et signalée (MP-P-09).
- En-tête : Prénom et Date en première ligne, titre centré entre deux espaces, objectif en langage élève sans étiquette (MP-O-12).
- Aucune forme écrite fautive ou inexistante dans tout le texte élève, y compris exemples, distracteurs et phrases de jugement (MP-CC-11).
- Aucune activité ne demande aux élèves d'utiliser un outil d'IA.

#### Format et impression
- A4 ; orientation cohérente avec la tâche ; marges de 2,5 cm ; largeur utile respectée (MP-F-01 à MP-F-06).
- Compatibilité photocopie : pas de fond gris, pas de trait fin, pas d'ombre, pas de contraste faible (MP-I-03, MP-T-05).
- Contrastes suffisants pour l'impression (MP-C-01).

#### Typographie
- Nombre de polices (signaler tout excès au-delà de deux) (MP-T-01).
- Police adaptée au lecteur (MP-T-02) ; taille conforme au degré.
- Majuscules, soulignement, italique : usage ponctuel (MP-T-03, MP-T-04).
- Accentuations simultanées limitées, hiérarchie respectée (MP-T-06).
- Cohérence typographique d'ensemble.

#### Organisation et densité
- Structure stable et continuité logique entre exercices (MP-O-01).
- Numérotation : un système par niveau (MP-O-02) ; zone d'identification selon la préférence (MP-O-03).
- Nombre d'exercices par page ; espaces blancs ; absence de surcharge (MP-O-04, MP-O-05).
- Aucune coupure de consigne, d'exercice, de tableau ou d'activité entre deux pages (MP-O-06).
- Nombre d'étapes entre consigne et action réduit (MP-O-07).
- Rôles identifiables ; même rôle, même format (MP-O-08, MP-O-09).

#### Consignes et charge cognitive
- Consignes directes, courtes, concrètes, sans négation, une action par phrase (MP-CO-01 à MP-CO-05, MP-CC-02).
- Cohérence consigne ↔ format de réponse (MP-CO-07).
- Informations strictement nécessaires ; pas de redondance inutile (MP-CC-01, MP-CC-05).
- **Aucun pré-marquage** des éléments à repérer (MP-CC-10).
- Aides et explications au plus près des actions (MP-CC-04).
- Exemple résolu pour toute tâche nouvelle (MP-CC-06).
- Lisibilité globale en un coup d'œil ; au plus 4 éléments principaux par exercice (MP-CI-02, MP-CI-03).

#### Zones de réponse
- Présentes pour toute production écrite, séparées de la consigne, suffisantes (MP-E-04 à MP-E-07).
- Construites avec R1 ; aucune ligne en tirets bas pour une phrase ; aucune ligne fusionnée (MP-E-10, X-01, X-02).
- Absentes pour les tâches sans écriture (MP-E-09).
- Interlignes et hauteur de ligne conformes (MP-E-01 à MP-E-03).

#### Images et couleurs
- Pertinence de chaque image ; lien direct image–tâche ; placement au-dessus ou à gauche (MP-I-01, MP-I-02).
- Lisibilité sans couleur ; pas de rouge/vert ni de rouge/bleu ; codes couleur constants (MP-C-02 à MP-C-04).
- Pas d'émoji ni de symbole coloré dans la fiche élève.

#### Aides et guidage
- Définitions des mots difficiles ; feedback ou auto-correction prévus (MP-A).
- Pour l'exploration : but visible, repères de progression, retours intermédiaires (MP-A).
- Pré-training : décision conforme, format adapté, au plus ¼ de page, placé avant l'exercice (MP-PT).

#### Partie enseignant·e
- Corrigé exact, avec explication brève par exercice.
- Barème cohérent (total vérifié par addition).
- Différenciation soutien / défi ; erreurs typiques de la notion ciblées.
- Prolongements numériques facultatifs, sans outil retiré ni non vérifié présenté comme autorisé.

#### Révision
- Proposition de révision après usage (MP-P-08) ; conformité globale au référentiel.

#### Format du relevé d'écarts

| Réf. règle | Constat (localisé : exercice, ligne) | Niveau : DOIT ou DEVRAIT | Correction proposée |
|---|---|---|---|

Le relevé est présenté **du plus grave au plus mineur**, en commençant par les écarts aux règles DOIT, puis DEVRAIT.


# EXTRAITS DE LA BIBLIOTHÈQUE IA 2

# PARTIE 10 — DÉPLOIEMENT PROGRESSIF ET RÉFÉRENCES

## Décider avant de demander, observer après la classe

Ces repères servent quand l'enseignant·e transforme ou crée une ressource. Ils complètent la procédure de conception (Partie 8) : l'IA s'y réfère pour rappeler ce qui n'a pas été décidé, sans décider à la place de l'enseignant·e.

**Les quatre temps d'une demande**

1. Pourquoi : l'intention propre à cette transformation, et le besoin qu'elle sert.
2. Ce que je décide : ce qui ne change pas (objectif, critères de réussite) et ce qui peut varier (guidage, quantité, complexité, contexte).
3. Ce que je demande : le contexte, la tâche précise, la forme attendue.
4. Ce que je contrôle : le risque propre à cette transformation (perdre l'objectif en simplifiant, souffler la réponse en aidant, décorer sans faire apprendre), si la transformation était nécessaire, et si l'IA l'était : une ressource existante convenait-elle ? Chaque demande consomme de l'énergie ; quelques échanges ciblés valent mieux qu'une série de régénérations.

Les deux premiers temps appartiennent à l'enseignant·e. L'IA peut les rendre explicites et poser une question si une information indispensable manque.

**Partir du problème, pas de la forme**

| Départ par la forme | Risque | Départ par le problème |
|---|---|---|
| Transformer en jeu | Amusant mais peu aligné | Les élèves s'engagent peu : quel défi ou quel rôle soutient l'activité ? |
| Rendre plus original | Surcharge, perte de lisibilité | La tâche est trop mécanique : comment provoquer justification et verbalisation ? |
| Numériser la fiche | Numérique sans valeur ajoutée | Besoin de retour rapide ou de collaboration : quel outil apporte une fonction utile ? |
| Ajouter des images | Décor sans aide à la compréhension | Un obstacle de compréhension appelle-t-il un schéma, un exemple ? |
| Créer un escape game | Activité lourde, parfois superficielle | Un besoin d'enquête ou de résolution progressive justifie-t-il ce format ? |

**Profondeur d'une transformation**

| Niveau | Type | Effet sur l'activité |
|---|---|---|
| 1. Surface | Mise en page, reformulation, clarification | Améliore la lisibilité, change peu la nature de la tâche |
| 2. Adaptation | Différenciation, aides progressives, version accessible | Répond à des besoins réels, soutient l'équité d'accès |
| 3. Outillage | Autocorrection, cartes d'aide, grilles, plan de travail | Modifie les conditions de travail, libère l'enseignant·e pour observer |
| 4. Socialisation | Tutorat, débat, correction croisée, production collective | Fait des interactions un levier d'apprentissage |
| 5. Reconfiguration | Fiche → enquête, exercice → situation-problème, réponse → production | Transforme la nature cognitive ou sociale de l'activité |
| 6. Dispositif | Parcours articulé (aides, autoévaluation, corrigés, ajustements) | Forte valeur, mais exige contrôle et faisabilité |

L'échelle décrit, elle ne hiérarchise pas : le bon niveau est celui qui répond au problème identifié, dans les contraintes de la classe.

**Après la classe : effet recherché, observations, traces**

| Effet recherché | Ce qu'on chercherait à observer | Traces envisageables |
|---|---|---|
| Engagement | Persévérance, implication dans les rôles ou les défis | Observation, productions terminées |
| Compréhension | Réponses mieux justifiées, capacité à expliquer | Billet de sortie, mini-quiz, explication orale |
| Autonomie | Moins de demandes d'aide immédiate, autocorrection pertinente | Traces d'autocorrection, tableau de suivi |
| Verbalisation | Échanges sur les stratégies, vocabulaire disciplinaire | Notes d'observation, critères de discussion |
| Différenciation effective | Tous les élèves entrent dans la tâche et progressent | Parcours réalisés, aides utilisées |
| Transfert | Usage de la notion dans une situation nouvelle | Tâche ouverte, production finale |
| Régulation | Obstacles repérés, ajustements pour la suite | Grille enseignant·e, erreurs-types |
| Mémorisation | Rappel correct après un délai, réutilisation spontanée | Mini-quiz différé, cartes de rappel, autotest |

Ces catégories orientent le regard ; elles se lisent au conditionnel (ce que l'on chercherait à observer) et ne prescrivent ni note ni mesure. L'IA peut proposer, dans la partie enseignant·e, l'effet visé, une observation et une trace ; elle ne présume jamais du résultat.

Statut : propositions de conception de l'auteur (22.11.2026), reprises de son travail sur la transformation des ressources ; sans référence propre dans cette section.
