"""Le chiffrage du programme : les plus et les moins, comparés à aujourd'hui.

Pourquoi un module de calcul, et non un tableau écrit à la main. La première
version du chiffrage était un tableau de phrases — « 0,3 à 0,6 Md€ »,
« modérée », « non chiffrable ». Relu comme l'aurait fait un contradicteur, ce
format laissait passer ce qu'un calcul n'aurait pas laissé passer : un volume
de renouvellements évités deux à trois fois trop grand, la gratuité des
renouvellements — une recette perdue chaque année — jamais comptée, une
attente d'asile de « dix-huit mois » quand l'indicateur officiel en donne dix,
et des économies sur l'asile comptées sans ce que coûtent ensuite les
personnes protégées, ou déboutées, plus tôt.

Ici, chaque montant est CALCULÉ à partir d'hypothèses écrites une seule fois,
chacune avec sa borne basse, sa borne haute et ce qui la justifie. Les totaux
et les soldes ne sont écrits nulle part : ils sont sommés. Une hypothèse
corrigée se corrige dans chaque ligne, chaque total et chaque phrase qui la
cite — et une phrase de la page qui affirmerait un solde que le calcul dément
fait échouer la construction du site (voir ``pages/chiffrage.py``). Les
valeurs publiées qui figurent déjà au registre (``chiffres.py``) y sont LUES,
et non recopiées : les deux ne peuvent pas diverger.

Conventions
-----------
* Les montants sont en millions d'euros par an, en euros de 2026.
* Un montant POSITIF est un « + » pour les finances publiques : une économie ou
  une recette. Un montant NÉGATIF est un « − » : une dépense ou une recette
  perdue. Le point de comparaison est toujours la situation actuelle, à droit
  constant — ni un programme concurrent, ni un monde idéal.
* « Finances publiques » s'entend toutes administrations confondues : État,
  sécurité sociale, collectivités. Un transfert d'un budget à l'autre — l'aide
  médicale de l'État qui devient assurance maladie — n'est ni un plus ni un
  moins, et il est écrit comme tel.
* Deux scénarios, et non un chiffre. Le PRUDENT retient pour chaque hypothèse
  la borne qui dégrade le solde de l'année considérée ; le FAVORABLE, celle qui
  l'améliore. Ce sont des scénarios cohérents — une hypothèse prend la même
  valeur dans toutes les lignes d'un même scénario —, et non des fourchettes
  additionnées ligne à ligne : c'est pourquoi les bornes d'un solde ne sont
  pas la somme des bornes de ses lignes.
* Deux blocs. Le premier (``etat``) compte ce que l'État fait autrement, à
  nombre de personnes inchangé. Le second (``travail``) compte ce que change le
  travail DÉCLARÉ de personnes déjà présentes : régularisées, ou demandeuses
  d'asile autorisées à travailler. Ni l'un ni l'autre ne compte ce que la
  réforme pourrait attirer de nouvelles arrivées — dans un sens comme dans
  l'autre : c'est l'objet de ``SENSIBILITES``, hors solde.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable

from .chiffres import CHIFFRES

# Les années affichées. L'année 5 tient lieu de régime de croisière : le titre
# de quatre ans y a fait un tour complet, et le nombre de personnes
# régularisées PLUS TÔT qu'elles ne l'auraient été sous le droit actuel cesse à
# peu près de croître (voir ``_regularises``).
ANNEES = (1, 2, 3, 5)

Valeur = Callable[[str], float]


def _lu(cle: str, echelle: float = 1.0) -> float:
    """Le premier nombre de la valeur publiée d'une fiche du registre.

    « 955 080 » donne 955080, « 222,2 millions d'euros » donne 222.2, et
    « 52 % », lu avec ``echelle=0.01``, donne 0.52. Une fiche dont la valeur
    ne commence plus par un nombre fait échouer la construction : c'est voulu.
    """
    texte = CHIFFRES[cle].exact or CHIFFRES[cle].valeur
    trouve = re.search(r"\d{1,3}(?:[ \u00a0\u202f]\d{3})+(?:,\d+)?|\d+(?:,\d+)?",
                       texte)
    if not trouve:
        raise ValueError(f"aucun nombre dans la fiche {cle!r} : {texte!r}")
    nombre = re.sub(r"[ \u00a0\u202f]", "", trouve.group()).replace(",", ".")
    return float(nombre) * echelle


@dataclass(frozen=True)
class Hypothese:
    """Une valeur dont dépend le chiffrage, avec ce qui permet de la contester.

    ``nature`` dit d'où vient la valeur, et donc comment la discuter :

    * ``constat`` — publiée par une source, datée : elle ne se discute pas,
      elle se vérifie. ``chiffre`` renvoie à sa fiche du registre ;
    * ``estimation`` — déduite de chiffres publiés, par un calcul écrit dans
      ``justification`` ;
    * ``hypothese`` — un comportement ou un volume que personne ne mesure : la
      fourchette dit notre ignorance, la justification ce qui la borne ;
    * ``parametre`` — un réglage que la loi fixerait : nous le chiffrons à la
      valeur que nous proposerions.
    """

    libelle: str
    bas: float
    haut: float
    unite: str
    nature: str
    justification: str
    chiffre: str = ""


@dataclass(frozen=True)
class Poste:
    """Une ligne du chiffrage : un plus ou un moins, et d'où il vient.

    ``calcul`` reçoit la valeur des hypothèses dans un scénario et l'année, et
    rend un montant en M€ — positif pour un plus, négatif pour un moins.
    ``formule`` dit le même calcul en français ; ``{cle}`` y est remplacé par
    la valeur de l'hypothèse, pour qu'un lecteur refasse le compte.
    ``quand`` dit le rythme : une dépense de transition ne se lit pas comme
    une dépense durable.
    """

    cle: str
    bloc: str
    engagement: str
    libelle: str
    aujourdhui: str
    avec: str
    formule: str
    calcul: Callable[[Valeur, int], float]
    quand: str


H = Hypothese

# ---------------------------------------------------------------------------
# Les hypothèses. L'ordre est celui des engagements ; les clés sont celles
# qu'utilisent les formules.
# ---------------------------------------------------------------------------

HYPOTHESES: dict[str, Hypothese] = {
    # -------------------------------------------------- le séjour, en préfecture
    "cout-agent": H(
        "Coût annuel d'un agent des services des étrangers", 56_800, 61_400, "€",
        "estimation",
        "La masse salariale des services des étrangers des préfectures, "
        "rapportée à leurs effectifs — 237,1 M€ pour 4 173 équivalents temps "
        "plein en 2024 —, donne 56 800 € ; le coût moyen d'un agent de l'action "
        "budgétaire correspondante, pensions comprises, 61 400 €.",
        chiffre="agents-etrangers"),
    "agents-plateformes": H(
        "Agents des plateformes qui instruisent les autorisations de travail",
        90, 130, "agents", "estimation",
        "90 équivalents temps plein fin 2021 dans les sept plateformes "
        "interrégionales (Sénat, 2022), 130 avant leur création. Aucun chiffre "
        "plus récent n'est publié."),
    "part-plateformes-economisee": H(
        "Part de ce travail que la réforme supprime", 0.4, 0.8, "%", "hypothese",
        "L'autorisation disparaît, mais le contrat et le salaire minimum de la "
        "branche restent vérifiés à la délivrance du titre : une partie du "
        "travail change de guichet au lieu de disparaître."),
    "renfort-prefectures": H(
        "Agents de renfort en préfecture, les deux premières années", 250, 500,
        "agents", "hypothese",
        "Tenir huit semaines, c'est d'abord résorber le stock : les délais "
        "d'instruction ont crû de 25 à 27 % en 2024 à effectifs presque "
        "constants. Un renfort temporaire de 6 à 12 % des 4 173 agents, "
        "le temps que le titre de quatre ans fasse baisser le flux.",
        chiffre="agents-etrangers"),
    "hors-delai-debut": H(
        "Dossiers traités hors délai la première année", 0.08, 0.2, "%",
        "hypothese",
        "Le stock de dossiers en retard ne se résorbe pas en un jour. Le "
        "septième engagement fixe à 5 % la part de titres délivrés par le "
        "silence au-delà de laquelle le délai devient une fiction."),
    "hors-delai-regime": H(
        "Dossiers traités hors délai ensuite", 0.01, 0.03, "%", "hypothese",
        "Sous le seuil d'alerte de 5 % que se fixe le septième engagement."),
    "indemnite-retard": H(
        "Indemnité forfaitaire par dossier traité hors délai", 100, 200, "€",
        "parametre",
        "Le montant que la loi fixerait. Nous proposons un forfait de l'ordre "
        "d'une demi-taxe de renouvellement : assez pour que le retard coûte à "
        "l'administration, pas assez pour qu'on dépose un dossier dans "
        "l'espoir qu'il soit traité en retard."),
    "affaires-etrangers": H(
        "Affaires d'étrangers enregistrées par les tribunaux administratifs",
        _lu("contentieux-ta"), _lu("contentieux-ta"), "affaires", "constat",
        "Contentieux des étrangers devant les tribunaux administratifs, 2025.",
        chiffre="contentieux-ta"),
    "part-affaires-procedure": H(
        "Part de ces affaires qui ne portent que sur la procédure", 0.1, 0.2,
        "%", "hypothese",
        "Aucune statistique nationale ne ventile ce contentieux par objet. Le "
        "Conseil d'État relève qu'une « part non négligeable » n'a pour seul "
        "objet que l'obtention d'un rendez-vous ou le respect d'un délai ; à "
        "Montreuil, un tiers des affaires d'étrangers de 2021 étaient des "
        "référés. Nous retenons 10 à 20 %, faute de mieux."),
    "cout-affaire-procedure": H(
        "Coût pour l'État d'une affaire de procédure", 1_100, 1_600, "€",
        "estimation",
        "L'Assemblée nationale estimait en 2021 à 1 575 € le coût d'un "
        "contentieux d'accès au rendez-vous : 750 € de tribunal, 500 € de "
        "préfecture, 325 € d'aide juridictionnelle. Un tribunal administratif "
        "coûte en moyenne 843 € par affaire jugée, frais de structure exclus."),
    "premiers-titres": H(
        "Premiers titres de séjour par an", _lu("premiers-titres"),
        _lu("premiers-titres"), "titres", "constat",
        "Premiers titres délivrés en 2025.", chiffre="premiers-titres"),
    "renouvellements": H(
        "Renouvellements de titres de séjour par an", _lu("renouvellements"),
        _lu("renouvellements"), "titres", "constat",
        "Titres renouvelés en 2025.", chiffre="renouvellements"),
    "renouvellements-travail-etudes": H(
        "Renouvellements pour motif économique ou d'études",
        _lu("renouvellements-travail-etudes"),
        _lu("renouvellements-travail-etudes"), "titres", "constat",
        "194 240 renouvellements pour motif économique et 144 230 pour études "
        "en 2024 : les seuls que l'engagement 3 concerne.",
        chiffre="renouvellements-travail-etudes"),
    "part-renouvellements-evites": H(
        "Part de ces renouvellements que le titre de quatre ans supprime",
        0.5, 0.75, "%", "hypothese",
        "Un titre d'un an renouvelé chaque année, remplacé par un titre de "
        "quatre ans, supprime trois renouvellements sur quatre. Une partie de "
        "ces titres est déjà pluriannuelle, et un étudiant qui devient salarié "
        "dépose encore une demande : la moitié à trois quarts."),
    "cout-renouvellement": H(
        "Coût d'instruction d'un renouvellement", 80, 160, "€", "estimation",
        "Répartie sur les quelque 1,37 million de titres délivrés ou "
        "renouvelés, la masse salariale des services des étrangers donne "
        "environ 170 € par titre ; un agent traite environ 620 demandes par "
        "an, soit une centaine d'euros chacune. Un renouvellement demande "
        "moins de vérifications qu'une première délivrance, que l'État évalue "
        "à 547 € tout compris.",
        chiffre="cout-premier-titre"),
    "taxe-renouvellement": H(
        "Taxe moyenne effectivement perçue sur un renouvellement", 160, 200,
        "€", "estimation",
        "Depuis le 1er mai 2026, 250 € (100 € au tarif réduit des étudiants), "
        "avec des exemptions. En 2017, derniers chiffres ventilés, les "
        "renouvellements portaient 72,5 % du produit des taxes : appliquée aux "
        "quelque 217 M€ de 2024, cette part donne environ 175 € par "
        "renouvellement au tarif de l'époque, près de 200 € à celui de 2026.",
        chiffre="taxes-titres"),
    "taxe-renouvellement-travail-etudes": H(
        "Taxe moyenne sur un renouvellement de travail ou d'études", 150, 190,
        "€", "estimation",
        "250 € pour un renouvellement de travail, 100 € pour un étudiant : "
        "186 € en moyenne pondérée par les volumes de 2024, un peu moins avec "
        "les exemptions.",
        chiffre="tarifs-titres"),
    "premiers-titres-tarif-plein": H(
        "Premiers titres payant le tarif plein", 130_000, 170_000, "titres",
        "estimation",
        "Sur 384 230 premiers titres, les étudiants paient le tarif réduit "
        "(≈ 118 000) et les personnes protégées sont exemptées (≈ 92 600) ; il "
        "reste environ 170 000 titres, dont certains exemptés à d'autres "
        "titres.",
        chiffre="premiers-titres"),
    "variation-taxe-premiere": H(
        "Variation de la taxe de première délivrance, alignée sur le coût",
        -100, 200, "€", "parametre",
        "L'État évalue à 547 € le coût de traitement d'une première "
        "délivrance, au-dessus du tarif plein de 350 € : l'aligner la "
        "relèverait de 200 €. Mais le programme fait baisser ce coût — plus "
        "d'autorisation de travail, dépôt en ligne, moins de passages au "
        "guichet —, et la taxe baisserait avec lui.",
        chiffre="cout-premier-titre"),
    "agents-accueil": H(
        "Agents d'accueil pour un rendez-vous sous quinze jours et un guichet "
        "garanti", 150, 400, "agents", "hypothese",
        "Une solution de substitution au dépôt en ligne est obligatoire depuis "
        "2023, et peu appliquée selon la Défenseure des droits. La garantir, "
        "avec un rendez-vous sous quinze jours : 4 à 10 % des effectifs des "
        "services des étrangers."),
    # --------------------------------------------------------------- l'asile
    "demandes-asile": H(
        "Demandes d'asile enregistrées par an", _lu("asile-demandes"),
        _lu("asile-demandes"), "demandes", "constat",
        "Demandes enregistrées en 2025, mineurs compris.",
        chiffre="asile-demandes"),
    "taux-protection": H(
        "Part des demandes qui aboutissent à une protection",
        _lu("asile-protection", 0.01), _lu("asile-protection", 0.01), "%",
        "constat", "Taux de protection 2025, recours compris.",
        chiffre="asile-protection"),
    "delai-asile-actuel": H(
        "Durée moyenne d'une demande d'asile aujourd'hui", 9.5, 10.5, "mois",
        "estimation",
        "De la présentation de la demande à la décision définitive : 299 jours "
        "en 2024 selon l'indicateur officiel, soit près de dix mois ; le délai "
        "de l'OFPRA a encore augmenté en 2025 (163 jours contre 138).",
        chiffre="delai-asile"),
    "delai-asile-programme": H(
        "Durée moyenne d'une demande d'asile avec le programme", 4, 5, "mois",
        "parametre",
        "Six mois au plus, recours compris : deux mois à l'OFPRA — la cible que "
        "le Gouvernement s'est lui-même fixée —, un mois de délai de recours, "
        "trois mois à la CNDA. Ceux qui ne font pas de recours sortent en "
        "deux ou trois mois : quatre à cinq mois en moyenne."),
    "ada-demandeurs": H(
        "Allocation pour demandeur d'asile, par an", _lu("ada-credits"),
        _lu("ada-credits"), "M€", "constat",
        "Crédits 2026 de l'allocation des seuls demandeurs d'asile, hors "
        "protection temporaire et frais de gestion.", chiffre="ada-credits"),
    "part-ada-duree": H(
        "Part de l'allocation qui dépend de la durée de la procédure", 0.6, 0.8,
        "%", "hypothese",
        "L'allocation est versée jusqu'au mois qui suit la décision définitive. "
        "Une partie n'en dépend pas : les procédures Dublin, dont le calendrier "
        "est européen, et les procédures déjà accélérées."),
    "hebergement-demandeurs": H(
        "Hébergement des demandeurs d'asile, par an", 780, 780, "M€",
        "estimation",
        "Places programmées pour 2026 multipliées par leur coût journalier : "
        "61 963 places de CADA à 21,91 €, 27 711 d'HUDA à 19,21 €, 5 080 de "
        "CAES à 27,36 €, 5 212 de PRAHDA — hors centres pour réfugiés.",
        chiffre="hebergement-asile"),
    "cout-place-mois": H(
        "Coût mensuel d'une place d'hébergement pour demandeur d'asile", 650,
        650, "€", "estimation",
        "Les 780 M€ ci-dessus rapportés aux quelque 100 000 places qu'ils "
        "financent, et à douze mois.", chiffre="hebergement-asile"),
    "part-hebergee": H(
        "Part des demandeurs d'asile hébergés par le dispositif national",
        0.5, 0.7, "%", "hypothese",
        "Le dispositif ne loge pas tous les demandeurs qui y ont droit ; les "
        "autres perçoivent un complément d'allocation, ou relèvent de "
        "l'hébergement d'urgence de droit commun."),
    "part-hebergement-economisee": H(
        "Part des places libérées qui devient une économie", 0.25, 0.6, "%",
        "hypothese",
        "Une procédure plus courte libère des places. Une partie servira "
        "d'abord à loger les demandeurs qui ne le sont pas aujourd'hui ; le "
        "reste se ferme, ou ne s'ouvre pas."),
    "decisions-ofpra-rattrapage": H(
        "Décisions supplémentaires de l'OFPRA pour résorber son stock",
        15_000, 30_000, "décisions par an", "estimation",
        "Ramener le délai de l'OFPRA de 5,4 à 2 mois, c'est ramener son stock "
        "d'environ 70 000 dossiers à environ 26 000 : 44 000 décisions de plus, "
        "étalées sur deux ou trois ans.", chiffre="ofpra-activite"),
    "cout-decision-ofpra": H(
        "Coût d'une décision de l'OFPRA", 700, 700, "€", "estimation",
        "109,5 M€ dépensés en 2025 pour 156 509 décisions.",
        chiffre="ofpra-activite"),
    "decisions-cnda-rattrapage": H(
        "Décisions supplémentaires de la CNDA pour résorber son stock",
        8_000, 15_000, "décisions par an", "estimation",
        "Avec 60 065 recours par an et un délai prévisible de près de sept "
        "mois, le stock de la Cour dépasse 30 000 affaires ; le ramener à trois "
        "mois de recours en demande près de 20 000 de moins.",
        chiffre="cnda-activite"),
    "decisions-cnda-permanentes": H(
        "Décisions supplémentaires de la CNDA, chaque année", 5_000, 8_000,
        "décisions par an", "estimation",
        "En 2025, la Cour a reçu 60 065 recours et rendu 53 086 décisions : "
        "l'écart, 7 000 par an, fait grossir son stock. Le combler est la "
        "condition d'un délai tenu.", chiffre="cnda-activite"),
    "part-recours": H(
        "Part des décisions de l'OFPRA portées devant la CNDA", 0.38, 0.38, "%",
        "estimation", "60 065 recours en 2025 pour 156 509 décisions de l'OFPRA.",
        chiffre="cnda-activite"),
    "cout-decision-cnda": H(
        "Coût d'une décision de la CNDA", 1_330, 1_600, "€", "estimation",
        "70,7 M€ de dépenses de personnel et de fonctionnement en 2025 pour "
        "53 086 décisions : 1 330 € ; davantage si le renfort passe par des "
        "magistrats permanents plutôt que vacataires.", chiffre="cnda-activite"),
    "cout-droit-commun": H(
        "Coût d'une année de droit commun pour une personne protégée",
        2_000, 5_000, "€", "hypothese",
        "Une personne protégée a droit sans délai au RSA — 651,69 € par mois "
        "pour une personne seule depuis avril 2026, à partir de 25 ans ou avec "
        "un enfant — et aux aides au logement. Une partie travaille, une "
        "partie a moins de 25 ans, et les enfants comptent dans le foyer de "
        "leurs parents : 2 000 à 5 000 € par personne et par an."),
    "part-non-compensee": H(
        "Part de ce coût que ne compense pas un emploi trouvé plus tôt",
        0.25, 1.0, "%", "hypothese",
        "Protégée plus tôt, une personne touche plus tôt le RSA ; mais si elle "
        "trouve aussi du travail plus tôt — le droit de travailler dès le "
        "dépôt y aide —, elle en sort plus tôt, et le coût s'annule. Il "
        "demeure si son insertion suit le calendrier de son arrivée plutôt "
        "que celui de sa protection. En Allemagne, sept mois d'interdiction "
        "de travailler de plus laissaient les réfugiés vingt points moins "
        "souvent en emploi cinq ans après (Marbach, Hainmueller et "
        "Hangartner, 2018)."),
    "recours-ame": H(
        "Part des déboutés qui recourent à l'aide médicale de l'État", 0.3, 0.6,
        "%", "hypothese",
        "Environ la moitié des personnes qui y ont droit la demandent, selon "
        "l'enquête « Premiers pas » (IRDES, 2019) comme selon le Sénat (2025)."),
    "cout-ame": H(
        "Coût annuel de l'aide médicale de l'État par bénéficiaire",
        2_890, 2_890, "€", "estimation",
        "1,386 Md€ de dépense en 2024 pour environ 480 000 bénéficiaires.",
        chiffre="ame"),
    "eloignements-supplementaires": H(
        "Éloignements forcés supplémentaires par an", 4_000, 4_000,
        "éloignements", "parametre",
        "L'« exécution effective » des rejets que promet l'engagement 4, "
        "chiffrée : un quart d'éloignements forcés de plus que les 15 569 de "
        "2025. C'est à peu près ce que les places de rétention existantes "
        "permettent ; au-delà, il faut en construire, et obtenir des "
        "laissez-passer qu'aucune loi ne fournit. Chaque millier de plus ou "
        "de moins est chiffré à part.",
        chiffre="eloignements"),
    "cout-eloignement": H(
        "Coût direct d'un éloignement forcé", _lu("cout-eloignement"),
        _lu("cout-eloignement"), "€", "constat",
        "Escortes, billets, frais de procédure — hors rétention et hors juges.",
        chiffre="cout-eloignement"),
    "cout-retention": H(
        "Coût d'un placement en rétention", 20_800, 20_800, "€", "estimation",
        "602 € par jour (Cour des comptes, 2022) pendant 34,5 jours, la durée "
        "moyenne en métropole en 2024. Hors juges et escortes.",
        chiffre="retention"),
    "placements-par-eloignement": H(
        "Placements en rétention par éloignement supplémentaire", 0.8, 1.6,
        "placements", "estimation",
        "En 2024, 16 222 placements en métropole pour 12 856 éloignements "
        "forcés : 1,26 par éloignement, parce que 38,8 % seulement des "
        "placements aboutissent à un départ. Moins si l'effort vise des "
        "personnes déjà détenues ou assignées, plus s'il repose sur la "
        "rétention.", chiffre="retention"),
    # ------------------------------------------------- comptes, contrôle
    "cout-suivi": H(
        "Rapport annuel, indicateurs publiés, suivi de cohortes", 1, 3, "M€",
        "hypothese",
        "Une équipe statistique et une enquête de suivi des personnes entrées "
        "sous le nouveau régime, sur le modèle des enquêtes existantes."),
    "agents-controle": H(
        "Agents de contrôle supplémentaires contre le travail dissimulé",
        100, 250, "agents", "parametre",
        "Le renfort que nous proposons : il n'a de sens que si l'emploi "
        "déclaré devient simple, et c'est ce que fait le programme."),
    "cout-controleur": H(
        "Coût annuel d'un agent de contrôle", 60_000, 80_000, "€", "hypothese",
        "Rémunération et charges d'un agent de catégorie A ou B, pensions "
        "comprises."),
    # ------------------------------------------------------ le travail déclaré
    "regularisations-debut": H(
        "Régularisations supplémentaires par an, les trois premières années",
        50_000, 50_000, "personnes", "hypothese",
        "Personne ne sait combien de personnes rempliraient les conditions — "
        "douze mois de présence, six mois de travail, identité établie, casier "
        "vérifié, employeur identifié —, puisque personne ne sait combien "
        "vivent sans titre. Deux repères : la France a régularisé 9 690 "
        "personnes par le travail en 2025, sous des critères plus stricts ; "
        "l'Espagne, qui a ramené en 2025 sa condition de présence de trois à "
        "deux ans, en attend 300 000 par an pendant trois ans. Nous retenons "
        "50 000 de plus par an les trois premières années, le temps "
        "d'absorber les personnes déjà présentes : un repère, pas une "
        "prévision — chaque tranche de 10 000 de plus ou de moins est "
        "chiffrée à part.",
        chiffre="aes-travail"),
    "regularisations-regime": H(
        "Régularisations supplémentaires par an, ensuite", 20_000, 20_000,
        "personnes", "hypothese",
        "Une fois absorbées les personnes déjà présentes, ne restent que celles "
        "qui atteignent chaque année douze mois de présence : le double des "
        "régularisations par le travail d'aujourd'hui."),
    "part-non-declares": H(
        "Part des personnes régularisées qui travaillaient sans être "
        "déclarées", 0.45, 0.8, "%", "hypothese",
        "Les régularisations actuelles exigent des bulletins de paie ; celles "
        "que le programme ajoute — preuve par faisceau d'indices, un an de "
        "présence — concernent d'abord des personnes qui travaillent sans être "
        "déclarées. Les autres cotisaient déjà, sous une autre identité : les "
        "régulariser ne rapporte presque rien de plus."),
    "prelevements-smic": H(
        "Prélèvements annuels sur un temps plein au SMIC", 5_640, 5_980, "€",
        "estimation",
        "Coût pour l'employeur moins salaire net, allègements déduits : 470 € "
        "par mois en 2025, 498 € depuis juin 2026 — dont environ 211 € de "
        "cotisations de retraite, qui ouvrent des droits futurs. Pas d'impôt "
        "sur le revenu à ce niveau de salaire.",
        chiffre="prelevements-smic"),
    "quotite": H(
        "Temps de travail moyen, rapporté à un temps plein", 0.7, 0.9, "%",
        "hypothese",
        "Les métiers concernés — bâtiment, restauration, nettoyage, aide à la "
        "personne, logistique — comptent beaucoup de temps partiels."),
    "mois-rappel": H(
        "Mois de cotisations dues pour la période antérieure", 6, 6, "mois",
        "parametre",
        "Les six mois de travail exigés : l'employeur qui les déclare et en "
        "paie les cotisations n'est pas poursuivi (engagement 1)."),
    "part-rappels-payes": H(
        "Part des employeurs qui paient ce rappel", 0.3, 0.7, "%", "hypothese",
        "Tous ne le feront pas : un employeur peut préférer licencier plutôt "
        "que payer six mois de cotisations."),
    "taxes-regularisation": H(
        "Taxes acquittées par une personne régularisée", 650, 650, "€",
        "constat",
        "Droit de visa de régularisation (300 €) et taxe de première délivrance "
        "(350 €), tarifs du 1er mai 2026.", chiffre="tarifs-titres"),
    "cout-dossier-regularisation": H(
        "Coût d'instruction d'une demande de régularisation", 547, 800, "€",
        "estimation",
        "Au moins le coût complet d'une première délivrance, évalué par l'État "
        "à 547 € ; davantage, parce que la preuve du travail par faisceau "
        "d'indices se vérifie pièce à pièce.", chiffre="cout-premier-titre"),
    "part-refus": H(
        "Part des demandes de régularisation refusées", 0.15, 0.35, "%",
        "hypothese",
        "Identité non établie, casier chargé, travail non prouvé : ces dossiers "
        "s'instruisent aussi."),
    "prestations-regularise": H(
        "Prestations versées chaque année à une personne régularisée",
        450, 1_800, "€", "hypothese",
        "Une personne seule au SMIC ne touche pas d'aide au logement — le "
        "barème s'arrête vers 14 900 € de revenus en zone 2, un temps plein en "
        "déclare environ 16 200 — et n'a droit ni au RSA ni à la prime "
        "d'activité avant cinq ans. Les prestations viennent des familles : "
        "15 à 30 % des personnes régularisées, 3 000 à 6 000 € par an "
        "d'allocations familiales et d'aide au logement."),
    "apl-premiere-annee": H(
        "Aide au logement de la première année", 800, 1_600, "€", "estimation",
        "L'aide se calcule sur les revenus déclarés des douze derniers mois — "
        "nuls pour qui travaillait au noir ou sous une autre identité : "
        "jusqu'à 2 700 € la première année pour un locataire seul, puis plus "
        "rien. Pour les 30 à 60 % qui louent en leur nom."),
    "formation-francais": H(
        "Formation civique et linguistique d'un nouveau titulaire", 600, 900,
        "€", "estimation",
        "85,8 M€ de formation linguistique en 2023 pour 128 000 contrats "
        "d'intégration républicaine, soit 670 € par signataire ; davantage "
        "avec l'« accès effectif » aux cours que promet le programme.",
        chiffre="cir-formation"),
    "part-adultes": H(
        "Part des adultes parmi les demandeurs d'asile", 0.75, 0.85, "%",
        "hypothese",
        "Les demandes comptent les mineurs qui accompagnent leurs parents."),
    "emploi-demandeurs": H(
        "Demandeurs d'asile qui travaillent pendant la procédure", 0.04, 0.15,
        "%", "hypothese",
        "Aujourd'hui, le travail n'est possible qu'après six mois et sur "
        "autorisation : 1 814 autorisations accordées d'avril 2021 à avril "
        "2022, environ 2 % des demandeurs adultes. Un droit ouvert dès le "
        "dépôt, sans autorisation, en fera travailler davantage — surtout "
        "parmi ceux qui ont déjà une promesse d'embauche."),
    "prelevements-demandeur": H(
        "Prélèvements annuels sur un demandeur d'asile qui travaille",
        2_000, 4_000, "€", "estimation",
        "Un emploi à mi-temps ou aux deux tiers d'un temps plein au SMIC.",
        chiffre="prelevements-smic"),
    "ada-mensuelle": H(
        "Allocation moyenne d'un demandeur d'asile, par mois", 209, 209, "€",
        "constat", "Montant moyen prévu pour 2026.", chiffre="ada-credits"),
    "part-ada-perdue": H(
        "Part de l'allocation que perd un demandeur qui travaille", 0.6, 1.0,
        "%", "hypothese",
        "Tout revenu d'activité est déduit de l'allocation (art. D. 553-12 du "
        "CESEDA) ; un temps partiel en laisse une partie."),
}

# Un étalement que la loi rend inévitable : votée la première année, elle
# s'applique à la moitié de celle-ci en moyenne. Le reste des rythmes est dit
# poste par poste.


def _loi(annee: int) -> float:
    return 0.5 if annee == 1 else 1.0


def _asile(annee: int) -> float:
    """Le chemin vers l'asile jugé en six mois, tenu deux ans après la loi.

    0 : le délai d'aujourd'hui ; 1 : le délai du programme. La première année
    avance peu — il faut recruter et former avant de juger plus vite.
    """
    return {1: 0.1, 2: 0.5}.get(annee, 1.0)


def _transition(annee: int) -> float:
    """Un renfort de deux ans et demi : plein les deux premières années."""
    return {1: 1.0, 2: 1.0, 3: 0.5}.get(annee, 0.0)


def _rattrapage(annee: int) -> float:
    """La résorption d'un stock : on recrute la première année."""
    return {1: 0.5, 2: 1.0, 3: 0.5}.get(annee, 0.0)


def _titre_quatre_ans(annee: int) -> float:
    """Les renouvellements évités : aucun la première année.

    Un titre délivré au second semestre de l'année 1 ne se renouvelle plus
    au second semestre de l'année 2 : l'effet n'est plein qu'en année 3.
    """
    return {1: 0.0, 2: 0.5}.get(annee, 1.0)


def _contentieux(annee: int) -> float:
    """Le contentieux évité suit les délais tenus, avec retard."""
    return {1: 0.3, 2: 0.7}.get(annee, 1.0)


def _hors_delai(v: Valeur, annee: int) -> float:
    debut, regime = v("hors-delai-debut"), v("hors-delai-regime")
    return {1: debut, 2: (debut + regime) / 2,
            3: regime + (debut - regime) / 4}.get(annee, regime)


def _renouvellements_evites(v: Valeur, annee: int) -> float:
    return (v("renouvellements-travail-etudes")
            * v("part-renouvellements-evites") * _titre_quatre_ans(annee))


def _reduction_asile(v: Valeur) -> float:
    """La part de l'attente que le programme supprime.

    L'allocation court jusqu'au mois qui suit la décision définitive : ce mois
    est ajouté aux deux durées.
    """
    return 1 - (v("delai-asile-programme") + 1) / (v("delai-asile-actuel") + 1)


def _mois_gagnes(v: Valeur, annee: int) -> float:
    return ((v("delai-asile-actuel") - v("delai-asile-programme"))
            * _asile(annee))


def _regularisations(v: Valeur, annee: int) -> float:
    """Régularisations supplémentaires de l'année — par rapport au droit actuel."""
    if annee <= 3:
        return v("regularisations-debut") * _loi(annee)
    return v("regularisations-regime")


def _regularises(v: Valeur, annee: int) -> float:
    """Personnes régularisées plus tôt qu'elles ne l'auraient été, en moyenne
    sur l'année. Une cohorte compte pour moitié l'année où elle entre.

    Sous le droit actuel, une partie de ces personnes aurait fini par être
    régularisée — au bout de trois à cinq ans de présence. Le programme avance
    donc leur régularisation plus qu'il ne la crée, et ce stock cesse à peu
    près de croître une fois ce délai écoulé : c'est pourquoi le chiffrage
    s'arrête à l'année 5 au lieu de prolonger la droite.
    """
    anciennes = sum(_regularisations(v, a) for a in range(1, annee))
    return anciennes + _regularisations(v, annee) / 2


def _prelevements_par_regularise(v: Valeur) -> float:
    return v("part-non-declares") * v("prelevements-smic") * v("quotite")


def _demandeurs_au_travail(v: Valeur, annee: int) -> float:
    """Demandeurs d'asile adultes qui travaillent, en moyenne sur l'année."""
    duree = v("delai-asile-actuel") - _mois_gagnes(v, annee)
    en_attente = v("demandes-asile") * v("part-adultes") * duree / 12
    return en_attente * v("emploi-demandeurs") * _loi(annee)


M = 1e6  # les calculs sont en euros, les montants en millions d'euros

# ---------------------------------------------------------------------------
# Les postes. Chacun dit ce qui se passe aujourd'hui, ce que le programme
# change, et le montant qui en résulte — en plus ou en moins.
# ---------------------------------------------------------------------------

POSTES: list[Poste] = [
    # ============================================ l'État fait autrement : 1
    Poste(
        "autorisations-travail", "etat", "1",
        "Autorisations de travail : l'instruction disparaît",
        "263 125 demandes en 2022, instruites par sept plateformes",
        "Le titre de séjour vaut autorisation ; le contrat reste vérifié",
        "{agents-plateformes} agents × {part-plateformes-economisee} du "
        "travail supprimé × {cout-agent}",
        lambda v, a: (v("agents-plateformes") * v("part-plateformes-economisee")
                      * v("cout-agent") * _loi(a) / M),
        "durable, dès le vote de la loi"),
    # ============================================ 2 : délais opposables
    Poste(
        "renfort-prefectures", "etat", "2",
        "Renfort des préfectures pour tenir huit semaines",
        "Délais d'instruction en hausse de 25 à 27 % en 2024",
        "Huit semaines, quatre pour un renouvellement, opposables",
        "{renfort-prefectures} agents × {cout-agent}, pendant deux ans et demi",
        lambda v, a: -(v("renfort-prefectures") * v("cout-agent")
                       * _transition(a) / M),
        "les deux premières années, la moitié la troisième"),
    Poste(
        "indemnites-retard", "etat", "2",
        "Indemnités pour délai dépassé",
        "Aucune : le silence vaut refus, et la lenteur ne coûte rien à "
        "l'administration",
        "Un forfait par dossier traité hors délai",
        "({renouvellements} renouvellements + {premiers-titres} premiers "
        "titres) × part hors délai — {hors-delai-debut} la première année, "
        "{hors-delai-regime} ensuite — × {indemnite-retard}",
        lambda v, a: -((v("renouvellements") + v("premiers-titres"))
                       * _hors_delai(v, a) * v("indemnite-retard") / M),
        "élevée la première année, puis décroissante par construction"),
    Poste(
        "contentieux-procedure", "etat", "2",
        "Contentieux de procédure évité",
        "Référés pour obtenir un rendez-vous, recours contre des refus nés du "
        "silence, ruptures de droits",
        "Un délai tenu, un rendez-vous garanti : ces recours n'ont plus d'objet",
        "{affaires-etrangers} affaires × {part-affaires-procedure} de "
        "procédure × {cout-affaire-procedure}",
        lambda v, a: (v("affaires-etrangers") * v("part-affaires-procedure")
                      * v("cout-affaire-procedure") * _contentieux(a) / M),
        "croissant les deux premières années"),
    # ============================================ 3 : titre de quatre ans
    Poste(
        "renouvellements-instruction", "etat", "3",
        "Renouvellements évités : l'instruction",
        "Titres de travail et d'études, souvent annuels",
        "Quatre ans dès le premier titre",
        "{renouvellements-travail-etudes} renouvellements × "
        "{part-renouvellements-evites} évités × {cout-renouvellement}",
        lambda v, a: (_renouvellements_evites(v, a) * v("cout-renouvellement")
                      / M),
        "à partir de la deuxième année"),
    Poste(
        "renouvellements-taxes", "etat", "3",
        "Renouvellements évités : la taxe qu'ils rapportaient",
        "Chaque renouvellement paie sa taxe",
        "La moitié à trois quarts de ces renouvellements disparaissent, et "
        "leur taxe avec eux",
        "renouvellements évités × {taxe-renouvellement-travail-etudes}",
        lambda v, a: -(_renouvellements_evites(v, a)
                       * v("taxe-renouvellement-travail-etudes") / M),
        "à partir de la deuxième année"),
    Poste(
        "perte-emploi", "etat", "3",
        "Titre maintenu douze mois après une perte d'emploi",
        "Déjà le cas pour la carte « salarié » : prolongée d'un an, puis de "
        "la durée des droits au chômage (art. L. 421-1 du CESEDA)",
        "Étendu aux contrats courts, qui n'ont pas cette protection",
        "≈ 0 : le droit actuel fait déjà l'essentiel",
        lambda v, a: 0.0,
        "sans effet mesurable"),
    # ============================================ 4 : l'asile
    Poste(
        "renfort-ofpra-cnda", "etat", "4",
        "Renfort de l'OFPRA et de la CNDA",
        "OFPRA en 5,4 mois, CNDA en 5,5 mois ; le stock de la Cour grossit",
        "Six mois au plus, recours compris",
        "({decisions-ofpra-rattrapage} décisions × {cout-decision-ofpra} + "
        "{decisions-cnda-rattrapage} décisions × {cout-decision-cnda}) le "
        "temps de résorber les stocks, puis {decisions-cnda-permanentes} "
        "décisions de la CNDA × {cout-decision-cnda} chaque année",
        lambda v, a: -(
            (v("decisions-ofpra-rattrapage") * v("cout-decision-ofpra")
             + v("decisions-cnda-rattrapage") * v("cout-decision-cnda"))
            * _rattrapage(a)
            + v("decisions-cnda-permanentes") * v("cout-decision-cnda")
            * _loi(a)) / M,
        "fort les deux premières années, puis durable pour la CNDA"),
    Poste(
        "ada-attente", "etat", "4",
        "Allocation des demandeurs d'asile : une attente plus courte",
        "Versée pendant près de dix mois en moyenne",
        "Versée quatre à cinq mois",
        "{ada-demandeurs} × {part-ada-duree} × part de l'attente supprimée "
        "({delai-asile-actuel} → {delai-asile-programme})",
        lambda v, a: (v("ada-demandeurs") * v("part-ada-duree")
                      * _reduction_asile(v) * _asile(a)),
        "croissant jusqu'à la troisième année"),
    Poste(
        "hebergement-attente", "etat", "4",
        "Hébergement des demandeurs d'asile : des séjours plus courts",
        "Un dispositif saturé, qui ne loge pas tous les demandeurs",
        "Des places libérées, dont une partie se ferme",
        "{hebergement-demandeurs} × part de l'attente supprimée × "
        "{part-hebergement-economisee}",
        lambda v, a: (v("hebergement-demandeurs") * _reduction_asile(v)
                      * v("part-hebergement-economisee") * _asile(a)),
        "croissant jusqu'à la troisième année"),
    Poste(
        "proteges-plus-tot", "etat", "4",
        "Personnes protégées plus tôt : le droit commun plus tôt",
        "Protégées au bout de dix mois en moyenne",
        "Protégées quatre à six mois plus tôt, en moyenne : RSA et aides au "
        "logement aussi",
        "{demandes-asile} demandes × {taux-protection} protégées × mois "
        "gagnés × {cout-droit-commun} par an × {part-non-compensee}",
        lambda v, a: -(v("demandes-asile") * v("taux-protection")
                       * _mois_gagnes(v, a) / 12 * v("cout-droit-commun")
                       * v("part-non-compensee") / M),
        "croissant jusqu'à la troisième année"),
    Poste(
        "deboutes-plus-tot", "etat", "4",
        "Personnes déboutées plus tôt : l'aide médicale plus tôt",
        "Hébergées et allocataires jusqu'à la décision définitive",
        "Déboutées plus tôt ; celles qui restent relèvent de l'AME",
        "{demandes-asile} demandes × part déboutée × mois gagnés × "
        "{recours-ame} × {cout-ame} par an",
        lambda v, a: -(v("demandes-asile") * (1 - v("taux-protection"))
                       * _mois_gagnes(v, a) / 12 * v("recours-ame")
                       * v("cout-ame") / M),
        "croissant jusqu'à la troisième année"),
    Poste(
        "eloignements", "etat", "4",
        "Exécution effective des rejets : plus d'éloignements",
        "15 569 éloignements forcés en 2025",
        "{eloignements-supplementaires} de plus chaque année",
        "{eloignements-supplementaires} × ({cout-eloignement} + "
        "{placements-par-eloignement} placement × {cout-retention})",
        lambda v, a: -(v("eloignements-supplementaires")
                       * (v("cout-eloignement") + v("placements-par-eloignement")
                          * v("cout-retention")) * _loi(a) / M),
        "durable, dès le vote de la loi"),
    # ============================================ 5 : aucune carence
    Poste(
        "carence", "etat", "5",
        "Aucune carence nouvelle",
        "RSA après cinq ans de séjour, ASPA après dix",
        "Inchangé : aucune condition ajoutée, aucune retirée",
        "0 : c'est le point",
        lambda v, a: 0.0,
        "sans effet"),
    # ============================================ 6 : zéro file d'attente
    Poste(
        "gratuite-renouvellements", "etat", "6",
        "Renouvellements gratuits",
        "250 € par renouvellement depuis le 1er mai 2026 (100 € pour un "
        "étudiant)",
        "0 €",
        "({renouvellements} renouvellements − renouvellements évités) × "
        "{taxe-renouvellement}",
        lambda v, a: -((v("renouvellements") - _renouvellements_evites(v, a))
                       * v("taxe-renouvellement") * _loi(a) / M),
        "durable, dès la loi de finances"),
    Poste(
        "taxe-premiere-delivrance", "etat", "6",
        "Taxe de première délivrance alignée sur le coût du traitement",
        "350 € au tarif plein ; un coût évalué à 547 € par l'État",
        "La taxe suit le coût — qui baisse avec la réforme",
        "{premiers-titres-tarif-plein} titres × {variation-taxe-premiere}",
        lambda v, a: (v("premiers-titres-tarif-plein")
                      * v("variation-taxe-premiere") * _loi(a) / M),
        "durable, dès la loi de finances"),
    Poste(
        "guichet-rendez-vous", "etat", "6",
        "Rendez-vous sous quinze jours et guichet physique garanti",
        "Aucun délai garanti ; une solution de substitution peu appliquée",
        "Un droit, avec un guichet pour qui ne peut pas passer par internet",
        "{agents-accueil} agents × {cout-agent}",
        lambda v, a: -(v("agents-accueil") * v("cout-agent") * _loi(a) / M),
        "durable"),
    # ============================================ 7 : rendre des comptes
    Poste(
        "rendre-des-comptes", "etat", "7",
        "Rapport annuel, indicateurs publiés, suivi de cohortes",
        "Aucun débat annuel, aucun seuil d'alerte",
        "Un débat obligatoire sur des indicateurs publiés à l'avance",
        "{cout-suivi} par an",
        lambda v, a: -v("cout-suivi") * _loi(a),
        "durable"),
    # ============================================ ce qu'on contrôle
    Poste(
        "travail-dissimule", "etat", "controle",
        "Contrôles du travail dissimulé renforcés",
        "Un employeur qui embauche au noir s'expose peu",
        "{agents-controle} agents de contrôle de plus",
        "{agents-controle} agents × {cout-controleur}",
        lambda v, a: -(v("agents-controle") * v("cout-controleur") * _loi(a)
                       / M),
        "durable"),
    # ============================================ le travail déclaré : 1
    Poste(
        "regularises-prelevements", "travail", "1",
        "Cotisations et contributions des personnes régularisées",
        "Un travail au noir, ou sous une autre identité",
        "Un salarié déclaré, qui cotise en son nom",
        "personnes régularisées plus tôt — {regularisations-debut} de plus "
        "par an les trois premières années, {regularisations-regime} "
        "ensuite, cumulées — × {part-non-declares} au noir × "
        "{prelevements-smic} × {quotite}",
        lambda v, a: (_regularises(v, a) * _prelevements_par_regularise(v)
                      / M),
        "croissant à mesure que les cohortes s'ajoutent"),
    Poste(
        "regularises-rappels", "travail", "1",
        "Cotisations des six mois antérieurs, payées par l'employeur",
        "Le silence protège l'employeur",
        "L'employeur qui déclare et paie n'est pas poursuivi",
        "régularisations de l'année × {part-non-declares} au noir × "
        "{mois-rappel} de prélèvements, à {prelevements-smic} par an × "
        "{quotite} × {part-rappels-payes}",
        lambda v, a: (_regularisations(v, a) * _prelevements_par_regularise(v)
                      * v("mois-rappel") / 12 * v("part-rappels-payes") / M),
        "une fois par régularisation"),
    Poste(
        "regularises-taxes", "travail", "1",
        "Taxes acquittées par les personnes régularisées",
        "9 690 régularisations par le travail en 2025",
        "Un droit sur critères, taxé comme aujourd'hui",
        "régularisations de l'année × {taxes-regularisation}",
        lambda v, a: _regularisations(v, a) * v("taxes-regularisation") / M,
        "une fois par régularisation"),
    Poste(
        "regularises-instruction", "travail", "1",
        "Instruction des demandes de régularisation",
        "Des dossiers examinés au cas par cas",
        "Plus de dossiers, examinés sur critères",
        "régularisations de l'année ÷ (1 − {part-refus}) × "
        "{cout-dossier-regularisation}",
        lambda v, a: -(_regularisations(v, a) / (1 - v("part-refus"))
                       * v("cout-dossier-regularisation") / M),
        "une fois par demande"),
    Poste(
        "regularises-prestations", "travail", "1",
        "Prestations ouvertes par le titre",
        "Aucune, hors aide médicale de l'État",
        "Aides au logement et prestations familiales ; ni RSA ni prime "
        "d'activité avant cinq ans",
        "personnes régularisées plus tôt × {prestations-regularise}, plus "
        "{apl-premiere-annee} d'aide au logement la première année",
        lambda v, a: -(_regularises(v, a) * v("prestations-regularise")
                       + _regularisations(v, a) * v("apl-premiere-annee")) / M,
        "croissant à mesure que les cohortes s'ajoutent"),
    Poste(
        "regularises-ame", "travail", "1",
        "Aide médicale de l'État remplacée par l'assurance maladie",
        "Soins pris en charge par l'AME, sur le budget de l'État",
        "Soins pris en charge par l'assurance maladie, que la personne "
        "finance par ses cotisations",
        "0 : un transfert entre budgets, pas une économie",
        lambda v, a: 0.0,
        "sans effet sur le solde"),
    Poste(
        "regularises-francais", "travail", "1",
        "Cours de français et formation civique des nouveaux titulaires",
        "Des cours prescrits à l'arrivée, peu suivis d'effet",
        "Un accès effectif aux cours, dès la régularisation",
        "régularisations de l'année × {formation-francais}",
        lambda v, a: -_regularisations(v, a) * v("formation-francais") / M,
        "une fois par régularisation"),
    # ============================================ le travail déclaré : 4
    Poste(
        "demandeurs-prelevements", "travail", "4",
        "Cotisations des demandeurs d'asile qui travaillent",
        "Travail interdit six mois, puis soumis à autorisation",
        "Travail autorisé dès le dépôt de la demande",
        "{demandes-asile} demandes × {part-adultes} d'adultes × durée "
        "d'attente × {emploi-demandeurs} au travail × "
        "{prelevements-demandeur}",
        lambda v, a: (_demandeurs_au_travail(v, a)
                      * v("prelevements-demandeur") / M),
        "durable, et d'autant plus faible que la procédure raccourcit"),
    Poste(
        "demandeurs-allocation", "travail", "4",
        "Allocation retirée aux demandeurs qui gagnent leur vie",
        "Une allocation payée à qui n'a pas le droit de travailler",
        "Le revenu d'activité vient en déduction de l'allocation",
        "demandeurs au travail × {ada-mensuelle} × 12 × {part-ada-perdue}",
        lambda v, a: (_demandeurs_au_travail(v, a) * v("ada-mensuelle") * 12
                      * v("part-ada-perdue") / M),
        "durable, et d'autant plus faible que la procédure raccourcit"),
]

BLOCS = (
    ("etat", "Ce que l'État fait autrement",
     "À nombre de personnes inchangé : l'administration du séjour, l'asile, "
     "les éloignements, les taxes."),
    ("travail", "Ce que change le travail déclaré",
     "Des personnes déjà présentes qui cotisent en leur nom : régularisées, "
     "ou demandeuses d'asile autorisées à travailler."),
)

ENGAGEMENTS = {
    "1": "Un titre qui vaut travail",
    "2": "Des délais opposables",
    "3": "Le titre de quatre ans",
    "4": "L'asile jugé vite",
    "5": "Aucune carence nouvelle",
    "6": "Zéro file d'attente",
    "7": "Rendre des comptes",
    "controle": "Ce qu'on contrôle",
}

# ---------------------------------------------------------------------------
# Hors solde : si les flux réagissent. Le programme ne sait pas dire combien
# de personnes il attirera — il le dit ailleurs, et c'est vrai dans les deux
# sens. Ces deux ordres de grandeur permettent au lecteur de faire son propre
# compte : ce que rapportent 10 000 travailleurs de plus, ce que coûtent
# 10 000 demandes d'asile de plus.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Sensibilite:
    """Un ordre de grandeur hors solde : ce que coûte ou rapporte une tranche
    de 10 000 personnes de plus, si les flux réagissent à la réforme."""

    cle: str
    libelle: str
    explication: str
    formule: str
    calcul: Callable[[Valeur], float]


def _par_regularisations(v: Valeur) -> float:
    """10 000 régularisations de plus chaque année : l'effet en année 5.

    Le calcul est celui des postes de régularisation eux-mêmes, avec un volume
    de 10 000 à la place du repère : le chiffrage est linéaire en volume, et
    la différence est exactement ce que change la tranche.
    """
    volumes = ("regularisations-debut", "regularisations-regime")
    tranche: Valeur = lambda c: 10_000 if c in volumes else v(c)  # noqa: E731
    return sum(p.calcul(tranche, 5) for p in POSTES
               if p.cle.startswith("regularises-"))


SENSIBILITES = (
    Sensibilite(
        "regularisations",
        "Par tranche de 10 000 régularisations de plus chaque année",
        "Le nombre de régularisations est l'hypothèse la plus fragile de ce "
        "chiffrage. Voici ce que change, au bout de cinq ans, chaque tranche "
        "de 10 000 régularisations annuelles de plus que notre repère — ou de "
        "moins, au signe près. Tout tient à la part de travail au noir et aux "
        "familles.",
        "10 000 × 4,5 cohortes × ({part-non-declares} au noir × "
        "{prelevements-smic} × {quotite} − {prestations-regularise}) + "
        "10 000 × ({taxes-regularisation} + {mois-rappel} de rappel × "
        "{part-rappels-payes} − {cout-dossier-regularisation} ÷ "
        "(1 − {part-refus}) − {apl-premiere-annee} − {formation-francais})",
        _par_regularisations),
    Sensibilite(
        "eloignements", "Par tranche de 1 000 éloignements forcés de plus",
        "L'exécution des rejets est chiffrée à 4 000 éloignements forcés de "
        "plus par an. Chaque millier au-delà — ou en deçà — coûte ou épargne "
        "ce montant chaque année.",
        "1 000 × ({cout-eloignement} + {placements-par-eloignement} × "
        "{cout-retention})",
        lambda v: -1_000 * (v("cout-eloignement")
                            + v("placements-par-eloignement")
                            * v("cout-retention")) / M),
    Sensibilite(
        "travailleurs", "Par tranche de 10 000 travailleurs de plus",
        "Si l'ouverture du travail attire des salariés — c'est son objet —, "
        "chaque tranche de 10 000, présents toute l'année et payés au SMIC, "
        "apporte ce montant chaque année, prestations familiales déduites. "
        "Au-dessus du SMIC, davantage.",
        "10 000 × ({prelevements-smic} × {quotite} − "
        "{prestations-regularise})",
        lambda v: 10_000 * (v("prelevements-smic") * v("quotite")
                            - v("prestations-regularise")) / M),
    Sensibilite(
        "demandes", "Par tranche de 10 000 demandes d'asile de plus",
        "Si le travail dès le dépôt attire des demandes — c'est le risque que "
        "nous reconnaissons —, chaque tranche de 10 000 coûte ce montant : "
        "l'instruction, puis l'allocation et l'hébergement le temps de la "
        "procédure. Sans compter la suite, protection ou éloignement.",
        "10 000 × ({cout-decision-ofpra} + {part-recours} × "
        "{cout-decision-cnda} + ({delai-asile-programme} de procédure + un "
        "mois) × ({ada-mensuelle} + {part-hebergee} × {cout-place-mois}))",
        lambda v: -10_000 * (
            v("cout-decision-ofpra") + v("part-recours") * v("cout-decision-cnda")
            + (v("delai-asile-programme") + 1)
            * (v("ada-mensuelle") + v("part-hebergee") * v("cout-place-mois"))
        ) / M),
)

# ---------------------------------------------------------------------------
# Le moteur
# ---------------------------------------------------------------------------

_SCENARIOS: dict[tuple[str, int], dict[str, float]] = {}


def _somme(postes: list[Poste], valeurs: dict[str, float], annee: int) -> float:
    return sum(p.calcul(valeurs.__getitem__, annee) for p in postes)


def scenario(nom: str, annee: int) -> dict[str, float]:
    """Les valeurs des hypothèses dans le scénario PRUDENT ou FAVORABLE.

    Chaque hypothèse prend la borne qui dégrade (prudent) ou améliore
    (favorable) le solde total de l'année, compte tenu des autres. Le solde est
    multilinéaire en ses hypothèses : on part du milieu des fourchettes et on
    ajuste une hypothèse à la fois jusqu'à ce qu'aucune ne bouge plus — ce qui
    atteint un sommet de la boîte des hypothèses, le plus défavorable (ou
    favorable) qu'on puisse atteindre en changeant une hypothèse à la fois.
    """
    if nom not in ("prudent", "favorable"):
        raise ValueError(f"scénario inconnu : {nom!r}")
    if (nom, annee) in _SCENARIOS:
        return _SCENARIOS[(nom, annee)]
    signe = 1 if nom == "favorable" else -1
    valeurs = {c: (h.bas + h.haut) / 2 for c, h in HYPOTHESES.items()}
    for _ in range(10):
        change = False
        for cle, h in HYPOTHESES.items():
            if h.bas == h.haut:
                valeurs[cle] = h.bas
                continue
            avec_bas = _somme(POSTES, {**valeurs, cle: h.bas}, annee)
            avec_haut = _somme(POSTES, {**valeurs, cle: h.haut}, annee)
            if abs(avec_haut - avec_bas) < 1e-9:
                # Sans effet cette année-là : elle garde sa valeur médiane.
                continue
            choix = h.haut if signe * (avec_haut - avec_bas) > 0 else h.bas
            if valeurs[cle] != choix:
                valeurs[cle] = choix
                change = True
        if not change:
            _SCENARIOS[(nom, annee)] = valeurs
            return valeurs
    raise RuntimeError("les scénarios ne se stabilisent pas")


def montant(poste: Poste, annee: int, nom: str) -> float:
    """Le montant d'un poste dans un scénario du solde total."""
    return poste.calcul(scenario(nom, annee).__getitem__, annee)


def total(postes: list[Poste], annee: int, nom: str) -> float:
    """La somme de quelques postes dans un scénario du solde total.

    Les sous-totaux sont pris dans les scénarios du TOTAL, pour que les
    lignes d'un tableau s'additionnent : le solde prudent est la somme des
    montants prudents, exactement.
    """
    return sum(montant(p, annee, nom) for p in postes)


def fourchette(postes: list[Poste], annee: int) -> tuple[float, float]:
    """Les deux valeurs d'un ensemble de postes, triées."""
    a, b = total(postes, annee, "prudent"), total(postes, annee, "favorable")
    return (min(a, b), max(a, b))


def milieu(annee: int, postes: list[Poste] | None = None) -> float:
    """Le solde quand toutes les hypothèses sont au milieu de leur fourchette.

    Donné pour mémoire, et nommé comme tel : ce n'est pas une prévision, et
    rien ne dit que la vérité soit au milieu.
    """
    postes = POSTES if postes is None else postes
    return _somme(postes, {k: (h.bas + h.haut) / 2
                           for k, h in HYPOTHESES.items()}, annee)


def solde(annee: int) -> tuple[float, float]:
    """Le solde total (prudent, favorable) d'une année."""
    return (total(POSTES, annee, "prudent"), total(POSTES, annee, "favorable"))


def plus_et_moins(annee: int, nom: str) -> tuple[float, float]:
    """La somme des plus et celle des moins, dans un scénario."""
    montants = [montant(p, annee, nom) for p in POSTES]
    return (sum(m for m in montants if m > 0),
            sum(m for m in montants if m < 0))


def postes_du_bloc(bloc: str) -> list[Poste]:
    return [p for p in POSTES if p.bloc == bloc]


def postes_de_l_engagement(engagement: str, bloc: str = "") -> list[Poste]:
    return [p for p in POSTES if p.engagement == engagement
            and (not bloc or p.bloc == bloc)]


def sensibilite(s: Sensibilite) -> tuple[float, float]:
    """Le plus bas et le plus haut d'une sensibilité.

    Évaluée à tous les sommets de la boîte de ses hypothèses — elles sont
    peu nombreuses —, et non aux deux seuls coins « tout bas » et « tout
    haut », qui ne sont pas les extrêmes quand une hypothèse joue en plus et
    une autre en moins.
    """
    variables = [c for c in dict.fromkeys(citees(s.formule))
                 if HYPOTHESES[c].bas != HYPOTHESES[c].haut]
    milieu = {c: (h.bas + h.haut) / 2 for c, h in HYPOTHESES.items()}
    resultats = []
    for rang in range(2 ** len(variables)):
        valeurs = dict(milieu)
        for i, c in enumerate(variables):
            h = HYPOTHESES[c]
            valeurs[c] = h.haut if rang >> i & 1 else h.bas
        resultats.append(s.calcul(valeurs.__getitem__))
    return (min(resultats), max(resultats))


def poids_des_hypotheses(annee: int) -> list[tuple[str, float]]:
    """Ce que chaque hypothèse déplace dans le solde de l'année, du plus au
    moins : l'écart de solde entre ses deux bornes, les autres étant au
    milieu de leur fourchette. C'est la liste de ce qui nous ferait mentir."""
    milieu = {c: (h.bas + h.haut) / 2 for c, h in HYPOTHESES.items()}
    ecarts = []
    for cle, h in HYPOTHESES.items():
        if h.bas == h.haut:
            continue
        ecart = abs(_somme(POSTES, {**milieu, cle: h.haut}, annee)
                    - _somme(POSTES, {**milieu, cle: h.bas}, annee))
        ecarts.append((cle, ecart))
    return sorted(ecarts, key=lambda e: e[1], reverse=True)


def citees(formule: str) -> list[str]:
    """Les clés d'hypothèses qu'une formule cite, dans l'ordre."""
    return re.findall(r"\{([a-z0-9-]+)\}", formule)


def verifier() -> None:
    """Ce qui doit être vrai pour que le chiffrage ait un sens.

    Appelée à la construction : une formule qui cite une hypothèse inconnue,
    une hypothèse que rien ne cite, une fiche du registre qui n'existe pas, et
    la construction échoue. Une hypothèse qu'aucune formule ne cite est une
    hypothèse qu'aucun lecteur ne peut retrouver dans un calcul.
    """
    formules = [p.formule for p in POSTES] + [s.formule for s in SENSIBILITES]
    cles = {cle for f in formules for cle in citees(f)}
    for cle in sorted(cles - set(HYPOTHESES)):
        raise KeyError(f"une formule cite une hypothèse inconnue : {cle!r}")
    for cle, h in HYPOTHESES.items():
        if h.bas > h.haut:
            raise ValueError(f"hypothèse {cle!r} : borne basse > borne haute")
        if h.chiffre and h.chiffre not in CHIFFRES:
            raise KeyError(f"hypothèse {cle!r} : fiche inconnue {h.chiffre!r}")
        if h.nature not in ("constat", "estimation", "hypothese", "parametre"):
            raise ValueError(f"hypothèse {cle!r} : nature {h.nature!r}")
    orphelines = sorted(set(HYPOTHESES) - cles)
    if orphelines:
        raise KeyError("hypothèses citées dans aucune formule : "
                       + ", ".join(orphelines))
    for annee in ANNEES:
        prudent, favorable = solde(annee)
        if prudent > favorable:
            raise ValueError(f"année {annee} : solde prudent > favorable")
