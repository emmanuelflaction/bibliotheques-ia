"""Contrôles déterministes du dépôt (à lancer depuis la racine : python3 outils/verifier.py).
Vérifie que chaque fichier annoncé par le guide existe, que chaque aperçu référencé existe,
et que les bibliothèques portent la même édition que le guide."""
import json, os, re, sys
h = open('index.html', encoding='utf-8').read()
i = h.index('const D = ') + len('const D = '); D = json.loads(h[i:h.index('};\n', i) + 1])
dm, manque, n = D['dmap'], [], 0
def ok(d, f):
    global n; n += 1
    if not os.path.exists(os.path.join(dm.get(d, '?'), f)): manque.append(f'{d} / {f}')
for it in D['items']:
    for fo in it['fo']:
        if fo.get('f'):
            ok(fo['d'], fo['f'])
            if fo.get('w'): ok(fo['d'], fo['f'].replace('.docx', ' (couleur).docx'))
            if fo.get('e'): ok(fo['d'], fo['f'].replace('Modèle ', 'Exemple rempli ').replace('.docx', ' (couleur).docx'))
            if fo.get('c'): ok(fo['d'], fo['f'].replace('.pdf', ' (couleur).pdf'))
        if fo.get('i') and fo['i'] not in D['img']: manque.append('aperçu absent du catalogue : ' + fo['i'])
for x in D['extras']:
    for f in x['f']: ok(x['d'], f)
for f in re.findall(r"\['([^'\]]+\.(?:md|txt|docx|zip|pdf))', '", h):
    if not any(os.path.exists(os.path.join(v, f)) for v in set(dm.values())): manque.append('fichier cité par le guide : ' + f)
ap = set(re.findall(r'apercus/[0-9a-f]{12}\.(?:jpg|png|svg)', h)); manque += [a for a in ap if not os.path.exists(a)]
ed = re.search(r'Édition du (\d+)&nbsp;(\w+) (\d{4})', h); ed = ed and f'{ed.group(1)} {ed.group(2)} {ed.group(3)}'
for b in ('bibliotheques/Bibliotheque-IA_1-technique_pour-IA_v1.md', 'bibliotheques/Bibliotheque-IA_2-pedagogique_pour-IA_v1.md'):
    if f'Édition du {ed}' not in open(b, encoding='utf-8').read(): manque.append(f'édition différente du guide ({ed}) : {b}')
print(f'{n} fichiers annoncés, {len(ap)} aperçus, édition du guide : {ed}')
print('Aucun problème.' if not manque else 'Problèmes :\n- ' + '\n- '.join(manque))
sys.exit(1 if manque else 0)
