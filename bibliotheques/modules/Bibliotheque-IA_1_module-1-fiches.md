# Bibliothèque IA 1 — module « Fiches » — v1

Édition du 22 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : fiches, documents et affiches : budget de page, gabarits G, GF et SP, recettes, règles de mise en page.

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

## 2.2 Budget de page (MP-O-11)

- Hauteur utile d'une page A4 portrait : 29,7 − 2 × 2,5 = **24,7 cm**.
- Pour absorber les écarts de rendu entre logiciels, l'IA DOIT planifier au plus **22 cm de contenu par page**, en-tête compris.
- Hauteur estimée d'un exercice : **consigne** (nombre de lignes × hauteur d'une ligne lue) + **exemple** éventuel + **items** (nombre × hauteur indiquée par le gabarit) + **zones d'écriture** (nombre de lignes × hauteur d'une ligne d'écriture) + **0,8 cm** d'espace après l'exercice.
- En-tête obligatoire (Prénom et Date, titre centré avec espace avant et après, objectif ; R7) : environ 3,5 cm en 5P-6P, 4,5 cm en 3P-4P, 5,5 cm en 1P-2P (estimation).
- **Planche de pièces (jeu)** : mention de la planche (environ 0,9 cm) + nombre de rangées × hauteur d'une pièce ; une planche = une page. Valeur testée : 2 × 8 dominos de 8 × 2,5 cm = **20,9 cm prévus** ; **21,1 cm rendus** lors du test du 30.10.2026, **20,7 cm** (de la marge haute au dernier trait) lors du contrôle des recettes v7. Toute autre dimension de pièce est une inférence de conception, à tester. **Depuis le 19.11.2026**, une planche n'est plus limitée au budget de 22 cm : elle occupe toute la surface utile (MP-J-11), la mention passe dans la marge du haut et des repères de coupe bordent la feuille (MP-J-12) ; les gabarits J1, J3, J4, J6 à J8 et J12 à J16 ont été redimensionnés en conséquence le 19.11.2026 (§ 3.8).
- Si le total d'une page dépasse 22 cm, l'IA applique la règle d'arbitrage (§ 0.3) **avant** de rédiger.
- **Page pleine (MP-O-14, révision du 2.11.2026)** : aucune page élève n'est remplie partiellement. Sur le rendu, le dernier objet imprimé de chaque page DOIT atteindre au moins **90 % du budget** : en A4 portrait, 19,8 cm de contenu sous la marge haute (dernier élément imprimé à 22,3 cm au moins du haut de la feuille, soit au plus 4,9 cm de blanc au-dessus de la marge basse) ; en A4 paysage, 12,8 cm. La mesure se fait sur l'image de la page rendue : seuls les éléments visibles comptent (un cadre blanc ou la marge blanche d'une image ne comptent pas). Si une page reste en dessous, l'IA choisit, selon la fiche, l'un de ces trois remèdes :
  1. **aérer** : augmenter les espacements (hauteur des lignes d'écriture et des cellules, espaces avant et après les exercices), sans dépasser 22 cm ni descendre sous les valeurs du degré ;
  2. **compléter** : ajouter quelques lignes d'écriture, ou un ou deux items ou exercices de même nature, au service du même objectif ;
  3. **passer en planche A5** (R15) : la feuille A4 porte deux exemplaires identiques, à découper ; on imprime deux fois moins. Réservé aux contenus courts : règle de jeu, petite fiche, bande, ticket, brevet. Budget d'un exemplaire A5 : 16,9 cm (A5 portrait, côte à côte) ou 12,3 cm (A5 paysage, empilés), à remplir aussi à 90 % au moins.
- Exceptions à la page pleine : la partie enseignant·e ; la dernière planche d'un jeu quand le nombre de pièces est fixé par le jeu (à déclarer dans la fiche technique). Le contrôle se fait sur le rendu (V20, fonction `verifier_remplissage` de l'Annexe I-C).

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

## 2.4 Limites de pages par type de fiche

| Type de fiche | Pages élève au maximum | Si le budget est dépassé |
|---|---|---|
| Entraînement (GF-A) | 2 | réduire les items, puis supprimer un exercice, ou proposer deux fiches |
| Évaluation (GF-B) | 2 | réduire les items ; ne jamais supprimer la tâche complexe |
| Remédiation (GF-C) | 2 | réduire les items |
| Devoir (GF-D) | 1 | réduire à 4-6 items |
| Atelier (GF-E) | 1 par station | une station = une page |
| Jeu (GF-F) | règle et aide : 1 page par groupe ; planches : annexes à découper, 1 page par planche ; trace écrite individuelle : 1 page au maximum | réduire le nombre de pièces, jamais leur taille ; une planche par page |
| Fiche de référence (GF-N, GF-O, GF-P) | 1 ; GF-P : 1 + verso | réduire le nombre d'exemples ou d'étapes |
| Page-son (GF-J) | 1 par graphème | réduire les mots, jamais la taille de l'écriture liée |
| Fiche sur document (GF-Q) | 1, document compris | agrandir le document sur une page séparée |
| Dossier documentaire (GF-R) | 1 de présentation et 1 de croisement ; documents en annexe | réduire à quatre documents |
| Fiche de terrain (GF-S) | 1 (recto) | réduire les rubriques |
| Billet de sortie (GF-T) | 3 billets par page | deux questions au plus |
| Suivi (GF-G, GF-H, GF-I, GF-K, GF-L, GF-U) | 1 | réduire les niveaux ou les rubriques |
| Dossier d'escape game (GF-X) | mise en situation 1, énigmes 1 par planche, feuille d'équipe 1 | réduire le nombre d'énigmes |
| Affiche (GF-V) | 1 A3 | réduire le nombre d'étapes, jamais le corps |

Les annexes facultatives (aide-mémoire, étiquettes à découper) ne comptent pas dans ce total ; elles sont annoncées dans la fiche technique et dans la partie enseignant·e.

## 2.5 Format affiche A3 et lisibilité à distance (v7.2)

Le Livre I est calibré pour la page A4. Les affiches, référentiels collectifs, glossaires, cartes mentales et infographies destinés à être lus depuis les places (TR17 à TR22) suivent la table ci-dessous, propre au format A3 (MP-F-07, GF-V, recette R9).

| Paramètre | Valeur | Statut |
|---|---|---|
| Format | A3 (29,7 × 42 cm), portrait ou paysage | Inférence de conception |
| Marges | 2,5 cm (MP-F-03) | Standard |
| Largeur utile | 24,7 cm en portrait ; 37 cm en paysage | Calculé |
| Budget de hauteur | ≤ 33 cm en portrait ; ≤ 22 cm en paysage | Calculé (37 cm ou 24,7 cm utiles, même rapport que 22 / 24,7) |
| Titre | 72 pt, gras, centré, deux lignes au plus | Inférence de conception ; testé sur rendu |
| Texte principal (lecteurs de 3P à 8P) | 48 pt, ou 36 pt si le tableau compte trois colonnes | Inférence de conception ; testé sur rendu |
| Texte principal (1P-2P) | 60 pt, trois à six mots par ligne, pictogramme à chaque ligne | Inférence de conception, non testé |
| Détail, exemple | 36 pt | Inférence de conception ; testé sur rendu |
| Plancher | 28 pt, pour ce qui se lit à moins d'un mètre (consigne de montage, source) | Inférence de conception |
| Nombre d'étapes ou de rubriques | Six au plus ; une ligne d'affiche = une idée | Verso des cartes TR17, TR18 |
| Couleur | Jamais seule porteuse d'information (X-08) ; affiche lisible en noir et blanc | Standard |

#### Distance de lecture selon la taille (Arial)

La hauteur de la capitale d'Arial vaut 0,716 fois le corps (métrique de la police). La distance-seuil suppose qu'une capitale reste identifiable à 5 minutes d'arc, convention de l'acuité 10/10 (connaissance non vérifiée dans la session). La distance de confort applique un facteur 2 (inférence de conception, à éprouver dans la classe).

| Corps | Capitale | Distance-seuil | Distance de confort |
|---|---|---|---|
| 28 pt | 7,1 mm | 4,9 m | 2,4 m |
| 36 pt | 9,1 mm | 6,3 m | 3,1 m |
| 48 pt | 12,1 mm | 8,3 m | 4,2 m |
| 60 pt | 15,2 mm | 10,4 m | 5,2 m |
| 72 pt | 18,2 mm | 12,5 m | 6,3 m |

*Valeurs calculées avec `distance_lecture_m` (Annexe I-C). Elles ne remplacent pas l'essai : placer l'affiche, puis la lire depuis la place la plus éloignée (V17).*

# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT

## 3.1 Chaîne de décision

> Objectif → indices de réussite → fonction (F, Livre II Partie 1) → processus cognitif (Partie 3) → patron (P, Partie 5) → micro-format (MF, Partie 6) → **gabarit d'exercice (G, § 3.3) ou de jeu (J, § 3.8)** → dimensions (Étape 2)

Les choix pédagogiques se font avec le Livre II. **Le gabarit est le point de passage obligé** entre la pédagogie et la mise en page : c'est lui qui apporte les dimensions, la hauteur estimée et la recette de construction.

## 3.2 Règle de couverture (originalité permise, jamais sans dimensions)

- Chaque exercice de la fiche DOIT correspondre à un gabarit G1 à G31 ; chaque pièce d'un jeu, à un gabarit J1 à J38 (§ 3.8) ; chaque outil permanent, à un gabarit SP (§ 3.9) ; chaque document, à un gabarit GF (§ 6.1).
- L'IA PEUT proposer un format non répertorié si elle le juge mieux adapté. Elle DOIT alors le décrire **avant de l'utiliser** avec la même fiche-type que les gabarits ci-dessous (usage, disposition, zone de réponse, items, hauteur estimée, recette, vigilance), et l'inscrire dans la fiche technique.

## 3.3 Catalogue des gabarits d'exercice (auto-portants, G1 à G31)

Chaque fiche donne tout ce qu'il faut pour construire l'exercice. Les hauteurs sont des **estimations pour 5P-6P (14 pt)** ; pour un autre degré, utiliser les hauteurs de ligne de la table 2.1. Dans les exemples, `______` représente une lacune calibrée (R2) et `[ligne]` une vraie ligne d'écriture (R1).

Règles communes : consigne directe au-dessus des données ; texte aligné à gauche ; numérotation 1, 2, 3 pour les exercices et a), b), c) pour les items ; exercice solidaire (R4).

### G1 — Entourer

- **Usage** : discrimination visuelle (son, nature d'un mot, plus grand / plus petit).
- **Disposition** : propositions alignées à gauche, précédées de a), b), c) ; image éventuelle à gauche de l'item.
- **Zone** : aucune ligne ; espaces blancs entre les propositions.
- **Items** : 3-5 lignes ; 3-4 propositions par ligne au maximum.
- **Hauteur** : consigne + lignes × 0,74 cm + 0,8 cm → environ 4 cm pour 4 lignes.
- **Recette** : texte simple, interligne 1,5 ; R4.
- **Vigilance** : propositions séparées par au moins 1,5 cm pour que le tracé ne déborde pas ; toutes les propositions sont des mots correctement orthographiés (X-13). **Entourer un mot dans une phrase** : une phrase par ligne, les mots séparés par un blanc d'au moins 0,8 cm (trois espaces insécables) et un interligne d'au moins 1,2 cm, pour que l'élève puisse tracer son ovale sans toucher le mot voisin ni la ligne suivante. **Pictogramme de consigne** : quand la consigne vise une chose précise (« Entoure le verbe »), utiliser `pictogramme_consigne(base, 'entoure', 'verbe')`, qui dessine l'ovale autour du mot visé, plutôt que le pictogramme générique « abc ».

### G2 — Relier

- **Usage** : mot ↔ définition, mot ↔ image, calcul ↔ résultat.
- **Disposition** : tableau sans bordures de 3 colonnes : colonne gauche (≈ 5 cm) / colonne vide (≥ 6 cm) / colonne droite (≈ 5 cm) ; point d'ancrage • en fin de colonne gauche et en début de colonne droite.
- **Zone** : la colonne vide centrale ; aucune ligne.
- **Items** : 3-5 paires.
- **Hauteur** : paires × 1,2 cm + consigne → environ 6 cm pour 4 paires.
- **Recette** : R3 sans bordures (lignes ≥ 1,2 cm, insécables).
- **Vigilance** : alignement garanti par le tableau, jamais par des espaces tapés.

### G3 — Compléter (lacune dans une phrase)

- **Usage** : conjugaison, vocabulaire, nombres ; réponse de **1 à 2 mots**.
- **Disposition** : phrase avec lacune au point de réponse ; indication éventuelle entre parenthèses après la lacune.
- **Zone** : lacune de 6-8 cm (nombre de tirets bas selon table 2.1) ; interligne 2,0.
- **Items** : 3-5 phrases.
- **Hauteur** : consigne + exemple + items × 0,99 cm + 0,8 cm → environ 7,5 cm pour 5 items.
- **Recette** : R2.
- **Vigilance** : réponse de 3 mots ou plus → G4 avec lignes en dessous. Éviter l'élision impossible (« Je ___ pris ») : amorce « J'___ » ou autre sujet.

```
3  Complète avec le verbe au passé composé.
   a) Hier, tu ______________________ (chanter) une chanson.
```

### G4 — Transformer, recopier

- **Usage** : changer le temps, la personne, le nombre ; recopier en appliquant une règle. La phrase source est toujours correcte (X-13).
- **Disposition** : phrase source alignée à gauche ; en dessous, 2 lignes d'écriture.
- **Zone** : **2 lignes de 14-16 cm par phrase, à tous les degrés**.
- **Items** : 3-4 phrases (exercice coûteux en place).
- **Hauteur** : par item 0,74 + 2 × 1,0 + 0,3 cm ≈ 3 cm → environ 10 cm pour 3 items.
- **Recette** : R1a.
- **Vigilance** : pas de phrase source fautive « à corriger » (X-13), sauf analyse d'erreurs demandée par l'enseignant·e aux conditions du § 3.7 ; pour travailler le jugement orthographique, voir d'abord les alternatives du § 3.7.

```
4  Écris la phrase au passé composé.
   a) Nous jouons au ballon.
      [ligne]
      [ligne]
```

### G5 — Remettre en ordre

- **Usage** : syntaxe, compréhension de la phrase.
- **Disposition** : mots séparés par des barres obliques, alignés à gauche ; puis lignes d'écriture.
- **Zone** : 2 lignes de 16 cm (la phrase reconstruite est une phrase écrite : MP-E-05).
- **Items** : 1 phrase de 5-7 mots par item ; 2-3 items.
- **Hauteur** : environ 3 cm par item.
- **Recette** : R1a.
- **Vigilance** : ponctuation hors des étiquettes ; vérifier qu'une seule phrase correcte est possible.

### G6 — Cocher (QCM, vrai / faux)

- **Usage** : compréhension, choix, autoévaluation.
- **Disposition** : options en ligne ou en colonne, chacune précédée d'une case.
- **Zone** : aucune ligne.
- **Items** : 3 options, une seule bonne réponse.
- **Hauteur** : environ 1 cm par question.
- **Recette** : cases = cellules vides bordées de 0,6 cm (R3) ou caractère ☐ vérifié sur rendu (R6).
- **Vigilance** : la case est à moins de 1 cm de son texte. Toutes les options sont des formes correctement orthographiées ; un vrai/faux porte sur le sens, un fait ou une règle, jamais sur une forme écrite fautive (X-13).

### G7 — Production courte guidée

- **Usage** : réinvestir une règle dans une ou plusieurs phrases personnelles.
- **Disposition** : consigne (contrainte explicite : verbe, mot, sujet imposé) ; amorce éventuelle ; lignes.
- **Zone** : 2 lignes par phrase demandée ; 5-6 lignes pour un mini-récit.
- **Items** : 1 consigne de production.
- **Hauteur** : consigne + lignes × 1,0 cm + 0,8 cm.
- **Recette** : R1a ; R1b si chaque ligne commence par une amorce (« Le matin, j'ai … »).
- **Vigilance** : une contrainte par phrase de consigne ; contrainte vérifiable.

```
7  Écris deux phrases au passé composé sur ta journée d'hier.
   Le matin, j'ai ________________________________________
   [ligne]
```

### G8 — Repérer dans un texte

- **Usage** : lecture active, grammaire, vocabulaire.
- **Disposition** : consigne en étapes numérotées (une action par étape) ; texte court aligné à gauche.
- **Zone** : aucune ligne ; au moins 1 cm d'espace sous le texte.
- **Items** : 2-4 lignes de texte ou 3-5 phrases courtes.
- **Hauteur** : consigne + lignes de texte × 0,74 cm + 0,8 cm → environ 5 cm.
- **Recette** : texte simple, interligne 1,5 ; R4.
- **Vigilance** : actions différentes (souligne / encadre / entoure) plutôt que couleurs ; aucun pré-marquage.

### G9 — Tableau à compléter

- **Usage** : conjugaison, synthèse, classement.
- **Disposition** : en-tête en gras ; une ligne d'exemple remplie, réponses en police d'élèves (MP-T-10) ; cellules vides aux endroits de réponse.
- **Zone** : cellules ≥ 5 cm × ≥ 1 cm ; largeur totale ≤ 16 cm.
- **Items** : 3-5 lignes + 1 ligne d'exemple.
- **Hauteur** : (1 + lignes) × 1,1 cm + consigne + 0,8 cm → environ 7 cm pour 4 lignes.
- **Recette** : R3.
- **Vigilance** : avec 5 colonnes sur 16 cm, la règle des 5 cm ne peut pas être tenue : réduire les colonnes de rappel (pronom, item) et garder ≥ 4 cm pour les colonnes de réponse, puis **déclarer l'écart**.

### G10 — Image et écriture

- **Usage** : premiers écrits, vocabulaire, description.
- **Disposition** : image au-dessus de la consigne (8 × 10 cm au maximum), lisible en noir et blanc ; lignes en dessous.
- **Zone** : 2 lignes en 3P-4P, 3-5 lignes à partir de 5P.
- **Items** : 1 image, 1 consigne.
- **Hauteur** : jusqu'à 10 cm d'image + lignes → environ 14 cm (exercice long).
- **Recette** : image dans une cellule de tableau insécable avec la consigne (R4) ; R1a.
- **Vigilance** : pas d'image décorative ; pas de photographie de personne réelle ; image générée sans texte incrusté (MP-I-05).

### G11 — Colorier selon une consigne

- **Usage** : formes, catégories, nombres (cycle 1 surtout).
- **Disposition** : dessins simples de 3-4 cm en grille régulière ; consigne qui **nomme les couleurs en toutes lettres**.
- **Zone** : les dessins.
- **Items** : 8 éléments au maximum ; 2-3 couleurs.
- **Hauteur** : environ 9 cm pour deux rangées.
- **Recette** : grille = tableau sans bordures, cellules égales.
- **Vigilance** : éviter rouge/vert et rouge/bleu ; prévoir une version « entoure / barre » pour la photocopie noir-blanc.

### G12 — Classer en colonnes

- **Usage** : tri selon un critère (nom/verbe, vivant/non-vivant).
- **Disposition** : banque de mots **au-dessus** du tableau ; une colonne par catégorie ; un exemple placé par colonne, en police d'élèves (MP-T-10).
- **Zone** : 2 colonnes de 6-8 cm ou 3 colonnes de 5 cm ; une ligne de 1 cm par entrée.
- **Items** : 2-3 catégories × 3-5 mots.
- **Hauteur** : banque 1,5 cm + (1 + entrées) × 1,0 cm + 0,8 cm → environ 7 cm.
- **Recette** : R3.
- **Vigilance** : banque de mots dans un ordre mélangé.

### G13 — Calcul posé

- **Usage** : opérations en colonnes.
- **Disposition** : tableau à cases (un chiffre par case), en-têtes de rang (C, D, U) en début d'apprentissage ; signe à gauche ; trait de résultat.
- **Zone** : cases ≥ 1 cm × 1 cm ; une ligne de cases pour les retenues.
- **Items** : 2-4 calculs côte à côte.
- **Hauteur** : environ 6 cm.
- **Recette** : R3 avec cellules carrées de hauteur exacte.
- **Vigilance** : jamais de calcul « posé » écrit en ligne.

### G14 — Chronologie

- **Usage** : succession dans le temps (récit, journée, cycle).
- **Disposition** : 4-5 vignettes encadrées de largeur égale, lecture de gauche à droite ; case de numéro sous chaque vignette.
- **Zone** : la case de numéro (≥ 1 cm).
- **Items** : 4-5 étapes.
- **Hauteur** : environ 7 cm.
- **Recette** : tableau de 4-5 colonnes égales (≤ 16 cm au total).
- **Vigilance** : vignettes lisibles en noir et blanc.

### G15 — Copier puis illustrer

- **Usage** : passage du non-lecteur au lecteur ; le dessin prouve la compréhension sans production écrite supplémentaire (TR02, BDRP-A1).
- **Structure** : carte à trois zones superposées : modèle (écriture liée ou script), ligne de copie, cadre de dessin. Repère de lot au verso, sans étiquette évaluative (X-05).
- **Dimensions** : carte de 8 × 10,1 cm ; zones de 2,2, 1,6 et 6,3 cm ; quatre cartes par planche (16 × 20,2 cm).
- **Recette** : R14 (`planche_zones`) ; R10 pour le modèle ; R12 pour le verso.
- **Contrôles** : V12, V15 si cursive.
- **Interdits** : modèle cursif dessiné ou généré (MP-CC-11) ; mot non décodable pour la classe.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G16 — Planche de recherche visuelle

- **Usage** : attention sélective, vocabulaire, repérage (TR01, TR02, BDRP-A2). La cible se donne par une image ou par un mot.
- **Structure** : consigne ; planche dense de formes ; nombre de cibles connu de l'enseignant·e.
- **Dimensions** : planche de 16 × 13 cm ; 7 cibles parmi 63 formes de 10 à 12 mm (valeurs de l'essai).
- **Recette** : R11 (formes simples ou icônes de la banque IC), jamais une image dense générée ; placement par programme avec une **distance minimale de 3 mm** entre deux formes (aucun contact, aucun chevauchement), vérifiée par calcul avant le rendu.
- **Contrôles** : compte des cibles par programme ; distance entre formes par programme ; V12.
- **Interdits** : reprendre un album ou des dessins tiers ; texte dans l'image (MP-I-05).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G17 — Série d'automatisation chronométrée

- **Usage** : automatiser des faits déjà compris (TR02, BDRP-A3, MF63).
- **Structure** : deux séries de 10 items en deux blocs ; sous chaque série, cases « mon temps » et « mon record ».
- **Dimensions** : lignes de 0,9 cm ; quatre colonnes de 4 cm ; case temps de 1 cm.
- **Recette** : R14 (`grille`).
- **Contrôles** : V1 à V10.
- **Interdits** : introduire une notion nouvelle ; afficher les temps ou les comparer entre élèves.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G18 — Grille croisée de nombres avec code

- **Usage** : double autovalidation par les cases croisées et par un message (TR03, BDRP-A6, MF64).
- **Structure** : calculs ; grille de 3 × 3 chiffres ; table résultat → lettre, ; six cases pour le message. Les consignes disent où écrire : « Cherche chaque résultat dans le tableau et lis sa lettre. », puis « Écris les lettres dans les six cases, dans l'ordre … » (V21 : aucune consigne « Écris » sans zone désignée).
- **Dimensions** : cases de 1,2 cm ; table de 16 cm.
- **Recette** : R14, avec contrôle par programme de la grille et du message.
- **Contrôles** : V11 (lignes et colonnes concordent ; chaque résultat donne une seule lettre) ; V21 : la consigne indique le sens de lecture de la grille (« un chiffre par case : chaque ligne de gauche à droite, chaque colonne de haut en bas »).
- **Interdits** : message trop prévisible ; grille non vérifiée par programme.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G19 — Tracé de chemin orienté

- **Usage** : motricité fine et orientation au cycle 1 (TR09, BDRP-A7, P23).
- **Structure** : échelle en quatre niveaux, de gauche à droite : 1 droit, 2 courbe, 3 zigzag arrondi, 4 labyrinthe. Point noir au départ, barre à l'arrivée.
- **Dimensions** : couloirs de 20, 16 et 11 mm ; labyrinthe de 6 × 10 cases de 13 mm. Dessin de 16 × 15 cm.
- **Recette** : R11 (`couloir`, `arrondir`, `labyrinthe`), inséré dans le .docx à l'échelle 1. Source vectorielle livrée en SVG et en PDF.
- **Contrôles** : V16 (largeur, séparation, chemin unique).
- **Interdits** : angle vif dans un couloir (le bord intérieur se croise) ; consigne écrite seule pour des non-lecteurs.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; largeurs = inférence de conception, à éprouver avec des élèves de 1P.

### G20 — Dictée réfléchie

- **Usage** : orthographe raisonnée (TR70, BDRP-I3, P24, MF75). Trois formes : **G20-a** à trous, **G20-b** à choix, **G20-c** négociée.
- **Structure** : le texte dicté figure dans la partie enseignant·e seulement. G20-a : phrases à lacunes, puis une justification. G20-b : tableau de paires de formes existantes à entourer, puis une justification. G20-c : phrase individuelle, phrase du groupe, tableau « le mot / notre raison ».
- **Dimensions** : lacunes de 6 cm (R2) ; cellules ≥ 1 cm ; lignes de 1 cm (R1a).
- **Recette** : R1a, R2, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : texte à corriger, forme fautive imprimée (X-13) ; G20-b propose seulement des formes existantes, sans phrase affichant la mauvaise forme (§ 3.7) ; texte à dicter absent de la partie enseignant·e (V21) ; page à moitié vide : ajouter des phrases ou des paires plutôt qu'aérer à l'excès (MP-O-14).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### G21 — Imagier et scène à légender (3.11.2026)

- **Usage** : nommer les éléments d'une scène ou d'une planche d'images : vocabulaire d'un thème, en langue 2 d'abord (TR16, BDRP-C8, MF01, MF17, MF39, F29). Trois formes : **G21-a** étiquettes-mots à découper et à coller dans des cases (élèves qui ne lisent pas encore la langue) ; **G21-b** mot à écrire sur une ligne numérotée ; **G21-c** écoute : l'enseignant·e dit un mot, l'élève écrit le numéro (variante de MF39, sans étiquettes).
- **Structure** : en-tête R7 (titre dans la langue cible, objectif en « je ») ; consigne ; **scène sans aucun texte** avec des pastilles blanches numérotées de 1 à n, posées par le document et non par le dessin ; lignes ou cases numérotées, en deux colonnes ; G21-a : bande d'étiquettes en bas, ordre mélangé, bords en pointillés. Partie enseignant·e : corrigé numéroté, déroulement, réemploi (J2, J7, SP11).
- **Image** : trois sources admises, dans cet ordre : (1) scène dessinée en R11 à partir de formes simples (l'essai) ; (2) image fournie par l'enseignant·e (photo, dessin, illustration sous licence) ; (3) image générée, **sans aucun texte ni enseigne lisible** (MP-I-05), relue élément par élément. Chaque élément est à **dénomination univoque** (un seul mot attendu, sans synonyme courant), bien séparé des autres ; 6 à 12 éléments. Les numéros sont posés par `scene_numerotee`, jamais générés.
- **Mots** : en langue étrangère, **l'article fait partie du mot** (der Baum, a dog) et figure sur l'étiquette et dans le corrigé ; aucune forme fautive ; orthographe et genre vérifiés par l'enseignant·e dans le moyen d'enseignement (l'IA le signale : statut non vérifié). La consigne est dans la langue cible dès 5P, doublée en français au besoin (cadrage).
- **Dimensions** : scène de 16 × 9,5 cm (G21-b) ou 14,5 × 8,6 cm (G21-a) ; pastilles de 4 mm de rayon, numéro en 11 pt ; 8 lignes de 1,1 cm en deux colonnes (G21-b) ou 8 cases de 1,4 cm (G21-a) ; étiquettes de 4 × 1,2 cm, quatre par rangée. Hauteur : 3 + 9,5 + 0,2 + 4,4 + 1,2 ≈ 18,5 cm (G21-b) ; G21-a ≈ 21 cm.
- **Recette** : R7 ; R11 (`Dessin`) ou image fournie ; `scene_numerotee` (pastilles) ; `lignes_numerotees` (lignes ou cases) ; `bande_etiquettes` (R8, MP-J-03, MP-J-05) ; Annexe I-C.
- **Contrôles** : V1 à V10, V12 (étiquettes) ; V21 : `verifier_imagier` (autant de repères que de mots, mots tous différents, article présent) ; pastilles lisibles et non superposées (contrôle par programme : distance ≥ 2 rayons) ; sur le rendu, chaque numéro désigne un seul élément.
- **Interdits** : texte ou enseigne lisible dans l'image ; numéro dessiné dans l'image générée ; élément ambigu (vélo ou bicyclette, banc ou bank) sans choix explicité dans le cadrage ; étiquettes fautives (X-13) ; dessin tiers reconnaissable ; personnage identifiable.
- **Statut** : testé sur rendu (3.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide), G21-a et G21-b, scène R11 ; image générée non testée dans le document (le visuel de la carte R16 en est un exemple, hors fiche) ; dimensions = inférence de conception.

### G22 — Lignes d'écriture, lignage romand (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : page ou bande de lignes pour l'écriture liée, au lignage en usage en Suisse romande : quatre lignes et trois couloirs égaux, **sans quadrillage** (le lignage Seyès français n'est pas utilisé).
- **Structure** : de haut en bas, ligne de plafond en pointillés, ligne du corps des lettres en trait fin, **ligne de base en trait épais**, ligne de plancher en pointillés. Le corps des lettres s'écrit entre la ligne du corps et la ligne de base ; les lettres hautes montent jusqu'au plafond, les lettres basses descendent jusqu'au plancher.
- **Repère en couleur** (facultatif, cycle 1) : couloirs « ciel, herbe, terre » ; la position suffit à les distinguer, la couleur s'ajoute (MP-C-05).
- **Dimensions** : module (hauteur d'un couloir) de 7 mm pour l'entrée dans l'écriture (mesuré sur le document « Lignes, document vertical » de la BDRP : 6,9 mm) ; 4 mm, puis 2,5 mm ou 2 mm ensuite (**indication de l'auteur, non vérifiée à une source officielle**) ; 8, 14 ou 20 lignes d'écriture par page A4.
- **Recette** : R11 : `lignage_romand(base, module_mm, couleurs, entete)` écrit la page en PDF ; inséré dans un .docx, le PDF garde son échelle. **Bande dans une fiche** : `bande_lignage` (R1c) place quelques lignes romandes dans une zone d'écriture, à la place des lignes simples. **Livret A5** : `livret_ecriture(base, module_mm, couleurs, feuilles, titre)` produit un cahier à plier (deux pages A5 par feuille A4 paysage, couverture avec un cartouche vide pour le prénom, sans ligne à remplir, repères du pli) : impression recto-verso avec retournement sur le bord court, pliage, agrafage dans le pli.
- **Modèle d'écriture** : les lettres ne sont jamais dessinées par l'IA ; l'enseignant·e écrit le modèle à la main ou avec la police d'écriture liée de son canton (R10).
- **Contrôles** : V15 si un modèle en écriture liée est ajouté ; impression à 100 %, sans « ajuster à la page ».
- **Interdits** : quadrillage Seyès ; lettre tracée ou générée par l'IA ; module inférieur à 2 mm.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; le module de 7 mm reproduit le document de la BDRP, les autres modules restent à confirmer avec les cahiers de l'établissement.

### G23 — Syllabes et sons (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : segmenter un mot en syllabes orales, puis en sons (conscience phonologique, 1P à 4P).
- **Structure** : bandeau de titre et de consigne, ligne du prénom, grille de 8 ou 12 cases. Par case : un cadre en pointillés pour l'image (collée par l'élève, ou insérée par l'enseignant·e), le mot écrit, une ligne « syllabes » où l'élève dessine un carré par syllabe, une ligne « sons » où il dessine un jeton par son.
- **Dimensions** : case de 4,65 × 11,7 cm (8 mots) ou de 4,65 × 7,8 cm (12 mots) ; lignes de 1,1 cm.
- **Recette** : R11 : `fiche_syllabes_sons(base, mots, colonnes, titre, taille_pt, images)` ; `images` : chemins des images, dans l'ordre des mots (banque d'icônes de la boîte à outils, ou images de l'enseignant·e).
- **Corrigé** : le nombre de syllabes et de sons de chaque mot, donné à l'enseignant·e à part ; les syllabes sont **orales** (« poule » : une syllabe orale à Lausanne, deux dans le Midi : choisir la norme de la classe et l'annoncer).
- **Contrôles** : V1 à V10 ; chaque image représente le mot sans ambiguïté.
- **Interdits** : mot dont le découpage en sons prête à discussion sans que le corrigé le signale ; image générée non relue.
- **Statut** : deux formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; cadres d'images vides dans l'essai.

### G24 — Maisons des nombres (21.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : décompositions additives d'un nombre (cycle 1) : le nombre est dans le toit, chaque étage reçoit deux nombres dont la somme est celle du toit.
- **Structure** : bandeau, ligne du prénom, 2 à 6 maisons par page ; étages de 1,1 cm au moins, deux cases par étage.
- **Recette** : R11 : `maison_des_nombres(base, nombres, titre)` ; jusqu'à 6, autant d'étages que de décompositions (n + 1) ; au-delà, la moitié (les décompositions symétriques ne sont pas répétées).
- **Corrigé** : toutes les décompositions, données à l'enseignant·e ; l'ordre des étages est libre.
- **Interdits** : étage prérempli avec une erreur ; nombre du toit supérieur à 20 sans raison didactique.
- **Statut** : deux pages (3 à 6, 7 à 10) produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### G25 — Reproduction sur quadrillage (21.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : repérage dans le plan, tracé à la règle : reproduire une figure du modèle sur un quadrillage vide.
- **Structure** : en haut, le modèle sur quadrillage ; en bas, le même quadrillage vide, ou seulement ses nœuds (`points=True`, plus difficile) ; carreaux de 1,4 cm.
- **Recette** : R11 : `reproduction_quadrillage(base, figure, cases, points, titre)` ; figures fournies dans `FIGURES` (maison, bateau, sapin, fusée) ; une figure personnelle se donne par ses lignes brisées, points aux nœuds.
- **Contrôles** : la fonction refuse une figure qui sort du quadrillage ; tous les sommets sont sur des nœuds.
- **Interdits** : figure dont un sommet tombe hors d'un nœud ; modèle et quadrillage de tailles différentes.
- **Statut** : quatre figures produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### Supports de classe et mises en page de projets (G26 à G31, 21.11.2026)

- **Principe** : six gabarits qui ne sont pas des exercices : des supports d'affichage (G26, G27) et des mises en page pour les projets des élèves (G28 à G31). Ils se remplissent à la main ; l'IA peut aussi en préparer le contenu, que l'enseignant·e relit.
- **G26 — Calendrier mensuel** : `calendrier_mensuel(base, annee, mois, titre)` : un mois par page, semaine du lundi au dimanche, jours calculés par programme, samedi et dimanche grisés ; cases de 4,7 cm ou plus pour écrire la date, le temps qu'il fait, un événement.
- **G27 — Étiquettes de l'horaire** : `etiquettes_horaire(base, etiquettes, colonnes, rangees, taille_pt, mention)` : 16 étiquettes de 9,3 × 3,3 cm, un cadre pour le pictogramme et le nom de l'activité ; repères de coupe (MP-J-12). Les pictogrammes viennent de la banque d'icônes ou sont dessinés par les élèves.
- **G28 — Livret à onglets** : `livret_a_onglets(base, onglets, titre, pas_mm)` : une feuille par onglet (3 à 8) ; chaque feuille est coupée 1,4 cm plus court que la suivante, les onglets restent visibles en bas, agrafage en haut.
- **G29 — Page de journal de classe** : `page_journal(base, titre, articles)` : bandeau du titre, numéro et date, 2 à 4 articles sur deux colonnes (titre, cadre d'illustration, lignes de 9 mm, signature).
- **G30 — Planche de bande dessinée** : `planche_bd(base, rangees, titre)` : cases vides numérotées, par bandes (par exemple 2, 3 et 2 cases), bandeau du titre et de l'auteur·e.
- **G31 — Plan d'exposé** : `plan_expose(base, parties, titre)` : sujet et question de départ, 2 à 4 parties (idée principale, mots-clés, image à montrer), conclusion, sources.
- **Vigilance** : pas de photo d'élève ni de nom complet dans un journal diffusé hors de la classe ; les sources d'un exposé sont notées par l'élève.
- **Statut** : un à quatre exemples par gabarit produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; découpe et agrafage du livret à onglets non essayés.

### Variantes de G11 et de G12

- **G11-b — Colorier selon un critère** (BDRP-A4) : neuf dessins au plus, une couleur, critère explicite lié à l'objectif. Grille de 3 × 3 cellules de 5,33 × 4,2 cm (R14). Le critère ne porte jamais sur l'esthétique. Statut : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).
- **G11-c — Coloriage codé** (BDRP-A8, MF64) : chaque case porte un calcul, le résultat renvoie à un crayon numéroté **et** à un motif nommé en mots (MP-C-05). Grille de 7 × 6 cases de 2,28 × 1,4 cm. Un code fondé sur la seule couleur est interdit (X-08). La légende nomme chaque motif par un mot courant que l'élève connaît (« rayures », « points », « quadrillage »), jamais par un terme technique (« zone rayée ») ; chaque motif de la légende est aussi dessiné (R11) à côté de son nom. Statut : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).
- **G12-b — Plateau de tri à étiquettes mobiles** (BDRP-A5, TR38) : plateau de deux colonnes de 8 cm, chacune à **cases d'accueil de 8 × 3,5 cm** (la cellule du plateau ; une par étiquette attendue, plus une case vide par colonne, annoncée dans la consigne) ; puis planche d'**étiquettes de 6 × 2,5 cm** (image ou mot), imprimée en double pour l'autocorrection, bords en pointillés (MP-J-05). La case mesure au moins l'étiquette + 0,5 cm par côté (MP-J-10, `verifier_case_piece` : jeu de 1 cm et 0,5 cm) ; les deux dimensions de l'étiquette et de la case figurent dans la fiche technique. La planche d'étiquettes, dernière planche à nombre de pièces fixé, est déclarée en exception de V20 (73 % sur l'essai). Conditionnement : plastification, velcro. Images à dénomination univoque. Statut : testé sur rendu (2.11.2026) ; révision du 2.11.2026, suite : la planche d'étiquettes de 5,33 × 4,2 cm reprise de G11-b dépassait les cases du plateau ; dimensions = inférence de conception.

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

## 3.6 Différenciation et mise en page (MP-D)

| Code | Règle | Niveau |
|---|---|---|
| MP-D-01 | Aucune étiquette de niveau évaluative sur la fiche élève. Un repère neutre est admis : symbole discret en en-tête (♣ ♦ ♠), lettre de version, items facultatifs marqués ★. **Étoiles de difficulté, sur demande** : si l'enseignant·e le demande, les exercices d'une fiche ou les cartes d'un jeu PEUVENT porter une à trois étoiles, de la tâche la plus simple à la plus difficile ; les étoiles décrivent la tâche, jamais l'élève ni un groupe d'élèves ; une ligne les explique à l'élève (« Choisis ton point de départ ») ; elles sont dessinées ou vérifiées sur le rendu (R6). Sans demande, le repère reste neutre. | DOIT |
| MP-D-02 | Deux dispositifs possibles : **parcours sur la même fiche** (items a-c, a-d, a-e ; aide-mémoire pour un parcours) ou **versions parallèles** (mêmes exercices, mêmes phrases et mêmes lettres d'items ; seuls l'étayage et l'étendue changent), ce qui permet une correction commune et un changement de version en cours de route. Autour d'une **fiche unique**, sans tripler la fiche (leviers : contenus, processus, productions, structures ; Forget, 2018) : difficulté croissante, chacun choisissant son point de départ avec un repère neutre ou, sur demande, des étoiles de difficulté (MP-D-01) ; noyau commun en haut de la fiche et prolongements facultatifs en bas ; aides détachées en libre accès, réutilisables d'une fiche à l'autre (J15) ; quantité plutôt qu'objectif (« au moins quatre exercices sur huit, dont le numéro 5 ») ; forme de la réponse au choix (écrire, entourer, relier, manipuler puis dessiner, expliquer oralement) ; organisation (seul, binôme d'entraide, petit groupe avec l'enseignant·e) ; trame stable (objectif, exemple, exercices gradués, défi). Si un élève choisit toujours trop facile ou trop difficile, l'enseignant·e oriente son point de départ. | DEVRAIT |
| MP-D-03 | Chaque version ou parcours respecte son propre budget de page (Étape 2). | DOIT |
| MP-D-04 | Les modalités d'attribution (diagnostic court, choix accompagné) et la consigne « une version décrit un besoin du moment, pas un niveau d'élève » figurent dans la partie enseignant·e. | DEVRAIT |
| MP-D-05 | **Classe multi-âges** (deux degrés, ou deux niveaux de programme, dans la même classe : très fréquente en 1P-2P, possible à tous les degrés, notamment dans les petits établissements et les classes spécialisées). Un seul matériel commun, avec une entrée par degré ou par niveau : par exemple une collection jusqu'à 5 ou jusqu'à 10, des images ou des mots, moins ou plus de cartes, une tâche de base et un prolongement. Aucun repère de degré ou de niveau n'est visible pour les élèves (MP-D-01) ; les entrées se distinguent par le contenu ou par un repère neutre. Dès qu'un des degrés ne lit pas encore, les consignes sont prévues à l'oral ou en pictogrammes. La partie enseignant·e indique quelle entrée convient à quel degré ou niveau, l'objectif du plan d'études de chacun (§ 1.2) et un moment commun (lancement, mise en commun). L'IA ne demande et n'utilise aucune information sur des élèves : elle part des degrés ou des niveaux annoncés. | DOIT |
| MP-D-06 | **Encadré « Si je bloque »**, sur demande ou pour un travail autonome (atelier, plan de travail, devoir) : deux ou trois stratégies dans l'ordre (relire la consigne et l'exemple, utiliser une aide en libre accès, demander à un·e camarade), puis le moment où demander à l'enseignant·e ; formulé en « je », avec pictogrammes si les élèves lisent peu ; jamais la réponse. | PEUT |

## 3.9 Catalogue des outils d'étayage permanents (SP1 à SP13, v7.2)

Les outils SP restent sous les yeux de l'élève ou de la classe. SP1 à SP3 sont des sous-mains ; SP4 et SP6 à SP13 des affiches au format GF-V (§ 2.5) ; SP5, des étiquettes. Les codes SP1 à SP8 viennent du balayage BDRP ; SP9 à SP13 les prolongent. Tous sont testés sur rendu (2.11.2026) ; leurs dimensions sont des inférences de conception.

**Zones laissées à la classe** (révision du 2.11.2026, suite) : plusieurs outils SP réservent une colonne ou une case que la classe remplit elle-même (photo, dessin, exemple trouvé en commun). Une telle zone porte toujours un **intitulé en tête de colonne** qui dit ce qu'on y mettra (« Notre photo ou notre dessin », « Notre exemple », « Croquis ») ; une colonne vide sans intitulé se lit comme un oubli de l'IA. L'intitulé compte comme contenu pour V20 ; la zone elle-même reste vide à la livraison.

### SP1 — Bande numérique à triple codage

- **Usage** : même quantité en chiffre, constellation de dé et doigts (TR11, BDRP-E1, MF59).
- **Structure** : trois rangées, 0 à 10 : chiffre ; dé (de 7 à 10 : 5 + n) ; main.
- **Dimensions** : A4 paysage ; onze colonnes de 2,24 cm ; rangées de 1,5, 2,3 et 2,3 cm.
- **Recette** : R9, R14, icônes IC-DE et IC-MAIN.
- **Contrôles** : V1 à V10, V12 ; trait de coupe en tirets entre les deux bandes de la page (MP-J-05).
- **Interdits** : polices ou pictogrammes tiers sans licence. La suite de 11 à 20 n'est pas testée.

### SP2 — Réglette avec repère de latéralité

- **Usage** : alphabet lié, chiffres, repère gauche et droite (TR11, BDRP-E2, MF66, MF67).
- **Structure** : main et mot « gauche » à gauche, main et mot « droite » à droite ; deux rangées de lettres ; une rangée de chiffres.
- **Dimensions** : A4 paysage ; 15 colonnes ; rangées de 1,9 cm ; lettres en 26 pt.
- **Recette** : R10, R14, icônes IC-LAT.
- **Contrôles** : V15, V12 ; trait de coupe en tirets entre les deux réglettes de la page (MP-J-05).
- **Interdits** : main seule, sans le mot ; repère placé du mauvais côté.

### SP3 — Sous-main personnel

- **Usage** : prénom en deux écritures, alphabet lié, suite des nombres jusqu'à 100 (TR11, BDRP-E3).
- **Structure** : bandeau prénom ; alphabet sur deux rangées ; tableau de 5 × 20 nombres.
- **Dimensions** : A3 paysage ; bandeau de 4 cm, rangées de 3 cm et de 1,6 cm.
- **Recette** : R9, R10, R14.
- **Contrôles** : V15, V12.
- **Interdits** : prénom réel dans une demande à l'IA ; prénom pré-imprimé sur le rendu livré : sous l'intitulé « Mon prénom », les deux cellules (script, écriture liée) sont livrées vides et remplies localement par l'enseignant·e, en GE Typo Libre pour la seconde (MP-P-10, R10).

### SP4 — Affiche-procédure en « je »

- **Usage** : procédure en étapes à la première personne (TR18, BDRP-E4).
- **Structure** : titre ; six étapes au plus : numéro, image, texte. La colonne d'images porte l'intitulé « Image » (colonne de 3,5 cm : un intitulé plus long se coupe) et reste vide : la classe la remplit (photo de l'élève en train de faire l'étape, ou dessin) ; aucune image générée. Intitulés en 28 pt gras, ligne de 1,6 cm.
- **Dimensions** : GF-V ; colonnes de 2,2, 3,5 et 19 cm ; étapes de 4,3 cm ; existe en format cahier (A5) au besoin.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : étape à deux actions ; image générée avec du texte (MP-I-05).

### SP5 — Étiquettes de coin ou de journée

- **Usage** : mot et pictogramme pour organiser la journée ou un coin (TR65, BDRP-E5).
- **Structure** : pictogramme, puis mot en gras.
- **Dimensions** : 8 × 4,8 cm ; six par planche.
- **Recette** : R14, icônes IC.
- **Contrôles** : V12 ; même pictogramme d'un support à l'autre.
- **Interdits** : pictogramme sans mot pour une information nécessaire.

### SP6 — Affiche-métaphore structurante

- **Usage** : donner une image stable à une notion : par exemple les wagons de la phrase (TR17, TR19, BDRP-E6).
- **Structure** (révision du 2.11.2026, suite) : quatre colonnes : **wagon** (forme dessinée R11, nom écrit dans le wagon) ; **nom complet** du groupe ou de la fonction ; **« Comment je le reconnais »** : le test opératoire en « je », tel qu'il est enseigné (déplacement, effacement, remplacement, encadrement, addition) ; **exemple** où le groupe est en gras. Une rangée par groupe, quatre rangées au plus ; une seule manipulation-clé par rangée, la plus discriminante (sujet : encadrement par « C'est … qui » ; complément de phrase : déplacement et effacement ; complément de verbe : ni effacement ni déplacement, remplacement par un pronom ; verbe conjugué : encadrement par « ne … pas »). Trois formats : A3, sous-main, gabarit vide (variante de MF02). Les noms sont les termes complets de la grammaire enseignée, dans la forme du moyen d'enseignement en usage (« complément de verbe », « complément de phrase », jamais « complément » seul) ; l'enseignant·e indique sa terminologie dans le cadrage, l'IA ne la devine pas.
- **Dimensions** : A3 paysage ; quatre colonnes de 4,4, 9, 13,6 et 10 cm ; ligne d'intitulés de 1,2 cm, rangées de 4,9 cm ; nom et exemple en 36 pt, test en 28 pt (quatre lignes au plus par cellule) ; wagon dessiné de 4,3 cm (R11), nom écrit dedans en petit ; titre en 56 pt. Valeurs de l'essai du 2.11.2026 (suite), rendu à 106 % du budget A3 ; inférence de conception.
- **Recette** : R9, R11 (wagons), R14.
- **Contrôles** : V17 ; V21 : chaque exemple réussit le test de sa rangée et échoue au test des autres rangées (vérifié à la main avant la mise en page) ; termes complets.
- **Interdits** : couleur des wagons sans repère écrit ; repérage fondé sur une question (« Qui ? », « Quoi ? », « Où ? ») : la question PEUT figurer en appui dans la colonne « Comment je le reconnais », jamais seule et jamais comme critère, parce qu'elle n'est pas le test enseigné et qu'elle confond complément de verbe et complément de phrase (« Où ? »).
- **Choix de conception** : la version « questions » de l'essai du 2.11.2026 a été remplacée par la version « tests opératoires », conforme aux groupes définis par manipulation dans le PER (L1 16 : « reconnaissance des groupes de la phrase simple par manipulation », complément de phrase « facultatif et permutable ») et aux cinq tests de la référence grammaticale romande (CIIP, 2013). Décision prise par l'IA faute d'arbitrage ; à confirmer par l'enseignant·e.

### SP7 — Affiche-acronyme de stratégie

- **Usage** : initiales qui rappellent une suite d'actions (TR17, BDRP-E7, MF71).
- **Structure** : initiale en 72 pt, action en 48 pt ; quatre lignes.
- **Dimensions** : GF-V ; colonnes de 5 et 19,7 cm ; lignes de 6,8 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : acronyme imposé sans apprentissage des actions.

### SP8 — Affiche mnémotechnique

- **Usage** : repère pour distinguer des formes proches, par exemple b, d, p, q (TR19, BDRP-E8, MF70).
- **Structure** : forme, puis phrase-repère ou geste décrit ; quatre lignes.
- **Dimensions** : GF-V ; lignes de 6,2 cm ; formes-repères (b, d, p, q) en 100 pt ; colonne de texte assez large pour qu'aucun mot ne soit coupé (sinon : réduire à 32 pt dans les limites de § 2.5, jamais couper un mot).
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : geste dessiné par l'IA sans contrôle ; méthode gestuelle tierce sans source.

### SP9 — Affiche de stratégies

- **Usage** : rendre visibles les étapes d'une tâche, à construire avec les élèves (TR17).
- **Structure** : titre ; six étapes : numéro, pictogramme, texte.
- **Dimensions** : GF-V ; étapes de 4,3 cm ; 32,3 cm de haut sur rendu.
- **Recette** : R9, R14, icônes IC-CON.
- **Contrôles** : V17 ; un pictogramme qui représente une opération porte son signe (+, −, ×, :) ; sinon, pictogramme d'action sans signe.
- **Interdits** : plus de six étapes ; pictogramme d'opération sans signe.

### SP10 — Référentiel collectif

- **Usage** : panneau durable, complété au fil des apprentissages (TR19).
- **Structure** : six rubriques : repère, exemple, case libre à compléter ; les trois colonnes portent un intitulé (« Repère », « Exemple », « Notre exemple », 28 pt gras, ligne de 1,6 cm) ; la troisième reste vide pour la classe.
- **Dimensions** : GF-V ; colonnes de 5, 11 et 8,7 cm ; rubriques de 4,2 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : exemple fautif (MP-CC-11) ; exemple qui ne contient pas le graphème de sa rubrique (V21, `verifier_graphemes`).

### SP11 — Glossaire de classe

- **Usage** : mot, définition courte, croquis (TR20).
- **Structure** : quatre entrées par affiche ; intitulés de colonnes « Mot », « Ce que ça veut dire », « Croquis » (28 pt gras, ligne de 1,6 cm) ; la colonne « Croquis » reste vide, dessinée par la classe.
- **Dimensions** : GF-V ; colonnes de 6, 12 et 6,7 cm ; entrées de 6,2 cm ; texte en 36 pt.
- **Recette** : R9, R14.
- **Contrôles** : V17 ; exactitude disciplinaire de chaque définition.
- **Interdits** : définition recopiée sans vérification.

### SP12 — Carte mentale

- **Usage** : structure de départ à enrichir (TR21, MF03).
- **Structure** : centre ; quatre branches au cycle 1, six au plus ensuite.
- **Dimensions** : dessin de 37 × 22,5 cm ; texte en 44 pt.
- **Recette** : R9, R11 ; insertion à l'échelle 1.
- **Contrôles** : V17.
- **Interdits** : carte livrée finie quand la classe doit la construire.

### SP13 — Infographie

- **Usage** : chiffres, pictogrammes et textes courts (TR22).
- **Structure** : quatre blocs numérotés dans l'ordre de lecture : chiffre, phrase.
- **Dimensions** : GF-V ; colonnes de 2,2, 9 et 13,5 cm ; blocs de 6,8 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17 ; chaque chiffre a une source, ou porte la mention « exemple fictif ».
- **Interdits** : chiffre inventé présenté comme réel.

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

Les recettes R1 à R6 servent aux exercices, la recette R7 à l'en-tête, la recette R8 aux planches de pièces des jeux. Les recettes R9 à R14 (v7.2) servent à l'affiche A3, à l'écriture liée, au dessin vectoriel, au recto-verso, aux contrôles combinatoires et aux grilles à zones ; la recette R15 (révision du 2.11.2026), à la planche A5. Chaque recette est décrite pour Word (enseignant·e ou IA intégrée à Word) puis renvoie au module python-docx de l'Annexe I-C, testé avec rendu PDF dans cette version.

### R1 — Lignes d'écriture (MP-E-10)

- **R1a, lignes en tableau (méthode par défaut)** : tableau d'**une colonne**, largeur 16 cm ; chaque ligne du tableau a une **hauteur exacte** de 1,0 cm (table 2.1) ; **seule la bordure inférieure** est visible ; lignes « insécables ». Dans Word : Insertion > Tableau > 1 colonne ; Propriétés du tableau > Ligne > Hauteur exacte ; Bordures > Bordure inférieure seule (et bordures intérieures horizontales).
- **R1b, ligne par tabulation (pour une amorce suivie d'une ligne)** : paragraphe à interligne **exact** de 28 pt ; **tabulation droite à 16 cm avec points de suite « ____ »** ; l'amorce est tapée, puis une tabulation trace la ligne jusqu'à la marge. Dans Word : Format > Tabulations > position 16 cm, alignement droite, points de suite 4. La position d'une tabulation se mesure **depuis la marge**, pas depuis le retrait du paragraphe : avec un retrait, la position reste 16 cm. **R1c, lignes d'écriture romandes (1P à 4P, au choix de l'enseignant·e)** : `bande_lignage(base, lignes, module_mm, couleurs, largeur_mm)` dessine une bande de lignes au lignage romand (plafond et plancher en pointillés, ligne du corps en trait fin, ligne de base en trait épais ; fiche G22), insérée à l'échelle 1 par `inserer_image` ; module de 7 mm pour l'entrée dans l'écriture, de 4 mm ensuite (indication non vérifiée à une source officielle, à confirmer avec les cahiers de l'établissement) ; couleurs « ciel, herbe, terre » seulement si l'impression est en couleur. L'IA propose le choix entre R1a et R1c pour une fiche de 1P à 4P qui comporte une zone d'écriture, et garde le même lignage dans toute la fiche ; sans réponse : lignes simples, annoncées en une ligne.
- **Interdit X-02** : des paragraphes vides consécutifs munis d'une bordure inférieure **fusionnent** à l'impression en une seule ligne. Vérifié dans cette version : trois paragraphes ainsi bordés s'impriment comme une seule ligne en bas d'un grand blanc.

### R2 — Lacune dans une phrase (MP-E-11)

- Réservée aux réponses de **1 à 2 mots**.
- Nombre de tirets bas **calculé** selon la police et la taille (table 2.1) : en Arial 14 pt, 22 tirets bas ≈ 6 cm, 29 ≈ 8 cm.
- Interligne 2,0 sur les items.
- Pour deux éléments séparés (auxiliaire et participe), deux lacunes séparées d'un espace sont admises si chacune mesure au moins 3 cm.

#### Typographie insécable (toutes les recettes)

- Les traits d'union des terminaisons et des segments (« -er », « -ir », « -iss- ») sont **insécables**, ainsi que l'espace de « en -ir ». Sans cela, la fin de ligne peut couper « en - » / « ir » (constaté lors du test du 30.10.2026).
- Dans Word : caractères spéciaux « trait d'union insécable » et « espace insécable » (Insertion > Symbole). Dans le module de l'Annexe I-C, la fonction `ecrire` les applique automatiquement.

### R3 — Tableau à compléter

- Lignes de hauteur **au moins** 1 cm (« au moins », pour que le texte ne soit jamais coupé), **insécables** ; ligne d'en-tête répétée.
- Largeur totale ≤ 16 cm ; largeurs de colonnes **fixées** (grille du tableau), jamais laissées en automatique.
- Bordures fines (0,75 pt) grises ou noires, visibles à la photocopie.

### R4 — Solidarité d'un exercice

- Tous les paragraphes d'un exercice, **sauf le dernier**, sont « solidaires du suivant » ; chaque paragraphe a ses « lignes solidaires ».
- Les lignes de tableau sont insécables.
- Ne **pas** enchaîner la solidarité d'un exercice au suivant (le bloc deviendrait plus haut qu'une page et Word l'ignorerait).
- Placer un **saut de page avant** l'exercice qui ne tient plus dans le budget de la page (Étape 2), plutôt que de compter sur la pagination automatique.
- Espace avant chaque consigne ≥ 10 pt ; un paragraphe vide de 6 pt après un tableau pour éviter que la consigne suivante colle à la dernière ligne (fonction `espace` de l'Annexe I-C).

### R5 — Encadré (rappel, aide, objectif de parcours)

- Tableau 1 × 1 bordé, largeur 16 cm, ligne insécable ; trame très claire (gris ≤ F2F2F2) ou aucune trame.
- Jamais de bordure de paragraphe pour un encadré : même risque de fusion que X-02.

### R6 — Symboles, cases et bilan (MP-C-06)

- Vérifié dans cette version : le caractère **☐** et l'étoile **★** **n'existent pas** dans Arial ni dans Calibri ; le demi-cercle **◐** existe dans Arial mais pas dans Calibri. Ils s'affichent par substitution de police, avec une taille et un aspect qui varient selon l'ordinateur.
- Méthode robuste : **bilan en mots dans des cellules** à entourer (« je sais faire » / « presque » / « j'ai besoin d'aide ») ; cases à cocher = **cellules vides bordées** de 0,6 cm.
- Si des symboles sont utilisés : les vérifier sur le rendu (Étape 5) et toujours les doubler d'un mot (MP-C-02).

### R7 — En-tête de la fiche (MP-O-12)

L'en-tête DOIT suivre cet ordre, sur toutes les fiches :

1. **Prénom et Date, tout en haut de la page** (première ligne) : « Prénom : » suivi d'une ligne, puis « Date : » suivi d'une ligne ; lignes tracées par tabulation à points de suite, jamais par des tirets bas tapés.
2. **Titre centré**, avec un espace avant et après d'au moins 12 pt (une ligne blanche).
3. **Objectif en langage élève** : une phrase à la première personne, **sans étiquette** : ni « Mon objectif : » ni « Objectif : » ; la phrase commence directement, avec une majuscule (« J'écris un verbe au passé composé avec ses deux parties. »), avec le vocabulaire du degré, sans code PER ni jargon, en cohérence avec les indices de réussite. La partie enseignant·e garde sa rubrique « Objectif » (§ 4.3, « En bref »).

Le repère discret de version (♣ ♦ ♠, MP-D-01) se place en en-tête de page, au-dessus ou à droite de la ligne Prénom et Date. Dans Word : un paragraphe avec deux tabulations à points de suite (la première vers le milieu de la ligne, la seconde à 16 cm, alignée à droite), puis le titre centré, puis l'objectif.

### R9 — Format affiche A3 (v7.2)

- `page_format` règle le format (A3 ou A4), l'orientation et les marges, puis renvoie la largeur et la hauteur utiles.
- `styles_affiche` crée les styles du § 2.5. `distance_lecture_m` calcule la distance de lecture d'un corps.
- Dans Word : Mise en page > Taille > A3 ; imprimer à 100 %, sans « Ajuster à la page ».
- Testé : dix documents rendus en A3 (29,7 × 42 cm mesurés) ; contenu de 32,3 cm de haut au plus en portrait, sous le budget de 33 cm.

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
- dans « En bref », **ce qui fait apprendre** dans ce jeu, en une ou deux phrases, en partant de la ligne « Fait apprendre si… / N'apprend rien si… » de sa section : le mécanisme qui fait travailler l'objectif (rappel actif, retour immédiat, nombre de réponses par élève et par partie, verbalisation), et ce qui ferait perdre l'apprentissage (attente, hasard dominant, réponse visible) ;
- dans « Déroulement conseillé », une **mise en commun** après la partie : ce qu'on a appris, les erreurs fréquentes, la règle ou la procédure à retenir ;
- dans « Corrigé expliqué », la **solution du jeu** (ordre de la boucle, paires ou familles), avec un « Pourquoi » pour chaque pièce ;
- dans « Différenciation », les **variantes de jeu** : solo, à trois, mélange des lots ; Pour tout jeu de parcours ou de compétition, proposer aussi une **variante coopérative**, fondée sur l'interdépendance positive et la responsabilité individuelle (Johnson & Johnson, 2009) : un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance seul ; un but commun chiffré (tous les pions arrivés en moins de dix tours, vingt cartes réussies) ; des rôles tournants (J13) ; l'aide qui rapporte (si l'explication d'un camarade permet de répondre, les deux avancent) ; l'erreur sans recul (le groupe explique, puis l'élève rejoue) ; des binômes par pion ; un bilan de fin de partie (« qu'est-ce qui nous a aidés ? »).
- dans le rapport de conformité, les contrôles **V11 à V13** (et V14 si le fichier est produit par du code ; V15 à V19 selon le gabarit ; V20 et V21 toujours).

**Pour un jeu ou une dictée**, la partie enseignant·e est une page à part entière, jamais oubliée (V21) : pour un jeu, la règle complète, la solution et le débriefing ; pour une dictée (G20), le texte à dicter en entier. La règle destinée aux élèves est imprimée avec le matériel, en étapes numérotées (MP-J-07), en planche A5 si elle tient sur une demi-page (R15). Avant le test en classe, elle renvoie à la grille « utile, utilisable, acceptable » (Tricot et al., 2003 ; Bibliothèque IA 2).


# ÉTAPE 6 — LIVRER

## 6.1 Gabarits de fiches et de dossiers de jeu

Les éléments entre chevrons `< >` sont à remplacer. Les durées figurent **dans la partie enseignant·e**, jamais sur la fiche élève. `[lignes : n]` désigne n lignes R1a ; `[encadré]` un encadré R5 ; `[bilan R6]` un bilan en mots dans des cellules.

### GF-A — Fiche d'entraînement (2 pages au maximum, environ 30 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                     <Titre de la fiche>                 (centré)

<objectif : une phrase à la 1re personne, en langage élève, sans étiquette>

[encadré] Rappel : <règle courte> — Exemple : <exemple résolu>
          (≤ ¼ de page ; seulement si la notion est nouvelle, fragile,
           réactivée ou combinée)

1  <Consigne directe — repérage>
   <3 à 5 items selon le gabarit>

2  <Consigne directe — entraînement>
   <items + zones selon le gabarit>

—— saut de page placé d'après la fiche technique ——

3  <Consigne directe — entraînement, variante>
   <items + zones>

4  <Consigne directe — transfert ou production>
   [lignes : 2 par phrase demandée ; 5-6 pour un mini-récit]

Je fais le point   [bilan R6 : 3 critères × je sais faire / presque / j'ai besoin d'aide]
```

### GF-B — Fiche d'évaluation (2 pages au maximum, 25-35 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                 <Titre — Évaluation>                    (centré)

<ce que je dois montrer, en langage élève, sans étiquette>     Total : ___ / ___

1  <Consigne — connaissances de base>                       … / __
2  <Consigne — application>                                 … / __
—— saut de page placé d'après la fiche technique ——
3  <Consigne — tâche plus complète>                         … / __
   [lignes : selon la production attendue]
Bonus ★ (facultatif)                                        … / __
```

Règles propres : ni pré-training ni aide-mémoire (MP-PT) ; barème visible ; items courts et une tâche complexe.

### GF-C — Fiche de remédiation (2 pages au maximum, 20-30 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                 <Titre — Je reprends …>                 (centré)

<objectif : une phrase en langage élève, sans étiquette>

1  Coche ce qui te correspond.   [cases R6 : 4 énoncés de difficulté]
   Avec ton enseignant·e, écris correctement un mot ou une forme
   qui te pose souvent problème.   [lignes : 2]
2  [encadré] Rappel : <règle courte> — Exemple : <exemple résolu>
3  <Consigne — entraînement guidé ; aide placée à côté de chaque item>
—— saut de page placé d'après la fiche technique ——
4  <Consigne — entraînement sans aide>
5  <Consigne — re-test : 2 items>
```

### GF-D — Devoir à la maison (1 page, environ 10 minutes)

En-tête R7 (Prénom et Date, titre centré, objectif). Quatre à six items courts et une question « explique ». Consignes compréhensibles **sans adulte**. Pas de pré-training ; une banque de mots PEUT figurer en bas de page avec la mention « Utilise cette aide si tu en as besoin ».

### GF-E — Ateliers (une page par station)

Quatre stations au plus (lire, manipuler, écrire, numérique) ; même structure visuelle d'une station à l'autre (MP-O-09) ; seul le contenu change.

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

### GF-G — Feuille de route par niveaux

- **Usage** : rendre visible une progression en autonomie (TR60, BDRP-B1, MF43).
- **Structure** : en-tête R7 ; tableau « niveau, ce que je sais faire, validé par, date » ; phrase rappelant qu'un niveau se reprend.
- **Dimensions** : 1 page ; colonnes de 2,4, 7,1, 3,5 et 3 cm ; lignes de 1,3 cm ; six à huit niveaux.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : visuels de jeux commerciaux ; niveau affiché comme étiquette de l'élève (X-05).

### GF-H — Trace longitudinale

- **Usage** : même tâche à plusieurs moments, pour voir ses progrès (TR71, BDRP-B2, P21).
- **Structure** : titre ; deux cadres de dessin par page, chacun avec le mois et le prénom.
- **Dimensions** : 1 page ; cadre de 16 × 7 cm ; lignes de 1,2 cm.
- **Recette** : R14.
- **Contrôles** : V1, V3, V7.
- **Interdits** : usage normatif ; production nominative transmise à une IA : l'IA conçoit le gabarit vierge seulement.

### GF-I — Menu à choix

- **Usage** : choix structuré dans un cadre d'exigence (TR61, BDRP-B3, MF46, MF68).
- **Structure** : en-tête R7 ; tableau « obligatoire » ; tableau « au choix » ; question sur les choix faits.
- **Dimensions** : 1 page ; colonnes de 14 et 2 cm ; lignes ≥ 1 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : choix d'exigence inégale ; objectif essentiel placé dans la partie au choix.

### GF-J — Page-son

- **Usage** : étude d'un graphème (TR08, BDRP-A9, MF39, MF66).
- **Structure** : en-tête R7 ; modèle lié, script et capitale, image-clé ; syllabes ; trois mots en deux écritures ; phrase en deux écritures ; copie.
- **Dimensions** : 1 page ; 3P-4P, 18 pt ; modèle lié en minuscule et en majuscule (« ch », « Ch »), 56 pt ; mots et phrase liés en 26 pt ; lignes de 1,2 cm.
- **Recette** : R7, R10, R14, R1a.
- **Contrôles** : V1 à V10, V15.
- **Interdits** : graphème non encore étudié dans les mots ; mot qui ne contient pas le graphème (V21) ; écriture liée dessinée ou générée ; image à dénomination ambiguë.

### GF-K — Carnet de rituel

- **Usage** : même micro-production quotidienne, référentiel à portée de main (TR71, BDRP-B5).
- **Structure** : page quotidienne invariable ; page-référentiel en trois colonnes. La date se demande une seule fois : en-tête R7 sans ligne Date sur la page quotidienne, la date étant écrite dans l'entrée du jour.
- **Dimensions** : 2 pages ; lignes de 1,2 cm ; 18 pt en 3P-4P.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : donner une correction publique du carnet.

### GF-L — Dossier de défis

- **Usage** : série de défis numérotés avec validation (TR60, BDRP-B6).
- **Structure** : en-tête R7 ; consigne ; 12 cases numérotées, chacune avec un défi rédigé, une zone de réponse et la mention « oui · pas encore » à entourer.
- **Dimensions** : 1 page ; cases de 5,33 × 3,6 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : compétition affichée entre élèves ; case de défi vide ou mention de réussite pré-remplie (« Réussi : oui ») (V21).

### GF-M — Brevet d'étape

- **Usage** : reconnaître une compétence validée (TR60, BDRP-I1).
- **Structure** : titre ; prénom ; compétence en « je » ; tableau date, validé par, prochaine étape.
- **Dimensions** : A5 paysage, deux brevets par feuille A4 (planche A5 empilée, R15) ; titre en 40 pt ; texte en 18 pt.
- **Recette** : R14, R15.
- **Contrôles** : V5, V7, V10, V20.
- **Interdits** : épreuve sommative déguisée ; absence de reprise possible.

### GF-N — Fiche théorique

- **Usage** : fixer une règle après la découverte (TR04).
- **Structure** : en-tête R7 ; encadré « Règle » ; tableau d'exemples ; encadré « Attention » ; mention de rangement.
- **Dimensions** : 1 page ; une règle, deux à trois exemples, un cas particulier. Le tableau d'exemples couvre **chaque cas énoncé par la règle** (une règle « -s ou -x » montre un exemple en -s et un exemple en -x) ; sinon, l'énoncé de la règle se limite aux cas illustrés.
- **Recette** : R5, R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : items à résoudre (la fiche clôt, elle ne fait pas chercher) ; forme fautive en contre-exemple (X-13).

### GF-O — Fiche guide

- **Usage** : marche à suivre gardée sous les yeux (TR05) ; fiche d'accompagnement d'un objet, protocole d'expérience, chemin de recherche ou fiche d'usage (TR39, TR40, TR55, TR58).
- **Structure** : en-tête R7 ; exemple résolu ; tableau de six étapes au plus : numéro, action, image.
- **Dimensions** : 1 page ; colonnes de 1,2, 9,8 et 5 cm ; étapes de 2 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : étape à deux actions ; image éloignée de son texte (MP-CC-04) ; notation abrégée non enseignée (« = 2 3 ») : on écrit la forme complète (« 2 dizaines et 3 unités », « 20 + 3 »).

### GF-P — Fiche de synthèse

- **Usage** : résumé à compléter d'une séquence (TR06).
- **Structure** : en-tête R7 ; phrases à trous ; schéma à légender (schéma conforme au contenu des phrases) ; trois questions d'auto-test, chacune suivie d'une ligne de réponse ; verso : « Je vérifie » (réponses) et « Pour aller plus loin » (une question, des lignes).
- **Dimensions** : recto de 22 cm au plus ; verso ; schéma de 14,5 × 5,6 cm.
- **Recette** : R2, R7, R11, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : synthèse livrée finie ; détail décoratif.

### GF-Q — Questionnaire sur document

- **Usage** : chercher une information dans un document réel (TR13) ; variante image (TR24 : je vois, je pense, je me demande) ; variante d'exploration d'une simulation (TR53 : question à tester, essais notés).
- **Structure** : en-tête R7 ; cadre pour le document ; question d'usage ; étapes de recherche ; explication.
- **Dimensions** : cadre de 16 × 6 cm ; 1 page.
- **Recette** : R2, R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : document généré présenté comme authentique ; donnée personnelle visible.

### GF-R — Dossier documentaire et grille de croisement

- **Usage** : enquêter à partir de documents réels (TR14, P17).
- **Structure** : page 1 : question d'enquête et liste des documents (numéro, titre, nature, source). Page 2 : grille de croisement (G9), réponse citant au moins deux documents.
- **Dimensions** : 2 pages ; quatre à six documents ; cellules de 4,5 × 1,8 cm.
- **Recette** : R5, R7, R14, R1a.
- **Contrôles** : V1 à V10 ; chaque source a été consultée.
- **Interdits** : source inventée ; document généré présenté comme réel.

### GF-S — Fiche-trace de sortie

- **Usage** : observer sur le terrain, puis exploiter en classe (TR41) ; relevé d'observations d'une expérience (TR40).
- **Structure** : en-tête R7 ; cadre de dessin et rubriques ; ce que j'entends ; question à poser ; mention pour le retour.
- **Dimensions** : 1 page ; cadre de 9 × 6 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : questionnaire fermé qui empêche d'observer.

### GF-T — Billet de sortie

- **Usage** : mini-retour de fin de leçon (TR66, MF44, MF32).
- **Structure** : trois billets par page : prénom et date ; ce que j'ai compris ; ce qui me reste à comprendre ; trois mots à entourer, précédés de la consigne « Entoure un mot : ».
- **Dimensions** : billet de 16 × 6,4 cm ; zones de 1, 2,2, 2,2 et 1 cm ; marges intérieures de 0,25 cm ; billets séparés par un intervalle et un trait de coupe en tirets.
- **Recette** : R14.
- **Contrôles** : V1, V7, V10 ; MP-J-09 s'applique : le billet n'a pas de titre ni d'objectif.
- **Interdits** : note ; émoji (X-08).

### GF-U — Page de carnet de bord

- **Usage** : entrée courte et régulière (TR71, MF35).
- **Structure** : en-tête R7 sans ligne Date (la date est celle de l'entrée, demandée une seule fois) ; date de l'entrée ; trois questions-guides ; cadre pour une trace collée.
- **Dimensions** : 1 page ; 7 lignes de 1 cm ; cadre de 16 × 4 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : donnée personnelle transmise à une IA.

### GF-V — Affiche A3

- **Usage** : format de base de TR17 à TR22 ; ne contient pas d'exercice.
- **Structure** : titre ; six lignes au plus ; repère, image, texte.
- **Dimensions** : § 2.5.
- **Recette** : R9, R14.
- **Contrôles** : V5, V7, V10, V17.
- **Interdits** : corps sous le plancher ; texte en paragraphe.

### GF-W — Planche de BD

- **Usage** : récit en cases pour présenter une notion (TR23, MF40).
- **Structure** : en-tête R7 ; six cases : image, puis texte ajouté dans le document.
- **Dimensions** : cases de 8 × 3,8 cm ; bandes de texte de 1,2 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10 ; stéréotypes et anachronismes relus.
- **Interdits** : texte généré dans l'image (MP-I-05).

### GF-X — Dossier d'escape game

- **Usage** : énigmes en équipe (TR37, P10, MF64), à partir de GF-F.
- **Structure** : mise en situation, règle et rôles (planche A5, R15) ; planche de cartes-énigmes ; feuille d'équipe (énigme, raison, chiffre, code, débriefing) ; partie enseignant·e (solution, débriefing). Consignes adressées à l'équipe, au pluriel (« Prenez »), sans mélange avec le singulier.
- **Dimensions** : 3 pages ; cartes de 8 × 6,5 cm ; cellules de 1,5 cm.
- **Recette** : R7, R8, R13 (`verifier_code`), R14.
- **Contrôles** : V11 (chaque énigme donne un seul chiffre, la suite donne le code), V12 ; V21 : chaque réponse est calculée par programme et vaut un chiffre de 0 à 9 (`verifier_code` avec le calcul de chaque énigme).
- **Interdits** : énigme sans lien avec l'objectif ; énigme dont la réponse a deux chiffres ou qui en admet plusieurs ; débriefing absent.

### GF-Y — Fiche de comparaison pour le débat

- **Usage** : comparer des productions inventées, puis argumenter (TR62, P05, P13, MF28).
- **Structure** : en-tête R7 ; deux productions ; tableau de critères ; avis écrit.
- **Dimensions** : 1 page ; colonnes de 6, 1,2, 1,2 et 7,6 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : production d'élève identifiable ; forme écrite fautive (X-13) ; mention « (inventée) » ou « (exemple fictif) » sur la face élève : le caractère fictif des productions est dit dans la partie enseignant·e.

### GF-Z — Fiche de commentaire de galerie

- **Usage** : commenter une production affichée (TR63, MF56).
- **Structure** : deux commentaires par page : un point fort, une piste, avec un modèle de phrase ; les deux commentaires sont séparés par un trait de coupe en tirets (MP-J-05, R15).
- **Dimensions** : 1 page ; quatre lignes par commentaire.
- **Recette** : R1a.
- **Contrôles** : V1, V3, V10.
- **Interdits** : exposer sans l'accord de l'élève.

### GF-AA — Grille d'évaluation et version élève

- **Usage** : outil de jugement de l'enseignant·e et version en « je » (TR68, TR67).
- **Structure** : page 1 (destinée à l'adulte) : critères × trois niveaux décrits. Page 2 : en-tête R7, mêmes critères en « je », bilan R6, puis « Ce que je vais améliorer » et des lignes.
- **Dimensions** : quatre colonnes de 4 cm ; cellules ≥ 2 cm ; 11 pt pour la page adulte.
- **Recette** : R6, R7, R14.
- **Contrôles** : V5, V8 ; critères alignés sur l'objectif ; [À VÉRIFIER dans le PER] si le texte n'a pas été consulté.
- **Interdits** : niveau défini par un adverbe seul ; version élève différente de la grille de l'adulte : mêmes critères, dans le même ordre, mêmes trois niveaux, formulés en « je » (contrôle ligne à ligne, V5) ; consigne « J'entoure le niveau que j'ai atteint. » obligatoire sur la page élève.

### Variantes de GF-B

- **GF-B2 — Grille à deux niveaux** (BDRP-B4) : colonnes « critères de base » et « perfectionnement ». Colonnes de 4, 6 et 6 cm. Objectif en langage élève en tête (R7) ; l'objectif du PER, ou la mention [À VÉRIFIER dans le PER], figure dans la partie enseignant·e, jamais sur la fiche élève. Courte : lignes de commentaire, puis planche A5 (R15).
- **GF-B3 — En-tête d'évaluation avec ressenti et aménagements** (BDRP-B7, MF73, variante de MF32) : deux bandeaux sous R7, tous deux faits de **zones de tracé**, jamais de lignes d'écriture (révision du 2.11.2026, suite). Bandeau 1 « Avant de commencer » : consigne « Entoure comment tu te sens. » ; trois repères à entourer (mots, par exemple « prêt·e · un peu inquiet·ète · perdu·e » ; aucun émoji, X-08), cellules de 4 à 6 cm × 1,1 cm. Bandeau 2 « Mes aménagements » : consigne « Coche ce que tu utilises. » ; cases à cocher (carré de 0,8 cm en bordure de la première colonne) devant chaque aménagement, trois à six items, lignes de 0,8 cm. Le reste de la page est l'évaluation elle-même (gabarit G ou GF) : **toute tâche de tracé ou de dessin (« Trace… », « Dessine… ») reçoit un cadre vide de 16 cm de large et de 2,4 cm au moins**, jamais des lignes d'écriture ; une question reçoit une ligne (R1b) ou une lacune (R2). Pour la page pleine, compléter par le contenu de l'évaluation, pas par des items d'aménagement (MP-O-14) ; les deux bandeaux tiennent en 6 cm. Les aménagements cochés restent visibles des pairs : à réserver à une version individuelle.

Tous les gabarits GF-G à GF-AA, GF-B2 et GF-B3 sont testés sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; leurs dimensions sont des inférences de conception, à ajuster après usage (MP-P-08).

## 6.2 Barèmes et codes de retour

**Barème générique par item (0-1-2)** : 2 = correct, avec la méthode ou la justification si elle est demandée ; 1 = idée juste, mais erreur de forme ou oubli partiel ; 0 = hors sujet ou non fait.

**Production écrite (/4)** : contrainte respectée (1) + contenu (1) + forme (1) + clarté (1).

**Fiche d'entraînement** : un retour critère par critère (« acquis » / « en cours » / « à revoir ») est préférable à une note.


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
