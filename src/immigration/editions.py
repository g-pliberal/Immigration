"""Le calendrier des sources : quand chaque chiffre du site doit être renouvelé.

Pourquoi ce module existe. Le registre des chiffres (``chiffres.py``) dit de
quelle année datent les données et quand elles ont été publiées. Il ne dit pas
quand elles cesseront d'être les plus récentes. Or la plupart des sources du
site paraissent à date fixe : la DGEF publie « L'essentiel de l'immigration »
chaque fin janvier, l'INSEE ses estimations chaque fin juin, le Conseil d'État
son rapport chaque automne. Le jour où l'édition suivante paraît, rien dans le
dépôt ne change, et un chiffre exact la veille devient un chiffre dépassé que
le site continue de présenter comme le plus récent. C'est le même défaut que
celui des phrases datées (``echeances.py``), appliqué aux chiffres.

Chaque chiffre du registre déclare donc **ici** l'édition qui le remplacera :
ce qui doit paraître, quand (en clair, pour la page « Tous les chiffres »), et
le jour à partir duquel on peut raisonnablement la tenir pour parue. Un
rapport ponctuel, sans édition suivante prévue, le dit aussi : l'absence de
déclaration est une faute, pas un « ponctuel » par défaut.

``scripts/verifier.py``, qui tourne chaque matin, en tire trois règles :

1. une édition attendue dans moins de ``PREAVIS`` jours est **signalée** ;
2. une édition qui devrait être parue est **signalée**, avec la liste des
   chiffres à reprendre ;
3. **passé ``DELAI`` jours**, la vérification **échoue** — et un échec planifié
   est signalé par courriel au propriétaire du dépôt.

Les dates ``attendue`` sont des estimations tirées du calendrier de l'édition
précédente, pas des dates annoncées : une publication peut glisser. Mettre un
chiffre à jour, c'est donc deux gestes — changer la valeur dans
``chiffres.py``, et déclarer ici l'édition d'après. Si l'édition attendue n'a
pas paru, on reporte sa date en disant pourquoi : le report reste écrit, et
le chiffre ne vieillit pas en silence.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass

from .echeances import PREAVIS

# Combien de jours une édition peut être parue sans que les chiffres qu'elle
# remplace aient été repris, avant que la vérification échoue. Assez pour
# qu'une parution en retard, ou une relecture prévue le mois suivant, ne fasse
# pas échouer le dépôt ; assez court pour qu'un chiffre dépassé ne reste pas
# une saison entière sur le site.
DELAI = 90


@dataclass(frozen=True)
class Edition:
    """La prochaine édition d'une source, ou l'absence d'édition prévue.

    ``titre`` dit ce qui doit paraître ; ``quand`` le dit en clair pour le
    lecteur (« fin janvier 2027 ») — jamais sous la forme « 1er février
    2027 », qui serait une date à venir à déclarer dans ``echeances.py`` ;
    ``attendue`` est le jour à partir duquel l'édition devrait être parue,
    ou ``None`` pour une source qui n'a pas d'édition suivante.
    """

    titre: str
    quand: str = ""
    attendue: datetime.date | None = None


def ponctuel(raison: str) -> Edition:
    """Une source sans édition suivante prévue — et pourquoi."""
    return Edition(titre=raison)


_DGEF = Edition(
    "Ministère de l'Intérieur, « L'essentiel de l'immigration » — données 2026",
    "fin janvier 2027", datetime.date(2027, 2, 1))
# L'édition 2026 est parue le 25 juin 2026.
_INSEE = Edition(
    "INSEE, « L'essentiel sur… les immigrés et les étrangers » — données 2026",
    "fin juin 2027", datetime.date(2027, 7, 15))
# Le site s'en tient aux crédits votés pour 2026 tant que ceux de 2027 ne le
# sont pas (voir l'échéance « plf-2027 ») : l'édition qui compte est la loi,
# pas le projet.
_LFI_2027 = Edition(
    "Loi de finances pour 2027, et les crédits qu'elle vote",
    "fin décembre 2026, si le budget est voté à temps",
    datetime.date(2027, 1, 1))
# Le projet annuel de performances 2027 accompagne le projet de loi de
# finances déposé en octobre 2026 : il porte les délais constatés en 2025.
_PAP_2027 = Edition(
    "Projet annuel de performances 2027, mission « Immigration, asile et "
    "intégration » — réalisé 2025",
    "octobre 2026", datetime.date(2026, 10, 15))
_CE_2026 = Edition(
    "Conseil d'État, rapport public 2026 — activité juridictionnelle de 2025",
    "septembre 2026", datetime.date(2026, 10, 1))
_CE_2027 = Edition(
    "Conseil d'État, rapport public 2027 — activité juridictionnelle de 2026",
    "septembre 2027", datetime.date(2027, 10, 1))
_RAPPORT_PONCTUEL = ponctuel("Aucune prévue : rapport ponctuel")

PROCHAINES: dict[str, Edition] = {
    # ---------------------------------------------------------------- population
    "immigres": _INSEE,
    "etrangers": _INSEE,
    "immigres-francais": _INSEE,
    # ------------------------------------------------------------------- flux
    "sejour-regulier": _DGEF,
    "premiers-titres": _DGEF,
    "titres-etudiants": _DGEF,
    "titres-humanitaire": _DGEF,
    "titres-familial": _DGEF,
    "titres-economique": _DGEF,
    "titres-divers": _DGEF,
    "part-travail": _DGEF,
    "renouvellements": _DGEF,
    "regularisations": _DGEF,
    # Un chiffre de presse, à remplacer par celui de la DGEF : au plus tard
    # par l'édition de janvier, qui portera aussi celui de 2026.
    "aes-travail": _DGEF,
    "renouvellements-travail-etudes": _RAPPORT_PONCTUEL,
    # ------------------------------------------------------------------ asile
    "asile-demandes": _DGEF,
    "asile-protection": _DGEF,
    "delai-asile": _PAP_2027,
    "ofpra-activite": Edition(
        "OFPRA, rapport d'activité 2026", "juillet 2027",
        datetime.date(2027, 8, 1)),
    "cnda-activite": Edition(
        "CNDA, rapport d'activité 2026", "mars 2027",
        datetime.date(2027, 4, 1)),
    "hebergement-asile": _LFI_2027,
    "ada-beneficiaires": Edition(
        "Sénat, rapport sur le projet de loi de finances pour 2027, mission "
        "« Immigration, asile et intégration »",
        "fin novembre 2026", datetime.date(2026, 12, 15)),
    # ------------------------------------------------------------ éloignement
    "oqtf-prononcees": _DGEF,
    "oqtf-executees": _DGEF,
    "eloignements": _DGEF,
    "cout-eloignement": _RAPPORT_PONCTUEL,
    "retention": _RAPPORT_PONCTUEL,
    # --------------------------------------------------------- administration
    "contentieux-ta": _CE_2027,
    # Le site cite déjà le rapport 2026 pour le contentieux des étrangers :
    # ce total-ci est resté à l'édition d'avant.
    "ta-affaires": _CE_2026,
    "agents-etrangers": ponctuel(
        "Aucune prévue : évaluation d'un article du projet de loi de finances "
        "pour 2026"),
    "cout-premier-titre": ponctuel(
        "Aucune prévue : évaluation d'un article du projet de loi de finances "
        "pour 2026"),
    # ----------------------------------------------------------------- argent
    "mission-budget": _LFI_2027,
    "ada-credits": _LFI_2027,
    "taxes-titres": _RAPPORT_PONCTUEL,
    "tarifs-titres": _LFI_2027,
    "prelevements-smic": Edition(
        "Groupe d'experts sur le SMIC, rapport 2026, et barèmes de janvier",
        "décembre 2026", datetime.date(2027, 1, 1)),
    "cir-formation": _RAPPORT_PONCTUEL,
    "irreguliere-cout": _RAPPORT_PONCTUEL,
    "ame": Edition(
        "Commission des comptes de la sécurité sociale, rapport de l'automne "
        "2026", "octobre 2026", datetime.date(2026, 11, 1)),
    "solde-budgetaire": ponctuel(
        "Aucune attendue : une fourchette tirée de travaux sans calendrier"),
}


def verifier(aujourdhui: datetime.date,
             prochaines: dict[str, Edition] | None = None,
             cles: set[str] | None = None) -> tuple[list[str], list[str]]:
    """Confronte le calendrier des sources à la date du jour.

    Renvoie les fautes (qui font échouer la vérification) et les
    avertissements (qui ne la font pas échouer). Les chiffres d'une même
    édition sont signalés ensemble : c'est une seule publication à relire.
    """
    if prochaines is None:
        prochaines = PROCHAINES
    if cles is None:
        from .chiffres import CHIFFRES
        cles = set(CHIFFRES)

    fautes: list[str] = []
    avertissements: list[str] = []

    for cle in sorted(cles - set(prochaines)):
        fautes.append(
            f"chiffre « {cle} » : aucune édition suivante déclarée dans "
            "src/immigration/editions.py — dire quand sa source le "
            "renouvellera, ou qu'elle ne le renouvellera pas")
    for cle in sorted(set(prochaines) - cles):
        fautes.append(
            f"src/immigration/editions.py : « {cle} » n'est pas une clé du "
            "registre des chiffres")

    par_edition: dict[Edition, list[str]] = {}
    for cle in sorted(set(prochaines) & cles):
        par_edition.setdefault(prochaines[cle], []).append(cle)

    for edition, liste in par_edition.items():
        if edition.attendue is None:
            continue
        chiffres = ", ".join(liste)
        verbe = "n'a" if len(liste) == 1 else "n'ont"
        ecart = (aujourdhui - edition.attendue).days
        if ecart >= DELAI:
            fautes.append(
                f"« {edition.titre} », attendue {edition.quand}, devrait être "
                f"parue depuis le {edition.attendue:%d/%m/%Y} : {chiffres} "
                f"{verbe} pas été repris depuis plus de {DELAI} jours. Mettre "
                "ces chiffres à jour et déclarer l'édition suivante, ou, si "
                "celle-ci n'a pas paru, reporter sa date en disant pourquoi")
        elif ecart >= 0:
            echec = edition.attendue + datetime.timedelta(days=DELAI)
            avertissements.append(
                f"« {edition.titre} » devrait être parue (attendue "
                f"{edition.quand}) : reprendre {chiffres} — la vérification "
                f"échouera à partir du {echec:%d/%m/%Y}")
        elif -ecart <= PREAVIS:
            avertissements.append(
                f"« {edition.titre} » attendue dans {-ecart} jour(s) "
                f"({edition.quand}) : {chiffres} seront à reprendre")

    return fautes, avertissements
