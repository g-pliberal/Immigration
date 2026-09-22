# Immigration — le programme du Parti libéral français

Un site statique de neuf pages : ce que fait la France aujourd'hui en matière
d'immigration, pourquoi ce système rate ses propres objectifs, et l'alternative
libérale que le parti propose — avec son chiffrage calculé, ses limites, les
onze objections qu'on lui oppose, et les trois seuils qui nous donneraient
tort.

**Le site : [g-pliberal.github.io/immigration](https://g-pliberal.github.io/immigration/)**

| Page | Ce qu'on y trouve |
| --- | --- |
| `index.html` | La promesse, les sept engagements, et où s'arrête l'ouverture |
| `aujourdhui.html` | Le droit en vigueur, le pacte européen, et les chiffres publics |
| `blocages.html` | Les cinq mécanismes qui font échouer le système |
| `programme.html` | Les sept engagements, texte par texte, avec calendrier et synthèse du chiffrage |
| `chiffrage.html` | Les plus et les moins de chaque engagement par rapport à aujourd'hui : poste par poste, année par année, deux scénarios, chaque hypothèse sourcée |
| `parcours.html` | Un comparateur : le même cas, en trois colonnes |
| `objections.html` | Onze objections dans leur version forte, et nos réponses |
| `chiffres.html` | Chaque chiffre du site, sa source, son millésime, sa réserve |
| `sources.html` | Les sources, la méthode, et ce que nous avons corrigé |

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
python scripts/construire.py            # écrit les pages
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
src/immigration/chiffres.py      LE REGISTRE : un chiffre, sa source, sa réserve
src/immigration/chiffrage.py     LE CHIFFRAGE : hypothèses, postes, scénarios
src/immigration/pages/           une page = un module
scripts/construire.py            écrit les pages
scripts/verifier.py              vérifie le dépôt sans rien installer
```

Les durées et les étapes du comparateur sont écrites dans
`src/immigration/pages/parcours.py` et déposées dans la page en JSON : le
script JavaScript ne connaît aucun chiffre, ce qui empêche la page et le module
de diverger.

## Les chiffres

**Les valeurs ne sont écrites qu'à un seul endroit** :
`src/immigration/chiffres.py`, une entrée par chiffre, avec ce qu'il mesure, sa
source, l'URL, l'année des *données*, l'évolution, et — le champ qui fait le
travail — la **réserve de méthode** : ce que le chiffre ne dit pas.

Les fiches de repères et les tableaux de chiffres sont **construits** depuis ce
registre (`g.nombre("premiers-titres")`, `g.reperes_chiffres([…])`) : ils ne
peuvent pas diverger des fiches, et une clé inconnue fait échouer la
construction. Quand un chiffre est repris dans une phrase, pour qu'elle se
lise, il porte le renvoi `g.renvoi("…")` qui mène à sa fiche.

`chiffres.html` est le rendu direct de ce registre : chaque chiffre du site
renvoie à sa fiche par le petit lien qui le suit.

Deux dates, et jamais une seule (`src/immigration/gabarit.py`) : `RELECTURE`
est la date de la dernière relecture du site, `MILLESIME` l'année des données
les plus récentes citées. Les confondre donnait à des chiffres vieux de deux
ans l'apparence de la fraîcheur — c'était le cas, et c'est corrigé.

Un chiffre périmé, une source qui manque, une objection mal formulée : les
corrections se proposent en *issue* ou en *pull request*.

## Le chiffrage

`src/immigration/chiffrage.py` calcule ce que chaque engagement coûte ou
rapporte aux finances publiques, **par rapport à la situation actuelle**. Rien
n'y est écrit à la main hormis les hypothèses :

- **chaque hypothèse** a une borne basse, une borne haute, une nature
  (*constat*, *estimation*, *hypothèse*, *paramètre*) et ce qui la justifie ;
  une valeur publiée est **lue dans le registre** (`_lu("renouvellements")`),
  pas recopiée ;
- **chaque poste** est un plus (économie, recette) ou un moins (dépense,
  recette perdue), avec sa formule en français et son calcul en Python ;
- **deux scénarios** : le *prudent* retient pour chaque hypothèse la borne qui
  dégrade le solde de l'année, le *favorable* celle qui l'améliore — des
  mondes cohérents, pas des bornes additionnées ligne à ligne ;
- **deux curseurs** affichés à part : le nombre de régularisations
  supplémentaires et d'éloignements supplémentaires, avec l'effet de chaque
  tranche.

Les phrases de la page qui tirent une conclusion du calcul (« le scénario
prudent reste négatif », « le signe du solde tient d'abord à la part de
travail au noir ») sont **vérifiées à la construction** par
`pages/chiffrage.py:constats` : une hypothèse corrigée qui les démentirait
fait échouer la construction au lieu de publier une phrase fausse. Changer une
hypothèse, c'est donc changer une ligne de `chiffrage.py`, relancer
`scripts/construire.py`, et lire ce qui casse.

## Ce que la relecture adverse a changé

Le site a été relu ligne à ligne comme l'aurait fait un contradicteur
compétent. Les dix corrections principales sont publiées sur le site lui-même,
dans [Sources et méthode](sources.html#corrections) — un programme qui se
corrige en silence donne à penser qu'il a quelque chose à cacher. En résumé :

- **l'engagement 5 a été refondé.** La carence de cinq ans sur les prestations
  non contributives est contraire à la Constitution (décision n° 2024-6 RIP du
  11 avril 2024, censure au fond), au droit de l'Union (directive 2011/98) et à
  trente-neuf conventions bilatérales. Le programme ne crée plus aucune carence ;
- **les chiffres sont passés aux données 2025** (384 230 premiers titres,
  l'ordre des motifs a changé) ;
- **le pacte européen** appliqué depuis le 12 juin 2026 et **l'expiration de
  l'article L. 435-4** au 31 décembre 2026 sont traités ;
- **un septième engagement** répond à « qui décide ? » : débat annuel,
  critères révisables, et trois seuils chiffrés qui nous donneraient tort ;
- **le comparateur a trois colonnes**, l'étape consulaire est rétablie et les
  barres promises sont hachurées ;
- **un chiffrage** poste par poste remplace « le coût net est probablement
  négatif » — puis un chiffrage **calculé** (page `chiffrage.html`) remplace
  ce tableau de phrases, et corrige ce qu'il laissait passer : les
  renouvellements évités (170 000 à 250 000, pas 600 000 à 700 000), la
  gratuité des renouvellements jamais comptée, une attente d'asile de dix mois
  et non dix-huit, le vrai coût d'un éloignement.

## Licences

- Code (Python, JavaScript, CSS d'origine) : **Apache 2.0** (`LICENSE`).
- Textes et infographies : **CC BY-SA 4.0**.
- Polices Public Sans et Instrument Serif : **SIL Open Font License**
  (`moteur/polices/`).
- Pictogrammes [Lucide](https://lucide.dev) 1.46.0 : **ISC**
  (`moteur/icones/LICENSE`).
