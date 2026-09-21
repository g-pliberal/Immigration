"""Les sept pages du site, une par module.

Chaque module expose une fonction ``construire()`` qui rend le HTML du corps
de la page, et une constante ``PAGE`` qui dit son fichier, son titre d'onglet
et sa description. ``scripts/construire.py`` les parcourt dans l'ordre de
``ORDRE``.
"""

from . import accueil, aujourdhui, blocages, programme, parcours, objections, sources

ORDRE = (accueil, aujourdhui, blocages, programme, parcours, objections, sources)

__all__ = ["ORDRE", "accueil", "aujourdhui", "blocages", "programme", "parcours",
           "objections", "sources"]
