# Bibliothèque IA 1 — module « Jeux » — v1

Édition du 22 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale et de sections de la Bibliothèque IA 2 par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : jeux imprimés : gabarits J, règles communes aux jeux, planches, contrôles des appariements, coopération.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# ÉTAPE 2 — SPÉCIFIER : FICHE TECHNIQUE ET BUDGET DE PAGE

## 2.1 Table unique des paramètres par degré

C'est la **seule source des valeurs chiffrées**. L'IA lit la colonne du degré et n'invente pas d'autres valeurs.

| Paramètre | 1P-2P | 3P-4P | 5P-6P | 7P-8P | Statut |
|---|---|---|---|---|---|
| Taille du texte lu par l'élève | 24 pt | 18 pt | 14 pt | 12 pt | Standard (MP-T) |
| Titre de la fiche | taille du texte + 2 à 4 pt, gras | idem | idem | idem | Inférence de conception |
| Police | Arial, Verdana, Tahoma ou Calibri ; une seule | idem | idem | idem | MP-T-01, MP-T-02 |
| Interligne de lecture | 1,5 | 1,5 | 1,5 | 1,5 | MP-E-01 |
| Interligne des phrases à trous | 2,0 | 2,0 | 2,0 | 2,0 | MP-E-02 |
| Hauteur d'une ligne d'écriture | ≥ 1,0 cm ; davantage ou « trottoirs » selon l'écriture des élèves (proposition) | 1,0 cm | 1,0 cm | 0,8 à 1,0 cm | MP-E-03 (8-10 mm) |
| Lacune d'un mot ou d'un nombre | 6-8 cm | 6-8 cm | 6-8 cm | 6-8 cm | MP-E-07 |
| Réponse d'une phrase | 2 lignes de 14-16 cm | idem | idem | idem | MP-E-05, MP-E-07 |
| Production courte | 5-6 lignes de 16 cm | idem | idem | idem | MP-E-07 |
| Cellule de tableau à remplir | ≥ 5 cm × ≥ 1 cm | idem | idem | idem | MP-E (table) |
| Exercices par page | 3-5 courts ou 1-2 longs | idem | idem | idem | MP-O-04 |
| Items par exercice | 3-5 (6-10 très courts et identiques pour l'automatisation) | idem | idem | idem | MP-CI-02 |
| Hauteur d'une ligne de texte lue | 1,27 cm | 0,95 cm | 0,74 cm | 0,64 cm | Calculée (taille × 1,5) |
| Hauteur d'un item à trou | 1,69 cm | 1,27 cm | 0,99 cm | 0,85 cm | Calculée (taille × 2,0) |
| Tirets bas pour 6 cm (Arial / Calibri) | 13 / 14 | 17 / 19 | 22 / 24 | 25 / 28 | Calculée (métriques des polices) |
| Tirets bas pour 8 cm (Arial / Calibri) | 17 / 19 | 23 / 25 | 29 / 33 | 34 / 38 | Calculée (métriques des polices) |
| Pièce de domino J1 | 9,3 × 5,3 cm ; 26 pt ; 10 dominos par planche | idem | 9,3 × 3,3 cm (deux moitiés de 4,65 cm) ; 18 pt ; 16 dominos par planche ; deux lignes dans la moitié question | idem | Révision du 19.11.2026 (MP-J-11, variantes par tranche d'âge, § 3.8) : 5P-8P rendu en PDF et regardé ; 1P-4P calculé et rendu en miniature ; non testé en classe. Ancienne pièce de 8 × 2,5 cm, 14 pt : testée le 30.10.2026 |
| Planche de pièces | une page ; toute la surface utile (MP-J-11) | idem | idem | idem | MP-J-11, MP-J-12 |

*Les valeurs « calculées » ont été établies dans cette version à partir de la taille de police et des métriques des polices (Liberation Sans et Carlito, métriquement identiques à Arial et Calibri). Elles servent à planifier ; le contrôle sur rendu (Étape 5) fait foi.*

*Cycle 3 (9S à 11S) — valeurs retenues le 21.11.2026, non testées en classe : appliquer les valeurs de la colonne 7P-8P (texte de 12 pt ; 11 pt seulement sur demande, pour un document dense de 10S-11S). Les règles propres aux non-lecteurs et à l'apprentissage initial de l'écriture (lignes d'écriture romandes, absence de ligne Prénom, consigne remplacée par un exemple déjà fait) ne s'appliquent pas au cycle 3. Les jeux ont leurs propres formats 9S-11S (§ 3.8, variantes par tranche d'âge). La progression d'une notion au cycle 3 se vérifie dans le PER ; sans vérification, elle est marquée « à vérifier ».*

## 2.3 Modèle de fiche technique

| N° | Gabarit | Patron / micro-format | Items | Réponse attendue | Zone de réponse | Hauteur estimée | Page |
|---|---|---|---|---|---|---|---|
| — | En-tête R7 | — | — | — | Prénom et Date ; titre centré ; objectif élève | … cm | 1 |
| 1 | G… | P…, MF… | … | geste / mot / phrase / production | … | … cm | 1 |
| … |  |  |  |  |  |  |  |
|  | **Total page 1** |  |  |  |  | **≤ 22 cm** |  |
|  | **Total page 2** |  |  |  |  | **≤ 22 cm** |  |

#### Exemple rempli (illustratif) — Fiche d'entraînement, passé composé, 5P, Arial 14 pt

| N° | Gabarit | Patron / micro-format | Items | Réponse attendue | Zone de réponse | Hauteur estimée | Page |
|---|---|---|---|---|---|---|---|
| — | En-tête R7 | — | — | — | Prénom et Date ; titre centré ; objectif élève | 3,5 cm | 1 |
| — | Encadré R5 | pré-training minimal | — | — | règle + 2 exemples (4 lignes) | 3,6 cm | 1 |
| 1 | G8 Repérage | P06 / MF04 | 4 | geste (souligner, encadrer) | aucune ligne | 5,3 cm | 1 |
| 2 | G9 Tableau | P06 / MF14 | 4 | 1 mot par cellule | cellules 5 cm × 1,1 cm | 7,1 cm | 1 |
|  | **Total page 1** |  |  |  |  | **19,5 cm** |  |
| 3 | G3 Compléter | P06 / MF15 | 5 | 2 mots (auxiliaire + participe) | lacune de 6 cm (22 tirets bas) | 7,4 cm | 2 |
| 4 | G7 Production | P12 / MF23 | 1 | 2 phrases | 4 lignes R1a | 6,3 cm | 2 |
| — | Bilan R6 | MF31 | 3 critères | choix entouré | cellules ≥ 1 cm | 3,8 cm | 2 |
|  | **Total page 2** |  |  |  |  | **17,5 cm** |  |

#### Fiche technique d'un jeu : planches de pièces

Pour un jeu, la fiche technique ajoute une ligne par planche.

| Planche | Gabarit J | Pièce (l × h) | Pièces par rangée × rangées | Contenu d'une pièce | Hauteur de la planche | Page |
|---|---|---|---|---|---|---|
| Lot Lune | J1 Domino-boucle | 8 × 2,5 cm (deux moitiés de 4 cm) | 2 × 8 = 16 | réponse en gras · question sur deux lignes, 14 pt | 0,9 + 8 × 2,5 = 20,9 cm | 2 |

#### Rubrique « Conditionnement » (v7.2, MP-O-13)

Pour toute ressource imprimée autre qu'une fiche à photocopier, la fiche technique ajoute une ligne : support, finition, découpe, montage, quantité par page, autocorrection portée par le matériel.

| Support | Finition | Découpe et montage | Quantité par page | Autocorrection |
|---|---|---|---|---|
| papier épais, feuille sous pochette effaçable, A3 | plastification, velcro, pincette, attache parisienne | par l'adulte, en atelier, par l'élève | n exemplaires, numérotés si les pièces doivent se retrouver | verso, double impression, rabat, forme, grille croisée, ou aucune |

# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT

## 3.1 Chaîne de décision

> Objectif → indices de réussite → fonction (F, Livre II Partie 1) → processus cognitif (Partie 3) → patron (P, Partie 5) → micro-format (MF, Partie 6) → **gabarit d'exercice (G, § 3.3) ou de jeu (J, § 3.8)** → dimensions (Étape 2)

Les choix pédagogiques se font avec le Livre II. **Le gabarit est le point de passage obligé** entre la pédagogie et la mise en page : c'est lui qui apporte les dimensions, la hauteur estimée et la recette de construction.

## 3.2 Règle de couverture (originalité permise, jamais sans dimensions)

- Chaque exercice de la fiche DOIT correspondre à un gabarit G1 à G31 ; chaque pièce d'un jeu, à un gabarit J1 à J38 (§ 3.8) ; chaque outil permanent, à un gabarit SP (§ 3.9) ; chaque document, à un gabarit GF (§ 6.1).
- L'IA PEUT proposer un format non répertorié si elle le juge mieux adapté. Elle DOIT alors le décrire **avant de l'utiliser** avec la même fiche-type que les gabarits ci-dessous (usage, disposition, zone de réponse, items, hauteur estimée, recette, vigilance), et l'inscrire dans la fiche technique.

## 3.4 Fiche-type pour un nouveau gabarit

Tout format nouveau DOIT être décrit ainsi avant usage : **Usage · Disposition · Zone de réponse (dimensions) · Items · Hauteur estimée · Recette (R1 à R8) · Vigilance**, puis reporté dans la fiche technique. Pour un gabarit de jeu, la fiche-type précise en plus la **pièce** (dimensions, contenu) et le **statut** (testé ou non testé).

Les fiches ajoutées en v7.2 sont présentées sous une forme condensée : **Usage · Structure · Dimensions · Recette · Contrôles · Interdits** (la structure reprend la disposition et les items ; les dimensions, la zone de réponse et la hauteur ; les interdits, la vigilance).

## 3.5 Correspondances patron × gabarit × micro-format

| Patron pédagogique (Livre II, Partie 5) | Gabarits compatibles | Micro-formats compatibles | Gabarits de jeu (J) |
|---|---|---|---|
| P01 Défi initial | G6, G10 | MF01, MF06, MF21 | — |
| P02 Enquête par indices | G8, G9, G12 | MF04, MF05, MF19, MF24, MF54 | — |
| P03 Comparaison contrastée | G9, G12 | MF07, MF08, MF22, MF55 | J3 |
| P04 Erreur à débusquer | G4, G6, G1 | MF14, MF16, MF30, MF33 | — |
| P05 Choix argumenté | G6, G7 | MF11, MF20 | — |
| P06 Exemple guidé puis autonome | G3, G4, G9, G13 | MF13, MF14, MF15, MF57 | — |
| P07 Tri raisonné | G1, G12 | MF08, MF09, MF10 | J3 |
| P08 Associations à justifier | G2, G21 | MF17, MF18 | J2 |
| P09 Prédire, tester, expliquer | G3, G7, G10 | MF06, MF19, MF52, MF53 | — |
| P10 Cas à résoudre | G3, G7, G9 | MF04, MF24, MF49, MF50 | J5 |
| P11 Experts complémentaires | G7, G9 | MF26, MF27, MF29 | — |
| P12 Production sous contraintes | G7, G10 | MF23, MF29, MF56 | — |
| P13 Confrontation des solutions | G6, G7, G9 | MF07, MF25, MF30 | — |
| P14 Rappel actif progressif | G1, G3, G6 | MF17, MF18, MF32 | J1, J2, J4, J5 |
| P15 Ateliers différenciés | G1 à G25, G29 à G31 | MF13, MF15, MF36 | J1 à J6 |
| P16 Transfert de contexte | G7, G10 | MF15, MF34 | — |
| P17 Investigation critique des sources | G8, G9 | MF04, MF07, MF16, MF54 | — |
| P18 Retour sur sa démarche | G6, G7 | MF21, MF31-MF35, MF51, MF58 | — |
| P19 Rallye de postes | G1 à G25 | MF05, MF38, MF43 | J1 à J38 |
| P20 Apprivoiser un outil de référence | G6, G8 | MF04, MF05, MF12 | — |
| P21 Même tâche, plusieurs temps | G10, G15 | MF21, MF35, MF43 | — |
| P22 Les élèves conçoivent l'exercice | G18 | MF23, MF64, MF68 | J4 |
| P23 Du vécu corporel à la trace | G19 | MF38, MF42 | — |
| P24 La dictée réfléchie | G20 | MF33, MF45, MF75 | — |

**Colonne J** : correspondances proposées (inférence de conception), sauf P14 → J1, testé le 30.10.2026.

**P04 (erreur à débusquer)** : pleinement utilisable en mathématiques, en sciences et pour un raisonnement ou un fait ; en langue écrite, à partir de formes correctes ou des productions des élèves eux-mêmes, ou, sur décision de l'enseignant·e et dès la 5P, avec des formes fautives marquées et corrigées (exception encadrée du § 3.7).

## 3.8 Catalogue des gabarits de jeu (J1 à J38)

Les gabarits J décrivent les **pièces imprimées** d'un jeu (dominos, cartes, plateau, dé). Ils sont distincts des gabarits d'exercice et de support G1 à G31 et suivent la fiche-type du § 3.4. La règle du jeu, la carte-mémoire et la trace individuelle relèvent des gabarits G et du dossier de jeu GF-F (§ 6.1). Les dimensions sont données pour 5P-6P (14 pt). J1 a été testé en v7 ; J7 à J16 ont été testés sur rendu en v7.2 ; pour J2 à J6, toute dimension est une **inférence de conception, à tester**. J17 à J20 (19.11.2026) sont dessinés par le code de l'Annexe I-C : rendu contrôlé, non testés en classe. J21 à J38 (20.11.2026) de même.

### Règles communes aux jeux (MP-J)

| Code | Règle | Niveau |
|---|---|---|
| MP-J-01 | **Unicité** : chaque question admet une seule pièce correcte dans tout le lot, pas seulement parmi les pièces voisines. | DOIT |
| MP-J-02 | **Aucun indice non visé** : aucune pièce ne se trouve par le radical, la longueur, la position sur la planche ou l'ordre d'impression. Il faut au moins trois formes du même mot dans le lot. | DOIT |
| MP-J-03 | **Ordre d'impression mélangé** : deux pièces voisines dans la solution ne sont jamais voisines sur la planche. | DOIT |
| MP-J-04 | **Autocorrection intégrée** : boucle qui se ferme, verso, ou carte-solution. Depuis la v7.2, la règle s'étend à tout objet imprimé destiné au travail autonome (rabat, forme de la découpe, double impression, grille croisée). Une carte que l'élève tire d'une pioche ne porte jamais sa réponse au verso (MP-J-14). | DEVRAIT |
| MP-J-05 | **Traits** : les traits de coupe sont en pointillés ; les séparations internes, en trait plein épais. | DOIT |
| MP-J-06 | Par défaut, **aucun repère de niveau** sur les pièces (MP-D-01) ; le lot se repère par la couleur du papier et par le contenu. Si l'enseignant·e demande des étoiles de difficulté, elles sont admises sur les cartes, aux conditions de MP-D-01. | DOIT |
| MP-J-07 | **Règle du jeu** en étapes numérotées, une action par phrase, avec un exemple résolu fait de pièces hors lot. Elle répond à **cinq questions** : quel est le but, et qu'apprend-on en jouant ; quel matériel, pour combien de joueurs ; que fait-on à son tour, étape par étape ; que se passe-t-il en cas d'erreur, et comment vérifie-t-on la réponse ; quand la partie est-elle terminée. Pour que chacun travaille, et pas seulement celui qui joue : groupes de trois ou quatre ; **tout le monde répond** (chaque élève note sa réponse, par exemple sur une ardoise, puis celui dont c'est le tour la dit) ; un·e vérificateur·trice tient le corrigé et change à chaque tour ; une partie modèle est jouée devant la classe ; le but d'apprentissage est annoncé avant de jouer (« à la fin, vous saurez… »). | DOIT |
| MP-J-08 | **Carte-mémoire** : elle sert à vérifier après la pose (P14), pas à chercher avant ; la règle le dit. | DEVRAIT |
| MP-J-09 | **En-tête** : la fiche de trace individuelle porte l'en-tête R7 ; la règle du jeu et les planches, matériel de groupe, portent un titre sans ligne Prénom et Date. | DEVRAIT |
| MP-J-10 | **Pièce mobile et case d'accueil** : toute case destinée à recevoir une pièce mobile (étiquette, carte, jeton, pince) mesure au moins la pièce + 0,5 cm par côté, en largeur et en hauteur ; les deux dimensions de la pièce et de la case figurent dans la fiche technique ; contrôle par programme (`verifier_case_piece`, Annexe I-C) et sur le rendu (V12). S'applique aussi aux fiches (G12-b, plateaux, tableaux à étiquettes). (révision du 2.11.2026, suite) | DOIT |
| MP-J-11 | **Surface de la planche** : une planche de pièces à découper (cartes, dominos, étiquettes, pièces, modèles) occupe **toute la surface utile de la page** — en A4 portrait, environ 18,6 × 26,4 cm, avec des marges d'environ 1,2 cm sur les côtés et 1,6 cm en haut et en bas. On **agrandit les pièces** ou on **change leur disposition** (nombre de colonnes et de rangées) au lieu de laisser une bande vide ; la zone restée vide ne dépasse pas une demi-hauteur de pièce. Les dimensions retenues et le calcul (colonnes × largeur, rangées × hauteur) figurent dans la fiche technique. La planche, tableau à hauteur exacte, échappe au budget de 22 cm (MP-O-11) ; son rendu est contrôlé (V12). Le texte et l'image de chaque pièce sont centrés sur la pièce, contrôlés sur le rendu. (révision du 19.11.2026) | DOIT |
| MP-J-12 | **Repères de coupe** : toute planche à découper porte des **repères de coupe au bord de la feuille**, pour la coupe au massicot : un trait fin (0,5 pt, noir, environ 0,45 cm de long) dans le prolongement de **chaque** ligne de coupe — en haut et en bas pour les coupes verticales, à gauche et à droite pour les coupes horizontales —, séparé de la planche par environ 0,25 cm et à au moins 0,5 cm du bord de la feuille (zone imprimable). Les pointillés restent pour la coupe aux ciseaux (MP-J-05). La mention de la planche se place dans la marge du haut, sans toucher les repères. (révision du 19.11.2026) | DOIT |
| MP-J-13 | **Choix présenté** : avant de produire un jeu, et chaque fois que l'enseignant·e demande quelles sont les possibilités, l'IA **montre le panorama des jeux** (image produite par `panorama_jeux`, Annexe I-C ; même image dans la page web du guide et dans le fichier « Panorama des jeux » de la boîte à outils). **Le panorama ne contient que des miniatures tirées des documents réels** — la page elle-même, réduite, du modèle Word ou de la planche prête à imprimer : l'enseignant·e obtient ce qu'il ou elle voit ; un gabarit sans document n'y figure qu'en liste, sans image, et l'IA ne dessine jamais de schéma à la place (20.11.2026). Elle présente ensuite en une ligne chacun les deux ou trois gabarits qui conviennent à la demande, donne sa recommandation et **attend le choix**. Pour un gabarit à variantes (formes J5-a à J5-d, variantes de J2, J3 et J4), elle présente les variantes de la même façon. Quand le degré est connu, elle montre la page de miniatures de la tranche d'âge (`miniatures_tranche`), avec le nombre de pièces ou de cases de chaque format. Si elle ne peut ni exécuter le code ni afficher une image, elle donne la liste des noms des jeux et renvoie au fichier. Dans ce qu'elle présente à l'enseignant·e, elle désigne chaque jeu ou exercice par son nom, sans code ; les panoramas et les mentions de planche ne portent pas de code (21.11.2026). Quand un **modèle Word à remplir** ou une **planche prête à imprimer** existe pour le gabarit retenu (liste à la fin du § 3.8), elle le signale. Pour une fiche, quand l'enseignant·e demande quels exercices sont possibles, elle montre de la même façon le **panorama des exercices** (`panorama_exercices`, gabarits G1 à G23 ; fichier « Panorama des exercices » de la boîte à outils). Exception : l'enseignant·e a déjà nommé le gabarit ou la forme. (19.11.2026) | DOIT |
| MP-J-14 | **Carte tirée, dos neutre** : une carte que l'élève tire d'une pioche ou reçoit face cachée (carte-défi d'un plateau, carte d'appel, carte de memory) a un **dos neutre et identique** : ni réponse ni indice au verso, parce que l'élève verrait la réponse avant de répondre. Chaque carte porte un numéro ; le contrôle passe par une **feuille de solutions numérotée** par lot, tenue par un·e camarade ou retournée sur la table. **Avant de produire les cartes, l'IA pose deux questions** : (1) dos **à motif** ou dos **blanc** ? (2) **avec une mention personnelle** au dos — par exemple le nom du jeu, ou une catégorie de cartes : « Défi », « Bonus », « Malus », « Chance » — ou **sans** ? Sans réponse, elle retient le dos à motif sans mention et le signale. **Dos à motif** (`dos_a_motif`), comme celui d'une carte à jouer : des lignes fines (losanges, carreaux ou vagues) remplissent un cadre aux angles arrondis, tracé d'un trait fin à environ 3 mm du bord de la carte ; la marge reste blanche. Le motif est le même sur toutes les cartes du jeu, il gêne la lecture par transparence et donne son unité au jeu ; un motif différent par jeu permet de trier des jeux mélangés. **Dos blanc** : rien n'est imprimé au verso ; à réserver à un papier assez épais pour que le recto ne se lise pas par transparence. **Mention personnelle** : la même sur toutes les cartes d'une pile, en gras dans un cartouche gris au centre de la carte (paramètre `texte`) ; jamais une mention qui distingue deux cartes d'une même pile ; plusieurs catégories donnent plusieurs piles, donc une planche par catégorie. Le cadre rend visible un décalage du recto-verso : essai d'impression avant de tirer tout le jeu (V13). Le verso-réponse reste réservé aux cartes que l'élève tient lui-même, question vers lui (J4, J14), et à la carte à pinces (J10). (19.11.2026) **Liseré** : chaque carte d'un jeu de cartes porte un cadre à coins arrondis, tracé à 3 mm du trait de coupe ; la teinte de la carte s'arrête au cadre et la marge reste blanche, comme sur une carte à jouer. Les modèles Word de la boîte à outils le portent déjà : pour un jeu de cartes en .docx, partir du modèle plutôt que d'un tableau neuf, qui ne le porte pas. En PDF, `planche_pdf(..., lisere=True)`, `cartes_categories` et `cartes_mots_interdits` le tracent (`lisere_cartes`) ; sans modèle Word, produire la planche de cartes en PDF. Pas de liseré sur un domino, un puzzle ou une tuile. (21.11.2026) | DOIT ; le liseré et le motif du dos sont des conventions (priorité 5) |

*MP-J-09 précise MP-O-12 pour le matériel de groupe (inférence de conception, conforme au test du 30.10.2026). MP-J-10 répond au défaut de G12-b (étiquettes plus grandes que les cases) relevé par la revue indépendante du 2.11.2026. MP-J-11 et MP-J-12 répondent à la demande de l'auteur du 19.11.2026 : planches qui laissaient le bas de la page vide, absence de repères pour le massicot ; règles appliquées au memory des consignes (19.11.2026, rendu PDF contrôlé, non testé en classe). MP-J-13 répond à sa demande du même jour : l'enseignant·e ne connaît pas les possibilités tant que l'IA ne les montre pas.*

### J1 — Domino-boucle (testé)

- **Usage** : entraînement et rappel actif d'une correspondance question ↔ réponse (conjugaison, calcul, mot ↔ image), avec autocorrection par la fermeture de la boucle.
- **Pièce** : domino de 9,3 × 3,3 cm, en deux moitiés de 4,65 cm (révision du 19.11.2026, MP-J-11 ; auparavant 8 × 2,5 cm). Moitié gauche : la réponse, en gras. Moitié droite : la question (par exemple le sujet, puis le verbe entre parenthèses, sur deux lignes). Texte de 16 à 20 pt, même corps sur toute la planche.
- **Disposition** : planche de 2 × 8 dominos sur toute la surface utile (18,6 × 26,4 cm) ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut ; traits de coupe en pointillés, séparation centrale en trait plein épais ; ordre d'impression mélangé ; une planche par page.
- **Zone de réponse** : aucune écriture ; le geste est de poser le domino.
- **Items** : 12 à 16 dominos par boucle ; chaque réponse est unique dans la boucle ; au moins trois formes du même mot (MP-J-02). Deux boucles équivalentes permettent la différenciation (MF46).
- **Hauteur** : 8 × 3,3 = 26,4 cm (calculé ; rendu PDF contrôlé le 19.11.2026). Version antérieure en .docx : mention 0,9 cm + rangées × 2,5 cm, soit 20,9 cm pour 8 rangées (calculé ; 21,1 cm rendus lors du test, 20,7 cm au contrôle des recettes v7).
- **Recette** : R8 (planche de pièces à découper) : en PDF, `planche_pdf` (Annexe I-C), repères de coupe compris, une planche par fichier ; en .docx, saut de page avant chaque planche.
- **Vigilance** : contrôler l'unicité et la fermeture (V11 ; script en Annexe I-C) ; éviter les verbes à voyelle initiale avec *je* (élision) ; imprimer sur papier épais ; la règle précise que la carte-mémoire sert à vérifier après la pose (MP-J-08).
- **Statut** : testé (5P, conjugaison du présent des verbes en -er et en -ir, 30.10.2026 ; rendu PDF contrôlé). Dimensions du 19.11.2026 : planche de la boucle Lune produite en PDF avec `planche_pdf` et regardée (corps de 19,5 pt ; police Liberation Sans pour l'essai) ; non imprimée, non testée en classe.

### J2 — Memory ou appariement (non testé)

- **Usage** : associer deux éléments (mot ↔ image, calcul ↔ résultat, mot ↔ définition), soit cartes face cachée (memory), soit à découvert (appariement).
- **Pièce** : carte de 6,2 × 6,6 cm (3 × 4 cartes remplissent la page, MP-J-11) ; une information par carte ; mot de 22 pt au moins sous une image, 32 pt sur une carte-mot ; image de 5 cm au plus ; texte et image centrés.
- **Disposition** : planche de 3 × 4 cartes (18,6 × 26,4 cm), soit 6 paires par planche ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 6 à 12 paires ; chaque carte n'a qu'une partenaire dans le lot (MP-J-01).
- **Hauteur** : 4 × 6,6 = 26,4 cm ; marges d'environ 1,65 cm en haut et en bas (calculé ; rendu PDF contrôlé le 19.11.2026).
- **Recette** : R8 avec une seule moitié par pièce (colonnes de 6,2 cm, rangées de 6,6 cm, 3 pièces par rangée), repères de coupe compris. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : pour la memory, aucune différence visible au dos : dos à motif encadré ou dos blanc, identique sur toutes les cartes, au choix de l'enseignant·e (`dos_a_motif`, MP-J-14) ; au cycle 1, pour des non-lecteurs, appariement image ↔ image ; aucune forme fautive (MP-CC-11).
- **Statut** : non testé ; dimensions = inférence de conception, à tester.

### J3 — Familles (non testé)

- **Usage** : classer des éléments selon une catégorie en réunissant les cartes d'une même famille (familles de mots, natures, groupes de verbes, multiples).
- **Pièce** : carte de 6,2 × 8,8 cm (révision du 19.11.2026, MP-J-11 ; auparavant 5 × 6,5 cm) ; en haut, le nom de la famille en mots ; au milieu, l'élément ; en bas, la liste des membres de la famille (pour pouvoir demander une carte).
- **Disposition** : planche de 3 × 3 cartes (18,6 × 26,4 cm) ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 4 à 6 familles de 4 à 6 cartes ; chaque carte appartient à une seule famille (MP-J-01).
- **Hauteur** : 3 × 8,8 = 26,4 cm (calculé ; disposition rendue en PDF le 19.11.2026).
- **Recette** : R8 avec une seule moitié par pièce (colonnes de 6,2 cm, 3 pièces par rangée, hauteur 8,8 cm) ; en PDF : `planche_pdf`, repères de coupe compris. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : la famille est nommée en mots, jamais par la seule couleur (X-08) ; familles équilibrées ; pour une catégorie orthographique, les membres sont écrits, pas seulement nommés à l'oral (X-17).
- **Statut** : non testé ; dimensions = inférence de conception, à tester.

### J4 — Cartes de rappel recto-verso (MF18) (non testé)

- **Usage** : rappel actif, seul·e ou en duo : la question au recto, la réponse au verso ; reprises espacées (MF18, P14).
- **Pièce** : carte de 9,3 × 6,6 cm (révision du 19.11.2026, MP-J-11 ; auparavant 8 × 5 cm) ; recto : la question ; verso : la réponse.
- **Disposition** : planche recto de 2 × 4 cartes (18,6 × 26,4 cm), repères de coupe au bord de la feuille (MP-J-12), puis planche verso dont les deux colonnes sont inversées, pour une impression recto-verso sur le bord long. Sans recto-verso : carte pliée en deux (question et réponse côte à côte).
- **Zone de réponse** : aucune ; l'élève répond oralement ou sur une ardoise, puis retourne la carte.
- **Items** : 8 à 16 cartes ; une seule réponse par question (MP-J-01).
- **Hauteur** : 4 × 6,6 = 26,4 cm par planche (calculé ; disposition du recto rendue en PDF le 19.11.2026).
- **Recette** : R8 (deux planches : recto, puis verso aux colonnes inversées) ; en PDF : `planche_pdf`, puis `verso_de` pour l'ordre du verso ; les marges égales à gauche et à droite gardent les repères alignés au verso. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : alignement recto-verso contrôlé sur une impression test (V13) ; papier assez épais pour que le verso ne se lise pas par transparence ; une fiche de suivi des reprises (MF43) peut accompagner le jeu. Ces cartes se tiennent en main, question vers l'élève : elles ne servent jamais de pioche (MP-J-14).
- **Statut** : non testé ; dimensions et inversion des colonnes = inférence de conception (calcul à confirmer sur l'imprimante de l'école).

### J5 — Plateau de parcours (révision du 19.11.2026 : quatre formes dessinées ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement varié sur un parcours (jeu de l'oie, course) ; les défis sont tirés sur des cartes.
- **Principe** (révision du 19.11.2026) : le plateau a la forme d'un **parcours** que l'élève suit des yeux — serpent, escargot, chemin ou circuit —, **jamais celle d'un tableau de cases**. Il est dessiné (R11, fonction `plateau_parcours` de l'Annexe I-C) et occupe toute la surface utile de la page (18,6 × 26,4 cm, comme MP-J-11).
- **J5-a — Serpent** : ruban de cases en lacets : 5 rangées de 6 cases, reliées par 4 cases de virage ; 34 cases de 3,1 × 2,9 cm (Départ, 1 à 32, Arrivée).
- **J5-b — Escargot** : spirale ronde qui s'enroule vers le centre, comme le jeu de l'oie traditionnel : 27 cases (Départ, 1 à 25, Arrivée au centre) ; bande de 2,5 cm de large, cases d'environ 3,1 cm de long ; spirale de 17,4 × 18,6 cm, sous deux cases d'accueil pour les cartes (pioche et défausse).
- **J5-c — Chemin** : cases rondes de 2,7 cm (« pas japonais ») reliées par un pointillé, sur 6 rangs en lacets ; 34 cases (Départ, 1 à 32, Arrivée).
- **J5-d — Circuit** : boucle fermée de 24 cases de 3,1 × 3,3 cm au bord de la page (Départ, 1 à 23) ; pioche et défausse au centre ; pour une partie en plusieurs tours ou à durée fixée.
- **Choix de la forme** (inférence de conception) : serpent ou chemin quand le sens du parcours doit se lire sans aide (cycle 1, début du cycle 2) ; escargot pour un jeu de l'oie ; circuit quand la partie ne doit pas se terminer par un « premier arrivé ». Sans indication de l'enseignant·e, l'IA propose l'escargot pour un « jeu de l'oie » et le serpent dans les autres cas, et le signale.
- **Pièce** : plateau d'une page ; Départ et Arrivée écrits en mots, autres cases numérotées (22 pt, gras) ; plus petite dimension d'une case : 2,5 cm au moins, pour qu'un pion y tienne ; cases spéciales grisées **et** au numéro entouré (jamais la teinte seule, MP-C-05), leur effet est écrit dans la règle ; cartes-défis au format J2 (6,2 × 6,6 cm) ou J4, plutôt que du texte dans les cases.
- **Disposition** : A4 portrait, mention dans la marge du haut ; rien à découper, donc aucun repère de coupe ; cases d'accueil des cartes : carte + 0,5 cm par côté (7,2 × 7,6 cm, MP-J-10) ; dé et pions : matériel de classe. Agrandissement en A3 à l'impression (141 %) pour un groupe de quatre : inférence de conception.
- **Zone de réponse** : aucune sur le plateau.
- **Items** : 12 à 24 cartes-défis ; une seule réponse correcte par carte ; cartes numérotées, à dos neutre : à motif encadré ou blanc, avec ou sans mention au dos (nom du jeu, catégorie de la pile : « Défi », « Bonus », « Malus », « Chance »), selon la réponse de l'enseignant·e aux deux questions de MP-J-14 : jamais de réponse au verso, l'élève la verrait en tirant la carte (MP-J-14) ; solutions sur une feuille numérotée par lot (MP-J-04).
- **Hauteur** : 26,4 cm pour les quatre formes (serpent : 9 × 2,93 ; escargot : 7,6 + 0,2 + 18,6 ; chemin : 6 rangs, virages de 2,37 cm de rayon ; circuit : 8 × 3,3) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `plateau_parcours(base, forme, titre, speciales)` écrit le plateau en PDF et en SVG à l'échelle 1 ; il s'imprime tel quel ou s'insère dans le dossier de jeu (`inserer_image`). L'ancien plateau en tableau (6 × 8 cases de 2,5 cm, R8 adaptée) est retiré.
- **Vigilance** : le hasard ne doit pas dominer : une réponse juste fait avancer ; les cases « piège » ne portent aucune information sur la notion ; quatre cases spéciales au plus par plateau (inférence de conception).
- **Interdits** : plateau présenté comme un tableau ou une grille pleine ; parcours dont le sens ne se lit pas (cases qui se suivent sans se toucher ni être reliées) ; case spéciale signalée par la seule teinte.
- **Statut** : les quatre formes ont été produites en PDF et regardées le 19.11.2026 (nombre et dimensions des cases calculés par la fonction ; polices de remplacement Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J6 — Dé à monter (révision du 19.11.2026 : grand ou petit ; rendu contrôlé, montage non réalisé)

- **Usage** : tirage au hasard d'un élément (pronom, nombre, consigne) pour un jeu ou un entraînement.
- **Pièce** : patron de cube en croix, avec sept languettes de collage ; deux formats : **J6-a, grand dé** : faces de 6 cm, un dé par page ; **J6-b, petit dé** : faces de 4,2 cm, deux dés identiques par page. Une information par face, centrée, en gras : 48 pt sur le grand dé, 30 pt sur le petit, jamais moins de 14 pt. (Auparavant : faces de 4 cm, puis de 5,5 cm.)
- **Disposition** : grand dé : croix de 3 faces en largeur et 4 en hauteur (18 × 24,9 cm avec la languette du haut) ; petit dé : deux patrons couchés, l'un sous l'autre (17,5 × 12,6 cm chacun). Les languettes des côtés se logent dans les angles libres de la croix. Contour à découper en pointillés (MP-J-05), plis en trait fin ; patron découpé aux ciseaux, donc sans repères de coupe (exception à MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 6 faces.
- **Hauteur** : grand dé : 24,9 cm ; petit dé : 2 × 12,6 + 0,8 = 26 cm (calculé par la fonction ; rendu PDF contrôlé le 19.11.2026).
- **Recette** : R11 : `de_a_monter(base, faces, format)` écrit le patron en PDF et en SVG à l'échelle 1 ; `format='grand'` ou `'petit'`. L'IA propose les deux formats et laisse choisir (MP-J-13) : le grand pour un dé lancé devant la classe ou pour les plus jeunes, le petit pour un dé par groupe. L'ancien tableau .docx (R8 adaptée) est retiré.
- **Vigilance** : papier épais ; montage par l'adulte ou en atelier ; vérifier que chaque face reste lisible une fois le dé monté.
- **Statut** : les deux formats ont été produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, montage réel non réalisé (V18).

### J7 — Loto (testé sur rendu)

- **Usage** : réactiver un répertoire : on entend ou on lit, on couvre (TR33, BDRP-D1).
- **Pièce** : carton de 7,5 × 5 cm, à 6 cases de 2,5 cm ; 8 cartons par planche. Cartes d'appel de 5 × 2,5 cm. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carton de 9,3 × 6,6 cm, à 6 cases de 3,1 × 3,3 cm, 2 × 4 cartons par planche ; cartes d'appel de 6,2 × 3,3 cm, 3 × 8 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Items** : 12 éléments, chacun sur 4 cartons (calculé : 8 × 6 / 12).
- **Hauteur** : 0,9 + 4 × 5 = 20,9 cm (calculé ; 20,0 cm de tracé mesurés). Depuis le 19.11.2026 : 4 × 6,6 = 26,4 cm (calculé).
- **Recette** : R14 (`planche_zones`, 3 sous-colonnes) ; R13 (`generer_loto`, `verifier_loto`) ; règle du jeu en planche A5 (R15) ; cartes d'appel en deux jeux, pour remplir la page (MP-O-14).
- **Contrôles** : V11, V12, V19 (fréquence exacte, aucun doublon, cartons tous différents).
- **Interdits** : deux cartons identiques ; élément absent des cartes d'appel ; jeu seulement oral pour une notion orthographique (X-17) ; règle rédigée au masculin seul (« le meneur ») : formulation épicène (« la personne qui lit », « on »).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### J8 — Symboles communs (testé sur rendu)

- **Usage** : discrimination rapide de mots ou d'images : deux cartes ont toujours exactement un élément commun (BDRP-D5). Le nom commercial du jeu n'est pas repris.
- **Pièce** : carte de 5 × 3,9 cm ; 4 éléments par carte ; 13 cartes pour 13 éléments (n = 3). Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 6,2 × 5,28 cm, 3 × 5 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Hauteur** : 0,9 + 5 × 3,9 = 20,4 cm (calculé). Depuis le 19.11.2026 : 5 × 5,28 = 26,4 cm (calculé).
- **Recette** : R14 ; R13 (`plan_projectif`, `verifier_symboles`) ; règle du jeu en planche A5 (R15).
- **Contrôles** : V19 (78 paires vérifiées par programme) ; V12.
- **Interdits** : construire les cartes à la main, sans vérification.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; construction n² + n + 1 vérifiée par programme ; dimensions = inférence de conception. Correction du 20.11.2026 : `plan_projectif` accepte n = 4 (21 cartes de 5 éléments, format 9S-11S), que l'ancienne formule ne construisait pas ; les trois formats (n = 2, 3 et 4) sont vérifiés par `verifier_symboles`.

### J9 — Grille « Trouve quelqu'un qui… » (testé sur rendu)

- **Usage** : prise de parole, langues, cohésion (BDRP-D6).
- **Pièce** : fiche individuelle, en-tête R7 ; grille de 4 × 4 cases de 4 × 3,4 cm.
- **Items** : 16 caractéristiques observables, chacune tenant dans sa case sans mot coupé (sinon : raccourcir l'item ; jamais couper un mot).
- **Hauteur** : en-tête + consigne + 13,6 cm (calculé).
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : items sur la santé, la famille, la religion ou l'origine.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J10 — Carte à pinces (testé sur rendu)

- **Usage** : choix autocorrigé ; l'élève pose une pince à linge sur la réponse de chaque question, puis retourne la carte (TR25, BDRP-C1).
- **Pièce** (révision du 2.11.2026, suite) : **une carte = une page** qui porte autant de questions que possible, et une pince par question. Chaque question occupe un bloc de trois lignes : la question à gauche (13,4 cm), ses trois réponses **empilées dans la colonne du bord droit** (2,2 cm × 0,85 cm par réponse), là où la pince se pose. Verso : le mot « bravo » (ou une image : étoile, coche) dans la cellule de la bonne réponse, rien dans les autres (MP-J-04).
- **Disposition** : A4 portrait, sur toute la hauteur utile de la page : 10 questions (10 × 2,55 cm) de la 5P à la 8P, 6 questions (6 × 4 cm, la phrase du bas étant plus grande) de la 1P à la 4P, 12 questions (12 × 2,1 cm) de la 9S à la 11S (révision du 19.11.2026 ; auparavant 8 questions, bas de page vide) ; marge droite du recto et marge gauche du verso réduites à 1,5 cm pour que la pince atteigne la colonne (dérogation déclarée à MP-F-03) ; blocs séparés par un trait plein épais, réponses par un trait fin ; sous la carte, la phrase « Quand mes 10 pinces sont posées, je retourne la carte : chaque pince doit être sur le mot « bravo ». » Variante A5 : 4 à 5 questions par carte, planche R15.
- **Items** : 10 questions (6 ou 12 selon la tranche d'âge) ; 3 réponses ; distracteurs fondés sur des erreurs typiques, expliqués dans la partie enseignant·e.
- **Hauteur** : mention 0,6 + 10 × 2,55 + phrase 1,2 = 27,3 cm, entre des marges haute et basse de 0,9 cm : la carte occupe toute la page (révision du 19.11.2026, rendu du modèle Word contrôlé ; auparavant 8 questions, 22,2 cm).
- **Règle pour les élèves** : en planche A5 (R15, côte à côte), six étapes numérotées (MP-J-07), exemple résolu avec une question hors carte : 1. Je prends la carte et une pince par question. 2. Je lis la question 1, je pince la réponse que je choisis, au bord de la carte. 3. Une pince par question. 4. Quand toutes mes pinces sont posées, je retourne la carte. 5. Chaque pince doit être sur « bravo » ; sinon je cherche pourquoi et je déplace la pince. 6. Je retire les pinces et je range la carte. Titre sans ligne Prénom et Date (MP-J-09).
- **Partie enseignant·e** (V21) : solution de toutes les questions ; pour chaque distracteur, l'erreur typique visée ; fabrication (recto-verso sur le bord long, impression test V13, plastification, une pince par question) ; débriefing (deux questions).
- **Recette** : `carte_a_pinces` (R14 : tableau à deux colonnes, cellule de question fusionnée sur trois lignes) ; R12 (au verso, colonne des réponses à gauche, même ordre des lignes) ; R15 (règle).
- **Contrôles** : V11 (une seule réponse juste par question ; `bravo` exactement une fois par bloc), V12, V13 (recto-verso sur impression test), V20, V21.
- **Interdits** : une question par carte (l'ancien format du 2.11.2026 : huit cartes de 8 × 5 cm, abandonné) ; forme écrite fautive en distracteur (X-13) ; marque lisible par transparence ; réponses en ligne loin du bord (la pince ne les atteint pas) ; lot livré sans règle élève ni partie enseignant·e.
- **Statut** : testé sur rendu (2.11.2026, suite ; LibreOffice, PDF regardé page par page, schéma OOXML valide) ; alignement recto-verso calculé, V13 non réalisé ; dimensions = inférence de conception. Révision du 19.11.2026 : nombre de questions porté à 6, 10 ou 12 pour remplir la page ; modèle Word rendu et mesuré ; `carte_a_pinces` non relancée avec ces nombres.

### J11 — Roue à fenêtre et rabat (testé sur rendu)

- **Usage** : contenu cyclique, correction immédiate (TR32, BDRP-C2). L'élève lit la question dans la fenêtre, répond, soulève le rabat.
- **Pièce** : deux disques de 11 cm. Dessous : six secteurs de 60°, question à 45 mm du centre, réponse à 28 mm. Dessus : fenêtre de 39 à 52 mm, rabat de 18 à 36 mm, charnière en trait fin à 18 mm ; ouverture de 54°.
- **Disposition** : les deux disques sur une page (dessin de 16 × 24 cm) ; attache parisienne au centre. **Écart déclaré** : 24 cm de haut, au-delà du budget de 22 cm, dans la hauteur utile de 24,7 cm.
- **Items** : 6 paires ; à 14 pt, la réponse tient en 23 mm (calculé).
- **Recette** : R11 (`roue_J11`), dessin vectoriel SVG et PDF à l'échelle 1 ; jamais de construction en .docx. Inséré dans un .docx, il garde 16 cm de large pour rester à l'échelle.
- **Contrôles** : V18 (chaque texte tient dans la fenêtre ou sous le rabat), montage d'essai réel avant la classe.
- **Interdits** : texte sur un trait de coupe ; réduire le disque pour ajouter des secteurs.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; géométrie calculée ; montage réel non réalisé. Remplace l'essai v0 PL-J11, dont les étiquettes débordaient sur la découpe.

### J12 — Lettres à fabriquer (testé sur rendu)

- **Usage** : matériel sensoriel de tracé (BDRP-C7).
- **Pièce** : plaque de 8 × 10 cm ; une lettre liée en 130 pt ; quatre plaques par page. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : plaque de 9,3 × 13,2 cm, 2 × 2 par page ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R10, R14. Les flèches de tracé sont ajoutées à la main par l'enseignant·e.
- **Conditionnement** : papier émeri, plaquette.
- **Contrôles** : V12, V15.
- **Interdits** : lettre dessinée ou générée ; flèche de tracé produite sans contrôle du geste enseigné.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; arbitrage du balayage : retenu comme gabarit J.

### J13 — Cartes de rôle (testé sur rendu)

- **Usage** : attribuer un rôle dans un travail de groupe (TR64, MF29, MF76) ; variante : cartes d'identité fictives pour l'interaction orale en langue (BDRP-I4).
- **Pièce** : carte de 8 × 5 cm : titre de 1,5 cm, deux phrases en 3,5 cm ; quatre rôles par groupe ; deux jeux de quatre cartes par planche (page pleine, MP-O-14). Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 6,6 cm, 2 × 4 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14.
- **Contrôles** : V12.
- **Interdits** : personne réelle, rôle lié au genre ou au niveau de l'élève.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J14 — Cartes d'erreurs (testé sur rendu)

- **Usage** : analyser une erreur de calcul ou de raisonnement (TR29, P04).
- **Pièce** : carte de 8 × 10 cm : auteur·e fictif·ve, résolution, consigne. Verso : ce qui s'est passé, calcul juste. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 13,2 cm, 2 × 2 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14, R12.
- **Contrôles** : V12, V13 ; corrigé recalculé par programme ; V21 : nombres et procédure adaptés à la progression du degré (MP-P-09) ; le verso nomme l'erreur de procédure (par exemple « a écrit 13 à côté du 3, sans faire de retenue »).
- **Interdits** : orthographe et grammaire, sauf analyse d'erreurs demandée par l'enseignant·e, dès la 5P, aux quatre conditions du § 3.7 (X-13, MP-CC-11) ; erreur attribuée à un·e élève identifiable.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J15 — Cartes d'aide graduée (testé sur rendu)

- **Usage** : coup de pouce à prendre soi-même, du plus ouvert au plus guidé (TR30, MP-D).
- **Pièce** : carte de 8 × 5 cm ; titre « Aide 1 » à « Aide 4 » ; une aide par carte. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 6,6 cm, 2 × 4 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14.
- **Contrôles** : V12 ; gradation portée par le numéro, jamais par la seule couleur (X-08).
- **Interdits** : donner la réponse dans la dernière aide ; repère évaluatif.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J16 — Cartons-réponses (testé sur rendu)

- **Usage** : vote à main levée sans écran (TR69, version papier).
- **Pièce** : carton de 8 × 10,5 cm : lettre de 110 pt, puis une ligne « je choisis A ». Quatre cartons par planche. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carton de 9,3 × 13,2 cm, 2 × 2 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14, style de cellule dédié.
- **Contrôles** : V12 ; lisible à distance (V17, capitale de 28 mm, seuil calculé de 19 m).
- **Interdits** : distinguer les réponses par la seule couleur.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J17 — Grille d'alignement (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement à deux, ou à deux équipes, sur des réponses courtes (résultats de calculs, formes conjuguées, mots) ; principe du « quatre à la suite ».
- **Principe** : chaque rond de la grille porte une réponse. À son tour, l'élève tire une question (carte-défi à dos neutre, MP-J-14, ou dé), trouve la réponse sur la grille et la couvre d'un jeton de sa couleur. Le premier qui aligne trois ou quatre jetons — en ligne, en colonne ou en diagonale — gagne.
- **Pièce** : plateau d'une page, dessiné (R11, fonction `grille_alignement`) : bandeau de titre et de consigne, puis cadre arrondi à double filet ; ronds à double cercle, réponse centrée en gras. 5P-8P : 5 × 7 = 35 ronds de 2,9 cm, corps de 20 pt, aligner 4.
- **Disposition** : A4 portrait, toute la surface utile (18,6 × 26,4 cm, MP-J-11) ; rien à découper, donc aucun repère de coupe ; jetons de deux couleurs ou de deux formes : matériel de classe (rond de 2,2 cm au moins, MP-J-10).
- **Items** : autant de réponses que de ronds ; une réponse peut figurer deux fois sur la grille (l'élève choisit alors où poser son jeton), jamais deux réponses différentes pour une même question (MP-J-01) ; les cartes couvrent toutes les réponses de la grille.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, grille de 24,4 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `grille_alignement(base, valeurs, colonnes, rangees, aligner, titre)` écrit le plateau en PDF et en SVG ; sans `valeurs`, les ronds portent les nombres de 1 à n. Un texte trop long pour un rond est refusé.
- **Vigilance** : la stratégie (bloquer l'adversaire) ne doit pas prendre le pas sur la notion : une réponse fausse fait passer le tour ; vérification par la feuille de solutions.
- **Interdits** : grille sans réponses (simple jeu d'alignement, sans apprentissage) ; distinction des joueurs par la seule couleur si les jetons sont imprimés (MP-C-05).
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J18 — Serpents et échelles (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement varié sur un parcours, quand on veut des retournements de situation ; les défis sont tirés sur des cartes, comme pour J5.
- **Principe** : cases numérotées en lacets, du Départ (en bas à gauche) à l'Arrivée (en haut). Au pied d'une échelle, l'élève tire une carte : s'il répond juste, il monte. Sur la tête d'un serpent, il tire une carte : s'il se trompe, il redescend jusqu'à la queue. **La réponse décide, pas le dé seul.**
- **Pièce** : plateau d'une page, dessiné (R11, fonction `serpents_echelles`) : cases en damier gris clair et blanc, numéro en gras dans le coin de la case ; échelles à deux montants et barreaux ; serpents au corps gris ondulant, tête ronde. 5P-8P : 6 × 8 = 48 cases de 3,0 cm au moins, 3 échelles et 3 serpents.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; échelles et serpents tirés au sort par la fonction (paramètre `graine`), sans croisement ni extrémité commune, ou imposés (paramètre `liens`) ; dé, roue J20 et pions : matériel de classe.
- **Exception à la règle des plateaux** : la grille est ici le principe du jeu ; le sens du parcours se lit par les numéros, par les mots Départ et Arrivée et par le damier. Pour un simple parcours, préférer J5.
- **Items** : 12 à 24 cartes-défis numérotées, à dos neutre (MP-J-14) ; feuille de solutions.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm et 8 rangées de 3,05 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `serpents_echelles(base, colonnes, rangees, liens, graine, titre)` écrit le plateau en PDF et en SVG.
- **Vigilance** : un serpent long en fin de parcours décourage : deux rangées de descente au plus près de l'Arrivée (inférence de conception) ; au cycle 1, expliquer le sens des lacets sur le plateau avant de jouer.
- **Interdits** : serpent ou échelle dont l'effet ne dépend pas d'une réponse ; plus d'un lien par case.
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J19 — Bataille navale (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement à deux sur une notion qui croise deux entrées : sujet × verbe (la forme conjuguée), nombre × nombre (le produit, la somme), lettre × chiffre (le repérage dans un quadrillage).
- **Principe** : chaque élève reçoit une fiche et la cache derrière un classeur. Il dessine ses bateaux dans la grille « Ma flotte ». Pour tirer, il **dit ou écrit la réponse** de la case visée (« nous finissons ») ; l'adversaire annonce « touché » ou « dans l'eau » ; le tireur note son essai dans la grille « Mes tirs ».
- **Pièce** : fiche d'une page par élève, dessinée (R11, fonction `bataille_navale`) : deux grilles identiques l'une sous l'autre, intitulés des colonnes et des lignes en gras, filet ondulé (l'eau) après chaque titre, trois bateaux modèles à côté de « Ma flotte ». 5P-8P : 6 × 6 = 36 cases par grille.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; les cases restent vides : l'élève y dessine et y écrit.
- **Items** : 5, 6 ou 8 intitulés par entrée ; chaque case a une seule réponse (MP-J-01) ; chaque croisement existe (pas de verbe sans la personne visée).
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, deux blocs de 12,2 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `bataille_navale(base, en_colonnes, en_lignes, taille, titre)` écrit la fiche en PDF et en SVG ; sans intitulés, les colonnes portent des lettres et les lignes des nombres.
- **Vigilance** : la réponse est dite avant le tir, vérifiée avec la carte-mémoire de la notion (MP-J-08) ; la flotte (un bateau de trois cases, un de deux, un d'une case) s'écrit dans la règle.
- **Interdits** : croisement qui produirait une forme inexistante ; tir annoncé par les seules coordonnées quand la notion visée est la réponse de la case.
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J20 — Roue de tirage (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : tirage au sort sans dé ni montage : un pronom, un nombre, une consigne, une catégorie de cartes ; remplace le dé J6 quand il faut plus de six issues ou une préparation immédiate.
- **Principe** : l'élève pose un trombone au centre de la roue, le tient avec la pointe d'un crayon et le fait tourner d'une pichenette ; le secteur où il s'arrête donne le tirage.
- **Pièce** : roue d'une page, dessinée (R11, fonction `roue_tirage`) : disque de 18,2 cm à double filet, 3 à 12 secteurs égaux, alternés blanc et gris clair quand leur nombre est pair, texte en gras (24 pt, réduit si besoin, jamais moins de 10 pt) ; sous la roue, vingt cases « Mes tirages » pour noter.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; trombone et crayon : matériel de classe.
- **Items** : 4 secteurs de la 1P à la 4P, 6 de la 5P à la 8P, 8 dès la 9S (inférence de conception) ; un texte court par secteur, sur une ou deux lignes.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, roue de 18,2 cm, cases de tirage) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `roue_tirage(base, secteurs, titre)` écrit la roue en PDF et en SVG. Un texte trop long pour un secteur est refusé.
- **Vigilance** : secteurs égaux, pour que le tirage reste équitable ; le texte n'est pas tourné : il se lit sans pencher la tête.
- **Interdits** : secteurs distingués par la seule teinte (le texte porte l'information, MP-C-05) ; plus de 12 secteurs.
- **Statut** : roues de 4, 6 et 8 secteurs produites en PDF et regardées le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, rotation du trombone non essayée.

### J21 — Puzzles à deux pièces (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : associer deux éléments (calcul et résultat, mot et définition, mot et image, fraction et nombre décimal) en atelier autonome ; l'élève se corrige seul.
- **Principe** : chaque puzzle est un rectangle coupé en deux par une ligne d'une forme propre (pointe, créneau ou demi-rond, à trois hauteurs, vers la gauche ou vers la droite : 18 formes). Seules les deux bonnes pièces s'emboîtent : **la découpe corrige** (MP-J-04).
- **Pièce** : puzzle de 9,3 × 4,4 cm en 5P-8P (deux pièces de 4,65 cm) ; élément de gauche en gras ; contour en pointillés, ligne d'emboîtement en trait plein, à découper aux ciseaux.
- **Disposition** : planche de 2 × 6 puzzles sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12) ; mention dans la marge du haut.
- **Items** : 8, 12 ou 18 paires par planche ; chaque élément de gauche a une seule réponse dans le lot, et aucune réponse ne figure deux fois (MP-J-01).
- **Recette** : R11 : `puzzle_association(base, paires, colonnes, rangees, taille_pt, mention)` ; un texte trop long est refusé.
- **Vigilance** : mélanger les paires avant l'appel, pour que deux puzzles voisins n'aient pas des formes proches ; plastifier avant de découper.
- **Interdits** : plus de 18 puzzles dans un même lot (deux formes seraient identiques) ; indice de couleur sur les pièces.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; emboîtement réel non essayé.

### J22 — Puzzle à bandes (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : ranger une suite (nombres, lettres, multiples, nombres décimaux, mots dans l'ordre alphabétique, étapes d'un récit).
- **Principe** : une image est coupée en bandes verticales ; chaque bande porte une étiquette en bas. Remises dans l'ordre des étiquettes, les bandes reforment l'image : **l'image corrige**.
- **Pièce** : bande de 26,4 cm de haut ; 5 bandes de 3,7 cm, 10 bandes de 1,9 cm ou 12 bandes de 1,6 cm ; étiquette en gras dans les 2,6 cm du bas.
- **Disposition** : toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Image** : celle de l'enseignant·e (paramètre `image` : photo ou dessin libre de droits ; l'image est étirée à la zone de 18,6 × 23,8 cm) ; sans image, la fonction dessine un paysage au trait.
- **Recette** : R11 : `puzzle_bandes(base, etiquettes, image, mention, taille_pt)` ; les étiquettes sont données dans l'ordre correct.
- **Vigilance** : une image aux formes continues d'une bande à l'autre, sans grand aplat uniforme ; les bandes se rangent sur une feuille-support ou dans une réglette.
- **Interdits** : étiquettes en double ; image qui contient déjà l'ordre (numéros visibles).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J23 — Mot mystère (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réactiver le vocabulaire d'une leçon ; fiche individuelle ou à deux.
- **Principe** : chaque définition donne un mot, écrit dans sa ligne de cases ; les lignes sont décalées pour que les cases grises, lues de haut en bas, forment le mot mystère.
- **Pièce** : fiche d'une page (R11, fonction `mot_mystere`) : bandeau de titre et de consigne, grille de cases de 2 cm au plus, définitions numérotées, cases du mot mystère en bas de page.
- **Items** : autant de mots que de lettres dans le mot mystère (4, 6 ou 8) ; chaque définition n'admet qu'un mot (MP-J-01) ; majuscules sans accent.
- **Recette** : `mot_mystere(base, mystere, mots, titre, taille_pt)` ; la fonction vérifie que le mot numéro i contient la lettre numéro i du mot mystère et place chaque mot.
- **Vigilance** : le mot mystère appartient à la leçon ; les définitions sont à la portée des élèves sans aide.
- **Interdits** : mot à accent indispensable au sens ; définition qui contient le mot ou un mot de la même famille.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J24 — Cocotte en papier (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : se poser des défis à deux (calcul mental, conjugaison, vocabulaire) ; l'élève qui tient la cocotte lit la question et vérifie la réponse.
- **Principe** : un carré à plier. Quatre mots à l'extérieur, huit nombres sur les volets, huit défis sous les volets : la question sur le volet, la réponse en gras dessous.
- **Pièce** : carré de 18,6 cm (R11, fonction `cocotte`) ; traits de pliage fins ; sous le carré, la règle du pliage en quatre étapes et la règle du jeu.
- **Items** : 4 mots courts, 8 nombres ou textes courts, 8 couples question-réponse ; une seule réponse par question (MP-J-01).
- **Recette** : `cocotte(base, coins, nombres, defis, titre, taille_pt)` ; un texte trop long pour sa zone est refusé.
- **Vigilance** : le pliage se montre une fois devant la classe ; papier de 80 g, non plastifié.
- **Interdits** : gage ou prédiction sur une personne ; texte sur un trait de pliage.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; emplacement des textes déduit du pliage par le calcul, **pliage réel non essayé** : plier un exemplaire avant de distribuer.

### J25 — Horloge à aiguilles (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : lire et régler l'heure ; matériel individuel de manipulation.
- **Pièce** : cadran de 17 cm (R11, fonction `horloge`) et deux aiguilles à découper : la petite, grise, pour les heures ; la grande, blanche, pour les minutes ; attache parisienne au centre.
- **Variantes** : chiffres de 1 à 12 seuls (1P-4P) ; graduations des minutes et nombres de 5 à 60 (5P-8P) ; heures de 13 à 24 en plus (9S-11S).
- **Disposition** : cadran en haut de la page, aiguilles et consigne dessous ; contours de découpe en pointillés.
- **Recette** : `horloge(base, minutes, heures_24, titre)`.
- **Vigilance** : imprimer sur papier épais ou plastifier ; les deux aiguilles se distinguent par la longueur et par la teinte, et leur nom est écrit dessus (MP-C-05).
- **Interdits** : chiffres romains ou cadran sans chiffres pour un premier apprentissage.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; montage réel non essayé.

### J26 — Mémo-fiches en éventail (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réviser une série (tables, conjugaisons, mots-outils, formules) ; les fiches se consultent une à une, réunies par une attache.
- **Pièce** : fiche haute de 13,2 cm, large de 6,2 cm, 4,65 cm ou 3,7 cm selon la tranche d'âge ; titre sur bandeau gris, lignes centrées, rond marquant le trou de l'attache en bas.
- **Disposition** : deux rangées de 3, 4 ou 5 fiches sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Items** : 6, 8 ou 10 fiches par planche ; 5 à 12 lignes par fiche ; un titre par fiche.
- **Recette** : R11 : `eventail(base, fiches, colonnes, taille_pt, mention)` ; le corps diminue si une ligne est trop longue, puis la planche est refusée.
- **Vigilance** : plastifier, percer à la perforatrice sur le rond, réunir par une attache parisienne ou un anneau.
- **Interdits** : fiche d'entraînement présentée comme évaluation ; repère de niveau sur la fiche, sauf étoiles de difficulté demandées (MP-J-06).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J27 — Bandes graphiques (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraîner le geste graphique avant et pendant l'apprentissage de l'écriture ; bandes plastifiées, feutre effaçable.
- **Pièce** : bande de 18,6 cm de long, haute de 6,6 cm, 4,4 cm ou 3,3 cm ; un point de départ, un modèle en trait plein sur le premier tiers, puis le même tracé en pointillés à repasser.
- **Motifs** : traits, zigzag, vagues, ponts, coupes, créneaux, boucles, spirales (liste `MOTIFS`).
- **Disposition** : 4, 6 ou 8 bandes sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Recette** : R11 : `bandes_graphiques(base, motifs, mention)`.
- **Vigilance** : le sens du tracé (de gauche à droite, depuis le point) se montre avant l'atelier ; ces bandes ne remplacent pas le modèle d'écriture liée de l'établissement.
- **Interdits** : lettres ou chiffres dessinés par la fonction (le tracé des lettres suit le modèle enseigné, R10).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J28 — Plateau à camemberts (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réviser plusieurs domaines ou plusieurs chapitres dans une même partie ; quiz à six catégories, sur le principe d'un jeu de questions connu, dont le nom commercial n'est pas repris.
- **Principe** : une roue à six rayons. Chaque case porte le symbole d'une catégorie : l'élève y répond à une question de cette catégorie. Au bout de chaque rayon, une grande case (grise, ou teintée en couleur) : une réponse juste y fait gagner la part de la catégorie, que l'élève colorie dans son camembert. Six parts : retour au centre et dernière question.
- **Pièce** : plateau d'une page (R11, fonction `plateau_camemberts`) : roue de 18 cm, couronne et rayons de cases, centre « Départ, Arrivée » ; sous la roue, la légende (symbole et nom de chaque catégorie) et quatre camemberts de score.
- **Catégories** : six, distinguées par un **symbole** (disque, triangle, carré, losange, étoile, croix), jamais par la seule couleur (MP-C-05) ; noms courts, au choix de l'enseignant·e.
- **Cartes** : cartes-questions à dos neutre (MP-J-14), une question par catégorie sur chaque carte, lues par un·e camarade ; la réponse est sur la carte, en gras, sous la question : `cartes_categories(base, cartes, colonnes, rangees, taille_pt, mention)` ; modèle Word à remplir dans la boîte à outils.
- **Recette** : `plateau_camemberts(base, categories, entre, rayon, titre)` ; `entre` : cases entre deux rayons ; `rayon` : cases par rayon.
- **Vigilance** : une partie complète est longue : fixer une durée, ou trois parts à gagner au lieu de six.
- **Interdits** : catégorie distinguée par la seule couleur ; question à plusieurs réponses possibles.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J29 — Cherche et trouve de mots (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : reconnaître vite une classe grammaticale, un son, une famille de mots, une propriété d'un nombre ; jeu de rapidité à deux, trois ou quatre.
- **Principe** : des mots sont dispersés sur la planche, penchés, sans se toucher. Une carte consigne est tirée (« Trouve un adjectif », « Trouve un mot qui contient le son [o] ») ; le premier qui pose le doigt sur un mot qui convient gagne la carte.
- **Pièce** : planche d'une page (R11, fonction `planche_lynx`) : bandeau de titre et de consigne, cadre arrondi, mots en gras ; cartes consignes à dos neutre (MP-J-14), produites avec `planche_pdf` (exemple de douze consignes à la page 4 de la planche prête à imprimer).
- **Items** : 20, 40 ou 65 mots environ ; plusieurs mots conviennent à chaque consigne, et la vérification se fait avec la carte-mémoire de la notion (MP-J-08).
- **Recette** : `planche_lynx(base, mots, graine, taille_pt, titre)` ; les mots sont placés au hasard (paramètre `graine`) ; la fonction refuse la planche s'il n'y a plus de place.
- **Vigilance** : les mots ne portent aucun indice de couleur ou de style ; un mot qui appartient à deux classes (« ferme », « sourire ») s'évite ou se discute.
- **Interdits** : forme fautive sur la planche ; couleur par classe grammaticale.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J30 — Mots interdits (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : définir, reformuler, mobiliser le vocabulaire d'une leçon à l'oral ; en équipes, dès la 5P.
- **Principe** : l'élève fait deviner à son équipe le mot du bandeau, sans prononcer les mots interdits écrits dessous ; un·e adversaire contrôle. Le nom commercial du jeu n'est pas repris.
- **Pièce** : carte de 6,2 × 8,8 cm (9 par planche) ou de 6,2 × 6,6 cm (12 par planche) : mot à faire deviner en gras sur bandeau gris, mention « sans dire », puis 3 ou 5 mots interdits.
- **Disposition** : toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12) ; cartes tirées d'une pioche : dos neutre (MP-J-14).
- **Recette** : R11 : `cartes_mots_interdits(base, cartes, colonnes, rangees, taille_pt, mention)`.
- **Vigilance** : les mots interdits sont ceux que l'élève dirait en premier ; le mot à deviner appartient à la leçon.
- **Interdits** : nom d'une personne de la classe ; mot dont la définition exige un mot interdit.
- **Statut** : deux formats (5P-8P, 9S-11S) produits en PDF et regardés le 20.11.2026 ; non imprimé, non testé en classe.

### J31 — Petit bac (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : mobiliser le vocabulaire par catégories, l'orthographe du début des mots, les classes grammaticales ; individuel ou par deux.
- **Principe** : une lettre est tirée par manche (roue J20 ou dé J6) ; chaque élève écrit, par colonne, un mot qui commence par cette lettre. Un mot juste : 1 point ; un mot que personne d'autre n'a : 2 points.
- **Pièce** : fiche d'une page (R11, fonction `petit_bac`) : bandeau de titre et de règle, ligne du prénom, grille (colonne « Lettre », 3 à 6 catégories, colonne « Points »), case du total.
- **Items** : 3 catégories et 4 manches (1P-4P), 5 et 6 (5P-8P), 6 et 8 (9S-11S) ; lignes de 5,2 cm, 3,5 cm ou 2,6 cm de haut.
- **Recette** : `petit_bac(base, categories, manches, titre, taille_pt)`.
- **Vigilance** : écarter les lettres rares (K, W, X, Y, Z) ; le temps d'une manche se fixe à l'avance.
- **Interdits** : catégorie sur la vie privée des élèves ; points retirés pour l'orthographe quand elle n'est pas l'objectif.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J32 — Cartes à terminaisons (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : automatiser un choix parmi peu de réponses : terminaisons d'un temps, accords, homophones, déterminants ; jeu de cartes à trois ou quatre, dès la 5P.
- **Principe** : chaque joueur reçoit six cartes-réponses (les terminaisons). Une carte-phrase à trou est retournée ; le premier qui pose la bonne terminaison s'en défausse ; une erreur fait piocher deux cartes. Le premier qui n'a plus de cartes gagne.
- **Pièces** : 12 cartes-phrases numérotées de 9,3 × 4,4 cm, le trou marqué par des points de suspension ; 24 cartes-terminaisons de 4,65 × 4,4 cm ; une feuille de solutions numérotée.
- **Vérification** : par la feuille de solutions, tenue par un·e camarade (MP-J-04) ; jamais de réponse au dos d'une carte tirée (MP-J-14).
- **Items** : chaque phrase n'admet qu'une terminaison du jeu (MP-J-01) ; chaque terminaison figure deux fois ; aucune forme fautive n'est imprimée : la phrase à trou reste incomplète.
- **Recette** : `planche_pdf(..., lisere=True)` pour les deux planches (liseré et repères de coupe compris) ; feuille de solutions en R11.
- **Interdits** : phrase qui accepte deux terminaisons ; terminaison absente du jeu.
- **Statut** : exemple 5P-8P (présent, verbes en -er et en -ir du type finir) produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J33 — Petits chevaux (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement sur cartes-défis dans un jeu de parcours connu des élèves ; deux à quatre joueurs.
- **Principe** : piste de 52 cases en croix, quatre écuries, quatre échelles de cinq marches vers le centre. Un 6 **et** une réponse juste font sortir un pion ; sur l'échelle, une réponse juste par marche. Un pion rejoint par un adversaire retourne à l'écurie.
- **Pièce** : plateau d'une page (R11, fonction `petits_chevaux`) : cases de 1,24 cm ; joueurs distingués par un **symbole** (disque, triangle, carré, étoile), jamais par la couleur seule (MP-C-05) ; règle en trois phrases sous le plateau.
- **Matériel** : seize pions de 1 cm au plus (MP-J-10 : jetons de classe ou pions découpés), un dé, des cartes-défis à dos neutre (modèle J5).
- **Recette** : `petits_chevaux(base, titre)`.
- **Vigilance** : partie longue : limiter à deux pions par joueur ou à une durée ; la capture peut décourager les plus jeunes : variante sans retour à l'écurie.
- **Interdits** : question dont l'enjeu est seulement de rejouer, sans lien avec l'objectif.
- **Statut** : un format produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; taille des cases (1,24 cm) à éprouver avec les pions de la classe.

### J34 — Qui est-ce ? (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : formuler des questions fermées avec le vocabulaire de la notion (pair, multiple de, supérieur à, décimal, négatif ; nature d'un mot ; propriétés d'une figure) ; à deux.
- **Principe** : chaque élève a la même grille. L'un choisit un élément en secret et l'écrit ; l'autre pose des questions auxquelles on répond par oui ou par non, et barre ce qui ne convient pas, jusqu'à trouver l'élément.
- **Pièce** : fiche d'une page (R11, fonction `grille_qui_est_ce`) : bandeau, 12, 24 ou 30 cases à coins arrondis, élément en gras ; ligne de l'élément secret en bas.
- **Items** : des nombres, des mots ou des figures nommées, **sans portrait** ; chaque élément se distingue des autres par au moins une propriété travaillée.
- **Recette** : `grille_qui_est_ce(base, elements, colonnes, titre, taille_pt)`.
- **Vigilance** : afficher les questions modèles (« Est-ce un multiple de 3 ? ») ; la fiche est à usage unique, ou glissée sous une pochette effaçable.
- **Interdits** : portraits ou caractéristiques physiques de personnes ; question sur un élève de la classe.
- **Statut** : trois formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J35 — Bataille (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : comparer deux valeurs : nombres et calculs, fractions, nombres décimaux et pourcentages, longueurs ; à deux.
- **Principe** : chaque joueur retourne une carte ; la plus grande valeur gagne les deux cartes ; deux valeurs égales : « bataille », chacun retourne une nouvelle carte.
- **Pièce** : carte de 6,2 × 6,6 cm (12 par planche), de 4,65 × 6,6 cm (16) ou de 4,65 × 5,28 cm (20) ; une valeur par carte, écrite sous des formes différentes d'une carte à l'autre.
- **Disposition** : `planche_pdf(..., lisere=True)`, toute la surface utile (MP-J-11), liseré et repères de coupe (MP-J-12) ; cartes tirées : dos neutre (MP-J-14) ; valeur écrite en grand (36 à 40 pt), réduite seulement si elle ne tient pas dans le cadre.
- **Items** : quelques valeurs égales sous deux écritures (3/5 et 60 %) pour provoquer des batailles ; vérification avec la carte-mémoire de la notion (MP-J-08).
- **Interdits** : valeurs toutes écrites sous la même forme (le jeu ne ferait plus comparer) ; unités mêlées sans que ce soit l'objectif.
- **Statut** : trois exemples produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J36 — Tuiles-lettres (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : lettres mobiles pour composer des mots, des anagrammes, des mots croisés sur table.
- **Pièce** : tuile de 3,1 × 3,3 cm (48 par planche), de 2,07 × 2,03 cm (117) ou de 1,55 cm de côté (204) ; lettre minuscule en gras ; un trait sous la lettre donne le bas de la tuile (b, d, p, q, n, u).
- **Répartition** : l'alphabet complet, puis les lettres selon leur fréquence en français (liste `FREQUENCES`, voyelles nombreuses) ; majuscules en option.
- **Recette** : R11 : `tuiles_lettres(base, colonnes, rangees, majuscules, mention)` ; repères de coupe (MP-J-12).
- **Vigilance** : plastifier avant de découper ; ranger par lettre dans une boîte à compartiments.
- **Interdits** : valeur en points sur les tuiles quand le calcul du score n'est pas l'objectif.
- **Statut** : trois formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J37 — Sudoku (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : raisonner par élimination ; activité d'autonomie, sans lien direct avec une notion.
- **Pièce** : fiche d'une page (R11, fonction `sudoku`) : quatre grilles de 4 × 4 cases (1P-4P), deux de 6 × 6 (5P-8P), deux de 9 × 9 (9S-11S) ; blocs en trait épais.
- **Contrôle** : chaque grille a **une seule solution**, vérifiée par programme (`_sudoku`) ; la page des solutions s'imprime à part (`solutions=True`).
- **Recette** : `sudoku(base, taille, grilles, trous, graine, solutions, titre)` ; `graine` change les grilles, `trous` la difficulté.
- **Vigilance** : montrer la règle sur une grille de 4 × 4 avant de laisser chercher.
- **Interdits** : grille recopiée d'une publication ; grille à plusieurs solutions.
- **Statut** : trois formats et leurs solutions produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J38 — Mot caché : la fleur (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : orthographe lexicale, lettres probables d'un mot ; à deux. Remplace le jeu du pendu : **aucune image de pendu** dans les ressources.
- **Principe** : un élève choisit un mot et trace un tiret par lettre ; l'autre propose des lettres. Lettre du mot : elle s'écrit sur son tiret. Lettre absente : elle est barrée dans l'alphabet, et celui qui a choisi le mot dessine une partie de la fleur : tige, feuille, feuille, cœur, quatre pétales. La fleur terminée en huit erreurs : le mot n'a pas été trouvé.
- **Pièce** : fiche d'une page (R11, fonction `mot_cache_fleur`) : le modèle de la fleur en huit étapes numérotées, puis trois zones de partie (tirets, alphabet à barrer, cadre « ma fleur »).
- **Recette** : `mot_cache_fleur(base, parties, titre)`.
- **Vigilance** : le mot vient de la liste de la semaine ; il est écrit en secret et montré à la fin.
- **Interdits** : potence, pendu ou toute image de violence ; mot inconnu des élèves.
- **Statut** : un format produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### Variantes par tranche d'âge (19.11.2026 ; formats calculés et rendus en miniature, non testés en classe)

- **Principe** : chaque gabarit de jeu existe en trois formats : moins de pièces ou de cases et une écriture plus grande pour les plus jeunes, davantage de pièces et une écriture plus petite ensuite. L'IA lit la tranche du degré demandé et applique les nombres ci-dessous ; les valeurs sont celles du dictionnaire `VARIANTES` (Annexe I-C), par planche A4.
- **Corps minimal du texte des pièces** : 24 pt de la 1P à la 4P (18 pt admis en 3P-4P, § 2.1), 14 pt de la 5P à la 8P (12 pt admis en 7P-8P), 12 pt de la 9S à la 11S (valeurs retenues le 21.11.2026, non testées en classe).
- **Affichage** (MP-J-13) : quand le degré est connu, l'IA montre la page de miniatures de la tranche (`miniatures_tranche`, ou les fichiers « Jeux par tranche d'âge » de la boîte à outils) à la place du panorama général.
- **Plateaux J5** : au cycle 3, les cases descendent à 2,1 cm au moins : prévoir des jetons plutôt que des pions (`case_min_mm=20`).
- **Gabarits absents d'une tranche** : J12 (lettres à fabriquer) seulement de la 1P à la 4P ; J14 (cartes d'erreurs) dès la 5P ; J9 demande de lire et d'écrire un prénom : dès la 3P (inférences de conception).
- **J1 — Domino-boucle** : 1P-4P : 10 dominos (9,3 × 5,3 cm · 26 pt) ; 5P-8P : 16 dominos (9,3 × 3,3 cm · 18 pt) ; 9S-11S : 20 dominos (9,3 × 2,6 cm · 14 pt).
- **J2 — Memory, appariement** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 40 pt) ; 5P-8P : 12 cartes (6,2 × 6,6 cm · 22 pt) ; 9S-11S : 20 cartes (4,7 × 5,3 cm · 14 pt).
- **J3 — Familles** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 24 pt) ; 5P-8P : 9 cartes (6,2 × 8,8 cm · 16 pt) ; 9S-11S : 16 cartes (4,7 × 6,6 cm · 12 pt).
- **J4 — Cartes recto-verso** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 18 pt) ; 9S-11S : 15 cartes (6,2 × 5,3 cm · 14 pt).
- **J5-a — Plateau · serpent** : 1P-4P : 19 cases (case de 3,8 cm au moins) ; 5P-8P : 34 cases (case de 2,9 cm au moins) ; 9S-11S : 53 cases (case de 2,3 cm au moins).
- **J5-b — Plateau · escargot** : 1P-4P : 15 cases (case de 3,2 cm au moins) ; 5P-8P : 27 cases (case de 2,5 cm au moins) ; 9S-11S : 42 cases (case de 2,1 cm au moins).
- **J5-c — Plateau · chemin** : 1P-4P : 21 cases (case de 3,6 cm au moins) ; 5P-8P : 34 cases (case de 2,7 cm au moins) ; 9S-11S : 55 cases (case de 2,2 cm au moins).
- **J5-d — Plateau · circuit** : 1P-4P : 16 cases (case de 4,4 cm au moins) ; 5P-8P : 24 cases (case de 3,1 cm au moins) ; 9S-11S : 34 cases (case de 2,3 cm au moins).
- **J6 — Dé à monter** : 1P-4P : 1 dé (faces de 6 cm) ; 5P-8P : 2 dés (faces de 4,2 cm) ; 9S-11S : 2 dés (faces de 4,2 cm). Les deux formats de dé sont possibles à tout âge.
- **J7 — Loto** : 1P-4P : 6 cartons (4 cases de 4,7 × 4,4 cm) ; 5P-8P : 8 cartons (6 cases de 3,1 × 3,3 cm) ; 9S-11S : 6 cartons (9 cases de 3,1 × 2,9 cm).
- **J8 — Symboles communs** : 1P-4P : 7 cartes (3 éléments par carte · 9,3 × 6,6 cm) ; 5P-8P : 13 cartes (4 éléments par carte · 6,2 × 5,3 cm) ; 9S-11S : 21 cartes (5 éléments par carte · 6,2 × 3,8 cm).
- **J9 — Trouve quelqu'un qui…** : 1P-4P : 6 cases (9,3 × 7,5 cm) ; 5P-8P : 16 cases (4,7 × 5,6 cm) ; 9S-11S : 25 cases (3,7 × 4,5 cm).
- **J10 — Carte à pinces** : 1P-4P : 6 questions (bloc de 4,0 cm · 3 réponses) ; 5P-8P : 10 questions (bloc de 2,5 cm · 3 réponses) ; 9S-11S : 12 questions (bloc de 2,1 cm · 3 réponses).
- **J11 — Roue à fenêtre et rabat** : 1P-4P : 4 secteurs (deux disques de 12,4 cm) ; 5P-8P : 6 secteurs (deux disques de 12,4 cm) ; 9S-11S : 8 secteurs (deux disques de 12,4 cm).
- **J12 — Lettres à fabriquer** : 1P-4P : 4 plaques (9,3 × 13,2 cm · 130 pt) ; 5P-8P : non proposé ; 9S-11S : non proposé.
- **J13 — Cartes de rôle** : 1P-4P : 4 cartes (9,3 × 13,2 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 16 pt) ; 9S-11S : 8 cartes (9,3 × 6,6 cm · 14 pt).
- **J14 — Cartes d'erreurs** : 1P-4P : non proposé ; 5P-8P : 4 cartes (9,3 × 13,2 cm · 16 pt) ; 9S-11S : 6 cartes (9,3 × 8,8 cm · 14 pt).
- **J15 — Cartes d'aide graduée** : 1P-4P : 4 cartes (9,3 × 13,2 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 16 pt) ; 9S-11S : 8 cartes (9,3 × 6,6 cm · 14 pt).
- **J16 — Cartons-réponses** : 1P-4P : 4 cartons (9,3 × 13,2 cm · 110 pt) ; 5P-8P : 4 cartons (9,3 × 13,2 cm · 110 pt) ; 9S-11S : 6 cartons (9,3 × 8,8 cm · 90 pt).
- **J17 — Grille d'alignement** : 1P-4P : 20 ronds (ronds de 3,9 cm · aligner 3) ; 5P-8P : 35 ronds (ronds de 2,9 cm · aligner 4) ; 9S-11S : 48 ronds (ronds de 2,6 cm · aligner 4).
- **J18 — Serpents et échelles** : 1P-4P : 30 cases (case de 3,7 cm au moins) ; 5P-8P : 48 cases (case de 3,0 cm au moins) ; 9S-11S : 80 cases (case de 2,3 cm au moins).
- **J19 — Bataille navale** : 1P-4P : 25 cases par grille (case de 2,0 cm au moins) ; 5P-8P : 36 cases par grille (case de 1,6 cm au moins) ; 9S-11S : 64 cases par grille (case de 1,2 cm au moins).
- **J20 — Roue de tirage** : 1P-4P : 4 secteurs ; 5P-8P : 6 secteurs ; 9S-11S : 8 secteurs (roue de 18,2 cm dans les trois cas).
- **J21 — Puzzles à deux pièces** : 1P-4P : 8 puzzles (9,3 × 6,6 cm · 28 pt) ; 5P-8P : 12 puzzles (9,3 × 4,4 cm · 20 pt) ; 9S-11S : 18 puzzles (6,2 × 4,4 cm · 14 pt).
- **J22 — Puzzle à bandes** : 1P-4P : 5 bandes de 3,7 cm ; 5P-8P : 10 bandes de 1,9 cm ; 9S-11S : 12 bandes de 1,6 cm.
- **J23 — Mot mystère** : 1P-4P : 4 mots (cases de 2 cm) ; 5P-8P : 6 mots (cases de 2 cm) ; 9S-11S : 8 mots (cases de 1,45 cm dans l'exemple).
- **J24 — Cocotte en papier** : 8 défis dans les trois tranches ; corps de 14 pt (1P-4P), puis de 12 pt.
- **J25 — Horloge à aiguilles** : 1P-4P : heures seules ; 5P-8P : heures et minutes ; 9S-11S : heures, minutes et heures de 13 à 24.
- **J26 — Mémo-fiches en éventail** : 1P-4P : 6 fiches (6,2 × 13,2 cm · 22 pt) ; 5P-8P : 8 fiches (4,65 × 13,2 cm · 15 pt) ; 9S-11S : 10 fiches (3,72 × 13,2 cm · 12 pt).
- **J27 — Bandes graphiques** : 1P-4P : 4 bandes de 6,6 cm ; 5P-8P : 6 bandes de 4,4 cm ; 9S-11S : 8 bandes de 3,3 cm.
- **J28 — Plateau à camemberts** : 1P-4P : 37 cases ; 5P-8P : 49 cases ; 9S-11S : 73 cases (case de 1,2 cm au moins).
- **J29 — Cherche et trouve de mots** : 1P-4P : 20 mots en 24 pt ; 5P-8P : 40 mots environ en 16 pt ; 9S-11S : 65 mots environ en 13 pt.
- **J30 — Mots interdits** : non proposé de la 1P à la 4P ; 5P-8P : 9 cartes (6,2 × 8,8 cm · 3 mots interdits) ; 9S-11S : 12 cartes (6,2 × 6,6 cm · 5 mots interdits).
- **J31 — Petit bac** : 1P-4P : 3 catégories, 4 manches ; 5P-8P : 5 catégories, 6 manches ; 9S-11S : 6 catégories, 8 manches.
- **J32 — Cartes à terminaisons** : proposé de la 5P à la 8P : 12 cartes-phrases (9,3 × 4,4 cm · 16 pt) et 24 cartes-terminaisons.
- **J33 — Petits chevaux** : un seul format : 52 cases de 1,24 cm.
- **J34 — Qui est-ce ?** : 1P-4P : 12 éléments ; 5P-8P : 24 éléments ; 9S-11S : 30 éléments.
- **J35 — Bataille** : 1P-4P : 12 cartes (6,2 × 6,6 cm · 30 pt) ; 5P-8P : 16 cartes (4,65 × 6,6 cm · 24 pt) ; 9S-11S : 20 cartes (4,65 × 5,28 cm · 22 pt).
- **J36 — Tuiles-lettres** : 1P-4P : 48 tuiles ; 5P-8P : 117 tuiles ; 9S-11S : 204 tuiles.
- **J37 — Sudoku** : 1P-4P : 4 grilles de 4 × 4 ; 5P-8P : 2 grilles de 6 × 6 ; 9S-11S : 2 grilles de 9 × 9.
- **J38 — Mot caché : la fleur** : un seul format : 3 parties par fiche, fleur en 8 étapes.

### Modèles Word à remplir et planches prêtes à imprimer (boîte à outils, 19.11.2026)

- **Principe** : la boîte à outils contient des fichiers que l'enseignant·e peut utiliser sans IA. L'IA les **signale** quand le gabarit retenu en possède un (MP-J-13), en particulier quand elle ne peut pas livrer de fichier ; si l'enseignant·e joint un modèle, l'IA le remplit **sans modifier les dimensions** des cases ni les repères de coupe.
- **Modèles Word à remplir** (dossier « 06_Modèles de jeux à remplir ») : une page de mode d'emploi, puis les planches des trois tranches d'âge, textes d'exemple en gris à remplacer : J1 dominos ; J2 memory (dos à motif, feuille des paires) ; J3 familles ; J4 cartes de rappel (recto-verso) ; J5 cartes-défis des plateaux (dos à motif, feuille de solutions) ; J7 loto (cartons, cartes d'appel à dos à motif, feuille de contrôle) ; J8 symboles communs (cartes construites et vérifiées par programme) ; J9 grille « Trouve quelqu'un qui… » ; J10 carte à pinces (recto-verso) ; J12 lettres à fabriquer (1P à 4P seulement) ; J13 cartes de rôle ; J14 cartes d'erreurs (recto-verso) ; J15 cartes d'aide graduée ; J16 cartons-réponses ; J28 cartes-questions à six catégories (dos à motif).
- **Planches prêtes à imprimer** (dossier « 07_Planches de jeu prêtes à imprimer », PDF) : plateaux de parcours J5 (quatre formes, trois tranches d'âge) ; dés à monter J6 (grand et petit) ; roues à fenêtre et rabat J11 (trois exemples, à 4, 6 et 8 secteurs) ; grilles d'alignement J17, serpents et échelles J18, fiches de bataille navale J19 et roues de tirage J20 (trois tranches d'âge, versions à nombres ou à lettres) ; exemples des gabarits J21 à J27, un par tranche d'âge (puzzles à deux pièces, puzzle à bandes, mot mystère, cocotte, horloge, mémo-fiches en éventail, bandes graphiques) ; plateaux à camemberts J28, planches de cherche-et-trouve J29, cartes à mots interdits J30 et grilles de petit bac J31 ; cartes à terminaisons J32, petits chevaux J33, grilles de « Qui est-ce ? » J34, cartes de bataille J35, tuiles-lettres J36, sudokus J37 avec solutions, fiche du mot caché J38 ; pages de lignes d'écriture au lignage romand G22 (modules de 7 mm, 4 mm et 2,5 mm) et livret d'écriture A5 ; fiches « syllabes et sons » G23, maisons des nombres G24, reproductions sur quadrillage G25, calendriers G26, étiquettes de l'horaire G27, livret à onglets G28, pages de journal G29, planches de bande dessinée G30 et plans d'exposé G31 ; dos à motif (losanges, carreaux, vagues).
- **Limite** : les modèles reprennent les formats des variantes par tranche d'âge ; pour un autre nombre de pièces, l'IA produit la planche avec `planche_pdf`.
- **Statut** : chaque gabarit J1 à J38 a un document réel depuis le 20.11.2026 ; c'est de ces documents, et d'eux seuls, que sont tirées les miniatures du panorama des jeux et des pages par tranche d'âge (table `SOURCES_JEUX`, Annexe I-C). Modèles et planches produits et regardés sur le rendu (LibreOffice, PDF) les 19 et 20.11.2026 ; non imprimés, non testés en classe ; rendu dans Word non contrôlé.

### Variantes de J2, J3 et J4 (non testées)

- **J2, appariement par la forme** (BDRP-C3) : chaque paire reçoit une coupe différente, ce qui corrige par la forme. Dessin vectoriel R11.
- **J2, cartes en double version** (BDRP-C8) : une version réunit image et mot ; elle sert de corrigé à l'association des cartes séparées. Le code couleur de lot est doublé d'un repère écrit.
- **J3, demande par propriété** (BDRP-D4b) : pour obtenir une carte, l'élève nomme la propriété recherchée.
- **J4, cartes construites par l'élève** (BDRP-C4) : l'élève écrit la réponse, fait corriger, découpe ; une carte réussie sort du paquet, une carte ratée y retourne.

# ÉTAPE 4 — CONSTRUIRE : STYLES ET RECETTES TECHNIQUES

## 4.1 Un rôle, un style (MP-S-01)

L'IA DEVRAIT créer des styles de paragraphe nommés et les utiliser pour **chaque** élément de même rôle. L'homogénéité visuelle (MP-O-09) devient ainsi structurelle, et l'enseignant·e peut ajuster une taille en un seul endroit. À défaut de styles nommés, la mise en forme directe DOIT être identique pour tous les éléments d'un même rôle.

| Style | Rôle | Réglages (5P-6P ; adapter la taille au degré) |
|---|---|---|
| Fiche-Identité | 1re ligne : Prénom et Date | 14 pt ; lignes par tabulation à points de suite (R7) |
| Fiche-Titre | titre de la fiche | 16-18 pt, gras, **centré**, espace avant et après ≥ 12 pt |
| Fiche-Objectif | objectif formulé pour l'élève | 14 pt ; la phrase seule, sans étiquette (« J'écris… ») ; espace après 12 pt |
| Fiche-Consigne | numéro + consigne | 14 pt, gras ; espace avant 10 pt ; solidaire du suivant |
| Fiche-Données | items, textes, phrases sources | 14 pt ; interligne 1,5 ; solidaire |
| Fiche-Lacune | items à lacune (R2) | 14 pt ; interligne 2,0 ; solidaire |
| Fiche-Exemple | exemple résolu | 14 pt ; l'exemple (ou la réponse d'un item déjà fait) en police d'élèves GE Typo Libre, 17,5 pt, sans gras ni italique (MP-T-10, `ecrire_exemple`) ; solidaire |
| Fiche-Aide | contenu d'un encadré d'aide | 13-14 pt dans un encadré R5 |
| Fiche-Bilan | autoévaluation | 14 pt dans un tableau R6 |
| Fiche-Étape | étape d'une règle du jeu | 14 pt ; numéro, tabulation, texte ; retrait suspendu de 0,8 cm ; une action par étape |
| Fiche-Pièce | texte d'une pièce de jeu (R8) | taille du degré, centré, interligne simple, sans espace avant ni après |
| Fiche-Mention | mention d'une planche (« à découper sur les pointillés ») | 11 pt, italique ; texte destiné à l'adulte qui découpe (inférence de conception) |
| Ens-Titre / Ens-Texte | partie enseignant·e | 13 pt gras / 11 pt |
| Affiche-Titre, Affiche-Texte, Affiche-Étape, Affiche-Détail, Affiche-Cellule | rôles d'une affiche A3 (GF-V) | 72 pt gras centré ; 48 pt ; 48 pt ; 36 pt ; 36 pt centré (§ 2.5) |


## 4.2 Recettes

### R8 — Planche de pièces à découper (jeux J1 à J6)

- **Tableau à largeurs fixées** : une colonne par moitié de pièce (pour J1 : 4 colonnes de 4 cm, soit deux dominos de 8 cm par rangée) ; largeur et hauteur totales calculées pour occuper toute la surface utile (MP-J-11), en agrandissant les pièces ou en changeant le nombre de colonnes et de rangées ; jamais de largeur automatique.
- **Repères de coupe** (MP-J-12) : un trait fin dans le prolongement de chaque ligne de coupe, dans les quatre marges. Dans Word : formes « Trait » positionnées par rapport à la page ; plus sûr : planche produite en PDF par le code (traits, pointillés et repères dessinés aux coordonnées exactes), contrôlée sur le rendu (V12) : fonctions `planche_pdf` (pièces de texte, dominos compris) et `reperes_de_coupe` de l'Annexe I-C (19.11.2026). Les planches à zones (R14) restent en .docx : marges de la section réduites à 1,2 cm sur les côtés et à 1,65 cm en haut et en bas, repères ajoutés en formes « Trait » ; aucune fonction ne les pose à ce jour.
- **Lignes à hauteur exacte et insécables** (2,5 cm pour J1).
- **Bordures définies cellule par cellule**, jamais par une bordure globale du tableau : contour de chaque pièce en **pointillés** (trait de coupe, 1 pt) ; séparation interne d'une pièce en **trait plein épais** (2,25 pt) (MP-J-05).
- **Saut de page avant chaque planche** (attribut « saut de page avant » sur la mention de la planche) ; une planche = une page ; une mention courte en haut (style Fiche-Mention), par exemple « Boucle Lune · 16 dominos · à découper sur les pointillés ».
- **Texte des pièces** : style Fiche-Pièce, centré verticalement et horizontalement ; la réponse en gras.
- **Ordre des pièces** : mélangé (MP-J-03 ; fonction `melanger_sans_voisins` de l'Annexe I-C).
- Dans Word : Insertion > Tableau ; Propriétés du tableau > Colonne (largeur fixe) et Ligne (hauteur exacte, fractionnement des lignes interdit) ; Bordures et trame > appliquer à la **cellule** (pointillés ou trait plein épais).
- Testé dans cette version : planche de 2 × 8 dominos rendue avec des rangées de 2,50 cm, une largeur de 16,0 cm et une hauteur de 20,7 cm de la marge haute au dernier trait ; fichier valide au schéma OOXML. Testé le 19.11.2026 : memory des consignes, 12 planches de 3 × 4 cartes de 6,2 × 6,6 cm (18,6 × 26,4 cm) produites en PDF avec repères de coupe et mention dans la marge du haut ; mots centrés sur leur boîte d'encre (le centrage d'images dans des cellules de tableau Word décalait légèrement les mots).

### R10 — Écriture liée composée (v7.2)

- L'écriture liée est **composée** en GE Typo Libre (`ecrire_cursive`) : jamais dessinée, jamais générée par une IA (MP-CC-11).
- Vérifié dans la session : famille exacte « GE Typo Libre », nom PostScript GETypoLibre, fichier `ge_typo_libre.otf`, incorporation autorisée (fsType 0) ; lettres accentuées, œ, guillemets et apostrophe présents. Le **point médian n'a pas de dessin visible** : la fonction le refuse.
- Le logiciel relie les lettres avec les ligatures de la police. Contrôle : V15, `verifier_cursive_pdf`.
- TrueRomande n'est jamais utilisée pour du texte composé automatiquement (MP-T-09) : les glyphes de É, À, « et » manquent, vérifié dans la session.
- Sans police installée : l'IA le déclare, laisse le modèle en script et écrit « écriture liée à ajouter par l'enseignant·e ».

### R11 — Dessin vectoriel (v7.2)

- Pour ce que le .docx construit mal : tracés, labyrinthes, disques, schémas. La classe `Dessin` écrit le même dessin en SVG et en PDF, à l'échelle 1, en millimètres.
- `couloir`, `arrondir`, `labyrinthe`, `roue_J11` servent G19 et J11 ; `plateau_parcours` (19.11.2026) sert J5 ; `de_a_monter` (19.11.2026) sert J6 ; `dos_a_motif` (19.11.2026) imprime le dos des cartes tirées ; `grille_alignement`, `serpents_echelles`, `bataille_navale` et `roue_tirage` (19.11.2026) servent J17 à J20 ; `puzzle_association`, `puzzle_bandes`, `mot_mystere`, `cocotte`, `horloge`, `eventail` et `bandes_graphiques` (20.11.2026) servent J21 à J27 ; `plateau_camemberts`, `planche_lynx`, `cartes_mots_interdits` et `petit_bac` servent J28 à J31, `lignage_romand` et `livret_ecriture` servent G22 ; `cartes_categories` (J28), `petits_chevaux`, `grille_qui_est_ce`, `tuiles_lettres`, `sudoku` et `mot_cache_fleur` servent J33 à J38, `fiche_syllabes_sons` sert G23 ; `maison_des_nombres`, `reproduction_quadrillage`, `calendrier_mensuel`, `etiquettes_horaire`, `livret_a_onglets`, `page_journal`, `planche_bd` et `plan_expose` (21.11.2026) servent G24 à G31 ; `panorama_supports` montre les fiches et supports qui ont un document prêt ; `panorama_jeux` et `panorama_exercices` montrent les gabarits disponibles.
- Insertion dans un .docx : image PNG à 300 ppp, avec `inserer_image`, à la largeur du dessin. Le fichier source reste le SVG ou le PDF. **Couleur (option, 21.11.2026)** : `definir_couleur('bleu')` avant l'appel d'une fonction de dessin teinte les fonds gris (cases spéciales, bandeaux, zones), les symboles de catégorie et les traits du dos des cartes ; teintes disponibles : bleu, orange, vert, violet, ciel, vermillon ; `definir_couleur(None)` revient au noir et blanc. La clarté de chaque gris est conservée : une photocopie en noir et blanc donne le même document. Les modèles Word à remplir ne sont pas concernés.
- Les icônes de la banque IC passent par `icone`. `Dessin` requiert PyMuPDF ; les chemins de police (`POLICES_PDF`) sont ceux de macOS, à adapter sur un autre système.

### R12 — Planche recto-verso (v7.2)

- `verso_de` inverse les colonnes d'une planche, pour une impression sur le bord long. Pour J10, la colonne des réponses passe au bord gauche du verso ; l'ordre des lignes est inchangé (`carte_a_pinces`, verso=True).
- Le PDF ne prouve pas l'alignement : V13 reste obligatoire sur papier.

### R13 — Contrôles combinatoires (v7.2)

- `generer_loto` et `verifier_loto` (J7), `plan_projectif` et `verifier_symboles` (J8), `verifier_appariement` (J2, J7, J10), `verifier_code` (GF-X : chaque énigme porte son calcul, qui doit donner un chiffre de 0 à 9), `verifier_graphemes` (GF-J, SP10, cartes de sons).
- Ces contrôles s'exécutent **avant** la mise en page (V11, V19, V21).

### R14 — Grille et planche à zones (v7.2)

- `grille` : tableau à largeurs fixées dont chaque cellule reçoit du texte, une image ou de l'écriture liée.
- `planche_zones` étend R8 : pièce découpée en zones superposées, sous-cellules côte à côte, contour en pointillés, séparations internes fines.
- `verifier_case_piece` (révision du 2.11.2026, suite ; MP-J-10) : reçoit les dimensions de la pièce mobile et de la case d'accueil (largeur et hauteur en cm) et refuse toute case qui ne dépasse pas la pièce d'au moins 0,5 cm par côté ; appelée avant `grille` pour tout plateau, tableau ou fiche qui reçoit des pièces mobiles (G12-b, J10 : la pince ; SP5 sur un tableau de journée).
- **Mots coupés** : dans toute cellule, un mot qui se coupe impose une cellule plus large, un item plus court ou une taille réduite dans les limites du degré ; jamais de césure (règle commune à R14 et R15 ; `verifier_mots_coupes` sur le texte extrait du PDF, V12 et V10).

### R15 — Planche A5 (révision du 2.11.2026)

- Pour un contenu court qui laisserait une page A4 à moitié vide (MP-O-14) : règle de jeu, petite fiche, bande, ticket, brevet. La feuille A4 porte **deux exemplaires identiques**, séparés par un **trait de coupe en tirets** (1 pt) ; on imprime deux fois moins et on coupe la feuille en deux.
- **Côte à côte** : A4 paysage, deux colonnes A5 portrait ; marges de 1 cm ; retrait intérieur de 0,9 cm ; largeur de contenu 12,05 cm. **Empilé** : A4 portrait, deux rangées A5 paysage ; largeur de contenu 17,2 cm.
- Le contenu garde les tailles du degré (MP-T-01) ; seules les largeurs (tableaux, lignes, images) suivent la largeur de l'exemplaire. Un mot qui se coupe mal dans une cellule étroite impose une cellule plus large ou une taille plus petite dans les limites du degré.
- La planche ouvre une **section propre** ; si le document continue après elle, la section suivante reprend l'A4 et ses marges (`nouvelle_section_a4`).
- Contrôle : V20 sur chaque exemplaire (budget A5 portrait 16,9 cm ; A5 paysage 12,3 cm), trait de coupe exclu de la mesure.
- Dans Word : Mise en page > Orientation > Paysage ; Marges 1 cm ; tableau de deux colonnes de 13,85 cm, ligne de hauteur « au moins » 18,9 cm ; bordure en tirets sur le bord commun seulement ; contenu copié dans les deux cellules.
- Fonction `planche_A5` de l'Annexe I-C. Testé dans cette version : règles de GF-X, J7 et J8, GF-B2 (côte à côte) ; GF-M (empilé) ; remplissage mesuré de 90 % au moins par exemplaire.

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
- dans « En bref », **ce qui fait apprendre** dans ce jeu, en une ou deux phrases : le mécanisme qui fait travailler l'objectif (rappel actif, retour immédiat, nombre de réponses par élève et par partie, verbalisation), et ce qui ferait perdre l'apprentissage (attente, hasard dominant, réponse visible) ;
- dans « Déroulement conseillé », une **mise en commun** après la partie : ce qu'on a appris, les erreurs fréquentes, la règle ou la procédure à retenir ;
- dans « Corrigé expliqué », la **solution du jeu** (ordre de la boucle, paires ou familles), avec un « Pourquoi » pour chaque pièce ;
- dans « Différenciation », les **variantes de jeu** : solo, à trois, mélange des lots ; Pour tout jeu de parcours ou de compétition, proposer aussi une **variante coopérative**, fondée sur l'interdépendance positive et la responsabilité individuelle (Johnson & Johnson, 2009) : un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance seul ; un but commun chiffré (tous les pions arrivés en moins de dix tours, vingt cartes réussies) ; des rôles tournants (J13) ; l'aide qui rapporte (si l'explication d'un camarade permet de répondre, les deux avancent) ; l'erreur sans recul (le groupe explique, puis l'élève rejoue) ; des binômes par pion ; un bilan de fin de partie (« qu'est-ce qui nous a aidés ? »).
- dans le rapport de conformité, les contrôles **V11 à V13** (et V14 si le fichier est produit par du code ; V15 à V19 selon le gabarit ; V20 et V21 toujours).

**Pour un jeu ou une dictée**, la partie enseignant·e est une page à part entière, jamais oubliée (V21) : pour un jeu, la règle complète, la solution et le débriefing ; pour une dictée (G20), le texte à dicter en entier. La règle destinée aux élèves est imprimée avec le matériel, en étapes numérotées (MP-J-07), en planche A5 si elle tient sur une demi-page (R15). Avant le test en classe, elle renvoie à la grille « utile, utilisable, acceptable » (Tricot et al., 2003 ; Bibliothèque IA 2).


# ÉTAPE 6 — LIVRER


## 6.1 Gabarits de fiches et de dossiers de jeu

### GF-F — Dossier de jeu (règle 1 page par groupe ; 1 page par planche ; trace 1 page)

Pièces du dossier, dans cet ordre :

1. **Règle du jeu et carte-mémoire** (1 page par groupe) : titre centré, sans ligne Prénom et Date (MP-J-09) ; phrase d'organisation ; exemple résolu fait de pièces hors lot ; règle en étapes numérotées (style Fiche-Étape, une action par étape) ; carte-mémoire (tableau de référence) dont la règle précise qu'elle sert à vérifier après la pose.
2. **Planches** (annexes à découper) : une page par planche (R8), mention courte en haut ; un lot par couleur de papier, sans repère de niveau (MP-J-06).
3. **Fiche de trace individuelle** (1 page au maximum) : en-tête R7 ; un ou deux exercices G (par exemple G3 et G7) qui font écrire la forme travaillée ; bilan R6.
4. **Partie enseignant·e** (fichier séparé) : structure du § 4.3, avec le tableau d'impression, la solution du jeu et les variantes.

```
<Titre du jeu>                                   [titre centré, sans Prénom ni Date]
Joue avec un ou une camarade.
Exemple : <question> donne <réponse>.            [Fiche-Exemple ; <réponse> en police d'élèves, MP-T-10]
[2 pièces hors lot]                              [R8 sans saut de page]
1  <Une action>                                  [Fiche-Étape]
2  <Une action>
…
<Carte-mémoire>                                  [tableau de référence]
—— saut de page avant chaque planche ——
<Lot> · <n> pièces · à découper sur les pointillés   [Fiche-Mention]
[planche R8 : ordre mélangé, coupe en pointillés, séparation en trait plein épais]
—— saut de page ——
Prénom : ____________________     Date : ______________   (R7, 1re ligne)
                     <Titre de la trace écrite>
<objectif en langage élève, sans étiquette>
1  <Consigne : écrire la forme travaillée>
   a) …   b) …   c) …
[bilan R6]
```


# ANNEXE I-A — STANDARD DE MISE EN PAGE MP-* (RÉFÉRENCE DES CODES)

## Règles détaillées

### MP-P — Principes de conception

| Id | Règle | Niveau |
|---|---|---|
| MP-P-01 | Concevoir le document à partir des besoins, des connaissances et des capacités des élèves visés. | DOIT |
| MP-P-02 | La mise en page facilite la tâche ; elle ne doit pas devenir une difficulté supplémentaire. Une mise en page cohérente réduit la charge cognitive inutile ; des repères visuels stables favorisent l'autonomie ; une bonne lisibilité réduit la fatigue de lecture et les erreurs. | DOIT |
| MP-P-03 | La disposition rend les actions évidentes ; la cohérence visuelle permet d'identifier rapidement ce qu'il faut faire et le rôle de chaque élément. | DOIT |
| MP-P-04 | Adapter l'interface (vocabulaire, syntaxe, structure, densité) au public cible. | DOIT |
| MP-P-05 | Penser la ressource selon son contexte d'usage : lieu (classe, domicile), moment, modalité (autonomie, guidée, devoir, remédiation), matériel disponible, temps et contraintes. | DOIT |
| MP-P-06 | Correspondance tâche–objectif : identifier si l'activité vise surtout à comprendre, agir ou explorer. Le format d'exercice découle de ce choix. | DOIT |
| MP-P-07 | Préférer des structures simples et familières à des organisations originales mais complexes. | DEVRAIT |
| MP-P-08 | Révision après usage : les supports sont testés et ajustés selon les retours. | DEVRAIT |

### MP-F — Format physique et impression

| Id | Règle | Niveau |
|---|---|---|
| MP-F-01 | Format A4. | DOIT |
| MP-F-02 | Orientation portrait par défaut. Le paysage PEUT être utilisé lorsque la tâche l'exige : tableaux larges, frises, cartes, zones de tracé étendues, lignes d'écriture « trottoirs ». | DOIT / PEUT |
| MP-F-03 | Marges de 2,5 cm sur chaque côté. | DOIT |
| MP-F-04 | Aucune information essentielle près des bords. | DOIT |
| MP-F-05 | Vérifier la cohérence du format et de l'orientation avec la tâche. | DOIT |
| MP-F-06 | **Largeur utile** : 16 cm en portrait (21 − 2 × 2,5), 24,7 cm en paysage (29,7 − 2 × 2,5). Aucune ligne d'écriture, aucun tableau ne dépasse cette largeur. | DOIT |

### MP-T — Typographie et hiérarchie visuelle

| Id | Règle | Niveau |
|---|---|---|
| MP-T-01 | Une police (idéal), deux au maximum ; au-delà de trois, la lisibilité diminue fortement. | DOIT |
| MP-T-02 | Lecteurs novices : police sans empattement (Arial, Verdana, Tahoma, Calibri) ou police scolaire locale. Lecteurs experts : police avec empattement possible. | DOIT / PEUT |
| MP-T-03 | Pas de texte entièrement en MAJUSCULES ; les capitales servent uniquement à attirer ponctuellement l'attention. | DOIT |
| MP-T-04 | Pas de soulignement ni d'italique excessifs. | DOIT |
| MP-T-05 | Pas d'effets décoratifs (ombres, reliefs, contours, ombrages) : incompatibles avec la photocopie. | DOIT |
| MP-T-06 | Hiérarchie d'accentuation, du plus discret au plus marqué : petites capitales → italique → capitales → gras → taille supérieure → autre police. Utiliser le niveau le plus faible suffisant. | DEVRAIT |
| MP-T-07 | Alignement à gauche pour les textes et consignes ; **pas de texte justifié** ; centrage réservé aux titres courts ou éléments isolés. | DOIT |

**Tailles de caractères par degré** (reprises dans la table 2.1)

| Degré | Taille du texte lu par l'élève |
|---|---|
| 1P-2P | 24 pt |
| 3P-4P | 18 pt |
| 5P-6P | 14 pt |
| 7P-8P | 12 pt |

Une réduction progressive est possible au cours du cycle.

### MP-E — Interlignes et zones d'écriture

| Id | Règle | Niveau |
|---|---|---|
| MP-E-01 | Interligne de lecture : 1,5. | DOIT |
| MP-E-02 | Interligne d'écriture : 2,0 minimum, ou lignes calibrées. | DOIT |
| MP-E-03 | Lignes d'écriture primaire calibrées à environ 8-10 mm. | DEVRAIT |
| MP-E-04 | Ne jamais coller la consigne et la zone de réponse. | DOIT |
| MP-E-05 | Au moins deux lignes pour une phrase produite. | DOIT |
| MP-E-06 | Espaces suffisants pour éviter une écriture compressée. | DOIT |
| MP-E-07 | Repères : réponse courte ≈ 6-8 cm ; phrase complète ≈ 10-14 cm ; production longue : 5-6 lignes sur la largeur utile. | DEVRAIT |
| MP-E-08 | Apprentissage du geste d'écriture : des « trottoirs » (trois lignes, dont une ligne principale) sur feuille en paysage permettent de travailler l'espacement entre les mots. La ligne principale DOIT rester identifiable sans couleur (épaisseur, trait). | PEUT |
| MP-E-09 | Pas de zone d'écriture pour les tâches sans production écrite (entourer, souligner, relier, cocher, colorier) : prévoir seulement l'espace nécessaire au geste. | DEVRAIT |

#### Table de dimensionnement des zones de réponse

| Réponse attendue | Zone |
|---|---|
| Un mot, un nombre | 1 ligne de 6-8 cm |
| Une phrase (production ou transformation) | au moins 2 lignes ; longueur 10-14 cm, au maximum la largeur utile (16 cm) |
| Production courte (mini-récit, description) | 5-6 lignes pleine largeur utile |
| Tableau à compléter | cellules d'au moins 5-6 cm de large et ≥ 1 cm de haut |
| Geste sans écriture | aucune ligne ; espace blanc autour des items |

### MP-O — Organisation et densité de page

| Id | Règle | Niveau |
|---|---|---|
| MP-O-01 | Structure stable : numéro → consigne → données → zone de réponse ; identique dans toute la fiche. | DOIT |
| MP-O-02 | Numérotation stable (1, 2, 3… ou A, B, C…) ; ne pas mélanger plusieurs systèmes à un même niveau. Usage courant : exercices 1, 2, 3 et items a), b), c). | DOIT |
| MP-O-03 | Zone d'identification **tout en haut de la page**, en première ligne : Prénom (ou Nom, selon la préférence de l'enseignant·e) et Date ; puis titre centré, puis objectif en langage élève, sans étiquette (MP-O-12, R7). **Exception pour les jeunes élèves** (1P-2P, et tout élève qui n'écrit pas encore sur une ligne) : aucune ligne « Prénom » ni « Date » ; ces élèves apprennent à écrire leur prénom, en grand, et ne peuvent pas le loger sur une ligne. À la place, la mention « Prénom au dos de la feuille » (l'élève l'écrit en grand au dos, ou y colle son étiquette-prénom) ; la date est notée par l'adulte. Recettes : `entete(..., jeunes=True)` pour Word, `definir_jeunes(True)` pour les fiches dessinées. En 3P-4P, demander à l'enseignant·e s'il faut garder la ligne. | DOIT |
| MP-O-04 | Au maximum 3-5 exercices courts par page, ou 1-2 exercices longs. | DOIT |
| MP-O-05 | Maintenir des espaces de respiration visuelle ; éviter la surcharge. | DOIT |
| MP-O-06 | Ne jamais séparer une consigne et son exercice par un saut de page ; ne jamais couper un tableau ou une activité entre deux pages. | DOIT |
| MP-O-07 | Réduire le nombre d'étapes entre la consigne et l'action. | DOIT |
| MP-O-08 | Blocs d'information clairement séparés ; rôles identifiables : consigne, données, réponse, aide, exemple. | DOIT |
| MP-O-09 | Homogénéité visuelle : un même rôle conserve le même format visuel dans tout le document. | DOIT |
| MP-O-10 | Limiter le nombre d'éléments simultanément visibles. | DOIT |

### MP-I — Images et schémas

| Id | Règle | Niveau |
|---|---|---|
| MP-I-01 | Image uniquement si elle est utile à la tâche ou à la compréhension d'un mot ; supprimer toute image ou décoration inutile. | DOIT |
| MP-I-02 | Placer l'image près de la tâche correspondante, au-dessus ou à gauche ; ne jamais séparer image et tâche par un saut de page. | DOIT |
| MP-I-03 | Lisibilité en noir et blanc et compatibilité photocopie ; éviter fonds gris, lignes fines, contrastes faibles. | DOIT |
| MP-I-04 | Utiliser des schémas ou représentations lorsque cela aide à comprendre, et seulement dans ce cas. | DEVRAIT |

### MP-C — Couleurs et contrastes

| Id | Règle | Niveau |
|---|---|---|
| MP-C-01 | Privilégier le contraste noir sur blanc ; garantir un contraste suffisant pour l'impression. | DOIT |
| MP-C-02 | La couleur n'est jamais l'unique porteur d'information ; l'information reste lisible sans couleur. | DOIT |
| MP-C-03 | Éviter les combinaisons vert/rouge et rouge/bleu, problématiques pour les élèves daltoniens. | DOIT |
| MP-C-04 | Si des couleurs sont utilisées : une même signification garde la même couleur dans tout le document. Pour un dessin R11, la couleur est une option (`definir_couleur`) : une seule teinte par document, qui remplace les gris par une teinte de même clarté ; les symboles de catégorie reçoivent chacun leur teinte, en plus de leur forme. | DOIT |
| MP-C-05 | Codage compatible daltonisme : forme + valeur de gris + couleur, par exemple ● plein / ◐ demi / ○ vide. | DEVRAIT |

### MP-CC — Charge cognitive et principes cognitifs

| Id | Règle | Niveau |
|---|---|---|
| MP-CC-01 | Ne conserver que les informations nécessaires à la tâche. | DOIT |
| MP-CC-02 | Mots concrets ; éviter les termes trop abstraits lorsque l'objectif est une action. | DEVRAIT |
| MP-CC-03 | Complexité syntaxique limitée : phrases courtes, peu de subordonnées. | DOIT |
| MP-CC-04 | Éviter l'attention divisée (*split attention*) : placer explications et aides au plus près des éléments concernés. L'élève ne doit pas chercher une information éloignée. | DOIT |
| MP-CC-05 | Informations multimodales complémentaires et non redondantes. | DEVRAIT |
| MP-CC-06 | Exemple résolu avant une production autonome lorsque la tâche est nouvelle. | DOIT |
| MP-CC-07 | Actions compréhensibles sans inférence ; lecture concise ; étapes réduites. | DOIT |
| MP-CC-08 | Conception simple, minimaliste et sans surcharge. | DOIT |
| MP-CC-09 | Lisibilité universelle : consignes courtes, vocabulaire adapté, hiérarchie visuelle claire. | DOIT |
| MP-CC-10 | Ne jamais pré-marquer (gras, italique, couleur) les éléments que l'élève doit lui-même repérer. | DOIT |

*Ancrage théorique :* théorie de la charge cognitive (Sweller et collègues), apprentissage multimédia (Mayer) : effets d'attention divisée, de redondance, d'exemple résolu, de pré-entraînement.

### MP-CO — Consignes

| Id | Règle | Niveau |
|---|---|---|
| MP-CO-01 | La consigne permet de comprendre immédiatement quoi faire ; une phrase courte suffit dans la majorité des cas. | DOIT |
| MP-CO-02 | Une seule action par phrase ; si plusieurs actions sont nécessaires, les présenter en étapes numérotées. | DOIT |
| MP-CO-03 | Pas de paragraphe de consigne : une consigne trop longue devient une tâche de lecture avant l'apprentissage. | DOIT |
| MP-CO-04 | Consigne directe, **sans titre d'exercice** qui la précède. | DOIT |
| MP-CO-05 | **Éviter la négation** (à proscrire : « Entoure les mots qui ne sont pas des verbes »). | DOIT |
| MP-CO-06 | Consigne placée au-dessus des données, et non à côté (lecture verticale). | DEVRAIT |
| MP-CO-07 | **Cohérence consigne ↔ format de réponse** : nombre de blancs, forme attendue, place disponible correspondent exactement à ce que la consigne demande. | DOIT |
| MP-CO-08 | Verbes de consigne stables d'une fiche à l'autre : souligne, entoure, encadre, relie, complète, coche, écris, classe, colorie, remets dans l'ordre. | DEVRAIT |

### MP-CI — Charge informationnelle par exercice

| Id | Règle | Niveau |
|---|---|---|
| MP-CI-01 | Un exercice ne présente pas trop d'informations simultanément. | DOIT |
| MP-CI-02 | Au maximum **quatre éléments principaux** visibles simultanément. « Élément principal » = bloc distinct (consigne, support ou données, aide, exemple, zone de réponse), et non nombre d'items. Items : 3-5 par défaut ; jusqu'à 6-10 items très courts et de structure identique pour l'automatisation (regrouper visuellement par blocs de 5). | DOIT |
| MP-CI-03 | En cas de surcharge, découper l'activité en étapes successives ; vérifier la lisibilité globale en un coup d'œil. | DOIT |

### MP-A — Aides intégrées et guidage

| Type d'activité | Aides à prévoir |
|---|---|
| **Comprendre** | Vocabulaire adapté ; définition des mots difficiles ; schémas ou représentations lorsque cela aide ; retour sur la compréhension ou la réussite. |
| **S'entraîner, répéter** | Consignes compréhensibles ; retour sur les erreurs ; exercices similaires pour stabiliser et consolider ; possibilité d'analyse d'erreur. |
| **Explorer** | But de la tâche explicite et maintenu visible ; indications pour éviter de se perdre ; repères de progression ; retours intermédiaires. |
| **Toutes** | Définitions nécessaires ; exemple résolu si la tâche est nouvelle ; feedback prévu ou auto-correction possible. |

### MP-PT — Pré-training

**Définition.** Rappel bref des éléments nécessaires avant l'activité. Il active des connaissances sans enseigner la notion complète ; il facilite l'autonomie en entrant dans la tâche sans surcharge liée à l'oubli de notions nécessaires.

#### Règle de décision

| Situation | Décision |
|---|---|
| Notion nouvelle, fragile, réactivée ou combinée | **Ajouter** un pré-training |
| Automatisation | Ne pas ajouter |
| Évaluation certificative | Ne pas ajouter |

#### Formats

| Format | Contenu | Usage |
|---|---|---|
| Minimal | Rappel court + un exemple simple | Cas courant |
| Guidé | Règle courte + deux exemples | Notion fragile |
| Renforcé | Plus développé | Réservé aux tâches complexes |

**Contraintes** : DOIT rester court et directement utile à l'exercice ; DOIT ne jamais dépasser **un quart de page** ; DEVRAIT être placé **avant** l'exercice concerné, au plus près de lui (MP-CC-04).

### Règles ajoutées dans les versions 6, 6.1, 6.2, 7 et 7.2 (et révision du 2.11.2026)

| Id | Règle | Niveau |
|---|---|---|
| MP-P-09 | Examiner l'adéquation de la demande à la progression PER du degré (notion, oral ou écrit, niveau d'attente) ; signaler l'écart et adapter sans refuser. | DOIT |
| MP-O-11 | Budget de page : au plus 22 cm de contenu planifié par page A4 portrait, en-tête compris ; calcul dans la fiche technique avant la rédaction. Exception : planche de pièces à découper (MP-J-11). | DOIT |
| MP-E-10 | Lignes d'écriture construites avec la recette R1 (tableau d'une colonne à hauteur exacte, bordure inférieure seule ; ou tabulation droite à points de suite). Interdits : tirets bas pour une réponse d'une phrase ou plus (X-01) ; paragraphes vides bordés consécutifs (X-02). | DOIT |
| MP-E-11 | Lacune dans une phrase : réservée à 1-2 mots ; nombre de tirets bas calculé selon la police et la taille (table 2.1). | DOIT |
| MP-C-06 | Symboles (☐, ★, ◐) : vérifier leur rendu ; préférer des mots dans des cellules et des cases dessinées (cellules vides bordées). | DEVRAIT |
| MP-S-01 | Un rôle, un style de paragraphe nommé (ou une mise en forme directe strictement identique). | DEVRAIT |
| MP-D-01 à MP-D-06 | Différenciation sans étiquette évaluative, dispositifs, budget par version, attribution, classe multi-âges, encadré « Si je bloque » (voir § 3.6). | DOIT / DEVRAIT / PEUT |
| MP-V-01 | Contrôle sur le rendu imprimé (V1-V10 et V20 ; V11 à V19 selon le cas ; V21) avant livraison, ou déclaration « Rendu non contrôlé » avec la liste des contrôles. | DOIT |
| MP-V-02 | Rapport de conformité livré avec la fiche. | DOIT |
| MP-O-12 | En-tête obligatoire dans cet ordre : Prénom et Date tout en haut (première ligne) ; titre centré avec un espace avant et après (≥ 12 pt) ; objectif en langage élève (une phrase à la première personne, sans étiquette « Mon objectif : » ; révision du 2.11.2026). Recette R7. Jeunes élèves : pas de ligne Prénom et Date (MP-O-03). | DOIT |
| MP-I-05 | Image générée par IA destinée à l'élève : aucun texte produit par le générateur dans l'image (souvent fautif ou inexistant) ; le texte est ajouté dans le document, puis relu (V10). Ni logo, ni marque, ni personne réelle reconnaissable. | DOIT |
| MP-CC-11 | Par défaut, aucune forme écrite fautive ou inexistante dans un support destiné à l'élève (consignes, exemples, items, distracteurs, banques de mots, phrases à corriger) ; alternatives au § 3.7 ; exception encadrée, sur décision de l'enseignant·e, dès la 5P, pour une analyse d'erreurs (quatre conditions, § 3.7) ; relecture orthographique avant livraison (V10). | DOIT |
| MP-V-03 | Statut des informations : vérifié dans la session (avec la source) / non vérifié / inférence de conception. | DEVRAIT |
| MP-J-01 à MP-J-13 | Règles communes aux jeux imprimés : choix présenté avec le panorama des jeux (MP-J-13) ; surface de la planche et repères de coupe (MP-J-11, MP-J-12) ; unicité, aucun indice non visé, ordre mélangé, autocorrection, traits de coupe, aucun repère de niveau, règle en étapes avec exemple hors lot, carte-mémoire pour vérifier, en-tête, case d'accueil ≥ pièce mobile + 0,5 cm par côté (voir § 3.8). (v7 ; MP-J-10 : révision du 2.11.2026, suite) | DOIT / DEVRAIT |
| MP-F-07 | Format A3 admis pour les affiches lues à distance (TR17 à TR22) ; paramètres du § 2.5 ; dérogation explicite à MP-F-01. (v7.2) | PEUT |
| MP-T-08 | Toute police scolaire est déclarée, installée et vérifiée sur le rendu ; sinon, repli libre annoncé. (v7.2, constat T4 du balayage BDRP) | DOIT |
| MP-T-09 | TrueRomande n'est jamais utilisée pour du texte composé automatiquement ; l'écriture liée est composée en GE Typo Libre (R10). (v7.2) | DOIT |
| MP-T-10 | **Exemple en police d'élèves** : partout où un exemple est donné ou affiché (exemple résolu, exemple déjà fait en tête de fiche, exemple d'un rappel, d'une règle de jeu ou d'une affiche, colonne « Exemple » d'un tableau), l'exemple est composé dans la police d'élèves **GE Typo Libre** (R10), comme écrit à la main, pour que l'élève distingue ce qui est donné de ce qui est montré en exemple. Ce qui est donné reste dans la police de la fiche : consigne, règle, intitulé « Exemple », item de départ. Dans un exercice dont le premier item est fait, l'item reste comme les autres et seule la réponse (ce que l'élève écrit, à l'endroit où il l'écrit) passe en police d'élèves. Corps : même hauteur apparente que le texte de la fiche, soit 1,25 fois le corps pour des lettres (17,5 pt pour 14 pt), 0,9 fois pour des chiffres seuls et 1,1 fois pour un mélange de lettres et de chiffres, un seul corps par exemple (`taille_eleve`) ; ni gras ni italique ; un léger retrait au début d'une cellule, la police ayant des attaques qui débordent à gauche. Caractère absent de la police (Â, Ä, Î, Ï, Ö, Ù, Û, Ü, Ÿ, ä, ÿ, æ, –, %, point médian) : le mot reste en script (`ecrire_exemple` le fait seul). Police non installée : repli annoncé (MP-T-08), l'exemple reste en italique. Ne s'applique pas aux données d'un jeu (texte des cartes, des dominos, des plateaux) ni au contenu d'un modèle rempli à adapter. Recettes : `ecrire_exemple`, option `{'eleve': taille}` d'`ecrire`, police `'Eleve'` de `Dessin` (`police_exemple_pdf`). (21.11.2026) | Convention (priorité 5) : appliquée par défaut |
| MP-P-10 | L'IA travaille avec des prénoms fictifs ou des marqueurs ; les prénoms réels sont insérés localement par l'enseignant·e (nLPD). (v7.2, constat T6 du balayage BDRP) | DOIT |
| MP-O-13 | Rubrique « Conditionnement » dans la fiche technique de toute ressource imprimée autre qu'une fiche à photocopier (§ 2.3). (v7.2) | DEVRAIT |
| MP-O-14 | Page pleine : aucune page élève remplie partiellement ; sur le rendu, chaque page atteint au moins 90 % du budget de hauteur (mesure sur l'image de la page) ; sinon aérer, compléter (lignes, items) ou passer en planche A5 (R15). Exceptions déclarées : partie enseignant·e, dernière planche d'un jeu à nombre de pièces fixé. Contrôle V20. (révision du 2.11.2026) | DOIT |


# EXTRAITS DE LA BIBLIOTHÈQUE IA 2

# PARTIE 10 — DÉPLOIEMENT PROGRESSIF ET RÉFÉRENCES

## Repères pour les jeux, la coopération et la différenciation

Ces repères complètent les règles de la Bibliothèque IA 1 (MP-J-07, MP-D-02, § 4.3). Ils servent à conseiller l'enseignant·e avant la production et à justifier les choix dans la partie enseignant·e.

**Évaluer une ressource : utile, utilisable, acceptable**

Le triptyque utilité, utilisabilité, acceptabilité (Tricot et al., 2003) donne trois questions : la ressource fait-elle apprendre ce qui est visé ? Est-elle facile à utiliser ? Les élèves et l'enseignant·e ont-ils envie de s'en servir, et le peuvent-ils dans leur contexte ? L'acceptabilité (ce que les utilisateurs pensent de la ressource) ne se confond pas avec l'accessibilité (la possibilité d'y accéder). La mise en page réduit la charge extrinsèque, celle qui vient de la présentation ; la charge intrinsèque dépend du contenu lui-même (Maitre, 2020).

- Utile : l'objectif d'apprentissage tient en une phrase et se relie au plan d'études ; chaque carte ou chaque case fait travailler cet objectif, sans tâche décorative ; le temps passé à apprendre dépasse le temps passé à attendre ou à gérer le matériel ; tous les élèves du groupe répondent ; l'erreur est exploitée (vérification, explication, nouvelle tentative) ; un moyen permet de savoir ce que les élèves ont appris ; les contenus sont relus.
- Utilisable : une marche à suivre écrite accompagne le jeu ; un élève peut expliquer la règle après une partie modèle ; les textes se lisent à la distance d'utilisation et la mise en page est la même sur toutes les cartes ; les images sont de style homogène ; la réponse n'est pas visible par celui qui doit la trouver et un corrigé est disponible ; le matériel est solide, facile à distribuer et à ranger ; la taille des groupes et la durée d'une partie sont définies ; des niveaux ou des variantes permettent à chacun de réussir.
- Acceptable : les élèves ont envie de rejouer ; la règle favorise l'entraide et ne met personne en échec devant les autres ; aucun élève n'est désigné comme « différent » par le matériel qu'il reçoit ; le niveau sonore et l'organisation conviennent à la classe ; le temps de préparation reste raisonnable ; un·e collègue pourrait reprendre le jeu sans explications ; les images sont libres de droits ou sourcées, et aucune donnée d'élève n'apparaît.

**Des règles du jeu qui font travailler tous les élèves**

Un jeu remis sans mode d'emploi laisse chaque groupe inventer ses règles. Une marche à suivre d'une demi-page répond à cinq questions : le but et ce qu'on apprend en jouant ; le matériel et le nombre de joueurs ; ce qu'on fait à son tour, étape par étape ; ce qui se passe en cas d'erreur et la façon de vérifier la réponse ; la fin de la partie.

- Groupes de trois ou quatre : au-delà, l'attente entre deux tours est longue.
- Tout le monde répond : chaque élève note sa réponse, celui dont c'est le tour la dit à voix haute.
- Un vérificateur ou une vérificatrice dispose du corrigé et change à chaque tour.
- Assez de cartes pour éviter les répétitions, numérotées et rangées par lots.
- Une partie modèle jouée devant la classe, et un but annoncé avant de jouer : « à la fin, vous saurez… ».

**De la compétition à la coopération**

Dans un jeu de l'oie classique, le premier arrivé gagne : la compétition vient de la règle, pas des élèves. Pour obtenir de la coopération, il faut changer la condition de victoire. Le principe central est l'interdépendance positive : chacun ne réussit que si les autres réussissent aussi ; elle va de pair avec la responsabilité individuelle (Johnson & Johnson, 2009). La fiche pratique du CTREQ (2023) y ajoute trois autres conditions : la promotion des interactions, les habiletés sociales et coopératives, et le retour du groupe sur son fonctionnement.

- Un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance tout seul.
- Un but commun chiffré : tous les pions arrivés en moins de dix tours, ou vingt cartes réussies.
- Des rôles tournants : lecteur ou lectrice, vérificateur ou vérificatrice, secrétaire, gardien ou gardienne du temps.
- L'aide qui rapporte : si l'explication d'un camarade permet de répondre, les deux avancent.
- L'erreur sans recul : le groupe explique, puis l'élève rejoue.
- Des binômes par pion, qui se mettent d'accord avant de répondre, et un bilan de fin de partie.

Si un élève décide de tout à la place des autres, renforcer les rôles. Si l'intérêt retombe sans enjeu, garder un défi : battre le score de la partie précédente, ou jouer équipe contre équipe.

**Différencier sans faire trois versions de chaque fiche**

La différenciation peut porter sur les contenus, les processus, les productions ou les structures (Forget, 2018). Tripler une fiche ne joue que sur les contenus, le levier le plus coûteux à préparer ; les autres se règlent autour d'une fiche unique.

- Difficulté croissante, avec un repère neutre : chacun choisit son point de départ.
- Noyau commun en haut de la fiche, prolongements facultatifs en bas.
- Aides détachées en libre accès : exemple résolu, rappel de la règle, pictogramme de la démarche.
- Quantité plutôt qu'objectif : « au moins quatre exercices sur huit, dont le numéro 5 ».
- Forme de la réponse au choix : écrire, entourer, relier, manipuler puis dessiner, expliquer oralement.
- Organisation : seul, en binôme d'entraide, ou en petit groupe avec l'enseignant·e.
- Trame stable : objectif, exemple, exercices gradués, défi.

Une fiche identique pour tous, avec des aides en libre accès, ne désigne personne comme « différent ». Le libre choix a une limite : certains élèves choisissent toujours trop facile ou trop difficile, et il faut alors orienter leur point de départ.

**Adapter selon l'obstacle, pas selon une étiquette**

Une adaptation part d'un obstacle observé dans la tâche, non d'un diagnostic ni d'une catégorie d'élèves. Trois obstacles fréquents, et des réponses qui gardent la notion intacte :

- Lecture : consigne courte, une action par phrase, consigne lue à voix haute ou illustrée, mots difficiles expliqués.
- Mémoire de travail : une étape à la fois, données visibles pendant toute la tâche, exemple résolu en tête, moins d'éléments à retenir en même temps.
- Planification : étapes numérotées, case « je vérifie » après chaque étape, temps indicatif.

La demande décrit un besoin de la tâche (« des élèves encore fragiles en lecture ») ; l'IA ne reçoit ni nom, ni diagnostic, ni historique d'élève, et l'aide reste en libre accès pour toute la classe.

**« Si je bloque, je… »**

Un encadré court sur les fiches de travail autonome rend visible une stratégie de régulation : relire la consigne et l'exemple, utiliser une aide en libre accès, demander à un·e camarade, puis seulement à l'enseignant·e (Bibliothèque IA 1, MP-D-06). Il soutient la métacognition (F43) s'il est expliqué en classe et repris lors de la mise en commun ; affiché sans être travaillé, il reste un décor.

**Classe multi-âges**

Deux degrés dans la même classe sont la règle en 1P-2P ; la situation se présente aussi à d'autres degrés, dans les petits établissements ou dans les classes spécialisées qui travaillent avec des programmes adaptés. Plutôt que deux ressources séparées, un matériel commun avec une entrée par degré ou par niveau permet de travailler ensemble (Bibliothèque IA 1, MP-D-05) :

- même jeu, deux lots : collection jusqu'à 5 ou jusqu'à 10, images seules ou images et mots ;
- même fiche, deux parcours : tâche de base et prolongement, sans repère de degré visible ;
- même activité, des rôles qui tournent : manipuler, expliquer, vérifier ; le tutorat entre âges reste un choix de l'enseignant·e ;
- un moment commun pour toute la classe : lancement et mise en commun, chacun·e avec son entrée.

L'objectif du plan d'études est indiqué pour chaque degré ou niveau ; la ressource ne désigne aucun élève par son âge ou par son niveau.

**Montrer que les élèves ont appris**

- Trois ou quatre questions identiques avant et après l'activité.
- Une fiche de suivi où l'élève note ce qui est réussi et ce qui reste difficile.
- Trois productions d'élèves commentées : une réussie, une moyenne, une en difficulté.
- Une courte observation ciblée : qui répond, qui attend, qui aide.

**Références de cette section**

Centre de transfert pour la réussite éducative du Québec. (2023, août). *Approche coopérative : les premiers pas vers la rétroaction par les pairs* [Fiche pratique]. https://www.ctreq.qc.ca/wp-content/uploads/2023/10/CTREQ-D232-Preparation-a-la-REPAIR-Guide-14x85-44329-V9.pdf#page=1

Forget, A. (2018). *Penser la différenciation pédagogique* (Carnets des sciences de l'éducation). Université de Genève. https://unige.ch/fapse/editions/index.php/download_file/view/544/492

Maitre, J.-P. (2020). *La théorie de la charge cognitive*. Centre de soutien à l'enseignement, Université de Lausanne. https://enseigner.unil.ch/ressources/wp-content/uploads/20CSE_IN_A_NUTSHELL_01_la_theorie_de_la_charge_cognitive.pdf

Tricot, A., et al. (2003). Utilité, utilisabilité, acceptabilité : interpréter les relations entre trois dimensions de l'évaluation des EIAH. Dans *Environnements informatiques pour l'apprentissage humain* (Strasbourg).

Statut des repères ajoutés le 22.11.2026 (adapter selon l'obstacle, « Si je bloque, je… », classe multi-âges) : propositions de conception de l'auteur, sans référence propre. Statut : existence des références citées vérifiée le 21.11.2026 (CTREQ, 2023 ; Forget, 2018 ; Johnson & Johnson, 2009 ; Maitre, 2020 ; Tricot et al., 2003 ; Bastien & Scapin, 1993, rapport INRIA RT-0156) ; les repères pratiques (astuces, variantes de règles) sont issus de l'enseignement de l'auteur et restent des inférences de conception, non testées à large échelle.
