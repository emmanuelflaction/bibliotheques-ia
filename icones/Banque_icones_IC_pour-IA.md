# Banque d'icônes IC — fichier à joindre à l'IA (v1.2, novembre 2026)

Licence : CC0 1.0 Universel (domaine public). 79 icônes noir et blanc pour les ressources imprimées du primaire. Fichiers : `png/CODE.png` (600 px de large ou de haut, à insérer) et `svg/CODE.svg` (source vectorielle).

## Règle pour l'IA

1. Pour une main qui compte, un repère de latéralité, une face de dé, un visage ou une émotion, un pictogramme de consigne, une modalité de travail, une modalité de vérification, du matériel de base dix, une horloge sans aiguilles ou des arcs syllabiques, utilise l'icône IC correspondante. Ne la dessine pas, ne la génère pas, ne la remplace pas par un emoji.
2. Si tu peux créer le fichier Word (exécution de code) et que les fichiers PNG sont joints : insère l'image à la taille conseillée et ajoute le texte de remplacement indiqué.
3. Si tu ne peux pas insérer d'image : écris le code entre crochets à l'endroit voulu, par exemple `[IC-CON-ENTOURE]`, et signale-le. L'enseignant·e remplacera chaque code par l'image.
4. N'utilise que les codes de la liste ci-dessous. N'invente aucun code.
5. Un pictogramme de consigne se place à gauche de la consigne écrite, qu'il ne remplace pas ; garde le même pictogramme pour la même action dans toute la ressource.
6. Mains : convention « pouce d'abord » (1 = pouce ; 2 = pouce et index…), mains vues de dos. Si l'enseignant·e indique une autre convention de comptage, n'utilise pas IC-MAIN et signale-le.
7. Visages et émotions : le sens tient aux traits du visage (bouche, yeux, sourcils) ; ne donne jamais le sens par la seule couleur. Pour nommer une émotion (joie, tristesse, colère, peur, surprise, dégoût, calme), utilise IC-EMO-* ; pour l'échelle content / moyen / pas content, IC-VIS3-*. Un visage exprime un ressenti : pour l'auto-évaluation d'un apprentissage, propose plutôt une échelle de mots (« je sais faire seul·e / avec aide / pas encore »).
8. Vérification : pour un jeu ou une fiche autocorrective, indique qui vérifie avec IC-VER-CORRIGE, IC-VER-CAMARADE ou IC-VER-ENSEIGNANT, et fournis le corrigé quand il est nécessaire.

## Insertion par script (python-docx)

```python
from docx import Document
from docx.shared import Cm

doc = Document()
p = doc.add_paragraph()
run = p.add_run()
run.add_picture('png/IC-CON-ENTOURE.png', height=Cm(1.3))
# texte de remplacement : propriété descr de l'élément wp:docPr
run._r.xpath('.//wp:docPr')[0].set('descr', 'Pictogramme : entoure')
p.add_run('  Entoure les mots qui commencent par « ch ».')
doc.save('fiche.docx')
```

## Catalogue

### Mains de comptage

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-MAIN-0 | Main : 0 | 2 à 2,5 cm de haut | Un poing fermé (zéro) | Main droite fermée vue de dos, pouce replié sur le côté (zéro). |
| IC-MAIN-1 | Main : 1 | 2 à 2,5 cm de haut | Une main montrant 1 doigt | Main droite vue de dos, 1 doigt levé, convention « pouce d'abord ». |
| IC-MAIN-2 | Main : 2 | 2 à 2,5 cm de haut | Une main montrant 2 doigts | Main droite vue de dos, 2 doigts levés, convention « pouce d'abord ». |
| IC-MAIN-3 | Main : 3 | 2 à 2,5 cm de haut | Une main montrant 3 doigts | Main droite vue de dos, 3 doigts levés, convention « pouce d'abord ». |
| IC-MAIN-4 | Main : 4 | 2 à 2,5 cm de haut | Une main montrant 4 doigts | Main droite vue de dos, 4 doigts levés, convention « pouce d'abord ». |
| IC-MAIN-5 | Main : 5 | 2 à 2,5 cm de haut | Une main montrant 5 doigts | Main droite vue de dos, 5 doigts levés, convention « pouce d'abord ». |
| IC-MAIN-6 | Mains : 6 | 2 à 2,5 cm de haut | Deux mains montrant 6 doigts | Main gauche ouverte (5) et main droite montrant 1, convention « pouce d'abord » ; mains vues de dos. |
| IC-MAIN-7 | Mains : 7 | 2 à 2,5 cm de haut | Deux mains montrant 7 doigts | Main gauche ouverte (5) et main droite montrant 2, convention « pouce d'abord » ; mains vues de dos. |
| IC-MAIN-8 | Mains : 8 | 2 à 2,5 cm de haut | Deux mains montrant 8 doigts | Main gauche ouverte (5) et main droite montrant 3, convention « pouce d'abord » ; mains vues de dos. |
| IC-MAIN-9 | Mains : 9 | 2 à 2,5 cm de haut | Deux mains montrant 9 doigts | Main gauche ouverte (5) et main droite montrant 4, convention « pouce d'abord » ; mains vues de dos. |
| IC-MAIN-10 | Mains : 10 | 2 à 2,5 cm de haut | Deux mains montrant 10 doigts | Main gauche ouverte (5) et main droite montrant 5, convention « pouce d'abord » ; mains vues de dos. |

### Latéralité

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-LAT-D | Main droite (repère) | 1,5 à 2 cm | Main droite (repère) | Dos de la main droite posée sur la table, vue par l'élève (pouce à gauche). |
| IC-LAT-G | Main gauche (repère) | 1,5 à 2 cm | Main gauche (repère) | Dos de la main gauche posée sur la table, vue par l'élève (pouce à droite). |

### Constellations de dé

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-DE-0 | Dé : 0 | 1,2 à 2 cm | Face de dé vide | Face de dé à 0 point, disposition standard. |
| IC-DE-1 | Dé : 1 | 1,2 à 2 cm | Face de dé montrant 1 point | Face de dé à 1 point, disposition standard. |
| IC-DE-2 | Dé : 2 | 1,2 à 2 cm | Face de dé montrant 2 points | Face de dé à 2 points, disposition standard. |
| IC-DE-3 | Dé : 3 | 1,2 à 2 cm | Face de dé montrant 3 points | Face de dé à 3 points, disposition standard. |
| IC-DE-4 | Dé : 4 | 1,2 à 2 cm | Face de dé montrant 4 points | Face de dé à 4 points, disposition standard. |
| IC-DE-5 | Dé : 5 | 1,2 à 2 cm | Face de dé montrant 5 points | Face de dé à 5 points, disposition standard. |
| IC-DE-6 | Dé : 6 | 1,2 à 2 cm | Face de dé montrant 6 points | Face de dé à 6 points, disposition standard. |

### Visages

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-VIS3-CONTENT | Visage content (échelle à 3) | 1,2 à 1,8 cm | Visage content | Échelle à trois visages ; le sens tient à la forme de la bouche, pas à la couleur (coloriable). |
| IC-VIS3-MOYEN | Visage moyen (échelle à 3) | 1,2 à 1,8 cm | Visage moyen | Échelle à trois visages ; le sens tient à la forme de la bouche, pas à la couleur (coloriable). |
| IC-VIS3-PAS-CONTENT | Visage pas content (échelle à 3) | 1,2 à 1,8 cm | Visage pas content | Échelle à trois visages ; le sens tient à la forme de la bouche, pas à la couleur (coloriable). |
| IC-VIS-VIERGE | Visage à compléter | 1,5 à 2 cm | Visage sans bouche, à compléter | Visage sans bouche : l'élève dessine lui-même son ressenti. |

### Émotions

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-EMO-JOIE | Joie | 1,5 à 2 cm | Visage : joie | Joie : grand sourire ouvert. Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-TRISTESSE | Tristesse | 1,5 à 2 cm | Visage : tristesse | Tristesse : sourcils relevés au centre, bouche vers le bas, une larme. Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-COLERE | Colère | 1,5 à 2 cm | Visage : colère | Colère : sourcils froncés en V, dents serrées. Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-PEUR | Peur | 1,5 à 2 cm | Visage : peur | Peur : sourcils inquiets, yeux grands ouverts, bouche qui tremble. Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-SURPRISE | Surprise | 1,5 à 2 cm | Visage : surprise | Surprise : sourcils hauts et arrondis, yeux grands ouverts, bouche en O. Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-DEGOUT | Dégoût | 1,5 à 2 cm | Visage : dégoût | Dégoût : yeux plissés, langue tirée (« beurk »). Le sens tient aux traits du visage, pas à la couleur (coloriable). |
| IC-EMO-CALME | Calme | 1,5 à 2 cm | Visage : calme | Calme : yeux fermés, léger sourire. Le sens tient aux traits du visage, pas à la couleur (coloriable). |

### Pictogrammes de consigne

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-CON-ENTOURE | Entoure | 1,2 à 1,5 cm | Pictogramme : entoure | Consigne « Entoure », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-SOULIGNE | Souligne | 1,2 à 1,5 cm | Pictogramme : souligne | Consigne « Souligne », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-BARRE | Barre | 1,2 à 1,5 cm | Pictogramme : barre | Consigne « Barre », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COCHE | Coche | 1,2 à 1,5 cm | Pictogramme : coche | Consigne « Coche », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-RELIE | Relie | 1,2 à 1,5 cm | Pictogramme : relie | Consigne « Relie » : des formes identiques reliées de gauche à droite, d'un point à l'autre ; un trait fini, un trait en cours ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COLORIE | Colorie | 1,2 à 1,5 cm | Pictogramme : colorie | Consigne « Colorie », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-ECRIS | Écris | 1,2 à 1,5 cm | Pictogramme : écris | Consigne « Écris », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-DESSINE | Dessine | 1,2 à 1,5 cm | Pictogramme : dessine | Consigne « Dessine », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-DECOUPE | Découpe | 1,2 à 1,5 cm | Pictogramme : découpe | Consigne « Découpe », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COLLE | Colle | 1,2 à 1,5 cm | Pictogramme : colle | Consigne « Colle », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-LIS | Lis | 1,2 à 1,5 cm | Pictogramme : lis | Consigne « Lis », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-ECOUTE | Écoute | 1,2 à 1,5 cm | Pictogramme : écoute | Consigne « Écoute », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-DIS | Dis, parle | 1,2 à 1,5 cm | Pictogramme : dis, parle | Consigne « Dis, parle », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-OBSERVE | Observe | 1,2 à 1,5 cm | Pictogramme : observe | Consigne « Observe », à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COMPTE | Compte | 1,2 à 1,5 cm | Pictogramme : compte | Consigne « Compte » : quatre points ; 1, 2, 3 sont écrits dessous, le 4 est presque fini (trait fin) ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-CALCULE | Calcule | 1,2 à 1,5 cm | Pictogramme : calcule | Consigne « Calcule » : 2 + 2 = ; la réponse (4) s'écrit dans la case, en trait fin, presque finie ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-CHERCHE | Cherche | 1,2 à 1,5 cm | Pictogramme : cherche | Consigne « Cherche » : le modèle (une étoile) seul en haut ; en bas, la loupe le retrouve parmi d'autres formes ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COMPARE | Compare | 1,2 à 1,5 cm | Pictogramme : compare | Consigne « Compare » : deux tours de cubes, un œil et une flèche double (sans signe mathématique) ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-COMPLETE | Complète | 1,2 à 1,5 cm | Pictogramme : complète | Consigne « Complète » : a ▢ c ; la lettre qui manque (b) s'écrit dans la case, en trait fin, pas encore finie ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-CORRIGE | Corrige | 1,2 à 1,5 cm | Pictogramme : corrige | Consigne « Corrige » : l'erreur est barrée ; la bonne réponse (4) s'écrit au-dessus, en trait fin, presque finie ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-EFFACE | Efface | 1,2 à 1,5 cm | Pictogramme : efface | Consigne « Efface » : la gomme efface le c de « abc » (lettre grisée, encore visible) ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-ENCADRE | Encadre | 1,2 à 1,5 cm | Pictogramme : encadre | Consigne « Encadre » : un cadre rectangulaire autour du mot (à distinguer d'« Entoure ») ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-LEVE-LA-MAIN | Lève la main | 1,2 à 1,5 cm | Pictogramme : lève la main | Consigne « Lève la main » : main levée vue de dos, index tendu à gauche, pouce replié, avec l'avant-bras ; traits de mouvement de part et d'autre de la main ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-MESURE | Mesure | 1,2 à 1,5 cm | Pictogramme : mesure | Consigne « Mesure » : un segment aligné sur le 0 d'une règle graduée et le résultat (7 cm) ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-NUMEROTE | Numérote | 1,2 à 1,5 cm | Pictogramme : numérote | Consigne « Numérote » : trois images de la croissance d'une plante (graine, pousse, fleur) ; les numéros 1 et 2 sont écrits en trait fin, le 3 est en cours ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-PEINS | Peins | 1,2 à 1,5 cm | Pictogramme : peins | Consigne « Peins » : une palette de peinture et un pinceau d'artiste (manche, virole, poils chargés de peinture) qui trace une bande de peinture ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-QUESTION | Pose une question | 1,2 à 1,5 cm | Pictogramme : pose une question | Consigne « Pose une question » : une personne et une bulle avec un point d'interrogation ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-RACONTE | Raconte | 1,2 à 1,5 cm | Pictogramme : raconte | Consigne « Raconte » : une personne et une bulle ; dans la bulle, une scène d'histoire (maison, arbre, soleil) (à distinguer de « Dis ») ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-RANGE | Range | 1,2 à 1,5 cm | Pictogramme : range | Consigne « Range » : cahier, ciseaux, crayon et colle ; une flèche part de chaque objet vers la boîte ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-RECOPIE | Recopie | 1,2 à 1,5 cm | Pictogramme : recopie | Consigne « Recopie » : un modèle de boucles en trait épais sur la ligne du haut, la copie en trait fin, en cours, sur la ligne du bas ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-REFLECHIS | Réfléchis | 1,2 à 1,5 cm | Pictogramme : réfléchis | Consigne « Réfléchis » : une personne et une bulle de pensée avec une ampoule ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-REPONDS | Réponds | 1,2 à 1,5 cm | Pictogramme : réponds | Consigne « Réponds » : une question ; la réponse s'écrit sur la ligne, en trait plus fin, pas encore finie ; à placer à gauche de la consigne écrite (non-lecteurs). |
| IC-CON-TRIE | Trie | 1,2 à 1,5 cm | Pictogramme : trie | Consigne « Trie » : deux ensembles ; un rond descend dans l'ensemble des ronds ; à placer à gauche de la consigne écrite (non-lecteurs). |

### Modalités de travail

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-MOD-SEUL | Seul·e | 1,2 à 1,5 cm | Seul·e | Travail individuel. |
| IC-MOD-DEUX | À deux | 1,2 à 1,5 cm | À deux | Travail en duo. |
| IC-MOD-GROUPE | En groupe | 1,2 à 1,5 cm | En groupe | Travail en groupe autour d'une table. |
| IC-MOD-SEUL-PUIS-DEUX | Seul·e, puis à deux | 1,2 à 1,5 cm de haut | Seul·e, puis à deux | Chercher d'abord seul·e, puis comparer avec un·e camarade. |

### Vérification

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-VER-CORRIGE | Je vérifie avec le corrigé | 1,2 à 1,5 cm de haut | Vérifier soi-même avec le corrigé | L'élève, à gauche, compare ses réponses avec le corrigé, à sa droite (fiches et jeux autocorrectifs). |
| IC-VER-CAMARADE | Un·e camarade vérifie | 1,2 à 1,5 cm de haut | Faire vérifier par un·e camarade | L'élève, à gauche, fait vérifier sa réponse par un·e camarade, à sa droite (jeux, entraînement à deux). |
| IC-VER-ENSEIGNANT | L’enseignant·e vérifie | 1,2 à 1,5 cm de haut | Faire vérifier par l'enseignant·e | L'élève, à gauche, fait vérifier sa réponse par l'enseignant·e, à sa droite. |

### Base dix

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-B10-UNITE | Unité (cube) | 0,5 × 0,5 cm | Unité (cube) | Un cube unité ; à imprimer à la même échelle que la barre et la plaque. |
| IC-B10-BARRE | Barre de dix | 0,5 × 5 cm | Barre de dix | Dix cubes alignés. |
| IC-B10-PLAQUE | Plaque de cent | 5 × 5 cm | Plaque de cent | Cent cubes (10 × 10). |

### Horloge

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-HOR-VIERGE | Horloge sans aiguilles | 3 à 5 cm | Horloge sans aiguilles | Cadran 1-12 avec graduations des minutes ; aiguilles à dessiner par l'élève ou à ajouter par script. |

### Arcs syllabiques

| Code | Nom | Taille conseillée | Texte de remplacement | Description |
|---|---|---|---|---|
| IC-SYL-1 | 1 syllabe | 1 cm de haut | 1 arc syllabique | 1 arc syllabique : un arc par syllabe orale. |
| IC-SYL-2 | 2 syllabes | 1 cm de haut | 2 arcs syllabiques | 2 arcs syllabiques : un arc par syllabe orale. |
| IC-SYL-3 | 3 syllabes | 1 cm de haut | 3 arcs syllabiques | 3 arcs syllabiques : un arc par syllabe orale. |
| IC-SYL-4 | 4 syllabes | 1 cm de haut | 4 arcs syllabiques | 4 arcs syllabiques : un arc par syllabe orale. |
