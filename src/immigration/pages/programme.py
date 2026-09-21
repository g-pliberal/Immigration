"""Le programme : les sept engagements, article par article.

Cette page a été refondue après une relecture adverse du programme — celle
qu'un contradicteur compétent aurait faite, et qu'il vaut mieux se faire à
soi-même. Trois changements portent l'essentiel :

* l'engagement 5 ne crée plus de délai de carence, parce que celui qui était
  proposé — cinq ans de résidence pour les prestations non contributives —
  a été jugé contraire à la Constitution le 11 avril 2024 ;
* l'engagement 4 promet un calendrier en deux temps, opposable, au lieu d'un
  « trois mois » qu'aucun pays comparable n'atteint et que le règlement
  européen ne laisse pas décider seul ;
* un septième engagement répond à la question que les six premiers
  laissaient sans réponse : qui décide, et à quoi verrait-on que nous nous
  sommes trompés.
"""

from __future__ import annotations

from .. import gabarit as g
from .accueil import ENGAGEMENTS

PAGE = {
    "fichier": "programme.html",
    "titre": "Le programme libéral pour l'immigration",
    "description": (
        "Sept engagements : un titre unique valant autorisation de travail, "
        "des délais opposables, un titre pluriannuel, l'asile jugé vite, "
        "aucune carence sociale nouvelle, zéro file d'attente, et un "
        "réexamen annuel devant le Parlement."),
}


def construire() -> str:
    corps = g.affiche(
        "La proposition",
        "Ouvrir le travail, <span class=\"serif\">tenir les délais</span>",
        "Sept engagements, chacun avec le texte qu'il faut changer, ce qu'il "
        "coûte, ce qu'on peut en attendre — et ce qui nous donnerait tort. "
        "Rien ici ne demande de sortir d'un traité, ni de réviser la "
        "Constitution.")

    corps += g.engagements(ENGAGEMENTS)

    corps += g.plan([
        ("un", "1. Un titre qui vaut travail"),
        ("deux", "2. Des délais opposables"),
        ("trois", "3. Le titre pluriannuel"),
        ("quatre", "4. L'asile en six mois"),
        ("cinq", "5. Aucune carence nouvelle"),
        ("six", "6. Zéro file d'attente"),
        ("sept", "7. Rendre des comptes"),
        ("controle", "Ce qu'on contrôle vraiment"),
        ("perimetre", "Ce que ce programme ne traite pas"),
        ("calendrier", "Calendrier"),
        ("chiffrage", "Chiffrage"),
    ])

    # ----------------------------------------------------------------- 1
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
         ["CESEDA, art. L. 435-4",
          "Régularisation « métiers en tension », discrétionnaire — et "
          "<strong>expire le 31 décembre 2026</strong>",
          "Remplacé par un droit sur critères, permanent et opposable"],
         ["CESEDA, admission exceptionnelle au séjour",
          "Régularisation discrétionnaire, au cas par cas : 28 610 décisions "
          "l'an dernier, en baisse de 10 %" + g.renvoi("regularisations"),
          "Remplacée par un droit sur critères : douze mois de présence, six "
          "mois de travail, identité établie, casier vérifié"]],
        legende="Les quatre textes qui portent l'essentiel de l'engagement 1.",
        classes_colonnes=["texte", "long", "long"])

    corps += g.cle(
        "Disons-le nous-mêmes : oui, c'est une voie de régularisation permanente",
        "Nous avons d'abord écrit « ce n'est pas une régularisation "
        "générale ». C'est exact et c'est insuffisant : un droit sur critères, "
        "ouvert en permanence, est <strong>plus</strong> puissant qu'une "
        "circulaire de régularisation, pas moins. Autant l'assumer.",
        corps="<p>Ce qu'il faut comparer, ce n'est pas « régulariser ou "
              "non » — la France régularise déjà, 28 610 fois l'an dernier, "
              "et régularisera encore. C'est <em>comment</em>. Aujourd'hui : "
              "un pouvoir discrétionnaire, des critères de circulaire "
              "opposables à personne, des réponses qui varient d'une "
              "préfecture à l'autre pour un dossier identique, et un "
              "dispositif légal qui expire dans quelques semaines. Demain : "
              "des conditions écrites dans la loi, vérifiables, refusables et "
              "contestables devant un juge.</p>"
              "<p><strong>Les critères, chiffrés</strong>, parce qu'un "
              "critère sans chiffre est une promesse sans contenu : douze "
              "mois de présence en France, six mois d'activité sur les douze "
              "derniers, identité établie, casier vérifié, employeur "
              "identifié. C'est plus ouvert que l'article L. 435-4 actuel "
              "(trois ans de présence, douze mois de travail sur "
              "vingt-quatre), et nous ne le cachons pas : c'est le "
              "point du programme sur lequel un adversaire a le plus de "
              "prise, et celui que le septième engagement met sous "
              "surveillance annuelle.</p>",
        identifiant="regularisation")

    corps += g.cle(
        "Le trou logique qu'il fallait boucher : comment prouver un travail interdit ?",
        "Un étranger en situation irrégulière ne peut pas produire un "
        "« emploi déclaré » : son employeur commettrait un délit en "
        "l'attestant. Le critère présupposait l'infraction qu'il devait "
        "résoudre.",
        corps="<p>Deux dispositions le règlent. D'abord, <strong>la preuve du "
              "travail se fait par faisceau d'indices</strong> — bulletins de "
              "paie même établis sous une autre identité, virements, "
              "attestations de collègues, plannings, badges —, comme le juge "
              "administratif l'admet déjà dans le contentieux de l'admission "
              "exceptionnelle. Le salarié n'a pas à obtenir la signature de "
              "celui qui a intérêt à la refuser.</p>"
              "<p>Ensuite, <strong>l'employeur qui régularise n'est pas "
              "poursuivi pour la période antérieure s'il déclare et paie les "
              "cotisations dues</strong> ; celui qui refuse de déclarer "
              "encourt les sanctions renforcées du travail dissimulé. "
              "L'incitation est inversée : aujourd'hui, le silence protège "
              "l'employeur ; demain, il l'expose. C'est une amnistie de "
              "cotisations, limitée et conditionnelle — nous préférons "
              "l'appeler par son nom plutôt que de la laisser découvrir.</p>",
        identifiant="preuve")

    corps += g.note(
        "<p><strong>Ce n'est pas une régularisation inconditionnelle.</strong> "
        "Identité non établie, casier chargé, fraude documentaire, refus de "
        "déclarer l'emploi restent des motifs de refus — et le deviennent "
        "réellement, puisque l'administration n'a plus à consacrer son temps "
        "à des dossiers que rien ne justifiait d'examiner.</p>", "vigilance")

    # ----------------------------------------------------------------- 2
    corps += """
<h2 id="deux">2. Un délai opposable, et le silence vaut accord</h2>
<p><strong>Ce qui change.</strong> Huit semaines pour instruire une première
demande de titre de travail ou d'études, quatre semaines pour un
renouvellement. Passé ce délai sans décision motivée notifiée, le titre est
réputé délivré, et l'administration délivre le document matériel sur simple
demande.</p>
<p>C'est la règle de droit commun française depuis la loi du 12 novembre 2013 —
le silence de l'administration vaut acceptation — dont le droit des étrangers
est l'une des principales exceptions. C'est aussi, en plus strict, ce que la
directive européenne sur le permis unique impose déjà : quatre mois pour
statuer. Nous proposons huit semaines. Le préfet conserve tous ses pouvoirs de
refus : il doit seulement les exercer dans un délai.</p>
"""

    corps += g.cle(
        "Et si le silence délivre un titre à quelqu'un de dangereux ?",
        "L'objection est bonne, et le programme n'y répondait pas. Elle se "
        "règle par une soupape écrite : <strong>un signalement d'ordre public "
        "suspend le délai</strong>, et ne l'éteint pas.",
        corps="<p>Trois garde-fous, qui n'existent pas dans un « silence vaut "
              "accord » nu. <strong>Un</strong> : la consultation des "
              "fichiers d'antécédents et du casier est faite à "
              "l'enregistrement, pas à la fin ; tant qu'elle n'est pas "
              "revenue, le délai ne court pas. <strong>Deux</strong> : un "
              "signalement motivé de l'autorité compétente suspend le délai "
              "pour une durée bornée et renouvelable une fois, mentionnée au "
              "dossier. <strong>Trois</strong> : un titre né du silence est "
              "retirable <em>ab initio</em> en cas de fraude ou de "
              "dissimulation, comme tout acte obtenu par fraude.</p>"
              "<p>Le droit administratif français prévoit déjà des exceptions "
              "au silence valant accord pour les décisions touchant à l'ordre "
              "public : nous les utilisons plutôt que de prétendre qu'elles "
              "n'existent pas.</p>",
        identifiant="soupape")

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

    # ----------------------------------------------------------------- 3
    corps += """
<h2 id="trois">3. Un titre pluriannuel dès la première délivrance</h2>
<p><strong>Ce qui change.</strong> Quatre ans pour le travail et les études dès
le premier titre, renouvelable en ligne sans présence physique quand rien n'a
changé. Dix ans — la carte de résident — après cinq ans de séjour régulier,
sur critères objectifs. Le titre n'est plus attaché à un employeur : il suit la
personne.</p>
<p><strong>Pourquoi.</strong> Parce que le renouvellement annuel est la
principale cause d'engorgement des préfectures. Le chiffre est sans appel :
<strong class="cle-texte">955 080 titres renouvelés l'an dernier contre 384 230
premiers titres</strong> — deux fois et demie plus de dossiers de gens déjà là,
déjà en règle, que de nouvelles arrivées.
"""
    corps += g.renvoi("renouvellements")
    corps += """ Et parce qu'un salarié dont le séjour dépend de son patron ne
négocie pas son salaire : rendre le titre portable, c'est retirer aux
employeurs indélicats un moyen de pression que la loi leur donne
aujourd'hui.</p>
"""

    corps += g.cle(
        "Et si la personne perd son emploi ?",
        "Le titre ne tombe pas avec le contrat : <strong>il reste valide douze "
        "mois</strong> pour retrouver un emploi, une fois par période de "
        "quatre ans.",
        corps="<p>C'est la question que tout système de permis de travail doit "
              "trancher, et que le programme laissait en blanc. Un titre qui "
              "s'éteint au premier licenciement rend le salarié captif — "
              "exactement ce que l'engagement prétend corriger. Un titre qui "
              "survit indéfiniment sans emploi transforme une immigration de "
              "travail en autre chose, et l'objection serait juste.</p>"
              "<p>Douze mois, donc : la durée d'indemnisation de droit commun, "
              "pour ne pas inventer une règle de plus. Pendant cette période, "
              "le titulaire cherche un emploi dans les mêmes conditions qu'un "
              "résident et perçoit, le cas échéant, l'assurance chômage qu'il "
              "a cotisée — un droit acheté, pas une aide.</p>",
        identifiant="perte-emploi")

    # ----------------------------------------------------------------- 4
    corps += """
<h2 id="quatre">4. L'asile jugé vite, travail autorisé dès le dépôt</h2>
<p><strong>Ce qui change.</strong> Le droit de travailler ouvert dès
l'enregistrement de la demande, et non après six mois. Un délai d'instruction
opposable à l'administration. En contrepartie, l'exécution effective des
décisions définitives de rejet.</p>
<p><strong>Et une promesse revue à la baisse, assumée.</strong> Ce programme
annonçait « trois mois recours compris ». Aucun pays comparable n'y parvient,
la seule notification et le délai de recours en consomment une part, et le
règlement européen applicable depuis juin 2026 fixe désormais ses propres
bornes. Promettre un chiffre intenable, c'est offrir la réplique. Nous
proposons donc un calendrier en deux temps, chacun opposable :</p>
"""

    corps += g.tableau(
        ["Échéance", "Délai opposable, recours compris", "Ce que cela suppose"],
        [["Deux ans après l'entrée en vigueur", "<strong>6 mois</strong>",
          "Montée en charge de l'OFPRA et de la CNDA, juge unique généralisé "
          "pour les demandes manifestement fondées comme manifestement "
          "infondées"],
         ["Au terme de la montée en charge", "<strong>3 mois</strong>",
          "Objectif maintenu, mais comme cible d'un délai déjà tenu à six "
          "mois — pas comme promesse de campagne"]],
        legende="Le calendrier de l'asile, revu après confrontation au droit "
                "européen et aux délais réellement atteints ailleurs.",
        classes_colonnes=["texte", "nombre", "long"])

    corps += g.note(
        "<p><strong>Le droit d'asile n'est pas négociable, et il n'est pas une "
        "politique migratoire.</strong> Il découle de la Constitution, de la "
        "Convention de Genève et désormais du pacte européen. Le rendre "
        "rapide, c'est le rendre crédible : une protection accordée en six "
        "mois vaut mieux qu'une protection accordée en deux ans — et c'est "
        "désormais <strong>plus d'un demandeur sur deux</strong> qui l'obtient"
        + g.renvoi("asile-protection") + ". Un refus prononcé en six mois "
        "s'exécute ; un refus prononcé après deux ans de vie installée ne "
        "s'exécute plus.</p>")

    # ----------------------------------------------------------------- 5
    corps += """
<h2 id="cinq">5. Aucun nouveau délai de carence</h2>
<p><strong>Ce que nous proposions, et pourquoi nous ne le proposons plus.</strong>
Ce programme annonçait l'ouverture des prestations non contributives après
<em>cinq ans de résidence régulière</em>. Cette mesure est contraire à la
Constitution, et il ne sert à rien de le découvrir en campagne : le Conseil
constitutionnel a jugé, le <strong>11 avril 2024</strong>, qu'une condition de
cinq ans de résidence pour l'accès des étrangers en séjour régulier aux
prestations sociales portait une <strong>« atteinte disproportionnée »</strong>
aux exigences des dixième et onzième alinéas du Préambule de 1946. Sur le fond,
pas sur la procédure.</p>
<p><strong>Ce que nous proposons à la place.</strong> Rien de nouveau — et
c'est le point. La France applique déjà des conditions de durée là où le
législateur a jugé qu'elles se justifiaient : cinq ans de séjour régulier
autorisant à travailler pour le RSA, dix ans pour l'allocation de solidarité
aux personnes âgées. Nous les maintenons, nous les écrivons clairement, et
nous refusons d'en créer d'autres. Le travail ouvre immédiatement les droits
qu'il finance.</p>
"""

    corps += g.tableau(
        ["Prestation", "Nature", "Aujourd'hui", "Avec le programme"],
        [["Assurance maladie", "Contributive",
          "Ouverte au titre de l'activité",
          "<strong>Inchangé</strong> — ouverte dès le premier jour de travail "
          "déclaré"],
         ["Retraite, chômage, indemnités journalières", "Contributives",
          "Dues au titre des cotisations versées",
          "<strong>Inchangé</strong> : un droit acheté n'est pas une aide"],
         ["Prestations familiales", "Non contributive",
          "Séjour régulier, sans condition de durée",
          "<strong>Inchangé</strong> — la CJUE a condamné la France le "
          "19 décembre 2024 sur une condition voisine"],
         ["Aide au logement (APL)", "Non contributive",
          "Séjour régulier, sans condition de durée générale",
          "<strong>Inchangé</strong> — expressément visé par la censure "
          "d'avril 2024"],
         ["RSA", "Non contributive",
          "<strong>5 ans</strong> de séjour régulier autorisant à travailler "
          "(art. L. 262-4 CASF), avec exceptions",
          "Inchangé, exceptions comprises"],
         ["Allocation de solidarité aux personnes âgées", "Non contributive",
          "<strong>10 ans</strong> de séjour régulier",
          "Inchangé"],
         ["Allocation pour demandeur d'asile", "Spécifique à l'asile",
          "Versée pendant la procédure, 204 € par mois",
          "Dépense réduite <em>mécaniquement</em> : le droit de travailler "
          "dès le dépôt et l'instruction en six mois raccourcissent "
          "l'attente"],
         ["Aide médicale de l'État", "Soins des personnes irrégulières",
          "≈ 480 000 bénéficiaires, 1,39 Md€" + g.renvoi("ame"),
          "Périmètre réduit <em>mécaniquement</em> : un travailleur régularisé "
          "relève de l'assurance maladie qu'il finance"]],
        legende="Prestation par prestation, parce qu'un programme qui parle "
                "de « prestations non contributives » en bloc se fait "
                "démonter ligne par ligne. La frontière contributif / non "
                "contributif ne recoupe pas celle du financement : les "
                "prestations familiales sont financées par cotisations et "
                "restent juridiquement non contributives.",
        classes_colonnes=["texte", "texte", "long", "long"])

    corps += g.cle(
        "Alors que devient l'objection de Milton Friedman ?",
        "Elle tient toujours — « on ne peut pas avoir à la fois des frontières "
        "ouvertes et un État-providence illimité » — et notre réponse change "
        "de nature : <strong>ce n'est pas l'aide qu'on ferme, c'est le "
        "travail qu'on ouvre</strong>.",
        corps="<p>La voie que ce programme ouvre exige un contrat de travail "
              "ou une promesse d'embauche. Elle n'est, par construction, pas "
              "plus attirante pour qui vient sans projet de travail : c'est "
              "la condition d'entrée elle-même, et non une carence ajoutée "
              "après coup, qui fait le tri. Un travailleur déclaré cotise dès "
              "le premier mois et finance les droits qu'il reçoit ; les "
              "prestations de solidarité restent soumises aux durées que le "
              "législateur a déjà fixées et que le juge a déjà validées.</p>"
              "<p><strong>Trois verrous</strong> interdisaient la version "
              "précédente, et il faut les connaître avant de proposer quoi "
              "que ce soit dans ce domaine : la Constitution (décision "
              "n° 2024-6 RIP) ; le droit de l'Union, où la directive 2011/98 "
              "garantit l'égalité de traitement en matière de sécurité "
              "sociale aux titulaires du permis unique, et où la CJUE censure "
              "régulièrement les discriminations indirectes ; et les "
              "trente-neuf conventions bilatérales de sécurité sociale "
              "conclues par la France, qui comportent une clause d'égalité de "
              "traitement.</p>"
              "<p>Nous avons donc changé d'avis sur ce point, et nous le "
              "disons à l'endroit où le lecteur le cherchera. Un programme "
              "qui ne corrige jamais rien n'a pas été relu.</p>",
        source="Conseil constitutionnel, décision n° 2024-6 RIP du 11 avril "
               "2024 ; CJUE, 19 décembre 2024, C-664/23 ; directive 2011/98/UE, "
               "art. 12 ; Sénat, rapport sur la proposition de loi créant une "
               "condition de durée de résidence.",
        identifiant="friedman")

    corps += g.note(
        "<p><strong>Ce que cela coûte à notre argumentaire, et nous "
        "l'assumons.</strong> La version précédente offrait une réponse "
        "spectaculaire à l'accusation d'« appel d'air social ». Celle-ci est "
        "plus faible rhétoriquement et plus solide juridiquement. Nous "
        "préférons un engagement qui survivra au Conseil constitutionnel à un "
        "engagement qui fait de l'effet en meeting et tombe en janvier.</p>",
        "vigilance")

    # ----------------------------------------------------------------- 6
    corps += """
<h2 id="six">6. Zéro file d'attente : le rendez-vous est un droit</h2>
<p><strong>Ce qui change.</strong> Toute démarche déposable en ligne, avec
accusé de réception horodaté valant preuve de dépôt. Un rendez-vous garanti
sous quinze jours, à défaut de quoi le dossier est réputé déposé à la date de
la demande de rendez-vous. Gratuité des renouvellements, et taxes de première
délivrance alignées sur le coût réel du traitement.</p>
<p><strong>Et un guichet, toujours.</strong> Ce programme proposait des
démarches « en ligne de bout en bout » tout en citant à l'appui le Défenseur
des droits — dont les rapports dénoncent précisément la dématérialisation
intégrale. L'incohérence était à nous, pas à lui. Le Conseil d'État juge depuis
le 3 juin 2022 qu'une procédure entièrement dématérialisée doit comporter une
solution de substitution : nous l'inscrivons au programme. En ligne par défaut,
guichet physique garanti pour qui ne peut pas ou ne veut pas, sans avoir à se
justifier.</p>
<p><strong>Ce qu'on y gagne.</strong> Une part réelle du contentieux des
étrangers disparaît : les référés pour obtenir un rendez-vous, les recours
contre les refus implicites nés du silence, les ruptures de droits dues à un
renouvellement tardif. Nous ne revendiquons pas la moitié du rôle des tribunaux
administratifs — cette moitié est faite pour l'essentiel de recours au fond
contre des refus et des OQTF, qui subsisteront.
"""
    corps += g.renvoi("contentieux-ta")
    corps += "</p>"

    # ----------------------------------------------------------------- 7
    corps += """
<h2 id="sept">7. Rendre des comptes : ce qui nous donnerait tort</h2>
<p>Nous refusons les quotas, et pour de bonnes raisons : ils ne s'appliquent ni
à l'asile, ni aux Européens, ni aux liens familiaux protégés, le Conseil
constitutionnel les a censurés en 2024, et un plafond épuisé ne se conteste pas
devant un juge. Mais refuser les quotas ne dispense pas de répondre à la
question qu'ils posent, et qui est légitime : <strong>qui décide, et comment le
Parlement reprend-il la main ?</strong></p>
<p><strong>Ce qui change.</strong> Un rapport annuel public et un débat
obligatoire au Parlement sur des indicateurs publiés à l'avance. Les critères
de l'engagement 1 — durée de présence, durée d'activité, seuils de
rémunération — sont fixés par la loi et révisables par elle, chaque année, à la
hausse comme à la baisse. Ce n'est pas un plafond de volume : c'est un réglage
de conditions, qui reste contestable devant un juge.</p>
"""

    corps += g.gestes([
        "<strong>Le taux d'emploi ne décolle pas.</strong> Si, trois ans après "
        "l'entrée en vigueur, le taux d'emploi à vingt-quatre mois des "
        "personnes entrées sous le nouveau régime n'excède pas celui de la "
        "cohorte entrée sous l'ancien, la réforme n'a pas produit l'effet qui "
        "la justifie. Indicateur : INSEE et DARES, cohortes suivies.",
        "<strong>L'administration ne suit pas.</strong> Si le délai médian "
        "d'instruction dépasse huit semaines deux années de suite, ou si plus "
        "de 5 % des titres sont délivrés par le silence plutôt que par une "
        "décision, l'engagement 2 est devenu une fiction : il faut des moyens, "
        "ou un délai révisé, et le dire.",
        "<strong>L'absorption ne suit pas.</strong> Si, dans les dix "
        "agglomérations les plus tendues, les loyers de marché progressent de "
        "plus de trois points au-dessus de l'inflation trois années de suite "
        "sans que l'offre de logement ait répondu, les critères d'entrée sont "
        "resserrés le temps que la construction rattrape.",
    ])

    corps += g.note(
        "<p><strong>Pourquoi écrire d'avance ce qui nous donnerait "
        "tort.</strong> Parce qu'un programme dont aucun résultat ne pourrait "
        "démentir les promesses n'est pas un programme, c'est une profession "
        "de foi — et parce que nos adversaires nous demanderont, à juste "
        "titre, ce que nous ferions si nous avions tort. Mieux vaut avoir "
        "répondu avant qu'ils ne posent la question.</p>", "resume")

    # ---------------------------------------------------------- contrôle
    corps += """
<h2 id="controle">Ce qu'on contrôle vraiment, et mieux</h2>
<p>Ouvrir le travail n'est pas renoncer au contrôle : c'est le concentrer là
où il protège quelqu'un. Une administration qui cesse d'instruire des
autorisations de travail et six cent mille renouvellements annuels peut enfin
faire ce qu'elle seule doit faire.</p>
"""

    corps += g.points([
        ("Identité et documents",
         "Vérification systématique à l'enregistrement — le pacte européen "
         "l'impose désormais aux frontières extérieures — et poursuite réelle "
         "de la fraude documentaire, aujourd'hui noyée dans la masse."),
        ("Casier judiciaire et ordre public",
         "Consultation systématique à l'entrée et à chaque renouvellement ; "
         "refus et retrait de titre en cas de condamnation grave ; "
         "suspension du délai de l'engagement 2 en cas de signalement."),
        ("Éloignement effectif",
         "Moins de décisions, mieux exécutées : les moyens vont aux étrangers "
         "condamnés et aux menaces avérées. C'est une dépense, pas une "
         "économie — plus de 4 500 € par éloignement forcé, hors rétention — "
         "et notre chiffrage l'inscrit." + g.renvoi("cout-eloignement")),
        ("Travail dissimulé",
         "Contrôles renforcés chez les employeurs : quand le travail légal "
         "devient simple, employer au noir n'a plus d'excuse et le sanctionner "
         "n'a plus de victime collatérale."),
    ])

    # --------------------------------------------------------- périmètre
    corps += """
<h2 id="perimetre">Ce que ce programme ne traite pas, et pourquoi</h2>
<p>Un programme qui se tait sur un sujet prend position par son silence. Voici
donc les sujets que nous ne traitons pas, et ce que ce silence signifie —
plutôt que de laisser un contradicteur le remplir à notre place.</p>
"""

    corps += g.tableau(
        ["Sujet", "Poids réel", "Notre position"],
        [["Immigration familiale",
          "≈ 90 000 premiers titres par an, soit près d'un quart",
          "<strong>Inchangée.</strong> Le droit de vivre en famille est "
          "protégé par la Constitution et par l'article 8 de la Convention "
          "européenne des droits de l'homme ; le durcissement voté en 2024 a "
          "été censuré. Nous n'avons pas de réforme à proposer ici, et nous "
          "ne feignons pas d'en avoir une"],
         ["Accès à la nationalité",
          "Un tiers des immigrés sont devenus français"
          + g.renvoi("immigres-francais"),
          "<strong>Hors périmètre.</strong> La nationalité relève de la "
          "citoyenneté, non de la politique migratoire. Nous refusons de nous "
          "en servir comme d'un levier de régulation des flux, dans un sens "
          "ou dans l'autre"],
         ["Outre-mer, et Mayotte en particulier",
          "Régime dérogatoire au CESEDA, situation sans comparaison en "
          "métropole",
          "<strong>Ce programme n'y est pas applicable tel quel</strong>, et "
          "le prétendre serait malhonnête. Une déclinaison séparée est "
          "nécessaire ; elle n'est pas écrite, et nous ne la ferons pas "
          "passer pour un détail d'application"],
         ["Mineurs non accompagnés",
          "Compétence des départements",
          "<strong>Relèvent de la protection de l'enfance</strong>, pas du "
          "droit des étrangers. Le programme ne change rien à leur régime et "
          "ne propose pas de l'y ramener"],
         ["Visas de court séjour, frontières extérieures",
          "Compétence européenne",
          "<strong>Non modifiables par une loi française.</strong> Le code "
          "des visas et le pacte européen s'imposent : c'est pourquoi l'étape "
          "consulaire subsiste dans nos parcours comparés"],
         ["Travail détaché",
          "Directive européenne, concurrence entre employeurs européens",
          "<strong>Sujet distinct.</strong> Un salarié détaché n'immigre pas ; "
          "confondre les deux débats arrange ceux qui veulent brouiller "
          "l'un par l'autre"]],
        legende="Les sujets hors périmètre. Quatre sur six échappent au "
                "législateur national ; les deux autres appellent un travail "
                "que nous n'avons pas fait.",
        classes_colonnes=["texte", "texte", "long"])

    corps += g.note(
        "<p><strong>Ce que ce programme ne propose pas.</strong> Ni "
        "suppression des frontières, ni accès inconditionnel de tous au "
        "territoire, ni sortie de la Convention européenne des droits de "
        "l'homme, ni régularisation générale et sans conditions, ni "
        "suppression de l'aide médicale de l'État. Chacun de ces mots revient "
        "dans le débat public ; aucun ne décrit ce qui est écrit ci-dessus. "
        "Et la limite que nous nous fixons est écrite noir sur blanc dans "
        "<a href=\"index.html#limites\">« pourquoi pas les frontières "
        "ouvertes »</a>.</p>", "avertissement")

    # -------------------------------------------------------- calendrier
    corps += """
<h2 id="calendrier">Calendrier, et ce qui relève de qui</h2>
"""

    corps += g.tableau(
        ["Échéance", "Ce qui entre en vigueur", "Norme concernée"],
        [["Immédiat, par décret",
          "Délais opposables et silence valant accord ; rendez-vous garanti "
          "sous quinze jours ; guichet physique de substitution ; gratuité "
          "des renouvellements",
          "Réglementaire. Compatible avec la directive 2011/98, qui impose "
          "déjà quatre mois"],
         ["Loi, première année",
          "Suppression de l'autorisation de travail et de l'opposabilité de "
          "la situation de l'emploi ; titre pluriannuel de quatre ans ; "
          "survie du titre douze mois après la perte d'emploi",
          "Loi nationale. Une loi courte, sur un seul sujet, qui abroge plus "
          "qu'elle n'ajoute"],
         ["Loi, première année",
          "Droit au séjour sur critères remplaçant l'admission "
          "exceptionnelle, avant l'expiration de l'article L. 435-4 le "
          "31 décembre 2026",
          "Loi nationale. Échéance contrainte : sans texte, retour au pur "
          "pouvoir discrétionnaire"],
         ["Loi, première année",
          "Débat annuel, indicateurs publiés, critères révisables",
          "Loi organique ou ordinaire selon le véhicule retenu"],
         ["Deux ans",
          "Asile jugé en six mois recours compris, puis trois mois à terme",
          "Articulé au règlement européen applicable depuis le 12 juin 2026 — "
          "et non contre lui"]],
        legende="Ordre de marche proposé. Rien n'exige de réviser la "
                "Constitution ni de dénoncer un traité ; c'est la contrainte "
                "que nous nous sommes donnée, et elle a coûté un "
                "engagement.",
        classes_colonnes=["texte", "long", "long"])

    # --------------------------------------------------------- chiffrage
    corps += """
<h2 id="chiffrage">Chiffrage : ce que cela coûte, ce que cela rapporte</h2>
<p>Ce programme affirmait que « le coût net est probablement négatif » sans
avancer un seul euro — dans un site dont la méthode affichée est « un chiffre,
une source, un millésime ». L'incohérence était la plus visible de toutes.
Voici donc un chiffrage, avec ses hypothèses, ses fourchettes et ce qu'il ne
sait pas faire.</p>
"""

    corps += g.tableau(
        ["Poste", "Sens", "Ordre de grandeur annuel", "Hypothèse retenue"],
        [["Allocation et hébergement des demandeurs d'asile",
          "Économie",
          "<strong>0,3 à 0,6 Md€</strong>",
          "L'allocation pèse 299 M€ et l'hébergement l'essentiel du reste de "
          "la mission de 2,16 Md€. Instruire en six mois au lieu de dix-huit "
          "réduit la durée moyenne indemnisée d'environ deux tiers ; le droit "
          "de travailler dès le dépôt en sort une partie du dispositif"
          + g.renvoi("ada-credits")],
         ["Instruction des renouvellements",
          "Économie",
          "<strong>600 000 à 700 000 dossiers de moins</strong>",
          "Conséquence arithmétique du titre de quatre ans appliqué aux "
          "955 080 renouvellements annuels. Nous donnons le volume et non un "
          "montant : le coût unitaire d'instruction n'est pas publié"
          + g.renvoi("renouvellements")],
         ["Autorisations de travail supprimées",
          "Économie",
          "Non chiffrable publiquement",
          "L'acte disparaît, mais aucune publication ne donne son coût "
          "d'instruction. Nous préférons l'écrire que d'inventer un chiffre"],
         ["Contentieux de procédure évité",
          "Économie",
          "Part minoritaire du contentieux des étrangers",
          "Référés rendez-vous, refus implicites, ruptures de droits. Nous ne "
          "revendiquons pas les 50 % du rôle des tribunaux : l'essentiel est "
          "du contentieux au fond, qui subsiste"],
         ["Cotisations sur du travail aujourd'hui dissimulé",
          "Recette",
          "Non chiffrable honnêtement",
          "Aucune statistique ne dénombre la population concernée. Tout "
          "chiffre avancé ici serait une extrapolation déguisée"],
         ["Officiers de protection et magistrats",
          "<strong>Dépense</strong>",
          "Dépense immédiate et durable",
          "C'est le prix de l'engagement 4. Il précède les économies qu'il "
          "produit"],
         ["Éloignements effectifs supplémentaires",
          "<strong>Dépense</strong>",
          "<strong>40 à 150 M€</strong>",
          "Plus de 4 500 € par éloignement forcé, et environ 16 000 € par "
          "personne retenue pour vingt-sept jours. Promettre plus "
          "d'éloignements, c'est promettre une dépense"
          + g.renvoi("cout-eloignement")],
         ["Indemnisation des délais dépassés",
          "<strong>Dépense</strong>",
          "Décroissante par construction",
          "Élevée la première année, nulle si l'engagement 2 est tenu. C'est "
          "le but : une dépense qui mesure notre propre échec"],
         ["Guichets physiques de substitution",
          "<strong>Dépense</strong>",
          "Modérée",
          "Compensée par la chute du volume de dossiers, mais réelle : un "
          "guichet garanti se paie"]],
        legende="Chiffrage par poste. Les fourchettes sont larges parce que "
                "les incertitudes le sont ; un chiffre unique serait plus "
                "convaincant et moins vrai.",
        classes_colonnes=["texte", "texte", "nombre", "long"])

    corps += g.cle(
        "Le point faible de ce chiffrage, et il faut le connaître",
        "<strong>Les dépenses sont immédiates, les économies sont "
        "différées.</strong> Recruter des magistrats coûte la première année ; "
        "le titre de quatre ans ne vide les files qu'à partir de la deuxième ; "
        "l'effet sur l'emploi et les cotisations se mesure sur une cohorte, "
        "donc sur plusieurs années.",
        corps="<p>Notre conclusion est donc plus prudente que la précédente : "
              "le solde est <strong>négatif les deux premières années</strong> "
              "— l'État dépense plus qu'il n'économise — et probablement "
              "positif ensuite. Dire « le coût net est négatif » sans "
              "préciser l'horizon était une facilité, et un adversaire "
              "attentif l'aurait relevée avant nous.</p>"
              "<p>Une réforme qui coûte deux ans avant de rapporter est "
              "défendable. Une réforme dont on cache qu'elle coûte deux ans "
              "ne l'est pas longtemps.</p>",
        identifiant="decalage")

    corps += """
<div class="actions">
  <a class="bouton" href="parcours.html">Voir ce que ça change, cas par cas</a>
  <a href="objections.html">Les onze objections</a>
</div>
"""
    return corps
