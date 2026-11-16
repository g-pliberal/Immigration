"""Le registre des échéances : les phrases du site qui ont une date de péremption.

Pourquoi ce module existe. Une partie du site décrit le droit tel qu'il est
*aujourd'hui* en parlant d'une date à venir : « l'article L. 435-4 expire le
31 décembre 2026 », « une circulaire publiée avant la fin de l'année », « le
projet de loi de finances n'est pas voté à ce jour ». Ces phrases sont exactes
le jour où on les écrit et fausses le lendemain de l'échéance — sans que rien
dans le dépôt ne change. Le contrôle de fraîcheur des pages (les pages
correspondent-elles à leurs modules ?) ne les voit donc jamais.

Chaque phrase de ce genre est déclarée **ici**, avec le jour où elle devient
fausse et ce qu'il faudra écrire à la place. Le texte des pages, lui, ne
change pas : une entrée décrit la phrase par des motifs cherchés dans le texte
**publié** (les pages HTML), si bien qu'on peut récrire une page sans toucher
à ce registre. ``scripts/verifier.py`` en tire trois règles :

1. **une échéance passée dont une page porte encore la phrase fait échouer la
   vérification** — et la vérification tourne chaque jour sur GitHub, même
   sans commit : le dépôt échoue tout seul le 1er janvier ;
2. une échéance à moins de ``PREAVIS`` jours est signalée sans échouer ;
3. **une date à venir écrite dans une page sans être couverte par une entrée
   fait échouer la vérification** : on ne peut pas ajouter une phrase datée
   en oubliant de la déclarer.

Une échéance passée dont plus aucune page ne porte la phrase est signalée
pour qu'on retire l'entrée, mais n'échoue pas : la page a été mise à jour,
c'est ce qu'on voulait.
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass

# Combien de jours avant une échéance la vérification commence à la signaler.
PREAVIS = 30

MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre")

# Une date écrite en toutes lettres : « 31 décembre 2026 », « 1er janvier 2027 ».
DATE_ECRITE = re.compile(
    r"\b(\d{1,2})(?:er)?\s+(" + "|".join(MOIS) + r")\s+(\d{4})\b")


@dataclass(frozen=True)
class Echeance:
    """Une affirmation du site qui cesse d'être vraie à une date connue.

    ``perime_le`` est le **premier jour où la phrase est fausse** (le lendemain
    de l'échéance), ou, pour une phrase dont on ne connaît pas le jour exact,
    la date à laquelle elle doit avoir été relue. ``motifs`` sont des
    expressions régulières cherchées dans le texte publié, espaces normalisés :
    chacune doit trouver la phrase sur au moins une page tant que l'entrée
    existe, sinon le registre ne décrit plus le site. ``a_faire`` dit ce que
    la relecture devra écrire à la place.
    """

    affirmation: str
    perime_le: datetime.date
    motifs: tuple[str, ...]
    a_faire: str


ECHEANCES: dict[str, Echeance] = {
    "l435-4": Echeance(
        affirmation="L'article L. 435-4 du CESEDA (régularisation par le "
                    "travail dans les métiers en tension) est en vigueur et "
                    "expire le 31 décembre 2026",
        perime_le=datetime.date(2027, 1, 1),
        motifs=(
            r"expire le 31 décembre 2026",
            r"disparaît le 31 décembre 2026",
            r"avant l'expiration de l'article L\. 435-4 le 31 décembre 2026",
            r"après le 31 décembre, la régularisation par le travail ne "
            r"reposera plus",
            r"plus ouvert que l'article L\. 435-4 actuel",
            r"Attente des trois ans de présence exigés \(art\. L\. 435-4\)",
        ),
        a_faire="Passer au passé (« a expiré le 31 décembre 2026 »), décrire "
                "le régime qui le remplace (circulaire, admission "
                "exceptionnelle de l'article L. 435-1), revoir la colonne "
                "« aujourd'hui » du comparateur et le tableau « ce qui "
                "change » du programme."),
    "circulaire-l435-4": Echeance(
        affirmation="La circulaire qui doit remplacer l'article L. 435-4 est "
                    "annoncée « avant la fin de l'année » 2026",
        perime_le=datetime.date(2027, 1, 1),
        motifs=(r"publiée avant la fin de l'année",),
        a_faire="Dire si la circulaire a été publiée, avec sa date et sa "
                "référence, et ce qu'elle reprend de l'article L. 435-4."),
    "plf-2027": Echeance(
        affirmation="Le projet de loi de finances pour 2027 n'est pas voté ; "
                    "le chiffrage s'en tient aux crédits votés pour 2026",
        # La loi de finances est d'ordinaire promulguée dans les derniers
        # jours de décembre : à défaut d'une date connue, c'est la date de
        # relecture obligatoire.
        perime_le=datetime.date(2027, 1, 1),
        motifs=(r"il n'est pas voté à ce jour",),
        a_faire="Remplacer les crédits 2026 par les crédits votés pour 2027 "
                "dans le registre des chiffres et dans le chiffrage, ou dire "
                "pourquoi la loi n'est toujours pas votée."),
}


def _date(jour: str, mois: str, annee: str) -> datetime.date | None:
    try:
        return datetime.date(int(annee), MOIS.index(mois) + 1, int(jour))
    except ValueError:
        return None


def verifier(textes: dict[str, str], aujourdhui: datetime.date
             ) -> tuple[list[str], list[str]]:
    """Confronte le registre au texte publié de chaque page.

    ``textes`` associe le nom d'une page à son texte, balises retirées.
    Renvoie les fautes (qui font échouer la vérification) et les
    avertissements (qui ne la font pas échouer).
    """
    fautes: list[str] = []
    avertissements: list[str] = []
    textes = {nom: re.sub(r"\s+", " ", t) for nom, t in textes.items()}

    # Où chaque entrée trouve-t-elle sa phrase ? Et quels passages couvre-t-elle ?
    couverts: dict[str, list[tuple[int, int]]] = {nom: [] for nom in textes}
    for cle, e in ECHEANCES.items():
        pages_echeance: set[str] = set()
        for motif in e.motifs:
            trouve = False
            for nom, texte in textes.items():
                for m in re.finditer(motif, texte):
                    trouve = True
                    pages_echeance.add(nom)
                    couverts[nom].append(m.span())
            if not trouve and e.perime_le > aujourdhui:
                fautes.append(
                    f"échéance « {cle} » : le motif « {motif} » ne se trouve "
                    "plus sur aucune page — le retirer du registre, ou "
                    "l'accorder au nouveau texte")

        pages = ", ".join(sorted(pages_echeance))
        reste = (e.perime_le - aujourdhui).days
        if reste <= 0:
            if pages_echeance:
                fautes.append(
                    f"échéance « {cle} » PASSÉE depuis le "
                    f"{e.perime_le:%d/%m/%Y} : « {e.affirmation} » — encore "
                    f"écrit sur {pages}. À faire : {e.a_faire}")
            else:
                avertissements.append(
                    f"échéance « {cle} » passée, et plus aucune page ne porte "
                    "la phrase : l'entrée peut être retirée de "
                    "src/immigration/echeances.py")
        elif reste <= PREAVIS:
            avertissements.append(
                f"échéance « {cle} » dans {reste} jour(s) "
                f"({e.perime_le:%d/%m/%Y}) : « {e.affirmation} » — sur "
                f"{pages}. À préparer : {e.a_faire}")

    # Une date à venir écrite dans une page doit être couverte par une entrée.
    for nom, texte in textes.items():
        for m in DATE_ECRITE.finditer(texte):
            date = _date(*m.groups())
            if date is None or date < aujourdhui:
                continue
            if any(debut <= m.start() and m.end() <= fin
                   for debut, fin in couverts[nom]):
                continue
            extrait = texte[max(0, m.start() - 60):m.end() + 20].strip()
            fautes.append(
                f"{nom} : date à venir « {m.group(0)} » qu'aucune échéance ne "
                f"couvre (« …{extrait}… ») — la déclarer dans "
                "src/immigration/echeances.py")

    return fautes, avertissements
