# Les pictogrammes du site

Ils viennent tous de **[Lucide](https://lucide.dev) 1.46.0**, sous licence ISC
(`LICENSE`, à côté). Un seul jeu, une seule grille — 24 × 24, trait de 2,
extrémités et jointures arrondies —, et rien qui soit dessiné à la main : c'est
ce qui les fait tenir ensemble à toutes les tailles, ce qu'un emoji ou un
caractère Unicode ne font pas, leur dessin changeant d'un système à l'autre.

**Les fichiers de ce dossier sont les originaux, recopiés sans retouche.** Le
site ne les charge pas : le gabarit écrit leur tracé DANS la page
(`src/immigration/gabarit.py`, table `ICONES`), parce que la page ne demande
aucune ressource à un tiers et qu'un fichier par icône coûterait une requête
par icône.

`../icone.svg` est l'icône du site elle-même : la même grille, le même trait,
le tracé de `trending-up` posé sur le carré de la charte du parti — le même,
couleur comprise, que celui du site `retraitecomptenotionelle`, pour que les
deux se reconnaissent dans une barre d'onglets.

## Ajouter un pictogramme

1. Télécharger l'original sur [lucide.dev](https://lucide.dev) et le déposer
   ici sans le retoucher.
2. Recopier ses `<path>` dans la table `ICONES` de
   `src/immigration/gabarit.py`, sans l'enveloppe `<svg>` : le gabarit la pose
   lui-même, avec la même grille et le même trait pour tous.
3. Reconstruire (`python scripts/construire.py`).

Les fichiers de ce dossier qui ne sont pas dans la table sont conservés parce
qu'ils viennent du dépôt d'origine et qu'un pictogramme de plus ne coûte rien
tant qu'il n'est pas chargé.
