"""L'état des lieux : ce que dit le droit, et ce que disent les chiffres."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "aujourdhui.html",
    "titre": "La politique d'immigration de la France aujourd'hui",
    "description": (
        "Qui entre, par quelle porte, avec quels délais : le droit en vigueur "
        "(CESEDA, loi du 26 janvier 2024, pacte européen appliqué depuis juin "
        "2026) et les chiffres publics de l'immigration en France."),
}


def construire() -> str:
    corps = g.affiche(
        "Le constat",
        "Ce que la France <span class=\"serif\">fait déjà</span>",
        "Avant de proposer autre chose, il faut dire ce qui existe — sans le "
        "noircir ni l'embellir. Voici les portes d'entrée, leur poids réel, "
        "les délais constatés, et ce que la dernière loi française et le "
        "premier pacte européen ont changé.")

    corps += g.plan([
        ("qui-entre", "Qui entre"),
        ("portes", "Les cinq portes"),
        ("travail", "La porte du travail"),
        ("asile", "L'asile"),
        ("eloignement", "L'éloignement"),
        ("loi-2024", "La loi de 2024"),
        ("pacte", "Le pacte européen"),
        ("cout", "Ce que cela coûte"),
    ])

    corps += """
<h2 id="qui-entre">Qui entre, et qui est là</h2>
<p>Deux chiffres à ne pas confondre. Le <em>stock</em> : huit millions
d'immigrés vivent en France, soit 11,6 % de la population — dont un tiers a
acquis la nationalité française et n'est donc plus étranger. Le <em>flux</em> :
384 230 premiers titres de séjour ont été délivrés l'an dernier à des
ressortissants de pays tiers, auxquels s'ajoutent les Européens, qui circulent
librement et ne demandent pas de titre.</p>
"""

    corps += g.reperes_chiffres([
        ("immigres", "Immigrés (stock)"),
        ("etrangers", "Étrangers (stock)"),
        ("premiers-titres", "Premiers titres (flux)"),
        ("asile-demandes", "Demandes d'asile"),
    ])

    corps += g.note(
        "<p><strong>Une précaution que ce site doit prendre avant que ses "
        "adversaires ne la lui reprochent.</strong> Le protocole de collecte "
        "du recensement a changé : les chiffres de population d'avant 2024 ne "
        "sont pas directement comparables à ceux de 2024 et 2025. Une partie "
        "de la hausse apparente du nombre d'immigrés est un effet de méthode, "
        "pas un flux de personnes. Qui présente l'écart entre 2023 et 2025 "
        "comme une arrivée se trompe, quel que soit le camp.</p>",
        "avertissement")

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
discours. Et ces proportions viennent de changer.</p>
"""

    # Le tableau est construit depuis le registre, et non recopié : c'est le
    # tableau le plus cité du site, celui qu'un contradicteur vérifiera en
    # premier, et celui qui était périmé de deux ans. Le faire dériver des
    # fiches garantit qu'il ne peut plus diverger d'elles.
    portes = [
        ("titres-etudiants", "Étudiants", "≈ 31 %"),
        ("titres-humanitaire", "Humanitaire", "≈ 24 %"),
        ("titres-familial", "Familial", "≈ 23 %"),
        ("titres-economique", "Économique", "≈ 13 %"),
        ("titres-divers", "Divers", "≈ 8 %"),
    ]
    corps += g.tableau(
        ["Motif du premier titre", "Nombre", "Part", "Évolution sur un an"],
        [[libelle,
          g.nombre(cle),
          part,
          g.escape(g.chiffre(cle).evolution) or "<span class=\"discret\">non "
          "publiée séparément</span>"]
         for cle, libelle, part in portes],
        legende="Premiers titres délivrés à des ressortissants de pays tiers, "
                "données 2025 (DGEF). Les lignes « Familial » et « Divers » "
                "portent une valeur <strong>déduite</strong> : le communiqué "
                "publie le total et l'évolution de ces motifs sans en "
                "détailler le volume — leur somme vaut 122 440. Chaque ligne "
                "renvoie à sa fiche. "
                + g.renvoi("premiers-titres"),
        classes_colonnes=["texte", "nombre", "nombre", "long"])

    corps += g.note(
        "<p>Retenez deux lignes. La première : <strong class=\"cle-texte\">un "
        "premier titre sur huit seulement est délivré pour travailler, et "
        "cette part baisse</strong>. La seconde : <strong>la hausse de 11,2 % "
        "des entrées en 2025 vient presque entièrement du motif "
        "humanitaire</strong>, c'est-à-dire de l'Afghanistan, de l'Ukraine et "
        "du Soudan — des crises que ni la loi de 2024, ni aucune loi "
        "française ne pilote. Un adversaire qui impute cette hausse à la "
        "politique migratoire se trompe de sujet ; un allié qui la passe sous "
        "silence nous dessert.</p>")

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
        "délais, nouveaux frais. Cette étape relève du code des visas "
        "européen : aucune réforme nationale ne la supprime.",
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
constitutionnelle et conventionnelle. La France a enregistré 151 665 demandes
l'an dernier, mineurs compris, en baisse de 3,7 %. L'OFPRA statue en premier
ressort ; la Cour nationale du droit d'asile (CNDA) juge les recours, que la
majorité des déboutés exercent.</p>
<p>Le recours devant la CNDA est suspensif <em>en procédure normale</em> —
mais il ne l'est pas dans plusieurs cas de procédure accélérée ou
d'irrecevabilité, où le droit au maintien sur le territoire prend fin avant la
décision du juge. La nuance compte : elle est l'un des points que le pacte
européen a resserrés.</p>
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
          "Maintien du droit au séjour pendant l'instance, en procédure "
          "normale"],
         ["Total, recours compris", "souvent plus de 18 mois",
          "Une vie entière suspendue à une décision, et des compétences qui "
          "rouillent"]],
        legende="Ordres de grandeur des délais d'asile (rapports d'activité "
                "OFPRA et CNDA, Cour des comptes). Les délais varient "
                "fortement selon la procédure — accélérée, normale, "
                "frontière.",
        classes_colonnes=["long", "texte", "long"])

    corps += g.note(
        "<p><strong>Un chiffre a changé, et il change l'argument.</strong> "
        "Le taux de protection atteint désormais 52 %, recours compris, contre "
        "environ un tiers les années précédentes : la montée des demandes "
        "afghanes et ukrainiennes a fait basculer la majorité. "
        + g.renvoi("asile-protection") +
        " Autrement dit, <strong class=\"cle-texte\">c'est maintenant plus "
        "d'un demandeur sur deux qui attend dix-huit mois une protection à "
        "laquelle il avait droit dès le premier jour</strong>. L'argument "
        "« ils attendent pour rien » était le nôtre il y a deux ans ; il est "
        "faux aujourd'hui, et l'argument de la lenteur en sort renforcé, pas "
        "affaibli.</p>")

    corps += """
<h2 id="eloignement">L'éloignement : beaucoup de décisions, peu d'effets</h2>
<p>La France prononce environ 140 000 obligations de quitter le territoire
français (OQTF) par an, et en exécute de l'ordre de 11 %. Les causes sont
connues : absence de laissez-passer consulaire du pays d'origine, personnes non
localisées, empêchements juridiques, capacités de rétention limitées, et un
contentieux massif.</p>
<p>Deux honnêtetés s'imposent ici. La première : <strong>les éloignements
augmentent</strong> — 24 985 l'an dernier, dont 15 569 forcés, en hausse de
15,7 % et de 21 %. Dire que « rien ne bouge » n'est plus exact.
"""
    corps += g.renvoi("eloignements")
    corps += """ La seconde : <strong>le « taux d'exécution des OQTF » est un
ratio boiteux</strong>, et nous ne voulons pas construire un argument sur un
chiffre que nous devrions défendre. Le numérateur et le dénominateur ne portent
pas sur les mêmes personnes, les départs spontanés ne sont pas tous constatés,
et des décisions que personne ne peut exécuter restent au dénominateur.</p>
<p>Ce qu'il mesure vraiment, et c'est suffisant : <strong>l'écart entre ce que
l'État écrit et ce qu'il peut faire</strong>. Une règle qu'on n'applique pas
n'est pas une règle sévère, c'est une règle fausse. Elle coûte cher, elle
occupe les tribunaux, elle nourrit le sentiment que rien ne fonctionne, et elle
ne protège personne.</p>
"""

    corps += g.cle(
        "Pourquoi les tribunaux administratifs sont-ils saturés ?",
        "Parce que le contentieux des étrangers représente désormais "
        "<strong>près de la moitié des requêtes nouvelles devant les tribunaux "
        "administratifs</strong>, en hausse de 9 % en un an, et environ autant "
        "en appel.",
        corps="<p>Il faut dire précisément de quoi cette masse est faite, "
              "parce que la version courte qu'on lit partout — « c'est du "
              "contentieux de procédure » — est fausse et se retourne en une "
              "phrase. L'essentiel des recours vise des refus de séjour et des "
              "OQTF : ce sont des contentieux <strong>au fond</strong>, qui "
              "subsisteraient en grande partie après notre réforme, et qui "
              "augmenteraient même si l'on éloigne davantage.</p>"
              "<p>Ce que la réforme supprime est une autre part, réelle et "
              "documentée : les référés pour obtenir un rendez-vous, les "
              "recours contre des refus implicites nés du silence, les "
              "contentieux de ruptures de droits causées par un "
              "renouvellement tardif. C'est un gain sérieux, et il ne vaut "
              "pas la moitié du rôle des tribunaux. Nous préférons le chiffrer "
              "bas et le tenir.</p>",
        source="Conseil d'État, rapport public 2025 sur l'activité "
               "juridictionnelle." + g.renvoi("contentieux-ta"),
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
        "tension</strong> : l'article L. 435-4 du CESEDA, voie d'admission "
        "exceptionnelle pour un salarié justifiant de douze mois de travail "
        "dans ces métiers sur vingt-quatre et de trois ans de présence. "
        "<strong>Ce dispositif est expérimental et expire le 31 décembre "
        "2026</strong> : aucune loi ne l'a prorogé à ce jour.</li>"
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
        "<p><strong>Une échéance que le débat public n'a pas vue.</strong> "
        "La seule voie légale ouverte depuis 2024 à un travailleur déjà "
        "présent et employé — l'article L. 435-4 — <strong>disparaît le "
        "31 décembre 2026</strong>. Sans texte de remplacement, on revient au "
        "pur pouvoir discrétionnaire de la circulaire. Notre engagement 1 "
        "n'est donc pas une proposition en l'air : c'est la réponse à un vide "
        "juridique daté.</p>", "avertissement")

    corps += """
<h2 id="pacte">Le pacte européen, appliqué depuis le 12 juin 2026</h2>
<p>Un programme national d'immigration écrit comme si la France décidait seule
de sa procédure d'asile serait périmé le jour de sa publication. Depuis le
12 juin 2026, neuf règlements et une directive — le « pacte sur la migration
et l'asile », adopté en mai 2024 — s'appliquent dans les vingt-sept États
membres. Le ministère de l'Intérieur en a publié la circulaire d'application
le 10 juin 2026.</p>
"""

    corps += g.points([
        ("Un filtrage obligatoire à l'entrée",
         "Identification, contrôle sanitaire et de sécurité, relevé "
         "biométrique avant toute procédure — ce que nos engagements 1 et 4 "
         "supposaient déjà, et qui est désormais du droit applicable."),
        ("Une procédure à la frontière",
         "Examen accéléré pour certaines nationalités, avec maintien à "
         "disposition : le calendrier de l'asile n'est plus un choix "
         "purement français."),
        ("Une solidarité chiffrée",
         "Un objectif de relocalisation — 21 000 demandeurs pour 2026 — ou "
         "une compensation financière de 20 000 € par personne refusée."),
        ("Des délais encadrés",
         "Le règlement fixe ses propres bornes d'instruction. Notre "
         "engagement 4 s'y inscrit désormais au lieu d'inventer un "
         "calendrier français isolé."),
    ])

    corps += g.note(
        "<p><strong>Ce que cela change pour ce programme.</strong> Deux de nos "
        "engagements y gagnent : le filtrage systématique et les délais "
        "encadrés sont maintenant du droit positif, ce qui nous dispense de "
        "les réclamer. Un engagement doit s'y plier : l'asile jugé en trois "
        "mois ne se décrète pas contre le règlement européen, il se construit "
        "dedans — c'est pourquoi nous avons remplacé une promesse de trois "
        "mois par un calendrier en deux temps, opposable, décrit au "
        "<a href=\"programme.html#quatre\">programme</a>.</p>")

    corps += """
<h2 id="cout">Ce que cela coûte, et ce que cela rapporte</h2>
<p>La mission budgétaire « Immigration, asile et intégration » pèse 2,16
milliards d'euros en 2026, dont 299 millions pour la seule allocation versée
aux demandeurs d'asile — c'est-à-dire au financement de l'attente de personnes
à qui l'on interdit par ailleurs de travailler. À côté, la Cour des comptes
chiffre à environ 1,8 milliard le coût direct annuel de la politique de lutte
contre l'immigration irrégulière, pour des résultats qu'elle juge
« inefficaces ». L'aide médicale de l'État couvre de l'ordre de 480 000
personnes pour une dépense de 1,39 milliard en 2024, soit environ 0,4 % des
dépenses d'assurance maladie.</p>
<p>Quant au solde budgétaire de l'immigration prise dans son ensemble — ce que
les immigrés versent en impôts et cotisations moins ce qu'ils reçoivent —, les
travaux disponibles (OCDE, CEPII) convergent sur un point : <strong
class="cle-texte">il est faible, positif ou négatif selon les méthodes, et
toujours proche de zéro</strong>, de l'ordre de quelques dixièmes de point de
PIB. Ni gouffre, ni manne : ce qui compte est l'emploi. Un immigré qui
travaille contribue ; un immigré qu'on empêche de travailler coûte.</p>
"""

    corps += g.reperes_chiffres([
        ("mission-budget", "Mission budgétaire"),
        ("ada-credits", "Allocation aux demandeurs d'asile"),
        ("irreguliere-cout", "Lutte contre l'irrégulier"),
        ("ame", "Aide médicale de l'État"),
    ])

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
  <a href="chiffres.html">Tous les chiffres</a>
</div>
"""
    return corps
