"""Le registre des chiffres : un chiffre, une source, un millésime, une réserve.

Pourquoi ce module existe. Le site promet, page « Sources et méthode », que
tout chiffre cité vient d'une publication publique et datée. Tant que les
chiffres étaient écrits en clair dans le texte de chaque page, cette promesse
était invérifiable et, pire, périssable : un chiffre corrigé à un endroit
restait faux aux trois autres, et rien ne disait de quelle année il datait.

Chaque chiffre est donc écrit **ici et une seule fois**, avec ce qu'il mesure,
d'où il vient, l'année des données — qui n'est pas l'année de publication —
et la réserve de méthode qu'il faut connaître avant de le citer. Les pages ne
l'écrivent plus : elles le demandent par sa clé. Un chiffre sans source ne
peut donc plus entrer dans le site, et la page ``chiffres.html`` se construit
toute seule à partir de ce dictionnaire.

Les arrondis restent volontaires (voir ``Chiffre.valeur``) : les séries
migratoires sont révisées d'une publication à l'autre, et une précision au
millier survit rarement à la suivante. Quand la source publie un chiffre
exact, on l'écrit exact dans ``exact`` et arrondi dans ``valeur`` — le lecteur
qui veut citer dispose des deux.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chiffre:
    """Un chiffre du site, avec tout ce qui permet de le contester.

    ``valeur`` est ce qui s'affiche dans le texte : un ordre de grandeur, tenu
    court. ``exact`` est la valeur publiée par la source, quand elle en publie
    une. ``annee`` est le millésime des DONNÉES ; ``publie`` la date de la
    publication qui les porte. Les deux diffèrent presque toujours d'un an, et
    c'est la confusion la plus fréquente du débat migratoire.

    ``reserve`` est le champ qui fait le travail : il dit ce que le chiffre ne
    dit pas. Un chiffre dont on ne sait pas énoncer la limite n'a rien à faire
    dans un document politique.
    """

    valeur: str
    mesure: str
    source: str
    url: str
    annee: str
    publie: str = ""
    exact: str = ""
    reserve: str = ""
    evolution: str = ""
    familles: tuple[str, ...] = field(default_factory=tuple)


# Les familles servent au classement de la page « Tous les chiffres ». L'ordre
# est celui de la lecture du site : qui est là, qui entre, l'asile, les
# sorties, l'administration, l'argent.
FAMILLES = (
    ("population", "Qui vit en France"),
    ("flux", "Qui entre, et par quelle porte"),
    ("asile", "L'asile"),
    ("eloignement", "Les sorties"),
    ("administration", "L'administration et le juge"),
    ("argent", "L'argent public"),
)

_DGEF = ("Ministère de l'Intérieur, DGEF/DSED, « L'essentiel de "
         "l'immigration » — données 2025")
_DGEF_URL = ("https://www.immigration.interieur.gouv.fr/documentation/"
             "etudes-et-statistiques/lessentiel-de-limmigration-donnees-2025.html")
_INSEE = "INSEE, « L'essentiel sur… les immigrés et les étrangers »"
_INSEE_URL = "https://www.insee.fr/fr/statistiques/3633212"
_CE = "Conseil d'État, rapport public 2025 — activité juridictionnelle"
_CE_URL = ("https://www.conseil-etat.fr/content/download/228336/document/"
           "CE_RA_2024_PDFweb_.pdf")
_CE_2026 = ("Conseil d'État, rapport public 2026 — activité juridictionnelle "
            "de 2025")
_CE_2026_URL = ("https://www.conseil-etat.fr/content/download/239412/document/"
                "CE_RA_2025_PDFweb_Access_0926.pdf")
_CDC = ("Cour des comptes, « La politique de lutte contre l'immigration "
        "irrégulière », rapport public thématique")
_CDC_URL = ("https://www.ccomptes.fr/sites/default/files/2024-01/"
            "20240104-communique-Politique-lutte-contre-immigration-irreguliere.pdf")
# Les documents budgétaires de 2026, dans la copie qu'en publie l'Assemblée
# nationale : le site du ministère des comptes publics refuse les accès
# automatisés, et un lien qu'on ne peut pas vérifier ne sert à rien.
_PAP = ("Projet annuel de performances 2026, mission « Immigration, asile et "
        "intégration »")
_PAP_URL = ("https://www.assemblee-nationale.fr/dyn/contenu/visualisation/"
            "1087981/file/PAP2026_BG_Immigration_asile_integration_IA.pdf")
_EVALUATIONS = ("Évaluations préalables des articles du projet de loi de "
                "finances pour 2026, article 30")
_EVALUATIONS_URL = ("https://www.assemblee-nationale.fr/dyn/dyn/contenu/"
                    "visualisation/1087921/file/"
                    "PLF%202026_Evaluations%20pr%C3%A9alables_Vdef.pdf")

# Une rupture de série que tout le site doit porter : le protocole de collecte
# du recensement a changé, et les chiffres de population d'avant 2024 ne se
# comparent pas à ceux de 2024 et 2025. Sans cette phrase, la hausse affichée
# se lit comme une hausse réelle — elle est pour partie un changement de
# méthode, et un adversaire a raison de le relever.
_RUPTURE = ("Rupture de série : le protocole de collecte du recensement a "
            "changé, les données antérieures à 2024 ne sont pas directement "
            "comparables. Une partie de la hausse affichée est un effet de "
            "méthode, pas un flux.")

CHIFFRES: dict[str, Chiffre] = {
    # ---------------------------------------------------------------- population
    "immigres": Chiffre(
        valeur="8,0 M", exact="8,0 millions, soit 11,6 % de la population",
        mesure="Personnes nées étrangères à l'étranger et vivant en France, "
               "qu'elles soient devenues françaises ou non",
        source=_INSEE, url=_INSEE_URL, annee="2025", publie="2026",
        reserve=_RUPTURE, familles=("population",)),
    "etrangers": Chiffre(
        valeur="6,3 M", exact="6,3 millions, soit 9,1 % de la population",
        mesure="Personnes n'ayant pas la nationalité française, qu'elles "
               "soient nées en France ou non",
        source=_INSEE, url=_INSEE_URL, annee="2025", publie="2026",
        reserve=_RUPTURE + " À ne pas confondre avec le nombre d'immigrés : "
                "les deux ensembles se recoupent sans se confondre.",
        familles=("population",)),
    "immigres-francais": Chiffre(
        valeur="33 %", exact="2,6 millions, soit 33 % des immigrés",
        mesure="Part des immigrés ayant acquis la nationalité française",
        source=_INSEE, url=_INSEE_URL, annee="2025", publie="2026",
        reserve="Ce tiers n'est plus étranger : le compter dans un chiffre "
                "d'« étrangers » est la première façon de fausser le débat.",
        familles=("population",)),
    "sejour-regulier": Chiffre(
        valeur="≈ 4,5 M", exact="environ 4,5 millions au 31 décembre 2025",
        mesure="Étrangers détenteurs d'un titre de séjour en cours de validité",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="+ 3,2 % sur un an",
        reserve="Ne comprend ni les Européens, qui n'ont pas besoin de titre, "
                "ni les personnes en situation irrégulière, qu'aucune "
                "statistique ne dénombre.",
        familles=("population",)),

    # --------------------------------------------------------------------- flux
    "premiers-titres": Chiffre(
        valeur="384 230", exact="384 230",
        mesure="Premiers titres de séjour délivrés en un an à des "
               "ressortissants de pays tiers",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="+ 11,2 % sur un an",
        reserve="Données provisoires. La hausse vient presque entièrement du "
                "motif humanitaire ; les autres motifs sont stables ou en "
                "baisse. Les Européens n'y figurent pas.",
        familles=("flux",)),
    "titres-etudiants": Chiffre(
        valeur="118 000", exact="environ 118 000, soit 31 %",
        mesure="Premiers titres délivrés pour motif étudiant",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="stable, au même niveau pour la troisième année",
        reserve="Un titre d'étudiant est annuel : la même personne réapparaît "
                "dans les renouvellements chaque année de ses études.",
        familles=("flux",)),
    "titres-humanitaire": Chiffre(
        valeur="92 600", exact="92 600, soit 24 %",
        mesure="Premiers titres délivrés pour motif humanitaire — réfugiés, "
               "protection subsidiaire, étrangers malades, victimes de traite",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="+ 65 % sur un an ; les protections subsidiaires ont plus "
                  "que doublé",
        reserve="C'est ce motif, et lui seul, qui explique la hausse de 2025. "
                "Il dépend des crises du monde, non de la politique "
                "migratoire française.",
        familles=("flux", "asile")),
    "titres-familial": Chiffre(
        valeur="≈ 90 000", exact="",
        mesure="Premiers titres délivrés pour motif familial",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="stable",
        reserve="Part déduite : le communiqué de la DGEF publie le total, et "
                "l'évolution de ce motif (stabilité), sans en détailler le "
                "volume. Le motif familial et le motif « divers » totalisent "
                "ensemble 122 440 titres. À remplacer par le chiffre publié "
                "dès la parution du tableau détaillé.",
        familles=("flux",)),
    "titres-economique": Chiffre(
        valeur="51 190", exact="51 190, soit 13 %",
        mesure="Premiers titres délivrés pour motif économique — salariés, "
               "travailleurs temporaires, cartes « talent », entrepreneurs",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="− 13 % sur un an, dont environ − 30 % pour les saisonniers",
        reserve="C'est le seul motif que la politique migratoire pilote "
                "directement, et il baisse. Le chiffre du site le plus "
                "important, et le plus contestable politiquement.",
        familles=("flux",)),
    "titres-divers": Chiffre(
        valeur="≈ 32 000", exact="",
        mesure="Premiers titres délivrés pour d'autres motifs — visiteurs, "
               "retraités, motifs non classés",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        reserve="Part déduite, comme le motif familial : voir la réserve de "
                "cette ligne.",
        familles=("flux",)),
    "part-travail": Chiffre(
        valeur="13 %", exact="51 190 sur 384 230",
        mesure="Part du travail dans les premiers titres de séjour",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="17 % en 2023, 13 % en 2025",
        reserve="La part baisse en partie parce que le motif humanitaire "
                "monte, non parce que le travail s'effondre en volume. Les "
                "deux lectures sont vraies et il faut donner les deux.",
        familles=("flux",)),
    "renouvellements": Chiffre(
        valeur="955 080", exact="955 080",
        mesure="Titres de séjour renouvelés en un an",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="+ 7,6 % sur un an ; près de deux renouvellements sur cinq "
                  "pour motif familial",
        reserve="C'est le chiffre qui décrit la charge réelle des "
                "préfectures : deux fois et demie plus de renouvellements que "
                "de premières demandes. Il ne mesure aucune entrée.",
        familles=("flux", "administration")),
    "regularisations": Chiffre(
        valeur="28 610", exact="28 610",
        mesure="Admissions exceptionnelles au séjour — les « régularisations »",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="− 10,1 % sur un an, après la circulaire de janvier 2025",
        reserve="Décisions discrétionnaires : le même dossier reçoit des "
                "réponses différentes selon la préfecture, ce qu'aucun chiffre "
                "national ne montre.",
        familles=("flux",)),
    "aes-travail": Chiffre(
        valeur="9 690", exact="9 690 régularisations pour motif économique en "
                              "2025, dont 1 655 au titre des métiers en tension",
        mesure="Régularisations par le travail",
        source="Ministère de l'Intérieur, instruction aux préfets rapportée "
               "par l'AFP le 15 avril 2026",
        url=("https://observalgerie.com/2026/04/17/immigration/titres-de-"
             "sejour-metiers-en-tension-pourquoi-si-peu-de-regularisations-"
             "en-2025"),
        annee="2025", publie="avril 2026",
        evolution="en baisse de plus de moitié sur un an ; la voie « métiers "
                  "en tension » de la loi de 2024 n'en a produit que 1 655",
        reserve="Chiffre rapporté par la presse d'après un document du "
                "ministère, et non tiré d'une publication statistique : il est "
                "à remplacer par celui de la DGEF dès sa parution détaillée. "
                "C'est le repère de l'hypothèse la plus fragile du chiffrage — "
                "combien de régularisations le programme ajouterait.",
        familles=("flux",)),
    "renouvellements-travail-etudes": Chiffre(
        valeur="338 470", exact="338 470 en 2024 : 194 240 pour motif "
                                "économique et 144 230 pour études",
        mesure="Titres de séjour renouvelés pour motif économique ou d'études",
        source="Assemblée nationale, commission des lois, rapport sur la "
               "proposition de loi n° 1799 (C. Capdevielle) — données du "
               "ministère de l'Intérieur",
        url=("https://www.assemblee-nationale.fr/dyn/contenu/visualisation/"
             "1097914/file/EAT%20-%20PPL%201799%20Renouvellement%20automatique"
             "%20des%20titres%20de%20s%C3%A9jour.pdf"),
        annee="2024", publie="décembre 2025",
        evolution="sur 879 790 renouvellements en 2024, tous motifs : "
                  "325 780 familiaux, 171 290 divers, 44 250 humanitaires",
        reserve="Champ : France hexagonale, hors Britanniques — un peu plus "
                "étroit que celui du total cité ailleurs sur ce site. Ce sont "
                "les seuls renouvellements que le titre de quatre ans de "
                "l'engagement 3 concerne : il ne supprime pas les 600 000 à "
                "700 000 renouvellements qu'annonçait la première version de "
                "ce programme.",
        familles=("flux", "administration")),

    # -------------------------------------------------------------------- asile
    "asile-demandes": Chiffre(
        valeur="151 665", exact="151 665",
        mesure="Demandes d'asile enregistrées en un an, mineurs compris",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="− 3,7 % sur un an",
        reserve="Une demande n'est pas une personne entrée cette année-là : "
                "une part est déposée par des personnes présentes depuis "
                "plusieurs mois.",
        familles=("asile",)),
    "asile-protection": Chiffre(
        valeur="52 %", exact="52 %",
        mesure="Taux de protection, recours devant la CNDA compris",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="environ un tiers les années précédentes",
        reserve="Ce taux dépend des nationalités qui demandent — il a bondi "
                "avec l'Afghanistan et l'Ukraine. Il ne mesure pas la "
                "sévérité de l'OFPRA.",
        familles=("asile",)),
    "delai-asile": Chiffre(
        valeur="299 jours", exact="299 jours en 2024",
        mesure="Délai global moyen d'une demande d'asile, de sa présentation "
               "à la décision définitive, recours compris",
        source=_PAP + ", indicateur 1.1", url=_PAP_URL,
        annee="2024", publie="octobre 2025",
        evolution="488 jours en 2021, 402 en 2022, 332 en 2023 ; cible de "
                  "185 jours",
        reserve="Une moyenne : les procédures accélérées sont plus courtes, "
                "celles qui passent par la CNDA plus longues. Le délai de "
                "l'OFPRA est remonté en 2025 (163 jours contre 138), ce qui "
                "laisse attendre un chiffre 2025 au moins égal. Ce site "
                "écrivait « dix-huit mois » : c'était vrai en 2021, ce ne "
                "l'est plus.",
        familles=("asile",)),
    "ofpra-activite": Chiffre(
        valeur="≈ 700 €", exact="environ 700 € par décision : 109,5 M€ de "
                                "dépenses pour 156 509 décisions en 2025",
        mesure="Coût d'une décision de l'OFPRA, et son délai d'instruction",
        source="OFPRA, rapport d'activité 2025",
        url=("https://www.ofpra.gouv.fr/sites/default/files/2026-07/"
             "Rapport%20d%27activit%C3%A9%202025%20Ofpra.pdf"),
        annee="2025", publie="juillet 2026",
        evolution="délai moyen d'instruction de 163 jours (5,4 mois), contre "
                  "138 en 2024 ; 1 065 agents, dont 490 officiers de "
                  "protection",
        reserve="Le coût par décision est notre calcul — dépenses de l'année "
                "divisées par les décisions : l'OFPRA ne le publie pas. Il "
                "comprend les frais de structure, et surestime donc un peu ce "
                "que coûte une décision de plus.",
        familles=("asile", "argent")),
    "cnda-activite": Chiffre(
        valeur="≈ 1 330 €", exact="environ 1 330 € par décision : 70,7 M€ de "
                                  "dépenses pour 53 086 décisions en 2025",
        mesure="Coût d'une décision de la Cour nationale du droit d'asile, et "
               "son délai de jugement",
        source="CNDA, rapport d'activité 2025 ; projet annuel de performances "
               "2026, programme « Conseil d'État et autres juridictions "
               "administratives »",
        url=("https://www.cnda.fr/Media/mediatheque-cnda/documents/"
             "rapports-d-activite/rapport-d-activite-2025"),
        annee="2025", publie="mars 2026",
        evolution="60 065 recours reçus ; délai moyen constaté de 5 mois et "
                  "15 jours, contre 5 mois et 9 jours en 2024",
        reserve="Coût calculé par nous, hors aide juridictionnelle (22,3 M€ "
                "en 2024), versée pour chaque recours quel que soit le délai. "
                "La Cour reçoit plus de recours qu'elle ne rend de décisions : "
                "son stock grossit.",
        familles=("asile", "argent")),
    "hebergement-asile": Chiffre(
        valeur="111 855 places", exact="111 855 places programmées pour 2026, "
                                       "dont 61 963 en CADA à 21,91 € par jour",
        mesure="Places d'hébergement pour demandeurs d'asile et réfugiés, et "
               "leur coût journalier",
        source=_PAP, url=_PAP_URL, annee="2026", publie="octobre 2025",
        evolution="946,6 M€ de crédits de paiement prévus pour l'hébergement ; "
                  "113 258 places en 2025",
        reserve="Des places programmées, pas des personnes logées. Le "
                "dispositif ne loge pas tous les demandeurs : une procédure "
                "plus courte libère des places, qui ne deviennent une économie "
                "que si elles ferment.",
        familles=("asile", "argent")),
    "ada-beneficiaires": Chiffre(
        valeur="74 200", exact="74 200 prévus pour 2026",
        mesure="Bénéficiaires prévus de l'allocation pour demandeur d'asile",
        source="Sénat, rapport sur le PLF 2026, mission « Immigration, asile "
               "et intégration »",
        url="https://www.senat.fr/rap/l25-139-315/l25-139-3152.html",
        annee="2026", publie="novembre 2025",
        evolution="16 000 de moins qu'en 2025",
        reserve="Une prévision budgétaire, pas un constat. L'allocation est "
                "de 204 € par mois pour une personne seule, non revalorisée "
                "depuis 2018.",
        familles=("asile", "argent")),

    # --------------------------------------------------------------- eloignement
    "oqtf-prononcees": Chiffre(
        valeur="≈ 140 000", exact="environ 140 000 en 2024",
        mesure="Obligations de quitter le territoire français prononcées en "
               "un an",
        source="Ministère de l'Intérieur, DGEF ; rapports parlementaires",
        url=_DGEF_URL, annee="2024", publie="2025",
        reserve="Une même personne peut recevoir plusieurs OQTF successives : "
                "le chiffre compte des décisions, pas des individus.",
        familles=("eloignement",)),
    "oqtf-executees": Chiffre(
        valeur="≈ 11 %", exact="11,4 % en 2024, environ 10,6 % en 2025",
        mesure="Part des obligations de quitter le territoire suivies d'un "
               "départ constaté",
        source="Ministère de l'Intérieur ; " + _CDC,
        url=_CDC_URL, annee="2024-2025", publie="2025-2026",
        evolution="17 % en 2013, 8,5 % en 2023, 11,4 % en 2024",
        reserve="Ratio boiteux, et il faut le dire avant qu'on ne le dise "
                "contre nous : le numérateur et le dénominateur ne portent "
                "pas sur les mêmes personnes — une OQTF de décembre ne peut "
                "pas être exécutée dans l'année —, les départs spontanés ne "
                "sont pas tous constatés, et des OQTF que personne ne peut "
                "exécuter restent au dénominateur. Il ne mesure pas une "
                "volonté politique ; il mesure l'écart entre ce qu'on écrit "
                "et ce qu'on peut faire.",
        familles=("eloignement",)),
    "eloignements": Chiffre(
        valeur="24 985", exact="24 985, dont 15 569 forcés",
        mesure="Éloignements réalisés en un an",
        source=_DGEF, url=_DGEF_URL, annee="2025", publie="janvier 2026",
        evolution="+ 15,7 % sur un an ; + 21 % pour les seuls éloignements "
                  "forcés",
        reserve="En hausse nette, et le site doit le dire : l'argument « rien "
                "ne bouge » n'est plus exact. Ce qui reste vrai est l'écart "
                "entre les décisions prononcées et les départs réalisés.",
        familles=("eloignement",)),
    "cout-eloignement": Chiffre(
        valeur="4 414 €", exact="4 414 € par éloignement forcé effectif",
        mesure="Coût direct moyen d'un éloignement forcé",
        source=_CDC, url=_CDC_URL, annee="2022", publie="janvier 2024",
        evolution="50,3 M€ dépensés pour 11 409 éloignements forcés en 2022",
        reserve="Coût direct seul : hors rétention — la Cour chiffre une "
                "journée à 602 €, soit environ 16 200 € pour les vingt-sept "
                "jours d'un séjour moyen de 2022 — et hors juges. Ce site "
                "écrivait « plus de 4 500 € » : le chiffre de la Cour est "
                "4 414 €. Promettre plus d'éloignements, c'est promettre une "
                "dépense, et le chiffrage l'inscrit.",
        familles=("eloignement", "argent")),
    "retention": Chiffre(
        valeur="34,5 jours", exact="34,5 jours de rétention en moyenne en "
                                   "métropole en 2024",
        mesure="Durée moyenne d'un placement en rétention, et son issue",
        source="Sénat, rapport d'information n° 4 (2025-2026), données du "
               "ministère de l'Intérieur ; Cour des comptes pour le coût "
               "journalier",
        url="https://www.senat.fr/rap/r25-004/r25-004_mono.html",
        annee="2024", publie="octobre 2025",
        evolution="16 222 personnes placées en métropole, dont 38,8 % "
                  "éloignées ; 602 € par jour de rétention (2022)",
        reserve="Un placement sur trois environ aboutit à un départ en "
                "métropole : un éloignement de plus coûte donc davantage qu'un "
                "séjour en rétention. Le coût journalier exclut les juges et "
                "les escortes.",
        familles=("eloignement", "argent")),

    # ------------------------------------------------------------ administration
    "contentieux-ta": Chiffre(
        valeur="46 %", exact="154 391 affaires en 2025, soit 46,1 % des "
                             "affaires nouvelles",
        mesure="Contentieux des étrangers devant les tribunaux "
               "administratifs : affaires nouvelles, et leur part du total",
        source=_CE_2026, url=_CE_2026_URL, annee="2025", publie="2026",
        evolution="+ 28 % en un an, + 54 % depuis 2021 ; 43 % des entrées en "
                  "2024 ; 55 % des affaires nouvelles en appel",
        reserve="Cette masse est faite pour l'essentiel de recours contre des "
                "refus de séjour et des OQTF, qui sont des contentieux AU "
                "FOND. Seule une partie tient à la procédure — rendez-vous "
                "impossibles, décisions implicites, retards de "
                "renouvellement —, et c'est cette partie-là, et non les 50 %, "
                "que la réforme supprimerait. La hausse de 2025 est portée, "
                "selon le Conseil d'État, par les procédures d'éloignement.",
        familles=("administration",)),
    "agents-etrangers": Chiffre(
        valeur="4 173", exact="4 172,73 équivalents temps plein en 2024, pour "
                              "237,1 M€ de masse salariale",
        mesure="Agents des services des étrangers des préfectures",
        source=_EVALUATIONS, url=_EVALUATIONS_URL, annee="2024",
        publie="octobre 2025",
        evolution="2 497 en 2011 ; masse salariale passée de 110,4 à "
                  "237,1 M€",
        reserve="Des équivalents temps plein, pas des personnes : 39 % des "
                "effectifs sont des contractuels (Sénat, 2025), souvent en "
                "contrats courts. La masse salariale ne comprend ni les locaux "
                "ni l'informatique.",
        familles=("administration", "argent")),
    "cout-premier-titre": Chiffre(
        valeur="547 €", exact="547 € par titre délivré pour la première fois, "
                              "en 2024",
        mesure="Coût complet de traitement d'une première délivrance de titre "
               "de séjour, évalué par l'État",
        source=_EVALUATIONS + " ; Sénat, rapport général n° 139 (2025-2026)",
        url=_EVALUATIONS_URL, annee="2024", publie="octobre 2025",
        evolution="395 € en 2011",
        reserve="Évaluation du ministère — masse salariale, informatique, "
                "soutien aux usagers — dont la méthode n'est pas publiée. Elle "
                "a servi à justifier la hausse des taxes de 2026. Le coût d'un "
                "renouvellement n'est pas publié.",
        familles=("administration", "argent")),
    "ta-affaires": Chiffre(
        valeur="280 000", exact="280 000 affaires nouvelles en 2024",
        mesure="Affaires enregistrées en un an par les tribunaux administratifs, "
               "tous contentieux confondus",
        source=_CE, url=_CE_URL, annee="2024", publie="2025",
        evolution="délai prévisible moyen de jugement : 11 mois et 7 jours, "
                  "en hausse de 20 jours",
        reserve="",
        familles=("administration",)),

    # ------------------------------------------------------------------- argent
    "mission-budget": Chiffre(
        valeur="2,13 Md€", exact="2,13 milliards d'euros de crédits de "
                                 "paiement (2 130 584 454 €)",
        mesure="Crédits de la mission « Immigration, asile et intégration »",
        source="Loi n° 2026-103 du 19 février 2026 de finances pour 2026, "
               "état B",
        url=("https://www.assemblee-nationale.fr/dyn/17/textes/"
             "l17t0227_texte-adopte-seance.pdf"),
        annee="2026", publie="février 2026",
        evolution="2,16 Md€ dans le projet de loi ; 2,08 Md€ votés pour 2025",
        reserve="Ce n'est pas « le coût de l'immigration » : la mission ne "
                "porte ni l'école, ni la santé, ni les prestations sociales, "
                "et ne comptabilise aucune recette. Ce site citait 2,16 Md€ : "
                "c'était le chiffre du projet de loi, pas celui de la loi "
                "votée.",
        familles=("argent",)),
    "ada-credits": Chiffre(
        valeur="222 M€", exact="222,2 millions d'euros pour les seuls "
                               "demandeurs d'asile ; 299,1 M€ avec "
                               "l'allocation des bénéficiaires de la "
                               "protection temporaire et les frais de gestion",
        mesure="Crédits de l'allocation pour demandeur d'asile",
        source=_PAP, url=_PAP_URL, annee="2026", publie="octobre 2025",
        evolution="− 10 % par rapport à 2025 ; 209 € par mois en moyenne, pour "
                  "74 198 allocataires",
        reserve="Une prévision, pas une dépense constatée. Ce site citait "
                "299 M€ : ce total comprend 71,9 M€ versés aux Ukrainiens sous "
                "protection temporaire, qui ont le droit de travailler et "
                "n'illustrent donc pas le coût d'une attente sans travail. "
                "C'est la dépense qu'un asile jugé vite réduit mécaniquement.",
        familles=("argent", "asile")),
    "taxes-titres": Chiffre(
        valeur="≈ 200 M€", exact="de l'ordre de 200 millions d'euros par an "
                                 "en 2019 et en 2022 ; environ 217 M€ en 2024",
        mesure="Produit annuel des taxes et droits de timbre sur les titres "
               "de séjour",
        source="Sénat, rapport général n° 139 (2025-2026), tome II, "
               "article 30 — données du ministère de l'Intérieur",
        url="https://www.senat.fr/rap/l25-139-21/l25-139-21_mono.html",
        annee="2019-2024", publie="novembre 2025",
        evolution="stable de 2019 à 2022 quand les titres délivrés "
                  "progressaient de 8,5 % ; tarifs relevés le 1er mai 2026",
        reserve="Recette du budget général, sans affectation depuis 2017. En "
                "2017, derniers chiffres ventilés (Assemblée nationale, "
                "rapport n° 2041), les renouvellements en portaient 72,5 % : "
                "c'est la recette que la gratuité des renouvellements fait "
                "disparaître.",
        familles=("argent", "administration")),
    "tarifs-titres": Chiffre(
        valeur="250 €", exact="250 € par renouvellement, 350 € pour une "
                              "première délivrance, depuis le 1er mai 2026",
        mesure="Taxe et droit de timbre acquittés sur un titre de séjour, au "
               "tarif plein",
        source="Loi n° 2026-103 du 19 février 2026 de finances pour 2026, "
               "art. 128 ; service-public.fr",
        url="https://www.service-public.gouv.fr/particuliers/actualites/A18881",
        annee="2026", publie="avril 2026",
        evolution="225 € avant le 1er mai 2026, pour une première délivrance "
                  "comme pour un renouvellement",
        reserve="Tarif réduit pour les étudiants (150 € et 100 €) ; "
                "exemptions pour les personnes protégées à la première "
                "délivrance, pour les retraités et les victimes de violences "
                "ou de traite. Une régularisation paie en outre un droit de "
                "visa de 300 € : 650 € en tout.",
        familles=("argent",)),
    "prelevements-smic": Chiffre(
        valeur="≈ 5 800 €", exact="470 € par mois en 2025, 498 € depuis "
                                  "juin 2026",
        mesure="Prélèvements sociaux sur un temps plein au SMIC — coût pour "
               "l'employeur moins salaire net, allègements déduits",
        source="Groupe d'experts sur le SMIC, rapport 2025 ; simulateur de "
               "l'Urssaf, barèmes de juillet 2026",
        url=("https://www.strategie-plan.gouv.fr/files/files/Publications/"
             "2025/2025-12-12%20-%20Rapport%20SMIC/"
             "SMIC-RAPPORT-2025-11decembre13h30-complet-2.pdf"),
        annee="2025-2026", publie="décembre 2025",
        evolution="SMIC à 12,31 € brut de l'heure depuis le 1er juin 2026",
        reserve="Dont environ 211 € par mois de cotisations de retraite, qui "
                "ouvrent des droits futurs : une recette aujourd'hui, une "
                "pension demain. Aucun impôt sur le revenu pour une personne "
                "seule à ce niveau de salaire. Le chiffre de 2026 vient d'une "
                "simulation, pas d'une publication.",
        familles=("argent",)),
    "cir-formation": Chiffre(
        valeur="85,8 M€", exact="85,82 M€ de formation linguistique en 2023, "
                                "pour environ 128 000 contrats d'intégration "
                                "républicaine",
        mesure="Formation linguistique des signataires du contrat "
               "d'intégration républicaine",
        source="Sénat, rapport d'information n° 772 (2023-2024)",
        url="https://www.senat.fr/rap/r23-772/r23-772_mono.html",
        annee="2023", publie="septembre 2024",
        evolution="28,7 M€ en 2016 ; une formation prescrite à 45,8 % des "
                  "signataires",
        reserve="7,40 € de l'heure, de 100 à 600 heures selon le niveau : de "
                "550 à 4 400 € par stagiaire. Le Sénat relève que 68 % "
                "seulement atteignaient le niveau A1 en 2023 : plus de moyens "
                "n'a pas donné plus de résultats.",
        familles=("argent",)),
    "irreguliere-cout": Chiffre(
        valeur="1,8 Md€", exact="environ 1,8 milliard d'euros par an",
        mesure="Coût direct de la politique de lutte contre l'immigration "
               "irrégulière",
        source=_CDC, url=_CDC_URL, annee="2023", publie="janvier 2024",
        evolution="près de 16 000 agents en équivalents temps plein",
        reserve="Coût direct, hors contentieux et hors coût d'opportunité du "
                "travail interdit. La Cour juge la politique « inefficace » "
                "au regard de ses propres objectifs.",
        familles=("argent", "eloignement")),
    "ame": Chiffre(
        valeur="≈ 480 000", exact="environ 480 000 bénéficiaires ; 1,386 Md€ "
                                  "de dépense en 2024",
        mesure="Bénéficiaires et coût de l'aide médicale de l'État",
        source="Commission des comptes de la sécurité sociale ; Sénat, "
               "rapport d'information sur l'AME",
        url="https://www.senat.fr/rap/r24-841/r24-841-syn.pdf",
        annee="2024-2025", publie="2025",
        evolution="+ 15,5 % de dépense en 2024 ; budget gelé à 1,2 Md€ en 2025",
        reserve="Environ 0,4 % des dépenses d'assurance maladie. C'est la "
                "dépense que la régularisation du travail réduit le plus "
                "directement : un travailleur déclaré relève de l'assurance "
                "maladie de droit commun, qu'il finance.",
        familles=("argent",)),
    "solde-budgetaire": Chiffre(
        valeur="≈ 0", exact="quelques dixièmes de point de PIB, positif ou "
                            "négatif selon la méthode",
        mesure="Solde budgétaire de l'immigration — impôts et cotisations "
               "versés moins prestations et biens publics reçus",
        source="OCDE, Perspectives des migrations internationales ; CEPII "
               "(X. Chojnicki, L. Ragot)",
        url="https://www.oecd.org/fr/migrations/",
        annee="travaux récurrents", publie="2021-2025",
        reserve="Très sensible aux conventions retenues — âge des arrivants, "
                "imputation des biens publics, horizon. Aucun chiffre unique "
                "ne fait consensus, et celui qui en avance un sans dire sa "
                "méthode se trompe ou trompe.",
        familles=("argent",)),
}


def chiffre(cle: str) -> Chiffre:
    """Le chiffre d'une clé, ou une erreur bruyante à la construction.

    Une clé fautive arrête ``scripts/construire.py`` : mieux vaut une page qui
    ne se construit pas qu'une page qui affiche ``{titres_economique}``.
    """
    if cle not in CHIFFRES:
        raise KeyError(
            f"chiffre inconnu : {cle!r}. Les clés connues sont : "
            + ", ".join(sorted(CHIFFRES)))
    return CHIFFRES[cle]


def par_famille() -> list[tuple[str, str, list[tuple[str, Chiffre]]]]:
    """Les chiffres groupés pour la page « Tous les chiffres »."""
    groupes = []
    for cle_famille, titre in FAMILLES:
        entrees = [(c, v) for c, v in CHIFFRES.items()
                   if cle_famille in v.familles]
        groupes.append((cle_famille, titre, entrees))
    return groupes
