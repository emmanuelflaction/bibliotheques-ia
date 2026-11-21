"""Modules de la Bibliothèque IA 1, tirés de la version intégrale (source unique), à joindre selon la tâche.

Lancer depuis la racine du dépôt :
    python3 outils/modules.py            écrit les modules dans bibliotheques/modules/
    python3 outils/modules.py --verifier  contrôle que les modules sont à jour et que tout le Livre I est couvert

Balisage : dans les bibliothèques Markdown, la ligne qui suit un titre peut porter
    <!-- modules : noyau, fiches -->
Le balisage vaut pour la section et ses sous-sections, jusqu'au titre suivant de même niveau ou de niveau
supérieur ; une sous-section balisée remplace le balisage de sa section. Dans la Bibliothèque IA 1, chaque ligne
appartient à au moins un module (contrôlé) ; dans la Bibliothèque IA 2, seules les sections balisées sont reprises.
Ne pas modifier les modules à la main : modifier la bibliothèque intégrale, puis relancer le script."""
import os, re, sys

MODULES = [  # (identifiant, nom affiché, nom de fichier, usage)
    ('noyau', 'Noyau', '0-noyau', 'toujours joint : posture, priorité des règles, statuts de vérification, cadre institutionnel, interdits, étapes du contrat, instruction système, liste des codes du Livre II'),
    ('fiches', 'Fiches', '1-fiches', 'fiches, documents et affiches : budget de page, gabarits G, GF et SP, recettes, règles de mise en page'),
    ('jeux', 'Jeux', '2-jeux', 'jeux imprimés : gabarits J, règles communes aux jeux, planches, contrôles des appariements, coopération'),
    ('differenciation', 'Différenciation et accessibilité', '3-differenciation', 'différenciation sur la fiche, statut de lecture, non-lecteurs, repères de différenciation et de coopération'),
    ('sequences', 'Séquences', '4-sequences', 'composer une séquence : fonctions pédagogiques, correspondance avec les huit fonctions du guide, critères de l\'écosystème, circulation et régulation'),
    ('verification', 'Vérification et livraison', '5-verification', 'contrôles sur le rendu, grille de relecture, rapport de conformité, partie enseignant·e, repli sans Word'),
    ('code', 'Code des recettes', '6-code', 'Annexe I-C : à joindre seulement à un outil qui exécute du code Python'),
]
IDS = [m[0] for m in MODULES]
B1 = 'bibliotheques/Bibliotheque-IA_1-technique_pour-IA_v1.md'
B2 = 'bibliotheques/Bibliotheque-IA_2-pedagogique_pour-IA_v1.md'
SORTIE = 'bibliotheques/modules'
BALISE = re.compile(r'^<!-- modules : ([a-z, ]+) -->$')

def sections(chemin):
    """Pour chaque ligne : (texte, niveau de titre ou 0, ensemble des modules effectifs, chaîne des titres parents)."""
    lignes = open(chemin, encoding='utf-8').read().split('\n')
    pile, code, res = [], False, []   # pile : (niveau, ligne de titre, modules)
    for i, l in enumerate(lignes):
        if l.startswith('```'): code = not code
        m = re.match(r'^(#{1,6}) ', l) if not code else None
        if m:
            n = len(m.group(1))
            while pile and pile[-1][0] >= n: pile.pop()
            b = BALISE.match(lignes[i + 1]) if i + 1 < len(lignes) else None
            mods = set(x.strip() for x in b.group(1).split(',')) if b else (pile[-1][2] if pile else set())
            assert mods <= set(IDS), (chemin, i + 1, mods)
            pile.append((n, l, mods))
            res.append((l, n, mods, [p[1] for p in pile[:-1]]))
        elif BALISE.match(l): continue
        else: res.append((l, 0, pile[-1][2] if pile else set(), [p[1] for p in pile]))
    return res

def edition():
    t = open(B1, encoding='utf-8').read()
    return re.search(r'Édition du (\d+ \w+ \d{4})', t).group(1)

def module(mid, nom, usage, b1, b2):
    ed = edition()
    tete = [f'# Bibliothèque IA 1 — module « {nom} » — v1', '',
            f'Édition du {ed}. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale' + (' et de sections de la Bibliothèque IA 2' if any(l for l in b2) else '') +
            ' par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. '
            'Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n\'est pas une publication officielle de la HEP Vaud.', '',
            f'> **Ce module** : {usage}.', '',
            '> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche '
            '(par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu\'à un outil qui exécute du code Python. '
            'Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. '
            'En cas de doute, ou si l\'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. '
            'L\'effet de ce découpage sur la fidélité des IA n\'est pas encore mesuré.', '']
    return '\n'.join(tete + b1 + (['', '# EXTRAITS DE LA BIBLIOTHÈQUE IA 2', ''] + b2 if b2 else [])).rstrip() + '\n'

def extraire(lignes, mid):
    out, emis = [], set()
    for k, (l, n, mods, parents) in enumerate(lignes):
        if mid not in mods: continue
        for p in parents:
            if p not in emis: out += ['', p, ''] if out else [p, '']; emis.add(p)
        if n: emis.add(l)
        out.append(l)
    return out

def tout():
    s1, s2 = sections(B1), sections(B2)
    sans = [(i + 1, l[:70]) for i, (l, n, mods, p) in enumerate(s1) if l.strip() and not mods]
    assert not sans, f'lignes de la Bibliothèque IA 1 sans module : {sans[:5]}'
    res = {}
    for mid, nom, fichier, usage in MODULES:
        res[f'Bibliotheque-IA_1_module-{fichier}.md'] = module(mid, nom, usage, extraire(s1, mid), extraire(s2, mid))
    return res

if __name__ == '__main__':
    res = tout()
    if '--verifier' in sys.argv:
        faux = [f for f, t in res.items() if not os.path.exists(os.path.join(SORTIE, f)) or open(os.path.join(SORTIE, f), encoding='utf-8').read() != t]
        print('Modules à jour.' if not faux else 'Modules à régénérer : ' + ', '.join(faux)); sys.exit(1 if faux else 0)
    os.makedirs(SORTIE, exist_ok=True)
    for f in os.listdir(SORTIE):
        if f.endswith('.md') and f not in res: os.remove(os.path.join(SORTIE, f))
    for f, t in res.items(): open(os.path.join(SORTIE, f), 'w', encoding='utf-8').write(t)
    for f, t in res.items(): print(f'{len(t.encode()) // 1024:4d} Ko  {f}')
