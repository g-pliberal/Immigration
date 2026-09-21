"""L'accueil : la promesse, les six engagements, et par où entrer."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "index.html",
    "titre": "Immigration — le programme du Parti libéral français",
    "description": (
        "Ce que fait la France en matière d'immigration, ce que cela produit, "
        "et l'alternative libérale : ouvrir le travail, garantir des délais, "
        "juger vite, et cesser de confondre venir travailler et vivre d'une "
        "aide."),
}

# Les six engagements. Ils sont écrits ici, une seule fois, et repris par la
# page Programme : deux listes d'engagements divergeraient dès la première
# correction, et le lecteur qui compare les deux pages compte les différences.
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
     "titre est réputé délivré. Aujourd'hui le silence de l'administration "
     "vaut refus, ce qui fait de la lenteur un instrument de politique "
     "publique."),
    ("4 ans", "Un titre pluriannuel dès la première délivrance.",
     "Quatre ans pour le travail et les études, renouvelables en ligne, au "
     "lieu d'un an renouvelé chaque année. Les files d'attente des préfectures "
     "sont pour l'essentiel faites de gens déjà en règle qui viennent le "
     "redemander."),
    ("3 mois", "L'asile jugé en trois mois, travail autorisé dès le dépôt.",
     "Un délai de trois mois recours compris, avec les moyens qui vont avec ; "
     "le droit de travailler dès l'enregistrement de la demande plutôt qu'après "
     "six mois d'inactivité forcée ; et l'éloignement effectif de ceux dont la "
     "demande est définitivement rejetée."),
    ("5 ans", "Le travail, pas le guichet : les aides après cinq ans.",
     "Les prestations non contributives — celles qu'on touche sans avoir "
     "cotisé — sont ouvertes après cinq ans de résidence régulière. Restent "
     "immédiats : les soins urgents, l'école des enfants, et les droits des "
     "réfugiés statutaires, qui relèvent de la protection et non de "
     "l'immigration de travail."),
    ("0", "Zéro file d'attente : le rendez-vous est un droit.",
     "Toute démarche en ligne de bout en bout, un rendez-vous garanti sous "
     "quinze jours quand la présence physique est nécessaire, et la gratuité "
     "des renouvellements. Le contentieux des étrangers, qui occupe environ "
     "quatre affaires sur dix devant les tribunaux administratifs, est d'abord "
     "un contentieux de procédure."),
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

    corps += g.reperes([
        ("Immigrés en France", "7,3 M",
         "10,7 % de la population — INSEE, 2023"),
        ("Premiers titres par an", "~330 000",
         "dont un tiers d'étudiants, un sixième de travail — DGEF, 2023-2024"),
        ("Part du travail", "≈ 17 %",
         "des premiers titres : la France fait entrer peu par le travail"),
        ("Décisions d'éloignement exécutées", "< 10 %",
         "des obligations de quitter le territoire prononcées"),
    ])

    corps += g.note(
        "<p><strong>Les chiffres de cette page sont des ordres de grandeur "
        "publics, datés et sourcés.</strong> Ils viennent du ministère de "
        "l'Intérieur, de l'INSEE, de l'OFPRA, de la Cour des comptes et de "
        "l'OCDE ; chaque page cite les siens, et "
        "<a href=\"sources.html\">Sources et méthode</a> les rassemble. Un "
        "chiffre d'immigration se périme vite : relisez la source avant de le "
        "citer.</p>", "resume")

    corps += """
<div class="paire">
  <div>
    <h2>Le constat</h2>
    <p>La France délivre environ 330 000 premiers titres de séjour par an. Un
    tiers va aux études, un peu plus d'un quart aux familles, un huitième à la
    protection — et <strong class="cle-texte">moins d'un sur six au
    travail</strong>. Ce n'est pas un hasard : notre droit traite le travail
    d'un étranger comme une exception qu'un préfet accorde, après avoir vérifié
    qu'aucun résident ne veut de l'emploi.</p>
    <p>Le résultat est connu de tous ceux qui l'ont vécu : des mois d'attente
    pour un contrat déjà signé, des files nocturnes devant les préfectures, un
    site qui ne donne pas de rendez-vous, un recours au tribunal pour obtenir
    ce rendez-vous — et, au bout, beaucoup de gens qui travaillent quand même,
    sans titre, pour un employeur qui en profite.</p>
    <p><a href="aujourdhui.html">Lire l'état des lieux</a> ·
    <a href="blocages.html">Ce qui coince, et pourquoi</a></p>
  </div>
  <div>
    <h2>La proposition</h2>
    <p>Elle tient en une phrase : <strong class="cle-texte">on ouvre la porte du
    travail, on ferme celle du guichet, et on juge vite</strong>.</p>
    <p>Ouvrir le travail, parce qu'un contrat de travail entre deux adultes
    consentants n'a pas à être autorisé par un tiers. Séparer l'accès au
    travail de l'accès aux aides non contributives, parce que c'est la seule
    objection sérieuse à l'ouverture, et qu'elle se traite par une règle de
    résidence plutôt que par une frontière. Juger vite, parce qu'une procédure
    d'asile qui dure deux ans fabrique elle-même l'irrégularité qu'on lui
    reproche ensuite.</p>
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
cela « les billets de mille laissés sur le trottoir ».</p>
<p>Et parce que la version française du débat est une impasse. Un camp promet
de fermer ce qui ne se ferme pas ; l'autre défend un système qu'il n'ose pas
décrire. Les deux laissent en place la même machine administrative : lente,
discrétionnaire, coûteuse, et qui rate ses propres objectifs — elle n'attire
pas les travailleurs dont l'économie manque, et n'éloigne pas ceux qui doivent
partir.</p>
"""

    corps += g.points([
        ("Le travail, pas la loterie",
         "Un titre délivré sur des critères écrits, vérifiables, opposables — "
         "et non sur l'appréciation d'un service au cas par cas."),
        ("Des délais tenus",
         "Une administration qui doit répondre dans un délai, et dont le "
         "silence vaut accord, cesse d'être un obstacle à franchir."),
        ("Pas d'aubaine sociale",
         "Les prestations non contributives après cinq ans de résidence : "
         "l'objection de Milton Friedman se traite par cette règle-là."),
        ("L'État sur son cœur de métier",
         "Contrôler les identités et les casiers, juger l'asile vite, "
         "exécuter les décisions — et laisser les contrats de travail "
         "tranquilles."),
    ])

    corps += g.note(
        "<p><strong>Ce site ne vend pas un chiffre magique.</strong> Il ne "
        "promet ni « zéro immigration », ni « frontières ouvertes demain ». "
        "Il décrit une règle claire, ses effets attendus, ses coûts, et les "
        "objections sérieuses qu'on lui oppose — avec leurs réponses, dans "
        "<a href=\"objections.html\">Objections</a>.</p>")

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html">Lire les six engagements</a>
  <a href="sources.html">Sources et méthode</a>
</div>
"""
    return corps
