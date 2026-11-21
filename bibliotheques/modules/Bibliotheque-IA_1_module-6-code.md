# Bibliothèque IA 1 — module « Code des recettes » — v1

Édition du 21 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : Annexe I-C : à joindre seulement à un outil qui exécute du code Python.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# ANNEXE I-C — MODULE PYTHON-DOCX DES RECETTES R1 À R15 (ET CONTRÔLES V11 À V21)

Pour les IA qui produisent le fichier .docx par du code. La v7 remplace le module de la v6 par le module « recettes R1-R6 corrigées », issu du test du 30.10.2026, complété par R3, R5, R6, R7 (en-tête), R8 (planche de pièces), les styles nommés et deux outils pour les jeux.

#### Ce que corrige le module (v7)

- **Ordre XML conforme au schéma** : `geometrie` remplace l'élément `w:tblW` existant au lieu d'en ajouter un second après `w:tblLook`, et range chaque élément de `w:tblPr` dans l'ordre du schéma ; `bordures` place `w:tcBorders` avant `w:shd` et `w:vAlign`. Le module de la v6 produisait ces deux erreurs ; le validateur OOXML les signale (contrôle refait dans cette version sur un fichier témoin).
- **Correctif `w:zoom`** : le gabarit de python-docx omet l'attribut obligatoire `w:percent` ; `page_a4` l'ajoute (valeur 100).
- **Traits d'union insécables** dans « -er », « -ir », « -iss- » (élément `w:noBreakHyphen`) et **espace insécable** dans « en -ir » : `ecrire` les applique, pour que la fin de ligne ne coupe pas « en - » / « ir ».
- **Tabulations conservées** : `ecrire` transforme chaque tabulation en élément `w:tab` (une tabulation passée à `add_text` est perdue).
- **Tabulation R1b** : la position se mesure depuis la marge, pas depuis le retrait.

**Test (v7)** : un document de cinq pages couvrant R1 à R8 (en-tête, encadré, lacunes, amorce et lignes, tableau, bilan, règle du jeu en étapes, exemple de deux dominos hors lot, carte-mémoire, deux planches de 2 × 8 dominos) a été généré, converti en PDF avec LibreOffice, regardé page par page et validé au schéma OOXML sans erreur. Mesures sur le rendu : lacune de 22 tirets bas = 6,04 cm ; rangées de dominos de 2,50 cm ; planche de 16,0 cm de large et 20,7 cm de haut ; « en -ir » non coupé. Le rendu dans Word n'a pas été contrôlé ; le contrôle de l'Étape 5 reste obligatoire.

```
"""Recettes R1 à R8 du Livre I (Annexe I-C), version 7.
Base : module « recettes R1-R6 corrigées » (ordre XML conforme au schéma, traits d'union et espaces
insécables, correctif w:zoom, tabulations conservées), complété par R3, R5, R6, R7 (en-tête),
R8 (planche de pièces à découper), les styles nommés et deux outils pour les jeux."""
from docx import Document
from docx.shared import Pt, Cm
import random
from docx.enum.text import WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LARGEUR_UTILE_CM = 16.0
TW = lambda cm: str(int(round(cm / 2.54 * 1440)))

def page_a4(doc, police='Arial', taille=14, interligne=1.5):
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.5)
        s.header_distance = s.footer_distance = Cm(1.25)
    st = doc.styles['Normal']
    st.font.name = police; st.font.size = Pt(taille)
    rpr = st.element.get_or_add_rPr()
    rpr.rFonts.set(qn('w:eastAsia'), police); rpr.rFonts.set(qn('w:hAnsi'), police); rpr.rFonts.set(qn('w:cs'), police)
    lang = OxmlElement('w:lang'); lang.set(qn('w:val'), 'fr-CH'); rpr.append(lang)
    pf = st.paragraph_format
    pf.line_spacing = interligne; pf.space_after = Pt(4); pf.space_before = Pt(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    z = doc.settings.element.find(qn('w:zoom'))
    if z is not None and z.get(qn('w:percent')) is None:
        z.set(qn('w:percent'), '100')          # attribut requis par le schéma (gabarit python-docx)
    cp = doc.core_properties
    cp.author = ''; cp.last_modified_by = ''; cp.comments = ''; cp.keywords = ''

def style_para(doc, nom, taille, gras=False, italique=False, interligne=1.5, avant=0, apres=4,
               retrait=0.0, suspendu=0.0, centre=False, exact_pt=None):
    st = doc.styles.add_style(nom, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles['Normal']
    st.quick_style = True
    st.font.size = Pt(taille); st.font.bold = gras; st.font.italic = italique
    pf = st.paragraph_format
    if exact_pt:
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(exact_pt)
    else:
        pf.line_spacing = interligne
    pf.space_before = Pt(avant); pf.space_after = Pt(apres)
    pf.left_indent = Cm(retrait); pf.first_line_indent = Cm(-suspendu) if suspendu else Cm(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER if centre else WD_ALIGN_PARAGRAPH.LEFT
    pf.widow_control = True
    return st

def solidariser(p, avec_suivant=True):
    """R4 : paragraphe solidaire du suivant (dans un exercice uniquement) et lignes solidaires."""
    p.paragraph_format.keep_with_next = avec_suivant
    p.paragraph_format.keep_together = True
    return p

def saut_de_page(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
    p.add_run().add_break(WD_BREAK.PAGE)
    return p

def ecrire(p, contenu):
    """contenu = str ou liste de segments (texte, {b, i, eleve}). {'eleve': taille} : segment d'exemple en police
    d'élèves, au corps taille_eleve(taille, texte) (MP-T-10, R10)."""
    if isinstance(contenu, str):
        contenu = [(contenu, {})]
    for seg in contenu:
        if isinstance(seg, str):
            seg = (seg, {})
        txt, o = seg
        r = p.add_run()
        txt = txt.replace(' -', ' -')          # « en -ir » ne se coupe pas en fin de ligne
        for t, tabs in enumerate(txt.split('\t')):
            if t:
                r._r.append(OxmlElement('w:tab'))
            for k, m in enumerate(tabs.split('-')):
                if k:
                    r._r.append(OxmlElement('w:noBreakHyphen'))   # trait d'union insécable (« -er », « -iss- »)
                if m:
                    r.add_text(m)
        if 'b' in o: r.bold = o['b']
        if 'i' in o: r.italic = o['i']
        if o.get('eleve'):                                                  # MP-T-10 : exemple en police d'élèves
            r.font.name = POLICE_CURSIVE; r.font.size = Pt(taille_eleve(o['eleve'], txt))
            rf = r._r.get_or_add_rPr().rFonts
            for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), POLICE_CURSIVE)
    return p

# ---------- géométrie des tableaux (ordre XML conforme) ----------
_TBLPR_ORDRE = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize', 'tblStyleColBandSize',
                'tblW', 'jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout', 'tblCellMar',
                'tblLook', 'tblCaption', 'tblDescription']

def _tblpr_set(tblPr, tag, el):
    old = tblPr.find(qn('w:' + tag))
    if old is not None:
        tblPr.remove(old)
    idx = _TBLPR_ORDRE.index(tag)
    for child in list(tblPr):
        name = child.tag.split('}')[1]
        if name in _TBLPR_ORDRE and _TBLPR_ORDRE.index(name) > idx:
            child.addprevious(el)
            return
    tblPr.append(el)

def geometrie(table, largeurs_cm, retrait_cm=0.0, marge_cell_cm=0.15):
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), TW(sum(largeurs_cm))); w.set(qn('w:type'), 'dxa')
    _tblpr_set(tblPr, 'tblW', w)
    ind = OxmlElement('w:tblInd'); ind.set(qn('w:w'), TW(retrait_cm)); ind.set(qn('w:type'), 'dxa')
    _tblpr_set(tblPr, 'tblInd', ind)
    mar = OxmlElement('w:tblCellMar')
    for edge, v in (('top', 0.0), ('left', marge_cell_cm), ('bottom', 0.0), ('right', marge_cell_cm)):
        e = OxmlElement(f'w:{edge}'); e.set(qn('w:w'), TW(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
    _tblpr_set(tblPr, 'tblCellMar', mar)
    grid = table._tbl.tblGrid
    for gc in list(grid):
        grid.remove(gc)
    for x in largeurs_cm:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), TW(x)); grid.append(gc)
    for row in table.rows:
        for j, c in enumerate(row.cells):
            c.width = Cm(largeurs_cm[j])

def bordures(cell, top=None, left=None, bottom=None, right=None):
    """Chaque bord : None (aucun) ou (val, sz en 1/8 pt). val : single, dashed, dotted…"""
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn('w:tcBorders'))
    if old is not None:
        tcPr.remove(old)
    b = OxmlElement('w:tcBorders')
    for edge, spec in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{edge}')
        if spec:
            e.set(qn('w:val'), spec[0]); e.set(qn('w:sz'), str(spec[1])); e.set(qn('w:space'), '0')
            e.set(qn('w:color'), spec[2] if len(spec) > 2 else '000000')
        else:
            e.set(qn('w:val'), 'nil')
        b.append(e)
    # tcBorders se place après tcW / gridSpan / vMerge et avant shd / vAlign
    va = tcPr.find(qn('w:vAlign')); shd = tcPr.find(qn('w:shd'))
    anchor = shd if shd is not None else va
    if anchor is not None:
        anchor.addprevious(b)
    else:
        tcPr.append(b)

def trame(cell, couleur='F2F2F2'):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), couleur)
    va = tcPr.find(qn('w:vAlign'))
    if va is not None:
        va.addprevious(shd)
    else:
        tcPr.append(shd)

def ligne_tableau(row, hauteur_cm, exacte=False, entete=False):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:cantSplit'))                      # ligne insécable (R3, R4)
    row.height = Cm(hauteur_cm)
    row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY if exacte else WD_ROW_HEIGHT_RULE.AT_LEAST
    if entete:
        trPr.append(OxmlElement('w:tblHeader'))

def solidariser_tableau(table, dernier_avec_suivant=False):
    """R4 appliquée aux tableaux : chaque ligne reste avec la suivante (pas de coupure)."""
    rows = table.rows
    for i, row in enumerate(rows):
        for c in row.cells:
            for p in c.paragraphs:
                solidariser(p, avec_suivant=(i < len(rows) - 1) or dernier_avec_suivant)

# ---------- R1 : lignes d'écriture ----------
def lignes_ecriture(doc, n, hauteur_cm=1.0, largeur_cm=LARGEUR_UTILE_CM, retrait_cm=0.0):
    """R1a : tableau d'une colonne, hauteur EXACTE, bordure inférieure seule."""
    t = doc.add_table(rows=n, cols=1)
    geometrie(t, [largeur_cm], retrait_cm)
    for row in t.rows:
        ligne_tableau(row, hauteur_cm, exacte=True)
        c = row.cells[0]
        bordures(c, bottom=('single', 6, '404040'))
        c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
        c.paragraphs[0].paragraph_format.space_after = Pt(0)
    solidariser_tableau(t)
    return t

def ligne_tabulation(doc, debut, style, largeur_cm=LARGEUR_UTILE_CM, retrait_cm=0.0, hauteur_pt=28):
    """R1b : amorce + tabulation droite à points de suite « ___ » jusqu'à la marge."""
    p = doc.add_paragraph(style=style)
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(hauteur_pt)
    pf.space_after = Pt(0); pf.space_before = Pt(4)
    pf.left_indent = Cm(retrait_cm); pf.first_line_indent = Cm(0)
    pf.tab_stops.add_tab_stop(Cm(largeur_cm), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)  # mesurée depuis la marge
    p.add_run(debut + '\t')
    solidariser(p)
    return p

# ---------- R2 : lacune ----------
def lacune(longueur_cm, police='Arial', taille=14):
    largeur_tiret = {('Arial', 12): 0.235, ('Arial', 14): 0.275, ('Arial', 18): 0.353, ('Arial', 24): 0.471,
                     ('Calibri', 12): 0.211, ('Calibri', 14): 0.246, ('Calibri', 18): 0.316, ('Calibri', 24): 0.422}
    return '_' * round(longueur_cm / largeur_tiret[(police, taille)])

# ---------- styles nommés (§ 4.1, MP-S-01) ----------
def styles_fiche(doc, taille=14):
    """Crée les styles du § 4.1 pour la taille du degré (table 2.1)."""
    style_para(doc, 'Fiche-Identité', taille, avant=0, apres=0)
    style_para(doc, 'Fiche-Titre', taille + 4, gras=True, centre=True, avant=18, apres=18, interligne=1.15)
    style_para(doc, 'Fiche-Objectif', taille, apres=12)
    style_para(doc, 'Fiche-Consigne', taille, gras=True, avant=10, apres=4)
    style_para(doc, 'Fiche-Données', taille)
    style_para(doc, 'Fiche-Lacune', taille, interligne=2.0, apres=0)
    style_para(doc, 'Fiche-Exemple', taille)              # l'exemple lui-même en police d'élèves (MP-T-10)
    style_para(doc, 'Fiche-Aide', taille, interligne=1.15, apres=2)
    style_para(doc, 'Fiche-Bilan', taille, interligne=1.0, apres=0)
    style_para(doc, 'Fiche-Étape', taille, interligne=1.15, apres=4, retrait=0.8, suspendu=0.8)
    style_para(doc, 'Fiche-Pièce', taille, interligne=1.0, apres=0, centre=True)
    style_para(doc, 'Fiche-Mention', 11, italique=True, interligne=1.0, apres=6)
    style_para(doc, 'Ens-Titre', 13, gras=True, avant=10, apres=4, interligne=1.15)
    style_para(doc, 'Ens-Texte', 11, interligne=1.15)

def paragraphe(doc, contenu, style, lier=True):
    p = doc.add_paragraph(style=style)
    ecrire(p, contenu)
    return solidariser(p, lier)

def _cellule(cell, contenu, style, gras=False):
    p = cell.paragraphs[0]
    p.style = cell.part.document.styles[style]
    ecrire(p, contenu if not gras else [(contenu, {'b': True})] if isinstance(contenu, str) else contenu)
    return p

def espace(doc, pt=6):
    """R4 : paragraphe vide de hauteur exacte (6 pt) après un tableau, pour que la consigne suivante ne colle pas."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(pt)
    pf.space_before = Pt(0); pf.space_after = Pt(0)
    return p

# ---------- R3 : tableau à compléter ----------
def tableau_a_completer(doc, entetes, lignes, largeurs_cm, hauteur_min_cm=1.0, style='Fiche-Bilan'):
    """R3 : largeurs fixées, lignes ≥ 1 cm (« au moins »), insécables, en-tête répété, bordures 0,75 pt."""
    t = doc.add_table(rows=1 + len(lignes), cols=len(entetes))
    geometrie(t, largeurs_cm)
    trait = ('single', 6, '595959')
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_min_cm, exacte=False, entete=(i == 0))
        valeurs = entetes if i == 0 else lignes[i - 1]
        for j, c in enumerate(row.cells):
            bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            _cellule(c, valeurs[j], style, gras=(i == 0))
    solidariser_tableau(t)
    return t

# ---------- R5 : encadré ----------
def encadre(doc, contenus, couleur='F2F2F2', style='Fiche-Aide'):
    """R5 : tableau 1 × 1 bordé, 16 cm, ligne insécable, trame très claire (jamais de bordure de paragraphe)."""
    t = doc.add_table(rows=1, cols=1)
    geometrie(t, [LARGEUR_UTILE_CM])
    row = t.rows[0]; ligne_tableau(row, 0.8)
    c = row.cells[0]
    trait = ('single', 6, '595959')
    bordures(c, top=trait, left=trait, bottom=trait, right=trait)
    if couleur:
        trame(c, couleur)
    _cellule(c, contenus[0], style)
    for contenu in contenus[1:]:
        p = c.add_paragraph(style=style); ecrire(p, contenu)
    solidariser_tableau(t)
    return t

# ---------- R6 : bilan en mots ----------
def cases_bilan(doc, criteres, choix=('je sais faire', 'presque', "j'ai besoin d'aide"),
                largeurs_cm=(7.0, 3.0, 3.0, 3.0), style='Fiche-Bilan'):
    """R6 : choix en MOTS dans des cellules à entourer (aucun glyphe fragile), lignes ≥ 1 cm."""
    t = doc.add_table(rows=len(criteres), cols=1 + len(choix))
    geometrie(t, list(largeurs_cm))
    trait = ('single', 6, '595959')
    for i, crit in enumerate(criteres):
        row = t.rows[i]; ligne_tableau(row, 1.0)
        for j, c in enumerate(row.cells):
            bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            _cellule(c, crit if j == 0 else choix[j - 1], style)
    solidariser_tableau(t)
    return t

# ---------- R7 : en-tête de la fiche (MP-O-12) ----------
def entete(doc, titre, objectif, largeur_cm=LARGEUR_UTILE_CM, jeunes=False):
    """R7 : 1) Prénom et Date tout en haut (tabulations à points de suite, mesurées depuis la marge) ;
    2) titre centré, espace avant et après ; 3) objectif formulé pour l'élève : la phrase seule, sans étiquette
    (« J'écris un verbe au passé composé avec ses deux parties. »), majuscule initiale, point final.
    jeunes=True (1P-2P, élèves qui n'écrivent pas encore sur une ligne) : pas de ligne Prénom et Date, mais la
    mention « Prénom au dos de la feuille » (MP-O-03)."""
    p = doc.add_paragraph(style='Fiche-Identité')
    if jeunes: ecrire(p, 'Prénom au dos de la feuille')
    ts = p.paragraph_format.tab_stops
    ts.add_tab_stop(Cm(largeur_cm * 0.58), WD_TAB_ALIGNMENT.LEFT, WD_TAB_LEADER.LINES)
    ts.add_tab_stop(Cm(largeur_cm * 0.62), WD_TAB_ALIGNMENT.LEFT)
    ts.add_tab_stop(Cm(largeur_cm), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    if not jeunes: ecrire(p, 'Prénom : \t\tDate : \t')
    t = doc.add_paragraph(style='Fiche-Titre'); ecrire(t, titre)
    objectif = objectif.strip()
    for etiquette in ('Mon objectif\u00a0:', 'Mon objectif :', 'Mon objectif:', 'Objectif\u00a0:', 'Objectif :', 'Objectif:'):
        if objectif.startswith(etiquette):
            objectif = objectif[len(etiquette):].strip()
    objectif = objectif[:1].upper() + objectif[1:]
    if objectif[-1:] not in '.!?':
        objectif += '.'
    o = doc.add_paragraph(style='Fiche-Objectif'); ecrire(o, objectif)
    return p, t, o

# ---------- règle du jeu en étapes numérotées (MP-J-07) ----------
def etapes(doc, liste, style='Fiche-Étape'):
    """Une étape = une action ; numéro, tabulation, texte ; retrait suspendu de 0,8 cm."""
    ps = []
    for k, txt in enumerate(liste, 1):
        p = doc.add_paragraph(style=style)
        ecrire(p, f'{k}\t' + txt if isinstance(txt, str) else [f'{k}\t'] + list(txt))
        ps.append(solidariser(p, k < len(liste)))
    return ps

# ---------- R8 : planche de pièces à découper ----------
COUPE = ('dashed', 8, '000000')        # trait de coupe : pointillés, 1 pt
INTERNE = ('single', 18, '000000')     # séparation interne : trait plein épais, 2,25 pt

def planche_pieces(doc, pieces, par_rangee=2, largeurs_moities_cm=(4.0, 4.0), hauteur_cm=2.5,
                   mention=None, saut_avant=True, style='Fiche-Pièce'):
    """R8 : planche de pièces (dominos, cartes) à découper.
    pieces : liste de pièces ; une pièce = liste de moitiés ; une moitié = liste de lignes (str ou segments).
    Tableau à largeurs fixées, lignes à hauteur EXACTE et insécables, bordures définies cellule par cellule
    (pointillés = coupe ; trait plein épais = séparation interne), saut de page avant la planche."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention)
        m.paragraph_format.page_break_before = saut_avant
        solidariser(m)
    n_m = len(largeurs_moities_cm)
    rangees = [pieces[i:i + par_rangee] for i in range(0, len(pieces), par_rangee)]
    t = doc.add_table(rows=len(rangees), cols=par_rangee * n_m)
    geometrie(t, list(largeurs_moities_cm) * par_rangee, marge_cell_cm=0.1)
    if not mention and saut_avant:
        t.rows[0].cells[0].paragraphs[0].paragraph_format.page_break_before = True
    for r, rangee in enumerate(rangees):
        row = t.rows[r]; ligne_tableau(row, hauteur_cm, exacte=True)
        for k in range(par_rangee):
            piece = rangee[k] if k < len(rangee) else None
            for h in range(n_m):
                c = row.cells[k * n_m + h]
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                if piece is None:
                    bordures(c)
                    continue
                gauche = COUPE if h == 0 else INTERNE
                droite = COUPE if h == n_m - 1 else INTERNE
                bordures(c, top=COUPE, left=gauche, bottom=COUPE, right=droite)
                lignes = piece[h]
                p = c.paragraphs[0]; p.style = doc.styles[style]; ecrire(p, lignes[0])
                for ligne in lignes[1:]:
                    q = c.add_paragraph(style=style); ecrire(q, ligne)
    return t

# ---------- outils pour les jeux (V11, MP-J-03) ----------
def melanger_sans_voisins(pieces, graine=1, essais=10000):
    """Ordre d'impression mélangé : deux pièces voisines dans la boucle ne sont jamais voisines sur la planche."""
    rng = random.Random(graine); n = len(pieces)
    pos = {id(p): i for i, p in enumerate(pieces)}
    o = list(pieces)
    for _ in range(essais):
        rng.shuffle(o)
        if all(abs(pos[id(o[k])] - pos[id(o[k + 1])]) % n not in (1, n - 1) for k in range(n - 1)):
            return o
    raise RuntimeError('aucun ordre trouvé')

def verifier_domino_boucle(dominos, solution):
    """V11 : dominos = [(réponse, question)], dans l'ordre de la boucle ; solution(question) -> réponse.
    Vérifie : réponses toutes différentes ; chaque question a exactement une pièce-réponse ; la boucle se ferme."""
    reponses = [d[0] for d in dominos]
    assert len(set(reponses)) == len(reponses), 'deux pièces portent la même réponse'
    for rep, q in dominos:
        assert reponses.count(solution(q)) == 1, f'question sans réponse unique : {q}'
    par_rep = {d[0]: d for d in dominos}
    d = dominos[0]
    for _ in range(len(dominos)):
        d = par_rep[solution(d[1])]
    assert d == dominos[0], 'la boucle ne se ferme pas'
    return True
```

#### Extension v7.2 : recettes R9 à R14

Le module ci-dessus reste valable tel quel. La v7.2 lui ajoute, à la suite, les recettes R9 à R14. Le fichier `recettes_v7.2.py` réunit les deux blocs.

**Test (v7.2)** : 54 documents d'essai générés, convertis en PDF avec LibreOffice 7.1, regardés page par page et validés au schéma OOXML sans erreur. Le rendu dans Word n'a pas été contrôlé ; le contrôle de l'Étape 5 reste obligatoire.

```
# =====================================================================================
# Extension v7.2 — recettes R9 à R14 (Référentiel pédagogique IA 7.2)
# =====================================================================================
import math, os, itertools

# ---------- R9 : format affiche A3 et lisibilité à distance ----------
FORMATS_CM = {'A4': (21.0, 29.7), 'A3': (29.7, 42.0)}
ARIAL_CAPITALE = 0.716                 # hauteur des capitales d'Arial, en fraction du corps (métrique de la police)

def page_format(doc, fmt='A3', paysage=False, police='Arial', taille=48, interligne=1.15, marge_cm=2.5):
    """R9 : A3 ou A4, portrait ou paysage, marges de 2,5 cm (MP-F-03). Appelle page_a4 pour la base du document."""
    page_a4(doc, police=police, taille=taille, interligne=interligne)
    from docx.enum.section import WD_ORIENT
    w, h = FORMATS_CM[fmt]
    if paysage:
        w, h = h, w
    for s in doc.sections:
        s.orientation = WD_ORIENT.LANDSCAPE if paysage else WD_ORIENT.PORTRAIT
        s.page_width, s.page_height = Cm(w), Cm(h)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(marge_cm)
    return w - 2 * marge_cm, h - 2 * marge_cm      # largeur et hauteur utiles (cm)

def styles_affiche(doc, texte=48, titre=72, detail=36):
    """R9 : styles d'une affiche A3 (table du § 2.5). Valeurs par défaut pour des lecteurs de 3P à 8P."""
    style_para(doc, 'Affiche-Titre', titre, gras=True, centre=True, interligne=1.0, avant=0, apres=18)
    style_para(doc, 'Affiche-Texte', texte, interligne=1.1, apres=8)
    style_para(doc, 'Affiche-Étape', texte, interligne=1.1, apres=0)
    style_para(doc, 'Affiche-Détail', detail, interligne=1.1, apres=4)
    style_para(doc, 'Affiche-Cellule', detail, interligne=1.05, apres=0, centre=True)

def distance_lecture_m(taille_pt, facteur=1.0, capitale=ARIAL_CAPITALE):
    """Distance (m) à laquelle la capitale sous-tend 5 minutes d'arc × facteur.
    facteur=1 : seuil théorique ; facteur=2 : confort (inférence de conception)."""
    h_mm = taille_pt * 25.4 / 72 * capitale
    return h_mm / math.tan(math.radians(5 * facteur / 60)) / 1000

# ---------- R10 : écriture liée composée en GE Typo Libre (jamais dessinée ni générée) ----------
POLICE_CURSIVE = 'GE Typo Libre'
CARACTERES_ABSENTS_CURSIVE = '·ÂÄÎÏÖÙÛÜŸäÿæÆ–—%'   # sans dessin dans ge_typo_libre.otf (vérifié le 21.11.2026) : jamais en cursive

def taille_eleve(taille, texte):
    """MP-T-10 : corps de la police d'élèves pour la même hauteur apparente que le texte de la fiche (Arial) :
    1,25 fois le corps pour des lettres (hauteur des minuscules), 0,9 fois pour des chiffres seuls (les chiffres de
    GE Typo Libre sont plus hauts), 1,1 fois pour un mélange. Un même exemple garde un seul corps."""
    chiffres = all(c in '0123456789 +-=×:,./' for c in texte); lettres = not any(c.isdigit() for c in texte)
    return round(taille * (0.9 if chiffres else 1.25 if lettres else 1.1) * 2) / 2

def ecrire_exemple(p, donnee, exemple, taille, suite=''):
    """MP-T-10 : une ligne d'exemple. donnee (consigne, item, intitulé « Exemple : ») dans la police de la fiche ;
    exemple (la réponse ou l'exemple montré) en police d'élèves, sans gras ni italique ; suite éventuelle dans la
    police de la fiche. Un mot qui contient un caractère absent de la police reste en script."""
    if donnee: ecrire(p, donnee)
    mots = exemple.split(' ')
    if not set(exemple) & set(CARACTERES_ABSENTS_CURSIVE): mots = [exemple]
    for k, m in enumerate(mots):
        if k: p.add_run(' ')
        if set(m) & set(CARACTERES_ABSENTS_CURSIVE): ecrire(p, m)
        else: ecrire_cursive(p, m, taille_eleve(taille, exemple))
    if suite: ecrire(p, suite)
    return p

def police_cursive_installee():
    for d in ('~/Library/Fonts', '/Library/Fonts', '~/.fonts', '~/.local/share/fonts'):
        if os.path.exists(os.path.join(os.path.expanduser(d), 'ge_typo_libre.otf')):
            return os.path.join(os.path.expanduser(d), 'ge_typo_libre.otf')
    return None

def ecrire_cursive(p, texte, taille):
    """R10 : run en GE Typo Libre. Refuse les caractères sans dessin ; une seule casse d'origine, aucun effet."""
    assert not set(texte) & set(CARACTERES_ABSENTS_CURSIVE), 'caractère absent de la police cursive'
    r = p.add_run(texte)
    r.font.name = POLICE_CURSIVE; r.font.size = Pt(taille)
    rf = r._r.get_or_add_rPr().rFonts
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), POLICE_CURSIVE)
    return r

def verifier_cursive_pdf(chemin_pdf):
    """V15 : la police cursive est incorporée au PDF (équivalent de pdffonts)."""
    import pymupdf
    d = pymupdf.open(chemin_pdf)
    noms = {f[3] for page in d for f in page.get_fonts()}
    return any('GETypoLibre' in n for n in noms), sorted(noms)

# ---------- R11 : dessin vectoriel (SVG et PDF à l'échelle 1, unités en mm) ----------
POLICES_PDF = {'Arial': '/System/Library/Fonts/Supplemental/Arial.ttf',
               'Arial-B': '/System/Library/Fonts/Supplemental/Arial Bold.ttf'}
if police_cursive_installee(): POLICES_PDF['Eleve'] = police_cursive_installee()   # MP-T-10 : police d'élèves

def police_exemple_pdf():
    """MP-T-10 : police de Dessin pour un exemple : 'Eleve' (GE Typo Libre) si elle est installée ; sinon 'Arial',
    repli à signaler (MP-T-08)."""
    return 'Eleve' if 'Eleve' in POLICES_PDF else 'Arial'

# Couleur facultative (21.11.2026). Par défaut : noir et blanc. La couleur ne porte jamais seule une information
# (MP-C-02) : un gris devient une teinte de même clarté, de sorte qu'une photocopie en noir et blanc reste identique.
TEINTES = {'bleu': (0.00, 0.45, 0.70), 'orange': (0.90, 0.62, 0.00), 'vert': (0.00, 0.62, 0.45),
           'violet': (0.80, 0.47, 0.65), 'ciel': (0.34, 0.71, 0.91), 'vermillon': (0.84, 0.37, 0.00)}
TEINTES_CATEGORIES = ('bleu', 'orange', 'vert', 'violet', 'ciel', 'vermillon')   # une teinte par symbole de catégorie
COULEUR = [None]

def definir_couleur(nom=None):
    """nom=None : noir et blanc (défaut). Sinon une clé de TEINTES : tous les dessins créés ensuite sont teintés
    (fonds gris, symboles de catégorie, dos des cartes). À remettre à None après la production."""
    assert nom is None or nom in TEINTES, 'teinte inconnue : ' + str(nom)
    COULEUR[0] = nom

JEUNES = [False]

def definir_jeunes(oui=True):
    """oui=True : fiches dessinées pour des élèves qui n'écrivent pas encore sur une ligne (1P-2P surtout) : la ligne
    « Prénom » devient la mention « Prénom au dos de la feuille » et aucune ligne de date n'est tracée (MP-O-03).
    À remettre à False après la production."""
    JEUNES[0] = bool(oui)

def _prenom():
    return 'Prénom au dos de la feuille' if JEUNES[0] else 'Prénom : ____________________'

def _teinter(fond):
    """Un gris devient une teinte de même clarté ; le blanc, le noir et les couleurs données restent inchangés."""
    if fond is None or COULEUR[0] is None or not (fond[0] == fond[1] == fond[2]) or fond[0] in (0, 1): return fond
    t = TEINTES[COULEUR[0]]; v = fond[0]; lum = 0.3 * t[0] + 0.59 * t[1] + 0.11 * t[2]
    if v >= lum: a = (1 - v) / (1 - lum); return tuple(1 - a * (1 - c) for c in t)
    return tuple(v / lum * c for c in t)

def couleur_trait():
    """Couleur des traits d'un dos de carte : la teinte choisie, assombrie ; noir sans couleur."""
    return (0, 0, 0) if COULEUR[0] is None else tuple(0.75 * c for c in TEINTES[COULEUR[0]])

class Dessin:
    """R11 : tracés, roues, patrons. Mêmes primitives vers SVG (fichier source) et vers PDF (échelle 1).
    Coordonnées en mm depuis le coin supérieur gauche."""
    def __init__(self, l=210, h=297):
        import pymupdf
        self.f = pymupdf; self.l, self.h = l, h
        self.d = pymupdf.open(); self.p = self.d.new_page(width=l * 72 / 25.4, height=h * 72 / 25.4)
        self.s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{l}mm" height="{h}mm" viewBox="0 0 {l} {h}">']
        self.k = 72 / 25.4; self.trait = (0, 0, 0)

    def _hex(self, c):
        return '#' + ''.join(f'{int(v*255):02x}' for v in c)

    def _P(self, x, y):
        return self.f.Point(x * self.k, y * self.k)

    def ligne(self, pts, ep=0.5, tirets=None, ferme=False, fond=None):
        sh = self.p.new_shape(); q = [self._P(*a) for a in pts]; fond = _teinter(fond)
        sh.draw_polyline(q + ([q[0]] if ferme else []))
        sh.finish(width=ep * self.k, color=self.trait, fill=fond, closePath=ferme,
                  dashes=None if not tirets else f'[{tirets[0]*self.k:.2f} {tirets[1]*self.k:.2f}] 0', lineCap=1, lineJoin=1)
        sh.commit()
        d = ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)
        a = f' stroke-dasharray="{tirets[0]} {tirets[1]}"' if tirets else ''
        f = '#' + ''.join(f'{int(c*255):02x}' for c in fond) if fond else 'none'
        self.s.append(f'<{"polygon" if ferme else "polyline"} points="{d}" fill="{f}" stroke="{self._hex(self.trait)}" stroke-width="{ep}"{a}/>')

    def cercle(self, cx, cy, r, ep=0.5, tirets=None, fond=None):
        sh = self.p.new_shape(); sh.draw_circle(self._P(cx, cy), r * self.k); fond = _teinter(fond)
        sh.finish(width=ep * self.k, color=self.trait if ep else None, fill=fond,
                  dashes=None if not tirets else f'[{tirets[0]*self.k:.2f} {tirets[1]*self.k:.2f}] 0')
        sh.commit()
        a = f' stroke-dasharray="{tirets[0]} {tirets[1]}"' if tirets else ''
        f = '#' + ''.join(f'{int(c*255):02x}' for c in fond) if fond else 'none'
        self.s.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{f}" stroke="{self._hex(self.trait)}" stroke-width="{ep}"{a}/>')

    def largeur_texte(self, txt, taille_pt, police='Arial'):
        return self.f.Font(fontfile=POLICES_PDF[police]).text_length(txt, fontsize=taille_pt) / self.k

    def texte(self, x, y, txt, taille_pt=14, ancre='m', police='Arial', rot=0):
        """(x, y) = centre de la ligne de base si ancre='m', début si ancre='s'. rot : degrés, sens horaire."""
        l = self.largeur_texte(txt, taille_pt, police)
        dx = -l / 2 if ancre == 'm' else 0
        a = math.radians(rot)
        px, py = x + dx * math.cos(a), y + dx * math.sin(a)
        Q = self._P(px, py)
        self.p.insert_text(Q, txt, fontsize=taille_pt, fontname=police.replace('-', ''), fontfile=POLICES_PDF[police],
                           morph=(Q, self.f.Matrix(-rot)))
        g = ' font-weight="bold"' if police.endswith('-B') else ''
        t = txt.replace('&', '&amp;').replace('<', '&lt;')
        self.s.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="Arial" font-size="{taille_pt*25.4/72:.2f}" '
                      f'text-anchor="{"middle" if ancre=="m" else "start"}"{g} transform="rotate({rot} {x:.2f} {y:.2f})">{t}</text>')

    def sauver(self, base):
        """Écrit base.svg (source vectorielle) et base.pdf (vectoriel, échelle 1)."""
        open(base + '.svg', 'w', encoding='utf-8').write('\n'.join(self.s) + '\n</svg>\n')
        self.d.save(base + '.pdf')
        return base + '.pdf'

    def png(self, base, dpi=300):
        self.p.get_pixmap(dpi=dpi).save(base + '.png')
        return base + '.png'

def arc_pts(cx, cy, r, a0, a1, n=40):
    """Points d'un arc ; angles en degrés depuis midi, sens horaire."""
    return [(cx + r * math.sin(math.radians(a0 + (a1 - a0) * i / n)),
             cy - r * math.cos(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def couloir(dessin, pts, largeur):
    """R11 : chemin à bords parallèles autour de la ligne médiane pts (G19)."""
    g, d = [], []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[max(i - 1, 0)]; x1, y1 = pts[min(i + 1, len(pts) - 1)]
        n = math.hypot(x1 - x0, y1 - y0) or 1
        nx, ny = -(y1 - y0) / n, (x1 - x0) / n
        g.append((x + nx * largeur / 2, y + ny * largeur / 2)); d.append((x - nx * largeur / 2, y - ny * largeur / 2))
    dessin.ligne(g, ep=0.7); dessin.ligne(d, ep=0.7)

def arrondir(pts, n=4):
    """R11 : arrondit une ligne brisée (coupe des coins) pour que le couloir garde sa largeur dans les virages."""
    for _ in range(n):
        q = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            q += [(a[0] * .75 + b[0] * .25, a[1] * .75 + b[1] * .25), (a[0] * .25 + b[0] * .75, a[1] * .25 + b[1] * .75)]
        pts = q + [pts[-1]]
    return pts

def couloir_valide(pts, largeur, marge=2.0, saut=12):
    """V16 : deux portions non voisines du couloir restent séparées d'au moins largeur + marge (mm)."""
    m = min(math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
            for i in range(len(pts)) for j in range(i + saut, len(pts)))
    return m >= largeur + marge, m

def labyrinthe(lignes, colonnes, graine=1):
    """Labyrinthe parfait : exactement un chemin entre deux cases (arbre couvrant, parcours en profondeur)."""
    rng = random.Random(graine)
    murs = {(l, c): {'N', 'S', 'E', 'O'} for l in range(lignes) for c in range(colonnes)}
    vu = {(0, 0)}; pile = [(0, 0)]
    D = {'N': (-1, 0, 'S'), 'S': (1, 0, 'N'), 'E': (0, 1, 'O'), 'O': (0, -1, 'E')}
    while pile:
        l, c = pile[-1]
        v = [(k, l + a, c + b, o) for k, (a, b, o) in D.items() if (l + a, c + b) in murs and (l + a, c + b) not in vu]
        if not v:
            pile.pop(); continue
        k, a, b, o = rng.choice(v)
        murs[(l, c)].discard(k); murs[(a, b)].discard(o); vu.add((a, b)); pile.append((a, b))
    return murs

def labyrinthe_unique(murs, lignes, colonnes):
    """V16 : case d'arrivée atteinte et nombre de passages = cases − 1 (arbre, donc chemin unique)."""
    passages = sum(len({'N', 'S', 'E', 'O'} - m) for m in murs.values()) // 2
    return passages == lignes * colonnes - 1

def tracer_labyrinthe(dessin, murs, lignes, colonnes, x0, y0, case):
    for (l, c), m in murs.items():
        x, y = x0 + c * case, y0 + l * case
        if 'N' in m and not (l == 0 and c == 0): dessin.ligne([(x, y), (x + case, y)], ep=0.7)
        if 'O' in m and not (l == 0 and c == 0): dessin.ligne([(x, y), (x, y + case)], ep=0.7)
        if l == lignes - 1 and 'S' in m and not c == colonnes - 1: dessin.ligne([(x, y + case), (x + case, y + case)], ep=0.7)
        if c == colonnes - 1 and 'E' in m and not l == lignes - 1: dessin.ligne([(x + case, y), (x + case, y + case)], ep=0.7)

def roue_J11(paires, base, degre_pt=14):
    """R11 : J11, deux disques de 11 cm. paires : [(question, réponse)] ; 6 secteurs.
    Disque inférieur (contenu) et disque supérieur (fenêtre, rabat). Renvoie le Dessin et le rapport V18."""
    n = len(paires); pas = 360 / n
    R, RM, RI = 55, 38, 16
    D = Dessin(160, 240); cx, y1, y2 = 56, 63, 184
    D.texte(0, 5, 'Disque du dessous : découpe sur les pointillés.', 12, ancre='s', police='Arial-B')
    D.cercle(cx, y1, R, ep=0.5, tirets=(3, 2)); D.cercle(cx, y1, RM, ep=0.25); D.cercle(cx, y1, 1.2, ep=0, fond=(0, 0, 0))
    D.cercle(cx, y1, RI, ep=0.25)
    for k, (q, r) in enumerate(paires):
        a = k * pas
        a2 = a + pas / 2
        D.ligne([(cx + RI * math.sin(math.radians(a2)), y1 - RI * math.cos(math.radians(a2))),
                 (cx + R * math.sin(math.radians(a2)), y1 - R * math.cos(math.radians(a2)))], ep=0.25)
        for t, rr in ((q, 45), (r, 28)):
            D.texte(cx + rr * math.sin(math.radians(a)), y1 - rr * math.cos(math.radians(a)), t, degre_pt, rot=a,
                    police='Arial-B' if rr == 28 else 'Arial')
    D.texte(0, 124, 'Disque du dessus : découpe la fenêtre et le rabat. Plie sur le trait fin.', 12, ancre='s', police='Arial-B')
    D.cercle(cx, y2, R, ep=0.5, tirets=(3, 2)); D.cercle(cx, y2, 1.2, ep=0, fond=(0, 0, 0))
    A = pas / 2 - 3
    fen = arc_pts(cx, y2, 52, -A, A) + arc_pts(cx, y2, 39, A, -A)
    D.ligne(fen, ep=0.5, tirets=(3, 2), ferme=True)
    D.ligne(arc_pts(cx, y2, 36, -A, A) + arc_pts(cx, y2, 18, A, A, 1)[1:], ep=0.5, tirets=(3, 2))
    D.ligne(arc_pts(cx, y2, 36, -A, -A, 1) + arc_pts(cx, y2, 18, -A, -A, 1)[1:], ep=0.5, tirets=(3, 2))
    D.ligne(arc_pts(cx, y2, 18, -A, A), ep=0.25, tirets=(1, 1))
    D.texte(cx, y2 + 16, 'Tourne.', 14); D.texte(cx, y2 + 24, 'Réponds.', 14); D.texte(cx, y2 + 32, 'Soulève le rabat.', 14)
    D.texte(118, 59, 'Attache parisienne', 11, ancre='s'); D.texte(118, 64, 'au centre des', 11, ancre='s'); D.texte(118, 69, 'deux disques.', 11, ancre='s')
    # V18 : chaque texte, centré dans la fenêtre ou sous le rabat, y tient entièrement
    rep = []
    for q, r in paires:
        lq, lr = D.largeur_texte(q, degre_pt), D.largeur_texte(r, degre_pt, 'Arial-B')
        cq = 2 * 45 * math.sin(math.radians(A)) ; cr = 2 * 28 * math.sin(math.radians(A))
        rep.append((q, r, round(lq, 1), round(cq, 1), round(lr, 1), round(cr, 1), lq < cq - 2 and lr < cr - 2))
    D.sauver(base); D.png(base)
    return D, rep

def inserer_image(doc_ou_cell, chemin, largeur_cm, centre=True):
    """Image de largeur exacte. Le dessin source reste le fichier SVG ou PDF."""
    p = doc_ou_cell.add_paragraph() if not hasattr(doc_ou_cell, 'add_run') else doc_ou_cell
    p.add_run().add_picture(chemin, width=Cm(largeur_cm))
    if centre:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
    return p

def icone(code, dossier, sortie, dpi=300):
    """Icône de la banque IC (SVG) convertie en PNG pour le .docx."""
    import pymupdf
    os.makedirs(sortie, exist_ok=True)
    png = os.path.join(sortie, code + '.png')
    if not os.path.exists(png):
        d = pymupdf.open(os.path.join(dossier, code + '.svg'))
        pymupdf.open('pdf', d.convert_to_pdf())[0].get_pixmap(dpi=dpi, alpha=False).save(png)
    return png

# ---------- R12 : planche recto-verso ----------
def verso_de(rangees):
    """R12 : inverse les colonnes pour une impression recto-verso sur le bord long (J4, J10, J14, G15)."""
    return [list(reversed(r)) for r in rangees]

def en_rangees(pieces, par_rangee):
    r = [pieces[i:i + par_rangee] for i in range(0, len(pieces), par_rangee)]
    while len(r[-1]) < par_rangee:
        r[-1].append(None)
    return r

# ---------- R13 : contrôles combinatoires (V11 élargi, V19) ----------
def generer_loto(elements, n_cartons, par_carton, graine=1, essais=200000):
    """J7 : chaque élément figure sur le même nombre de cartons ; cartons tous différents, aucun doublon dans un carton."""
    f = n_cartons * par_carton / len(elements)
    assert f == int(f), 'le produit cartons × cases doit être un multiple du nombre d\'éléments'
    rng = random.Random(graine); f = int(f)
    for _ in range(essais):
        reste = {e: f for e in elements}; cartons = []
        try:
            for _c in range(n_cartons):
                pris = []
                for _k in range(par_carton):
                    m = max(v for e, v in reste.items() if e not in pris)
                    choix = [e for e, v in reste.items() if v >= max(m - 1, 1) and e not in pris]
                    e = rng.choice(choix); pris.append(e); reste[e] -= 1
                cartons.append(pris)
        except (ValueError, IndexError):
            continue
        if not verifier_loto(cartons, elements, f, silence=True):
            continue
        return cartons
    raise RuntimeError('aucune répartition trouvée')

def verifier_loto(cartons, elements, frequence, silence=False):
    """V19 : fréquence exacte de chaque élément ; pas de doublon dans un carton ; cartons tous différents."""
    try:
        for e in elements:
            assert sum(c.count(e) for c in cartons) == frequence, f'fréquence de {e}'
        assert all(len(set(c)) == len(c) for c in cartons), 'doublon dans un carton'
        assert len({frozenset(c) for c in cartons}) == len(cartons), 'deux cartons identiques'
    except AssertionError:
        if silence:
            return False
        raise
    return True

def plan_projectif(n):
    """J8 : n premier, ou n = 4 ; n² + n + 1 cartes de n + 1 symboles ; deux cartes quelconques partagent exactement un symbole."""
    M = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]          # produit dans le corps à quatre éléments
    f = (lambda a, x, b: M[a][x] ^ b) if n == 4 else (lambda a, x, b: (a * x + b) % n)
    cartes = []
    for a in range(n):
        for b in range(n):
            cartes.append([x * n + f(a, x, b) for x in range(n)] + [n * n + a])
    for x in range(n):
        cartes.append([x * n + y for y in range(n)] + [n * n + n])
    cartes.append([n * n + i for i in range(n + 1)])
    return cartes

def verifier_symboles(cartes):
    """V19 : chaque paire de cartes a exactement un symbole commun."""
    for a, b in itertools.combinations(cartes, 2):
        assert len(set(a) & set(b)) == 1, (a, b)
    return True

def verifier_appariement(paires):
    """V11 : chaque question a une seule réponse, chaque réponse une seule question (mémoire, carte à pince, loto)."""
    q = [p[0] for p in paires]; r = [p[1] for p in paires]
    assert len(set(q)) == len(q) and len(set(r)) == len(r), 'appariement ambigu'
    return True

def verifier_code(enigmes, code):
    """V11 et V21 (escape game) : chaque énigme porte son calcul ('calcul', expression arithmétique)
    et le chiffre annoncé ('chiffre') ; le calcul DOIT donner un nombre entier de 0 à 9 égal au chiffre annoncé,
    et la suite des chiffres donne le code final. Une énigme dont la réponse a deux chiffres est refusée."""
    for i, e in enumerate(enigmes, 1):
        assert 'calcul' in e, f'énigme {i} : calcul absent, le chiffre ne peut pas être vérifié'
        assert set(e['calcul']) <= set('0123456789+-*/%() '), f'énigme {i} : calcul non arithmétique'
        r = eval(e['calcul'], {'__builtins__': {}})
        assert r == int(r) and 0 <= int(r) <= 9, f"énigme {i} : la réponse {r} n'est pas un chiffre de 0 à 9"
        assert int(r) == int(e['chiffre']), f'énigme {i} : chiffre annoncé {e["chiffre"]}, calcul {int(r)}'
    assert ''.join(str(e['chiffre']) for e in enigmes) == code, 'code incohérent'
    return True

def verifier_graphemes(paires):
    """V21 : chaque mot proposé contient bien le graphème étudié (son et graphème, cartes de sons, mots à trier).
    paires : [(graphème, mot)]. La comparaison ignore la casse ; accents conservés (é ≠ e)."""
    fautes = [(g, m) for g, m in paires if g.lower() not in m.lower()]
    assert not fautes, f'graphème absent du mot : {fautes}'
    return True

# ---------- R14 : grille à zones et planche à zones ----------
TRAIT = ('single', 6, '595959')
TRAIT_FORT = ('single', 12, '000000')

def _remplir(cell, contenu, style, doc):
    """contenu : None ; str ; liste de lignes (str ou segments) ; {'img': chemin ou liste, 'cm': largeur} ; {'cursive': texte, 'pt': taille}."""
    p = cell.paragraphs[0]; p.style = doc.styles[style]
    p.paragraph_format.keep_with_next = True
    if contenu is None:
        return
    lignes = contenu if isinstance(contenu, list) else [contenu]
    for i, l in enumerate(lignes):
        if i:
            p = cell.add_paragraph(style=style)
        if l is None:
            continue
        if isinstance(l, tuple):
            l = [l]
        if isinstance(l, dict) and 'img' in l:
            for im in (l['img'] if isinstance(l['img'], list) else [l['img']]):
                p.add_run().add_picture(im, width=Cm(l['cm']))
        elif isinstance(l, dict) and 'cursive' in l:
            ecrire_cursive(p, l['cursive'], l['pt'])
        else:
            ecrire(p, l)

def grille(doc, lignes, largeurs_cm, hauteurs_cm=1.0, exacte=False, style='Fiche-Bilan', trait=TRAIT,
           entete=False, vertical=WD_ALIGN_VERTICAL.CENTER, marge_cell_cm=0.15):
    """R14 : tableau à largeurs fixées dont chaque cellule reçoit texte, image ou cursive."""
    t = doc.add_table(rows=len(lignes), cols=len(largeurs_cm))
    geometrie(t, list(largeurs_cm), marge_cell_cm=marge_cell_cm)
    hs = hauteurs_cm if isinstance(hauteurs_cm, (list, tuple)) else [hauteurs_cm] * len(lignes)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hs[i], exacte=exacte, entete=(entete and i == 0))
        for j, c in enumerate(row.cells):
            if trait:
                bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            else:
                bordures(c)
            c.vertical_alignment = vertical
            contenu = lignes[i][j]
            if entete and i == 0 and isinstance(contenu, str):
                contenu = [[(contenu, {'b': True})]]
            _remplir(c, contenu, style, doc)
    solidariser_tableau(t)
    return t

def planche_zones(doc, rangees, largeur_cm, hauteurs_cm, sous_colonnes=1, mention=None, saut_avant=True,
                  style='Fiche-Pièce', zones_verticales=None):
    """R14 / R8 : planche de pièces découpées en zones superposées.
    rangees : liste de rangées ; pièce = liste de zones (une par hauteur) ou None ;
    zone = contenu unique ou tuple de contenus côte à côte (sous-cellules de largeur égale)."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention)
        m.paragraph_format.page_break_before = saut_avant
        solidariser(m)
    nz = len(hauteurs_cm); npc = len(rangees[0])
    t = doc.add_table(rows=nz * len(rangees), cols=npc * sous_colonnes)
    geometrie(t, [largeur_cm / sous_colonnes] * (npc * sous_colonnes), marge_cell_cm=0.1)
    fin = ('single', 4, '595959')
    for r, rangee in enumerate(rangees):
        for z in range(nz):
            row = t.rows[r * nz + z]; ligne_tableau(row, hauteurs_cm[z], exacte=True)
        for k, piece in enumerate(rangee):
            for z in range(nz):
                zone = None if piece is None else piece[z]
                cells = zone if isinstance(zone, tuple) else (zone,)
                span = sous_colonnes // len(cells)
                for s, contenu in enumerate(cells):
                    c0 = k * sous_colonnes + s * span
                    c = t.cell(r * nz + z, c0)
                    if span > 1:
                        c = c.merge(t.cell(r * nz + z, c0 + span - 1))
                    c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    if piece is None:
                        bordures(c); _remplir(c, None, style, doc); continue
                    bordures(c, top=COUPE if z == 0 else fin, bottom=COUPE if z == nz - 1 else fin,
                             left=COUPE if s == 0 else fin, right=COUPE if s == len(cells) - 1 else fin)
                    _remplir(c, contenu, style, doc)
    return t
```

#### Révision du 2 novembre 2026 : R7, `verifier_code`, `verifier_graphemes`, R15 et V20

Trois changements dans les blocs ci-dessus : R7 écrit l'objectif sans étiquette (une étiquette fournie par erreur est retirée) ; `verifier_code` exige le calcul de chaque énigme et refuse une réponse qui n'est pas un chiffre de 0 à 9 ; `verifier_graphemes` (V21) est ajoutée. Le bloc suivant ajoute R15 (planche A5) et V20 (page pleine) ; il se place à la fin du module. Le fichier `recettes_v7.2.py` (révision du 2 novembre 2026) réunit les trois blocs.

**Test (révision du 2.11.2026)** : 54 documents d'essai corrigés, convertis en PDF avec LibreOffice, mesurés page par page (remplissage de 90 % au moins sur toutes les pages élèves, mesuré sur l'image de la page) et validés au schéma OOXML ; R7, R15, `verifier_code`, `verifier_graphemes` et `verifier_remplissage` testés sur un document d'essai (cas conformes et cas fautifs refusés). Le rendu dans Word n'a pas été contrôlé.

```
# =====================================================================================
# Révision du 2 novembre 2026 — R15 (planche A5) et V20 (page pleine, MP-O-14)
# =====================================================================================
from docx.enum.section import WD_SECTION, WD_ORIENT

COUPE_A5 = ('dashed', 8, '000000')     # trait de coupe entre les deux exemplaires A5

# ---------- R15 : planche A5, deux exemplaires sur une feuille A4 (MP-O-14) ----------
def planche_A5(doc, remplir, disposition='cote_a_cote', marge_cm=1.0, retrait_cm=0.9, nouvelle_section=True):
    """R15 : une feuille A4 porte deux exemplaires A5 identiques séparés par un trait de coupe en tirets.
    'cote_a_cote' : A4 paysage, deux colonnes A5 portrait, largeur de contenu 12,05 cm (règle de jeu, petite fiche) ;
    'empile' : A4 portrait, deux rangées A5 paysage, largeur de contenu 17,2 cm (bande, ticket de sortie).
    remplir(cellule, largeur_cm) écrit UN exemplaire dans la cellule (cellule.add_paragraph, cellule.add_table) ;
    elle est appelée deux fois, pour que les deux moitiés soient identiques.
    La planche ouvre une section propre ; la suite du document reprend sa mise en page avec nouvelle_section_a4()."""
    s = doc.add_section(WD_SECTION.NEW_PAGE) if nouvelle_section else doc.sections[-1]
    if disposition == 'cote_a_cote':
        s.orientation = WD_ORIENT.LANDSCAPE; s.page_width, s.page_height = Cm(29.7), Cm(21.0)
    else:
        s.orientation = WD_ORIENT.PORTRAIT; s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    for m in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
        setattr(s, m, Cm(marge_cm))
    pw, ph = s.page_width.cm, s.page_height.cm
    if disposition == 'cote_a_cote':
        cw, chh = (pw - 2 * marge_cm) / 2, ph - 2 * marge_cm
        t = doc.add_table(rows=1, cols=2); cells = [t.cell(0, 0), t.cell(0, 1)]
    else:
        cw, chh = pw - 2 * marge_cm, (ph - 2 * marge_cm) / 2
        t = doc.add_table(rows=2, cols=1); cells = [t.cell(0, 0), t.cell(1, 0)]
    geometrie(t, [cw] * len(t.columns), marge_cell_cm=0.0)
    for row in t.rows:
        ligne_tableau(row, chh - 0.1)
    if disposition == 'cote_a_cote':
        bordures(cells[0], right=COUPE_A5); bordures(cells[1], left=COUPE_A5)
    else:
        bordures(cells[0], bottom=COUPE_A5); bordures(cells[1])
    for c in cells:
        tcPr = c._tc.get_or_add_tcPr()
        mar = OxmlElement('w:tcMar')
        for edge, v in (('top', 0.6), ('left', retrait_cm), ('bottom', 0.0), ('right', retrait_cm)):
            e = OxmlElement(f'w:{edge}'); e.set(qn('w:w'), TW(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
        b = tcPr.find(qn('w:tcBorders'))
        if b is not None:
            b.addnext(mar)
        else:
            tcPr.append(mar)
        c.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        remplir(c, cw - 2 * retrait_cm)
    return t

def nouvelle_section_a4(doc, paysage=False, marge_cm=2.5):
    """Après une planche A5 placée en milieu de document : reprend l'A4 avec les marges du Livre I (MP-F-03)."""
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE if paysage else WD_ORIENT.PORTRAIT
    s.page_width, s.page_height = (Cm(29.7), Cm(21.0)) if paysage else (Cm(21.0), Cm(29.7))
    for m in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
        setattr(s, m, Cm(marge_cm))
    return s

# ---------- V20 : remplissage des pages sur le rendu (MP-O-14) ----------
_PT_CM = 72 / 2.54

def budget_page(largeur_cm, hauteur_cm):
    """Marge haute et budget de hauteur (§ 2.2 et § 2.5) selon le format de la page."""
    if abs(largeur_cm - 21) < .5 and abs(hauteur_cm - 29.7) < .5:
        return 2.5, 22.0                        # A4 portrait
    if abs(largeur_cm - 29.7) < .5 and abs(hauteur_cm - 21) < .5:
        return 2.5, 16 * 22 / 24.7              # A4 paysage
    if abs(largeur_cm - 29.7) < .5 and abs(hauteur_cm - 42) < .5:
        return 2.5, 33.0                        # A3 portrait
    if abs(largeur_cm - 42) < .5 and abs(hauteur_cm - 29.7) < .5:
        return 2.5, 22.0                        # A3 paysage
    return 2.5, (hauteur_cm - 5) * 22 / 24.7

def remplissage_pages(chemin_pdf, planches_A5=None, dpi=50, gris=200):
    """Mesure, page par page, la position du dernier élément VISIBLE (encre sur l'image rendue de la page),
    rapportée au budget de hauteur. Un cadre blanc, une bordure absente ou la marge blanche d'une image ne
    comptent pas. planches_A5 : {numéro de page: 'cote_a_cote' ou 'empile'} ; pour ces pages, la mesure porte
    sur un exemplaire A5 (marge haute 1,6 cm), le trait de coupe étant ignoré. Requiert PyMuPDF et NumPy."""
    import pymupdf, numpy as np
    planches_A5 = planches_A5 or {}
    res = []
    with pymupdf.open(chemin_pdf) as doc:
        for i, pg in enumerate(doc, 1):
            pix = pg.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY, alpha=False)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.stride)[:, :pix.width]
            px = dpi / 2.54                                  # pixels par centimètre
            encre = img < gris
            disp = planches_A5.get(i)
            if disp == 'cote_a_cote':                        # trait de coupe vertical au milieu
                m = pix.width // 2; d = int(0.3 * px) + 1
                encre[:, m - d:m + d] = False
            if disp == 'empile':                             # exemplaire du haut seulement
                encre = encre[:pix.height // 2 - int(0.3 * px)]
            lignes = np.where(encre.any(axis=1))[0]
            bas = float(lignes[-1] + 1) / px if len(lignes) else 0.0
            if disp == 'empile':
                haut, bud = 1.6, (29.7 - 2) / 2 * 22 / 24.7
            elif disp == 'cote_a_cote':
                haut, bud = 1.6, (21 - 2) * 22 / 24.7
            else:
                haut, bud = budget_page(pix.width / px, pix.height / px)
            bas = float(bas)
            res.append({'page': i, 'bas_cm': round(bas, 1), 'remplissage': round((bas - haut) / bud, 2)})
    return res

def verifier_remplissage(chemin_pdf, seuil=0.90, plafond=1.10, pages_exclues=(), planches_A5=None):
    """V20 (MP-O-14) : aucune page élève remplie partiellement. Chaque page, hors pages exclues (partie
    enseignant·e, dernière planche d'un jeu de pièces déclarée dans la fiche technique), atteint au moins 90 %
    du budget de hauteur (A4 portrait : 19,8 cm sous la marge haute, soit au plus 4,9 cm de blanc en bas) et ne le dépasse pas de plus de 10 % (débordement probable). Renvoie les mesures."""
    mesures = remplissage_pages(chemin_pdf, planches_A5)
    fautes = [m for m in mesures if m['page'] not in pages_exclues and not (seuil <= m['remplissage'] <= plafond)]
    assert not fautes, ('pages hors limites (aérer, ajouter des lignes ou des exercices, ou passer en planche A5) : '
                        + ', '.join(f"p{m['page']} {int(m['remplissage'] * 100)} %" for m in fautes))
    return mesures
```

#### Révision du 2 novembre 2026, suite : `verifier_case_piece` (MP-J-10), `verifier_mots_coupes` et `carte_a_pinces` (J10)

Trois ajouts à la fin du module : `verifier_case_piece` refuse une case d'accueil qui ne dépasse pas la pièce mobile de 0,5 cm par côté (G12-b, plateaux, tableaux à étiquettes) ; `verifier_mots_coupes` compare les mots du .docx aux mots du PDF rendu et signale tout mot coupé par une cellule trop étroite (J9, SP8 ; R14, R15) ; `carte_a_pinces` construit la carte J10 (une page, un bloc de trois lignes par question, réponses empilées au bord, verso avec « bravo »). Le fichier `recettes_v7.2.py` réunit les quatre blocs.

**Test (révision du 2.11.2026, suite)** : `verifier_case_piece` accepte (6 × 2,5 ; 8 × 3,5) et refuse (6 × 2,5 ; 6,8 × 3,5) et l'ancienne étiquette de G12-b (5,33 × 4,2 ; 8 × 3,2) ; `verifier_mots_coupes` signale un mot long placé dans une cellule de 1,5 cm sur un document d'essai rendu par LibreOffice ; `carte_a_pinces` testée sur J10 (recto 103 %, verso 98 %, « bravo » une fois par bloc) (statut : vérifié).

```
# ---------- Révision du 2 novembre 2026, suite : MP-J-10 (pièces mobiles) et mots coupés ----------
MARGE_PIECE_CM = 0.5

def verifier_case_piece(piece_cm, case_cm, marge_cm=MARGE_PIECE_CM, nom='case'):
    """MP-J-10 (V12) : une case destinée à recevoir une pièce mobile (étiquette, carte, jeton, pince)
    dépasse la pièce d'au moins 0,5 cm par côté, en largeur et en hauteur.
    piece_cm, case_cm : (largeur, hauteur) en cm. Refuse (AssertionError) toute case trop petite ;
    renvoie le jeu (dépassement par côté) en cm. À appeler avant grille() pour tout plateau à étiquettes."""
    (lp, hp), (lc, hc) = piece_cm, case_cm
    jeu_l, jeu_h = (lc - lp) / 2, (hc - hp) / 2
    fautes = []
    if jeu_l < marge_cm - 1e-9:
        fautes.append(f'largeur : pièce {lp} cm, {nom} {lc} cm, jeu {jeu_l:.2f} cm par côté (min {marge_cm})')
    if jeu_h < marge_cm - 1e-9:
        fautes.append(f'hauteur : pièce {hp} cm, {nom} {hc} cm, jeu {jeu_h:.2f} cm par côté (min {marge_cm})')
    assert not fautes, 'MP-J-10, case plus petite que la pièce + 0,5 cm par côté — ' + ' ; '.join(fautes)
    return round(jeu_l, 2), round(jeu_h, 2)

def verifier_mots_coupes(chemin_docx, chemin_pdf, minimum=4):
    """V10, V12 (R14, R15) : aucun mot du document n'est coupé au rendu. Compare les mots du .docx
    (python-docx : paragraphes et cellules) aux mots du PDF rendu (PyMuPDF) ; un mot d'au moins `minimum`
    lettres présent dans le .docx et absent du PDF a été coupé par une cellule trop étroite ou une césure.
    Renvoie la liste des mots coupés ; AssertionError s'il y en a."""
    import re, pymupdf
    from docx import Document
    def mots(texte):
        return set(m.lower() for m in re.findall(r"[^\W\d_]+(?:[’'][^\W\d_]+)?", texte) if len(m) >= minimum)
    d = Document(chemin_docx)
    textes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                textes.append(c.text)
    attendus = mots('\n'.join(textes))
    with pymupdf.open(chemin_pdf) as pdf:
        rendu = mots('\n'.join(page.get_text() for page in pdf))
    coupes = sorted(attendus - rendu)
    assert not coupes, 'mots coupés au rendu (élargir la cellule, raccourcir l’item ou réduire la taille) : ' + ', '.join(coupes)
    return coupes

# ---------- J10 : carte à pinces, une carte = une page (révision du 2.11.2026, suite) ----------
def carte_a_pinces(doc, questions, verso=False, largeur_q=13.4, largeur_opt=2.2, h_opt=0.85, mention=None, taille_q_pt=None):
    """J10 (révision du 2.11.2026, suite) : une carte = une page ; une question par bloc de trois lignes ;
    les trois réponses empilées dans la colonne du bord (droite au recto, gauche au verso) ; une pince par question.
    Au verso, le mot « bravo » dans la cellule de la bonne réponse (MP-J-04). questions : [(question, [r1, r2, r3], indice_juste)].
    Le numéro est tout à gauche ; la question est centrée dans son bloc, en grand (taille_q_pt : 28 pt jusqu'à
    6 questions, 22 pt jusqu'à 10, 18 pt au-delà, à réduire si une question est longue)."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention); solidariser(m)
    n = len(questions)
    t = doc.add_table(rows=3 * n, cols=2)
    cols = [largeur_opt, largeur_q] if verso else [largeur_q, largeur_opt]
    geometrie(t, cols, marge_cell_cm=0.12)
    iq, io = (1, 0) if verso else (0, 1)
    for k, (q, reps, juste) in enumerate(questions):
        for z in range(3):
            row = t.rows[3 * k + z]; ligne_tableau(row, h_opt, exacte=True)
            c = row.cells[io]; c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            bordures(c, top=TRAIT_FORT if z == 0 else TRAIT, bottom=TRAIT_FORT if z == 2 else TRAIT,
                       left=TRAIT_FORT, right=TRAIT_FORT)
            txt = ('bravo' if (verso and z == juste) else None) if verso else reps[z]
            _remplir(c, [[(txt, {'b': True})]] if txt else None, 'Fiche-Données', doc)
            for pp in c.paragraphs: pp.alignment = WD_ALIGN_PARAGRAPH.CENTER; pp.paragraph_format.space_after = Pt(0)
        for z in range(3):
            bordures(t.cell(3 * k + z, iq), top=TRAIT_FORT if z == 0 else None, bottom=TRAIT_FORT if z == 2 else None,
                       left=TRAIT_FORT, right=TRAIT_FORT)
        a = t.cell(3 * k, iq).merge(t.cell(3 * k + 2, iq)); a.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        _remplir(a, None if verso else [[(f'{k + 1}.', {'b': True}), '\t' + q]], 'Fiche-Données', doc)
        tq = taille_q_pt or (28 if n <= 6 else 22 if n <= 10 else 18)
        for pp in a.paragraphs:
            pp.paragraph_format.space_after = Pt(0); pp.paragraph_format.left_indent = Cm(0.2)
            pp.paragraph_format.tab_stops.add_tab_stop(Cm(largeur_q / 2), WD_TAB_ALIGNMENT.CENTER)   # question centrée dans le bloc
            for r in pp.runs: r.font.size = Pt(tq)
    solidariser_tableau(t)
    return t
```

#### 3 novembre 2026 : G21, imagier et scène à légender

Quatre fonctions ajoutées pour G21 : `scene_numerotee` pose sur une image sans texte (PDF R11, PNG ou JPG) des pastilles blanches numérotées aux positions données et refuse deux pastilles trop proches ; `lignes_numerotees` écrit n lignes (ou cases, G21-a) numérotées en colonnes ; `bande_etiquettes` produit la bande d'étiquettes-mots à découper (ordre mélangé, pointillés) ; `verifier_imagier` contrôle repères, mots et articles (V21). Le fichier `recettes_v7.2.py` réunit les cinq blocs.

**Test (3.11.2026)** : essais G21-a (105 %) et G21-b (95 %) rendus et mesurés, scène de parc dessinée en R11 (huit éléments), schéma OOXML valide ; `verifier_imagier` refuse un mot sans article et un nombre de mots différent du nombre de repères (statut : vérifié).

```
# ---------- G21 : imagier et scène à légender (3.11.2026) ----------
def scene_numerotee(image, reperes, base, largeur_mm=160, rayon_mm=4.0, taille_pt=11, dpi=300):
    """G21, R11 : pose sur une image (PNG, JPG ou PDF, sans texte : MP-I-05) des pastilles blanches numérotées
    de 1 à n, aux positions données en fraction de la largeur et de la hauteur (0 à 1). L'image est mise à la
    largeur demandée ; la hauteur suit. Écrit base.pdf (vectoriel) et base.png. reperes : [(x, y)], dans l'ordre
    des numéros. Deux pastilles à moins de 2 rayons l'une de l'autre sont refusées (lisibilité)."""
    import pymupdf, math
    k = 72 / 25.4
    src = pymupdf.open(image)
    if src.is_pdf:
        pg = src[0]; w0, h0 = pg.rect.width, pg.rect.height
    else:
        pix = pymupdf.Pixmap(image); w0, h0 = pix.width, pix.height
    hauteur_mm = largeur_mm * h0 / w0
    d = pymupdf.open(); p = d.new_page(width=largeur_mm * k, height=hauteur_mm * k)
    if src.is_pdf:
        p.show_pdf_page(p.rect, src, 0)
    else:
        p.insert_image(p.rect, filename=image)
    pts = [(x * largeur_mm, y * hauteur_mm) for x, y in reperes]
    for i, (xa, ya) in enumerate(pts):
        for xb, yb in pts[i + 1:]:
            assert math.hypot(xa - xb, ya - yb) >= 2 * rayon_mm, f'pastilles trop proches : {i + 1}'
    for i, (x, y) in enumerate(pts, 1):
        c = pymupdf.Point(x * k, y * k)
        sh = p.new_shape(); sh.draw_circle(c, rayon_mm * k)
        sh.finish(width=0.6 * k, color=(0, 0, 0), fill=(1, 1, 1)); sh.commit()
        txt = str(i)
        f = pymupdf.Font('helv'); lt = f.text_length(txt, fontsize=taille_pt)
        p.insert_text(pymupdf.Point(c.x - lt / 2, c.y + taille_pt * 0.36), txt, fontsize=taille_pt, fontname='helv')
    d.save(base + '.pdf'); p.get_pixmap(dpi=dpi).save(base + '.png')
    return base + '.png', hauteur_mm / 10

def lignes_numerotees(doc, n, colonnes=2, hauteur_cm=1.0, largeur_cm=LARGEUR_UTILE_CM, style='Fiche-Données', amorce='', cases=False):
    """G21 : n lignes d'écriture numérotées (1, 2, …), réparties en colonnes, bordure inférieure seule (R1a) ;
    cases=True : cadres complets, pour coller une étiquette (G21-a)."""
    lignes_par_col = -(-n // colonnes)
    t = doc.add_table(rows=lignes_par_col, cols=colonnes)
    geometrie(t, [largeur_cm / colonnes] * colonnes, marge_cell_cm=0.15)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_cm, exacte=True)
        for j, c in enumerate(row.cells):
            num = j * lignes_par_col + i + 1
            c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
            if num <= n:
                if cases:
                    bordures(c, top=TRAIT, bottom=TRAIT, left=TRAIT, right=TRAIT); c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                else:
                    bordures(c, bottom=TRAIT)
                _remplir(c, [[(f'{num}.  ', {'b': True}), amorce]], style, doc)
            else:
                bordures(c); _remplir(c, None, style, doc)
            for pp in c.paragraphs: pp.paragraph_format.space_after = Pt(0)
    solidariser_tableau(t)
    return t

def bande_etiquettes(doc, mots, par_rangee=4, hauteur_cm=1.2, largeur_cm=LARGEUR_UTILE_CM, style='Fiche-Pièce', melange=True, graine=1):
    """G21-a : étiquettes-mots à découper (R8), bords en pointillés (MP-J-05), ordre mélangé (MP-J-03)."""
    mots = list(mots)
    if melange:
        mots = melanger_sans_voisins(mots, graine=graine)
    rangees = en_rangees(mots, par_rangee)
    t = doc.add_table(rows=len(rangees), cols=par_rangee)
    geometrie(t, [largeur_cm / par_rangee] * par_rangee, marge_cell_cm=0.1)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_cm, exacte=True)
        for j, c in enumerate(row.cells):
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if j < len(rangees[i]):
                bordures(c, top=COUPE, bottom=COUPE, left=COUPE, right=COUPE)
                _remplir(c, [[rangees[i][j]]], style, doc)
                for pp in c.paragraphs: pp.alignment = WD_ALIGN_PARAGRAPH.CENTER; pp.paragraph_format.space_after = Pt(0)
            else:
                bordures(c); _remplir(c, None, style, doc)
    solidariser_tableau(t)
    return t

def verifier_imagier(reperes, mots, articles=('der', 'die', 'das', 'le', 'la', 'les', 'un', 'une', 'a', 'an', 'the')):
    """V21 (G21) : autant de repères que de mots ; mots tous différents ; en langue étrangère, chaque mot
    commence par un article de la liste (l'article fait partie du mot appris)."""
    assert len(reperes) == len(mots), f'{len(reperes)} repères pour {len(mots)} mots'
    assert len(set(m.lower() for m in mots)) == len(mots), 'mot en double'
    sans = [m for m in mots if m.split()[0].lower() not in articles]
    assert not sans, f'mots sans article : {sans}'
    return True
```

#### 19 novembre 2026 : J5, plateaux de parcours (serpent, escargot, chemin, circuit)

`plateau_parcours` dessine le plateau de J5 avec la classe `Dessin` (R11), sur toute la surface utile d'une page A4 portrait, sans tableau : `'serpent'` (ruban de cases en lacets), `'escargot'` (spirale ronde, pioche et défausse en haut), `'chemin'` (cases rondes reliées par un pointillé) ou `'circuit'` (boucle fermée, pioche et défausse au centre). La fonction refuse une case de moins de 2,5 cm, des cases rondes qui se chevauchent et une case d'accueil de cartes trop petite (`verifier_case_piece`, MP-J-10) ; elle renvoie le chemin du PDF, le nombre de cases et la plus petite dimension d'une case. Le bloc se place à la fin du module, après `verifier_case_piece`.

**Test (19.11.2026)** : quatre plateaux produits et regardés sur le rendu PDF : serpent 34 cases (29,3 mm), escargot 27 cases (25,0 mm), chemin 34 cases (27,0 mm), circuit 24 cases (31,0 mm) ; essai fait avec la police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J5 : plateaux de parcours (19.11.2026) — serpent, escargot, chemin, circuit ----------
PLATEAU_MM = (12.0, 16.5, 186.0, 264.0)        # x0, y0, largeur, hauteur : surface utile A4 portrait (MP-J-11)
CASE_MIN_MM = 25.0                             # plus petite dimension d'une case : un pion y tient
CARTE_DEFI_MM = (62.0, 66.0)                   # carte-défi au format J2

def _mot_ou_numero(d, x, y, i, n, boucle, taille_pt, speciale=False, mots=0.8):
    """Départ et Arrivée en mots, les autres cases numérotées de 1 à n - 2 (circuit : de 1 à n - 1).
    Case spéciale : numéro entouré, en plus du fond gris (jamais la teinte seule, MP-C-05)."""
    mot = 'Départ' if i == 0 else ('Arrivée' if i == n - 1 and not boucle else str(i))
    t = taille_pt if mot.isdigit() else max(taille_pt * mots, 11)             # « Départ », « Arrivée » : presque le corps des numéros
    d.texte(x, y + t * 0.125, mot, t, police='Arial-B')
    if speciale:
        d.cercle(x, y, taille_pt * 0.32, ep=0.8)

def _ruban(d, cases, colonnes, rangees, boucle, speciales, taille_pt):
    """Cases carrées qui se suivent sur une grille : contour du ruban en trait épais, séparation de deux
    cases qui se suivent en trait fin. Renvoie les rectangles (x, y, l, h) dans l'ordre du parcours."""
    x0, y0, L, H = PLATEAU_MM; l, h = L / colonnes, H / rangees
    n = len(cases); rang = {c: i for i, c in enumerate(cases)}
    for (c, r), i in rang.items():
        x, y = x0 + c * l, y0 + r * h
        if i in speciales:
            d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for (c, r), i in rang.items():
        x, y = x0 + c * l, y0 + r * h
        for (dc, dr), a, b in (((0, -1), (x, y), (x + l, y)), ((1, 0), (x + l, y), (x + l, y + h)),
                               ((0, 1), (x, y + h), (x + l, y + h)), ((-1, 0), (x, y), (x, y + h))):
            j = rang.get((c + dc, r + dr))
            suite = j is not None and (abs(i - j) == 1 or (boucle and abs(i - j) == n - 1))
            if not suite or j > i:
                d.ligne([a, b], ep=0.35 if suite else 1.4)
        _mot_ou_numero(d, x + l / 2, y + h / 2, i, n, boucle, taille_pt, i in speciales, mots=min(0.95, 0.82 * l / d.largeur_texte('Arrivée', taille_pt, 'Arial-B')))
    return [(x0 + c * l, y0 + r * h, l, h) for c, r in cases]

def _logement(d, x, y, mot):
    """Case d'accueil d'une pile de cartes-défis : carte + 0,5 cm par côté (MP-J-10), en tirets."""
    l, h = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10
    verifier_case_piece((CARTE_DEFI_MM[0] / 10, CARTE_DEFI_MM[1] / 10), (l / 10, h / 10), nom=mot)
    d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, tirets=(2, 1.5), ferme=True)
    d.texte(x + l / 2, y + h / 2 + 2, mot, 16)
    return l, h

def plateau_parcours(base, forme='serpent', titre='', speciales=(), colonnes=6, rangees=None, bande_mm=25.0,
                     diametre_mm=27.0, rangs=6, taille_pt=22, case_min_mm=CASE_MIN_MM, long_mm=31.0, dessin=None):
    """J5 : plateau de parcours d'une page A4 portrait, sur toute la surface utile, sans tableau.
    forme = 'serpent'  : ruban de cases en lacets, une case de liaison à chaque virage (J5-a) ;
            'escargot' : spirale ronde vers le centre, pioche et défausse en haut de la page (J5-b) ;
            'chemin'   : cases rondes (« pas japonais ») le long d'un chemin en lacets (J5-c) ;
            'circuit'  : boucle fermée au bord de la page, pioche et défausse au centre (J5-d).
    speciales : numéros des cases grisées au numéro entouré (« rejoue », « recule » : sens donné par la règle).
    case_min_mm : 25 par défaut ; 20 pour des jetons, au secondaire. long_mm : longueur d'une case de l'escargot.
    dessin : si un Dessin est fourni, le plateau y est tracé et aucun fichier n'est écrit (miniatures).
    Écrit base.svg et base.pdf ; renvoie (chemin du PDF, nombre de cases, plus petite dimension
    d'une case en mm)."""
    x0, y0, L, H = PLATEAU_MM; d = dessin or Dessin(); speciales = set(speciales)
    if forme in ('serpent', 'circuit'):
        if forme == 'serpent':
            rangees = rangees or 9; assert rangees % 2 == 1, 'serpent : nombre impair de rangées'
            cases = []
            for r in range(rangees):
                if r % 2 == 0:
                    cs = list(range(colonnes)); cases += [(c, r) for c in (cs if r % 4 == 0 else cs[::-1])]
                else:
                    cases.append((colonnes - 1 if r % 4 == 1 else 0, r))
        else:
            rangees = rangees or 8
            cases = ([(c, 0) for c in range(colonnes)] + [(colonnes - 1, r) for r in range(1, rangees)] +
                     [(c, rangees - 1) for c in range(colonnes - 2, -1, -1)] +
                     [(0, r) for r in range(rangees - 2, 0, -1)])
            lg, hg = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10
            e = (H - 2 * H / rangees - 2 * hg) / 3
            assert e >= 5 and L - 2 * L / colonnes >= lg + 10, 'circuit : centre trop petit pour les deux piles'
            for k, mot in enumerate(('Pioche', 'Défausse')):
                _logement(d, x0 + (L - lg) / 2, y0 + H / rangees + e + k * (hg + e), mot)
        rects = _ruban(d, cases, colonnes, rangees, forme == 'circuit', speciales, taille_pt)
        n, mini = len(cases), min(rects[0][2], rects[0][3])
    elif forme == 'escargot':
        lg, hg = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10; r0 = 20.0
        R = (H - hg - 2 + bande_mm / 2) / 2                                 # spirale sous les piles, centrée
        cx, cy = x0 + L / 2 + bande_mm / 4, y0 + H - R
        T = 2 * math.pi * (R - bande_mm - r0) / bande_mm                    # angle total de la bande
        rext = lambda t: R - bande_mm * t / (2 * math.pi)                   # bord extérieur ; intérieur = rext - bande
        pt = lambda r, t: (cx - r * math.sin(t), cy + r * math.cos(t))      # départ en bas, sens horaire
        pas = 400; ts = [T * i / pas for i in range(pas + 1)]
        cum = [0.0]
        for a, b in zip(ts, ts[1:]):
            cum.append(cum[-1] + (rext((a + b) / 2) - bande_mm / 2) * (b - a))
        n = round(cum[-1] / long_mm); coupes = [0.0]
        for i in range(1, n):
            cible = cum[-1] * i / n; j = next(k for k, v in enumerate(cum) if v >= cible); coupes.append(ts[j])
        coupes.append(T)
        for i in range(n):
            a, b = coupes[i], coupes[i + 1]; arc = [a + (b - a) * k / 20 for k in range(21)]
            if i in speciales:
                d.ligne([pt(rext(t), t) for t in arc] + [pt(rext(t) - bande_mm, t) for t in arc[::-1]],
                        ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
        d.ligne([pt(rext(t), t) for t in ts], ep=1.4); d.ligne([pt(rext(t) - bande_mm, t) for t in ts], ep=1.4)
        for i, t in enumerate(coupes):
            d.ligne([pt(rext(t), t), pt(rext(t) - bande_mm, t)], ep=1.4 if i in (0, n) else 0.35)
        for i in range(n):
            t = (coupes[i] + coupes[i + 1]) / 2; x, y = pt(rext(t) - bande_mm / 2, t)
            _mot_ou_numero(d, x, y, i, n + 1, False, taille_pt, i in speciales)
        d.texte(cx, cy + 2 + taille_pt * 0.1, 'Arrivée', max(16, taille_pt * 1.2), police='Arial-B')
        _logement(d, x0, y0, 'Pioche'); _logement(d, x0 + L - lg, y0, 'Défausse')
        for xc in (x0 + lg, x0 + L - lg):                                   # coins des piles hors de la spirale
            t = math.atan2(cx - xc, y0 + hg - cy) % (2 * math.pi)
            assert math.hypot(cx - xc, cy - y0 - hg) >= rext(t) + 2, 'escargot : une pile touche la spirale'
        mini = min(bande_mm, cum[-1] / n); n += 1                           # longueur mesurée au milieu de la bande
    elif forme == 'chemin':
        r = diametre_mm / 2; R = (H - diametre_mm) / (2 * (rangs - 1))       # rayon des virages
        xa, xb = x0 + r + R, x0 + L - r - R; axe = []                        # ligne médiane du chemin
        for k in range(rangs):
            y = y0 + r + 2 * R * k; va = k % 2 == 0
            axe += [(xa, y), (xb, y)] if va else [(xb, y), (xa, y)]
            if k < rangs - 1:
                c = xb if va else xa
                axe += [(c + (R if va else -R) * math.sin(math.radians(a)), y + R - R * math.cos(math.radians(a)))
                        for a in range(10, 180, 10)]
        cum = [0.0]
        for a, b in zip(axe, axe[1:]):
            cum.append(cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        n = int(cum[-1] // (diametre_mm + 4)) + 1; pas = cum[-1] / (n - 1); centres = []
        for i in range(n):
            s = min(pas * i, cum[-1] - 1e-6); j = next(k for k in range(len(cum) - 1) if cum[k + 1] >= s)
            f = (s - cum[j]) / (cum[j + 1] - cum[j])
            (xa_, ya_), (xb_, yb_) = axe[j], axe[j + 1]
            centres.append((xa_ + f * (xb_ - xa_), ya_ + f * (yb_ - ya_)))
        d.ligne(axe, ep=0.8, tirets=(2, 2))
        for i, (x, y) in enumerate(centres):
            d.cercle(x, y, r, ep=1.2, fond=(0.85, 0.85, 0.85) if i in speciales else (1, 1, 1))
            _mot_ou_numero(d, x, y, i, n, False, taille_pt * 0.9, i in speciales)
        ecart = min(math.hypot(a[0] - b[0], a[1] - b[1]) for i, a in enumerate(centres) for b in centres[i + 1:])
        mini = min(diametre_mm, ecart)
        assert mini >= diametre_mm - 0.01, 'chemin : deux cases se chevauchent ; réduire rangs ou diametre_mm'
    else:
        raise ValueError(forme)
    assert mini >= case_min_mm, f'cases de {mini:.1f} mm : trop petites pour un pion (minimum {case_min_mm} mm)'
    if titre:
        d.texte(105, 11.5, titre, 10)
    return (None if dessin else d.sauver(base)), n, round(mini, 1)
```

#### 19 novembre 2026 : planches à découper en PDF (MP-J-11, MP-J-12)

`planche_pdf` produit une planche de pièces en PDF avec la classe `Dessin` (R11) : colonnes × rangées de pièces sur toute la surface utile (18,6 × 26,4 cm), contours en pointillés, séparation interne des dominos en trait plein épais, repères de coupe dans les quatre marges, mention dans la marge du haut. Le texte est centré ; s'il est trop large, le corps diminue jusqu'au minimum demandé, puis la planche est refusée. `dimensions_piece` donne la taille d'une pièce pour un nombre de colonnes et de rangées ; `reperes_de_coupe` pose les repères sur n'importe quel `Dessin`. Le bloc se place après `Dessin` et `melanger_sans_voisins`.

**Test (19.11.2026)** : J1, boucle Lune, 2 × 8 dominos de 9,3 × 3,3 cm (corps de 19,5 pt), ordre mélangé ; dispositions J3 (3 × 3 cartes de 6,2 × 8,8 cm) et J4 (2 × 4 cartes de 9,3 × 6,6 cm) ; un texte trop long est refusé ; rendus PDF regardés, police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- MP-J-11 et MP-J-12 : planche de pièces en PDF, toute la page, repères de coupe (19.11.2026) ----------
SURFACE_MM = (12.0, 16.5, 186.0, 264.0)        # x0, y0, largeur, hauteur : surface utile A4 portrait (MP-J-11)

def dimensions_piece(colonnes, rangees):
    """MP-J-11 : largeur et hauteur d'une pièce (cm) quand colonnes × rangees pièces remplissent la page."""
    return round(SURFACE_MM[2] / colonnes / 10, 2), round(SURFACE_MM[3] / rangees / 10, 2)

def reperes_de_coupe(d, xs, ys, long_mm=4.5, ecart_mm=2.5):
    """MP-J-12 : un trait fin (0,5 pt) dans le prolongement de chaque ligne de coupe, dans les quatre marges.
    xs : abscisses des coupes verticales ; ys : ordonnées des coupes horizontales (mm)."""
    x0, y0, L, H = SURFACE_MM; ep = 0.5 * 25.4 / 72
    assert min(x0, y0) - ecart_mm - long_mm >= 5, 'repères hors de la zone imprimable'
    for x in xs:
        d.ligne([(x, y0 - ecart_mm - long_mm), (x, y0 - ecart_mm)], ep=ep)
        d.ligne([(x, y0 + H + ecart_mm), (x, y0 + H + ecart_mm + long_mm)], ep=ep)
    for y in ys:
        d.ligne([(x0 - ecart_mm - long_mm, y), (x0 - ecart_mm, y)], ep=ep)
        d.ligne([(x0 + L + ecart_mm, y), (x0 + L + ecart_mm + long_mm, y)], ep=ep)

def planche_pdf(base, pieces, colonnes, rangees, mention='', taille_pt=16, taille_min_pt=12, gras_gauche=True,
                dessin=None, lisere=False):
    """R8 en PDF : colonnes × rangees pièces sur toute la surface utile (MP-J-11), contour en pointillés
    (MP-J-05), repères de coupe (MP-J-12), mention dans la marge du haut.
    pieces : une chaîne par pièce (lignes séparées par '\\n'), ou un couple (moitié gauche, moitié droite)
    pour un domino : séparation interne en trait plein épais, moitié gauche en gras (la réponse).
    Le texte est centré dans sa pièce ou sa moitié ; s'il est trop large, le corps diminue jusqu'à
    taille_min_pt, puis la planche est refusée. Une planche par appel ; l'ordre des pièces est celui reçu
    (à mélanger avant : melanger_sans_voisins, MP-J-03 ; verso : verso_de, R12).
    dessin : si un Dessin est fourni, la planche y est tracée et aucun fichier n'est écrit (miniatures).
    lisere=True pour un jeu de cartes (MP-J-14) : cadre aux coins arrondis à 3 mm du trait de coupe, tracé avant
    le texte (lisere_cartes) ; le texte reste à l'intérieur du cadre. Pas de liseré pour un domino ni un puzzle.
    Écrit base.svg et base.pdf ; renvoie (chemin du PDF, largeur et hauteur d'une pièce en cm, corps utilisé)."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees; jeu = 10 if lisere else 6
    assert len(pieces) <= colonnes * rangees, 'trop de pièces pour une planche'
    d = dessin or Dessin(); moities = [p if isinstance(p, (tuple, list)) else (p,) for p in pieces]
    corps = taille_pt
    while True:                                                             # même corps pour toute la planche
        trop = [t for m in moities for k, bloc in enumerate(m) for t in bloc.split('\n')
                if d.largeur_texte(t, corps, 'Arial-B' if len(m) == 2 and k == 0 and gras_gauche else 'Arial')
                > l / len(m) - jeu]
        if not trop: break
        corps -= 0.5
        assert corps >= taille_min_pt, f'texte trop long pour la pièce : {trop[0]!r}'
    if lisere: lisere_cartes(d, colonnes, rangees)                         # MP-J-14, sous le texte
    for i, m in enumerate(moities):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; lm = l / len(m)
        for k, bloc in enumerate(m):
            lignes = bloc.split('\n'); pas = corps * 1.25 * 25.4 / 72
            yb = y + h / 2 - (len(lignes) - 1) * pas / 2 + corps * 0.125
            for j, t in enumerate(lignes):
                d.texte(x + lm * (k + 0.5), yb + j * pas, t, corps,
                        police='Arial-B' if len(m) == 2 and k == 0 and gras_gauche else 'Arial')
            if k:
                d.ligne([(x + lm * k, y), (x + lm * k, y + h)], ep=0.8)       # séparation interne : 2,25 pt
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs:
        d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))            # traits de coupe : 1 pt, pointillés
    for y in ys:
        d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention:
        assert d.largeur_texte(mention, 8) <= L - 10, 'mention trop longue'
        d.texte(105, 8.0, mention, 8)                                       # marge du haut, au-dessus des repères
    return (None if dessin else d.sauver(base)), (round(l / 10, 2), round(h / 10, 2)), corps
```

#### 19 novembre 2026 : panorama des jeux (MP-J-13)

`panorama_jeux` dessine avec la classe `Dessin` (R11) une image A4 paysage qui présente les jeux disponibles **uniquement par des miniatures tirées des documents réels** : la page du modèle Word ou de la planche prête à imprimer est insérée telle quelle, réduite (`show_pdf_page`), avec le nom, l'usage et la page du document (sans code depuis le 21.11.2026). La table `SOURCES_JEUX` donne, pour chaque gabarit, le document de la boîte à outils, la page de chaque tranche d'âge et le nombre de pièces par planche ; un gabarit sans document est cité dans une liste, sans image (20.11.2026). `miniatures_tranche` compose de la même façon la page d'une tranche d'âge (fonction commune `_page_miniatures`). L'IA l'affiche avant de proposer un jeu, ou quand on lui demande quelles sont les possibilités (MP-J-13). Les listes `JEUX` et `SOURCES_JEUX` se complètent à chaque nouveau gabarit ou nouveau document ; un modèle Word est converti en PDF avant l'appel. `panorama_exercices` fait de même pour les gabarits d'exercice G1 à G23 (liste `EXERCICES`, schémas dans `_vignette_exercice`) : l'IA l'affiche quand on lui demande quels exercices sont possibles. Le bloc se place après `Dessin` et `arc_pts`.

**Test (19.11.2026)** : images produites à partir du code de cette annexe et regardées (panorama des jeux, 20.11.2026 : 41 miniatures de documents réels, aucun gabarit en liste ; pages par tranche d'âge : 38 à 40 miniatures ; panorama des exercices : 23 gabarits, en schémas ; textes sans débordement) ; police Liberation Sans à la place d'Arial ; affichage par une IA dans une conversation : non testé.

```
# ---------- MP-J-13 : panorama des jeux, image à montrer avant de choisir (19.11.2026) ----------
JEUX = [('J1', 'Domino-boucle', 'question et réponse, en boucle'), ('J2', 'Memory, appariement', 'associer deux éléments'),
        ('J3', 'Familles', 'classer par catégorie'), ('J4', 'Cartes recto-verso', 'rappel : question, puis réponse'),
        ('J5-a', 'Plateau · serpent', 'parcours avec cartes-défis'), ('J5-b', 'Plateau · escargot', 'jeu de l\'oie, arrivée au centre'),
        ('J5-c', 'Plateau · chemin', 'parcours de cases rondes'), ('J5-d', 'Plateau · circuit', 'boucle, partie en plusieurs tours'),
        ('J6', 'Dé à monter', 'tirer un élément au hasard'), ('J7', 'Loto', 'on entend ou on lit, on couvre'),
        ('J8', 'Symboles communs', 'trouver vite l\'élément commun'), ('J9', 'Trouve quelqu\'un qui…', 'questionner ses camarades'),
        ('J10', 'Carte à pinces', 'choisir, puis se corriger au verso'), ('J11', 'Roue à fenêtre et rabat', 'réponse sous le rabat'),
        ('J12', 'Lettres à fabriquer', 'tracer avec le doigt'), ('J13', 'Cartes de rôle', 'un rôle dans le groupe'),
        ('J14', 'Cartes d\'erreurs', 'analyser une démarche'), ('J15', 'Cartes d\'aide graduée', 'se donner un coup de pouce'),
        ('J16', 'Cartons-réponses', 'voter sans écran'), ('J17', 'Grille d\'alignement', 'répondre pour aligner ses jetons'),
        ('J18', 'Serpents et échelles', 'monter si l\'on répond juste'), ('J19', 'Bataille navale', 'croiser une colonne et une ligne'),
        ('J20', 'Roue de tirage', 'tirer au sort sans dé'), ('J21', 'Puzzles à deux pièces', 'associer : la découpe corrige'),
        ('J22', 'Puzzle à bandes', 'ranger pour reformer l\'image'), ('J23', 'Mot mystère', 'des définitions, un mot caché'),
        ('J24', 'Cocotte en papier', 'se poser des défis à deux'), ('J25', 'Horloge à aiguilles', 'lire et régler l\'heure'),
        ('J26', 'Mémo-fiches en éventail', 'réviser, fiche après fiche'), ('J27', 'Bandes graphiques', 'repasser un tracé au feutre'),
        ('J28', 'Plateau à camemberts', 'quiz à six catégories'), ('J29', 'Cherche et trouve', 'repérer vite un mot qui convient'),
        ('J30', 'Mots interdits', 'faire deviner sans dire'), ('J31', 'Petit bac', 'un mot par catégorie et par lettre'),
        ('J32', 'Cartes à terminaisons', 'compléter la phrase tirée'), ('J33', 'Petits chevaux', 'avancer en répondant'),
        ('J34', 'Qui est-ce ?', 'questionner par oui ou par non'), ('J35', 'Bataille', 'comparer deux cartes'),
        ('J36', 'Tuiles-lettres', 'composer des mots'), ('J37', 'Sudoku', 'raisonner par élimination'),
        ('J38', 'Mot caché : la fleur', 'deviner un mot, lettre après lettre')]

_J5 = 'J5 — Plateaux de parcours (serpent, escargot, chemin, circuit) — 1P-4P, 5P-8P, 9S-11S'
_DE = ('Dé à monter — grand dé (faces de 6 cm, chiffres)', 'Dé à monter — deux petits dés (faces de 4,2 cm, chiffres)')
# code : (document de la boîte à outils, ou un document par tranche ; page de chaque tranche 1P-4P, 5P-8P, 9S-11S,
#         None si le gabarit n'est pas proposé à cet âge ; unité ; nombre par planche pour chaque tranche)
SOURCES_JEUX = {
    'J1': ('Modèle J1 — dominos', (2, 3, 4), 'dominos', (10, 16, 20)),
    'J2': ('Modèle J2 — memory, paires question-réponse (dos à motif)', (3, 5, 7), 'cartes', (6, 12, 20)),
    'J3': ('Modèle J3 — familles', (2, 3, 4), 'cartes', (6, 9, 16)),
    'J4': ('Modèle J4 — cartes de rappel (recto-verso)', (2, 4, 6), 'cartes', (6, 8, 15)),
    'J5-a': (_J5, (1, 5, 9), 'cases', (19, 34, 53)), 'J5-b': (_J5, (2, 6, 10), 'cases', (15, 27, 42)),
    'J5-c': (_J5, (3, 7, 11), 'cases', (21, 34, 55)), 'J5-d': (_J5, (4, 8, 12), 'cases', (16, 24, 34)),
    'J6': ((_DE[0], _DE[1], _DE[1]), (1, 1, 1), 'dés', (1, 2, 2)),
    'J7': ('Modèle J7 — loto, cartons et cartes d’appel (dos à motif, feuille de contrôle)', (4, 7, 12), 'cartons', (6, 8, 6)),
    'J8': ('Modèle J8 — symboles communs', (2, 3, 4), 'cartes', (7, 13, 21)),
    'J9': ('Modèle J9 — grille « Trouve quelqu’un qui… »', (2, 3, 4), 'cases', (6, 16, 25)),
    'J10': ('Modèle J10 — carte à pinces (recto-verso)', (2, 4, 6), 'questions', (6, 10, 12)),
    'J11': ('J11 — Roue à fenêtre et rabat (exemples à 4, 6 et 8 secteurs)', (1, 2, 3), 'secteurs', (4, 6, 8)),
    'J12': ('Modèle J12 — lettres à fabriquer', (2, None, None), 'plaques', (4, None, None)),
    'J13': ('Modèle J13 — cartes de rôle', (2, 3, 4), 'cartes', (4, 8, 8)),
    'J14': ('Modèle J14 — cartes d’erreurs (recto-verso)', (None, 2, 4), 'cartes', (None, 4, 6)),
    'J15': ('Modèle J15 — cartes d’aide graduée', (2, 3, 4), 'cartes', (4, 8, 8)),
    'J16': ('Modèle J16 — cartons-réponses', (2, 3, 4), 'cartons', (4, 4, 6)),
    'J17': ('J17 — Grille d’alignement (nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'ronds', (20, 35, 48)),
    'J18': ('J18 — Serpents et échelles — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases', (30, 48, 80)),
    'J19': ('J19 — Bataille navale (lettres et nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases par grille', (25, 36, 64)),
    'J20': ('J20 — Roue de tirage (nombres) — 4, 6 et 8 secteurs', (1, 2, 3), 'secteurs', (4, 6, 8)),
    'J21': ('J21 — Puzzles à deux pièces (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'puzzles', (8, 12, 18)),
    'J22': ('J22 — Puzzle à bandes (exemples) — 5, 10 et 12 bandes', (1, 2, 3), 'bandes', (5, 10, 12)),
    'J23': ('J23 — Mot mystère (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'mots', (4, 6, 8)),
    'J24': ('J24 — Cocotte en papier (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'défis', (8, 8, 8)),
    'J25': ('J25 — Horloge à aiguilles — heures, minutes, 24 heures', (1, 2, 3), 'graduations', (12, 60, 60)),
    'J26': ('J26 — Mémo-fiches en éventail (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'fiches', (6, 8, 10)),
    'J27': ('J27 — Bandes graphiques — 4, 6 et 8 bandes', (1, 2, 3), 'bandes', (4, 6, 8)),
    'J28': ('J28 — Plateau à camemberts — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases', (37, 49, 73)),
    'J29': ('J29 — Cherche et trouve de mots (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'mots', (20, 38, 66)),
    'J30': ('J30 — Mots interdits (exemples) — 5P-8P, 9S-11S', (None, 1, 2), 'cartes', (None, 9, 12)),
    'J31': ('J31 — Petit bac — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases à remplir', (12, 30, 48)),
    'J32': ('J32 — Cartes à terminaisons (exemple 5P-8P, avec solutions)', (None, 1, None), 'cartes-phrases', (None, 12, None)),
    'J33': ('J33 — Petits chevaux', (1, 1, 1), 'cases', (52, 52, 52)),
    'J34': ('J34 — Qui est-ce (nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'éléments', (12, 24, 30)),
    'J35': ('J35 — Bataille (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cartes', (12, 16, 20)),
    'J36': ('J36 — Tuiles-lettres — 48, 117 et 204 tuiles', (1, 2, 3), 'tuiles', (48, 117, 204)),
    'J37': ('J37 — Sudoku — 4 × 4, 6 × 6, 9 × 9, avec solutions', (1, 2, 3), 'grilles', (4, 2, 2)),
    'J38': ('J38 — Mot caché, la fleur', (1, 1, 1), 'parties', (3, 3, 3))}

def _page_miniatures(base, titres, entrees, dossier, dpi, sources=None):
    """Page A4 portrait de miniatures. Chaque miniature est la page du document réel, insérée telle quelle et réduite
    (jamais un schéma). entrees : liste de (code, nom, ligne 2, tranche). Écrit base.pdf et base.png ; renvoie le PNG."""
    import os
    d = Dessin(); m = 8; col = 5 if len(entrees) < 25 else 6 if len(entrees) < 36 else 7       # 5 × 5, 6 × 6 ou 7 × 7 miniatures
    k = {5: 0.14, 6: 0.115, 7: 0.097}[col]
    l, h = (210 - 2 * m) / col, (297 - 2 * m) / col
    d.texte(m + l / 2, m + 14, titres[0], {5: 13, 6: 11, 7: 9.5}[col], police='Arial-B')
    for j, t in enumerate(titres[1:]): d.texte(m + l / 2, m + 21 + j * (4.3 if col < 7 else 3.4), t, {5: 7.5, 6: 6.2, 7: 5.2}[col])
    sans = []; ouverts = {}
    for code, nom, ligne2, tranche in entrees:
        doc, pages, unite, nombres = (sources or SOURCES_JEUX).get(code, (None, (None,) * 3, '', ()))
        if doc is None or pages[tranche - 1] is None: sans.append(nom); continue
        i = len([1 for e in entrees[:entrees.index((code, nom, ligne2, tranche))] if e[1] not in sans]) + 1
        x, y = m + (i % col) * l, m + (i // col) * h; mx, my = x + (l - 210 * k) / 2, y + 1.5
        doc = doc if isinstance(doc, str) else doc[tranche - 1]; page = pages[tranche - 1]
        src = ouverts.setdefault(doc, d.f.open(os.path.join(dossier, doc + '.pdf'))); r = src[page - 1].rect; w, t = r.width / d.k * k, r.height / d.k * k
        ox, oy = mx + (210 * k - w) / 2, my + (297 * k - t) / 2
        d.p.show_pdf_page(d.f.Rect(ox * d.k, oy * d.k, (ox + w) * d.k, (oy + t) * d.k), src, page - 1)
        d.ligne([(mx, my), (mx + 210 * k, my), (mx + 210 * k, my + 297 * k), (mx, my + 297 * k)], ep=0.25, ferme=True)
        by = my + 297 * k; lignes = ((nom, 7.2 if col < 7 else 6.2, 'Arial-B'), (ligne2 or f'{nombres[tranche - 1]} {unite}'.replace('1 dés', '1 dé'), 6.4, 'Arial'),
                                    (('modèle Word' if doc.startswith('Modèle') else 'planche PDF') + f' · page {page}', 5.6, 'Arial'))
        for j, (t, c, pol) in enumerate(lignes):
            while d.largeur_texte(t, c, pol) > l - 1.5: c -= 0.2; assert c >= 4.5, t
            d.texte(x + l / 2, by + (3.4 if col < 7 else 3.0) + j * {5: 3.3, 6: 2.9, 7: 2.5}[col], t, c, police=pol)
    if sans:                                                                # sans document : une liste, jamais d'image
        d.texte(m + 2, m + 40, 'Sans document prêt :', 7, ancre='s', police='Arial-B')
        for j, t in enumerate(sans): d.texte(m + 2, m + 44 + j * 3.3, t, 6.2, ancre='s')
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return d.png(base, dpi)

def panorama_jeux(base, dossier, dpi=200):
    """MP-J-13 : image à afficher avant de choisir un jeu. Elle ne contient que des miniatures tirées des documents
    réels de la boîte à outils (SOURCES_JEUX), au format 5P-8P (ou, à défaut, au premier format existant) :
    l'enseignant·e obtient ce qu'il ou elle voit. dossier : dossier où ces documents se trouvent en PDF (un modèle
    Word y est d'abord converti en PDF, sans rien changer)."""
    def tr(code):
        pages = SOURCES_JEUX.get(code, (None, (None,) * 3))[1]
        return 2 if pages[1] is not None else next((t for t in (1, 3) if pages[t - 1] is not None), 2)
    return _page_miniatures(base, ('Jeux imprimés', 'Chaque miniature est une page', 'du document réel, réduite.', 'Dites le nom', 'du jeu choisi.'),
                            [(c, n, u, tr(c)) for c, n, u in JEUX], dossier, dpi)

SUPPORTS = [('G22', 'Lignes d\'écriture romandes', 'pages de 7, 4 et 2,5 mm'), ('G23', 'Syllabes et sons', 'image, syllabes, sons'),
            ('G24', 'Maisons des nombres', 'décomposer un nombre'), ('G25', 'Reproduction sur quadrillage', 'tracer la même figure'),
            ('G26', 'Calendrier mensuel', 'un mois, lundi à dimanche'), ('G27', 'Étiquettes de l\'horaire', 'afficher la journée'),
            ('G28', 'Livret à onglets', 'une feuille par onglet'), ('G29', 'Page de journal', 'articles sur deux colonnes'),
            ('G30', 'Planche de BD', 'cases vides à dessiner'), ('G31', 'Plan d\'exposé', 'préparer sa présentation')]
SOURCES_SUPPORTS = {
    'G22': ('G22 — Lignes d’écriture, lignage romand — 7 mm, 4 mm et 2,5 mm', (1, 1, 1), '', ()),
    'G23': ('G23 — Syllabes et sons (exemples) — 8 et 12 mots', (2, 2, 2), '', ()),
    'G24': ('G24 — Maisons des nombres — 3 à 6, 7 à 10', (2, 2, 2), '', ()),
    'G25': ('G25 — Reproduction sur quadrillage — maison, bateau, sapin, fusée', (1, 1, 1), '', ()),
    'G26': ('G26 — Calendrier mensuel (exemples) — décembre 2026, janvier et février 2027', (1, 1, 1), '', ()),
    'G27': ('G27 — Étiquettes de l’horaire (exemple, 16 étiquettes)', (1, 1, 1), '', ()),
    'G28': ('G28 — Livret à onglets (exemple, livret de rentrée à 5 onglets)', (1, 1, 1), '', ()),
    'G29': ('G29 — Page de journal de classe — 3 et 4 articles', (1, 1, 1), '', ()),
    'G30': ('G30 — Planches de bande dessinée — 3, 7 et 10 cases', (2, 2, 2), '', ()),
    'G31': ('G31 — Plan d’exposé — 2 et 3 parties', (2, 2, 2), '', ())}

def panorama_supports(base, dossier, dpi=200):
    """Page des fiches et supports qui ont un document prêt à imprimer (G22 à G31) : miniatures tirées des documents
    réels, comme pour les jeux. Complète panorama_exercices, qui montre G1 à G23 en schémas."""
    return _page_miniatures(base, ('Fiches et supports', 'Chaque miniature est une page', 'du document réel, réduite.', 'Dites le nom', 'du support choisi.'),
                            [(c, n, u, 1) for c, n, u in SUPPORTS], dossier, dpi, SOURCES_SUPPORTS)

def miniatures_tranche(base, tranche, dossier, dpi=200):
    """Page des jeux proposés à une tranche d'âge (1 : 1P-4P ; 2 : 5P-8P ; 3 : 9S-11S) : pour chaque gabarit, la page
    réelle du format de cette tranche, réduite, avec le nombre de pièces, de cases ou de questions par planche."""
    noms = ('1P à 4P', '5P à 8P', '9S à 11S')
    return _page_miniatures(base, ('Jeux · ' + noms[tranche - 1], 'Chaque miniature est une page', 'du document réel, réduite.', 'Sous le nom : nombre de pièces,', 'de cases ou de questions.'),
                            [(c, n, None, tranche) for c, n, u in JEUX if SOURCES_JEUX[c][1][tranche - 1] is not None], dossier, dpi)


# ---------- Panorama des gabarits d'exercice G1 à G23 (19.11.2026) ----------
EXERCICES = [('G1', 'Entourer'), ('G2', 'Relier'), ('G3', 'Compléter'), ('G4', 'Transformer, recopier'), ('G5', 'Remettre en ordre'),
             ('G6', 'Cocher'), ('G7', 'Production courte guidée'), ('G8', 'Repérer dans un texte'), ('G9', 'Tableau à compléter'),
             ('G10', 'Image et écriture'), ('G11', 'Colorier selon une consigne'), ('G12', 'Classer en colonnes'), ('G13', 'Calcul posé'),
             ('G14', 'Chronologie'), ('G15', 'Copier puis illustrer'), ('G16', 'Recherche visuelle'), ('G17', 'Série chronométrée'),
             ('G18', 'Grille croisée de nombres'), ('G19', 'Tracé de chemin'), ('G20', 'Dictée réfléchie'), ('G21', 'Imagier, scène à légender'), ('G22', 'Lignes d\'écriture romandes'), ('G23', 'Syllabes et sons')]

def _vignette_exercice(d, code, x, y, l, h):
    """Schéma d'un gabarit d'exercice dans la boîte (x, y, l, h), en mm : des formes, aucun texte d'élève."""
    G = (0.82, 0.82, 0.82); N = (0.35, 0.35, 0.35); cx, cy = x + l / 2, y + h / 2
    def rect(a, b, w, t, ep=0.5, fond=None, tirets=None):
        d.ligne([(a, b), (a + w, b), (a + w, b + t), (a, b + t)], ep=ep, ferme=True, fond=fond, tirets=tirets)
    mot = lambda a, b, w: rect(a, b, w, 1.8, ep=0, fond=N)                   # un mot imprimé : barre sombre
    ligne = lambda a, b, w: d.ligne([(a, b), (a + w, b)], ep=0.35)          # une ligne d'écriture
    if code == 'G1':
        for i in range(5): rect(x + 4 + i * 7.5, cy - 2.5, 5, 5, fond=G if i == 3 else None)
        d.cercle(x + 4 + 3 * 7.5 + 2.5, cy, 5, ep=0.8)
    elif code == 'G2':
        for i in range(3): d.cercle(x + 8, y + 5 + i * 8.5, 1.3, ep=0, fond=N); d.cercle(x + l - 8, y + 5 + i * 8.5, 1.3, ep=0, fond=N); mot(x + 1, y + 4 + i * 8.5, 5); mot(x + l - 6, y + 4 + i * 8.5, 5)
        for a, b in ((0, 2), (1, 0), (2, 1)): d.ligne([(x + 8, y + 5 + a * 8.5), (x + l - 8, y + 5 + b * 8.5)], ep=0.6)
    elif code == 'G3':
        for j in range(3): mot(x + 3, y + 6 + j * 8, 9); ligne(x + 14, y + 7.8 + j * 8, 11); mot(x + 27, y + 6 + j * 8, 8)
    elif code == 'G4':
        mot(x + 3, y + 5, 10); mot(x + 15, y + 5, 7); mot(x + 24, y + 5, 9); d.ligne([(cx, y + 9.5), (cx, y + 14)], ep=0.8); d.ligne([(cx - 1.8, y + 12), (cx, y + 14.4), (cx + 1.8, y + 12)], ep=0.8)
        for j in range(2): ligne(x + 3, y + 19 + j * 5, l - 6)
    elif code == 'G5':
        for i, t in enumerate('312'): rect(x + 3 + i * 12, cy - 5, 10, 10, fond=(1, 1, 1)); d.texte(x + 8 + i * 12, cy + 2, t, 13, police='Arial-B')
    elif code == 'G6':
        for j in range(3): rect(x + 5, y + 4 + j * 8, 4, 4); mot(x + 12, y + 5.2 + j * 8, 14 + 3 * j)
        d.ligne([(x + 5.8, y + 14), (x + 6.9, y + 15.4), (x + 8.6, y + 12.6)], ep=0.9)
    elif code == 'G7':
        mot(x + 3, y + 5, 12); ligne(x + 17, y + 6.8, l - 20)
        for j in range(3): ligne(x + 3, y + 13 + j * 5.5, l - 6)
    elif code == 'G8':
        for j in range(4):
            for i, w in enumerate((8, 6, 10, 7)): mot(x + 3 + sum((8, 6, 10, 7)[:i]) + i * 1.6, y + 5 + j * 6, w)
        rect(x + 3 + 8 + 1.6 - 0.6, y + 5 + 6 - 1, 7.2, 3.8, ep=0.6); rect(x + 3 + 14 + 3.2 - 0.6, y + 5 + 18 - 1, 11.2, 3.8, ep=0.6)
    elif code == 'G9':
        for j in range(4):
            for i in range(3): rect(x + 4 + i * 11, y + 3 + j * 5.6, 11, 5.6, ep=0.4, fond=G if j == 0 else None)
    elif code in ('G10', 'G15'):
        a = x + 3 if code == 'G10' else x + l - 19; b = x + 22 if code == 'G10' else x + 3
        rect(a, y + 4, 16, 16, tirets=(1, 1) if code == 'G15' else None)
        if code == 'G10': d.ligne([(a + 2, y + 17), (a + 7, y + 9), (a + 10, y + 13), (a + 12, y + 11), (a + 15, y + 17)], ep=0.6); d.cercle(a + 12, y + 7.5, 1.5, ep=0.5)
        else: mot(b, y + 2.5, 14)
        for j in range(3): ligne(b, y + 9 + j * 5, l - 25)
    elif code == 'G11':
        for i in range(12): rect(x + 5 + (i % 4) * 8, y + 3 + (i // 4) * 7, 8, 7, ep=0.4, fond=(G if i in (1, 6, 8) else (0.6, 0.6, 0.6) if i in (3, 5, 10) else None))
    elif code == 'G12':
        for i in range(2):
            rect(x + 4 + i * 17, y + 2.5, 16, 5, fond=G); rect(x + 4 + i * 17, y + 7.5, 16, 17, ep=0.4)
            for j in range(2 + i): mot(x + 7 + i * 17, y + 11 + j * 4.5, 9)
    elif code == 'G13':
        for j, t in enumerate(('47', '25')): d.texte(cx + 2, y + 9 + j * 7, t, 15, police='Arial-B')
        d.texte(cx - 9, y + 16, '+', 15, police='Arial-B'); d.ligne([(cx - 12, y + 18.5), (cx + 9, y + 18.5)], ep=0.8); rect(cx - 6, y + 20, 14, 6, ep=0.4)
    elif code == 'G14':
        d.ligne([(x + 3, cy + 3), (x + l - 3, cy + 3)], ep=0.9); d.ligne([(x + l - 5.5, cy + 1), (x + l - 3, cy + 3), (x + l - 5.5, cy + 5)], ep=0.9)
        for i in range(4): d.ligne([(x + 7 + i * 9, cy + 1), (x + 7 + i * 9, cy + 5)], ep=0.6); rect(x + 3.5 + i * 9, cy - 8, 7, 6, ep=0.4)
    elif code == 'G16':
        alea = random.Random(7)
        for i in range(26):
            a, b = x + 3 + alea.random() * (l - 6), y + 3 + alea.random() * (h - 6)
            if i % 9 == 0: d.ligne([(a - 1.5, b + 1.3), (a, b - 1.5), (a + 1.5, b + 1.3)], ep=0.5, ferme=True, fond=N); d.cercle(a, b, 3, ep=0.6)
            else: d.cercle(a, b, 1.2, ep=0.4)
    elif code == 'G17':
        for i in range(2):
            for j in range(4): mot(x + 3 + i * 13, y + 5 + j * 5.5, 5); ligne(x + 9 + i * 13, y + 6.8 + j * 5.5, 5)
        d.cercle(x + l - 7, cy, 5, ep=0.7); d.ligne([(x + l - 7, cy), (x + l - 7, cy - 3.5)], ep=0.6); d.ligne([(x + l - 7, cy), (x + l - 4.8, cy + 1)], ep=0.6); rect(x + l - 8, cy - 7, 2, 1.6, ep=0, fond=N)
    elif code == 'G18':
        for i in range(20): rect(x + 6 + (i % 5) * 6, y + 2 + (i // 5) * 6, 6, 6, ep=0.4, fond=N if i in (2, 6, 13, 17) else None)
    elif code == 'G19':
        pts = [(x + 3 + t * (l - 8) / 30, cy + 7 * math.sin(t * 0.42)) for t in range(31)]
        for s in (-2.2, 2.2): d.ligne([(a, b + s) for a, b in pts], ep=0.5)
        d.ligne([(x + l - 7, pts[-1][1] - 2.5), (x + l - 3, pts[-1][1]), (x + l - 7, pts[-1][1] + 2.5)], ep=0.9)
    elif code == 'G20':
        d.ligne(arc_pts(x + 20, y + 5, 3, 0, 90, 5) + arc_pts(x + 20, y + 8, 3, 90, 180, 5) + [(x + 9, y + 11), (x + 6, y + 14), (x + 6.5, y + 11)] +
                arc_pts(x + 6, y + 8, 3, 180, 270, 5) + arc_pts(x + 6, y + 5, 3, 270, 360, 5), ep=0.6, ferme=True)
        mot(x + 6, y + 5.6, 13)
        for j in range(2): ligne(x + 3, y + 19 + j * 5, l - 6)
        d.cercle(x + l - 6, y + 7, 3.2, ep=0.6); d.texte(x + l - 6, y + 8.6, '?', 10, police='Arial-B')
    elif code == 'G23':
        for i in range(3):
            xx = x + 3 + i * 12.5; rect(xx, y + 2, 11, 23); rect(xx + 1.5, y + 3.5, 8, 8, ep=0.3, tirets=(0.8, 0.8)); mot(xx + 2, y + 13.5, 7)
            for q in range(2): rect(xx + 1.5 + q * 3.2, y + 17, 2.4, 2.4, ep=0.4)
            for q in range(3): d.cercle(xx + 2.6 + q * 3, y + 22.5, 1.1, ep=0.4)
    elif code == 'G22':
        for i in range(3):
            yy = y + 3 + i * 8.5
            for k, (ep, t) in enumerate(((0.25, (0.4, 0.9)), (0.25, None), (0.6, None), (0.25, (0.4, 0.9)))): d.ligne([(x + 2, yy + k * 2), (x + l - 2, yy + k * 2)], ep=ep, tirets=t)
    elif code == 'G21':
        rect(x + 3, y + 2.5, 20, 22); d.ligne([(x + 3, y + 18), (x + 23, y + 18)], ep=0.4); rect(x + 6, y + 10, 6, 8, ep=0.4); d.cercle(x + 18, y + 8, 2.2, ep=0.4)
        for i, (a, b) in enumerate(((x + 9, y + 12), (x + 18, y + 8), (x + 14, y + 20))): d.cercle(a, b, 1.8, ep=0.4, fond=(1, 1, 1)); d.texte(a, b + 1, str(i + 1), 5.5, police='Arial-B')
        for i in range(3): d.texte(x + 27, y + 8.5 + i * 6.5, str(i + 1), 7, police='Arial-B'); ligne(x + 30, y + 8.7 + i * 6.5, l - 33)

def panorama_exercices(base, dpi=150):
    """Image A4 paysage qui présente les gabarits d'exercice G1 à G23 : à afficher avant de composer une fiche, ou
    quand on demande quels exercices sont possibles. Écrit base.svg, base.pdf et base.png ; renvoie le chemin du PNG."""
    L, H, m, col, ran = 297, 210, 8, 6, 4; l, h = (L - 2 * m) / col, (H - 2 * m) / ran; d = Dessin(L, H)
    d.texte(m + l / 2, m + 16, 'Exercices', 16, police='Arial-B'); d.texte(m + l / 2, m + 23, 'les gabarits disponibles', 10)
    d.texte(m + l / 2, m + 33, 'Dites le nom', 9); d.texte(m + l / 2, m + 37.5, 'de l’exercice choisi.', 9)
    for i, (code, nom) in enumerate(EXERCICES, 1):
        x, y = m + (i % col) * l, m + (i // col) * h
        d.ligne([(x + 1.5, y + 1.5), (x + l - 1.5, y + 1.5), (x + l - 1.5, y + h - 1.5), (x + 1.5, y + h - 1.5)], ep=0.3, ferme=True)
        _vignette_exercice(d, code, x + 4, y + 4, l - 8, 27)
        d.texte(x + l / 2, y + 39, nom, 8.4, police='Arial-B')                  # nom seul, sans code (21.11.2026)
        assert d.largeur_texte(nom, 8.4, 'Arial-B') <= l - 6, code
    d.sauver(base)
    return d.png(base, dpi)
```

#### 19 novembre 2026 : dé à monter, grand ou petit (J6)

`de_a_monter` dessine le patron du dé avec la classe `Dessin` (R11) : croix de six faces, sept languettes de collage, contour en pointillés, plis en trait fin, textes centrés. `format='grand'` donne un dé à faces de 6 cm, seul sur la page ; `format='petit'`, deux dés à faces de 4,2 cm. Un texte trop large fait diminuer le corps jusqu'à 14 pt, puis le patron est refusé. Le bloc se place avant `VARIANTES`, qui l'utilise pour les miniatures.

**Test (19.11.2026)** : grand dé et petit dé produits en PDF et regardés (chiffres, puis pronoms sur une ou deux lignes) ; police Liberation Sans à la place d'Arial ; non imprimé, montage non réalisé.

```
# ---------- J6 : dé à monter, grand (un par page) ou petit (deux par page) (19.11.2026) ----------
def de_a_monter(base, faces=('1', '2', '3', '4', '5', '6'), format='grand', taille_pt=None, mention=True, dessin=None):
    """J6 : patron de cube en croix, avec languettes de collage, sur une page A4 portrait.
    format = 'grand' : faces de 6 cm, un dé par page (patron de 18 × 24,9 cm) ;
             'petit' : faces de 4,2 cm, deux dés identiques par page (patrons couchés de 17,5 × 12,6 cm).
    faces : six textes courts (haut de la colonne, bras gauche, centre, bras droit, puis les deux faces du bas).
    Contour à découper en pointillés (MP-J-05), plis en trait fin ; le texte est centré, son corps diminue
    s'il est trop large (minimum 14 pt). Écrit base.svg et base.pdf ; renvoie (chemin du PDF, côté d'une
    face en cm, nombre de dés sur la page)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); grand = format == 'grand'
    c, lang = (60.0, 9.0) if grand else (42.0, 7.0); assert len(faces) == 6, 'un dé a six faces'
    croix = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
    languettes = {((1, 0), 'haut'), ((1, 0), 'gauche'), ((1, 0), 'droite'), ((1, 2), 'gauche'), ((1, 2), 'droite'),
                  ((1, 3), 'gauche'), ((1, 3), 'droite')}
    cotes = {'haut': ((0, 0), (1, 0), (0, -1)), 'bas': ((0, 1), (1, 1), (0, 1)),
             'gauche': ((0, 0), (0, 1), (-1, 0)), 'droite': ((1, 0), (1, 1), (1, 0))}
    if not grand:                                                           # patron couché : colonnes et rangées échangées
        croix = [(r, q) for q, r in croix]; tourne = {'haut': 'gauche', 'gauche': 'haut', 'droite': 'bas', 'bas': 'droite'}
        languettes = {((r, q), tourne[s]) for (q, r), s in languettes}
    corps = taille_pt or (48 if grand else 30)
    while max(d.largeur_texte(t, corps, 'Arial-B') for f in faces for t in f.split('\n')) > c - 8:
        corps -= 1; assert corps >= 14, 'texte trop long pour une face du dé'
    origines = ([(x0 + (L - 3 * c) / 2, y0 + (H - 4 * c - lang) / 2 + lang)] if grand else
                [(x0 + (L - 4 * c - lang) / 2 + lang, y0 + (H - 6 * c - 8) / 2 + k * (3 * c + 8)) for k in range(2)])
    for ox, oy in origines:
        for i, (q, r) in enumerate(croix):
            X, Y = ox + q * c, oy + r * c
            for nom, (a, b, n) in cotes.items():
                P, Q = (X + a[0] * c, Y + a[1] * c), (X + b[0] * c, Y + b[1] * c)
                if (q + n[0], r + n[1]) in croix:
                    d.ligne([P, Q], ep=0.25)                                 # pli entre deux faces
                elif ((q, r), nom) in languettes:
                    u = ((Q[0] - P[0]) / c, (Q[1] - P[1]) / c); d.ligne([P, Q], ep=0.25)
                    d.ligne([P, (P[0] + n[0] * lang + u[0] * lang, P[1] + n[1] * lang + u[1] * lang),
                             (Q[0] + n[0] * lang - u[0] * lang, Q[1] + n[1] * lang - u[1] * lang), Q], ep=0.35, tirets=(1, 1.2))
                else:
                    d.ligne([P, Q], ep=0.35, tirets=(1, 1.2))                # bord à découper
            lignes = faces[i].split('\n'); pas = corps * 1.2 * 25.4 / 72
            for j, t in enumerate(lignes):
                d.texte(X + c / 2, Y + c / 2 - (len(lignes) - 1) * pas / 2 + corps * 0.125 + j * pas, t, corps, police='Arial-B')
    if mention:
        d.texte(105, 8.0, 'Dé à monter · découper sur les pointillés · plier sur les traits fins · coller les languettes', 8)
    return (None if dessin else d.sauver(base)), c / 10, len(origines)
```

#### 19 novembre 2026 : variantes par tranche d'âge et miniatures des formats

`VARIANTES` donne, pour chaque gabarit de jeu et chaque tranche d'âge (1 : 1P à 4P ; 2 : 5P à 8P ; 3 : 9S à 11S), le format de la planche : colonnes, rangées et corps du texte, ou les paramètres du plateau. Depuis le 20.11.2026, les pages de miniatures par tranche d'âge ne sont plus dessinées ici : `miniatures_tranche` (bloc MP-J-13) les compose à partir des pages réelles des documents. Le bloc se place après `JEUX`.

**Test (19.11.2026)** : douze plateaux J5 produits en pleine page (quatre formes, trois tranches) ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- Variantes des jeux par tranche d'âge et miniatures des formats (19.11.2026) ----------
TRANCHES = {1: '1P à 4P (cycle 1, 4 à 8 ans)', 2: '5P à 8P (cycle 2, 8 à 12 ans)', 3: '9S à 11S (cycle 3, 12 à 15 ans)'}
# Par gabarit : une entrée par tranche (None : gabarit non proposé à cet âge).
# planche : (colonnes, rangées, corps en pt) ; plateau : paramètres de plateau_parcours ; autres : paramètres de la fonction du gabarit.
VARIANTES = {
    'J1': ('planche', 'dominos', {1: (2, 5, 26), 2: (2, 8, 18), 3: (2, 10, 14)}),
    'J2': ('planche', 'cartes', {1: (2, 3, 40), 2: (3, 4, 22), 3: (4, 5, 14)}),
    'J3': ('planche', 'cartes', {1: (2, 3, 24), 2: (3, 3, 16), 3: (4, 4, 12)}),
    'J4': ('planche', 'cartes', {1: (2, 3, 28), 2: (2, 4, 18), 3: (3, 5, 14)}),
    'J5-a': ('plateau', 'cases', {1: dict(forme='serpent', colonnes=4, rangees=7, taille_pt=32),
                                  2: dict(forme='serpent'),
                                  3: dict(forme='serpent', colonnes=8, rangees=11, taille_pt=16, case_min_mm=20)}),
    'J5-b': ('plateau', 'cases', {1: dict(forme='escargot', bande_mm=32, long_mm=42, taille_pt=30),
                                  2: dict(forme='escargot'),
                                  3: dict(forme='escargot', bande_mm=21, long_mm=25, taille_pt=15, case_min_mm=20)}),
    'J5-c': ('plateau', 'cases', {1: dict(forme='chemin', diametre_mm=36, rangs=5, taille_pt=30),
                                  2: dict(forme='chemin'),
                                  3: dict(forme='chemin', diametre_mm=22, rangs=8, taille_pt=16, case_min_mm=20)}),
    'J5-d': ('plateau', 'cases', {1: dict(forme='circuit', colonnes=4, rangees=6, taille_pt=32),
                                  2: dict(forme='circuit'),
                                  3: dict(forme='circuit', colonnes=8, rangees=11, taille_pt=16, case_min_mm=20)}),
    'J6': ('de', 'dés', {1: 'grand', 2: 'petit', 3: 'petit'}),                        # format de de_a_monter
    'J7': ('loto', 'cartons', {1: (2, 3, 2, 2), 2: (2, 4, 3, 2), 3: (2, 3, 3, 3)}),      # cartons c × r, cases a × b
    'J8': ('symboles', 'cartes', {1: (2, 4, 7, 3), 2: (3, 5, 13, 4), 3: (3, 7, 21, 5)}),  # c, r, cartes, éléments
    'J9': ('grille', 'cases', {1: (2, 3), 2: (4, 4), 3: (5, 5)}),
    'J10': ('pinces', 'questions', {1: 6, 2: 10, 3: 12}),
    'J11': ('roue', 'secteurs', {1: 4, 2: 6, 3: 8}),
    'J12': ('planche', 'plaques', {1: (2, 2, 130), 2: None, 3: None}),
    'J13': ('planche', 'cartes', {1: (2, 2, 28), 2: (2, 4, 16), 3: (2, 4, 14)}),
    'J14': ('planche', 'cartes', {1: None, 2: (2, 2, 16), 3: (2, 3, 14)}),
    'J15': ('planche', 'cartes', {1: (2, 2, 28), 2: (2, 4, 16), 3: (2, 4, 14)}),
    'J16': ('planche', 'cartons', {1: (2, 2, 110), 2: (2, 2, 110), 3: (2, 3, 90)}),
    'J17': ('alignement', 'ronds', {1: dict(colonnes=4, rangees=5, aligner=3, taille_pt=28), 2: dict(colonnes=5, rangees=7, aligner=4),
                                    3: dict(colonnes=6, rangees=8, aligner=4, taille_pt=15)}),
    'J18': ('echelles', 'cases', {1: dict(colonnes=5, rangees=6, taille_pt=20), 2: dict(colonnes=6, rangees=8),
                                  3: dict(colonnes=8, rangees=10, taille_pt=11, case_min_mm=20)}),
    'J19': ('navale', 'cases par grille', {1: dict(taille=5), 2: dict(taille=6), 3: dict(taille=8)}),
    'J20': ('tirage', 'secteurs', {1: 4, 2: 6, 3: 8}),
    'J21': ('association', 'puzzles', {1: dict(colonnes=2, rangees=4, taille_pt=28), 2: dict(colonnes=2, rangees=6, taille_pt=20),
                                       3: dict(colonnes=3, rangees=6, taille_pt=14)}),
    'J22': ('bandes', 'bandes', {1: 5, 2: 10, 3: 12}),
    'J23': ('mystere', 'mots', {1: 4, 2: 6, 3: 8}),
    'J24': ('cocotte', 'défis', {1: dict(taille_pt=14), 2: dict(taille_pt=12), 3: dict(taille_pt=12)}),
    'J25': ('horloge', 'graduations', {1: dict(), 2: dict(minutes=True), 3: dict(minutes=True, heures_24=True)}),
    'J26': ('eventail', 'fiches', {1: dict(colonnes=3, taille_pt=22), 2: dict(colonnes=4, taille_pt=15), 3: dict(colonnes=5, taille_pt=12)}),
    'J27': ('graphisme', 'bandes', {1: ('traits', 'zigzag', 'vagues', 'ponts'), 2: ('zigzag', 'vagues', 'ponts', 'coupes', 'creneaux', 'boucles'),
                                    3: ('traits', 'zigzag', 'vagues', 'ponts', 'creneaux', 'boucles', 'spirales', 'coupes')}),
    'J28': ('camemberts', 'cases', {1: dict(entre=3, rayon=2), 2: dict(entre=4, rayon=3), 3: dict(entre=6, rayon=5)}),
    'J29': ('lynx', 'mots', {1: dict(taille_pt=24), 2: dict(taille_pt=16), 3: dict(taille_pt=13)}),
    'J30': ('interdits', 'cartes', {1: None, 2: dict(colonnes=3, rangees=3, taille_pt=16), 3: dict(colonnes=3, rangees=4, taille_pt=13)}),
    'J31': ('bac', 'cases à remplir', {1: dict(manches=4, taille_pt=14), 2: dict(manches=6), 3: dict(manches=8, taille_pt=11)}),
    'J32': ('terminaisons', 'cartes-phrases', {1: None, 2: (2, 6, 16), 3: None}),
    'J33': ('chevaux', 'cases', {1: dict(), 2: dict(), 3: dict()}),
    'J34': ('qui', 'éléments', {1: dict(colonnes=3, taille_pt=40), 2: dict(colonnes=4, taille_pt=30), 3: dict(colonnes=5, taille_pt=22)}),
    'J35': ('planche', 'cartes', {1: (3, 4, 30), 2: (4, 4, 24), 3: (4, 5, 22)}),
    'J36': ('tuiles', 'tuiles', {1: dict(colonnes=6, rangees=8), 2: dict(colonnes=9, rangees=13), 3: dict(colonnes=12, rangees=17)}),
    'J37': ('sudoku', 'grilles', {1: dict(taille=4, grilles=4), 2: dict(taille=6, grilles=2), 3: dict(taille=9, grilles=2)}),
    'J38': ('fleur', 'parties', {1: dict(parties=3), 2: dict(parties=3), 3: dict(parties=3)})}
```

#### 19 novembre 2026 : dos à motif des cartes tirées (MP-J-14)

`dos_a_motif` dessine avec la classe `Dessin` (R11) le verso d'une planche de cartes tirées, à la manière d'un dos de carte à jouer : sur chaque carte, des lignes fines (losanges, carreaux ou vagues, pas de 2 mm, trait de 0,2 mm) remplissent un cadre aux angles arrondis, tracé à 3 mm du bord ; la marge reste blanche. `colonnes` et `rangees` reprennent ceux du recto. Le paramètre `texte` ajoute au centre de chaque carte une mention personnelle (nom du jeu, catégorie) dans un cartouche gris. La page s'imprime au verso de la planche, retournement sur le bord long ; le cadre rend visible un décalage, d'où l'essai d'impression. Pour un dos blanc, la fonction n'est pas appelée. Le bloc se place après `planche_pdf`, dont il reprend `SURFACE_MM`, et après `arc_pts`.

**Test du liseré (21.11.2026)** : `lisere_cartes` appelé par `planche_pdf`, `cartes_categories` et `cartes_mots_interdits` ; planches J30, J32 et J35 produites en noir et blanc et en couleur et regardées : cadre à 3 mm du trait de coupe, texte à l'intérieur ; police Liberation Sans à la place d'Arial ; non imprimé.

**Test (19.11.2026)** : trois motifs encadrés produits et regardés sur une planche de 3 × 4 cartes, puis un dos à mention « Bonus » ; planches de 2 × 3 et de 4 × 5 cartes produites ; mention trop longue refusée ; couverture d'encre mesurée sur l'image : 18 % (losanges, carreaux), 11 % (vagues) ; opacité réelle sur papier et alignement recto-verso : non testés à l'impression.

```
# ---------- MP-J-14 : dos des cartes tirées, motif encadré et mention facultative (19.11.2026) ----------
def dos_a_motif(base, motif='losanges', colonnes=3, rangees=4, texte=None, taille_pt=14, marge_mm=3.0, rayon_mm=3.0,
                pas_mm=2.0, ep=0.2, dpi=300):
    """MP-J-14 : verso d'une planche de cartes tirées (cartes-défis, memory, cartes d'appel), comme le dos d'une
    carte à jouer : sur chaque carte, un motif de lignes fines dans un cadre aux angles arrondis, à 3 mm du bord,
    la marge restant blanche. colonnes et rangees : ceux du recto. Le motif est le même sur toutes les cartes.
    motif = 'losanges' (deux séries d'obliques), 'carreaux' (quadrillage) ou 'vagues' (lignes ondulées) :
    un motif par jeu, pour trier des jeux mélangés.
    texte : mention facultative, la même au dos de chaque carte de la planche : nom du jeu ou catégorie de cartes
    (« Défi », « Bonus », « Malus », « Chance »), en gras dans un cartouche gris au centre de la carte ;
    jamais un texte qui distingue deux cartes d'une même pile.
    Le cadre rend visible un décalage du recto-verso : faire un essai d'impression (V13).
    Écrit base.svg, base.pdf et base.png ; renvoie le PDF."""
    x0, y0, L, H = SURFACE_MM; d = Dessin(); l, h = L / colonnes, H / rangees; r = rayon_mm; d.trait = couleur_trait()
    assert motif in ('losanges', 'carreaux', 'vagues'), motif
    if texte:
        lt = d.largeur_texte(texte, taille_pt, 'Arial-B'); ht = taille_pt * 25.4 / 72
        assert lt + 6 <= l - 2 * marge_mm - 4, 'texte trop long pour le dos de la carte'
    for i in range(colonnes * rangees):
        xa, ya = x0 + (i % colonnes) * l + marge_mm, y0 + (i // colonnes) * h + marge_mm
        xb, yb = xa + l - 2 * marge_mm, ya + h - 2 * marge_mm
        def dedans(x, y):                                                   # dans le cadre aux angles arrondis
            if not (xa <= x <= xb and ya <= y <= yb): return False
            cx = xa + r if x < xa + r else (xb - r if x > xb - r else x)
            cy = ya + r if y < ya + r else (yb - r if y > yb - r else y)
            return math.hypot(x - cx, y - cy) <= r + 1e-6
        def trace(pts):                                                     # ne garde que la partie située dans le cadre
            suite = []
            for p in pts:
                if dedans(*p): suite.append(p)
                else:
                    if len(suite) > 1: d.ligne(suite, ep=ep)
                    suite = []
            if len(suite) > 1: d.ligne(suite, ep=ep)
        def segment(a, b):
            n = max(2, int(math.hypot(b[0] - a[0], b[1] - a[1]) / 0.3))
            pts = [(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n) for k in range(n + 1)]
            ok = [p for p in pts if dedans(*p)]
            if len(ok) > 1: d.ligne([ok[0], ok[-1]], ep=ep)
        if motif == 'carreaux':
            for k in range(1, int((xb - xa) / pas_mm) + 1): segment((xa + k * pas_mm, ya), (xa + k * pas_mm, yb))
            for k in range(1, int((yb - ya) / pas_mm) + 1): segment((xa, ya + k * pas_mm), (xb, ya + k * pas_mm))
        elif motif == 'losanges':
            q = pas_mm * math.sqrt(2); cx, cy = (xa + xb) / 2, (ya + yb) / 2; m = int((xb - xa + yb - ya) / q) + 1
            for k in range(-m, m + 1):
                c = cx - cy + k * q; x1, x2 = max(xa, ya + c), min(xb, yb + c)        # obliques x - y = c
                if x1 < x2: segment((x1, x1 - c), (x2, x2 - c))
                c = cx + cy + k * q; x1, x2 = max(xa, c - yb), min(xb, c - ya)        # obliques x + y = c
                if x1 < x2: segment((x1, c - x1), (x2, c - x2))
        else:
            n = int((xb - xa) / (pas_mm / 4))
            for k in range(int((yb - ya) / pas_mm)):
                y = ya + (k + 0.5) * pas_mm
                trace([(xa + (xb - xa) * j / n, y + pas_mm * 0.35 * math.sin(math.pi * j / 8 + k * math.pi)) for j in range(n + 1)])
        cadre = (arc_pts(xb - r, ya + r, r, 0, 90, 8) + arc_pts(xb - r, yb - r, r, 90, 180, 8) +
                 arc_pts(xa + r, yb - r, r, 180, 270, 8) + arc_pts(xa + r, ya + r, r, 270, 360, 8))
        d.ligne(cadre, ep=0.3, ferme=True)
        if texte:
            cx, cy = (xa + xb) / 2, (ya + yb) / 2
            d.ligne([(cx - lt / 2 - 3, cy - ht / 2 - 2), (cx + lt / 2 + 3, cy - ht / 2 - 2), (cx + lt / 2 + 3, cy + ht / 2 + 2),
                     (cx - lt / 2 - 3, cy + ht / 2 + 2)], ep=0.3, ferme=True, fond=(0.85, 0.85, 0.85))
            d.texte(cx, cy + taille_pt * 0.125, texte, taille_pt, police='Arial-B')
    d.png(base, dpi)
    return d.sauver(base)

def lisere_cartes(d, colonnes, rangees, marge_mm=3.0, rayon_mm=3.5, ep=0.44):
    """MP-J-14 : liseré de chaque carte d'une planche de colonnes × rangees cartes (SURFACE_MM), comme sur une carte
    à jouer : cadre aux coins arrondis à marge_mm du trait de coupe, trait de 1,25 pt ; en couleur (definir_couleur),
    l'intérieur du cadre est teinté et la marge reste blanche. À appeler AVANT de tracer le contenu des cartes,
    qui reste à l'intérieur du cadre (au moins 2 mm de jeu)."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees; r = rayon_mm
    garde = d.trait
    if COULEUR[0] is not None and tuple(d.trait) == (0, 0, 0): d.trait = couleur_trait()
    fond = _teinter((0.93, 0.93, 0.93)) if COULEUR[0] is not None else None
    for i in range(colonnes * rangees):
        xa, ya = x0 + (i % colonnes) * l + marge_mm, y0 + (i // colonnes) * h + marge_mm
        xb, yb = xa + l - 2 * marge_mm, ya + h - 2 * marge_mm
        d.ligne(arc_pts(xb - r, ya + r, r, 0, 90, 8) + arc_pts(xb - r, yb - r, r, 90, 180, 8) +
                arc_pts(xa + r, yb - r, r, 180, 270, 8) + arc_pts(xa + r, ya + r, r, 270, 360, 8), ep=ep, ferme=True, fond=fond)
    d.trait = garde
```

#### 19 novembre 2026 : grille d'alignement, serpents et échelles, bataille navale, roue de tirage (J17 à J20)

Quatre fonctions dessinent avec la classe `Dessin` (R11) les plateaux des gabarits J17 à J20, sur toute la surface utile de la page : `grille_alignement`, `serpents_echelles`, `bataille_navale` et `roue_tirage`. Elles partagent un bandeau de titre arrondi (`_bandeau`, `_cadre_arrondi`), renvoient le chemin du PDF, le nombre de ronds, de cases ou de secteurs et la dimension utile, et acceptent le paramètre `dessin` pour les miniatures. Le bloc se place après `Dessin`, `arc_pts` et `SURFACE_MM`.

**Test (19.11.2026)** : douze planches produites et regardées sur le rendu PDF (quatre gabarits, trois tranches d'âge) ; serpents et échelles tirés au sort sans croisement sur les trois formats ; un texte trop long pour un rond ou pour un secteur est refusé ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J17 à J20 : grille d'alignement, serpents et échelles, bataille navale, roue de tirage (19.11.2026) ----------
def _cadre_arrondi(d, x, y, l, h, r=6.0, ep=1.2, fond=None):
    """Rectangle aux angles arrondis (cadre de plateau, bandeau de titre)."""
    d.ligne(arc_pts(x + l - r, y + r, r, 0, 90, 8) + arc_pts(x + l - r, y + h - r, r, 90, 180, 8) +
            arc_pts(x + r, y + h - r, r, 180, 270, 8) + arc_pts(x + r, y + r, r, 270, 360, 8), ep=ep, ferme=True, fond=fond)

def _bandeau(d, titre, consigne, haut=20.0):
    """Bandeau de titre d'un plateau : cadre gris arrondi, titre en gras, consigne pour les élèves. Renvoie sa hauteur.
    Pour des non-lecteurs (definir_jeunes), la consigne n'est pas écrite : passer consigne=None et montrer un exemple."""
    x0, y0, L, H = SURFACE_MM
    _cadre_arrondi(d, x0, y0, L, haut - 4, r=5, ep=0.8, fond=(0.9, 0.9, 0.9))
    d.texte(x0 + 6, y0 + 7.5, titre, 17, ancre='s', police='Arial-B')
    if consigne: d.texte(x0 + 6, y0 + 13.2, consigne, 10, ancre='s')
    return haut

def grille_alignement(base, valeurs=None, colonnes=5, rangees=7, aligner=4, titre=None, taille_pt=20, dessin=None):
    """J17 : grille d'alignement (principe du « quatre à la suite »). Chaque rond porte une réponse ; l'élève tire une
    question, trouve la réponse sur la grille et la couvre d'un jeton de sa couleur ; le premier qui aligne `aligner`
    jetons gagne. valeurs : colonnes × rangees réponses (par défaut les nombres de 1 à n).
    Renvoie (chemin du PDF, nombre de ronds, diamètre d'un rond en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees
    valeurs = [str(v) for v in (valeurs or range(1, n + 1))]; assert len(valeurs) == n, 'une réponse par rond'
    haut = _bandeau(d, titre or f'Aligne {aligner} !', f'Réponds, puis pose ton jeton sur la réponse. Aligne {aligner} jetons : en ligne, en colonne ou en diagonale.')
    _cadre_arrondi(d, x0, y0 + haut, L, H - haut, r=9, ep=1.4); _cadre_arrondi(d, x0 + 1.8, y0 + haut + 1.8, L - 3.6, H - haut - 3.6, r=7.5, ep=0.35)
    l, h = (L - 10) / colonnes, (H - haut - 10) / rangees; r = min(l, h) * 0.44
    for i, v in enumerate(valeurs):
        cx, cy = x0 + 5 + (i % colonnes + 0.5) * l, y0 + haut + 5 + (i // colonnes + 0.5) * h
        d.cercle(cx, cy, r, ep=1.0, fond=(1, 1, 1)); d.cercle(cx, cy, r - 1.4, ep=0.3)
        t = taille_pt
        while d.largeur_texte(v, t, 'Arial-B') > 2 * r - 6: t -= 1; assert t >= 9, f'réponse trop longue pour un rond : {v!r}'
        d.texte(cx, cy + t * 0.125, v, t, police='Arial-B')
    assert 2 * r >= 22, 'ronds trop petits pour un jeton'
    return (None if dessin else d.sauver(base)), n, round(2 * r, 1)

def serpents_echelles(base, colonnes=6, rangees=8, liens=None, graine=1, titre='Serpents et échelles', taille_pt=14,
                      case_min_mm=25.0, dessin=None):
    """J18 : plateau de serpents et échelles. Cases numérotées en lacets, du bas à gauche (Départ) jusqu'en haut
    (Arrivée). Une échelle fait monter, un serpent fait redescendre : l'élève ne monte l'échelle, ou n'évite le
    serpent, que s'il répond juste à la carte-défi tirée (le hasard ne décide pas seul).
    liens : couples (case de départ, case d'arrivée) ; arrivée plus grande = échelle, plus petite = serpent ;
    par défaut, tirés au sort avec `graine`. Renvoie (chemin du PDF, nombre de cases, plus petit côté d'une case)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees
    haut = _bandeau(d, titre, 'Échelle : je monte si je réponds juste. Serpent : je redescends si je me trompe.')
    l, h = L / colonnes, (H - haut) / rangees; assert min(l, h) >= case_min_mm, f'cases de {min(l, h):.1f} mm : trop petites'
    def centre(k):                                                          # centre de la case numéro k (1 à n)
        r, q = divmod(k - 1, colonnes); q = q if r % 2 == 0 else colonnes - 1 - q
        return x0 + (q + 0.5) * l, y0 + H - (r + 0.5) * h
    if liens is None:                                                       # tirage : extrémités toutes différentes
        alea = random.Random(graine); liens = []; nb = max(2, n // 16)
        def croise(p, q, u, v):                                             # deux liens se coupent ou se frôlent
            pts = lambda a, b: [(a[0] + (b[0] - a[0]) * t / 12, a[1] + (b[1] - a[1]) * t / 12) for t in range(13)]
            return min(math.hypot(a[0] - b[0], a[1] - b[1]) for a in pts(p, q) for b in pts(u, v)) < 0.95 * max(l, h)
        for sens in (1, -1) * nb:
            for _ in range(400):
                a = alea.randrange(2, n); b = a + sens * alea.randrange(colonnes + 1, 3 * colonnes)
                if not 2 <= b <= n - 1: continue
                p, q = centre(a), centre(b)
                if l * 0.6 < abs(p[0] - q[0]) < l * 2.6 and not any(croise(p, q, centre(u), centre(v)) for u, v in liens):
                    liens.append((a, b)); break
    for k in range(1, n + 1):
        cx, cy = centre(k); r, q = divmod(k - 1, colonnes)
        d.ligne([(cx - l / 2, cy - h / 2), (cx + l / 2, cy - h / 2), (cx + l / 2, cy + h / 2), (cx - l / 2, cy + h / 2)], ep=0.35,
                ferme=True, fond=(0.93, 0.93, 0.93) if (r + round((cx - x0) / l - 0.5)) % 2 else (1, 1, 1))
    for a, b in liens:
        (xa, ya), (xb, yb) = centre(a), centre(b); xa += l * 0.1; xb += l * 0.1; ya += h * 0.14; yb += h * 0.14   # sous les numéros
        lg = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa) / lg, (yb - ya) / lg
        if b > a:                                                           # échelle : deux montants, des barreaux
            e = min(l, h) * 0.13
            for s in (-1, 1): d.ligne([(xa - s * uy * e, ya + s * ux * e), (xb - s * uy * e, yb + s * ux * e)], ep=0.9)
            for j in range(1, int(lg / 6.5)):
                px, py = xa + ux * j * 6.5, ya + uy * j * 6.5; d.ligne([(px - uy * e, py + ux * e), (px + uy * e, py - ux * e)], ep=0.7)
        else:                                                               # serpent : corps ondulant, de la tête (a) à la queue (b)
            m = 80; amp = min(l, h) * 0.26; ondes = max(1.5, round(lg / 34) + 0.5); g, dr = [], []
            for j in range(m + 1):
                t = j / m; o = amp * math.sin(t * ondes * 2 * math.pi) * min(1, t * 5)
                px, py = xa + ux * lg * t - uy * o, ya + uy * lg * t + ux * o; w = 2.5 if t < 0.7 else 2.5 - 2.1 * (t - 0.7) / 0.3
                g.append((px - uy * w, py + ux * w)); dr.append((px + uy * w, py - ux * w))
            d.ligne(g + dr[::-1], ep=0.5, ferme=True, fond=(0.72, 0.72, 0.72))
            d.cercle(xa, ya, 3.6, ep=0.6, fond=(0.72, 0.72, 0.72)); d.cercle(xa - ux * 1.2 - uy * 1.3, ya - uy * 1.2 + ux * 1.3, 0.6, ep=0, fond=(0, 0, 0))
            d.cercle(xa - ux * 1.2 + uy * 1.3, ya - uy * 1.2 - ux * 1.3, 0.6, ep=0, fond=(0, 0, 0))
            d.ligne([(xa - ux * 3.6, ya - uy * 3.6), (xa - ux * 6, ya - uy * 6), (xa - ux * 7.2 - uy * 1, ya - uy * 7.2 + ux * 1)], ep=0.4)
            d.ligne([(xa - ux * 6, ya - uy * 6), (xa - ux * 7.2 + uy * 1, ya - uy * 7.2 - ux * 1)], ep=0.4)
    for k in range(1, n + 1):                                               # numéros par-dessus, dans le coin de la case
        cx, cy = centre(k); mot = 'Départ' if k == 1 else ('Arrivée' if k == n else str(k)); t = taille_pt if mot.isdigit() else max(taille_pt * 0.95, 10)
        r, lm = divmod(k - 1, colonnes), d.largeur_texte(mot, t, 'Arial-B'); xg, yh = cx - l / 2 + 0.5, cy - h / 2 + 0.5
        d.ligne([(xg, yh), (xg + lm + 2.6, yh), (xg + lm + 2.6, yh + t * 0.36 + 2.4), (xg, yh + t * 0.36 + 2.4)], ep=0, ferme=True,
                fond=(0.93, 0.93, 0.93) if (r[0] + round((cx - x0) / l - 0.5)) % 2 else (1, 1, 1))   # pastille : le numéro reste lisible
        d.texte(cx - l / 2 + 1.8, cy - h / 2 + 1.5 + t * 0.36, mot, t, ancre='s', police='Arial-B')
    d.ligne([(x0, y0 + haut), (x0 + L, y0 + haut), (x0 + L, y0 + H), (x0, y0 + H)], ep=1.4, ferme=True)
    return (None if dessin else d.sauver(base)), n, round(min(l, h), 1)

def bataille_navale(base, en_colonnes=None, en_lignes=None, taille=6, titre='Bataille navale', taille_pt=12, dessin=None):
    """J19 : fiche de bataille navale pour un joueur : en haut « Ma flotte » (il y dessine ses bateaux), en bas
    « Mes tirs » (il y note ses essais). Pour tirer sur une case, l'élève dit la réponse formée par la colonne et la
    ligne (par exemple un sujet et un verbe : la forme conjuguée ; deux nombres : leur produit).
    en_colonnes, en_lignes : intitulés des colonnes et des lignes (par défaut A, B, C… et 1, 2, 3…).
    Renvoie (chemin du PDF, nombre de cases par grille, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin()
    en_colonnes = list(en_colonnes or 'ABCDEFGHIJ'[:taille]); en_lignes = [str(v) for v in (en_lignes or range(1, taille + 1))]
    c, r = len(en_colonnes), len(en_lignes)
    haut = _bandeau(d, titre, 'Dis la réponse de la case pour tirer. Touché : une croix. Dans l’eau : un point.')
    marge = max(d.largeur_texte(t, taille_pt, 'Arial-B') for t in en_lignes) + 6; bloc = (H - haut) / 2
    cl, ch = (L - marge) / c, (bloc - 24) / r; gx = x0 + marge; cote = min(cl, ch)
    for k, nom in enumerate(('Ma flotte', 'Mes tirs')):
        gy = y0 + haut + k * bloc + 19; lt = d.largeur_texte(nom, 14, 'Arial-B'); fin = x0 + L - (34 if k == 0 else 0)
        d.texte(x0, gy - 12, nom, 14, ancre='s', police='Arial-B')
        d.ligne([(x0 + lt + 4 + 0.5 * j, gy - 13.5 + 1.2 * math.sin(j * 0.55)) for j in range(int((fin - x0 - lt - 6) * 2))], ep=0.35)
        if k == 0:                                                          # la flotte à dessiner : trois coques arrondies
            for q, cases in enumerate((3, 2, 1)): _cadre_arrondi(d, x0 + L - 31 + (0, 16, 27)[q], gy - 16, cases * 4.5 - 0.5, 4.5, r=2, ep=0.6, fond=(0.8, 0.8, 0.8))
        for i, t in enumerate(en_colonnes):
            s = taille_pt
            while d.largeur_texte(t, s, 'Arial-B') > cl - 2: s -= 0.5; assert s >= 7, f'intitulé trop long : {t!r}'
            d.texte(gx + (i + 0.5) * cl, gy - 2.5, t, s, police='Arial-B')
        for j, t in enumerate(en_lignes): d.texte(gx - 3 - d.largeur_texte(t, taille_pt, 'Arial-B') / 2, gy + (j + 0.5) * ch + taille_pt * 0.125, t, taille_pt, police='Arial-B')
        for i in range(c + 1): d.ligne([(gx + i * cl, gy), (gx + i * cl, gy + r * ch)], ep=1.2 if i in (0, c) else 0.35)
        for j in range(r + 1): d.ligne([(gx, gy + j * ch), (gx + c * cl, gy + j * ch)], ep=1.2 if j in (0, r) else 0.35)
    assert cote >= 12, 'cases trop petites'
    return (None if dessin else d.sauver(base)), c * r, round(cote, 1)

def roue_tirage(base, secteurs=('1', '2', '3', '4', '5', '6'), titre='Roue de tirage', taille_pt=24, dessin=None):
    """J20 : roue de tirage à faire tourner avec un trombone tenu par la pointe d'un crayon : elle remplace le dé
    et tire un mot, un nombre ou une consigne. secteurs : 3 à 12 textes courts.
    Renvoie (chemin du PDF, nombre de secteurs, diamètre de la roue en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(secteurs); assert 3 <= n <= 12, 'de 3 à 12 secteurs'
    haut = _bandeau(d, titre, 'Pose un trombone au centre, tiens-le avec la pointe d’un crayon, puis fais-le tourner.')
    R = min(L, H - haut - 40) / 2 - 2; cx, cy = x0 + L / 2, y0 + haut + 6 + R
    for k, t in enumerate(secteurs):
        a0, a1 = 360 * k / n, 360 * (k + 1) / n
        d.ligne(arc_pts(cx, cy, R, a0, a1, 24) + [(cx, cy)], ep=0.6, ferme=True, fond=(0.88, 0.88, 0.88) if k % 2 and n % 2 == 0 else (1, 1, 1))
        am = math.radians((a0 + a1) / 2); px, py = cx + 0.62 * R * math.sin(am), cy - 0.62 * R * math.cos(am); s = taille_pt
        large = 2 * 0.62 * R * math.sin(math.pi / n) - 6
        for j, ligne in enumerate(t.split('\n')):
            while d.largeur_texte(ligne, s, 'Arial-B') > large: s -= 1; assert s >= 10, f'texte trop long pour un secteur : {ligne!r}'
        lignes = t.split('\n'); pas = s * 1.2 * 25.4 / 72
        for j, ligne in enumerate(lignes): d.texte(px, py - (len(lignes) - 1) * pas / 2 + s * 0.125 + j * pas, ligne, s, police='Arial-B')
    d.cercle(cx, cy, R, ep=1.4); d.cercle(cx, cy, R + 2, ep=0.35); d.cercle(cx, cy, 5, ep=0.8, fond=(1, 1, 1)); d.cercle(cx, cy, 1, ep=0, fond=(0, 0, 0))
    by = cy + R + 12; cases = 10; cb = (y0 + H - by - 8 - 2) / 2; d.texte(x0, by + 4, 'Mes tirages', 12, ancre='s', police='Arial-B')
    for k in range(2 * cases):                                              # vingt cases pour noter les tirages
        _cadre_arrondi(d, x0 + (k % cases) * (L / cases) + 1, by + 8 + (k // cases) * (cb + 2), L / cases - 2, cb, r=2.5, ep=0.5)
    return (None if dessin else d.sauver(base)), n, round(2 * R, 1)
```

#### 20 novembre 2026 : puzzles, mot mystère, cocotte, horloge, éventail, bandes graphiques (J21 à J27)

Sept fonctions dessinent avec la classe `Dessin` (R11) les gabarits J21 à J27 : `puzzle_association`, `puzzle_bandes`, `mot_mystere`, `cocotte`, `horloge`, `eventail` et `bandes_graphiques`. Les planches à découper occupent toute la surface utile et portent les repères de coupe (`reperes_de_coupe`). Chaque fonction renvoie le chemin du PDF, le nombre de pièces et la dimension utile. Le bloc se place après `Dessin`, `arc_pts`, `SURFACE_MM`, `reperes_de_coupe` et `_bandeau`.

**Test (20.11.2026)** : vingt et une planches produites et regardées sur le rendu PDF (sept gabarits, trois tranches d'âge) ; un texte trop long est refusé ; `mot_mystere` refuse un mot qui ne contient pas la lettre attendue ; police Liberation Sans à la place d'Arial ; non imprimé ; pliage de la cocotte, emboîtement des puzzles et montage de l'horloge non essayés.

```
# ---------- J21 à J27 : puzzles, mot mystère, cocotte, horloge, éventail, bandes graphiques (20.11.2026) ----------
def _mention(d, texte):
    """Mention d'une planche à découper, dans la marge du haut."""
    assert d.largeur_texte(texte, 8) <= SURFACE_MM[2] - 10, 'mention trop longue'; d.texte(105, 8.0, texte, 8)

def _texte_ajuste(d, x, y, t, taille_pt, large, police='Arial', mini=8):
    """Écrit t centré en (x, y) ; réduit le corps jusqu'à ce que le texte tienne dans large (mm) ; refuse sous mini."""
    while d.largeur_texte(t, taille_pt, police) > large: taille_pt -= 0.5; assert taille_pt >= mini, f'texte trop long : {t!r}'
    d.texte(x, y + taille_pt * 0.125, t, taille_pt, police=police); return taille_pt

def puzzle_association(base, paires, colonnes=2, rangees=6, taille_pt=18, mention='', dessin=None):
    """J21 : puzzles à deux pièces. paires : [(gauche, droite)], par exemple (mot, définition) ou (calcul, résultat).
    Chaque puzzle est coupé par une ligne d'une forme différente : seules les deux bonnes pièces s'emboîtent
    (autocorrection par la découpe, 18 formes). Renvoie (chemin du PDF, nombre de puzzles, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(paires) <= min(colonnes * rangees, 18), 'trop de paires (18 formes de coupe au plus)'
    for i, (g, dr) in enumerate(paires):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; xm = x + l / 2; a = min(l * 0.09, h * 0.2)
        cy = y + h * (0.3, 0.5, 0.7)[i % 3]; s = 1 if (i // 3) % 2 == 0 else -1; forme = (i // 6) % 3
        if forme == 0: dent = [(xm, cy - a), (xm + s * a, cy), (xm, cy + a)]                          # pointe
        elif forme == 1: dent = [(xm, cy - a), (xm + s * a, cy - a), (xm + s * a, cy + a), (xm, cy + a)]  # créneau
        else: dent = [(xm + s * a * math.sin(math.radians(t)), cy - a * math.cos(math.radians(t))) for t in range(0, 181, 15)]  # demi-rond
        d.ligne([(xm, y)] + dent + [(xm, y + h)], ep=0.6)
        for k, t in enumerate((g, dr)):
            lignes = t.split('\n'); c = taille_pt; cx = x + l * (0.25 + 0.5 * k)
            while max(d.largeur_texte(z, c, 'Arial-B' if k == 0 else 'Arial') for z in lignes) > l / 2 - a - 5: c -= 0.5; assert c >= 9, f'texte trop long : {t!r}'
            pas = c * 1.25 * 25.4 / 72
            for j, z in enumerate(lignes): d.texte(cx, y + h / 2 - (len(lignes) - 1) * pas / 2 + c * 0.125 + j * pas, z, c, police='Arial-B' if k == 0 else 'Arial')
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(paires), (round(l / 10, 2), round(h / 10, 2))

def _scene(d, x, y, l, h):
    """Image par défaut du puzzle à bandes : un paysage au trait (collines, soleil, maison, arbre, nuages)."""
    d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, ferme=True, fond=(0.95, 0.95, 0.95))
    d.cercle(x + l * 0.8, y + h * 0.2, h * 0.09, ep=0.8, fond=(1, 1, 1))
    for k in range(12):
        a = math.radians(k * 30); d.ligne([(x + l * 0.8 + h * 0.11 * math.cos(a), y + h * 0.2 + h * 0.11 * math.sin(a)), (x + l * 0.8 + h * 0.14 * math.cos(a), y + h * 0.2 + h * 0.14 * math.sin(a))], ep=0.6)
    for cx, cy, r in ((0.2, 0.16, 0.05), (0.27, 0.14, 0.065), (0.34, 0.17, 0.05), (0.52, 0.3, 0.04), (0.58, 0.28, 0.05)): d.cercle(x + l * cx, y + h * cy, h * r, ep=0.6, fond=(1, 1, 1))
    for base_y, amp, ph, gris in ((0.62, 0.07, 0.0, 0.8), (0.74, 0.05, 1.7, 0.88)):
        pts = [(x + l * t / 60, y + h * (base_y - amp * math.sin(ph + t / 60 * 2 * math.pi * 1.3))) for t in range(61)]
        d.ligne(pts + [(x + l, y + h), (x, y + h)], ep=0.7, ferme=True, fond=(gris,) * 3)
    mx, my, w = x + l * 0.36, y + h * 0.66, l * 0.2
    d.ligne([(mx, my), (mx + w, my), (mx + w, my + w * 0.7), (mx, my + w * 0.7)], ep=0.8, ferme=True, fond=(1, 1, 1))
    d.ligne([(mx - w * 0.08, my), (mx + w / 2, my - w * 0.45), (mx + w * 1.08, my)], ep=0.8, ferme=True, fond=(0.6, 0.6, 0.6))
    d.ligne([(mx + w * 0.4, my + w * 0.7), (mx + w * 0.4, my + w * 0.3), (mx + w * 0.6, my + w * 0.3), (mx + w * 0.6, my + w * 0.7)], ep=0.6)
    for q in (0.12, 0.72): d.ligne([(mx + w * q, my + w * 0.15), (mx + w * (q + 0.16), my + w * 0.15), (mx + w * (q + 0.16), my + w * 0.33), (mx + w * q, my + w * 0.33)], ep=0.5, ferme=True)
    tx, ty = x + l * 0.13, y + h * 0.78
    d.ligne([(tx - l * 0.012, ty), (tx - l * 0.012, ty - h * 0.14), (tx + l * 0.012, ty - h * 0.14), (tx + l * 0.012, ty)], ep=0.7, ferme=True, fond=(0.5, 0.5, 0.5))
    for cx, cy, r in ((0, -0.2, 0.07), (-0.04, -0.16, 0.05), (0.04, -0.16, 0.05)): d.cercle(tx + l * cx, ty + h * cy, h * r, ep=0.7, fond=(0.75, 0.75, 0.75))

def puzzle_bandes(base, etiquettes, image=None, mention='', taille_pt=28, dessin=None):
    """J22 : puzzle à bandes. Une image est coupée en bandes verticales ; chaque bande porte en bas une étiquette
    (nombre, lettre, mot) : remises dans l'ordre des étiquettes, les bandes reforment l'image (autocorrection).
    etiquettes : dans l'ordre correct, de gauche à droite. image : chemin d'une image (photo, dessin) ; sans image,
    un paysage au trait est dessiné. Renvoie (chemin du PDF, nombre de bandes, largeur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(etiquettes); l = L / n; hi = H - 26
    assert 3 <= n <= 12, 'de 3 à 12 bandes'
    if image and dessin is None: d.p.insert_image(d.f.Rect(x0 * d.k, y0 * d.k, (x0 + L) * d.k, (y0 + hi) * d.k), filename=image, keep_proportion=False)
    else: _scene(d, x0, y0, L, hi)
    d.ligne([(x0, y0 + hi), (x0 + L, y0 + hi)], ep=0.6)
    for i, t in enumerate(etiquettes): _texte_ajuste(d, x0 + (i + 0.5) * l, y0 + hi + 13, str(t), taille_pt, l - 3, 'Arial-B')
    xs = [x0 + i * l for i in range(n + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in (y0, y0 + H): d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, (y0, y0 + H))
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), n, round(l, 1)

def mot_mystere(base, mystere, mots, titre='Le mot mystère', taille_pt=12, dessin=None):
    """J23 : grille de mots à un mot mystère. mots : [(mot, définition)], un par lettre du mot mystère, dans l'ordre ;
    le mot numéro i contient la lettre numéro i du mot mystère. Chaque mot s'écrit sur une ligne ; les lignes sont
    décalées pour que les lettres du mot mystère tombent dans la colonne grisée. Majuscules sans accent.
    Renvoie (chemin du PDF, nombre de mots, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(mystere); assert len(mots) == n, 'un mot par lettre du mot mystère'
    pos = []
    for lettre, (mot, _) in zip(mystere, mots):
        assert mot.isalpha() and mot == mot.upper() and lettre in mot, f'{mot!r} doit contenir {lettre!r}, en majuscules sans accent'
        pos.append(min(range(len(mot)), key=lambda k: (mot[k] != lettre, abs(k - len(mot) / 2))))
    g, dr = max(pos), max(len(m) - p for (m, _), p in zip(mots, pos)); haut = _bandeau(d, titre, 'Écris chaque mot dans sa ligne. Les cases teintées donnent le mot mystère.')
    hd = max(26.0, n * (taille_pt * 0.62 + 1.5) + 14); c = min((L - 12) / (g + dr), (H - haut - hd - 22) / n, 20.0); gx = x0 + 12 + ((L - 12) - (g + dr) * c) / 2
    d.ligne([(gx + g * c, y0 + haut), (gx + (g + 1) * c, y0 + haut), (gx + (g + 1) * c, y0 + haut + n * c), (gx + g * c, y0 + haut + n * c)], ep=0, ferme=True, fond=(0.82, 0.82, 0.82))
    for i, ((mot, _), p) in enumerate(zip(mots, pos)):
        y = y0 + haut + i * c; xa = gx + (g - p) * c
        d.texte(xa - 5, y + c / 2 + 1.6, str(i + 1), 12, police='Arial-B')
        for k in range(len(mot)): d.ligne([(xa + k * c, y), (xa + (k + 1) * c, y), (xa + (k + 1) * c, y + c), (xa + k * c, y + c)], ep=0.5, ferme=True)
    yd = y0 + haut + n * c + 9; pas = (y0 + H - 20 - yd) / n
    for i, (_, definition) in enumerate(mots):
        t = taille_pt
        while d.largeur_texte(f'{i + 1}. {definition}', t) > L: t -= 0.5; assert t >= 9, f'définition trop longue : {definition!r}'
        d.texte(x0, yd + i * pas + 3, f'{i + 1}.', t, ancre='s', police='Arial-B'); d.texte(x0 + 8, yd + i * pas + 3, definition, t, ancre='s')
    d.texte(x0, y0 + H - 5, 'Le mot mystère :', 13, ancre='s', police='Arial-B'); lx = x0 + d.largeur_texte('Le mot mystère :', 13, 'Arial-B') + 5
    for k in range(n): d.ligne([(lx + k * 11, y0 + H - 12), (lx + k * 11 + 10, y0 + H - 12), (lx + k * 11 + 10, y0 + H - 2), (lx + k * 11, y0 + H - 2)], ep=0.6, ferme=True, fond=(0.9, 0.9, 0.9))
    assert c >= 9, 'cases trop petites : raccourcir les mots'
    return (None if dessin else d.sauver(base)), n, round(c, 1)

def cocotte(base, coins, nombres, defis, titre='Cocotte en papier', taille_pt=12, dessin=None):
    """J24 : cocotte en papier (salière). coins : 4 mots visibles à l'extérieur ; nombres : 8 textes courts sur les
    volets ; defis : 8 couples (question, réponse) cachés sous les volets, dans le même ordre que nombres.
    Carré de 18,6 cm à découper, puis règle du pliage en quatre étapes.
    Renvoie (chemin du PDF, nombre de défis, côté du carré en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); S = L; cx, cy = x0 + S / 2, y0 + S / 2
    assert len(coins) == 4 and len(nombres) == 8 and len(defis) == 8, '4 coins, 8 nombres, 8 défis'
    d.ligne([(x0, y0), (x0 + S, y0), (x0 + S, y0 + S), (x0, y0 + S)], ep=0.35, tirets=(1, 1.2), ferme=True); reperes_de_coupe(d, (x0, x0 + S), (y0, y0 + S))
    for a, b in (((x0, y0), (x0 + S, y0 + S)), ((x0 + S, y0), (x0, y0 + S)), ((cx, y0), (cx, y0 + S)), ((x0, cy), (x0 + S, cy))): d.ligne([a, b], ep=0.25)
    for q in (-S / 4, S / 4): d.ligne([(cx + q, y0), (cx + q, y0 + S)], ep=0.25); d.ligne([(x0, cy + q), (x0 + S, cy + q)], ep=0.25)
    d.ligne([(cx, y0), (x0 + S, cy), (cx, y0 + S), (x0, cy)], ep=0.6, ferme=True)
    for k, t in enumerate(coins):                                           # carrés des coins : l'extérieur de la cocotte
        sx, sy = ((-1, -1), (1, -1), (1, 1), (-1, 1))[k]; tt = taille_pt + 4
        while d.largeur_texte(t, tt, 'Arial-B') > S * 0.25: tt -= 0.5; assert tt >= 9, f'texte trop long : {t!r}'
        d.texte(cx + sx * S * 0.385, cy + sy * S * 0.385, t, tt, police='Arial-B', rot=(-45, 45, -45, 45)[k])
    for k in range(8):                                                      # par huitième : nombre (volet), question et réponse (dessous)
        sx, sy = ((1, -1), (1, 1), (-1, 1), (-1, -1))[k // 2]; inv = (k % 2 == 1) != (sx * sy > 0)
        def P(u, v): return (cx + sx * S * (v if inv else u), cy + sy * S * (u if inv else v))
        q, r = defis[k]
        for (u, v), t, c, pol in (((0.4167, 0.165), nombres[k], taille_pt + 4, 'Arial-B'), ((0.325, 0.075), q, taille_pt, 'Arial'), ((0.175, 0.075), r, taille_pt, 'Arial-B')):
            px, py = P(u, v); _texte_ajuste(d, px, py, t, c, S * 0.105, pol, mini=7)
    y = y0 + S + 9; d.texte(x0, y, titre + ' : le pliage', 13, ancre='s', police='Arial-B')
    etapes = ('1. Découpe le carré. Pose-le, face imprimée contre la table.', '2. Plie les quatre coins vers le centre. Retourne le carré.',
              '3. Plie encore les quatre coins vers le centre.', '4. Plie en deux, glisse le pouce et l’index de chaque main sous les quatre coins.',
              'Le jeu : ton camarade choisit un mot, puis un nombre ; soulève le volet, lis le défi, vérifie la réponse (en gras).')
    pas = (y0 + H - y - 8) / len(etapes)
    for j, t in enumerate(etapes): _texte_ajuste(d, x0 + L / 2, y + 8 + j * pas, t, 11.5, L, mini=9)
    return (None if dessin else d.sauver(base)), 8, round(S, 1)

def horloge(base, minutes=False, heures_24=False, titre='Mon horloge', dessin=None):
    """J25 : horloge à aiguilles mobiles. Cadran de 17 cm, chiffres de 1 à 12 ; minutes=True ajoute les graduations
    des minutes et les nombres 5, 10… 60 ; heures_24=True ajoute les heures de 13 à 24. Sous le cadran, les deux
    aiguilles à découper ; une attache parisienne au centre.
    Renvoie (chemin du PDF, nombre de graduations, diamètre du cadran en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); R = 85.0; cx, cy = x0 + L / 2, y0 + R + 1
    d.cercle(cx, cy, R, ep=0.35, tirets=(1, 1.2)); re = R - (13 if minutes else 3); d.cercle(cx, cy, re, ep=1.2); d.cercle(cx, cy, 1.2, ep=0, fond=(0, 0, 0))
    for k in range(60 if minutes else 12):
        a = math.radians(k * (6 if minutes else 30)); gros = (k % 5 == 0) or not minutes; r1 = re - (6 if gros else 3)
        d.ligne([(cx + re * math.sin(a), cy - re * math.cos(a)), (cx + r1 * math.sin(a), cy - r1 * math.cos(a))], ep=1.0 if gros else 0.4)
    for hh in range(1, 13):
        a = math.radians(hh * 30); d.texte(cx + (re - 15) * math.sin(a), cy - (re - 15) * math.cos(a) + 3.2, str(hh), 26, police='Arial-B')
        if heures_24: d.texte(cx + (re - 29) * math.sin(a), cy - (re - 29) * math.cos(a) + 1.6, str(hh + 12), 13)
        if minutes: d.texte(cx + (R - 6.5) * math.sin(a), cy - (R - 6.5) * math.cos(a) + 1.5, str(hh * 5), 12)
    y = y0 + 2 * R + 12; d.texte(x0, y, titre + ' : découpe le cadran et les deux aiguilles. Fixe-les au centre avec une attache parisienne.', 10.5, ancre='s')
    for k, (lg, nom, large) in enumerate(((re - 26, 'heures', 13), (re - 9, 'minutes', 9))):  # aiguilles : la petite et la grande
        ya = y + 14 + k * 26; xa = x0 + 14
        d.ligne([(xa - 9, ya - large / 2), (xa + lg - large, ya - large / 2), (xa + lg, ya), (xa + lg - large, ya + large / 2), (xa - 9, ya + large / 2)], ep=0.35, tirets=(1, 1.2), ferme=True, fond=(0.85, 0.85, 0.85) if k == 0 else (1, 1, 1))
        d.cercle(xa, ya, 1.2, ep=0, fond=(0, 0, 0)); d.texte(xa + lg / 2, ya + 1.5, nom, 11, police='Arial-B')
    return (None if dessin else d.sauver(base)), 60 if minutes else 12, round(2 * R, 1)

def eventail(base, fiches, colonnes=4, taille_pt=16, mention='', dessin=None):
    """J26 : mémo-fiches en éventail. fiches : [(titre, [lignes])] ; deux rangées de `colonnes` fiches hautes de
    13,2 cm ; un rond marque le trou de l'attache (attache parisienne ou anneau) : les fiches s'ouvrent en éventail.
    Renvoie (chemin du PDF, nombre de fiches, largeur et hauteur d'une fiche en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / 2
    assert len(fiches) <= 2 * colonnes, 'trop de fiches pour une planche'
    for i, (t, lignes) in enumerate(fiches):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h
        d.ligne([(x + 2, y + 2), (x + l - 2, y + 2), (x + l - 2, y + 17), (x + 2, y + 17)], ep=0, ferme=True, fond=(0.88, 0.88, 0.88))
        _texte_ajuste(d, x + l / 2, y + 10.5, t, taille_pt + 2, l - 7, 'Arial-B', mini=9)
        pas = (h - 17 - 16) / max(len(lignes), 1)
        for j, z in enumerate(lignes): _texte_ajuste(d, x + l / 2, y + 17 + (j + 0.6) * pas, z, taille_pt, l - 5, mini=8)
        d.cercle(x + l / 2, y + h - 7, 2.5, ep=0.5); d.ligne([(x + l / 2 - 1.2, y + h - 7), (x + l / 2 + 1.2, y + h - 7)], ep=0.3); d.ligne([(x + l / 2, y + h - 8.2), (x + l / 2, y + h - 5.8)], ep=0.3)
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0, y0 + h, y0 + H]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(fiches), (round(l / 10, 2), round(h / 10, 2))

MOTIFS = ('traits', 'zigzag', 'vagues', 'ponts', 'creneaux', 'boucles', 'spirales', 'coupes')

def _motif(nom, x, y, l, a, pas):
    """Points d'un motif graphique : départ en (x, y), longueur l, amplitude a, largeur d'un motif pas (mm)."""
    n = max(1, int(l / pas)); pts = []
    for k in range(n):
        xk = x + k * pas
        if nom == 'traits': pts.append([(xk + pas / 2, y - a), (xk + pas / 2, y + a)])
        elif nom == 'zigzag': pts += [(xk, y + a), (xk + pas / 2, y - a)] + ([(xk + pas, y + a)] if k == n - 1 else [])
        elif nom == 'vagues': pts += [(xk + pas * t / 16, y - a * math.sin(2 * math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'ponts': pts += [(xk + pas * t / 16, y + a - 2 * a * math.sin(math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'coupes': pts += [(xk + pas * t / 16, y - a + 2 * a * math.sin(math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'creneaux': pts += [(xk, y + a), (xk, y - a), (xk + pas / 2, y - a), (xk + pas / 2, y + a)] + ([(xk + pas, y + a)] if k == n - 1 else [])
        elif nom == 'boucles': pts += [(xk + pas * t / 24 - a * 0.75 * math.sin(2 * math.pi * t / 24), y + a * math.cos(2 * math.pi * t / 24)) for t in range(25 if k == n - 1 else 24)]
        elif nom == 'spirales': pts.append([(xk + pas / 2 + (a * t / 60) * math.cos(t / 60 * 5 * math.pi), y + (a * t / 60) * math.sin(t / 60 * 5 * math.pi)) for t in range(61)])
    return pts if nom in ('traits', 'spirales') else [pts]

def bandes_graphiques(base, motifs=('traits', 'zigzag', 'vagues', 'ponts', 'boucles'), mention='', dessin=None):
    """J27 : bandes graphiques à plastifier (feutre effaçable). Une bande par motif de MOTIFS : un point de départ,
    un modèle en trait plein sur le premier tiers, puis le même tracé en pointillés à repasser.
    Renvoie (chemin du PDF, nombre de bandes, hauteur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(motifs); h = H / n; assert 3 <= n <= 8, 'de 3 à 8 bandes'
    for i, nom in enumerate(motifs):
        assert nom in MOTIFS, nom
        y = y0 + (i + 0.5) * h; a = h * 0.3; pas = (a * 1.1 if nom == 'traits' else a * 2.6 if nom == 'spirales' else a * 2)
        d.cercle(x0 + 7, y + (0 if nom in ('vagues', 'spirales') else -a if nom in ('traits', 'coupes') else a), 1.8, ep=0, fond=(0, 0, 0))
        nb = max(1, int((L - 20) / pas)); modele = max(1, nb // 3)
        for part, dx, k, tirets in ((modele, 0, 0, None), (nb - modele, modele * pas, 1, (1.2, 1.6))):
            if part <= 0: continue
            for seg in _motif(nom, x0 + 12 + dx, y, part * pas, a, pas): d.ligne(seg, ep=0.9 if k == 0 else 0.6, tirets=tirets)
    xs = (x0, x0 + L); ys = [y0 + r * h for r in range(n + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), n, round(h, 1)
```

#### 20 novembre 2026 : plateau à camemberts, cherche-et-trouve, mots interdits, petit bac, lignage romand (J28 à J31, G22)

Cinq fonctions dessinent avec la classe `Dessin` (R11) les gabarits J28 à J31 et G22 : `plateau_camemberts`, `planche_lynx`, `cartes_mots_interdits`, `petit_bac` et `lignage_romand`. Les catégories du plateau se distinguent par un symbole (`_symbole`), jamais par la couleur seule. Le bloc se place après le bloc J21 à J27 (il utilise `_bandeau`, `_cadre_arrondi`, `_mention` et `_texte_ajuste`).

**Test (20.11.2026)** : quatorze pages produites et regardées sur le rendu PDF ; `planche_lynx` place 20, 38 et 66 mots sans chevauchement ; le module de 7 mm de `lignage_romand` reproduit le document « Lignes, document vertical » de la BDRP (6,9 mm mesurés) ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J28 à J31 et G22 : plateau à camemberts, cherche-et-trouve, mots interdits, petit bac, lignage romand (20.11.2026) ----------
def _symbole(d, k, x, y, r, fond=(0.15, 0.15, 0.15)):
    """Symbole de la catégorie k (0 à 5) : disque, triangle, carré, losange, étoile, croix. Jamais la couleur seule."""
    if COULEUR[0]: fond = TEINTES[TEINTES_CATEGORIES[k % 6]]
    if k == 0: d.cercle(x, y, r * 0.9, ep=0.3, fond=fond)
    elif k == 1: d.ligne([(x, y - r), (x + r, y + r * 0.8), (x - r, y + r * 0.8)], ep=0.3, ferme=True, fond=fond)
    elif k == 2: d.ligne([(x - r * 0.85, y - r * 0.85), (x + r * 0.85, y - r * 0.85), (x + r * 0.85, y + r * 0.85), (x - r * 0.85, y + r * 0.85)], ep=0.3, ferme=True, fond=fond)
    elif k == 3: d.ligne([(x, y - r * 1.1), (x + r * 0.8, y), (x, y + r * 1.1), (x - r * 0.8, y)], ep=0.3, ferme=True, fond=fond)
    elif k == 4: d.ligne([(x + (r * 1.1 if j % 2 == 0 else r * 0.45) * math.sin(math.radians(36 * j)), y - (r * 1.1 if j % 2 == 0 else r * 0.45) * math.cos(math.radians(36 * j))) for j in range(10)], ep=0.3, ferme=True, fond=fond)
    else:
        a, b = r, r * 0.35
        d.ligne([(x - b, y - a), (x + b, y - a), (x + b, y - b), (x + a, y - b), (x + a, y + b), (x + b, y + b), (x + b, y + a), (x - b, y + a), (x - b, y + b), (x - a, y + b), (x - a, y - b), (x - b, y - b)], ep=0.3, ferme=True, fond=fond)

def plateau_camemberts(base, categories, entre=4, rayon=3, titre='Le tour des savoirs', dessin=None):
    """J28 : plateau de quiz à six catégories (roue à six rayons). categories : 6 noms courts. entre : cases entre deux
    rayons sur la couronne ; rayon : cases par rayon. Chaque case porte le symbole d'une catégorie ; au bout de chaque
    rayon, une grande case : une réponse juste y fait gagner la part de cette catégorie. Sous la roue : la légende
    et quatre camemberts de score à colorier. Renvoie (chemin du PDF, nombre de cases, plus petit côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert len(categories) == 6, 'six catégories'
    R = 90.0; cx, cy = x0 + L / 2, y0 + R + 1; w = 15.0; rh = 15.0; n = 6 * (entre + 1); pas = 360 / n; lr = (R - w - rh) / rayon; lw = 14.0
    P = lambda r, a: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    for j in range(6):                                                      # rayons, du bord vers le centre
        a = 60 * j; ux, uy = math.sin(math.radians(a)), -math.cos(math.radians(a))
        for q in range(rayon):
            r1, r2 = R - w - q * lr, R - w - (q + 1) * lr; k = (j + q + 2) % 6
            d.ligne([(cx + ux * r1 - uy * lw / 2, cy + uy * r1 + ux * lw / 2), (cx + ux * r1 + uy * lw / 2, cy + uy * r1 - ux * lw / 2),
                     (cx + ux * r2 + uy * lw / 2, cy + uy * r2 - ux * lw / 2), (cx + ux * r2 - uy * lw / 2, cy + uy * r2 + ux * lw / 2)], ep=0.5, ferme=True, fond=(1, 1, 1))
            _symbole(d, k, cx + ux * (r1 + r2) / 2, cy + uy * (r1 + r2) / 2, 2.8)
    for i in range(n):                                                      # couronne
        a = i * pas; j, p = divmod(i, entre + 1); grande = p == 0
        rejoue = entre >= 5 and p in (2, entre - 1)
        d.ligne(arc_pts(cx, cy, R, a - pas / 2, a + pas / 2, 8) + arc_pts(cx, cy, R - w, a + pas / 2, a - pas / 2, 8), ep=1.1 if grande else 0.5, ferme=True,
                fond=(0.85, 0.85, 0.85) if grande else (1, 1, 1))
        px, py = P(R - w / 2, a)
        if rejoue: d.texte(px, py + 1.2, 'rejoue', 6.5, police='Arial-B', rot=a if a <= 90 or a >= 270 else a - 180)
        else: _symbole(d, j if grande else (j + p + 1 + (p > entre // 2)) % 6, px, py, 4.2 if grande else 2.8)
    d.cercle(cx, cy, rh, ep=1.1, fond=(0.92, 0.92, 0.92)); d.texte(cx, cy - 1, 'Départ', 9, police='Arial-B'); d.texte(cx, cy + 4, 'Arrivée', 9, police='Arial-B')
    y = y0 + 2 * R + 8; d.texte(x0, y, titre, 14, ancre='s', police='Arial-B')
    for k, nom in enumerate(categories):                                    # légende : symbole et nom
        xx, yy = x0 + 4 + (k % 2) * 62, y + 11 + (k // 2) * 11; _symbole(d, k, xx, yy - 1.5, 3.2)
        t = 11
        while d.largeur_texte(nom, t) > 50: t -= 0.5; assert t >= 8, f'nom de catégorie trop long : {nom!r}'
        d.texte(xx + 7, yy, nom, t, ancre='s')
    for t, yy in (('Grande case au bout d’un rayon : si tu réponds juste, colorie la part de ton camembert.', y + 47), ('Six parts coloriées : retourne au centre et réponds à une dernière question.', y + 53)): d.texte(x0, yy, t, 9, ancre='s')
    for k in range(4):                                                      # quatre camemberts de score
        px, py = x0 + L - 46 + (k % 2) * 30, y + 6 + (k // 2) * 31; rr = 13.0
        for s in range(6):
            d.ligne(arc_pts(px, py, rr, 60 * s - 30, 60 * s + 30, 6) + [(px, py)], ep=0.5, ferme=True)
            _symbole(d, s, px + rr * 0.62 * math.sin(math.radians(60 * s)), py - rr * 0.62 * math.cos(math.radians(60 * s)), 1.6)
    cote = min(w, 2 * math.pi * (R - w / 2) / n, lr, lw); assert cote >= 11, 'cases trop petites'
    return (None if dessin else d.sauver(base)), n + 6 * rayon + 1, round(cote, 1)

def planche_lynx(base, mots, graine=1, taille_pt=15, titre='Cherche et trouve', dessin=None):
    """J29 : planche de cherche-et-trouve. Les mots sont dispersés sur la page, penchés, sans se toucher. Une carte
    consigne est tirée (« Trouve un adjectif », « Trouve un mot de la famille de… ») ; le premier qui pose le doigt
    sur un mot qui convient gagne la carte. Renvoie (chemin du PDF, nombre de mots, corps en pt)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); alea = random.Random(graine)
    haut = _bandeau(d, titre, 'Tire une carte, lis la consigne, cherche un mot qui convient et pose ton doigt dessus.')
    _cadre_arrondi(d, x0, y0 + haut, L, H - haut, r=8, ep=1.2); poses = []; rc = taille_pt * 0.19
    for mot in sorted(mots, key=len, reverse=True):
        lg = d.largeur_texte(mot, taille_pt, 'Arial-B')
        candidats = []                                                      # (écart au mot le plus proche, x, y, rot, points)
        for essai in range(4000):
            rot = alea.choice((-35, -25, -15, -8, 0, 8, 15, 25, 35, 0, 0, 90, -90)); a = math.radians(rot)
            x, y = alea.uniform(x0 + 6, x0 + L - 6), alea.uniform(y0 + haut + 6, y0 + H - 6)
            pts = [(x + (t - lg / 2) * math.cos(a), y + (t - lg / 2) * math.sin(a)) for t in [lg * k / max(1, int(lg / rc)) for k in range(max(1, int(lg / rc)) + 1)]]
            if any(not (x0 + 5 < px < x0 + L - 5 and y0 + haut + 5 < py < y0 + H - 5) for px, py in pts): continue
            ecart = min((math.hypot(px - qx, py - qy) for autres in poses for qx, qy in autres for px, py in pts), default=1e9)
            if ecart < 2 * rc + 3.5: continue
            candidats.append((ecart, x, y, rot, pts))
            if len(candidats) == 40: break
        if not candidats: raise AssertionError(f'plus de place pour {mot!r} : réduire le corps ou le nombre de mots')
        _, x, y, rot, pts = max(candidats, key=lambda c: c[0]); a = math.radians(rot)   # le plus loin des autres : mots bien répartis
        poses.append(pts); d.texte(x + rc * 0.6 * math.sin(a) * -1, y + rc * 0.6 * math.cos(a), mot, taille_pt, police='Arial-B', rot=rot)
    return (None if dessin else d.sauver(base)), len(mots), taille_pt

def cartes_mots_interdits(base, cartes, colonnes=3, rangees=3, taille_pt=16, mention='', dessin=None, lisere=True):
    """J30 : cartes à mots interdits. cartes : [(mot à faire deviner, [mots interdits])]. L'élève fait deviner le mot
    du bandeau sans prononcer les mots interdits. lisere : cadre arrondi à 3 mm du trait de coupe (MP-J-14).
    Renvoie (chemin du PDF, nombre de cartes, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(cartes) <= colonnes * rangees, 'trop de cartes pour une planche'
    if lisere: lisere_cartes(d, colonnes, rangees)
    e = 5.5 if lisere else 3                                                # bandeau à l'intérieur du liseré
    for i, (mot, interdits) in enumerate(cartes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; hb = min(18.0, h * 0.24)
        d.ligne([(x + e, y + e), (x + l - e, y + e), (x + l - e, y + e + hb), (x + e, y + e + hb)], ep=0.6, ferme=True, fond=(0.85, 0.85, 0.85))
        _texte_ajuste(d, x + l / 2, y + e + hb / 2 + 1, mot, taille_pt + 3, l - 2 * e - 4, 'Arial-B', mini=10)
        d.texte(x + l / 2, y + e + hb + 6.5, 'sans dire', 8); pas = (h - hb - 2 * e - 13) / max(len(interdits), 1)
        for j, z in enumerate(interdits): _texte_ajuste(d, x + l / 2, y + e + hb + 10 + (j + 0.5) * pas, z, taille_pt, l - 2 * e - 4, mini=9)
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(cartes), (round(l / 10, 2), round(h / 10, 2))

def petit_bac(base, categories, manches=6, titre='Petit bac', taille_pt=12, dessin=None):
    """J31 : grille de petit bac. Une lettre est tirée par manche ; chaque élève écrit un mot par catégorie qui commence
    par cette lettre. categories : 3 à 6 noms courts. Renvoie (chemin du PDF, nombre de cases à remplir, hauteur d'une ligne en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(categories); assert 3 <= n <= 6, 'de 3 à 6 catégories'
    haut = _bandeau(d, titre, 'Une lettre par ligne. Écris un mot par colonne. Un mot juste : 1 point ; un mot que personne d’autre n’a : 2 points.')
    d.texte(x0, y0 + haut + 6, 'Prénom : ____________________', 12, ancre='s'); y1 = y0 + haut + 12; he = 12.0; hl = (y0 + H - y1 - he - 12) / manches
    la, lp = 18.0, 20.0; lc = (L - la - lp) / n; xs = [x0, x0 + la] + [x0 + la + (k + 1) * lc for k in range(n)] + [x0 + L]
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y1 + he), (x0, y1 + he)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for k, t in enumerate(['Lettre'] + list(categories) + ['Points']): _texte_ajuste(d, (xs[k] + xs[k + 1]) / 2, y1 + he / 2 + 0.5, t, taille_pt, xs[k + 1] - xs[k] - 3, 'Arial-B', mini=8)
    for x in xs: d.ligne([(x, y1), (x, y1 + he + manches * hl)], ep=1.0 if x in (x0, x0 + L) else 0.4)
    for j in range(manches + 1): d.ligne([(x0, y1 + he + j * hl), (x0 + L, y1 + he + j * hl)], ep=1.0 if j in (0, manches) else 0.4)
    d.ligne([(x0, y1), (x0 + L, y1)], ep=1.0); yt = y1 + he + manches * hl + 8
    d.texte(x0 + L - lp - 3 - d.largeur_texte('Total :', 13, 'Arial-B'), yt, 'Total :', 13, ancre='s', police='Arial-B')
    d.ligne([(x0 + L - lp, yt - 6.5), (x0 + L, yt - 6.5), (x0 + L, yt + 3), (x0 + L - lp, yt + 3)], ep=0.8, ferme=True)
    assert hl >= 12, 'lignes trop basses'
    return (None if dessin else d.sauver(base)), n * manches, round(hl, 1)

def lignage_romand(base, module_mm=7.0, couleurs=True, entete=True, dessin=None):
    """G22 : page de lignes d'écriture au lignage romand (quatre lignes, trois couloirs égaux, sans quadrillage) :
    ligne de base épaisse, ligne du corps des lettres en trait fin, lignes de plafond et de plancher en pointillés.
    module_mm : hauteur d'un couloir (7 mm : modèle de la BDRP pour l'entrée dans l'écriture ; 4 mm, 2,5 mm ou 2 mm
    ensuite). couleurs=True colore les couloirs : ciel (lettres hautes), herbe (corps), terre (lettres basses).
    Renvoie (chemin du PDF, nombre de lignes d'écriture, module en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); m = module_mm; assert 2 <= m <= 10, 'module de 2 à 10 mm'
    haut = 12.0 if entete else 0.0; esp = max(5.0, 1.6 * m); n = int((H - haut + esp) / (3 * m + esp)); esp = (H - haut - n * 3 * m) / max(n - 1, 1)
    if entete and JEUNES[0]: d.texte(x0, y0 + 6, _prenom(), 12, ancre='s')
    elif entete: d.texte(x0, y0 + 6, 'Prénom : ____________________', 12, ancre='s'); d.texte(x0 + L - d.largeur_texte('Date : ______________', 12), y0 + 6, 'Date : ______________', 12, ancre='s')
    for i in range(n):
        y = y0 + haut + i * (3 * m + esp)
        if couleurs:
            for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(x0, y + k * m), (x0 + L, y + k * m), (x0 + L, y + (k + 1) * m), (x0, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
        d.ligne([(x0, y), (x0 + L, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(x0, y + m), (x0 + L, y + m)], ep=0.25)
        d.ligne([(x0, y + 2 * m), (x0 + L, y + 2 * m)], ep=0.55); d.ligne([(x0, y + 3 * m), (x0 + L, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    return (None if dessin else d.sauver(base)), n, m
```

#### 20 novembre 2026 : cartes à catégories, petits chevaux, Qui est-ce ?, tuiles-lettres, sudoku, mot caché, syllabes et sons, livret d'écriture

Huit fonctions complètent les gabarits J28, J33 à J38, G22 et G23 : `cartes_categories`, `petits_chevaux`, `grille_qui_est_ce`, `tuiles_lettres`, `sudoku`, `mot_cache_fleur`, `fiche_syllabes_sons` et `livret_ecriture`. `_decoupe` trace les pointillés et les repères de coupe d'une planche ; `_sudoku` construit une grille et vérifie par programme que sa solution est unique ; `_fleur` dessine la fleur étape par étape. Le bloc se place après le bloc J28 à J31 (il utilise `_symbole`, `_bandeau`, `_cadre_arrondi`, `_mention` et `_texte_ajuste`).

**Test (20.11.2026)** : toutes les pages produites et regardées sur le rendu PDF ; sudokus de 4 × 4, 6 × 6 et 9 × 9 à solution unique, pages de solutions comprises ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe ; pliage et agrafage du livret non essayés ; insertion d'images dans la fiche « syllabes et sons » non essayée.

```
# ---------- J28 (cartes), J33 à J38, G22 (livret), G23 : cartes à catégories, petits chevaux, qui est-ce, tuiles-lettres, sudoku, fleur, syllabes (20.11.2026) ----------
def _decoupe(d, colonnes, rangees, mention=''):
    """Pointillés et repères de coupe d'une planche de colonnes × rangees pièces ; renvoie (largeur, hauteur) d'une pièce."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return l, h

def cartes_categories(base, cartes, colonnes=2, rangees=2, taille_pt=11, mention='', dessin=None, lisere=True):
    """J28 : cartes-questions du plateau à camemberts. cartes : une liste par carte de six couples (question, réponse),
    dans l'ordre des catégories (disque, triangle, carré, losange, étoile, croix). La carte est lue par un·e camarade :
    la réponse est écrite en gras sous la question. lisere : cadre arrondi à 3 mm du trait de coupe (MP-J-14).
    Renvoie (chemin du PDF, nombre de cartes, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(cartes) <= colonnes * rangees and all(len(c) == 6 for c in cartes), 'six questions par carte'
    if lisere: lisere_cartes(d, colonnes, rangees)
    e = 2.5 if lisere else 0                                                # contenu à l'intérieur du liseré
    for i, carte in enumerate(cartes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; pas = (h - 8 - 2 * e) / 6
        for k, (q, r) in enumerate(carte):
            yy = y + 4 + e + k * pas; _symbole(d, k, x + 8 + e, yy + pas / 2, 2.8)
            if k: d.ligne([(x + 4 + e, yy), (x + l - 4 - e, yy)], ep=0.2)
            lignes = q.split('\n'); t = taille_pt
            while max(d.largeur_texte(z, t) for z in lignes) > l - 20 - 2 * e: t -= 0.5; assert t >= 7.5, f'question trop longue : {q!r}'
            p = t * 1.2 * 25.4 / 72; ya = yy + pas / 2 - (len(lignes) + 1) * p / 2 + t * 0.3
            for j, z in enumerate(lignes): d.texte(x + 14 + e, ya + j * p, z, t, ancre='s')
            tr = t
            while d.largeur_texte(r, tr, 'Arial-B') > l - 20 - 2 * e: tr -= 0.5
            d.texte(x + 14 + e, ya + len(lignes) * p + 0.6, r, tr, ancre='s', police='Arial-B')
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), len(cartes), (round(l / 10, 2), round(h / 10, 2))

def petits_chevaux(base, titre='Les petits chevaux', dessin=None):
    """J33 : plateau de petits chevaux pour quatre joueurs (symboles : disque, triangle, carré, étoile). Piste de
    52 cases en croix, quatre écuries, quatre échelles numérotées de 1 à 5 vers le centre. Pour sortir un pion ou
    monter une marche de l'échelle, l'élève répond à une carte-défi.
    Renvoie (chemin du PDF, nombre de cases de la piste, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); haut = _bandeau(d, titre, 'Un 6 et une réponse juste : ton pion sort de l’écurie. Sur l’échelle : une réponse juste par marche.')
    c = L / 15; oy = y0 + haut; sym = (0, 1, 2, 4)
    def case(i, j, fond=None, ep=0.5): d.ligne([(x0 + i * c, oy + j * c), (x0 + (i + 1) * c, oy + j * c), (x0 + (i + 1) * c, oy + (j + 1) * c), (x0 + i * c, oy + (j + 1) * c)], ep=ep, ferme=True, fond=fond)
    piste = 0
    for i in range(15):
        for j in range(15):
            croix = 6 <= i <= 8 or 6 <= j <= 8; centre = 6 <= i <= 8 and 6 <= j <= 8
            if not croix or centre: continue
            echelle = (i == 7 and 1 <= j <= 13) or (j == 7 and 1 <= i <= 13)
            case(i, j, fond=(0.88, 0.88, 0.88) if echelle else (1, 1, 1)); piste += 0 if echelle else 1
            if echelle:
                n = j if (i == 7 and j < 7) else 14 - j if i == 7 else i if i < 7 else 14 - i
                d.texte(x0 + (i + 0.5) * c, oy + (j + 0.5) * c + 1.8, str(n), 13, police='Arial-B')
    d.ligne([(x0 + 6 * c, oy + 6 * c), (x0 + 9 * c, oy + 6 * c), (x0 + 9 * c, oy + 9 * c), (x0 + 6 * c, oy + 9 * c)], ep=1.0, ferme=True, fond=(1, 1, 1))
    d.ligne([(x0 + 6 * c, oy + 6 * c), (x0 + 9 * c, oy + 9 * c)], ep=0.4); d.ligne([(x0 + 9 * c, oy + 6 * c), (x0 + 6 * c, oy + 9 * c)], ep=0.4)
    d.cercle(x0 + 7.5 * c, oy + 7.5 * c, c * 0.75, ep=0.6, fond=(1, 1, 1)); d.texte(x0 + 7.5 * c, oy + 7.5 * c + 1.2, 'Arrivée', 8.5, police='Arial-B')
    for k, (ex, ey, dep, tete) in enumerate(((0, 0, (6, 1), (7, 0)), (9, 0, (13, 6), (14, 7)), (9, 9, (8, 13), (7, 14)), (0, 9, (1, 8), (0, 7)))):
        _cadre_arrondi(d, x0 + ex * c + 3, oy + ey * c + 3, 6 * c - 6, 6 * c - 6, r=8, ep=1.0, fond=(0.94, 0.94, 0.94))
        _symbole(d, sym[k], x0 + (ex + 3) * c, oy + (ey + 3) * c, 6.5)
        for a, b in ((1.4, 1.4), (4.6, 1.4), (1.4, 4.6), (4.6, 4.6)): d.cercle(x0 + (ex + a) * c, oy + (ey + b) * c, c * 0.55, ep=0.8, fond=(1, 1, 1))
        _symbole(d, sym[k], x0 + (dep[0] + 0.5) * c, oy + (dep[1] + 0.5) * c, 3.0); _symbole(d, sym[k], x0 + (tete[0] + 0.5) * c, oy + (tete[1] + 0.5) * c, 1.8, fond=(0.6, 0.6, 0.6))
    y = oy + 15 * c + 8
    for j, t in enumerate(('Chaque joueur choisit un symbole et pose ses quatre pions dans son écurie.', 'Case marquée de ton symbole : le départ de tes pions. Ils font le tour de la piste dans le sens des aiguilles d’une montre.',
                           'Tu arrives sur un pion adverse : il retourne à son écurie. Le premier qui amène ses quatre pions au centre gagne.')):
        _texte_ajuste(d, x0 + L / 2, y + j * ((y0 + H - y - 4) / 3) + 3, t, 10.5, L, mini=8.5)
    return (None if dessin else d.sauver(base)), piste, round(c, 1)

def grille_qui_est_ce(base, elements, colonnes=4, titre='Qui est-ce ?', taille_pt=26, dessin=None):
    """J34 : grille de « Qui est-ce ? » sans images : des nombres, des mots ou des figures nommées. Chaque élève a une
    grille ; l'un choisit un élément en secret, l'autre pose des questions auxquelles on répond par oui ou par non et
    barre ce qui ne convient pas. Renvoie (chemin du PDF, nombre d'éléments, largeur et hauteur d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(elements); r = -(-n // colonnes); assert n == r * colonnes, 'grille incomplète'
    haut = _bandeau(d, titre, 'Pose une question à laquelle on répond par oui ou par non. Barre ce qui ne convient pas. Trouve l’élément secret.')
    hs = 14.0; l, h = L / colonnes, (H - haut - hs) / r
    for i, e in enumerate(elements):
        x, y = x0 + (i % colonnes) * l, y0 + haut + (i // colonnes) * h
        _cadre_arrondi(d, x + 1.5, y + 1.5, l - 3, h - 3, r=4, ep=0.8); _texte_ajuste(d, x + l / 2, y + h / 2 + 1, str(e), taille_pt, l - 8, 'Arial-B', mini=10)
    d.texte(x0, y0 + H - 4, 'Mon élément secret (écris-le, puis cache-le) : ____________', 12, ancre='s')
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

FREQUENCES = 'eeeeeeeeeeeeeeeaaaaaaaaaiiiiiiiinnnnnnooooooorrrrrrsssssstttttttuuuuuuullllldddmmmggbbccppffhhvvjqkwxyzéè'

def tuiles_lettres(base, colonnes=9, rangees=13, majuscules=False, mention='', dessin=None):
    """J36 : planche de tuiles-lettres à découper, pour composer des mots (lettres mobiles, jeux de mots croisés sur
    table). Les lettres suivent leur fréquence en français (FREQUENCES) ; un trait sous chaque lettre donne le bas
    de la tuile (b, d, p, q, n, u). Renvoie (chemin du PDF, nombre de tuiles, largeur et hauteur d'une tuile en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees; l, h = L / colonnes, H / rangees
    lettres = sorted(FREQUENCES[k * len(FREQUENCES) // n] if n <= len(FREQUENCES) else FREQUENCES[k % len(FREQUENCES)] for k in range(n))
    if n >= 26: lettres = sorted(set('abcdefghijklmnopqrstuvwxyz')) + sorted(FREQUENCES[k * len(FREQUENCES) // (n - 26)] for k in range(n - 26)); lettres.sort()
    t = min(l, h) * 1.75
    for i, z in enumerate(lettres):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; z = z.upper() if majuscules else z
        d.texte(x + l / 2, y + h * 0.66, z, t, police='Arial-B'); d.ligne([(x + l * 0.25, y + h * 0.85), (x + l * 0.75, y + h * 0.85)], ep=0.5)
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

def _sudoku(n, trous, graine):
    """Grille de sudoku n × n (4, 6 ou 9) à solution unique : renvoie (grille à trous, solution) ; 0 = case vide."""
    br, bc = {4: (2, 2), 6: (2, 3), 9: (3, 3)}[n]; alea = random.Random(graine)
    def ordre(taille, nb):                                                  # mélange des groupes, puis dans chaque groupe
        g = list(range(nb)); alea.shuffle(g); o = []
        for a in g: q = list(range(taille)); alea.shuffle(q); o += [a * taille + b for b in q]
        return o
    lig, col = ordre(br, n // br), ordre(bc, n // bc); ch = list(range(1, n + 1)); alea.shuffle(ch)
    sol = [[ch[(bc * (r % br) + r // br + c) % n] for c in col] for r in lig]
    def nombre(g, limite=2):                                                # nombre de solutions, arrêté à limite
        best = None
        for r in range(n):
            for c in range(n):
                if g[r][c] == 0:
                    pris = set(g[r]) | {g[k][c] for k in range(n)} | {g[a][b] for a in range(r - r % br, r - r % br + br) for b in range(c - c % bc, c - c % bc + bc)}
                    cand = [v for v in range(1, n + 1) if v not in pris]
                    if best is None or len(cand) < len(best[2]): best = (r, c, cand)
        if best is None: return 1
        total = 0
        for v in best[2]:
            g[best[0]][best[1]] = v; total += nombre(g, limite - total); g[best[0]][best[1]] = 0
            if total >= limite: break
        return total
    g = [row[:] for row in sol]; cases = [(r, c) for r in range(n) for c in range(n)]; alea.shuffle(cases); faits = 0
    for r, c in cases:
        if faits >= trous: break
        v = g[r][c]; g[r][c] = 0
        if nombre(g) == 1: faits += 1
        else: g[r][c] = v
    return g, sol

def sudoku(base, taille=6, grilles=2, trous=None, graine=1, solutions=False, titre='Sudoku', dessin=None):
    """J37 : sudokus de 4 × 4, 6 × 6 ou 9 × 9 cases, à solution unique (vérifiée par programme). grilles : nombre de
    grilles sur la page (1, 2 ou 4) ; solutions=True imprime les grilles remplies (page de l'enseignant·e).
    Renvoie (chemin du PDF, nombre de grilles, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = taille; br, bc = {4: (2, 2), 6: (2, 3), 9: (3, 3)}[n]
    trous = trous or {4: 9, 6: 20, 9: 46}[n]
    haut = _bandeau(d, titre + (' : solutions' if solutions else ''), f'Chaque ligne, chaque colonne et chaque bloc contient une seule fois les nombres de 1 à {n}.')
    cg, rg = (2, 2) if grilles == 4 else (1, grilles); lz, hz = L / cg, (H - haut) / rg; cote = min(lz, hz) - 8; c = cote / n
    for k in range(grilles):
        g, sol = _sudoku(n, trous, graine + k); g = sol if solutions else g
        gx, gy = x0 + (k % cg) * lz + (lz - cote) / 2, y0 + haut + (k // cg) * hz + (hz - cote) / 2
        for r in range(n):
            for q in range(n):
                if g[r][q]: d.texte(gx + (q + 0.5) * c, gy + (r + 0.5) * c + c * 0.17, str(g[r][q]), c * 1.35, police='Arial-B' if not solutions else 'Arial')
        for i in range(n + 1):
            d.ligne([(gx + i * c, gy), (gx + i * c, gy + cote)], ep=1.3 if i % bc == 0 else 0.35); d.ligne([(gx, gy + i * c), (gx + cote, gy + i * c)], ep=1.3 if i % br == 0 else 0.35)
    return (None if dessin else d.sauver(base)), grilles, round(c, 1)

def _fleur(d, x, y, s, etapes=8):
    """La fleur du jeu du mot caché, dessinée jusqu'à l'étape donnée : tige, deux feuilles, cœur, quatre pétales.
    (x, y) : pied de la tige ; s : hauteur totale en mm."""
    if etapes >= 1: d.ligne([(x, y), (x, y - s * 0.62)], ep=0.9)
    for k, sx in ((2, -1), (3, 1)):
        if etapes >= k: d.ligne([(x, y - s * 0.22)] + [(x + sx * s * 0.2 * (t / 8), y - s * 0.22 - s * 0.16 * math.sin(math.pi * t / 8) * (1 if t <= 8 else 0) - s * 0.05 * t / 8) for t in range(9)] + [(x + sx * s * 0.2 * (t / 8), y - s * 0.22 - s * 0.05 * t / 8 + s * 0.05 * math.sin(math.pi * t / 8)) for t in range(8, -1, -1)], ep=0.7, ferme=True)
    cy = y - s * 0.75
    for k, (ax, ay) in ((5, (0, -1)), (6, (1, 0)), (7, (0, 1)), (8, (-1, 0))):
        if etapes >= k: d.cercle(x + ax * s * 0.16, cy + ay * s * 0.16, s * 0.1, ep=0.7, fond=(1, 1, 1))
    if etapes >= 4: d.cercle(x, cy, s * 0.085, ep=0.8, fond=(0.75, 0.75, 0.75))

def mot_cache_fleur(base, parties=3, titre='Le mot caché : la fleur', dessin=None):
    """J38 : jeu du mot caché à deux. Un élève choisit un mot et trace un tiret par lettre ; l'autre propose des lettres.
    Lettre absente du mot : celui qui a choisi le mot dessine une partie de la fleur (tige, feuille, feuille, cœur,
    quatre pétales). La fleur terminée en huit erreurs : le mot n'est pas trouvé. Aucune image de pendu.
    Renvoie (chemin du PDF, nombre de parties par fiche, nombre d'étapes de la fleur)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); haut = _bandeau(d, titre, 'Lettre du mot : écris-la sur son tiret. Lettre absente : barre-la et dessine une partie de la fleur.')
    for k in range(1, 9):                                                   # le modèle, étape par étape
        xx = x0 + (k - 0.5) * L / 8; _fleur(d, xx, y0 + haut + 24, 22, k); d.texte(xx - 9, y0 + haut + 6, str(k), 9, police='Arial-B')
    yz = y0 + haut + 30; hz = (y0 + H - yz) / parties
    for p in range(parties):
        y = yz + p * hz; _cadre_arrondi(d, x0, y + 2, L, hz - 4, r=6, ep=0.9); lf = min(46.0, hz - 14)
        d.ligne([(x0 + L - lf - 6, y + 7), (x0 + L - 6, y + 7), (x0 + L - 6, y + hz - 7), (x0 + L - lf - 6, y + hz - 7)], ep=0.4, tirets=(1, 1.2), ferme=True)
        d.texte(x0 + L - lf / 2 - 6, y + hz - 9.5, 'ma fleur', 8); d.texte(x0 + 6, y + 13, 'Le mot (un tiret par lettre) :', 11, ancre='s', police='Arial-B')
        d.ligne([(x0 + 6, y + hz * 0.52), (x0 + L - lf - 12, y + hz * 0.52)], ep=0.3, tirets=(0.4, 1.4))
        lz = (L - lf - 20) / 13
        for i, z in enumerate('abcdefghijklmnopqrstuvwxyz'): d.texte(x0 + 8 + (i % 13 + 0.5) * lz, y + hz - 17 + (i // 13) * 7.5, z, 13)
    return (None if dessin else d.sauver(base)), parties, 8

def fiche_syllabes_sons(base, mots, colonnes=4, titre='Syllabes et sons', taille_pt=16, images=None, dessin=None, exemple=None):
    """G23 : fiche « syllabes et sons ». Par mot : un cadre pour l'image (collée par l'élève, ou insérée : images =
    liste de chemins), le mot écrit, une ligne où dessiner un carré par syllabe et une ligne où dessiner un jeton par son.
    Non-lecteurs (definir_jeunes, ou exemple donné) : aucune consigne écrite ; la première case est un exemple déjà
    fait, sur fond teinté : exemple = (mot, nombre de syllabes, nombre de sons), par défaut ('ballon', 2, 4), avec un
    ballon dessiné ; un petit carré et un petit rond remplacent les mots « syllabes » et « sons ».
    Renvoie (chemin du PDF, nombre de mots, largeur et hauteur d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(mots)
    if exemple is None and JEUNES[0]: exemple = ('ballon', 2, 4)
    dec = 1 if exemple else 0; r = -(-(n + dec) // colonnes)
    haut = _bandeau(d, titre, None if exemple else 'Colle l’image du mot. Dessine un carré par syllabe, puis un jeton par son.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); yg = y0 + haut + 10; l, h = L / colonnes, (y0 + H - yg - (5 if exemple else 0)) / r
    for i, mot in enumerate(([exemple[0]] if exemple else []) + list(mots)):
        x, y = x0 + (i % colonnes) * l, yg + (i // colonnes) * h; hi = h - 34; ex = bool(exemple) and i == 0
        d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=1.4 if ex else 0.7, ferme=True, fond=(0.9, 0.9, 0.9) if ex else None)
        if ex:                                                                # exemple déjà fait : un ballon, ses carrés, ses jetons
            cx, cy, rb = x + l / 2, y + 4 + (hi - 4) / 2, min(l - 12, hi - 8) / 2; d.cercle(cx, cy, rb, ep=1.0, fond=(1, 1, 1))
            d.ligne([(cx + rb * math.cos(a * math.pi / 20) * 0.45, cy + rb * math.sin(a * math.pi / 20)) for a in range(-10, 11)], ep=0.6); d.ligne([(cx - rb, cy), (cx + rb, cy)], ep=0.6)
        elif images and dessin is None: d.p.insert_image(d.f.Rect((x + 3) * d.k, (y + 3) * d.k, (x + l - 3) * d.k, (y + hi) * d.k), filename=images[i - dec])
        else: d.ligne([(x + 4, y + 4), (x + l - 4, y + 4), (x + l - 4, y + hi), (x + 4, y + hi)], ep=0.3, tirets=(1, 1.2), ferme=True)
        _texte_ajuste(d, x + l / 2, y + hi + 7, mot, taille_pt, l - 6, mini=10)
        for k, nom in enumerate(('syllabes', 'sons')):
            yy = y + hi + 11 + k * 11; d.ligne([(x, yy), (x + l, yy)], ep=0.3)
            if not exemple: d.texte(x + 2, yy + 3, nom, 6, ancre='s'); continue
            if k == 0: d.ligne([(x + 1.5, yy + 1.5), (x + 4.5, yy + 1.5), (x + 4.5, yy + 4.5), (x + 1.5, yy + 4.5)], ep=0.4, ferme=True)   # repère : carré = syllabe
            else: d.cercle(x + 3, yy + 3, 1.5, ep=0.4)                                                                               # repère : rond = son
            if ex:
                for j in range(exemple[1 + k]):
                    xj = x + 10 + j * 8.5
                    if k == 0: d.ligne([(xj, yy + 2), (xj + 6.5, yy + 2), (xj + 6.5, yy + 8.5), (xj, yy + 8.5)], ep=0.8, ferme=True, fond=(0.45, 0.45, 0.45))
                    else: d.cercle(xj + 3.2, yy + 5.3, 3.2, ep=0.8, fond=(0.45, 0.45, 0.45))
    if exemple: d.texte(x0, y0 + H - 0.5, 'Pour l’adulte : un carré par syllabe, un jeton par son. La première case montre l’exemple.', 7, ancre='s')
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

def livret_ecriture(base, module_mm=7.0, couleurs=True, feuilles=3, titre='Mon cahier d’écriture'):
    """G22, livret : cahier A5 de lignes d'écriture au lignage romand. Chaque feuille A4 paysage porte deux pages A5 ;
    impression recto-verso (retournement sur le bord court), pliage au milieu, agrafage dans le pli. La première
    face porte la couverture : le titre et un cartouche vide pour le prénom, sans ligne Prénom ni Classe (MP-O-03).
    Renvoie (chemin du PDF, nombre de pages A5 de lignes, module en mm)."""
    d = Dessin(297, 210); m = module_mm; assert feuilles >= 1
    def lignes(x, large):
        esp = max(5.0, 1.6 * m); n = int((180 + esp) / (3 * m + esp)); esp = (180 - n * 3 * m) / max(n - 1, 1)
        for i in range(n):
            y = 15 + i * (3 * m + esp)
            if couleurs:
                for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(x, y + k * m), (x + large, y + k * m), (x + large, y + (k + 1) * m), (x, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
            d.ligne([(x, y), (x + large, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(x, y + m), (x + large, y + m)], ep=0.25)
            d.ligne([(x, y + 2 * m), (x + large, y + 2 * m)], ep=0.55); d.ligne([(x, y + 3 * m), (x + large, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    for face in range(2 * feuilles):
        if face: d.p = d.d.new_page(width=297 * d.k, height=210 * d.k)
        d.ligne([(148.5, 4), (148.5, 9)], ep=0.3); d.ligne([(148.5, 201), (148.5, 206)], ep=0.3)   # repères du pli
        if face == 0:                                                       # couverture à droite, dos à gauche
            _cadre_arrondi(d, 160.5, 14, 124.5, 182, r=8, ep=1.2); _cadre_arrondi(d, 163, 16.5, 119.5, 177, r=6.5, ep=0.35)
            d.texte(222.75, 70, titre, 22, police='Arial-B')
            _cadre_arrondi(d, 172.75, 98, 100, 36, r=6, ep=0.8)               # cartouche du prénom, sans ligne (MP-O-03) :
                                                                                # l'enfant l'écrit en grand, ou l'adulte y colle l'étiquette
            lignes(12, 124.5)
        else: lignes(12, 124.5); lignes(160.5, 124.5)
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return base + '.pdf', 4 * feuilles - 1, m
```

#### 21 novembre 2026 : maisons des nombres, quadrillage, calendrier, étiquettes, livret à onglets, journal, bande dessinée, exposé (G24 à G31)

Huit fonctions dessinent avec la classe `Dessin` (R11) les gabarits G24 à G31 : `maison_des_nombres`, `reproduction_quadrillage`, `calendrier_mensuel`, `etiquettes_horaire`, `livret_a_onglets`, `page_journal`, `planche_bd` et `plan_expose`. Le bloc se place après le bloc précédent (il utilise `_bandeau`, `_cadre_arrondi`, `_mention`, `_texte_ajuste` et `_decoupe`).

**Test (21.11.2026)** : vingt-trois pages produites et regardées sur le rendu PDF ; les jours de décembre 2026, de janvier et de février 2027 sont calculés par le module `calendar` ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- G24 à G31 : maison des nombres, quadrillage, calendrier, étiquettes, livret à onglets, journal, BD, exposé (21.11.2026) ----------
def maison_des_nombres(base, nombres=(5, 6, 7, 8), titre='Les maisons des nombres', dessin=None):
    """G24 : maisons des nombres. Le nombre est écrit dans le toit ; chaque étage reçoit deux nombres dont la somme
    est celle du toit (décompositions additives). nombres : 2 à 6 maisons par page.
    Renvoie (chemin du PDF, nombre de maisons, hauteur d'un étage en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(nombres); assert 2 <= n <= 6, 'de 2 à 6 maisons'
    haut = _bandeau(d, titre, None if JEUNES[0] else 'À chaque étage, écris deux nombres : ensemble, ils font le nombre du toit.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); col = 2 if n <= 4 else 3; ran = -(-n // col)
    lz, hz = L / col, (H - haut - 10 - (5 if JEUNES[0] else 0)) / ran; et = 0
    if JEUNES[0]: d.texte(x0, y0 + H - 0.5, 'Pour l’adulte : à chaque étage, deux nombres qui font ensemble le nombre du toit. Le premier étage montre l’exemple.', 7, ancre='s')
    for i, nb in enumerate(nombres):
        x, y = x0 + (i % col) * lz + 6, y0 + haut + 10 + (i // col) * hz + 3; l, h = lz - 12, hz - 8; ht = min(30.0, h * 0.26); etages = nb + 1 if nb <= 6 else (nb + 2) // 2
        d.ligne([(x - 3, y + ht), (x + l / 2, y), (x + l + 3, y + ht)], ep=1.2, ferme=True, fond=(0.88, 0.88, 0.88)); d.texte(x + l / 2, y + ht * 0.78, str(nb), min(30, ht * 1.6), police='Arial-B')
        he = (h - ht) / etages; et = he
        for k in range(etages + 1): d.ligne([(x, y + ht + k * he), (x + l, y + ht + k * he)], ep=1.0 if k in (0, etages) else 0.4)
        if JEUNES[0]:                                                         # non-lecteurs : le premier étage est déjà rempli
            d.ligne([(x, y + ht), (x + l, y + ht), (x + l, y + ht + he), (x, y + ht + he)], ep=0, ferme=True, fond=(0.9, 0.9, 0.9)); te = min(26, he * 1.9)
            pe = police_exemple_pdf(); te = te * 0.9 if pe == 'Eleve' else te   # MP-T-10 : l'exemple en police d'élèves
            dy = te * (0.14 if pe == 'Eleve' else 0.125)                     # ligne de base : chiffres centrés dans l'étage
            d.texte(x + l / 4, y + ht + he / 2 + dy, '1', te, police=pe); d.texte(x + 3 * l / 4, y + ht + he / 2 + dy, str(nb - 1), te, police=pe)
            d.ligne([(x, y + ht), (x + l, y + ht)], ep=1.0); d.ligne([(x, y + ht + he), (x + l, y + ht + he)], ep=0.4)
        for xx, ep in ((x, 1.0), (x + l / 2, 0.4), (x + l, 1.0)): d.ligne([(xx, y + ht), (xx, y + h)], ep=ep)
    return (None if dessin else d.sauver(base)), n, round(et, 1)

FIGURES = {'maison': [[(1, 6), (1, 3), (4, 0), (7, 3), (7, 6), (1, 6)], [(3, 6), (3, 4), (5, 4), (5, 6)], [(1, 3), (7, 3)]],
           'bateau': [[(0, 5), (8, 5), (6, 7), (2, 7), (0, 5)], [(4, 5), (4, 0), (7, 4), (4, 4)], [(4, 1), (1, 4), (4, 4)]],
           'sapin': [[(4, 0), (6, 2), (5, 2), (7, 4), (6, 4), (8, 6), (5, 6), (5, 7), (3, 7), (3, 6), (0, 6), (2, 4), (1, 4), (3, 2), (2, 2), (4, 0)]],
           'fusée': [[(4, 0), (6, 2), (6, 6), (7, 7), (5, 7), (5, 6), (3, 6), (3, 7), (1, 7), (2, 6), (2, 2), (4, 0)], [(3, 3), (5, 3), (5, 4), (3, 4), (3, 3)]]}

def reproduction_quadrillage(base, figure='maison', cases=(8, 7), points=False, titre='Je reproduis la figure', dessin=None):
    """G25 : reproduction d'une figure sur quadrillage. En haut, le modèle ; en bas, le même quadrillage vide.
    figure : nom d'une figure de FIGURES, ou liste de lignes brisées (points aux nœuds du quadrillage) ;
    cases : (colonnes, rangées) ; points=True remplace le quadrillage du bas par les seuls nœuds (plus difficile).
    Renvoie (chemin du PDF, nombre de segments à tracer, côté d'un carreau en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); fig = FIGURES[figure] if isinstance(figure, str) else figure; c, r = cases
    haut = _bandeau(d, titre, 'Observe le modèle. Trace la même figure sur le quadrillage du bas, à la règle.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); hz = (H - haut - 14) / 2; pas = min((L - 10) / c, (hz - 12) / r, 14.0)
    for k, nom in enumerate(('Le modèle', 'À toi')):
        gx, gy = x0 + (L - c * pas) / 2, y0 + haut + 14 + k * hz + 6; d.texte(x0, gy - 2, nom, 12, ancre='s', police='Arial-B')
        if k == 1 and points:
            for i in range(c + 1):
                for j in range(r + 1): d.cercle(gx + i * pas, gy + j * pas, 0.5, ep=0, fond=(0, 0, 0))
        else:
            for i in range(c + 1): d.ligne([(gx + i * pas, gy), (gx + i * pas, gy + r * pas)], ep=0.25)
            for j in range(r + 1): d.ligne([(gx, gy + j * pas), (gx + c * pas, gy + j * pas)], ep=0.25)
        if k == 0:
            for ligne in fig: d.ligne([(gx + a * pas, gy + b * pas) for a, b in ligne], ep=1.3)
    assert all(0 <= a <= c and 0 <= b <= r for ligne in fig for a, b in ligne), 'figure hors du quadrillage'
    return (None if dessin else d.sauver(base)), sum(len(q) - 1 for q in fig), round(pas, 1)

MOIS = ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')

def calendrier_mensuel(base, annee, mois, titre=None, dessin=None):
    """G26 : calendrier d'un mois, semaine du lundi au dimanche, grandes cases pour écrire ou coller une étiquette.
    Les jours sont calculés par programme. Renvoie (chemin du PDF, nombre de jours, hauteur d'une case en mm)."""
    import calendar
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); semaines = calendar.Calendar(firstweekday=0).monthdayscalendar(annee, mois)
    haut = _bandeau(d, titre or f'{MOIS[mois - 1].capitalize()} {annee}', 'Chaque jour : la date, le temps qu’il fait, un événement de la classe.')
    he = 10.0; l, h = L / 7, (H - haut - he) / len(semaines); y1 = y0 + haut
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y1 + he), (x0, y1 + he)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for i, j in enumerate(('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche')): d.texte(x0 + (i + 0.5) * l, y1 + he / 2 + 1.5, j, 11, police='Arial-B')
    for s, semaine in enumerate(semaines):
        for i, jour in enumerate(semaine):
            x, y = x0 + i * l, y1 + he + s * h
            d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, ferme=True, fond=(0.94, 0.94, 0.94) if (i >= 5 or not jour) else (1, 1, 1))
            if jour: d.texte(x + 3, y + 7.5, str(jour), 16, ancre='s', police='Arial-B')
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y0 + H), (x0, y0 + H)], ep=1.1, ferme=True)
    return (None if dessin else d.sauver(base)), calendar.monthrange(annee, mois)[1], round(h, 1)

def etiquettes_horaire(base, etiquettes, colonnes=2, rangees=8, taille_pt=20, mention='', dessin=None):
    """G27 : étiquettes de l'horaire de la journée, à afficher dans l'ordre. Par étiquette : un cadre pour un
    pictogramme (dessiné, collé ou inséré) et le nom de l'activité. Renvoie (chemin du PDF, nombre d'étiquettes,
    largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees; assert len(etiquettes) <= colonnes * rangees
    for i, t in enumerate(etiquettes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; c = h - 8
        _cadre_arrondi(d, x + 4, y + 4, c, c, r=3, ep=0.6); _texte_ajuste(d, x + c + 8 + (l - c - 12) / 2, y + h / 2 + 0.5, t, taille_pt, l - c - 14, 'Arial-B', mini=10)
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), len(etiquettes), (round(l / 10, 2), round(h / 10, 2))

def livret_a_onglets(base, onglets, titre='Mon livret', pas_mm=14.0):
    """G28 : livret à onglets étagés. Une feuille par onglet : chaque feuille est coupée un peu plus court que la
    suivante, de sorte que tous les onglets restent visibles en bas ; les feuilles s'agrafent en haut.
    onglets : 3 à 8 titres, du premier (feuille la plus courte) au dernier (feuille entière).
    Renvoie (chemin du PDF, nombre de feuilles, hauteur d'un onglet en mm)."""
    x0, y0, L, H = SURFACE_MM; d = Dessin(); n = len(onglets); assert 3 <= n <= 8, 'de 3 à 8 onglets'
    for k, nom in enumerate(onglets):
        if k: d.p = d.d.new_page(width=210 * d.k, height=297 * d.k)
        bas = y0 + H - (n - 1 - k) * pas_mm; _mention(d, f'{titre} · feuille {k + 1} sur {n} · couper sur le pointillé, agrafer en haut')
        if k == 0: d.texte(x0 + L / 2, y0 + 16, titre, 26, police='Arial-B'); d.texte(x0 + L / 2, y0 + 30, 'Prénom : ____________________', 13)
        else: d.texte(x0, y0 + 12, nom, 18, ancre='s', police='Arial-B')
        for j in range(int((bas - pas_mm - y0 - (40 if k == 0 else 22)) / 11)): d.ligne([(x0, y0 + (48 if k == 0 else 30) + j * 11), (x0 + L, y0 + (48 if k == 0 else 30) + j * 11)], ep=0.25)
        d.ligne([(x0, bas - pas_mm), (x0 + L, bas - pas_mm), (x0 + L, bas), (x0, bas)], ep=0.8, ferme=True, fond=(0.88, 0.88, 0.88)); d.texte(x0 + L / 2, bas - pas_mm / 2 + 1.8, nom, 14, police='Arial-B')
        if k < n - 1: d.ligne([(0, bas), (210, bas)], ep=0.35, tirets=(1, 1.2))
        d.ligne([(x0, y0), (x0 + L, y0), (x0 + L, bas), (x0, bas)], ep=0.5, ferme=True)
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return base + '.pdf', n, pas_mm

def page_journal(base, titre='Le journal de la classe', articles=3, dessin=None):
    """G29 : page de journal de classe à remplir à la main : bandeau du titre, numéro et date, puis des articles sur
    deux colonnes (titre, cadre d'illustration, lignes d'écriture, signature). articles : 2 à 4.
    Renvoie (chemin du PDF, nombre d'articles, interligne en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert 2 <= articles <= 4
    d.ligne([(x0, y0), (x0 + L, y0), (x0 + L, y0 + 24), (x0, y0 + 24)], ep=1.2, ferme=True, fond=(0.9, 0.9, 0.9)); d.texte(x0 + L / 2, y0 + 15, titre, 26, police='Arial-B')
    d.texte(x0, y0 + 31, 'Numéro ______', 11, ancre='s'); d.texte(x0 + L - d.largeur_texte('Date : ____________________', 11), y0 + 31, 'Date : ____________________', 11, ancre='s')
    d.ligne([(x0, y0 + 34), (x0 + L, y0 + 34)], ep=0.8); zones = {2: [(0, 0, 1, 1), (1, 0, 1, 1)], 3: [(0, 0, 1, 1), (1, 0, 1, 0.5), (1, 0.5, 1, 0.5)], 4: [(0, 0, 1, 0.5), (1, 0, 1, 0.5), (0, 0.5, 1, 0.5), (1, 0.5, 1, 0.5)]}[articles]
    yz = y0 + 38; hz = y0 + H - yz; lc = (L - 8) / 2; il = 9.0
    for cx, fy, _, fh in zones:
        x, y, h = x0 + cx * (lc + 8), yz + fy * hz + 2, fh * hz - 6
        d.ligne([(x, y + 9), (x + lc, y + 9)], ep=0.9); d.texte(x, y + 3.5, 'Titre :', 8, ancre='s'); hi = min(42.0, h * 0.3)
        d.ligne([(x, y + 13), (x + lc, y + 13), (x + lc, y + 13 + hi), (x, y + 13 + hi)], ep=0.4, tirets=(1, 1.2), ferme=True); d.texte(x + lc / 2, y + 13 + hi / 2 + 1, 'dessin ou photo', 8)
        for j in range(int((h - hi - 30) / il)): d.ligne([(x, y + hi + 24 + j * il), (x + lc, y + hi + 24 + j * il)], ep=0.25)
        d.texte(x, y + h - 1, 'Écrit par : ____________________', 9, ancre='s')
    d.ligne([(x0 + lc + 4, yz), (x0 + lc + 4, y0 + H)], ep=0.3)
    return (None if dessin else d.sauver(base)), articles, il

def planche_bd(base, rangees=(2, 3, 2), titre=True, dessin=None):
    """G30 : planche de bande dessinée vide. rangees : nombre de cases de chaque bande, de haut en bas
    (par exemple (2, 3, 2)) ; titre=True réserve un bandeau pour le titre et le nom de l'auteur·e.
    Renvoie (chemin du PDF, nombre de cases, hauteur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); g = 5.0; haut = 20.0 if titre else 0.0
    if titre: _cadre_arrondi(d, x0, y0, L, 15, r=4, ep=0.9); d.texte(x0 + 4, y0 + 9.5, 'Titre :', 11, ancre='s', police='Arial-B'); d.texte(x0 + L - 62, y0 + 9.5, 'Par :', 11, ancre='s', police='Arial-B')
    hb = (H - haut - g * (len(rangees) - 1)) / len(rangees); n = 0
    for j, nb in enumerate(rangees):
        lc = (L - g * (nb - 1)) / nb
        for i in range(nb):
            x, y = x0 + i * (lc + g), y0 + haut + j * (hb + g); d.ligne([(x, y), (x + lc, y), (x + lc, y + hb), (x, y + hb)], ep=1.2, ferme=True); n += 1
            d.texte(x + 3, y + 5, str(n), 8, ancre='s')
    return (None if dessin else d.sauver(base)), n, round(hb, 1)

def plan_expose(base, parties=3, titre='Mon exposé', dessin=None):
    """G31 : plan d'exposé sur une page : sujet et question de départ, deux à quatre parties (idée principale, mots-clés,
    image à montrer), conclusion, sources. Renvoie (chemin du PDF, nombre de parties, hauteur d'une partie en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert 2 <= parties <= 4
    haut = _bandeau(d, titre, 'Prépare ton exposé : une idée par partie, quelques mots-clés, pas de phrases entières.')
    def bloc(y, h, nom, lignes):
        _cadre_arrondi(d, x0, y, L, h, r=4, ep=0.8); d.texte(x0 + 4, y + 6.5, nom, 11, ancre='s', police='Arial-B')
        for j in range(lignes): d.ligne([(x0 + 4, y + 15 + j * 9), (x0 + L - 4, y + 15 + j * 9)], ep=0.25)
    y = y0 + haut; d.texte(x0, y + 5, 'Prénom : ____________________', 12, ancre='s'); y += 9
    bloc(y, 28, 'Mon sujet et ma question de départ', 2); y += 31; hp = (y0 + H - y - 31 - 22 - 3 * (parties + 1)) / parties
    for k in range(parties):
        _cadre_arrondi(d, x0, y, L, hp, r=4, ep=0.8); d.texte(x0 + 4, y + 6.5, f'Partie {k + 1} : mon idée principale', 11, ancre='s', police='Arial-B'); li = hp - 14
        d.ligne([(x0 + L - 4 - li, y + 10), (x0 + L - 4, y + 10), (x0 + L - 4, y + 10 + li - 2), (x0 + L - 4 - li, y + 10 + li - 2)], ep=0.4, tirets=(1, 1.2), ferme=True); d.texte(x0 + L - 4 - li / 2, y + 10 + li / 2, 'image à montrer', 8)
        for j in range(int((hp - 12) / 9)): d.ligne([(x0 + 4, y + 16 + j * 9), (x0 + L - 10 - li, y + 16 + j * 9)], ep=0.25)
        y += hp + 3
    bloc(y, 31, 'Ma conclusion : ce qu’il faut retenir', 2); y += 34; bloc(y, 22, 'Mes sources (livre, site, personne interrogée)', 1)
    return (None if dessin else d.sauver(base)), parties, round(hp, 1)
```

#### 21 novembre 2026 : bande de lignes d'écriture romandes dans une fiche (R1c)

`bande_lignage` dessine avec la classe `Dessin` (R11) une bande de une à douze lignes d'écriture au lignage romand, de la largeur utile de la fiche (16 cm par défaut) : le même tracé que la page G22, sans en-tête. Elle remplace les lignes simples R1a dans une zone d'écriture quand l'enseignant·e de 1P à 4P le demande ; l'image PNG s'insère à l'échelle 1 avec `inserer_image(doc, chemin, largeur_cm=16)`. Le bloc se place après `Dessin` et `inserer_image`.

**Test (21.11.2026)** : bandes de trois lignes produites en modules de 7 mm et de 4 mm, en noir et blanc et en couleur, et regardées sur le rendu ; insertion dans un .docx contrôlée (largeur de 16 cm) ; non imprimé, non testé en classe ; modules à confirmer avec les cahiers de l'établissement.

```
# ---------- Pictogramme de consigne composé : le geste et le mot visé (21.11.2026) ----------
def pictogramme_consigne(base, geste='entoure', mot='verbe', hauteur_mm=13.0, dpi=300):
    """Pictogramme qui porte la consigne entière : le mot visé (« verbe », « nom », « sujet », un son…) avec le geste
    à faire dessus. geste : 'entoure' (ovale), 'encadre' (rectangle), 'souligne' (trait dessous), 'barre' (trait
    en travers). Remplace le pictogramme générique « abc » quand la consigne vise une chose précise ; se place à
    gauche de la consigne écrite, qu'il ne remplace jamais (MP-C-02). Renvoie (chemin du PNG, largeur en cm) ;
    insertion à l'échelle : inserer_image(doc, chemin, largeur_cm=largeur)."""
    assert geste in ('entoure', 'encadre', 'souligne', 'barre'), 'geste inconnu : ' + geste
    t = hauteur_mm * 1.25; d0 = Dessin(60, 20); lm = d0.largeur_texte(mot, t, 'Arial-B'); H = hauteur_mm; L = lm + H * 1.1; d = Dessin(L, H)
    cx, cy = L / 2, H / 2; d.texte(cx, cy + t * 0.125, mot, t, police='Arial-B')
    if geste == 'entoure': d.ligne([(cx + (L / 2 - 0.8) * math.cos(a * math.pi / 30), cy + (H / 2 - 0.8) * math.sin(a * math.pi / 30)) for a in range(60)], ep=0.8, ferme=True)
    elif geste == 'encadre': d.ligne([(0.8, 0.8), (L - 0.8, 0.8), (L - 0.8, H - 0.8), (0.8, H - 0.8)], ep=0.8, ferme=True)
    elif geste == 'souligne': d.ligne([(cx - lm / 2, H - 1.6), (cx + lm / 2, H - 1.6)], ep=0.9)
    else: d.ligne([(cx - lm / 2 - 1, H - 2.0), (cx + lm / 2 + 1, 2.0)], ep=0.9)
    d.sauver(base)
    return d.png(base, dpi), round(L / 10, 2)

# ---------- R1c : bande de lignes d'écriture romandes, à insérer dans une fiche (21.11.2026) ----------
def bande_lignage(base, lignes=3, module_mm=7.0, couleurs=False, largeur_mm=160.0, dpi=300):
    """R1c : bande de lignes d'écriture au lignage romand, pour une zone d'écriture d'une fiche (1P à 4P, si
    l'enseignant·e la préfère aux lignes simples R1a). Même tracé que la page G22 : plafond et plancher en
    pointillés, ligne du corps en trait fin, ligne de base en trait épais. module_mm : 7 pour l'entrée dans
    l'écriture, 4 ensuite. couleurs=True colore les couloirs ciel, herbe, terre (impression en couleur).
    Écrit base.svg, base.pdf et base.png ; renvoie (chemin du PNG, hauteur en cm). Insertion à l'échelle 1 :
    inserer_image(doc, chemin, largeur_cm=largeur_mm / 10)."""
    m = module_mm; assert 2 <= m <= 10, 'module de 2 à 10 mm'; assert 1 <= lignes <= 12, '1 à 12 lignes'
    esp = max(4.0, 1.2 * m); H = lignes * 3 * m + (lignes - 1) * esp + 1.0; L = largeur_mm; d = Dessin(L, H)
    for i in range(lignes):
        y = 0.5 + i * (3 * m + esp)
        if couleurs:
            for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(0, y + k * m), (L, y + k * m), (L, y + (k + 1) * m), (0, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
        d.ligne([(0, y), (L, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(0, y + m), (L, y + m)], ep=0.25)
        d.ligne([(0, y + 2 * m), (L, y + 2 * m)], ep=0.55); d.ligne([(0, y + 3 * m), (L, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    d.sauver(base)
    return d.png(base, dpi), round(H / 10, 2)
```

#### Exemple d'usage (fiche, puis jeu)

```
doc = Document(); page_a4(doc, police="Arial", taille=14); styles_fiche(doc, 14)
entete(doc, "Le passé composé", "J'écris un verbe au passé composé avec ses deux parties.")  # R7 : la phrase seule
paragraphe(doc, "1\tÉcris la phrase au passé composé.", "Fiche-Consigne")
paragraphe(doc, "a) Nous jouons au ballon.", "Fiche-Données")
lignes_ecriture(doc, 2)                                   # R1a : 2 vraies lignes de 1 cm
ligne_tabulation(doc, "Le matin, j'ai ", "Fiche-Données")  # R1b : amorce + ligne
paragraphe(doc, "b) Hier, tu " + lacune(6) + " (chanter).", "Fiche-Lacune")  # R2
# Jeu : dominos = [(réponse, question)] dans l'ordre de la boucle
verifier_domino_boucle(dominos, solution)                 # V11
def regle_du_jeu(cellule, largeur):                       # un exemplaire de la règle (liste regle)
    cellule.paragraphs[0].text = "Règle du jeu"
    for i, e in enumerate(regle, 1):
        cellule.add_paragraph(f"{i}. {e}")
planche_A5(doc, regle_du_jeu)                              # R15 : deux exemplaires A5 sur une feuille A4
nouvelle_section_a4(doc)                                   # retour à l'A4 pour la planche de pièces
ordre = melanger_sans_voisins(dominos, graine=3)           # MP-J-03
planche_pieces(doc, [[[[(r, {"b": True})]], [q[0], f"({q[1]})"]] for r, q in ordre],
               mention="Boucle Lune · 16 dominos · à découper sur les pointillés")  # R8
```

**Exemple de vérification d'un domino-boucle (V11)** : script du test du 30.10.2026. Il calcule les formes du présent (verbes en -er réguliers et verbes en -ir du type finir), construit deux boucles, vérifie l'unicité de chaque forme, l'unicité de la réponse à chaque question et la fermeture, puis mélange l'ordre d'impression sans voisins.

```
"""Données du domino-boucle : conjugaison calculée, boucles construites et vérifiées."""
import random

PERS = {'je': 1, 'tu': 2, 'il': 3, 'elle': 3, 'on': 3, 'nous': 4, 'vous': 5, 'ils': 6, 'elles': 6}
GN = {'Tom et moi': 4, 'Mes amies': 6, 'Le chat': 3, 'Lina et toi': 5, 'Mes parents': 6,
      'Le bébé': 3, 'Léa et moi': 4, 'Les arbres': 6, 'Ma tante': 3, 'Noé et toi': 5, 'Les élèves': 6}
PRONOM_DE = {1: 'je', 2: 'tu', 3: 'il, elle, on', 4: 'nous', 5: 'vous', 6: 'ils, elles'}

def personne(sujet):
    return PERS.get(sujet) or GN[sujet]

def groupe(verbe):
    return 'er' if verbe.endswith('er') else 'ir'

def present(verbe, p):
    """Présent de l'indicatif : verbes réguliers en -er (sans -cer, -ger, -yer, -eler, -eter)
    et verbes en -ir du type finir (2e groupe)."""
    rad = verbe[:-2]
    if groupe(verbe) == 'er':
        assert not verbe.endswith(('cer', 'ger', 'yer', 'eler', 'eter')), verbe
        return rad + ['e', 'es', 'e', 'ons', 'ez', 'ent'][p - 1]
    return rad + ['is', 'is', 'it', 'issons', 'issez', 'issent'][p - 1]

def terminaison(verbe, p):
    return present(verbe, p)[len(verbe) - 2:]

# Items (sujet, verbe) — 4 verbes × 4 formes distinctes par boucle
LUNE = [('je', 'chanter'), ('tu', 'chanter'), ('nous', 'chanter'), ('elles', 'chanter'),
        ('on', 'jouer'), ('tu', 'jouer'), ('vous', 'jouer'), ('ils', 'jouer'),
        ('je', 'choisir'), ('elle', 'choisir'), ('nous', 'choisir'), ('ils', 'choisir'),
        ('tu', 'remplir'), ('il', 'remplir'), ('vous', 'remplir'), ('elles', 'remplir')]

SOLEIL = [('je', 'danser'), ('Tom et moi', 'danser'), ('Mes amies', 'danser'), ('tu', 'danser'),
          ('Le chat', 'regarder'), ('tu', 'regarder'), ('Lina et toi', 'regarder'), ('Mes parents', 'regarder'),
          ('je', 'grandir'), ('Le bébé', 'grandir'), ('Léa et moi', 'grandir'), ('Les arbres', 'grandir'),
          ('tu', 'réussir'), ('Ma tante', 'réussir'), ('Noé et toi', 'réussir'), ('Les élèves', 'réussir')]

def boucle(items, graine):
    """Ordre circulaire : groupes alternés (-er / -ir), jamais deux fois le même sujet de suite."""
    rng = random.Random(graine)
    er = [i for i in items if groupe(i[1]) == 'er']
    ir = [i for i in items if groupe(i[1]) == 'ir']
    for _ in range(10000):
        rng.shuffle(er); rng.shuffle(ir)
        seq = [x for pair in zip(er, ir) for x in pair]
        ok = all(seq[k][0] != seq[(k + 1) % len(seq)][0] and seq[k][1] != seq[(k + 1) % len(seq)][1]
                 for k in range(len(seq)))
        # éviter deux occurrences consécutives du même verbe à deux positions d'écart (variété)
        ok = ok and all(seq[k][1] != seq[(k + 2) % len(seq)][1] for k in range(len(seq)))
        if ok:
            return seq
    raise RuntimeError('pas de boucle')

def dominos(seq):
    """Domino k = [forme de l'item k | item k+1] ; le dernier renvoie au premier."""
    n = len(seq)
    return [(present(seq[k][1], personne(seq[k][0])), seq[(k + 1) % n]) for k in range(n)]

def verifier(seq, nom):
    ds = dominos(seq)
    formes = [d[0] for d in ds]
    assert len(set(formes)) == len(formes), f'{nom} : formes en double'
    # chaque moitié droite a exactement une moitié gauche correspondante
    for d in ds:
        s, v = d[1]
        rep = present(v, personne(s))
        assert formes.count(rep) == 1, (nom, d)
    # la chaîne parcourue depuis n'importe quel domino revient au départ après n poses
    par_forme = {d[0]: d for d in ds}
    d = ds[0]
    for _ in range(len(ds)):
        s, v = d[1]
        d = par_forme[present(v, personne(s))]
    assert d == ds[0]
    return ds

def ordre_impression(ds, graine):
    rng = random.Random(graine)
    o = ds[:]
    while True:
        rng.shuffle(o)
        # aucune paire voisine sur la planche ne doit être une paire voisine de la boucle
        pos = {d: i for i, d in enumerate(ds)}
        if all(abs(pos[o[k]] - pos[o[k + 1]]) % len(ds) not in (1, len(ds) - 1) for k in range(len(o) - 1)):
            return o

SEQ_LUNE = boucle(LUNE, 5)
SEQ_SOLEIL = boucle(SOLEIL, 11)
DOM_LUNE = verifier(SEQ_LUNE, 'Lune')
DOM_SOLEIL = verifier(SEQ_SOLEIL, 'Soleil')
IMP_LUNE = ordre_impression(DOM_LUNE, 3)
IMP_SOLEIL = ordre_impression(DOM_SOLEIL, 7)

# Fiche « Après le jeu » : items G3 (sujet, verbe, début, fin)
FICHE = [('a', 'Je ', 'marcher', ' jusqu’à l’école.', 'je'),
         ('b', 'Tu ', 'remplir', ' ta gourde.', 'tu'),
         ('c', 'Mes cousins ', 'bâtir', ' une cabane.', 'ils'),
         ('d', 'Vous ', 'dessiner', ' un dragon.', 'vous'),
         ('e', 'Ma voisine ', 'nourrir', ' son chat.', 'elle')]

if __name__ == '__main__':
    for nom, seq, ds in (('LUNE', SEQ_LUNE, DOM_LUNE), ('SOLEIL', SEQ_SOLEIL, DOM_SOLEIL)):
        print(nom)
        for k, d in enumerate(ds, 1):
            print(f'{k:2d}  [{d[0]:13s}| {d[1][0]} ({d[1][1]})]')
    for it in FICHE:
        print(it[0], present(it[2], PERS[it[4]]))
    for v in ('parler', 'finir'):
        print([present(v, p) for p in range(1, 7)])
```
