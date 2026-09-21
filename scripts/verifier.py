#!/usr/bin/env python3
"""Vérifie le site sans rien installer : pages à jour, liens et fichiers.

    python scripts/verifier.py

Ce n'est pas un validateur HTML, et cela ne remplace pas une relecture. Cela
attrape les trois fautes qu'on commet vraiment en écrivant un site de huit
pages à la main : une page régénérée qu'on a oublié de commiter, un lien
interne vers un fichier ou une ancre qui n'existe pas, et une ressource
— feuille, script, police, image — appelée mais absente du dépôt.

Aucune dépendance : le dépôt doit se vérifier sur une machine nue, et un
outillage qu'il faut installer avant de l'exécuter finit par ne plus
s'exécuter.
"""

from __future__ import annotations

import html.parser
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent


class Collecteur(html.parser.HTMLParser):
    """Relève les liens, les ressources et les ancres d'une page."""

    def __init__(self) -> None:
        super().__init__()
        self.liens: list[str] = []
        self.ressources: list[str] = []
        self.ancres: set[str] = set()

    def handle_starttag(self, balise: str, attributs: list[tuple[str, str]]) -> None:
        a = dict(attributs)
        if "id" in a:
            self.ancres.add(a["id"])
        if balise == "a" and "href" in a:
            self.liens.append(a["href"])
        if balise in ("link", "script", "img") and (a.get("href") or a.get("src")):
            self.ressources.append(a.get("href") or a.get("src"))


def pages() -> dict[str, Collecteur]:
    releve: dict[str, Collecteur] = {}
    for chemin in sorted(RACINE.glob("*.html")):
        c = Collecteur()
        c.feed(chemin.read_text(encoding="utf-8"))
        releve[chemin.name] = c
    return releve


def main() -> int:
    fautes: list[str] = []

    # 1. Les pages correspondent-elles à leur module ?
    construction = subprocess.run(
        [sys.executable, str(RACINE / "scripts" / "construire.py"), "--verifier"],
        capture_output=True, text=True)
    if construction.returncode != 0:
        fautes.append(construction.stdout.strip() + construction.stderr.strip())

    releve = pages()
    # Le nombre attendu vient des modules, et non d'un nombre écrit ici : une
    # page ajoutée sans être déclarée, ou déclarée sans être construite, doit
    # se voir — c'est exactement la faute que ce script existe pour attraper.
    sys.path.insert(0, str(RACINE / "src"))
    from immigration.pages import ORDRE  # noqa: E402

    attendues = {module.PAGE["fichier"] for module in ORDRE}
    if set(releve) != attendues:
        for orpheline in sorted(set(releve) - attendues):
            fautes.append(f"{orpheline} : page à la racine qu'aucun module ne "
                          "construit — la supprimer ou lui écrire un module")
        for manquante in sorted(attendues - set(releve)):
            fautes.append(f"{manquante} : page déclarée dans `pages/__init__.py` "
                          "mais absente de la racine")

    # 2. Les liens internes mènent-ils quelque part ?
    for nom, page in releve.items():
        for lien in page.liens:
            if lien.startswith(("http://", "https://", "mailto:")):
                continue
            cible, _, ancre = lien.partition("#")
            cible = cible or nom
            if cible not in releve and not (RACINE / cible).exists():
                fautes.append(f"{nom} : lien vers « {cible} », qui n'existe pas")
            elif ancre and cible in releve and ancre not in releve[cible].ancres:
                fautes.append(f"{nom} : ancre « #{ancre} » absente de {cible}")

        # 3. Les ressources appelées sont-elles dans le dépôt ?
        for ressource in page.ressources:
            if ressource.startswith(("http://", "https://", "data:")):
                fautes.append(f"{nom} : ressource tierce « {ressource} » — le site "
                              "ne doit rien demander à un tiers")
            elif not (RACINE / ressource).exists():
                fautes.append(f"{nom} : ressource absente « {ressource} »")

    # 4. Et les polices appelées par la feuille de style ?
    style = (RACINE / "moteur" / "style.css").read_text(encoding="utf-8")
    for police in re.findall(r"url\(([^)]+)\)", style):
        chemin = RACINE / "moteur" / police.strip("\"'")
        if not chemin.exists():
            fautes.append(f"style.css : police absente « {police} »")

    if fautes:
        print("\n".join(f"  — {f}" for f in fautes), file=sys.stderr)
        print(f"\n{len(fautes)} problème(s).", file=sys.stderr)
        return 1
    print(f"{len(releve)} pages, liens internes, ancres et ressources : "
          "tout est en place.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
