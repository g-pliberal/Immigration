"""Le programme : les six engagements, article par article."""

from __future__ import annotations

from .. import gabarit as g
from .accueil import ENGAGEMENTS

PAGE = {
    "fichier": "programme.html",
    "titre": "Le programme libéral pour l'immigration",
    "description": (
        "Six engagements : un titre unique valant autorisation de travail, des "
        "délais opposables, un titre pluriannuel, l'asile en trois mois, les "
        "prestations non contributives après cinq ans, zéro file d'attente."),
}


def construire() -> str:
    corps = g.affiche(
        "La proposition",
        "Ouvrir le travail, <span class=\"serif\">tenir les délais</span>",
        "Six engagements, chacun avec le texte qu'il faut changer, ce qu'il "
        "coûte, et ce qu'on peut en attendre. Rien ici ne demande de sortir "
        "d'un traité, ni de réviser la Constitution.")

    corps += g.engagements(ENGAGEMENTS)

    corps += g.plan([
        ("un", "1. Un titre qui vaut travail"),
        ("deux", "2. Des délais opposables"),
        ("trois", "3. Le titre pluriannuel"),
        ("quatre", "4. L'asile en trois mois"),
        ("cinq", "5. Travail et guichet séparés"),
        ("six", "6. Zéro file d'attente"),
        ("controle", "Ce qu'on contrôle vraiment"),
        ("calendrier", "Calendrier et coût"),
    ])

    corps += """
<h2 id="un">1. Un seul titre, qui vaut autorisation de travailler</h2>
<p><strong>Ce qui change.</strong> L'autorisation de travail disparaît comme
acte administratif distinct. Tout étranger en séjour régulier — travail,
études, famille, protection — peut occuper un emploi, en changer, changer de
métier et de région, dans les mêmes conditions qu'un résident. La délivrance
du titre elle-même repose sur des critères objectifs : un contrat ou une
promesse d'embauche, l'identité établie, un casier judiciaire vérifié, une
rémunération au moins égale au minimum légal de la branche.</p>
<p><strong>Ce qu'on supprime.</strong> L'opposabilité de la situation de
l'emploi et les listes de métiers en tension. Un arrêté ne décide plus, métier
par métier et région par région, où le marché du travail a le droit de
fonctionner.</p>
"""

    corps += g.tableau(
        ["Texte", "Aujourd'hui", "Après"],
        [["Code du travail, art. L. 5221-2",
          "Autorisation de travail préalable, demandée par l'employeur",
          "Abrogé : le titre de séjour régulier vaut autorisation"],
         ["Code du travail, art. R. 5221-20",
          "Refus possible au titre de la situation de l'emploi",
          "Abrogé, listes de métiers en tension comprises"],
         ["CESEDA, admission exceptionnelle au séjour",
          "Régularisation discrétionnaire, au cas par cas",
          "Remplacée par un droit sur critères : emploi déclaré, identité "
          "établie, casier vierge, durée de présence"]],
        legende="Les trois textes qui portent l'essentiel de l'engagement 1.",
        classes_colonnes=["texte", "long", "long"])

    corps += g.note(
        "<p><strong>Ce n'est pas une régularisation générale.</strong> C'est "
        "un droit soumis à conditions, contrôlable, et refusable : identité "
        "non établie, casier chargé, fraude documentaire, emploi non déclaré "
        "restent des motifs de refus — et le deviennent réellement, puisque "
        "l'administration n'a plus à consacrer son temps à des dossiers que "
        "rien ne justifiait d'examiner.</p>", "vigilance")

    corps += """
<h2 id="deux">2. Un délai opposable, et le silence vaut accord</h2>
<p><strong>Ce qui change.</strong> Huit semaines pour instruire une première
demande de titre de travail ou d'études, quatre semaines pour un
renouvellement. Passé ce délai sans décision motivée notifiée, le titre est
réputé délivré, et l'administration délivre le document matériel sur simple
demande.</p>
<p>C'est la règle de droit commun française depuis 2013 — le silence de
l'administration vaut acceptation — dont le droit des étrangers est l'une des
principales exceptions. Nous proposons d'y mettre fin. Le préfet conserve tous
ses pouvoirs de refus : il doit seulement les exercer dans un délai.</p>
"""

    corps += g.points([
        ("Un récépissé qui vaut droit au travail",
         "Dès le dépôt d'un dossier complet, et jusqu'à la décision : aucune "
         "rupture de droits par la faute du guichet."),
        ("Une responsabilité de l'État",
         "Le dépassement de délai ouvre droit à indemnisation forfaitaire, "
         "comme pour tout service public qui ne rend pas le service dû."),
        ("Un dossier complet, une fois",
         "La liste des pièces est limitative, publiée, et ne peut pas être "
         "complétée en cours d'instruction."),
        ("Et pour l'administration",
         "Des moyens redéployés : ce qu'on cesse d'instruire — autorisations "
         "de travail, renouvellements annuels — finance les délais qu'on tient."),
    ])

    corps += """
<h2 id="trois">3. Un titre pluriannuel dès la première délivrance</h2>
<p><strong>Ce qui change.</strong> Quatre ans pour le travail et les études dès
le premier titre, renouvelable en ligne sans présence physique quand rien n'a
changé. Dix ans — la carte de résident — après cinq ans de séjour régulier,
sur critères objectifs. Le titre n'est plus attaché à un employeur : il suit la
personne.</p>
<p><strong>Pourquoi.</strong> Parce que le renouvellement annuel est la
principale cause d'engorgement des préfectures, et parce qu'un salarié dont le
séjour dépend de son patron ne négocie pas son salaire. Rendre le titre
portable, c'est rendre au marché du travail sa fluidité — et retirer aux
employeurs indélicats un moyen de pression que la loi leur donne
aujourd'hui.</p>
"""

    corps += """
<h2 id="quatre">4. L'asile jugé en trois mois, travail autorisé dès le dépôt</h2>
<p><strong>Ce qui change.</strong> Un objectif de trois mois, recours compris,
opposable à l'administration. Le droit de travailler ouvert dès
l'enregistrement de la demande, et non après six mois. En contrepartie,
l'exécution effective des décisions définitives de rejet.</p>
<p><strong>Comment on tient trois mois.</strong> En redéployant vers l'OFPRA et
la CNDA une partie des moyens que l'on cesse de consacrer à l'hébergement de
l'attente et à l'instruction des autorisations de travail ; en jugeant en juge
unique les procédures manifestement infondées comme manifestement fondées ; et
en cessant de traiter comme un contentieux de masse ce qui devrait être une
décision rapide prise sur un dossier.</p>
"""

    corps += g.note(
        "<p><strong>Le droit d'asile n'est pas négociable, et il n'est pas une "
        "politique migratoire.</strong> Il découle de la Constitution et de la "
        "Convention de Genève. Le rendre rapide, c'est le rendre crédible : "
        "une protection accordée en trois mois vaut mieux qu'une protection "
        "accordée en deux ans, et un refus prononcé en trois mois s'exécute, "
        "quand un refus prononcé après deux ans de vie installée ne s'exécute "
        "plus.</p>")

    corps += """
<h2 id="cinq">5. Le travail, pas le guichet</h2>
<p><strong>Ce qui change.</strong> Les prestations <em>non contributives</em> —
celles qu'on perçoit sans avoir cotisé : revenu de solidarité, allocations de
logement, minima sociaux — sont ouvertes après cinq ans de résidence régulière.
Les prestations <em>contributives</em>, elles, sont dues dès le premier euro
cotisé : ce sont des droits achetés, pas des aides.</p>
<p><strong>Ce qui ne change pas.</strong> Les soins urgents et la santé
publique, l'école obligatoire des enfants, et l'intégralité des droits des
réfugiés statutaires, qui relèvent de la protection internationale.</p>
"""

    corps += g.cle(
        "Pourquoi cette règle est la clé de tout le reste",
        "C'est la réponse à l'objection de Milton Friedman : <strong>« on ne "
        "peut pas avoir à la fois des frontières ouvertes et un État-providence "
        "illimité »</strong>. Exact — alors on choisit lequel des deux on "
        "ouvre, et on le dit.",
        corps="<p>Nous ouvrons le travail et différons l'aide. Ce choix est "
              "cohérent : il fait venir des gens qui viennent pour travailler, "
              "il supprime l'argument de l'« appel d'air » social, et il "
              "protège le consentement à l'impôt — sans lequel aucune politique "
              "migratoire ouverte ne tient politiquement. Il a une "
              "contrepartie que nous assumons : pendant cinq ans, un "
              "travailleur étranger cotise et ne reçoit pas tout. C'est un "
              "marché explicite, écrit dans la loi, et connu avant de "
              "venir — ce que le système actuel ne fait pas.</p>",
        source="M. Friedman, conférence de 1978 ; la règle proposée est "
               "voisine de celles en vigueur dans plusieurs pays d'accueil.")

    corps += """
<h2 id="six">6. Zéro file d'attente : le rendez-vous est un droit</h2>
<p><strong>Ce qui change.</strong> Toute démarche déposable en ligne de bout en
bout, avec accusé de réception horodaté valant preuve de dépôt. Quand la
présence physique est nécessaire, un rendez-vous garanti sous quinze jours,
à défaut de quoi le dossier est réputé déposé à la date de la demande de
rendez-vous. Gratuité des renouvellements, et taxes de première délivrance
alignées sur le coût réel du traitement.</p>
<p><strong>Ce qu'on y gagne.</strong> L'essentiel du contentieux des étrangers
— environ quatre affaires sur dix devant les tribunaux administratifs — porte
sur la procédure, pas sur le fond. Le supprimer rend au juge administratif le
temps qu'il doit à l'urbanisme, à la fiscalité et à la fonction publique, et
rend aux préfectures des agents aujourd'hui occupés à gérer une pénurie de
rendez-vous qu'elles ont elles-mêmes créée.</p>
"""

    corps += """
<h2 id="controle">Ce qu'on contrôle vraiment, et mieux</h2>
<p>Ouvrir le travail n'est pas renoncer au contrôle : c'est le concentrer là
où il protège quelqu'un. Une administration qui cesse d'instruire des
autorisations de travail et des renouvellements annuels peut enfin faire ce
qu'elle seule doit faire.</p>
"""

    corps += g.points([
        ("Identité et documents",
         "Vérification systématique, et poursuite réelle de la fraude "
         "documentaire — qui est aujourd'hui noyée dans la masse."),
        ("Casier judiciaire et ordre public",
         "Consultation systématique à l'entrée et à chaque renouvellement ; "
         "refus et retrait de titre en cas de condamnation grave."),
        ("Éloignement effectif",
         "Moins de décisions, mieux exécutées : les moyens vont aux "
         "étrangers condamnés et aux menaces avérées, et la négociation des "
         "laissez-passer consulaires devient une priorité diplomatique."),
        ("Travail dissimulé",
         "Contrôles renforcés chez les employeurs : quand le travail légal "
         "devient simple, employer au noir n'a plus d'excuse et le sanctionner "
         "n'a plus de victime collatérale."),
    ])

    corps += g.note(
        "<p><strong>Ce que ce programme ne propose pas.</strong> Ni "
        "suppression des frontières, ni accès inconditionnel de tous au "
        "territoire, ni sortie de la Convention européenne des droits de "
        "l'homme, ni régularisation générale et sans conditions. Chacun de ces "
        "mots revient dans le débat public ; aucun ne décrit ce qui est écrit "
        "ci-dessus.</p>", "avertissement")

    corps += """
<h2 id="calendrier">Calendrier, coût, et ce qui se finance tout seul</h2>
"""

    corps += g.tableau(
        ["Échéance", "Ce qui entre en vigueur", "Ce que ça suppose"],
        [["Immédiat, par décret",
          "Délais opposables et silence valant accord ; rendez-vous garanti ; "
          "gratuité des renouvellements",
          "Aucune loi : ce sont des dispositions réglementaires"],
         ["Loi, première année",
          "Suppression de l'autorisation de travail et de l'opposabilité de la "
          "situation de l'emploi ; titre pluriannuel de quatre ans",
          "Une loi courte, sur un seul sujet, qui abroge plus qu'elle "
          "n'ajoute"],
         ["Loi, première année",
          "Délai de cinq ans pour les prestations non contributives",
          "Le point juridiquement le plus délicat : à rédiger en tenant compte "
          "du principe d'égalité et des engagements européens"],
         ["Deux ans",
          "Asile en trois mois recours compris",
          "Redéploiement de moyens vers l'OFPRA et la CNDA, et réforme de "
          "leur procédure"]],
        legende="Ordre de marche proposé. Deux mesures sur quatre ne "
                "demandent aucune loi.",
        classes_colonnes=["texte", "long", "long"])

    corps += g.note(
        "<p><strong>Le coût net est probablement négatif — au sens où l'on "
        "dépense moins.</strong> On cesse de financer l'attente (hébergement "
        "et allocation de demandeurs d'asile qui n'ont pas le droit de "
        "travailler), on supprime l'instruction de centaines de milliers "
        "d'actes devenus inutiles, on vide une grande partie du contentieux "
        "administratif, et l'on encaisse les cotisations de travailleurs "
        "aujourd'hui dissimulés. En face, il faut payer des juges et des "
        "officiers de protection supplémentaires pendant la montée en charge, "
        "et assumer que le délai de cinq ans sur les prestations ne "
        "s'applique qu'aux nouveaux entrants.</p>")

    corps += """
<div class="actions">
  <a class="bouton" href="parcours.html">Voir ce que ça change, cas par cas</a>
  <a href="objections.html">Les objections</a>
</div>
"""
    return corps
