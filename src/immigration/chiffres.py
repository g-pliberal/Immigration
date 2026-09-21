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
_CDC = ("Cour des comptes, « La politique de lutte contre l'immigration "
        "irrégulière », rapport public thématique")
_CDC_URL = ("https://www.ccomptes.fr/sites/default/files/2024-01/"
            "20240104-communique-Politique-lutte-contre-immigration-irreguliere.pdf")

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
        valeur="> 4 500 €", exact="plus de 4 500 € par éloignement forcé",
        mesure="Coût direct moyen d'un éloignement forcé",
        source=_CDC, url=_CDC_URL, annee="2022", publie="janvier 2024",
        evolution="50 M€ dépensés pour 11 409 éloignements forcés en 2022",
        reserve="Coût direct seul : hors rétention, que la Cour chiffre à "
                "environ 16 000 € par personne pour un séjour moyen de "
                "vingt-sept jours. Promettre plus d'éloignements, c'est donc "
                "promettre une dépense, et notre chiffrage doit l'inscrire.",
        familles=("eloignement", "argent")),

    # ------------------------------------------------------------ administration
    "contentieux-ta": Chiffre(
        valeur="≈ 50 %", exact="près de la moitié des requêtes nouvelles",
        mesure="Part du contentieux des étrangers dans les affaires nouvelles "
               "des tribunaux administratifs",
        source=_CE, url=_CE_URL, annee="2024", publie="2025",
        evolution="+ 9 % en un an ; environ 50 % également en appel",
        reserve="Cette masse est faite pour l'essentiel de recours contre des "
                "refus de séjour et des OQTF, qui sont des contentieux AU "
                "FOND. Seule une partie tient à la procédure — rendez-vous "
                "impossibles, décisions implicites, retards de "
                "renouvellement —, et c'est cette partie-là, et non les 50 %, "
                "que la réforme supprimerait.",
        familles=("administration",)),
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
        valeur="2,16 Md€", exact="2,16 milliards d'euros",
        mesure="Crédits de la mission « Immigration, asile et intégration »",
        source="Loi de finances pour 2026",
        url="https://www.senat.fr/rap/l25-139-315/l25-139-3152.html",
        annee="2026", publie="décembre 2025",
        evolution="+ 80 M€ sur un an",
        reserve="Ce n'est pas « le coût de l'immigration » : la mission ne "
                "porte ni l'école, ni la santé, ni les prestations sociales, "
                "et ne comptabilise aucune recette.",
        familles=("argent",)),
    "ada-credits": Chiffre(
        valeur="299 M€", exact="299,1 millions d'euros",
        mesure="Crédits de l'allocation pour demandeur d'asile",
        source="Loi de finances pour 2026",
        url="https://www.senat.fr/rap/l25-139-315/l25-139-3152.html",
        annee="2026", publie="décembre 2025",
        evolution="− 12 % à périmètre constant",
        reserve="C'est la dépense qu'un asile jugé vite réduit "
                "mécaniquement : on paie l'attente de personnes à qui l'on "
                "interdit par ailleurs de travailler.",
        familles=("argent", "asile")),
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
