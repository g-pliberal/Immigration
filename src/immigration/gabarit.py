"""Le gabarit du site : ce qui est commun à toutes les pages.

Le site est fait de fichiers HTML statiques, écrits par ``scripts/construire.py``
à partir des modules de ``src/immigration/pages/``. Pourquoi un générateur
plutôt que des fichiers tenus à la main : le bandeau, le pied de page, la
navigation et les avertissements de méthode sont les mêmes partout, et neuf
copies d'un même bandeau divergent dès la première correction. La même raison
vaut pour les chiffres, qui vivent dans ``chiffres.py`` et que ce module sait
poser dans une page (voir ``nombre`` et ``renvoi``).

L'apparence — variables de couleur, noms de classes, polices — est celle du
dépôt `retraitecomptenotionelle`, reprise sans retouche (voir
``moteur/style.css``). Les deux sites sont ceux du même parti et doivent se
reconnaître comme tels.
"""

from __future__ import annotations

from html import escape

from .chiffres import CHIFFRES, Chiffre, chiffre

DEPOT = "https://github.com/g-pliberal/immigration"
SITE_PARENT = "https://partiliberalfrancais.fr/"

# DEUX dates, et jamais une seule. Le site confondait la date de sa dernière
# relecture et le millésime des chiffres qu'il cite : un pied de page qui
# annonçait « chiffres arrêtés en septembre 2026 » sous un tableau de données
# 2023. La confusion est l'erreur la plus facile à retourner contre nous —
# elle donne à des chiffres vieux de deux ans l'apparence de la fraîcheur.
#
# `RELECTURE` est la date à laquelle le site a été relu et corrigé.
# `MILLESIME` est l'année des données les plus récentes qu'il cite ; chaque
# chiffre porte en outre la sienne dans `chiffres.py`, qui fait foi.
RELECTURE = "septembre 2026"
MILLESIME = "2025"

# Les pages, dans l'ordre où elles se lisent, groupées comme le bandeau les
# montre. Le premier élément d'un couple est le fichier, le second le libellé.
GROUPES_NAVIGATION: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = (
    ("Le constat", (
        ("aujourdhui.html", "Aujourd'hui"),
        ("blocages.html", "Ce qui coince"),
    )),
    ("La proposition", (
        ("programme.html", "Le programme"),
        ("chiffrage.html", "Chiffrage"),
        ("parcours.html", "Parcours comparés"),
    )),
    ("Pour aller plus loin", (
        ("objections.html", "Objections"),
        ("chiffres.html", "Tous les chiffres"),
        ("sources.html", "Sources"),
    )),
)

# Les pictogrammes écrits dans la page plutôt que chargés : le site ne demande
# aucune ressource à un tiers, et un fichier de plus par icône coûterait une
# requête par icône. Tracés de Lucide 1.46.0 (ISC), recopiés sans retouche
# depuis `moteur/icones/`.
_ENVELOPPE = ('xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
              'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
              'stroke-linejoin="round"')
ICONES = {
    "arrow-left": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "circle-help": ('<circle cx="12" cy="12" r="10"/>'
                    '<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>'
                    '<path d="M12 17h.01"/>'),
    "triangle-alert": ('<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 '
                       '21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/>'
                       '<path d="M12 17h.01"/>'),
    "trending-up": '<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
}


def icone(nom: str, titre: str = "") -> str:
    """Un pictogramme écrit dans la page.

    Sans ``titre`` il est décoratif : le texte à côté dit déjà ce qu'il dit, et
    une synthèse vocale n'a pas à l'entendre deux fois.
    """
    if nom not in ICONES:
        raise KeyError(f"pictogramme inconnu : {nom}")
    if titre:
        return (f'<svg class="icone" {_ENVELOPPE} role="img">'
                f"<title>{escape(titre)}</title>{ICONES[nom]}</svg>")
    return (f'<svg class="icone" {_ENVELOPPE} aria-hidden="true" '
            f'focusable="false">{ICONES[nom]}</svg>')


def navigation(page_active: str) -> str:
    """Les liens du bandeau, par groupe : une étiquette, puis les pages.

    L'étiquette est du texte lu par tout le monde, et non un ``aria-label`` que
    seule une synthèse vocale entendrait.
    """
    def liens(pages: tuple[tuple[str, str], ...]) -> str:
        return "".join(
            f'<a href="{fichier}"'
            + (' aria-current="page"' if fichier == page_active else "")
            + f">{escape(libelle)}</a>"
            for fichier, libelle in pages
        )
    return "".join(
        f'<span class="groupe"><span class="etiquette">{escape(etiquette)}</span>'
        f'<span class="liens">{liens(pages)}</span></span>'
        for etiquette, pages in GROUPES_NAVIGATION
    )


def entete(page_active: str) -> str:
    """Bandeau de tête, précédé du lien d'évitement.

    Le nom du site n'est pas un ``<h1>`` : chaque page porte son propre titre,
    énorme, et c'est lui le ``<h1>``. « Immigration » est le nom du site,
    répété à l'identique sur chaque page.
    """
    return f"""<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="bandeau"><div class="interieur">
  <p class="nom"><a href="index.html">{icone('trending-up')}<span>Immigration</span></a></p>
  <nav aria-label="Navigation principale">{navigation(page_active)}</nav>
</div></header>"""


def affiche(surtitre: str, titre: str, chapeau: str) -> str:
    """Le bloc de tête d'une page : sur-titre, titre massif, chapeau.

    ``titre`` et ``chapeau`` sont du HTML — ils portent les passages en or et
    les liens ; ``surtitre`` est du texte. Le titre est mis en capitales PAR LE
    STYLE et jamais dans le texte : certaines synthèses vocales épellent lettre
    à lettre un mot écrit en majuscules.
    """
    return (f'<div class="affiche"><p class="surtitre">{escape(surtitre)}</p>'
            f'<h1>{titre}</h1><p class="chapeau">{chapeau}</p></div>')


def plan(entrees: list[tuple[str, str]], etiquette: str = "Dans cette page") -> str:
    """Le sommaire d'une page longue : des ancres, en une rangée."""
    items = "".join(f'<li><a href="#{ancre}">{escape(libelle)}</a></li>'
                    for ancre, libelle in entrees)
    return (f'<nav class="plan" aria-label="{escape(etiquette)}">'
            f'<p class="etiquette">{escape(etiquette)}</p><ol>{items}</ol></nav>')


_UNITES = ("zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
           "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
           "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf")
_DIZAINES = {2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante",
             6: "soixante"}


def en_lettres(n: int) -> str:
    """Un nombre de 0 à 99 écrit en toutes lettres : « quarante et un ».

    Pour les comptes que le site écrit dans ses phrases — « les quarante
    fiches » — et qui doivent suivre le registre au lieu d'être recopiés : un
    compte écrit à la main était faux dès la fiche suivante.
    """
    if not 0 <= n < 100:
        raise ValueError(f"en_lettres ne sait écrire que de 0 à 99 : {n}")
    if n < 20:
        return _UNITES[n]
    dizaine, unite = divmod(n, 10)
    if dizaine in (7, 9):  # soixante-dix, quatre-vingt-dix : on repart de dix
        base = "soixante" if dizaine == 7 else "quatre-vingt"
        reste = 10 + unite
        if dizaine == 7 and unite == 1:
            return "soixante et onze"
        return f"{base}-{_UNITES[reste]}"
    if dizaine == 8:
        return "quatre-vingts" if unite == 0 else f"quatre-vingt-{_UNITES[unite]}"
    if unite == 0:
        return _DIZAINES[dizaine]
    if unite == 1:
        return f"{_DIZAINES[dizaine]} et un"
    return f"{_DIZAINES[dizaine]}-{_UNITES[unite]}"


def fiches_du_registre() -> str:
    """« quarante » : le nombre de fiches du registre, en toutes lettres."""
    return en_lettres(len(CHIFFRES))


def fiche(etiquette: str, valeur: str, precision: str = "") -> str:
    """Un chiffre, ce qu'il mesure, et la phrase qui le situe.

    ``precision`` est du HTML : elle porte presque toujours la source, parce
    qu'un chiffre d'immigration sans source est un argument de comptoir.
    """
    suite = f'<div class="precision">{precision}</div>' if precision else ""
    return (f'<div class="fiche"><div class="etiquette">{escape(etiquette)}</div>'
            f'<div class="valeur">{valeur}</div>{suite}</div>')


def reperes(entrees: list[tuple[str, str, str]]) -> str:
    """Les trois ou quatre chiffres d'ouverture d'une page."""
    return ('<div class="fiches reperes">'
            + "".join(fiche(e, v, p) for e, v, p in entrees) + "</div>")


def points(entrees: list[tuple[str, str]]) -> str:
    """Quelques idées, une par bloc, titre puis phrase.

    Les titres sont de vrais ``<h3>`` : c'est par eux qu'une synthèse vocale
    parcourt la page.
    """
    corps = "".join(f'<div class="point"><h3>{escape(titre)}</h3><p>{texte}</p></div>'
                    for titre, texte in entrees)
    return f'<div class="points">{corps}</div>'


def engagements(entrees: list[tuple[str, str, str]]) -> str:
    """Les engagements du programme : un rang, un chiffre, une promesse.

    C'est le bloc que l'on retient quand on ne lit rien d'autre, et il est
    identique d'une page à l'autre pour cette raison.
    """
    corps = "".join(
        f'<div class="engagement"><p class="rang">{i:02d}</p>'
        f'<p class="chiffre">{chiffre}</p>'
        f'<p class="promesse">{promesse}</p>'
        f'<div class="detail">{detail}</div></div>'
        for i, (chiffre, promesse, detail) in enumerate(entrees, start=1)
    )
    return f'<section class="engagements"><div class="grille">{corps}</div></section>'


def gestes(entrees: list[str]) -> str:
    """Une liste numérotée dont le rang est un chiffre massif."""
    corps = "".join(f'<li><span class="rang" aria-hidden="true">{i}</span>'
                    f"<span>{texte}</span></li>"
                    for i, texte in enumerate(entrees, start=1))
    return f'<ol class="gestes">{corps}</ol>'


def cle(question: str, reponse: str, corps: str = "", source: str = "",
        identifiant: str = "") -> str:
    """Une question, sa réponse en une phrase, et ce qui l'étaye.

    Faite pour deux lecteurs : celui qui lit la question et la réponse et
    s'arrête là, et celui qui descend d'un cran. Encadrée pour se découper —
    une capture de ce bloc se comprend hors du site.
    """
    ancre = f' id="{identifiant}"' if identifiant else ""
    fin = f'<p class="source">{source}</p>' if source else ""
    return (f'<section class="cle"{ancre}><h3>{escape(question)}</h3>'
            f'<p class="reponse">{reponse}</p>{corps}{fin}</section>')


def note(texte: str, genre: str = "") -> str:
    """Un encart court : une réserve, un rappel, un avertissement."""
    classe = f"note {genre}".strip()
    if genre == "avertissement":
        return (f'<div class="{classe}">{icone("triangle-alert", "Attention")}'
                f"<div>{texte}</div></div>")
    return f'<div class="{classe}">{texte}</div>'


def depliant(titre: str, corps: str) -> str:
    """Un repli : le détail que la plupart des lecteurs n'ouvriront pas."""
    return (f'<details class="section"><summary>{icone("chevron-down")}'
            f"{escape(titre)}</summary><div class=\"dedans\">{corps}</div></details>")


def tableau(entetes: list[str], lignes: list[list[str]], legende: str = "",
            classes_colonnes: list[str] | None = None,
            pied: list[list[str]] | None = None) -> str:
    """Un tableau, avec sa légende au-dessus.

    ``classes_colonnes`` dit comment chaque colonne s'aligne : ``texte``,
    ``nombre``, ``date`` ou ``long``. Un nombre aligné à gauche ne se compare
    pas d'une ligne à l'autre, et c'est tout ce qu'on demande à un tableau.

    ``pied`` porte les lignes de total, dans un ``<tfoot>`` : un total n'est
    pas une ligne comme les autres, et une synthèse vocale doit pouvoir le
    dire.
    """
    classes = classes_colonnes or ["texte"] * len(entetes)

    def rangees(lignes: list[list[str]]) -> str:
        html = ""
        for ligne in lignes:
            cellules = f'<th scope="row" class="{classes[0]}">{ligne[0]}</th>'
            cellules += "".join(f'<td class="{c}">{v}</td>'
                                for v, c in zip(ligne[1:], classes[1:]))
            html += f"<tr>{cellules}</tr>"
        return html

    tete = "".join(f'<th scope="col" class="{c}">{e}</th>'
                   for e, c in zip(entetes, classes))
    cap = f"<caption>{legende}</caption>" if legende else ""
    fin = f"<tfoot>{rangees(pied)}</tfoot>" if pied else ""
    return (f'<div class="defilant"><table>{cap}<thead><tr>{tete}</tr></thead>'
            f"<tbody>{rangees(lignes)}</tbody>{fin}</table></div>")


# ---------------------------------------------------------------------------
# Les chiffres dans le texte
#
# Aucune page n'écrit plus un chiffre en clair : elle appelle `nombre("cle")`,
# et le registre fournit la valeur. Un chiffre corrigé dans `chiffres.py` se
# corrige partout, et un chiffre sans entrée au registre fait échouer la
# construction — ce qui est le but.
# ---------------------------------------------------------------------------


def nombre(cle: str, avec_renvoi: bool = True) -> str:
    """Un chiffre du registre, suivi du renvoi vers sa fiche.

    Le renvoi est un lien discret vers ``chiffres.html``, où le lecteur trouve
    la source, le millésime et la réserve de méthode. C'est ce qui rend la
    promesse « un chiffre, une source, un millésime » vérifiable en un clic
    plutôt qu'affirmée en bas de page.
    """
    c = chiffre(cle)
    texte = f'<span class="nombre">{c.valeur}</span>'
    return texte + renvoi(cle) if avec_renvoi else texte


def renvoi(cle: str) -> str:
    """Le renvoi seul, pour une phrase qui cite le chiffre à sa façon."""
    c = chiffre(cle)
    titre = f"{c.mesure} — {c.source}, données {c.annee}"
    return (f'<a class="renvoi" href="chiffres.html#c-{cle}" '
            f'title="{escape(titre)}"><span class="hors-ecran">Source du '
            f'chiffre, année des données : </span>'
            f'{escape(c.annee)}</a>')


def fiche_chiffre(cle: str, etiquette: str = "") -> str:
    """Une fiche de repère construite depuis le registre.

    L'étiquette par défaut est ce que le chiffre mesure, et la précision porte
    le millésime et la source : une fiche qui se recopie sans sa source est
    une fiche qui finira citée de travers.
    """
    c = chiffre(cle)
    precision = f'{escape(c.mesure)} — {escape(c.source.split(",")[0])}, '
    precision += f'{escape(c.annee)}{renvoi(cle)}'
    return fiche(etiquette or c.mesure.split(" —")[0], c.valeur, precision)


def reperes_chiffres(entrees: list[tuple[str, str]]) -> str:
    """Les trois ou quatre chiffres d'ouverture, pris au registre."""
    return ('<div class="fiches reperes">'
            + "".join(fiche_chiffre(cle, etiquette)
                      for cle, etiquette in entrees) + "</div>")


def pied() -> str:
    """Pied de page : d'où viennent les chiffres, et ce que la page n'est pas.

    Il ne porte aucune mention légale : le site du parti édite et héberge la
    page, et deux déclarations concurrentes valent moins qu'une.
    """
    return f"""<footer>
  <p><strong>Ce site est un document politique.</strong> Il expose le droit
  en vigueur, les chiffres publics qui le décrivent, et la réforme que le
  Parti libéral français propose à leur place. Il ne vaut ni conseil
  juridique, ni information administrative : pour une démarche, voir
  <a href="https://www.service-public.fr/particuliers/vosdroits/N110">service-public.fr</a>.</p>
  <p><strong>Site relu en {RELECTURE}</strong> ; chiffres les plus récents
  cités : données <strong>{MILLESIME}</strong>. Les deux dates diffèrent, et
  c'est normal : une donnée migratoire est publiée l'année suivante. Chaque
  chiffre porte la sienne dans <a href="chiffres.html">Tous les chiffres</a>,
  avec sa source et sa réserve de méthode ; la
  <a href="sources.html">méthode</a> dit le reste. Textes et infographies sous
  <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>,
  code sous licence Apache 2.0, le tout sur <a href="{DEPOT}">GitHub</a>.</p>
  <p class="retour-site">Un site du
  <a href="{SITE_PARENT}" target="_top">Parti libéral français</a>.</p>
</footer>"""


def page(fichier: str, titre_onglet: str, description: str, corps: str,
         scripts: str = "") -> str:
    """La page entière, de ``<!doctype>`` au ``</html>``."""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- La couleur du bandeau du navigateur, sur téléphone : la page commence là
     où la barre d'adresse finit, sans liseré d'une autre couleur entre les
     deux. -->
<meta name="theme-color" content="#0b3d3a">
<title>{escape(titre_onglet)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(titre_onglet)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<link rel="icon" href="moteur/icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="moteur/icone.svg">
<link rel="stylesheet" href="moteur/style.css">
</head>
<body>
{entete(fichier)}
<main id="contenu" tabindex="-1">
{corps}
</main>
{pied()}
{scripts}</body>
</html>
"""
