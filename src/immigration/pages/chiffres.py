"""Tous les chiffres du site, avec leur source, leur année et leur réserve.

Cette page n'a pas de texte propre : elle est le rendu du registre
``src/immigration/chiffres.py``. Elle existe pour une raison précise — un
programme politique qui annonce « un chiffre, une source, un millésime » doit
pouvoir être pris au mot en un clic, et non renvoyer à une bibliographie où
le lecteur devra retrouver lui-même lequel des vingt rapports porte lequel
des vingt chiffres.

Chaque fiche porte aussi ce que le chiffre NE dit PAS. C'est la partie
inhabituelle, et c'est la plus utile : un contradicteur qui cherche la faille
la trouve écrite, datée et assumée, ce qui lui retire l'essentiel de son
effet.
"""

from __future__ import annotations

from .. import chiffres as registre
from .. import gabarit as g

PAGE = {
    "fichier": "chiffres.html",
    "titre": "Tous les chiffres, leurs sources et leurs réserves",
    "description": (
        "Chaque chiffre cité sur le site, avec sa valeur publiée, sa source, "
        "l'année des données, son évolution et la réserve de méthode qu'il "
        "faut connaître avant de le citer."),
}


def _fiche(cle: str, c: registre.Chiffre) -> str:
    """Une fiche : la valeur, ce qu'elle mesure, d'où elle vient, ses limites."""
    lignes = [
        ("Ce qu'il mesure", g.escape(c.mesure)),
        ("Valeur publiée", g.escape(c.exact or c.valeur)),
        ("Année des données", g.escape(c.annee)),
    ]
    if c.publie:
        lignes.append(("Date de publication", g.escape(c.publie)))
    if c.evolution:
        lignes.append(("Évolution", g.escape(c.evolution)))
    lignes.append(
        ("Source", f'<a href="{c.url}" rel="noopener">{g.escape(c.source)}</a>'))

    corps = "".join(f"<dt>{etiquette}</dt><dd>{valeur}</dd>"
                    for etiquette, valeur in lignes)
    reserve = ""
    if c.reserve:
        reserve = g.note(f"<p><strong>Ce que ce chiffre ne dit pas.</strong> "
                         f"{g.escape(c.reserve)}</p>", "vigilance")
    return (f'<section class="chiffre-fiche" id="c-{cle}">'
            f'<p class="valeur">{c.valeur}</p>'
            f"<dl class=\"gloses\">{corps}</dl>{reserve}</section>")


def construire() -> str:
    corps = g.affiche(
        "Pour aller plus loin",
        "Tous les chiffres, <span class=\"serif\">et leurs limites</span>",
        f"Les {g.fiches_du_registre()} chiffres cités sur ce site, un par "
        "fiche : la valeur "
        "publiée, la source exacte, l'année des <em>données</em> — qui n'est "
        "pas celle de la publication — et ce que le chiffre ne dit pas. "
        "Chaque chiffre du site renvoie ici.")

    corps += g.note(
        "<p><strong>Cette page est écrite par le programme qui écrit le "
        "site.</strong> Les valeurs n'existent qu'à un seul endroit du dépôt "
        "(<code>src/immigration/chiffres.py</code>) ; les fiches de repères et "
        "les tableaux de chiffres en sont construits, et les phrases qui "
        "citent un chiffre portent le lien qui ramène ici. Un chiffre corrigé "
        "se corrige partout, et une clé inconnue fait échouer la construction "
        "du site. C'est une garantie mécanique, pas une promesse.</p>",
        "resume")

    corps += g.plan([(cle, titre) for cle, titre, _ in registre.par_famille()])

    for cle_famille, titre, entrees in registre.par_famille():
        corps += f'<h2 id="{cle_famille}">{g.escape(titre)}</h2>'
        corps += '<div class="chiffres-grille">'
        corps += "".join(_fiche(cle, c) for cle, c in entrees)
        corps += "</div>"

    corps += """
<h2 id="corriger">Un chiffre faux, périmé, ou mal lu</h2>
<p>Les séries migratoires sont révisées d'une publication à l'autre, les
périmètres changent, et une donnée provisoire est corrigée l'année suivante.
Une fiche de cette page qui ne correspond plus à sa source est un défaut du
site, pas un détail&nbsp;: la correction se propose sur
<a href="https://github.com/g-pliberal/immigration">le dépôt</a>, et elle est
publiée avec sa date.</p>
<p>Deux fiches portent la mention «&nbsp;part déduite&nbsp;»&nbsp;: le
communiqué de la DGEF publie le total et les évolutions sans détailler ces
deux motifs. Nous préférons l'écrire plutôt que d'arrondir en silence.</p>
"""

    corps += """
<div class="actions">
  <a class="bouton" href="sources.html">La méthode et les sources</a>
  <a href="programme.html">Le programme</a>
</div>
"""
    return corps
