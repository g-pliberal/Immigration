#!/usr/bin/env python3
"""Écrit les pages HTML du site à partir des modules Python.

    python scripts/construire.py            # écrit les pages
    python scripts/construire.py --verifier # échoue si elles ne sont pas à jour

Le second mode est celui d'une vérification automatique : il compare l'octet
et ne touche à rien. Les pages HTML sont versionnées — le site est servi tel
quel par GitHub Pages, sans étape de construction chez l'hébergeur — et une
page qui aurait été modifiée à la main, sans son module, doit se voir.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "src"))

from immigration import gabarit  # noqa: E402
from immigration.pages import ORDRE  # noqa: E402


def rendre() -> dict[pathlib.Path, str]:
    """Le HTML de chaque page, par chemin de fichier."""
    pages: dict[pathlib.Path, str] = {}
    for module in ORDRE:
        infos = module.PAGE
        pages[RACINE / infos["fichier"]] = gabarit.page(
            infos["fichier"], infos["titre"], infos["description"],
            module.construire(), getattr(module, "SCRIPTS", ""))
    return pages


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument("--verifier", action="store_true",
                           help="ne rien écrire, échouer si une page diffère")
    arguments = analyseur.parse_args()

    ecarts: list[str] = []
    for chemin, html in rendre().items():
        ancien = chemin.read_text(encoding="utf-8") if chemin.exists() else None
        if ancien == html:
            continue
        if arguments.verifier:
            ecarts.append(chemin.name)
            continue
        chemin.write_text(html, encoding="utf-8")
        print(f"écrit  {chemin.relative_to(RACINE)}  ({len(html):,} octets)"
              .replace(",", " "))

    if ecarts:
        print("Ces pages ne correspondent plus à leur module : "
              + ", ".join(sorted(ecarts)), file=sys.stderr)
        print("Relancer : python scripts/construire.py", file=sys.stderr)
        return 1
    if arguments.verifier:
        print(f"Les {len(ORDRE)} pages sont à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
