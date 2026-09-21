"""Sources et méthode : d'où viennent les chiffres, et ce qu'ils valent."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "sources.html",
    "titre": "Sources et méthode",
    "description": (
        "Les sources publiques utilisées — DGEF, INSEE, OFPRA, CNDA, Cour des "
        "comptes, OCDE — la méthode de citation des chiffres, et les limites "
        "assumées de ce site."),
}

# Les sources, par famille. Le libellé dit ce qu'on y trouve : une liste de
# liens nus n'aide personne à vérifier quoi que ce soit.
SOURCES = [
    ("Les chiffres de l'immigration", [
        ("https://www.immigration.interieur.gouv.fr/Info-ressources/Etudes-et-statistiques/Statistiques",
         "Ministère de l'Intérieur, direction générale des étrangers en France "
         "(DGEF)",
         "Les publications « L'essentiel de l'immigration » et les tableaux "
         "annuels : premiers titres par motif, visas, éloignements, "
         "acquisitions de nationalité. C'est la source des flux."),
        ("https://www.insee.fr/fr/statistiques/3633212",
         "INSEE — immigrés et descendants d'immigrés",
         "Les stocks : combien d'immigrés et d'étrangers vivent en France, "
         "leur âge, leur emploi, leur origine. À ne pas confondre avec les "
         "flux ci-dessus."),
        ("https://ec.europa.eu/eurostat/web/migration-asylum/overview",
         "Eurostat — migration et asile",
         "Les mêmes grandeurs, comparables d'un pays européen à l'autre : "
         "c'est là qu'on vérifie si la France est une exception ou non."),
    ]),
    ("L'asile", [
        ("https://www.ofpra.gouv.fr/publications/rapports-dactivite",
         "OFPRA — rapports d'activité",
         "Demandes enregistrées, décisions, taux de protection, délais "
         "moyens d'instruction, par nationalité."),
        ("https://www.cnda.fr/Ressources-juridiques-et-geopolitiques/Rapports-d-activite",
         "Cour nationale du droit d'asile — rapports d'activité",
         "Les recours : volume, délais de jugement, taux d'annulation des "
         "décisions de l'OFPRA."),
    ]),
    ("Le droit en vigueur", [
        ("https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000042777182/",
         "CESEDA — code de l'entrée et du séjour des étrangers et du droit "
         "d'asile",
         "Le texte de référence : conditions de séjour, procédure d'asile, "
         "éloignement."),
        ("https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000006178264/",
         "Code du travail, art. L. 5221-1 et suivants",
         "L'autorisation de travail et son régime — le cœur de ce que le "
         "programme propose d'abroger."),
        ("https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049049130",
         "Loi n° 2024-42 du 26 janvier 2024",
         "La dernière grande loi, « pour contrôler l'immigration, améliorer "
         "l'intégration », dans sa version promulguée."),
        ("https://www.conseil-constitutionnel.fr/decision/2024/2023863DC.htm",
         "Conseil constitutionnel, décision n° 2023-863 DC du 25 janvier 2024",
         "La censure d'une trentaine d'articles de cette loi, et ses motifs."),
    ]),
    ("Les coûts et l'administration", [
        ("https://www.ccomptes.fr/fr/recherche?search_api_fulltext=immigration",
         "Cour des comptes",
         "Rapports sur l'entrée et le séjour des étrangers, l'hébergement des "
         "demandeurs d'asile, l'aide médicale de l'État et l'exécution des "
         "mesures d'éloignement."),
        ("https://www.conseil-etat.fr/publications-colloques/etudes-et-rapports",
         "Conseil d'État et juridiction administrative",
         "Le poids du contentieux des étrangers dans l'activité des tribunaux "
         "administratifs."),
        ("https://www.defenseurdesdroits.fr/rapports-annuels-11",
         "Défenseur des droits",
         "Les rapports sur la dématérialisation des services publics et "
         "l'accès aux guichets des préfectures."),
    ]),
    ("La recherche économique", [
        ("https://www.oecd.org/fr/migrations/",
         "OCDE — Perspectives des migrations internationales",
         "La synthèse annuelle, et les travaux sur l'impact budgétaire des "
         "migrations, d'où viennent les ordres de grandeur cités ici."),
        ("https://www.cepii.fr/CEPII/fr/publications/publications.asp",
         "CEPII",
         "Les travaux français sur l'impact budgétaire et macroéconomique de "
         "l'immigration (notamment X. Chojnicki et L. Ragot)."),
        ("https://www.aeaweb.org/articles?id=10.1257/jep.25.3.83",
         "M. Clemens, « Economics and Emigration: Trillion-Dollar Bills on the "
         "Sidewalk? » (2011)",
         "L'article de référence sur la « prime de lieu » : ce qu'un même "
         "travailleur gagne de plus du seul fait du pays où il travaille."),
        ("https://www.jstor.org/stable/2523702",
         "D. Card, « The Impact of the Mariel Boatlift on the Miami Labor "
         "Market » (1990)",
         "L'épisode le plus étudié d'arrivée soudaine et massive, et le point "
         "de départ de toute la littérature sur l'effet salarial."),
    ]),
]


def construire() -> str:
    corps = g.affiche(
        "Pour aller plus loin",
        "Sources <span class=\"serif\">et méthode</span>",
        "Tout chiffre cité sur ce site vient d'une publication publique et "
        "datée. Voici lesquelles, comment nous les citons, et ce que cette "
        "page ne peut pas vous garantir.")

    corps += g.note(
        "<p><strong>Les chiffres de ce site sont arrondis, et c'est "
        "volontaire.</strong> « Environ 330 000 premiers titres » se retient "
        "et se vérifie ; « 326 954 » donne une illusion de précision que "
        "la statistique migratoire n'a pas — les séries sont révisées, les "
        "périmètres changent d'une publication à l'autre, et les données "
        "provisoires d'une année sont corrigées la suivante. Pour citer un "
        "chiffre exact, allez à la source et prenez le sien, avec son "
        "millésime.</p>", "resume")

    for famille, entrees in SOURCES:
        corps += f"<h2>{famille}</h2><dl class=\"gloses\">"
        for url, nom, quoi in entrees:
            corps += (f'<dt><a href="{url}" rel="noopener">{nom}</a></dt>'
                      f"<dd>{quoi}</dd>")
        corps += "</dl>"

    corps += """
<h2 id="methode">Notre méthode</h2>
"""

    corps += g.gestes([
        "<strong>Un chiffre, une source, un millésime.</strong> Aucun chiffre "
        "n'est cité sans qu'on puisse dire d'où il vient et de quelle année "
        "il date.",
        "<strong>Des ordres de grandeur plutôt que des décimales.</strong> Les "
        "séries migratoires sont révisées ; une précision au millier "
        "survivrait rarement à la publication suivante.",
        "<strong>Les objections d'abord dans leur version forte.</strong> "
        "Celles de la page <a href=\"objections.html\">Objections</a> sont "
        "écrites comme les formulerait un contradicteur informé.",
        "<strong>Ce qu'on ignore est écrit.</strong> Trois incertitudes "
        "majeures sont nommées en fin de page Objections, et elles ne sont "
        "pas résolues.",
    ])

    corps += """
<h2 id="limites">Les limites de ce site</h2>
<p>Ce site est un <strong>document politique</strong>, écrit par un parti pour
défendre une réforme. Il n'est ni neutre, ni exhaustif, et ne prétend pas
l'être : il choisit ses chiffres pour éclairer une thèse. Ce qu'il s'interdit,
c'est de citer un chiffre faux, de tronquer une objection sérieuse, ou de
présenter comme acquis ce qui est discuté.</p>
<p>Il ne donne aucune information administrative individuelle. Pour une
démarche, la source est
<a href="https://www.service-public.fr/particuliers/vosdroits/N110">service-public.fr</a>
et, pour l'asile, l'<a href="https://www.ofpra.gouv.fr/">OFPRA</a>. Pour un
litige, un avocat ou une association spécialisée.</p>
<p>Une erreur, un chiffre périmé, une source qui manque&nbsp;? Le site est
ouvert : les corrections se proposent sur
<a href="https://github.com/g-pliberal/immigration">le dépôt</a>, et sont
publiées avec leur date.</p>
"""

    corps += """
<div class="actions">
  <a class="bouton" href="index.html">Revenir au programme</a>
</div>
"""
    return corps
