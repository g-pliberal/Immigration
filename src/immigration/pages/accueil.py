"""L'accueil : la promesse, les sept engagements, et par où entrer."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "index.html",
    "titre": "Immigration — le programme du Parti libéral français",
    "description": (
        "Ce que fait la France en matière d'immigration, ce que cela produit, "
        "et l'alternative libérale : ouvrir le travail, garantir des délais, "
        "juger vite, et rendre des comptes chaque année."),
}

# Les sept engagements. Ils sont écrits ici, une seule fois, et repris par la
# page Programme : deux listes d'engagements divergeraient dès la première
# correction, et le lecteur qui compare les deux pages compte les différences.
#
# Le septième a été ajouté après relecture critique du programme. Il répond à
# la seule objection à laquelle les six premiers ne répondaient pas : si l'on
# renonce aux quotas — et il faut y renoncer, le Conseil constitutionnel les a
# censurés en 2024 —, alors qui décide, et comment saurons-nous que nous nous
# sommes trompés ? Un programme sans réponse à cette question se fait traiter
# d'irresponsable, et il a tort de s'en étonner.
ENGAGEMENTS = [
    ("1", "Un seul titre, qui vaut autorisation de travailler.",
     "L'autorisation de travail disparaît comme acte distinct : un étranger en "
     "séjour régulier travaille, change d'employeur et de métier comme un "
     "Français. Fin de l'« opposabilité de la situation de l'emploi » et des "
     "listes de métiers en tension, qui font décider par arrêté ce qu'un "
     "contrat de travail dit déjà."),
    ("8 sem.", "Un délai opposable, et le silence vaut accord.",
     "Huit semaines pour instruire une première demande de titre de travail, "
     "quatre pour un renouvellement. Passé ce délai sans réponse motivée, le "
     "titre est réputé délivré — sauf signalement d'ordre public, qui suspend "
     "le délai. Aujourd'hui le silence de l'administration vaut refus, ce qui "
     "fait de la lenteur un instrument de politique publique."),
    ("4 ans", "Un titre pluriannuel dès la première délivrance.",
     "Quatre ans pour le travail et les études, renouvelables en ligne, au "
     "lieu d'un an renouvelé chaque année. Le titre survit à la perte "
     "d'emploi pendant douze mois. La France a délivré 384 230 premiers "
     "titres l'an dernier et en a renouvelé 955 080 : les files sont faites "
     "de gens déjà en règle."),
    # Le chiffre affiché est celui que nous nous engageons à tenir, pas la
    # cible lointaine. Afficher « 3 mois » en gros et « six mois » en petit,
    # c'est offrir la citation à l'adversaire : il retiendra le grand chiffre
    # et produira le petit.
    ("6 mois", "L'asile jugé vite, travail autorisé dès le dépôt.",
     "Six mois recours compris, opposables à l'administration, dans les deux "
     "ans — et trois mois comme cible une fois ce délai tenu. Le droit de "
     "travailler dès l'enregistrement de la demande plutôt qu'après six mois "
     "d'inactivité forcée ; et l'exécution effective des rejets définitifs."),
    ("0", "Aucun nouveau délai de carence.",
     "Nous ne créons aucune carence nouvelle : nous maintenons celle qui "
     "existe déjà pour le RSA — cinq ans de séjour régulier, article L. 262-4 "
     "du code de l'action sociale — et nous refusons de l'étendre au "
     "logement, aux prestations familiales et à l'autonomie, que le Conseil "
     "constitutionnel a protégés en avril 2024. Le travail ouvre "
     "immédiatement les droits qu'il finance."),
    ("15 j", "Zéro file d'attente : le rendez-vous est un droit.",
     "Toute démarche faisable en ligne, un guichet physique garanti pour qui "
     "ne peut pas ou ne veut pas — le Conseil d'État l'impose depuis 2022 —, "
     "un rendez-vous sous quinze jours, et la gratuité des renouvellements."),
    ("1 / an", "Ce qui nous donnerait tort, écrit d'avance.",
     "Un débat annuel au Parlement sur des indicateurs publiés, des critères "
     "révisables par la loi, et trois seuils chiffrés dont le franchissement "
     "nous obligerait à corriger le tir. Nous refusons les quotas — censurés "
     "en 2024 — mais pas le contrôle démocratique."),
]


def construire() -> str:
    corps = g.affiche(
        "Programme",
        "Travailler, <span class=\"serif\">pas attendre</span>",
        "La France ne choisit pas entre « plus » et « moins » d'immigration : "
        "elle choisit entre une immigration <strong class=\"cle-texte\">de "
        "travail, rapide et contrôlée</strong> et une immigration subie, lente "
        "et irrégulière. Elle a aujourd'hui la seconde. Voici comment on passe "
        "à la première.")

    corps += g.reperes_chiffres([
        ("immigres", "Immigrés en France"),
        ("premiers-titres", "Premiers titres par an"),
        ("part-travail", "Part du travail"),
        ("renouvellements", "Renouvellements par an"),
    ])

    corps += g.note(
        "<p><strong>Les chiffres de ce site sont publics, datés et "
        "contestables — et chacun renvoie à sa fiche.</strong> Cliquez "
        "l'année qui suit un chiffre : vous y trouverez la source exacte, "
        "l'année des données, l'évolution, et <em>ce que le chiffre ne dit "
        "pas</em>. Les vingt-sept fiches sont rassemblées dans "
        "<a href=\"chiffres.html\">Tous les chiffres</a>. Un programme qui "
        "demande qu'on le croie sur parole ne mérite pas qu'on le lise.</p>",
        "resume")

    corps += """
<div class="paire">
  <div>
    <h2>Le constat</h2>
    <p>La France a délivré 384 230 premiers titres de séjour l'an dernier. Près
    d'un tiers va aux études, un quart à la protection, un peu moins d'un quart
    aux familles — et <strong class="cle-texte">treize pour cent au
    travail</strong>, en baisse de 13 % sur un an. Ce n'est pas un hasard :
    notre droit traite le travail d'un étranger comme une exception qu'un
    préfet accorde, après avoir vérifié qu'aucun résident ne veut de
    l'emploi.</p>
    <p>Le résultat est connu de tous ceux qui l'ont vécu : des mois d'attente
    pour un contrat déjà signé, un site qui ne donne pas de rendez-vous, un
    recours au tribunal pour obtenir ce rendez-vous — et, au bout, beaucoup de
    gens qui travaillent quand même, sans titre, pour un employeur qui en
    profite.</p>
    <p><a href="aujourdhui.html">Lire l'état des lieux</a> ·
    <a href="blocages.html">Ce qui coince, et pourquoi</a></p>
  </div>
  <div>
    <h2>La proposition</h2>
    <p>Elle tient en une phrase : <strong class="cle-texte">on ouvre la porte du
    travail, on juge vite, et on rend des comptes</strong>.</p>
    <p>Ouvrir le travail, parce qu'un employeur qui embauche et un adulte qui
    accepte n'ont pas besoin qu'un service d'État vérifie d'abord si le poste
    aurait pu revenir à quelqu'un d'autre. Juger vite, parce qu'une procédure
    d'asile qui dure dix-huit mois fabrique elle-même l'irrégularité qu'on lui
    reproche ensuite. Rendre des comptes, parce qu'une réforme dont personne ne
    peut dire à quelle condition elle aurait échoué n'est pas une réforme, mais
    une profession de foi.</p>
    <p><a href="programme.html">Lire le programme</a> ·
    <a href="parcours.html">Comparer les parcours</a></p>
  </div>
</div>
"""

    corps += g.engagements(ENGAGEMENTS)

    corps += """
<h2 id="pourquoi">Pourquoi un libéral parle d'immigration</h2>
<p>Parce que c'est, de toutes les libertés, celle dont la privation coûte le
plus cher à qui la subit. Un même travailleur, à compétence égale, produit et
gagne plusieurs fois plus en France que dans le pays où il est né : l'écart ne
tient pas à lui, il tient à la frontière. L'économiste Michael Clemens appelle
cela <em>les billets de mille milliards laissés sur le trottoir</em> — et
précise lui-même que son estimation suppose que les institutions du pays
d'accueil tiennent, ce qui est exactement la question politique.</p>
<p>Et parce que la version française du débat est une impasse. Un camp promet
de fermer ce qui ne se ferme pas ; l'autre défend un système qu'il n'ose pas
décrire. Les deux laissent en place la même machine administrative : lente,
discrétionnaire, coûteuse, et qui rate ses propres objectifs — elle n'attire
pas les travailleurs dont l'économie manque, et n'éloigne pas ceux qui doivent
partir.</p>
"""

    corps += g.cle(
        "Alors pourquoi pas les frontières ouvertes ?",
        "Parce que l'argument économique qui plaide pour l'ouverture ne dit "
        "rien de la vitesse à laquelle une société absorbe, ni de ce qu'elle "
        "accepte. <strong>Nous nous arrêtons là où l'ouverture cesserait "
        "d'être consentie</strong> — et nous préférons l'écrire que de laisser "
        "nos adversaires l'écrire pour nous.",
        corps="<p>Trois limites, et elles sont dans le texte du programme, pas "
              "dans ses intentions. <strong>Le consentement à l'impôt</strong> "
              "d'abord : une ouverture qui donnerait le sentiment que l'on "
              "peut venir vivre d'une aide sans avoir cotisé serait défaite "
              "à l'élection suivante, et emporterait avec elle ce qu'elle "
              "aurait ouvert. <strong>La capacité d'absorption</strong> "
              "ensuite : le logement, l'école et les transports s'ajustent en "
              "années quand une arrivée se compte en mois — c'est pourquoi le "
              "programme est adossé à une réforme de l'offre de logement, et "
              "pourquoi il est faux de dire que l'une va sans l'autre. "
              "<strong>La sécurité</strong> enfin : l'identité établie et le "
              "casier vérifié ne sont pas des concessions faites à "
              "l'adversaire, ce sont les conditions auxquelles un État peut "
              "se permettre d'être ouvert sur le reste.</p>"
              "<p>Ce que nous proposons est donc borné, et le restera : un "
              "droit de venir <em>travailler</em>, conditionné, vérifiable, "
              "refusable, et révisable chaque année par le Parlement. Ce "
              "n'est pas la suppression des frontières, et nous ne l'écrivons "
              "pas comme une étape vers elle.</p>",
        identifiant="limites")

    corps += g.points([
        ("Le travail, pas la loterie",
         "Un titre délivré sur des critères écrits, vérifiables, opposables — "
         "et non sur l'appréciation d'un service au cas par cas."),
        ("Des délais tenus",
         "Une administration qui doit répondre dans un délai, et dont le "
         "silence vaut accord, cesse d'être un obstacle à franchir."),
        ("Pas d'aubaine sociale, pas de carence nouvelle",
         "Le travail ouvre les droits qu'il finance ; la solidarité reste "
         "soumise aux règles de résidence qui existent déjà. Nous n'en "
         "ajoutons aucune."),
        ("L'État sur son cœur de métier",
         "Contrôler les identités et les casiers, juger l'asile vite, "
         "exécuter les décisions — et laisser les contrats de travail "
         "tranquilles."),
    ])

    corps += g.note(
        "<p><strong>Ce site ne vend pas un chiffre magique.</strong> Il ne "
        "promet ni « zéro immigration », ni « frontières ouvertes demain ». "
        "Il décrit une règle claire, ses effets attendus, ses coûts, les "
        "objections sérieuses qu'on lui oppose — onze, dans "
        "<a href=\"objections.html\">Objections</a> — et les trois seuils qui "
        "nous obligeraient à reconnaître que nous nous sommes trompés.</p>")

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html">Lire les sept engagements</a>
  <a href="chiffres.html">Tous les chiffres</a>
</div>
"""
    return corps
