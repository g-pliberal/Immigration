"""Les objections sérieuses, et ce qu'on y répond.

Une page de programme qui n'expose que ses arguments ne convainc personne :
elle donne au lecteur le sentiment, souvent juste, qu'on lui cache la moitié
du dossier. Les objections reprises ici sont celles qui se tiennent — pas des
épouvantails commodes —, et deux d'entre elles ne reçoivent pas de réponse
complète. C'est dit.
"""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "objections.html",
    "titre": "Objections — et ce que nous y répondons",
    "description": (
        "Appel d'air, salaires, logement, intégration, sécurité, "
        "État-providence, fuite des cerveaux : les objections sérieuses au "
        "programme libéral sur l'immigration, et leurs réponses."),
}


def construire() -> str:
    corps = g.affiche(
        "Pour aller plus loin",
        "Les objections <span class=\"serif\">qui se tiennent</span>",
        "Sept objections, dans leur version forte — celle que formulerait "
        "quelqu'un d'informé et de bonne foi, pas la caricature qu'il est "
        "facile de renverser.")

    corps += g.plan([
        ("appel-air", "L'appel d'air"),
        ("salaires", "Les salaires"),
        ("logement", "Le logement"),
        ("integration", "L'intégration"),
        ("securite", "La sécurité"),
        ("providence", "L'État-providence"),
        ("cerveaux", "La fuite des cerveaux"),
    ])

    corps += g.cle(
        "« Vous allez créer un appel d'air »",
        "En partie, oui — et c'est assumé pour le travail, pas pour le "
        "guichet. Une règle plus simple fera venir davantage de gens qui "
        "viennent travailler, et moins de gens qui viennent tenter leur "
        "chance sans projet.",
        corps="<p>Ce que la recherche montre, c'est que les flux répondent "
              "surtout à la demande de travail et aux réseaux déjà installés, "
              "et beaucoup moins aux règles d'accès aux prestations. Notre "
              "réforme agit précisément là : elle ouvre la voie légale du "
              "travail et ferme pour cinq ans celle des aides non "
              "contributives. Elle rend donc la France plus attirante pour "
              "celui qui a une promesse d'embauche, et strictement pas plus "
              "attirante pour celui qui n'en a pas.</p>"
              "<p>Il faut ajouter une chose que nos adversaires ont raison de "
              "souligner : <strong>nous ne savons pas chiffrer précisément "
              "l'ampleur de la réponse</strong>. Aucun pays comparable n'a "
              "mené exactement cette politique. C'est pourquoi le programme "
              "prévoit des critères révisables et une clause de réexamen "
              "public des résultats, et non une promesse de nombre.</p>",
        identifiant="appel-air")

    corps += g.cle(
        "« Cela fera baisser les salaires des Français »",
        "La littérature économique, très abondante sur ce point, trouve des "
        "effets faibles à nuls en moyenne — et les effets négatifs, quand ils "
        "existent, frappent d'abord <strong>les immigrés déjà installés</strong>, "
        "pas les natifs.",
        corps="<p>La raison tient en une phrase : un travailleur n'est pas "
              "seulement une offre de travail, c'est aussi une demande de "
              "biens, de services et de logement, donc des emplois. Les "
              "études d'épisodes réels — arrivées massives et soudaines — ne "
              "retrouvent pas l'effondrement des salaires que la théorie la "
              "plus simple prédit.</p>"
              "<p>Il y a mieux : notre réforme <em>protège</em> les salaires "
              "bas. Aujourd'hui, la concurrence la plus dure vient du travail "
              "non déclaré, où l'on ne peut ni exiger le minimum légal, ni se "
              "syndiquer, ni porter plainte. Rendre ces travailleurs légaux, "
              "c'est les obliger à coûter ce que coûte un salarié déclaré, et "
              "supprimer l'avantage de l'employeur qui triche.</p>",
        source="Card (1990), Peri, Dustmann-Schönberg-Stuhler (2016), "
               "synthèses OCDE — voir Sources.",
        identifiant="salaires")

    corps += g.cle(
        "« Et le logement ? Il n'y en a déjà pas assez »",
        "C'est l'objection la plus solide, et notre réponse est qu'elle vise "
        "la mauvaise cause. La pénurie française de logements est une pénurie "
        "d'offre, produite par la contrainte réglementaire, pas par la "
        "démographie.",
        corps="<p>On ne construit pas parce qu'il est long, coûteux et "
              "politiquement risqué de délivrer un permis, dans un pays où "
              "les communes tirent peu de bénéfice à accueillir des habitants "
              "de plus. Un libéral répond à une pénurie par l'offre : "
              "libération du foncier constructible, simplification des règles "
              "d'urbanisme, réforme de la fiscalité locale pour que "
              "construire rapporte à la commune qui construit.</p>"
              "<p>Reste un point de calendrier qu'il faut reconnaître : "
              "<strong>le logement met des années à s'ajuster, une arrivée "
              "quelques mois</strong>. Une ouverture du travail sans réforme "
              "de l'offre de logement tend, à court terme et localement, les "
              "loyers. Les deux réformes vont ensemble ; c'est une condition, "
              "pas un détail.</p>",
        identifiant="logement")

    corps += g.cle(
        "« L'intégration ne suit pas »",
        "Le premier facteur d'intégration mesurable est l'emploi — et notre "
        "système commence par l'interdire pendant des mois, puis attache le "
        "titre à un employeur unique.",
        corps="<p>Le taux d'emploi des immigrés extra-européens est en France "
              "parmi les plus faibles d'Europe de l'Ouest, celui des femmes "
              "plus encore. Ce résultat n'est pas indépendant des règles : des "
              "années sans droit de travailler, un diplôme étranger jamais "
              "reconnu, un titre annuel qui décourage l'employeur, et une "
              "assignation de fait au secteur informel produisent exactement "
              "ce qu'on observe.</p>"
              "<p>Le programme ajoute deux choses que la seule ouverture ne "
              "donne pas : la reconnaissance rapide des qualifications "
              "acquises à l'étranger, et un accès effectif aux cours de "
              "français, dont la condition de langue exigée à chaque étape du "
              "séjour est aujourd'hui le pendant sans moyens.</p>",
        identifiant="integration")

    corps += g.cle(
        "« Et la sécurité ? »",
        "Un programme libéral n'a aucune raison d'être laxiste sur la "
        "délinquance — et toutes les raisons de vouloir un État qui puisse "
        "réellement éloigner un étranger condamné.",
        corps="<p>Aujourd'hui, l'administration prononce plus de 130 000 "
              "décisions d'éloignement pour en exécuter moins d'une sur dix, "
              "et ses moyens sont dispersés sur cette masse. En cessant de "
              "poursuivre des gens dont le seul tort est de travailler sans "
              "l'accord d'un service, elle concentre ses moyens sur les "
              "étrangers condamnés et les menaces avérées — où l'éloignement "
              "est justifié, et où il devient possible.</p>"
              "<p>S'y ajoutent deux gains directs de la régularisation du "
              "travail : des identités établies et vérifiées plutôt qu'une "
              "population sans existence administrative, et des victimes ou "
              "témoins qui peuvent enfin aller au commissariat sans risquer "
              "l'expulsion.</p>",
        identifiant="securite")

    corps += g.cle(
        "« Frontières ouvertes et État-providence sont incompatibles »",
        "Nous sommes d'accord avec Milton Friedman : il faut choisir. Nous "
        "choisissons d'ouvrir le travail et de différer l'aide non "
        "contributive de cinq ans.",
        corps="<p>C'est la seule réponse cohérente, et elle a un prix que nous "
              "assumons : pendant cinq ans, un travailleur étranger cotise "
              "sans recevoir l'ensemble des prestations financées par "
              "l'impôt. Ce n'est pas une position confortable à tenir — ni "
              "devant ceux qui trouvent l'ouverture excessive, ni devant ceux "
              "qui trouvent le délai injuste.</p>"
              "<p>Deux réserves honnêtes. D'abord, la règle devra être "
              "rédigée avec soin pour tenir devant le Conseil constitutionnel "
              "et le droit européen : un délai de carence a déjà été censuré "
              "en 2024, pour un motif de procédure, et le principe d'égalité "
              "encadre ce genre de distinction. Ensuite, elle ne s'applique "
              "pas aux réfugiés statutaires, dont les droits relèvent d'un "
              "engagement international que nous ne proposons pas de "
              "renégocier.</p>",
        identifiant="providence")

    corps += g.cle(
        "« Vous videz les pays pauvres de leurs médecins »",
        "L'objection est réelle pour quelques professions et quelques pays, et "
        "elle est très exagérée dans le débat général.",
        corps="<p>Les transferts d'argent envoyés par les migrants vers leur "
              "pays d'origine dépassent, à l'échelle mondiale, l'ensemble de "
              "l'aide publique au développement. S'y ajoutent les retours, les "
              "compétences rapportées et les réseaux d'affaires créés. Pour "
              "la plupart des métiers, l'émigration élève le rendement de "
              "l'éducation dans le pays de départ et y augmente le nombre de "
              "diplômés, y compris parmi ceux qui restent.</p>"
              "<p>Le cas des professions de santé de quelques pays à faible "
              "densité médicale est différent, et mérite des conventions "
              "bilatérales : formation financée, rotations, compensations. "
              "C'est un problème ciblé, qui appelle un instrument ciblé — pas "
              "l'interdiction générale faite à des adultes de vendre leur "
              "travail où ils le souhaitent.</p>",
        identifiant="cerveaux")

    corps += g.note(
        "<p><strong>Ce que nous ne savons pas.</strong> L'ampleur exacte de la "
        "réponse migratoire à une ouverture du travail ; l'effet local sur les "
        "loyers pendant les années où l'offre de logement s'ajuste ; la "
        "solidité juridique du délai de cinq ans sur les prestations non "
        "contributives. Une page de programme qui prétendrait avoir la réponse "
        "à ces trois questions mentirait.</p>", "avertissement")

    corps += """
<div class="actions">
  <a class="bouton" href="sources.html">Sources et méthode</a>
  <a href="programme.html">Relire le programme</a>
</div>
"""
    return corps
