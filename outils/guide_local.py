"""Construit la version du guide pour le Drive (un seul fichier, aperçus intégrés, liens vers les dossiers du Drive)
à partir de index.html et du dossier apercus (python3 outils/guide_local.py sortie.html)."""
import base64, re, sys
h = open('index.html', encoding='utf-8').read()
typ = {'jpg': 'jpeg', 'png': 'png', 'svg': 'svg+xml'}
h = re.sub(r'apercus/([0-9a-f]{12})\.(jpg|png|svg)', lambda m: f'data:image/{typ[m.group(2)]};base64,' + base64.b64encode(open(m.group(0), 'rb').read()).decode(), h)
a = '"local": true, "web": true'; assert h.count(a) == 1
open(sys.argv[1] if len(sys.argv) > 1 else 'guide_local.html', 'w', encoding='utf-8').write(h.replace(a, '"local": true, "web": false'))
