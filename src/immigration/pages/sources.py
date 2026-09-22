"""Sources et méthode : d'où viennent les chiffres, et ce qu'ils valent."""

from __future__ import annotations

from .. import chiffrage as c
from .. import gabarit as g
from .chiffrage import fourchette, milliers

PAGE = {
    "fichier": "sources.html",
    "titre": "Sources et méthode",
    "description": (
        "Les sources publiques utilisées — DGEF, INSEE, OFPRA, CNDA, Conseil "
        "d'État, Conseil constitutionnel, CJUE, Cour des comptes, OCDE — la "
        "méthode de citation des chiffres, et les limites assumées de ce "
        "site."),
}

# Les sources, par famille. Le libellé dit ce qu'on y trouve : une liste de
# liens nus n'aide personne à vérifier quoi que ce soit.
SOURCES = [
    ("Les chiffres de l'immigration", [
        ("https://www.immigration.interieur.gouv.fr/documentation/"
         "etudes-et-statistiques/lessentiel-de-limmigration-donnees-2025.html",
         "Ministère de l'Intérieur, DGEF/DSED — « L'essentiel de "
         "l'immigration », données 2025",
         "Les publications annuelles : premiers titres par motif, "
         "renouvellements, régularisations, visas, éloignements, acquisitions "
         "de nationalité. C'est la source des flux, et celle de la majorité "
         "des chiffres de ce site."),
        ("https://www.insee.fr/fr/statistiques/3633212",
         "INSEE — immigrés et descendants d'immigrés",
         "Les stocks : combien d'immigrés et d'étrangers vivent en France, "
         "leur âge, leur emploi, leur origine. Attention à la rupture de "
         "série : le protocole du recensement a changé, les années "
         "antérieures à 2024 ne sont pas comparables."),
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
        ("https://www.cnda.fr/Ressources-juridiques-et-geopolitiques/"
         "Rapports-d-activite",
         "Cour nationale du droit d'asile — rapports d'activité",
         "Les recours : volume, délais de jugement, taux d'annulation des "
         "décisions de l'OFPRA."),
        ("https://www.immigration.interieur.gouv.fr/actualites/actualites/"
         "pacte-europeen-sur-migration-et-lasile-publication-de-circulaire-"
         "dapplication",
         "Pacte européen sur la migration et l'asile — circulaire "
         "d'application du 10 juin 2026",
         "Neuf règlements et une directive, applicables depuis le 12 juin "
         "2026 : filtrage aux frontières extérieures, procédure à la "
         "frontière, solidarité obligatoire. Aucun programme national d'asile "
         "ne s'écrit plus sans eux."),
    ]),
    ("Le droit en vigueur", [
        ("https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000042777182/",
         "CESEDA — code de l'entrée et du séjour des étrangers et du droit "
         "d'asile",
         "Le texte de référence : conditions de séjour, procédure d'asile, "
         "éloignement. L'article L. 435-4, voie de régularisation par les "
         "métiers en tension, expire le 31 décembre 2026."),
        ("https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/"
         "LEGISCTA000006178264/",
         "Code du travail, art. L. 5221-1 et suivants",
         "L'autorisation de travail et son régime — le cœur de ce que le "
         "programme propose d'abroger."),
        ("https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046600837/",
         "Code de l'action sociale et des familles, art. L. 262-4",
         "La condition de cinq ans de séjour régulier autorisant à travailler "
         "pour le RSA — la règle que le programme maintient, et dont il "
         "refuse d'étendre le principe."),
        ("https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=celex%3A32011L0098",
         "Directive 2011/98/UE — permis unique",
         "Quatre mois pour statuer sur une demande de permis (art. 5), et "
         "égalité de traitement en matière de sécurité sociale (art. 12). "
         "Le premier fonde notre engagement 2 ; le second interdisait notre "
         "ancien engagement 5."),
        ("https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049049130",
         "Loi n° 2024-42 du 26 janvier 2024",
         "La dernière grande loi, « pour contrôler l'immigration, améliorer "
         "l'intégration », dans sa version promulguée."),
    ]),
    ("Les décisions qui contraignent le programme", [
        ("https://www.conseil-constitutionnel.fr/decision/2024/2023863DC.htm",
         "Conseil constitutionnel, décision n° 2023-863 DC du 25 janvier 2024",
         "La censure d'une trentaine d'articles de la loi de 2024 — quotas "
         "migratoires, regroupement familial, caution étudiante — pour "
         "l'essentiel comme cavaliers législatifs, donc pour un motif de "
         "procédure."),
        ("https://www.conseil-constitutionnel.fr/decision/2024/20246RIP.htm",
         "Conseil constitutionnel, décision n° 2024-6 RIP du 11 avril 2024",
         "La décision qui a fait changer ce programme d'avis. Une condition "
         "de cinq ans de résidence pour l'accès des étrangers en séjour "
         "régulier aux prestations sociales porte une « atteinte "
         "disproportionnée » aux exigences des dixième et onzième alinéas du "
         "Préambule de 1946 — sur le fond, et non pour un motif de procédure."),
        ("https://curia.europa.eu/juris/liste.jsf?num=C-664/23",
         "CJUE, 19 décembre 2024, affaire C-664/23",
         "La France condamnée sur une condition posée aux prestations "
         "familiales des titulaires du permis unique : une charge "
         "supplémentaire qui ne pèse pas sur les nationaux est contraire à "
         "l'égalité de traitement."),
        ("https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2022-06-03/452798",
         "Conseil d'État, 3 juin 2022, n° 452798",
         "Une procédure administrative entièrement dématérialisée doit "
         "comporter une solution de substitution. C'est le fondement du "
         "guichet physique garanti de notre engagement 6."),
        ("https://www.senat.fr/rap/l24-426/l24-4265.html",
         "Sénat — rapport sur la proposition de loi créant une condition de "
         "durée de résidence pour le versement de certaines prestations",
         "L'inventaire des obstacles : Constitution, droit de l'Union, et "
         "trente-neuf conventions bilatérales de sécurité sociale comportant "
         "une clause d'égalité de traitement. À lire avant toute proposition "
         "de carence sociale."),
    ]),
    ("Les coûts et l'administration", [
        ("https://www.ccomptes.fr/sites/default/files/2024-01/"
         "20240104-communique-Politique-lutte-contre-immigration-irreguliere.pdf",
         "Cour des comptes — « La politique de lutte contre l'immigration "
         "irrégulière », janvier 2024",
         "Environ 1,8 milliard d'euros par an, près de 16 000 agents, des "
         "résultats jugés inefficaces, et les coûts unitaires : 4 414 € par "
         "éloignement forcé, 602 € par journée de rétention."),
        ("https://www.senat.fr/rap/l25-139-315/l25-139-3152.html",
         "Sénat — mission « Immigration, asile et intégration », PLF 2026",
         "Les crédits de la mission dans le projet de loi, et les prévisions "
         "de bénéficiaires de l'allocation pour demandeur d'asile."),
        ("https://www.conseil-etat.fr/publications-colloques/etudes-et-rapports",
         "Conseil d'État — rapport public sur l'activité juridictionnelle",
         "Le poids du contentieux des étrangers : près de la moitié des "
         "requêtes nouvelles devant les tribunaux administratifs, et environ "
         "autant en appel."),
        ("https://www.senat.fr/rap/r24-841/r24-841-syn.pdf",
         "Sénat — rapport d'information sur l'aide médicale de l'État",
         "Bénéficiaires, dépense constatée et budget voté, et la comparaison "
         "avec les dispositifs équivalents en Europe."),
        ("https://www.defenseurdesdroits.fr/rapports-annuels-11",
         "Défenseur des droits",
         "Les rapports sur la dématérialisation des services publics et "
         "l'accès aux guichets des préfectures — y compris quand ils "
         "contredisent ce que ce site proposait."),
    ]),
    ("Le chiffrage du programme", [
        ("https://www.assemblee-nationale.fr/dyn/contenu/visualisation/"
         "1087981/file/PAP2026_BG_Immigration_asile_integration_IA.pdf",
         "Projet annuel de performances 2026 — « Immigration, asile et "
         "intégration »",
         "L'allocation des seuls demandeurs d'asile (222,2 M€), les places "
         "d'hébergement et leur coût journalier, et l'indicateur du délai "
         "global d'une demande d'asile : 299 jours en 2024."),
        ("https://www.assemblee-nationale.fr/dyn/17/textes/"
         "l17t0227_texte-adopte-seance.pdf",
         "Loi n° 2026-103 du 19 février 2026 de finances pour 2026",
         "Les crédits votés de la mission (2,13 Md€, état B) et les nouveaux "
         "tarifs des titres de séjour (art. 128)."),
        ("https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/"
         "1087921/file/PLF%202026_Evaluations%20pr%C3%A9alables_Vdef.pdf",
         "Évaluations préalables du projet de loi de finances pour 2026, "
         "article 30",
         "Les effectifs des services des étrangers des préfectures (4 173 "
         "équivalents temps plein en 2024), leur masse salariale, et le coût "
         "d'une première délivrance de titre évalué par l'État : 547 €."),
        ("https://www.senat.fr/rap/l25-139-21/l25-139-21_mono.html",
         "Sénat — rapport général sur le projet de loi de finances pour 2026, "
         "article 30",
         "Le produit des taxes sur les titres de séjour — de l'ordre de "
         "200 M€ par an —, et l'évolution du coût d'un titre depuis 2011."),
        ("https://www.service-public.gouv.fr/particuliers/actualites/A18881",
         "service-public.fr — les tarifs des titres de séjour au 1er mai 2026",
         "350 € pour une première délivrance, 250 € pour un renouvellement, "
         "300 € de droit de visa de régularisation."),
        ("https://www.assemblee-nationale.fr/dyn/contenu/visualisation/"
         "1097914/file/EAT%20-%20PPL%201799%20Renouvellement%20automatique"
         "%20des%20titres%20de%20s%C3%A9jour.pdf",
         "Assemblée nationale — rapport sur la proposition de loi n° 1799 "
         "(renouvellement automatique des titres)",
         "Les renouvellements de 2024 par motif : c'est lui qui montre que le "
         "titre de quatre ans ne concerne que 338 470 renouvellements de "
         "travail et d'études."),
        ("https://www.ofpra.gouv.fr/sites/default/files/2026-07/"
         "Rapport%20d%27activit%C3%A9%202025%20Ofpra.pdf",
         "OFPRA — rapport d'activité 2025",
         "156 509 décisions, 163 jours d'instruction en moyenne, 109,5 M€ de "
         "dépenses."),
        ("https://www.cnda.fr/Media/mediatheque-cnda/documents/"
         "rapports-d-activite/rapport-d-activite-2025",
         "Cour nationale du droit d'asile — rapport d'activité 2025",
         "53 086 décisions pour 60 065 recours, et un délai moyen de cinq "
         "mois et demi."),
        ("https://www.conseil-etat.fr/content/download/239412/document/"
         "CE_RA_2025_PDFweb_Access_0926.pdf",
         "Conseil d'État — rapport public 2026, activité juridictionnelle de "
         "2025",
         "154 391 affaires d'étrangers devant les tribunaux administratifs, "
         "46 % des entrées, une hausse portée par les procédures "
         "d'éloignement."),
        ("https://www.senat.fr/rap/r25-004/r25-004_mono.html",
         "Sénat — rapport d'information n° 4 (2025-2026) sur la rétention",
         "34,5 jours de rétention en moyenne en 2024, et 38,8 % seulement des "
         "placements qui aboutissent à un éloignement en métropole."),
        ("https://www.strategie-plan.gouv.fr/files/files/Publications/2025/"
         "2025-12-12%20-%20Rapport%20SMIC/"
         "SMIC-RAPPORT-2025-11decembre13h30-complet-2.pdf",
         "Groupe d'experts sur le SMIC — rapport 2025",
         "Le coût d'un salarié au SMIC pour son employeur, et ce qui en "
         "revient au salarié : ce qu'une régularisation fait entrer en "
         "cotisations."),
        ("https://www.senat.fr/rap/r23-772/r23-772_mono.html",
         "Sénat — rapport d'information n° 772 (2023-2024) sur la formation "
         "linguistique",
         "Ce que coûtent les cours de français du contrat d'intégration "
         "républicaine, et ce qu'ils produisent."),
        ("https://doi.org/10.1086/730122",
         "J. Elias, J. Monras et J. Vázquez-Grenno, « Understanding the "
         "Effects of Granting Work Permits to Undocumented Immigrants » (2025)",
         "La régularisation espagnole de 2005 : environ 4 000 € de "
         "cotisations de plus par personne régularisée et par an. C'est la "
         "borne haute de notre hypothèse, pas notre hypothèse."),
        ("https://doi.org/10.1126/sciadv.aap9519",
         "M. Marbach, J. Hainmueller et D. Hangartner, « The long-term impact "
         "of employment bans on the economic integration of refugees » (2018)",
         "Sept mois d'interdiction de travailler de plus : vingt points "
         "d'emploi de moins cinq ans après, chez les réfugiés arrivés en "
         "Allemagne. Le gain que ce chiffrage ne compte presque pas."),
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
         "travailleur gagne de plus du seul fait du pays où il travaille. "
         "Clemens précise lui-même que son estimation suppose que les "
         "institutions du pays d'accueil continuent de fonctionner."),
        ("https://www.jstor.org/stable/2523702",
         "D. Card, « The Impact of the Mariel Boatlift on the Miami Labor "
         "Market » (1990)",
         "L'épisode le plus étudié d'arrivée soudaine et massive. À lire "
         "avec les deux textes suivants : la conclusion de Card est disputée, "
         "et citer l'un sans les autres serait malhonnête."),
        ("https://www.nber.org/papers/w21588",
         "G. Borjas, « The Wage Impact of the Marielitos: A Reappraisal » "
         "(2016)",
         "La contestation la plus sérieuse de Card : en restreignant "
         "l'échantillon aux hommes non diplômés, Borjas trouve une baisse de "
         "salaire marquée."),
        ("https://www.journals.uchicago.edu/doi/10.1086/701464",
         "G. Peri et V. Yasenov, « The Labor Market Effects of a Refugee "
         "Wave » (2019)",
         "La réplique à Borjas, par contrôle synthétique : la conclusion "
         "initiale de Card résiste. La controverse n'est pas close."),
        ("https://academic.oup.com/restud/article/84/1/356/2669971",
         "C. Dustmann, U. Schönberg et J. Stuhler, « Labor Supply Shocks, "
         "Native Wages, and the Adjustment of Local Employment » (2017)",
         "Des effets négatifs marqués sur l'emploi local, sur le cas des "
         "navetteurs tchèques. Ce site le cite parce qu'il ne va PAS dans "
         "son sens."),
    ]),
]


def construire() -> str:
    corps = g.affiche(
        "Pour aller plus loin",
        "Sources <span class=\"serif\">et méthode</span>",
        "Tout chiffre cité sur ce site vient d'une publication publique et "
        "datée, et renvoie à sa fiche. Voici les sources, comment nous les "
        "citons, ce que nous avons corrigé, et ce que cette page ne peut pas "
        "vous garantir.")

    corps += g.note(
        "<p><strong>Chaque chiffre du site a une fiche, et chaque fiche a une "
        "réserve.</strong> Les valeurs vivent dans un registre unique — "
        "<code>src/immigration/chiffres.py</code> — d'où les fiches de "
        "repères et les tableaux de chiffres sont <em>construits</em> : ils "
        "ne peuvent pas diverger des fiches, et une clé inconnue fait échouer "
        "la construction du site. Quand un chiffre est repris dans une phrase, "
        "pour qu'elle se lise, il est suivi du petit lien qui mène à sa "
        f"fiche. Les {g.fiches_du_registre()} fiches, avec leur source, leur "
        "millésime et ce "
        "que le chiffre ne dit pas, sont dans "
        "<a href=\"chiffres.html\">Tous les chiffres</a>.</p>",
        "resume")

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
        "<strong>Un chiffre, une source, un millésime — et une réserve.</strong> "
        "Chaque chiffre porte l'année de ses <em>données</em>, qui n'est pas "
        "celle de sa publication, et la phrase qui dit ce qu'il ne prouve pas.",
        "<strong>Des ordres de grandeur plutôt que des décimales.</strong> Les "
        "séries migratoires sont révisées ; quand la source publie une valeur "
        "exacte, la fiche la donne à côté de l'arrondi.",
        "<strong>Les objections d'abord dans leur version forte.</strong> "
        "Les onze de la page <a href=\"objections.html\">Objections</a> sont "
        "écrites comme les formulerait un contradicteur informé — y compris "
        "celles qui ne sont pas économiques.",
        "<strong>Les sources qui nous contredisent sont citées aussi.</strong> "
        "Borjas contre Card, Dustmann contre nous, le Défenseur des droits "
        "contre notre engagement 6 : un dossier d'où les pièces gênantes ont "
        "été retirées ne vaut rien.",
        "<strong>Ce qu'on ignore est écrit, et ce qu'on a corrigé aussi.</strong> "
        "Quatre incertitudes majeures sont nommées en fin de page Objections ; "
        "les changements d'avis sont listés ci-dessous plutôt que faits en "
        "silence.",
    ])

    corps += """
<h2 id="corrections">Ce que nous avons corrigé, et pourquoi</h2>
<p>Ce site a été relu ligne à ligne comme l'aurait fait un adversaire
compétent. Voici ce que cette relecture a changé. Nous le publions parce
qu'un programme qui se corrige sans le dire donne à penser qu'il a quelque
chose à cacher — et parce que la première version de ces pages circule
peut-être encore.</p>
"""

    corps += g.tableau(
        ["Ce que le site disait", "Pourquoi c'était faux ou fragile",
         "Ce qu'il dit maintenant"],
        [["Prestations non contributives après cinq ans de résidence, "
          "« la clé de tout le reste »",
          "Le Conseil constitutionnel a jugé cette durée disproportionnée le "
          "11 avril 2024. S'y ajoutent la directive 2011/98 et trente-neuf "
          "conventions bilatérales",
          "Aucune carence nouvelle : les règles existantes sont maintenues, "
          "aucune n'est ajoutée, et la réponse à Friedman passe par la "
          "condition d'entrée"],
         ["« Un délai de carence a été censuré en 2024 pour un motif de "
          "procédure »",
          "Confusion entre la décision DC du 25 janvier 2024 (cavaliers "
          "législatifs) et la décision RIP du 11 avril 2024 (censure au fond)",
          "Les deux décisions sont citées séparément, avec leur portée exacte"],
         ["Environ 330 000 premiers titres, un sur six pour le travail",
          "Données 2023 présentées sous un millésime 2026. Le total est passé "
          "à 384 230 et l'ordre des motifs a changé",
          "Données 2025, avec l'évolution par motif et la hausse expliquée "
          "par l'humanitaire"],
         ["« L'essentiel du contentieux des étrangers porte sur la procédure, "
          "pas sur le fond »",
          "Faux : la masse est faite de recours contre des refus de séjour et "
          "des OQTF, qui sont des contentieux au fond",
          "La part procédurale est revendiquée, la moitié du rôle des "
          "tribunaux ne l'est plus"],
         ["Moins de 10 % des OQTF exécutées",
          "Chiffre périmé — le taux est remonté à 11,4 % — et ratio "
          "méthodologiquement boiteux",
          "Le chiffre à jour, la hausse des éloignements, et la critique du "
          "ratio faite par nous plutôt que contre nous"],
         ["L'asile jugé en trois mois recours compris",
          "Aucun pays comparable n'y parvient, et le règlement européen "
          "applicable depuis juin 2026 fixe ses propres bornes",
          "Six mois opposables à deux ans, trois mois à terme"],
         ["« Strictement pas plus attirante » pour qui n'a pas de promesse "
          "d'embauche",
          "Démenti par notre propre engagement 4, qui ouvre le travail dès le "
          "dépôt d'une demande d'asile",
          "L'effet est reconnu, et la contrepartie — instruction rapide, "
          "rejets exécutés — est explicitée"],
         ["Démarches « en ligne de bout en bout »",
          "Contredit par le Défenseur des droits, que le site citait en "
          "source, et par le Conseil d'État du 3 juin 2022",
          "En ligne par défaut, guichet physique garanti"],
         ["« Le coût net est probablement négatif »",
          "Aucun euro avancé, dans un site dont la méthode affichée exige une "
          "source par chiffre",
          "Un chiffrage calculé, en deux scénarios, et l'aveu qu'il coûte "
          "d'abord — voir le tableau suivant"],
         ["Card (1990) cité seul ; « billets de mille »",
          "L'étude la plus contestée de la discipline, et une traduction qui "
          "divise le titre de Clemens par un milliard",
          "La controverse Borjas / Peri-Yasenov est citée, et les « billets "
          "de mille milliards » rétablis"]],
        legende="Les dix corrections principales. Les autres — l'échéance de "
                "l'article L. 435-4, le pacte européen, la survie du titre "
                "après un licenciement, la preuve du travail, la soupape "
                "d'ordre public — sont des ajouts plutôt que des "
                "rectifications.",
        classes_colonnes=["long", "long", "long"])

    # Ce que le chiffrage a corrigé. Les montants sont pris au module de
    # calcul, comme sur la page du chiffrage : une correction qui citerait un
    # chiffre différent de celui qu'elle corrige serait une faute de plus.
    def postes(*cles: str) -> list:
        return [p for p in c.POSTES if p.cle in cles]

    evites = sorted(
        round(c._renouvellements_evites(c.scenario(nom, 5).__getitem__, 5), -4)
        for nom in ("prudent", "favorable"))
    corps += """
<h3 id="corrections-chiffrage">Ce que le chiffrage a corrigé</h3>
<p>Calculer le chiffrage au lieu de l'écrire a fait apparaître des fautes que
le tableau de phrases laissait passer. Les voici, avec le chiffre qui les
remplace — tiré du même calcul que la <a href="chiffrage.html">page du
chiffrage</a>.</p>
"""
    corps += g.tableau(
        ["Ce que le site disait", "Pourquoi c'était faux ou fragile",
         "Ce qu'il dit maintenant"],
        [["« 600 000 à 700 000 dossiers de moins » grâce au titre de quatre "
          "ans",
          "Le titre de quatre ans ne vise que les titres de travail et "
          "d'études : 338 470 renouvellements en 2024, pas 955 080",
          f"{milliers(evites[0])} à {milliers(evites[1])} renouvellements "
          "de moins par an"],
         ["Rien sur la gratuité des renouvellements",
          "C'est une recette que l'État perçoit aujourd'hui, et que "
          "l'engagement 6 supprime",
          "Comptée : " + fourchette(*c.fourchette(postes(
              "gratuite-renouvellements", "renouvellements-taxes"), 5),
              absolu=True)
          + " de recette perdue par an, le plus gros moins durable du "
          "programme"],
         ["« Instruire en six mois au lieu de dix-huit » ; « dix-huit mois » "
          "d'attente",
          "Vrai en 2021. L'indicateur officiel donne 299 jours en 2024",
          "Près de dix mois, partout sur le site, et des économies "
          "recalculées sur cette base"],
         ["« 0,3 à 0,6 Md€ » d'économies sur l'asile",
          "Comptées sans ce que coûtent les personnes protégées plus tôt — le "
          "RSA plus tôt — ni les déboutées plus tôt — l'aide médicale plus "
          "tôt",
          "Les plus et les moins de l'asile calculés ensemble : "
          + fourchette(*c.fourchette(postes(
              "ada-attente", "hebergement-attente", "proteges-plus-tot",
              "deboutes-plus-tot", "renfort-ofpra-cnda"), 5))
          + " par an, éloignements non compris"],
         ["Éloignements : « plus de 4 500 € » l'unité, « 40 à 150 M€ » en "
          "tout",
          "La Cour des comptes écrit 4 414 €, hors rétention ; or un "
          "éloignement demande en moyenne plus d'un placement en rétention, "
          "à environ 20 800 € le placement",
          fourchette(*c.fourchette(postes("eloignements"), 5))
          + " par an pour 4 000 éloignements forcés de plus, et le prix de "
          "chaque millier au-delà"],
         ["L'allocation des demandeurs d'asile à 299 M€, la mission à "
          "2,16 Md€",
          "Le premier chiffre comprend les Ukrainiens sous protection "
          "temporaire, qui ont le droit de travailler ; le second est celui "
          "du projet de loi, pas de la loi votée",
          "222 M€ et 2,13 Md€"],
         ["Le contentieux des étrangers, « ≈ 50 % » des tribunaux "
          "administratifs",
          "43 % en 2024",
          "46 % en 2025, dernier chiffre publié"],
         ["La gratuité des renouvellements « immédiate, par décret »",
          "Le montant des taxes est écrit dans la loi (CESEDA, "
          "art. L. 436-1)",
          "Rangée dans la loi de finances de la première année"],
         ["« Le solde est négatif les deux premières années, et probablement "
          "positif ensuite »",
          "Aucun calcul ne l'établissait",
          "Négatif sur tout l'horizon dans le scénario prudent ; nettement "
          "positif à terme dans le scénario favorable ; entre les deux, une "
          "hypothèse que personne ne mesure — la part de travail au noir"]],
        legende="Les corrections apportées par le chiffrage, en septembre "
                "2026.",
        classes_colonnes=["long", "long", "long"])

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
  <a class="bouton" href="chiffres.html">Tous les chiffres, un par un</a>
  <a href="index.html">Revenir au programme</a>
</div>
"""
    return corps
