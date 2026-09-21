# Immigration — le programme du Parti libéral français

Un site statique de sept pages : ce que fait la France aujourd'hui en matière
d'immigration, pourquoi ce système rate ses propres objectifs, et l'alternative
libérale que le parti propose — avec ses coûts, ses limites et les objections
qu'on lui oppose.

**Le site : [g-pliberal.github.io/immigration](https://g-pliberal.github.io/immigration/)**

| Page | Ce qu'on y trouve |
| --- | --- |
| `index.html` | La promesse et les six engagements |
| `aujourdhui.html` | Le droit en vigueur et les chiffres publics |
| `blocages.html` | Les cinq mécanismes qui font échouer le système |
| `programme.html` | Les six engagements, texte par texte, avec calendrier et coût |
| `parcours.html` | Un comparateur : le même cas, aujourd'hui et après |
| `objections.html` | Sept objections dans leur version forte, et nos réponses |
| `sources.html` | Les sources publiques, la méthode, et ce que le site ne garantit pas |

## L'apparence

Elle est reprise telle quelle du dépôt
[`retraitecomptenotionelle`](https://github.com/g-pliberal/retraitecomptenotionelle) :
même feuille de style (`moteur/style.css`), mêmes polices servies par le dépôt,
mêmes noms de classes, même icône. Les deux sites sont ceux du même parti et
doivent se reconnaître comme tels — c'est la raison de cette copie, et la
raison pour laquelle on n'y touche pas à la légère. Les ajouts propres à ce
site-ci (le comparateur de parcours) sont regroupés **à la fin** de la feuille,
sous un titre qui le dit, et ne redéfinissent aucune variable de la charte.

Le site ne demande rien à un tiers : ni police, ni script, ni mesure
d'audience. Une visite ne laisse d'adresse IP nulle part ailleurs que chez
l'hébergeur.

## Construire

Les pages HTML sont **écrites par un script et versionnées** : GitHub Pages les
sert telles quelles, sans étape de construction. On ne les modifie donc jamais
à la main — on modifie le module Python qui les produit, et on relance :

```sh
python scripts/construire.py            # écrit les sept pages
python scripts/construire.py --verifier # échoue si elles ne sont pas à jour
python scripts/verifier.py              # pages à jour, liens, ancres, ressources
```

Aucune dépendance : Python 3.10 suffit. Pour regarder le site en local :

```sh
python -m http.server 8000   # puis http://localhost:8000/
```

## Où se trouve quoi

```
index.html, aujourdhui.html, …   les pages, écrites par le script
moteur/style.css                 la charte du parti + les ajouts de ce site
moteur/polices/                  Public Sans et Instrument Serif (OFL)
moteur/icones/                   les tracés Lucide (ISC) recopiés sans retouche
moteur/js/parcours.js            le comparateur, sans dépendance
src/immigration/gabarit.py       bandeau, affiche, pied, fragments communs
src/immigration/pages/           une page = un module
scripts/construire.py            écrit les pages
scripts/verifier.py              vérifie le dépôt sans rien installer
```

Les durées et les étapes du comparateur sont écrites dans
`src/immigration/pages/parcours.py` et déposées dans la page en JSON : le
script JavaScript ne connaît aucun chiffre, ce qui empêche la page et le module
de diverger.

## Les chiffres

Tout chiffre cité vient d'une publication publique et datée — DGEF, INSEE,
OFPRA, CNDA, Cour des comptes, Conseil d'État, OCDE, CEPII. Ils sont **arrondis
volontairement** : les séries migratoires sont révisées d'une publication à
l'autre, et une précision au millier survit rarement à la suivante. La page
[Sources et méthode](sources.html) les rassemble, avec ce que le site
s'interdit et ce qu'il ne sait pas.

Les chiffres sont arrêtés à la date indiquée dans `MILLESIME`
(`src/immigration/gabarit.py`), reprise dans le pied de chaque page. Un chiffre
périmé, une source qui manque, une objection mal formulée : les corrections se
proposent en *issue* ou en *pull request*.

## Licences

- Code (Python, JavaScript, CSS d'origine) : **Apache 2.0** (`LICENSE`).
- Textes et infographies : **CC BY-SA 4.0**.
- Polices Public Sans et Instrument Serif : **SIL Open Font License**
  (`moteur/polices/`).
- Pictogrammes [Lucide](https://lucide.dev) 1.46.0 : **ISC**
  (`moteur/icones/LICENSE`).
