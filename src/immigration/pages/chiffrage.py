"""Le chiffrage : les plus et les moins du programme, comparés à aujourd'hui.

Cette page n'écrit aucun montant. Elle les demande au module
``immigration.chiffrage``, qui les calcule à partir d'hypothèses écrites une
seule fois — chacune avec sa fourchette et ce qui la justifie. Les phrases qui
tirent une conclusion du calcul (« au mieux, la première année s'équilibre »,
« le signe du solde tient d'abord à la part de travail au noir ») sont
VÉRIFIÉES à la construction : si une hypothèse corrigée venait à les démentir,
la construction échouerait plutôt que de publier une phrase fausse.
"""

from __future__ import annotations

import math
import re
from html import escape

from .. import chiffrage as c
from .. import gabarit as g

PAGE = {
    "fichier": "chiffrage.html",
    "titre": "Le chiffrage — les plus et les moins du programme",
    "description": (
        "Ce que chaque engagement du programme libéral coûte ou rapporte aux "
        "finances publiques, comparé à la situation actuelle : poste par "
        "poste, année par année, deux scénarios, et chaque hypothèse écrite."),
}

MOINS = "−"
INSECABLE = " "

# ---------------------------------------------------------------------------
# Mise en forme. Des ordres de grandeur, pas des décimales : une fourchette de
# plusieurs centaines de millions ne se lit pas au million près.
# ---------------------------------------------------------------------------


def milliers(n: float, decimales: int = 0) -> str:
    """Un nombre à la française : espace insécable, virgule décimale."""
    return f"{abs(n):,.{decimales}f}".replace(",", INSECABLE).replace(".", ",")


_milliers = milliers


def _arrondi(v: float) -> float:
    """L'arrondi qu'autorise l'incertitude, selon l'ordre de grandeur.

    Au pas le plus proche, les moitiés loin de zéro — « 1,5 » donne 2, et
    non 2 ici et 0 là selon la parité, comme le fait ``round``. Sous un
    million, au dixième : un poste de 0,5 M€ n'est pas nul.
    """
    a = abs(v)
    if a < 1:
        pas = 0.1
    elif a < 20:
        pas = 1
    elif a < 100:
        pas = 5
    else:
        pas = 10
    return math.copysign(math.floor(a / pas + 0.5) * pas, v)


def meur(v: float, signe: bool = True, unite: bool = True) -> str:
    """Un montant en millions d'euros, signé : « + 45 M€ », « − 1,2 Md€ »."""
    r = _arrondi(v)
    if abs(r) < 0.05:
        return "≈" + INSECABLE + "0"
    if abs(r) >= 1000:
        corps = _milliers(r / 1000, 1).rstrip("0").rstrip(",")
        suffixe = "Md€"
    else:
        corps = _milliers(r, 1 if abs(r) < 1 else 0)
        suffixe = "M€"
    texte = corps + (INSECABLE + suffixe if unite else "")
    if signe:
        texte = ("+" if r > 0 else MOINS) + INSECABLE + texte
    return texte


def _classe(bas: float, haut: float) -> str:
    rb, rh = _arrondi(bas), _arrondi(haut)
    if abs(rb) < 0.05 and abs(rh) < 0.05:
        return "nul"
    if rb >= 0 and rh >= 0:
        return "plus"
    if rb <= 0 and rh <= 0:
        return "moins"
    return "incertain"


def fourchette(bas: float, haut: float, absolu: bool = False) -> str:
    """« − 540 à + 820 M€ », avec la pastille de son signe.

    Deux bornes que l'arrondi confond s'écrivent en un seul montant. Avec
    ``absolu``, les montants perdent leur signe — pour une phrase qui le dit
    déjà : « une recette de 150 à 190 M€ », « coûte 85 à 150 M€ » — et
    gardent la pastille qui le montre.
    """
    bas, haut = min(bas, haut), max(bas, haut)
    if absolu and bas < 0 < haut:
        raise ValueError("une fourchette qui passe par zéro garde ses signes")
    classe = _classe(bas, haut)
    signe = not absolu
    if absolu:
        bas, haut = sorted((abs(bas), abs(haut)))
    if meur(bas, signe) == meur(haut, signe):
        texte = meur(bas, signe)
    elif (abs(_arrondi(bas)) >= 1000) == (abs(_arrondi(haut)) >= 1000):
        texte = f"{meur(bas, signe, unite=False)} à {meur(haut, signe)}"
    else:
        texte = f"{meur(bas, signe)} à {meur(haut, signe)}"
    return f'<span class="montant {classe}">{texte}</span>'


def _nombre(v: float, unite: str) -> str:
    if unite == "%":
        return _milliers(v * 100, 0 if abs(v * 100 - round(v * 100)) < 1e-9 else 1)
    decimales = 0 if abs(v - round(v)) < 1e-9 else 1
    return _milliers(v, decimales)


def valeur(h: c.Hypothese) -> str:
    """La valeur d'une hypothèse, bornes et unité : « 40 à 80 % ».

    Une fourchette qui passe par zéro porte ses signes, « − 100 à + 200 € » :
    sans eux, on lirait une borne basse positive.
    """
    def signe(v: float) -> str:
        if h.bas >= 0 or v == 0:
            return ""
        return ("+" if v > 0 else MOINS) + INSECABLE

    unite = {"%": INSECABLE + "%", "€": INSECABLE + "€",
             "M€": INSECABLE + "M€", "mois": INSECABLE + "mois"}.get(h.unite, "")
    if h.bas == h.haut:
        return signe(h.bas) + _nombre(h.bas, h.unite) + unite
    return (signe(h.bas) + _nombre(h.bas, h.unite) + " à "
            + signe(h.haut) + _nombre(h.haut, h.unite) + unite)


def insecables(texte: str) -> str:
    """Les espaces qu'on ne coupe pas : « 547 € », « 263 125 », « 46 % ».

    Appliqué aux textes du chiffrage seulement, jamais à une page entière :
    un attribut comme ``viewBox="0 0 800 316"`` se prendrait pour un nombre.
    """
    texte = re.sub(r"(?<=\d) (?=\d{3}\b)", INSECABLE, texte)
    texte = re.sub(r"(?<=\d) (?=€|%|M€|Md€|(?:mois|jours|ans)\b)",
                   INSECABLE, texte)
    return texte


def remplir(texte: str) -> str:
    """Remplace chaque ``{cle}`` par la valeur de l'hypothèse — en gras."""
    for cle in dict.fromkeys(c.citees(texte)):
        texte = texte.replace("{" + cle + "}",
                              f"<strong>{valeur(c.HYPOTHESES[cle])}</strong>")
    return insecables(texte)


def _renvoi_hypothese(h: c.Hypothese) -> str:
    return g.renvoi(h.chiffre) if h.chiffre else ""


# ---------------------------------------------------------------------------
# Ce que le calcul doit confirmer pour que la page puisse l'écrire
# ---------------------------------------------------------------------------


def constats() -> dict[str, object]:
    """Les conclusions que la page tire du calcul, vérifiées une à une."""
    soldes = {a: c.solde(a) for a in c.ANNEES}
    etat = {a: c.fourchette(c.postes_du_bloc("etat"), a) for a in c.ANNEES}
    travail = {a: c.fourchette(c.postes_du_bloc("travail"), a) for a in c.ANNEES}
    poids = c.poids_des_hypotheses(5)
    gratuite = next(p for p in c.POSTES if p.cle == "gratuite-renouvellements")
    moins_durables = [p for p in c.postes_du_bloc("etat")
                      if p.cle not in ("eloignements", "proteges-plus-tot")]

    # 1. La première année coûte, quel que soit le scénario — à l'arrondi près.
    assert soldes[1][1] < 20, "l'année 1 n'est plus déficitaire"
    # 2. Le solde prudent reste négatif sur tout l'horizon : le programme ne
    #    se finance pas tout seul dans le pire des cas.
    assert all(soldes[a][0] < 0 for a in c.ANNEES), "prudent devenu positif"
    # 3. Le solde favorable devient nettement positif à terme.
    assert soldes[5][1] > 100, "le scénario favorable ne rapporte plus"
    # 4. La gratuité des renouvellements est, dans les deux scénarios, le plus
    #    gros moins durable de l'État en année 5 — éloignements et droit
    #    commun des personnes protégées mis à part, qui dépendent d'un curseur
    #    et d'une hypothèse de comportement.
    for nom in ("prudent", "favorable"):
        assert (min(moins_durables, key=lambda p: c.montant(p, 5, nom)) is
                gratuite), f"la gratuité n'est plus le premier moins ({nom})"
    # 5. Ce qui fait le signe du solde à terme : la part de travail au noir
    #    parmi les personnes régularisées, puis leurs prestations.
    assert poids[0][0] == "part-non-declares", poids[:3]
    assert poids[1][0] == "prestations-regularise", poids[:3]
    # 6. Le travail déclaré coûte un peu dans le scénario prudent, rapporte
    #    nettement dans le favorable : c'est ce que dit « En bref ».
    assert -150 < travail[5][0] < 0 < 100 < travail[5][1], travail[5]
    return {"soldes": soldes, "etat": etat, "travail": travail,
            "poids": poids, "gratuite": gratuite}


# ---------------------------------------------------------------------------
# Les blocs de la page
# ---------------------------------------------------------------------------


def _ligne_poste(p: c.Poste) -> list[str]:
    return [escape(p.libelle), remplir(p.aujourdhui), remplir(p.avec),
            fourchette(*c.fourchette([p], 1)), fourchette(*c.fourchette([p], 5))]


def _tableau_engagement(cle: str) -> str:
    postes = c.postes_de_l_engagement(cle)
    titre = c.ENGAGEMENTS[cle]
    numero = f"Engagement {cle} — " if cle.isdigit() else ""
    pied = [["Solde", "", "", fourchette(*c.fourchette(postes, 1)),
             fourchette(*c.fourchette(postes, 5))]]
    return g.tableau(
        ["Poste", "Aujourd'hui", "Avec le programme", "Année 1", "Année 5"],
        [_ligne_poste(p) for p in postes],
        legende=f"{numero}{escape(titre)}. Montants annuels, du scénario "
                "prudent au scénario favorable.",
        classes_colonnes=["texte", "texte long", "texte long", "nombre",
                          "nombre"],
        pied=pied)


def _calcul_engagement(cle: str) -> str:
    items = "".join(
        f"<dt>{escape(p.libelle)}</dt><dd>{remplir(p.formule)}. "
        f"<span class=\"discret\">Rythme : {escape(p.quand)}.</span></dd>"
        for p in c.postes_de_l_engagement(cle))
    return g.depliant("Le calcul, ligne par ligne",
                      f'<dl class="gloses">{items}</dl>')


def _tableau_annees() -> str:
    def cellules(fonction) -> list[str]:
        return [fonction(a) for a in c.ANNEES]

    def plus(a: int) -> str:
        valeurs = [c.plus_et_moins(a, nom)[0] for nom in ("prudent", "favorable")]
        return fourchette(*valeurs)

    def moins(a: int) -> str:
        valeurs = [c.plus_et_moins(a, nom)[1] for nom in ("prudent", "favorable")]
        return fourchette(*valeurs)

    def bloc(nom: str):
        return lambda a: fourchette(*c.fourchette(c.postes_du_bloc(nom), a))

    def milieu(a: int) -> str:
        return fourchette(c.milieu(a), c.milieu(a))

    lignes = [
        ["Les plus : économies et recettes"] + cellules(plus),
        ["Les moins : dépenses et recettes perdues"] + cellules(moins),
    ]
    pied = [["Solde", *[fourchette(*c.solde(a)) for a in c.ANNEES]],
            ["<span class=\"dont\">dont ce que l'État fait autrement</span>"]
            + cellules(bloc("etat")),
            ["<span class=\"dont\">dont le travail déclaré</span>"]
            + cellules(bloc("travail")),
            ["<span class=\"dont\">pour mémoire : toutes les hypothèses au "
             "milieu de leur fourchette</span>", *cellules(milieu)]]
    return g.tableau(
        ["", *[f"Année {a}" for a in c.ANNEES]],
        lignes,
        legende="Le solde du programme année par année, en millions d'euros "
                "par an, du scénario prudent au scénario favorable. Les plus "
                "et les moins de chaque colonne sont ceux des deux scénarios "
                "du solde : ils s'additionnent.",
        classes_colonnes=["texte", "nombre", "nombre", "nombre", "nombre"],
        pied=pied)


def _tableau_hypotheses() -> str:
    natures = {"constat": "Constat", "estimation": "Estimation",
               "hypothese": "Hypothèse", "parametre": "Paramètre"}
    lignes = [[escape(h.libelle), valeur(h), natures[h.nature],
               insecables(escape(h.justification)) + _renvoi_hypothese(h)]
              for h in c.HYPOTHESES.values()]
    return g.tableau(
        ["Hypothèse", "Valeur", "Nature", "D'où elle vient"], lignes,
        legende=f"Les {len(c.HYPOTHESES)} hypothèses du chiffrage. Un "
                "<strong>constat</strong> se vérifie à sa source ; une "
                "<strong>estimation</strong> se refait à partir de chiffres "
                "publiés ; une <strong>hypothèse</strong> dit ce que personne "
                "ne mesure ; un <strong>paramètre</strong> est un réglage que "
                "la loi fixerait.",
        classes_colonnes=["texte", "nombre", "texte", "texte long"])


def _fourchettes_svg() -> str:
    """Les fourchettes de l'année 5, engagement par engagement.

    Une barre par engagement, de son montant le plus bas à son montant le
    plus haut ; la part à gauche de zéro est un moins, la part à droite un
    plus. Le graphique ne dit rien que les tableaux ne disent : il le fait
    voir. Chaque fourchette est écrite en toutes lettres dans une colonne à
    droite, alignée comme dans un tableau, et la couleur n'y ajoute que le
    signe, déjà écrit.
    """
    rangs = [(cle, c.ENGAGEMENTS[cle],
              c.fourchette(c.postes_de_l_engagement(cle), 5))
             for cle in c.ENGAGEMENTS]
    rangs.append(("solde", "Solde du programme", c.solde(5)))
    pas = 250
    mini = pas * int(min(min(b for _, _, (b, _) in rangs), 0) // pas)
    maxi = pas * int(-(-max(max(h for _, _, (_, h) in rangs), 0) // pas))
    largeur, gauche, colonne, marge = 800, 200, 170, 16
    haut_ligne, haut_tete = 34, 30
    trace = largeur - gauche - colonne - 2 * marge

    def x(v: float) -> float:
        return gauche + marge + (v - mini) / (maxi - mini) * trace

    def graduation(v: int) -> str:
        if v == 0:
            return "0"
        return ("+" if v > 0 else MOINS) + INSECABLE + _milliers(v)

    hauteur = haut_tete + haut_ligne * len(rangs) + 8
    svg = [f'<svg viewBox="0 0 {largeur} {hauteur}" role="img" '
           'aria-labelledby="fourchettes-titre fourchettes-desc">',
           '<title id="fourchettes-titre">Ce que chaque engagement coûte ou '
           'rapporte la cinquième année, en millions d\'euros</title>',
           '<desc id="fourchettes-desc">Pour chaque engagement, une barre va '
           'du scénario prudent au scénario favorable ; à gauche de zéro, un '
           'coût, à droite, un gain. Les montants sont écrits à droite de '
           'chaque barre, et détaillés dans les tableaux qui suivent.</desc>']
    for v in range(mini, maxi + 1, pas):
        classe = "axe" if v == 0 else "grille"
        svg.append(f'<line class="{classe}" x1="{x(v):.1f}" x2="{x(v):.1f}" '
                   f'y1="{haut_tete - 8}" y2="{hauteur - 4}"/>')
        svg.append(f'<text class="graduation" x="{x(v):.1f}" '
                   f'y="{haut_tete - 14}" text-anchor="middle">'
                   f'{graduation(v)}</text>')
    svg.append(f'<text class="graduation" x="{largeur - 4}" '
               f'y="{haut_tete - 14}" text-anchor="end">M€ par an</text>')
    for i, (cle, libelle, (bas, haut)) in enumerate(rangs):
        y = haut_tete + i * haut_ligne + haut_ligne / 2
        total = cle == "solde"
        epaisseur = 14 if total else 10
        haut_barre = y - epaisseur / 2
        classe = " total" if total else ""
        numero = f"{cle}. " if cle.isdigit() else ""
        svg.append(f'<text class="etiquette{classe}" x="{gauche - 8}" '
                   f'y="{y + 4:.1f}" text-anchor="end">'
                   f'{escape(numero + libelle)}</text>')
        if bas < -0.5:
            fin = min(haut, 0)
            svg.append(f'<rect class="barre-moins" x="{x(bas):.1f}" '
                       f'y="{haut_barre:.1f}" '
                       f'width="{max(x(fin) - x(bas), 2):.1f}" '
                       f'height="{epaisseur}"/>')
        if haut > 0.5:
            debut = max(bas, 0)
            svg.append(f'<rect class="barre-plus" x="{x(debut):.1f}" '
                       f'y="{haut_barre:.1f}" '
                       f'width="{max(x(haut) - x(debut), 2):.1f}" '
                       f'height="{epaisseur}"/>')
        if abs(bas) <= 0.5 and abs(haut) <= 0.5:
            svg.append(f'<rect class="barre-nulle" x="{x(0) - 1:.1f}" '
                       f'y="{haut_barre:.1f}" width="2" height="{epaisseur}"/>')
        texte = fourchette(bas, haut).split(">", 1)[1].rsplit("<", 1)[0]
        svg.append(f'<text class="valeur{classe}" x="{largeur - 4}" '
                   f'y="{y + 4:.1f}" text-anchor="end">{texte}</text>')
    svg.append("</svg>")
    return ('<figure class="fourchettes"><div class="defilant">'
            + "".join(svg) + "</div>"
            '<figcaption><ul class="legende">'
            '<li><span class="pastille ecart-moins" aria-hidden="true"></span>'
            "Part de la fourchette qui est un coût</li>"
            '<li><span class="pastille ecart-plus" aria-hidden="true"></span>'
            "Part qui est un gain</li></ul></figcaption></figure>")


def construire() -> str:
    c.verifier()
    k = constats()
    s1, s5 = k["soldes"][1], k["soldes"][5]

    corps = g.affiche(
        "La proposition",
        "Les plus, <span class=\"serif\">les moins</span>",
        "Ce que chaque engagement coûte ou rapporte aux finances publiques, "
        "comparé à ce que l'État dépense et encaisse aujourd'hui. Deux "
        "scénarios plutôt qu'un chiffre, chaque hypothèse écrite, et des "
        "totaux que personne n'a tapés : ils sont calculés.")

    gratuite = k["gratuite"]
    regul = next(p for p in c.POSTES if p.cle == "regularises-prelevements")
    corps += g.reperes([
        ("Solde la première année", fourchette(*s1),
         "Du scénario prudent au scénario favorable, par an."),
        ("Solde la cinquième année", fourchette(*s5),
         "Quand le titre de quatre ans a fait un tour complet."),
        ("Le plus gros moins durable", fourchette(*c.fourchette([gratuite], 5)),
         "La gratuité des renouvellements : une recette perdue chaque année."
         + g.renvoi("taxes-titres")),
        ("Le plus gros plus", fourchette(*c.fourchette([regul], 5)),
         "Les cotisations des personnes régularisées, en année 5."
         + g.renvoi("prelevements-smic")),
    ])

    corps += g.note(
        "<p><strong>Ce chiffrage est calculé, pas écrit.</strong> Chaque "
        "montant de cette page sort d'un calcul fait à partir de "
        f"{len(c.HYPOTHESES)} hypothèses, chacune avec sa borne basse, sa "
        "borne haute et ce qui la justifie ; les chiffres publiés y sont lus "
        "dans le registre du site, et non recopiés. Les totaux ne sont écrits "
        "nulle part : ils sont sommés. Et les phrases qui tirent une "
        "conclusion du calcul sont vérifiées à la construction du site — si "
        "une hypothèse corrigée venait à les démentir, la page ne se "
        "construirait plus.</p>", "resume")

    corps += g.plan([
        ("bref", "En bref"),
        ("aujourdhui", "Aujourd'hui"),
        ("engagements", "Engagement par engagement"),
        ("annees", "Année par année"),
        ("sans-euros", "Ce qui ne se compte pas en euros"),
        ("flux", "Si les flux réagissent"),
        ("mentir", "Ce qui nous ferait mentir"),
        ("hypotheses", "Les hypothèses"),
        ("pas-compte", "Ce que ce chiffrage ne compte pas"),
        ("methode", "La méthode"),
    ])

    # ---------------------------------------------------------------- en bref
    e1, e5 = k["etat"][1], k["etat"][5]
    t5 = k["travail"][5]
    taxes_perdues = c.fourchette(
        [p for p in c.POSTES
         if p.cle in ("gratuite-renouvellements", "renouvellements-taxes")], 5)
    corps += '<h2 id="bref">En bref</h2>'
    corps += g.cle(
        "Le programme coûte-t-il, ou rapporte-t-il ?",
        "<strong>Il coûte d'abord</strong> : la première année, de "
        f"{fourchette(*s1)} — au mieux, il s'équilibre. <strong>À terme, tout "
        "dépend "
        "d'une question</strong> : les personnes que le programme régularise "
        "travaillaient-elles au noir, ou déjà sous une autre identité ? Le "
        f"solde de la cinquième année va de {fourchette(*s5)}.",
        corps="<p><strong>Ce que l'État fait autrement</strong> — délais, "
              "titre de quatre ans, asile jugé vite, guichet garanti, "
              "renouvellements gratuits, éloignements — pèse "
              f"{fourchette(*e1)} la première année et {fourchette(*e5)} la "
              "cinquième. Les renouvellements gratuits en sont le plus gros "
              "moins durable : avec ceux que le titre de quatre ans supprime, "
              f"une recette de {fourchette(*taxes_perdues, absolu=True)} par "
              "an que l'État perçoit aujourd'hui, et que le programme lui "
              "retire. Juger l'asile vite fait économiser l'hébergement et "
              "l'allocation, mais ouvre plus tôt le RSA aux personnes "
              "protégées et l'aide médicale aux déboutées ; et l'exécution "
              "effective des rejets coûte cher, parce qu'un éloignement forcé "
              "passe le plus souvent par la rétention.</p>"
              "<p><strong>Ce que change le travail déclaré</strong> — des "
              "personnes déjà présentes qui cotisent enfin en leur nom — "
              f"pèse {fourchette(*t5)} la cinquième année. C'est là que se "
              "joue le signe du solde, et nous ne le connaissons pas : si les "
              "personnes régularisées travaillaient surtout au noir et vivent "
              "seules, elles rapportent beaucoup plus qu'elles ne coûtent ; "
              "si elles cotisaient déjà sous une autre identité et ont des "
              "enfants en France, leur régularisation coûte un peu plus "
              "qu'elle ne rapporte.</p>"
              "<p><strong>Ce que nous en concluons.</strong> Ce programme "
              "n'est pas une source d'économies, et nous cessons de le "
              "présenter comme tel. Il coûte ses premières années ; il peut "
              "rapporter ensuite, s'il fait vraiment passer du travail au noir "
              "au travail déclaré — ce qui est son objet. C'est une réforme "
              "qu'on défend pour ce qu'elle change, pas pour ce qu'elle "
              "rapporterait au budget.</p>",
        identifiant="verdict")

    # ------------------------------------------------------------ aujourd'hui
    corps += """
<h2 id="aujourdhui">Aujourd'hui : ce que coûte ce que le programme change</h2>
<p>Le point de comparaison de tout ce chiffrage est la situation actuelle, à
droit constant. Voici ce qu'elle coûte et ce qu'elle rapporte, sur les seuls
postes que le programme modifie. Chaque chiffre renvoie à sa fiche.</p>
"""
    corps += g.tableau(
        ["Poste", "Aujourd'hui"],
        [["Taxes sur les titres de séjour",
          "De l'ordre de 200 M€ de recettes par an"
          + g.renvoi("taxes-titres") + ", dont près des trois quarts sur les "
          "renouvellements ; 250 € par renouvellement et 350 € par première "
          "délivrance depuis le 1er mai 2026" + g.renvoi("tarifs-titres")],
         ["Instruction des titres en préfecture",
          g.nombre("agents-etrangers") + " agents en équivalent temps plein, "
          "237 M€ de masse salariale ; 547 € par première délivrance selon "
          "l'État" + g.renvoi("cout-premier-titre")],
         ["Renouvellements",
          g.nombre("renouvellements") + " par an, dont "
          + g.nombre("renouvellements-travail-etudes")
          + " pour le travail ou les études"],
         ["Régularisations par le travail",
          g.nombre("aes-travail") + " en 2025, sur décision discrétionnaire"],
         ["Allocation des demandeurs d'asile",
          g.nombre("ada-credits") + " en 2026, 209 € par mois en moyenne"],
         ["Hébergement des demandeurs d'asile",
          g.nombre("hebergement-asile") + " programmées pour les demandeurs "
          "d'asile et les réfugiés ; environ 780 M€ par an pour les seules "
          "places des demandeurs"],
         ["Durée d'une demande d'asile",
          g.nombre("delai-asile") + " en moyenne, recours compris ; environ "
          "700 € par décision de l'OFPRA" + g.renvoi("ofpra-activite")
          + ", 1 330 € par décision de la CNDA" + g.renvoi("cnda-activite")],
         ["Éloignements forcés",
          "15 569 en 2025" + g.renvoi("eloignements") + " ; "
          + g.nombre("cout-eloignement") + " chacun hors rétention, et "
          + g.nombre("retention") + " de rétention en moyenne"],
         ["Contentieux des étrangers",
          "154 391 affaires nouvelles devant les tribunaux administratifs "
          "en 2025, soit " + g.nombre("contentieux-ta") + " du total"],
         ["Aide médicale de l'État",
          g.nombre("ame") + " bénéficiaires, 1,39 Md€ de dépense en 2024"],
         ["Mission « Immigration, asile et intégration »",
          g.nombre("mission-budget") + " de crédits votés pour 2026"]],
        legende="La situation actuelle, sur les postes que le programme "
                "change. Les recettes y figurent avec les dépenses : un "
                "chiffrage qui ne compte que l'une des deux colonnes est un "
                "argument, pas un chiffrage.",
        classes_colonnes=["texte", "texte long"])

    # ------------------------------------------------------- les engagements
    corps += """
<h2 id="engagements">Les plus et les moins, engagement par engagement</h2>
<p>Chaque ligne dit ce qui se passe aujourd'hui, ce que le programme change,
et ce que cela coûte ou rapporte chaque année, du scénario prudent au scénario
favorable. Un montant précédé de « + » est une économie ou une recette ; de
« − », une dépense ou une recette perdue. Sous chaque tableau, le calcul
ligne par ligne, avec les valeurs de ses hypothèses.</p>
"""
    corps += _fourchettes_svg()
    for cle, titre in c.ENGAGEMENTS.items():
        ancre = f"engagement-{cle}"
        intitule = f"{cle}. {titre}" if cle.isdigit() else titre
        corps += f'<h3 id="{ancre}">{escape(intitule)}</h3>'
        corps += _tableau_engagement(cle)
        corps += _calcul_engagement(cle)

    corps += g.note(
        "<p><strong>Pourquoi les bornes d'un solde ne sont pas la somme des "
        "bornes de ses lignes.</strong> Chaque solde est calculé dans deux "
        "scénarios cohérents : le prudent retient, pour chaque hypothèse, la "
        "borne qui dégrade le solde total de l'année ; le favorable, celle "
        "qui l'améliore. Une même hypothèse — la durée d'une demande d'asile, "
        "par exemple — joue en plus sur une ligne et en moins sur une autre : "
        "additionner les pires bornes de chaque ligne décrirait un monde "
        "impossible.</p>", "vigilance")

    # ------------------------------------------------------- année par année
    corps += """
<h2 id="annees">Année par année</h2>
<p>La loi est votée la première année et s'applique, en moyenne, à sa moitié ;
le titre de quatre ans ne supprime ses premiers renouvellements que la
deuxième année ; l'asile atteint six mois au bout de deux ans. D'où un
programme qui coûte avant de rapporter — s'il rapporte.</p>
"""
    corps += _tableau_annees()
    corps += g.cle(
        "Pourquoi s'arrêter à la cinquième année ?",
        "Parce que c'est là que le programme atteint son régime : le titre de "
        "quatre ans a fait un tour complet, et le nombre de personnes "
        "régularisées <em>plus tôt</em> qu'elles ne l'auraient été cesse à "
        "peu près de croître.",
        corps="<p>Sous le droit actuel, une partie de ces personnes aurait "
              "fini par être régularisée, au bout de trois à cinq ans de "
              "présence : le programme avance leur régularisation plus qu'il "
              "ne la crée. Prolonger la droite au-delà de cinq ans reviendrait "
              "à compter comme un gain du programme des cotisations que le "
              "droit actuel aurait fini par percevoir.</p>"
              "<p>Deux effets commencent justement après la cinquième année, "
              "et ce chiffrage ne les compte pas : les premières personnes "
              "régularisées accèdent alors au RSA et à la prime d'activité, "
              "et les cotisations de retraite versées depuis le premier jour "
              "commenceront, bien plus tard, à se payer en pensions. Nous les "
              "écrivons plus bas, dans ce que ce chiffrage ne compte pas.</p>",
        identifiant="horizon")

    # ------------------------------------------ ce qui ne se compte pas en €
    corps += """
<h2 id="sans-euros">Les plus et les moins qui ne se comptent pas en euros</h2>
<p>Un programme ne se juge pas à son seul solde budgétaire, et celui-ci moins
que tout autre : son objet est de rendre l'administration tenable et le
travail déclaré. Voici ce qu'il change en délais, en dossiers et en droits —
en plus, et en moins.</p>
"""
    renouv_evites = sorted(
        round(c._renouvellements_evites(c.scenario(nom, 5).__getitem__, 5),
              -4) for nom in ("prudent", "favorable"))
    corps += g.tableau(
        ["", "Aujourd'hui", "Avec le programme", "Sens"],
        [["Durée d'une demande d'asile",
          g.nombre("delai-asile") + " en moyenne, sans délai opposable",
          "Six mois au plus, recours compris, opposables", "Plus"],
         ["Travail des demandeurs d'asile",
          "Interdit six mois, puis sur autorisation : environ 2 % des "
          "demandeurs adultes en obtiennent une",
          "Autorisé dès le dépôt de la demande", "Plus"],
         ["Renouvellements de titres",
          g.nombre("renouvellements") + " par an, payants",
          f"{_milliers(renouv_evites[0])} à {_milliers(renouv_evites[1])} "
          "de moins par an, et gratuits",
          "Plus"],
         ["Délai d'instruction d'un titre",
          "Aucun délai garanti ; délais en hausse de 25 à 27 % en 2024 ; le "
          "silence vaut refus",
          "Huit semaines, quatre pour un renouvellement ; le silence vaut "
          "accord", "Plus"],
         ["Régularisation par le travail",
          g.nombre("aes-travail") + " en 2025, au cas par cas",
          "Un droit sur critères, contestable devant un juge — et "
          "nettement plus de régularisations : 50 000 de plus par an dans "
          "notre repère, les premières années", "Moins, aux yeux de "
          "beaucoup — et nous le disons"],
         ["Éloignements forcés",
          "15 569 en 2025" + g.renvoi("eloignements"),
          "4 000 de plus par an : plus de rétention, plus de contentieux",
          "Plus pour l'autorité de la loi, moins pour le budget"],
         ["Contentieux de procédure",
          "Référés pour obtenir un rendez-vous, recours contre des refus nés "
          "du silence",
          "Sans objet dès que les délais sont tenus", "Plus"],
         ["Attractivité",
          "Une porte du travail étroite, une demande d'asile longue",
          "Une porte du travail ouverte, une demande d'asile où l'on "
          "travaille : la France attire davantage — des salariés, et sans "
          "doute des demandeurs d'asile", "Plus et moins : voir ci-dessous"]],
        legende="Ce que le programme change, hors euros. La colonne « Sens » "
                "dit de quel côté nous rangeons chaque effet ; un lecteur "
                "peut ranger autrement la régularisation, les éloignements ou "
                "l'attractivité, et nous le comprenons.",
        classes_colonnes=["texte", "texte long", "texte long", "texte"])

    # ------------------------------------------------- si les flux réagissent
    corps += """
<h2 id="flux">Si les flux réagissent</h2>
<p>Ce chiffrage compte les personnes déjà présentes. Il ne compte pas celles
que la réforme pourrait attirer, parce que personne ne sait les compter — ni
nous, ni ceux qui promettent un « appel d'air ». Voici de quoi faire son
propre compte, tranche par tranche, dans un sens comme dans l'autre.</p>
"""
    fiches = []
    for s in c.SENSIBILITES:
        bas, haut = c.sensibilite(s)
        fiches.append(g.fiche(s.libelle, fourchette(bas, haut),
                              insecables(escape(s.explication))))
    corps += '<div class="fiches reperes">' + "".join(fiches) + "</div>"
    corps += g.depliant(
        "Le calcul de ces quatre tranches",
        '<dl class="gloses">' + "".join(
            f"<dt>{escape(s.libelle)}</dt><dd>{remplir(s.formule)}</dd>"
            for s in c.SENSIBILITES) + "</dl>")

    # ------------------------------------------------ ce qui nous ferait mentir
    poids = k["poids"][:6]
    corps += """
<h2 id="mentir">Ce qui nous ferait mentir</h2>
<p>Les hypothèses ne pèsent pas toutes autant. Voici celles qui déplacent le
plus le solde de la cinquième année quand on les fait passer d'une borne à
l'autre, toutes les autres restant au milieu de leur fourchette. Ce sont
celles qu'il faut surveiller — et que le débat annuel du septième engagement
doit mesurer.</p>
"""
    corps += g.tableau(
        ["Hypothèse", "Fourchette", "Ce qu'elle déplace dans le solde"],
        [[escape(c.HYPOTHESES[cle].libelle), valeur(c.HYPOTHESES[cle]),
          f'<span class="montant">{meur(ecart, signe=False)}</span>']
         for cle, ecart in poids],
        legende="Les six hypothèses qui pèsent le plus sur le solde de "
                "l'année 5, par l'écart qu'elles produisent entre leurs deux "
                "bornes.",
        classes_colonnes=["texte", "nombre", "nombre"])
    corps += g.note(
        "<p><strong>La première de la liste est celle que nous ne savons "
        "pas mesurer, et c'est la plus importante.</strong> Quelle part des "
        "personnes régularisées travaillait au noir, et quelle part cotisait "
        "déjà sous une autre identité ? Aucune statistique ne le dit. C'est "
        "pourquoi le programme prévoit un suivi des personnes entrées sous le "
        "nouveau régime : dans trois ans, cette hypothèse pourra être "
        "remplacée par un constat.</p>", "vigilance")

    # ----------------------------------------------------------- hypothèses
    corps += f"""
<h2 id="hypotheses">Les {len(c.HYPOTHESES)} hypothèses, une par une</h2>
<p>Chaque ligne donne la valeur retenue — ses deux bornes quand elle en a
deux —, sa nature, et d'où elle vient. Une valeur publiée renvoie à sa fiche,
avec sa source et son année.</p>
"""
    corps += g.depliant("Afficher les hypothèses", _tableau_hypotheses())

    # ------------------------------------------------------ pas compté
    corps += """
<h2 id="pas-compte">Ce que ce chiffrage ne compte pas</h2>
<p>Un chiffrage qui ne dit pas ce qu'il laisse de côté laisse croire qu'il
compte tout. Voici ce que celui-ci ne compte pas, et dans quel sens chaque
oubli joue.</p>
"""
    corps += g.points([
        ("Après la cinquième année (en moins)",
         "Au bout de cinq ans de titre, les personnes régularisées ont droit "
         "à la prime d'activité — de l'ordre de deux cents euros par mois "
         "pour une personne seule au SMIC — et, si elles perdent leur "
         "emploi, au RSA. Et les cotisations de retraite, comptées ici comme "
         "des recettes, ouvrent des droits qui se paieront en pensions."),
        ("Les familles (en moins)",
         "Une personne régularisée peut, au bout de dix-huit mois, faire venir "
         "sa famille par le regroupement familial. L'école, les soins et le "
         "logement de ces familles ne sont pas comptés : ils dépendent de "
         "décisions que personne ne peut prévoir."),
        ("Les arrivées nouvelles (dans les deux sens)",
         "Des salariés attirés par la porte du travail rapportent ; des "
         "demandeurs d'asile attirés par le travail dès le dépôt coûtent. Les "
         "ordres de grandeur sont plus haut, tranche par tranche."),
        ("L'économie (en plus)",
         "Des emplois pourvus, des entreprises qui cessent de renoncer à "
         "recruter, des salariés qui changent d'employeur : aucun effet sur "
         "la croissance, les salaires ou les recettes de TVA n'est compté."),
        ("L'insertion des réfugiés (en plus)",
         "Travailler dès le dépôt de la demande rend l'emploi plus fréquent "
         "des années plus tard : en Allemagne, sept mois d'interdiction de "
         "plus coûtaient vingt points d'emploi cinq ans après. Ce gain n'est "
         "compté qu'à travers la part non compensée du RSA."),
        ("L'investissement (en moins)",
         "Le téléservice des étrangers est désormais évalué à 178,6 M€ au "
         "total, plus de trois fois son devis initial ; le rendre capable de "
         "tenir des délais opposables, et construire des places de rétention "
         "si l'on veut éloigner au-delà de 4 000 personnes de plus par an, "
         "coûterait davantage."),
    ])

    # ---------------------------------------------------------------- méthode
    corps += """
<h2 id="methode">La méthode</h2>
"""
    corps += g.gestes([
        "<strong>Le point de comparaison est la situation actuelle</strong>, "
        "à droit constant : les tarifs, les effectifs et les délais "
        "d'aujourd'hui — pas les cibles que le Gouvernement s'est fixées, ni "
        "le programme d'un autre parti.",
        "<strong>Les finances publiques, toutes ensemble</strong> : État, "
        "sécurité sociale, collectivités. Un transfert d'un budget à l'autre "
        "n'est ni un plus ni un moins — l'aide médicale de l'État qui devient "
        "assurance maladie en est le cas type.",
        "<strong>Deux scénarios, pas un chiffre</strong> : le prudent retient "
        "pour chaque hypothèse la borne qui dégrade le solde de l'année, le "
        "favorable celle qui l'améliore. Le milieu des fourchettes est donné "
        "pour mémoire : ce n'est pas une prévision.",
        "<strong>Deux curseurs, fixés et affichés</strong> : le nombre de "
        "régularisations supplémentaires (50 000 par an les trois premières "
        "années, 20 000 ensuite) et d'éloignements forcés supplémentaires "
        "(4 000 par an). Ce ne sont pas des incertitudes mais des volumes ; "
        "chaque tranche est chiffrée à part.",
        "<strong>Des euros de 2026, sans actualisation</strong>, et des "
        "arrondis à la mesure de l'incertitude : au million près sous vingt "
        "millions, à cinq millions près au-dessous de cent, à dix au-delà.",
    ])

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html#chiffrage">Revenir au programme</a>
  <a href="chiffres.html">Tous les chiffres</a>
  <a href="sources.html#corrections">Ce que nous avons corrigé</a>
</div>
"""
    return corps
