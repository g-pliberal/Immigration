"""L'état des lieux : ce que dit le droit, et ce que disent les chiffres."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "aujourdhui.html",
    "titre": "La politique d'immigration de la France aujourd'hui",
    "description": (
        "Qui entre, par quelle porte, avec quels délais : le droit en vigueur "
        "(CESEDA, loi du 26 janvier 2024) et les chiffres publics de "
        "l'immigration en France."),
}


def construire() -> str:
    corps = g.affiche(
        "Le constat",
        "Ce que la France <span class=\"serif\">fait déjà</span>",
        "Avant de proposer autre chose, il faut dire ce qui existe — sans le "
        "noircir ni l'embellir. Voici les portes d'entrée, leur poids réel, "
        "les délais constatés, et ce que la dernière loi a changé.")

    corps += g.plan([
        ("qui-entre", "Qui entre"),
        ("portes", "Les cinq portes"),
        ("travail", "La porte du travail"),
        ("asile", "L'asile"),
        ("eloignement", "L'éloignement"),
        ("loi-2024", "La loi de 2024"),
        ("cout", "Ce que cela coûte"),
    ])

    corps += """
<h2 id="qui-entre">Qui entre, et qui est là</h2>
<p>Deux chiffres à ne pas confondre. Le <em>stock</em> : 7,3 millions
d'immigrés vivent en France, soit 10,7 % de la population — dont un tiers a
acquis la nationalité française et n'est donc plus étranger (INSEE, 2023). Le
<em>flux</em> : environ 330 000 premiers titres de séjour sont délivrés chaque
année à des ressortissants de pays tiers, auxquels s'ajoutent les Européens,
qui circulent librement et ne demandent pas de titre.</p>
"""

    corps += g.reperes([
        ("Immigrés (stock)", "7,3 M", "10,7 % de la population — INSEE, 2023"),
        ("Étrangers (stock)", "5,6 M", "8,2 % de la population — INSEE, 2023"),
        ("Premiers titres (flux)", "~330 000",
         "par an, pays tiers — DGEF, 2023-2024"),
        ("Demandes d'asile", "~150 000",
         "par an, mineurs compris — OFPRA, 2023-2024"),
    ])

    corps += g.note(
        "<p><strong>« Immigré », « étranger », « sans-papiers » ne désignent "
        "pas les mêmes personnes.</strong> Un immigré est né étranger à "
        "l'étranger, qu'il soit devenu français ou non. Un étranger n'a pas la "
        "nationalité française, qu'il soit né en France ou non. Un étranger en "
        "situation irrégulière n'a pas de titre valide — ce qui n'a jamais "
        "empêché personne de travailler, seulement de le faire légalement. "
        "Les trois chiffres diffèrent d'un facteur dix ; les confondre est la "
        "première façon de mal poser le débat.</p>")

    corps += """
<h2 id="portes">Les cinq portes, et leur poids réel</h2>
<p>La France ne délivre pas « des titres » : elle délivre cinq familles de
titres, dont les proportions disent la politique menée mieux qu'aucun
discours.</p>
"""

    corps += g.tableau(
        ["Motif du premier titre", "Ordre de grandeur", "Part", "Ce que c'est"],
        [["Étudiants", "~110 000", "≈ 33 %",
          "Inscription dans un établissement ; titre d'un an, renouvelé à "
          "chaque année d'études"],
         ["Familial", "~90 000", "≈ 28 %",
          "Conjoint ou enfant de Français, regroupement familial, liens "
          "personnels et familiaux"],
         ["Économique", "~55 000", "≈ 17 %",
          "Salariés, travailleurs temporaires, cartes « talent », "
          "entrepreneurs"],
         ["Humanitaire", "~40 000", "≈ 12 %",
          "Réfugiés, protection subsidiaire, étrangers malades, victimes de "
          "traite"],
         ["Divers", "~35 000", "≈ 10 %",
          "Visiteurs, retraités, motifs non classés ailleurs"]],
        legende="Premiers titres de séjour délivrés à des ressortissants de "
                "pays tiers, ordres de grandeur 2023-2024 (source : DGEF, "
                "« L'essentiel de l'immigration »). Les arrondis font que la "
                "somme des parts ne tombe pas exactement sur 100 %.",
        classes_colonnes=["texte", "nombre", "nombre", "long"])

    corps += g.note(
        "<p>Retenez cette ligne : <strong class=\"cle-texte\">un premier titre "
        "sur six seulement est délivré pour travailler</strong>. La France est "
        "un pays d'immigration familiale et étudiante, pas un pays "
        "d'immigration de travail — et c'est le produit direct de règles qui "
        "rendent la porte du travail étroite, comme on va le voir.</p>")

    corps += """
<h2 id="travail">La porte du travail : une autorisation, pas un droit</h2>
<p>Un étranger qui veut travailler en France ne demande pas seulement un titre
de séjour : il lui faut une <strong>autorisation de travail</strong>, demandée
par l'employeur et instruite par les services de l'État (plateforme nationale,
sous l'autorité des DREETS). L'article L. 5221-2 du code du travail en fait une
condition de l'emploi ; le refus est possible, et motivé, entre autres, par
un critère qui n'a rien à voir avec le candidat.</p>
"""

    corps += g.cle(
        "Qu'est-ce que l'« opposabilité de la situation de l'emploi » ?",
        "C'est la règle qui permet à l'administration de refuser une "
        "autorisation de travail au motif qu'il y a, sur le marché local, "
        "assez de demandeurs d'emploi pour le poste — <strong>même si "
        "l'employeur, lui, n'a trouvé personne</strong>.",
        corps="<p>L'administration compare le métier et la zone d'emploi à des "
              "statistiques. L'employeur, qui a passé l'annonce et fait les "
              "entretiens, n'a pas voix au chapitre : son constat de pénurie "
              "ne fait pas preuve. La règle est écartée pour les métiers "
              "inscrits sur une liste dite « en tension », fixée par arrêté et "
              "révisée épisodiquement — autrement dit, un arrêté décide "
              "métier par métier, région par région, où le marché du travail a "
              "le droit de fonctionner.</p>",
        source="Code du travail, art. L. 5221-2 et R. 5221-20 ; arrêté fixant "
               "la liste des métiers en tension.",
        identifiant="opposabilite")

    corps += g.gestes([
        "<strong>L'employeur dépose la demande</strong> d'autorisation de "
        "travail en ligne, avec le contrat, les justificatifs de recherche "
        "et la preuve du respect du droit du travail.",
        "<strong>L'administration instruit</strong> : conformité du contrat, "
        "rémunération au moins égale au SMIC, respect des règles du métier — "
        "et, hors métiers en tension, situation de l'emploi.",
        "<strong>Le consulat délivre un visa long séjour</strong> si le "
        "travailleur est encore à l'étranger : nouveau dossier, nouveaux "
        "délais, nouveaux frais.",
        "<strong>La préfecture valide le titre</strong> à l'arrivée, souvent "
        "via le portail numérique, et le travailleur paie les taxes de "
        "délivrance.",
        "<strong>Et l'on recommence</strong> : la plupart de ces titres valent "
        "un an. Le renouvellement se demande deux à quatre mois avant "
        "l'échéance, et rouvre la même file.",
    ])

    corps += g.note(
        "<p><strong>Changer d'employeur n'est pas libre.</strong> "
        "L'autorisation de travail est attachée à un emploi ; en changer "
        "suppose, pour beaucoup de titres, une nouvelle demande. Un salarié "
        "dont le droit au séjour dépend de son patron est un salarié qui ne "
        "négocie pas, ne dénonce pas, et ne part pas. C'est le contraire d'un "
        "marché du travail libre — et cela nuit d'abord aux salariés "
        "français du même secteur, qui affrontent une concurrence sans "
        "défense.</p>", "vigilance")

    corps += """
<h2 id="asile">L'asile : un droit constitutionnel, une procédure lente</h2>
<p>Le droit d'asile n'est pas une politique migratoire : c'est une obligation
constitutionnelle et conventionnelle. La France reçoit de l'ordre de 150 000
demandes par an (mineurs compris). L'OFPRA statue en premier ressort ; la Cour
nationale du droit d'asile (CNDA) juge les recours, que la majorité des
déboutés exercent — et le recours est suspensif.</p>
"""

    corps += g.tableau(
        ["Étape", "Délai constaté", "Ce qu'il se passe pendant"],
        [["Enregistrement de la demande (guichet unique)", "quelques jours à "
          "quelques semaines", "Aucun droit au travail ; hébergement selon les "
          "places disponibles"],
         ["Instruction OFPRA", "de l'ordre de 4 à 6 mois",
          "Droit de travailler ouvert seulement au-delà de six mois, et sur "
          "autorisation"],
         ["Recours devant la CNDA", "de l'ordre de 6 à 12 mois",
          "Maintien du droit au séjour pendant l'instance"],
         ["Total, recours compris", "souvent plus de 18 mois",
          "Une vie entière suspendue à une décision, et des compétences qui "
          "rouillent"]],
        legende="Ordres de grandeur des délais d'asile (sources : rapports "
                "d'activité OFPRA et CNDA, Cour des comptes). Les délais "
                "varient fortement selon la procédure — accélérée, normale, "
                "Dublin.",
        classes_colonnes=["long", "texte", "long"])

    corps += g.note(
        "<p>Environ un tiers des demandes aboutissent à une protection, "
        "recours compris. Autrement dit : <strong class=\"cle-texte\">deux "
        "demandeurs sur trois attendent plus d'un an pour un refus</strong>, "
        "et un sur trois attend plus d'un an un statut auquel il avait droit "
        "dès le premier jour. Les deux attentes sont coûteuses — pour eux, et "
        "pour les finances publiques qui les hébergent sans qu'ils puissent "
        "travailler.</p>")

    corps += """
<h2 id="eloignement">L'éloignement : beaucoup de décisions, peu d'effets</h2>
<p>La France prononce un peu plus de 130 000 obligations de quitter le
territoire français (OQTF) par an. Moins d'une sur dix est exécutée. Les causes
sont connues et documentées : absence de laissez-passer consulaire du pays
d'origine, personnes non localisées, empêchements juridiques, capacités de
rétention limitées, et un contentieux massif.</p>
<p>Ce taux est l'argument favori de ceux qui veulent durcir la loi. Il devrait
d'abord être celui de ceux qui veulent la simplifier : <strong>une règle qu'on
n'applique pas n'est pas une règle sévère, c'est une règle fausse</strong>.
Elle coûte cher, elle occupe les tribunaux, elle nourrit le sentiment que rien
ne fonctionne, et elle ne protège personne.</p>
"""

    corps += g.cle(
        "Pourquoi les tribunaux administratifs sont-ils saturés ?",
        "Parce que le contentieux des étrangers représente, selon les années "
        "et les juridictions, <strong>environ 40 % des affaires jugées par les "
        "tribunaux administratifs</strong> — et davantage en appel.",
        corps="<p>Ce contentieux ne porte pas d'abord sur le fond, mais sur la "
              "procédure : refus implicites, rendez-vous impossibles à "
              "obtenir, titres non renouvelés à temps, décisions mal "
              "motivées. Une administration qui répondrait dans les délais "
              "supprimerait l'essentiel de ce contentieux — et rendrait au "
              "juge le temps qu'il doit aux autres litiges.</p>",
        source="Conseil d'État, rapports sur le contentieux des étrangers ; "
               "rapports annuels de la juridiction administrative.",
        identifiant="contentieux")

    corps += """
<h2 id="loi-2024">La loi du 26 janvier 2024, et ce qu'il en reste</h2>
<p>La dernière grande loi — « pour contrôler l'immigration, améliorer
l'intégration » — a été adoptée en janvier 2024 après un parcours
parlementaire heurté. Le Conseil constitutionnel en a censuré une trentaine
d'articles le 25 janvier 2024, pour l'essentiel comme « cavaliers
législatifs » : des dispositions sans lien avec le texte initial, introduites
en cours de navette.</p>
"""

    corps += g.depliant(
        "Ce que la loi de 2024 a effectivement changé",
        "<ul class=\"serree\">"
        "<li><strong>Régularisation par le travail dans les métiers en "
        "tension</strong> : une voie d'admission exceptionnelle au séjour, "
        "inscrite dans le CESEDA à titre temporaire, pour des salariés déjà "
        "présents et employés dans ces métiers.</li>"
        "<li><strong>Condition de langue</strong> renforcée pour la "
        "délivrance de certaines cartes pluriannuelles et pour la carte de "
        "résident.</li>"
        "<li><strong>Carte « talent »</strong> : le passeport talent est "
        "réorganisé et renommé, avec une mention pour les professions "
        "médicales.</li>"
        "<li><strong>Éloignement</strong> : élargissement des cas où une OQTF "
        "peut être prononcée, et durcissement pour les étrangers condamnés.</li>"
        "<li><strong>Amende pour emploi d'étranger sans titre</strong> et "
        "sanctions des marchands de sommeil.</li>"
        "</ul>"
        "<h4>Et ce que le Conseil constitutionnel a censuré</h4>"
        "<p>Notamment : les quotas migratoires pluriannuels votés par le "
        "Parlement, le durcissement du regroupement familial, la caution "
        "demandée aux étudiants étrangers, le délai de carence pour certaines "
        "prestations sociales, et le durcissement de l'accès à la nationalité "
        "pour les personnes nées en France. La plupart l'ont été pour un motif "
        "de procédure — l'absence de lien avec le texte déposé —, et non sur "
        "le fond.</p>"
        "<p class=\"discret\">Décision n° 2023-863 DC du 25 janvier 2024.</p>")

    corps += g.note(
        "<p><strong>La leçon de 2024 n'est pas « il faut une loi de plus ».</strong> "
        "C'est que notre débat produit des textes longs, votés dans l'urgence, "
        "largement censurés, et qui laissent intacte la machine qui pose "
        "problème : l'autorisation préalable de travailler, les délais sans "
        "sanction, et des décisions d'éloignement qu'on ne peut pas "
        "exécuter.</p>", "avertissement")

    corps += """
<h2 id="cout">Ce que cela coûte, et ce que cela rapporte</h2>
<p>Le budget de la mission « Immigration, asile et intégration » se compte en
milliards d'euros, dont une large part va à l'hébergement et à l'allocation
des demandeurs d'asile — c'est-à-dire au financement de l'attente. L'aide
médicale de l'État (AME), qui soigne les étrangers en situation irrégulière
sous condition de ressources et d'ancienneté, concerne de l'ordre de 450 000
personnes pour un coût annuel voisin de 1,2 milliard d'euros, soit environ
0,4 % des dépenses d'assurance maladie.</p>
<p>Quant au solde budgétaire de l'immigration prise dans son ensemble — ce que
les immigrés versent en impôts et cotisations moins ce qu'ils reçoivent —, les
travaux disponibles (OCDE, CEPII) convergent sur un point : <strong
class="cle-texte">il est faible, positif ou négatif selon les méthodes, et
toujours proche de zéro</strong>, de l'ordre de quelques dixièmes de point de
PIB. Ni gouffre, ni manne : ce qui compte est l'emploi. Un immigré qui
travaille contribue ; un immigré qu'on empêche de travailler coûte.</p>
"""

    corps += g.note(
        "<p>C'est tout l'enjeu de la réforme proposée ici : le taux d'emploi "
        "des immigrés extra-européens est en France l'un des plus faibles "
        "d'Europe de l'Ouest, et particulièrement celui des femmes. Ce n'est "
        "pas une fatalité culturelle : c'est, pour une part qu'on peut "
        "mesurer, le produit d'années passées sans droit de travailler, avec "
        "un titre attaché à un employeur, et un diplôme étranger jamais "
        "reconnu.</p>")

    corps += """
<div class="actions">
  <a class="bouton" href="blocages.html">Ce qui coince, et pourquoi</a>
  <a href="sources.html">Voir les sources</a>
</div>
"""
    return corps
