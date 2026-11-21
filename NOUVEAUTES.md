# Nouveautés

## 21 novembre 2026 (analyser, puis transformer une ressource)

- Guide, page « Améliorer une ressource » : deux temps séparés. « Analyser une fiche / ressource » : l'IA remet un bref rapport (ce qu'elle comprend du document, ce qui fonctionne, possibilités d'amélioration numérotées) et demande de confirmer ou de corriger sa lecture. « Transformer votre fiche / ressource (facultatif) » : l'enseignant·e coche la possibilité retenue et colle un second texte.
- Textes destinés à l'IA visibles sur toutes les pages, en langage courant, sans code ni renvoi chiffré ; les détails sont dans la Bibliothèque IA 1 : § 0.6 « Analyser, puis transformer une ressource » et § 0.7 « Demandes venant du guide web », avec l'index qui relie chaque nom du guide à son gabarit, contrôlé par `outils/verifier.py`.
- Bibliothèque IA 1, § 6.4 : prompt court « Analyser, puis transformer ».

## 21 novembre 2026 (arbitrages)

Décisions de l'auteur sur les propositions de la révision d'ensemble, appliquées le même jour (même édition).

- Orthographe : par défaut, l'élève ne voit toujours que des formes correctes ; exception encadrée, sur décision de l'enseignant·e, dès la 5P et pour une notion déjà enseignée : une analyse d'erreurs où chaque forme fautive est marquée, corrigée et justifiée, une seule fois, jamais en distracteur ni en exemple. Aucune exception au cycle 1 (Bibliothèque IA 1, § 3.7, règles X-13, MP-CC-11, V10 ; Bibliothèque IA 2, patrons et micro-formats concernés ; guide, rubrique « Vérifier »).
- Élèves et IA : de la 1P à la 8P, une fiche ne demande jamais à un·e élève d'utiliser un outil d'IA ; de la 9S à la 11S, seulement sur demande de l'enseignant·e, avec un outil fourni ou autorisé par le canton ou l'établissement, en classe, et pour vérifier ou critiquer la réponse de l'outil (Bibliothèque IA 1, § 1.5 et instruction système).
- Secondaire I : les valeurs de la 9S-11S (colonne 7P-8P, texte de 12 pt) et le tutoiement par défaut sont confirmés.
- Liseré des cartes et police d'élèves des exemples : conventions du projet, appliquées par défaut ; l'enseignant·e peut demander de s'en passer.
- Fonctions : les huit fonctions du guide restent la porte d'entrée ; leur correspondance avec les 43 fonctions de la Bibliothèque IA 2 est donnée dans les deux bibliothèques, avec les fonctions qu'elles ne couvrent pas (diagnostic, autoévaluation, métacognition, régulation…) ; le guide le signale.
- Codes : plus aucun code de gabarit dans les panoramas (« Dites le nom »), dans les titres et mentions des modèles Word, ni dans les mentions des planches ; les codes restent dans les noms de fichiers et dans les bibliothèques. Panoramas et aperçus du guide refaits.
- Table des correspondances : les ateliers différenciés et le rallye de postes admettent désormais les gabarits G1 à G25 (et G29 à G31 pour les ateliers).
- Modules : la Bibliothèque IA 1 intégrale reste la source unique ; le script `outils/modules.py` en tire sept modules (noyau, fiches, jeux, différenciation et accessibilité, séquences, vérification et livraison, code des recettes), à l'essai dans `bibliotheques/modules`. `outils/verifier.py` contrôle qu'ils sont à jour.
- Police GE Typo Libre : mention ajoutée dans LICENCE.md ; conditions de diffusion à vérifier auprès du DIP.

## Édition du 21 novembre 2026 (révision d'ensemble)

- Bibliothèques : en-tête opérationnel (édition, champ, dépendances) à la place du long historique, déplacé ci-dessous ; la Bibliothèque IA 3 n'est plus annoncée (le guide est une page web) ; dénombrements corrigés (71 types de ressources, 72 micro-formats, gabarits G1 à G31).
- Bibliothèque IA 1 : priorité des règles (sécurité et droit, DOIT, règles conditionnelles, DEVRAIT, conventions, préférences de l'enseignant·e) et quatre statuts de vérification ; degrés 1P à 11S, cycle 3 et valeurs proposées pour la 9S-11S (§ 1.5, § 2.1, instruction système).
- Guide : quatre entrées par besoin (améliorer une ressource, créer, composer une séquence, explorer), demande qui nomme les fichiers à joindre, prévoit un repli si l'outil ne produit pas de Word et demande les statuts de vérification ; formats disponibles affichés sur chaque fiche ; séquence avec ressources permanentes, observation et ajustement ; exemple commenté de bout en bout ; aperçus chargés à la demande (page plus légère) ; lien d'évitement et texte de présentation lisible sans JavaScript.

## 21 novembre 2026 (suite)

- Exemples en police d'élèves : partout où un exemple est donné ou affiché, il est écrit en GE Typo Libre, pour distinguer ce qui est donné de ce qui est montré en exemple (règle MP-T-10, fonctions `ecrire_exemple` et `taille_eleve`, police `'Eleve'` des dessins) ; maisons des nombres, exemples de formes de fiches et affiches mis à jour.
- Liseré dans les recettes PDF (`lisere_cartes`, option `lisere=True` de `planche_pdf`) ; planches de bataille, de cartes à terminaisons et de mots interdits refaites avec liseré et texte agrandi.
- Livret d'écriture : la couverture porte un cadre vide pour le prénom, sans ligne Prénom ni Classe.
- Panoramas des jeux, des tranches d'âge, des fiches et supports, des formes de fiches et des affiches refaits à partir des documents actuels.
- Exemples remplis des jeux en Word : un calcul ne se coupe plus en fin de ligne (espaces insécables autour des signes et devant « % ») ; liseré contrôlé dans Word pour les jeux de cartes.
- Guide : nouvelle rubrique « Conseils » (règles du jeu en cinq questions, coopération, différenciation autour d'une fiche unique, grille « utile, utilisable, acceptable » à remplir) ; option « en coopération » dans la demande d'un jeu.
- Bibliothèque IA 1 : règles MP-J-07 et MP-D-02 complétées, astuces pratiques et variante coopérative dans la partie enseignant·e.
- Bibliothèque IA 2 : section « Repères pour les jeux, la coopération et la différenciation ».
- Mention de la licence CC BY-NC-SA 4.0 dans les deux bibliothèques.
- Non-lecteurs : aucune consigne écrite destinée à l'élève, mais un exemple déjà fait en tête de la fiche et une ligne « Pour l'adulte » en bas de page (règle, recettes G23 et G24, page-son).
- Cartes : liseré à coins arrondis à 3 mm du trait de coupe, marge blanche autour (dix jeux de cartes, modèles et exemples ; règle MP-J-14).
- Carte à pinces : numéro à gauche, question centrée et agrandie. Plateaux : « Départ » et « Arrivée » aussi grands que la case le permet.
- Mot mystère : « cases teintées » ; dans les fichiers en couleur, « fond teinté » au lieu de « fond gris ».
- Jeux de cartes (memory, familles, cartes de rappel, cartes-défis, cartes de rôle, d'erreurs et d'aide) : le texte est agrandi pour occuper la carte, dans les modèles et dans les exemples.
- Conjugaison : « je (chanter) », l'infinitif en italique.
- Trois affiches redessinées, à titre d'essai : « Je me lave les mains », « Pour résoudre un problème », « b, d, p ou q ? ».
- Exemples de formes de fiches : pages pleines (aération automatique jusqu'à 92 % de la hauteur au moins) ; fiche d'entraînement enrichie.
- Exercice « Entourer » : mots espacés et interligne large ; nouvelle recette `pictogramme_consigne` (le geste et le mot visé, par exemple « verbe » entouré).
- Jeunes élèves (1P-2P) : plus de ligne « Prénom » ni « Date » ; mention « Prénom au dos de la feuille » (règle MP-O-03, recettes `entete(..., jeunes=True)` et `definir_jeunes`). Fiches G22 (7 mm), G23 et G24 corrigées.
- Exemples de jeux plus variés : conjugaison au présent, participes passés, pluriel des noms, contraires, synonymes, nature des mots, pays et capitales.
- Aspect retravaillé : numéros lisibles sur « Serpents et échelles », mots mieux répartis dans « Cherche et trouve », carte à pinces centrée, cartons de loto mieux délimités, « Départ » et « Arrivée » plus grands sur les plateaux.
- Nouveau nom du guide : « Composer un écosystème de ressources ». Nouvelle rubrique « Composer une séquence » : plusieurs ressources reliées, chacune avec sa fonction, et une demande d'ensemble pour l'IA.
- Page « Qu'est-ce qu'un écosystème de ressources ? » dans les Conseils, et section correspondante dans la Bibliothèque IA 2 (définition de travail, cinq critères, conduite attendue de l'IA).
- Étoiles de difficulté : admises sur demande (un choix dans la demande du guide ; règles MP-D-01 et MP-J-06 de la Bibliothèque IA 1).
- Guide : plus aucun code dans les textes affichés ; la demande à l'IA se termine par une ligne « Repère pour l'IA ».
- Pictogrammes de consigne : un choix dans la demande du guide et une option dans la Bibliothèque IA 1 les font placer devant chaque consigne (codes IC-CON).
- Bibliothèque IA 2 : références CTREQ et Maitre (2020) ajoutées, trois défauts de mise en page corrigés dans le Word.

## 21 novembre 2026
- Toutes les planches existent aussi en couleur (fichiers « (couleur) »).
- Treize exemples de jeux remplis de vrais contenus, à adapter (fichiers « Exemple rempli »).
- Modèles Word : correction d'une page vide en fin de document dans Word.
- Licence CC BY-NC-SA 4.0.
- Guide en ligne (`index.html`).
- Exemples en couleur des 27 formes de fiches et des 13 affiches et aides permanentes.
- Couleur en option pour les jeux dessinés et versions en couleur des modèles Word.
- De la 1P à la 4P : lignes simples ou lignes d'écriture romandes, au choix.
- Nouveaux supports : calendrier, horaire, livret à onglets, journal de classe, bande dessinée, exposé, maisons des nombres, quadrillage.
- Panoramas des formes de fiches et des affiches.

## 20 novembre 2026
- Dix-huit nouveaux jeux, dont les puzzles, le mot mystère, la cocotte, l'horloge, le petit bac, les petits chevaux et le sudoku.
- Lignes d'écriture romandes, syllabes et sons.
- Panoramas composés de vraies pages.

## 19 novembre 2026
- Grille d'alignement, serpents et échelles, bataille navale, roue de tirage.
- Quatre plateaux de parcours, dés à monter, dos de cartes à motif.
- Modèles Word à remplir.

## 2 novembre 2026
- Mise à jour de la version 1.

## 31 octobre 2026
- Version 1 des bibliothèques.

## Historique détaillé des bibliothèques (notes d'origine)

**Bibliothèque IA 1.** Version v1 du 31 octobre 2026, mise à jour le 2 novembre 2026 : Référentiel pédagogique IA 7.2, révision du 2 novembre 2026 (page pleine MP-O-14 et planche A5 R15 ; objectif sans étiquette ; contrôles V20 et V21), suite du 2 novembre 2026 (MP-J-10 pièces mobiles et cases d'accueil ; SP6 par tests opératoires ; GF-B3 en zones de tracé ; J10 refondu en carte à pinces multi-questions avec règle élève ; intitulés des zones laissées à la classe ; points mineurs des gabarits) ; 3 novembre 2026 : G21 Imagier et scène à légender (TR16), fonctions scene_numerotee, lignes_numerotees, bande_etiquettes, verifier_imagier. Types de ressources alignés sur le Catalogue Ressources au primaire (71 types, TR01 à TR71 ; renumérotation du 3 novembre 2026 : l'imagier prend TR16, les types TR16 à TR70 du 2 novembre deviennent TR17 à TR71) ; éléments de réalisation complétés pour chaque type. 19 novembre 2026 : planches à découper — toute la surface utile de la page (MP-J-11) et repères de coupe pour le massicot (MP-J-12) ; gabarit J2 redimensionné ; J5 refondu en quatre plateaux de parcours dessinés, sans tableau (serpent, escargot, chemin, circuit ; fonction plateau_parcours) ; gabarits J1, J3, J4, J6 à J8 et J12 à J16 redimensionnés pour la page entière ; fonctions planche_pdf et reperes_de_coupe ; MP-J-13 : l'IA montre le panorama des jeux et attend le choix (fonction panorama_jeux) ; variantes des jeux par tranche d'âge (1P-4P, 5P-8P, 9S-11S) et miniatures des formats (fonction miniatures_tranche) ; MP-J-14 : carte tirée à dos neutre, solutions sur une feuille numérotée ; carte à pinces sur toute la page (6, 10 ou 12 questions) ; dé à monter grand ou petit (fonction de_a_monter) ; dos à motif des cartes tirées (fonction dos_a_motif : motif encadré à 3 mm du bord, mention personnelle possible ; l'IA demande dos à motif ou blanc, avec ou sans mention) ; quatre gabarits de jeu ajoutés : J17 grille d'alignement, J18 serpents et échelles, J19 bataille navale, J20 roue de tirage ; panorama des exercices G1 à G21 (fonction panorama_exercices) ; modèles Word à remplir et planches prêtes à imprimer signalés au § 3.8 ; instruction système complétée (présentation des possibilités, questions sur le dos des cartes) ; 20.11.2026 : panorama des jeux et pages par tranche d'âge composés uniquement de miniatures tirées des documents réels ; un document réel pour chaque gabarit J1 à J20 (modèles J3, J8, J9, J12, J13, J15, J16 ; planche J11) ; plan_projectif corrigé pour n = 4 ; sept gabarits ajoutés : J21 puzzles à deux pièces, J22 puzzle à bandes, J23 mot mystère, J24 cocotte en papier, J25 horloge à aiguilles, J26 mémo-fiches en éventail, J27 bandes graphiques ; puis J28 plateau à camemberts, J29 cherche et trouve de mots, J30 mots interdits, J31 petit bac et G22 lignes d'écriture au lignage romand ; puis J32 cartes à terminaisons, J33 petits chevaux, J34 Qui est-ce ?, J35 bataille, J36 tuiles-lettres, J37 sudoku, J38 mot caché (la fleur, à la place du pendu), G23 syllabes et sons, cartes-questions de J28 et livret d'écriture A5 ; 21.11.2026 : G24 maisons des nombres, G25 reproduction sur quadrillage, G26 à G31 supports de classe et mises en page de projets (calendrier, étiquettes de l'horaire, livret à onglets, journal, bande dessinée, exposé) ; le guide pour l'enseignant·e est remplacé par une page web ; lignes d'écriture au choix en 1P à 4P : lignes simples ou lignes romandes (R1c, `bande_lignage`) ; couleur en option pour les dessins R11 (`definir_couleur`) ; règle du jeu en cinq questions, variante coopérative, astuces pratiques et différenciation autour d'une fiche unique (MP-J-07, MP-D-02, § 4.3) ; option « pictogrammes de consigne » (§ publics, codes IC-CON) ; étoiles de difficulté admises sur demande (MP-D-01, MP-J-06) ; J18 : numéros sur pastille ; J29 : mots mieux répartis ; J5 : « Départ » et « Arrivée » d'au moins 11 pt ; jeunes élèves : pas de ligne Prénom ni Date (MP-O-03, `definir_jeunes`) ; G1 : blancs pour entourer un mot dans une phrase, pictogramme composé `pictogramme_consigne` ; plateaux : « Départ » et « Arrivée » en grand ; carte à pinces : numéro à gauche, question centrée en grand ; J23 : « cases teintées » ; cartes : liseré à coins arrondis (MP-J-14), puis dans les recettes PDF (`lisere_cartes` ; J28, J30, J32, J35) ; non-lecteurs : aucune consigne écrite, un exemple déjà fait en tête de fiche (G23, G24) ; exemples en police d'élèves GE Typo Libre (MP-T-10, `ecrire_exemple`, `taille_eleve`, police `'Eleve'` de `Dessin`) ; couverture du livret d'écriture : cartouche du prénom sans ligne. Licence : CC BY-NC-SA 4.0. Emmanuel Flaction – emmanuel.flaction@hepl.ch

**Bibliothèque IA 2.** Version v1 du 31 octobre 2026, mise à jour le 2 novembre 2026 : Référentiel pédagogique IA 7.2, révision du 2 novembre 2026 (en-tête des fiches sans étiquette « Mon objectif », Livre I). Types de ressources alignés sur le Catalogue Ressources au primaire (71 types, TR01 à TR71, numérotation des cartes ; TR16 Imagier et scène à légender ajouté le 3 novembre 2026, les types TR16 à TR70 du 2 novembre devenant TR17 à TR71) ; éléments de réalisation complétés pour chaque type. Emmanuel Flaction – emmanuel.flaction@hepl.ch Licence : CC BY-NC-SA 4.0.
