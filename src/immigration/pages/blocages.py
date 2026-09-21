"""Le diagnostic : pourquoi ce système rate ses propres objectifs."""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "blocages.html",
    "titre": "Ce qui coince — diagnostic de la politique migratoire française",
    "description": (
        "Autorisation préalable de travailler, délais sans sanction, asile "
        "interminable, décisions inexécutées : les cinq mécanismes qui font "
        "échouer la politique migratoire française, et ce que dit — et ne dit "
        "pas — la recherche économique."),
}


def construire() -> str:
    corps = g.affiche(
        "Le constat",
        "Un système qui <span class=\"serif\">rate sa propre cible</span>",
        "Le reproche fait ici n'est pas idéologique : ce système ne fait pas "
        "ce qu'il prétend faire. Il n'attire pas les travailleurs dont "
        "l'économie manque, n'éloigne pas ceux qui doivent partir, et fabrique "
        "lui-même l'irrégularité qu'il dénonce.")

    corps += g.plan([
        ("cinq", "Les cinq mécanismes"),
        ("irregularite", "L'irrégularité fabriquée"),
        ("recherche", "Ce que dit la recherche"),
        ("faux-debat", "Trois faux débats"),
    ])

    corps += """
<h2 id="cinq">Les cinq mécanismes</h2>
<p>Ils sont indépendants les uns des autres, et c'est ce qui les rend
tenaces : corriger l'un sans les autres ne produit presque rien.</p>
"""

    corps += g.cle(
        "1. L'autorisation préalable de travailler",
        "Un contrat entre un employeur français et un travailleur étranger "
        "n'est pas valable par lui-même : il lui faut l'accord d'un tiers qui "
        "ne connaît ni l'un ni l'autre.",
        corps="<p>Ce tiers décide au vu de statistiques d'emploi — "
              "l'opposabilité de la situation de l'emploi — corrigées par une "
              "liste de métiers dits en tension. Une liste administrative "
              "arrive toujours après la pénurie qu'elle constate, et ne dit "
              "rien des compétences qu'un employeur cherche vraiment. "
              "Résultat : un aide-soignant manque à l'hôpital pendant que son "
              "dossier attend, et une entreprise renonce à recruter plutôt que "
              "d'attendre six mois une réponse qu'elle ne peut pas "
              "anticiper.</p>"
              "<p>Le résultat se lit dans les chiffres : le motif économique "
              "a reculé de 13 % en un an, et les titres saisonniers "
              "d'environ 30 %. C'est le seul motif que la politique "
              "migratoire pilote réellement, et c'est celui qui baisse."
              + g.renvoi("titres-economique") + "</p>",
        source="Code du travail, art. L. 5221-2 ; liste des métiers en tension "
               "fixée par arrêté.")

    corps += g.cle(
        "2. Le délai sans sanction, et le silence qui vaut refus",
        "L'administration n'a, en pratique, aucune obligation de résultat sur "
        "les délais — et son silence prolongé vaut décision de refus, qu'il "
        "faut attaquer au tribunal.",
        corps="<p>Dans presque tout le droit administratif français, le "
              "silence de l'administration vaut acceptation depuis la loi du "
              "12 novembre 2013, entrée en vigueur en 2014. Le droit des "
              "étrangers est l'une des grandes exceptions : là, le silence "
              "vaut rejet. La conséquence est mécanique — la lenteur devient "
              "gratuite pour celui qui la produit, et très coûteuse pour "
              "celui qui la subit. C'est ainsi qu'un pays finit avec des "
              "files d'attente nocturnes devant ses préfectures et des "
              "référés pour obtenir un rendez-vous.</p>",
        source="Défenseur des droits, rapports sur la dématérialisation des "
               "services publics ; Conseil d'État, 3 juin 2022, n° 452798 ; "
               "jurisprudence des référés « mesures utiles ».")

    corps += g.cle(
        "3. L'asile long, et l'interdiction de travailler pendant",
        "On interdit à un demandeur d'asile de travailler pendant six mois, "
        "puis on lui reproche de ne pas s'intégrer.",
        corps="<p>Un adulte valide, souvent qualifié, reste hébergé et "
              "indemnisé sans avoir le droit de gagner sa vie, pendant que sa "
              "demande chemine. Et la majorité de ces personnes obtiendront "
              "une protection : le taux est désormais de 52 %, recours "
              "compris." + g.renvoi("asile-protection") + " Nous faisons donc "
              "attendre dix-huit mois, aux frais du contribuable, des gens "
              "dont plus d'un sur deux avait droit à rester dès le premier "
              "jour.</p>"
              "<p>Les pays qui ont ouvert le travail plus tôt n'ont pas "
              "constaté l'afflux annoncé, mais une baisse du coût "
              "d'hébergement et un meilleur taux d'emploi ultérieur, y "
              "compris pour les réfugiés reconnus.</p>",
        source="CESEDA, art. L. 554-1 ; rapports OFPRA/CNDA ; travaux de "
               "l'OCDE sur l'insertion des réfugiés.")

    corps += g.cle(
        "4. Des décisions d'éloignement qu'on ne peut pas exécuter",
        "Prononcer 140 000 obligations de quitter le territoire pour en "
        "exécuter environ une sur neuf n'est pas de la fermeté : c'est un "
        "système qui écrit des décisions sans effet.",
        corps="<p>L'exécution suppose un laissez-passer consulaire que le pays "
              "d'origine délivre ou non, une personne localisée, des places de "
              "rétention, et un juge qui valide. Aucune loi française ne peut "
              "à elle seule produire les trois premiers. Multiplier les "
              "décisions symboliques sature les tribunaux et détourne les "
              "moyens de la petite minorité de cas — étrangers condamnés, "
              "menaces à l'ordre public — où l'éloignement est à la fois "
              "possible et nécessaire.</p>"
              "<p><strong>Deux précisions d'honnêteté.</strong> Les "
              "éloignements <em>augmentent</em> : 24 985 l'an dernier, en "
              "hausse de 15,7 %." + g.renvoi("eloignements") + " Et le « taux "
              "d'exécution » est un ratio dont nous ne voulons pas dépendre : "
              "il compare des décisions d'une année à des départs d'une "
              "autre, et laisse au dénominateur des mesures que personne ne "
              "peut exécuter. Il ne mesure pas une volonté ; il mesure un "
              "écart entre l'écrit et le possible. C'est suffisant.</p>",
        source="Cour des comptes, « La politique de lutte contre l'immigration "
               "irrégulière », janvier 2024." + g.renvoi("oqtf-executees"))

    corps += g.cle(
        "5. Le titre d'un an, et la file d'attente qu'il crée",
        "L'essentiel des demandes traitées en préfecture ne sont pas des "
        "arrivées : ce sont des renouvellements de gens déjà là, déjà en "
        "règle, déjà employés.",
        corps="<p>Le chiffre est sans appel : <strong "
              "class=\"cle-texte\">955 080 titres renouvelés contre 384 230 "
              "premiers titres</strong> — deux fois et demie plus de "
              "renouvellements que d'arrivées, et une hausse de 7,6 % en un "
              "an." + g.renvoi("renouvellements") + " Un titre d'un an oblige "
              "son détenteur à redéposer un dossier tous les ans, deux à "
              "quatre mois avant l'échéance.</p>"
              "<p>Multiplié par des millions de titres valides, ce rythme "
              "engorge le guichet, occupe des agents à re-vérifier ce qu'ils "
              "ont vérifié l'an passé, et crée des ruptures de droits — perte "
              "d'emploi, de logement, de compte bancaire — quand le "
              "renouvellement arrive en retard.</p>",
        source="Rapports de la Cour des comptes sur l'accueil des étrangers "
               "en préfecture ; Défenseur des droits.")

    corps += """
<h2 id="irregularite">L'irrégularité est fabriquée par la règle</h2>
<p>C'est le point que les deux camps du débat français évitent. Une part
importante des étrangers en situation irrégulière n'a pas franchi une
frontière clandestinement : ils sont entrés légalement, avec un visa, un titre
étudiant ou une demande d'asile, et sont devenus irréguliers <strong
class="cle-texte">par l'expiration d'un titre, un refus de renouvellement ou
un rejet d'asile</strong>. L'irrégularité est, pour beaucoup, une sortie du
système légal, pas une entrée en dehors de lui.</p>
<p>La conséquence pratique est brutale : ces personnes travaillent presque
toutes. Elles travaillent au noir, sans cotiser, sans recours contre un
employeur qui abuse, en tirant vers le bas les conditions de leurs collègues
déclarés. La règle n'a pas empêché le travail ; elle l'a rendu invisible et
sans droits.</p>
<p><strong>Aucune statistique ne dénombre cette population</strong>, et il faut
le dire avant de l'estimer : les chiffres qui circulent — de 300 000 à
900 000 — sont des extrapolations faites à partir de l'aide médicale de l'État
ou des régularisations, et aucun n'a la solidité des chiffres cités ailleurs
sur ce site. Nous n'en retenons aucun.</p>
"""

    corps += g.points([
        ("Ce que l'irrégularité coûte à l'étranger",
         "Pas de contrat, pas de recours, pas de logement, pas de compte, et "
         "une dépendance totale à l'employeur ou au marchand de sommeil."),
        ("Ce qu'elle coûte au salarié français",
         "Une concurrence qui ne peut ni se syndiquer, ni refuser, ni porter "
         "plainte : le pire concurrent possible sur un marché du travail."),
        ("Ce qu'elle coûte à l'État",
         "Des cotisations jamais perçues, un contentieux massif, et environ "
         "1,8 milliard par an de lutte que la Cour des comptes juge "
         "inefficace." + g.renvoi("irreguliere-cout")),
        ("Ce qu'elle coûte à la confiance",
         "Une loi que chacun sait inappliquée nourrit l'idée que l'État ne "
         "contrôle plus rien — le carburant du discours le plus dur."),
    ])

    corps += """
<h2 id="recherche">Ce que dit la recherche économique — et ce qu'elle ne dit pas</h2>
<p>Le débat français se passe souvent d'elle. Elle existe pourtant, elle est
abondante, et ses résultats sont plus stables que les discours ne le laissent
croire. Ils sont aussi plus disputés que ne le laisse croire le camp qui nous
est favorable, et nous préférons l'écrire.</p>
"""

    corps += g.tableau(
        ["Question", "Ce que trouve la littérature", "Ce qui reste disputé"],
        [["Effet sur les salaires des natifs",
          "Faible à nul en moyenne ; les effets négatifs, quand ils "
          "apparaissent, se concentrent sur les immigrés déjà installés et "
          "sur les natifs les moins qualifiés du même bassin",
          "L'épisode de Mariel (Card, 1990), longtemps donné comme preuve, a "
          "été contesté par Borjas (2016) puis redéfendu par Peri et Yasenov. "
          "La controverse n'est pas tranchée : qui la cache s'expose"],
         ["Effet sur l'emploi des natifs",
          "Pas d'effet de substitution massif à l'échelle d'un pays : "
          "l'arrivée de travailleurs crée aussi de la demande, des "
          "entreprises et des emplois",
          "Dustmann, Schönberg et Stuhler trouvent au contraire, sur les "
          "navetteurs tchèques, des effets négatifs marqués sur l'emploi "
          "local. L'ampleur dépend de la rigidité des salaires et de la "
          "vitesse d'ajustement"],
         ["Solde budgétaire",
          "Proche de zéro, de l'ordre de quelques dixièmes de point de PIB, "
          "positif ou négatif selon la méthode et l'âge des arrivants",
          "Très sensible aux conventions : imputation des biens publics, "
          "horizon retenu, traitement des descendants. Aucun chiffre unique "
          "ne fait consensus"]],
        legende="Synthèse des ordres de grandeur issus de la littérature "
                "économique (voir Sources). Les études citées portent sur des "
                "pays et des périodes différents ; <strong>aucune ne dit ce "
                "que produirait exactement la réforme proposée ici</strong>, "
                "et c'est la limite principale de tout cet argumentaire.",
        classes_colonnes=["texte", "long", "long"])

    corps += g.note(
        "<p><strong>Le chiffre qui change tout est celui-ci :</strong> à "
        "compétences égales, un même travailleur produit et gagne plusieurs "
        "fois plus en France que dans un pays pauvre. Cet écart — la « prime "
        "de lieu » — est la plus grande inefficacité connue de l'économie "
        "mondiale. La lever, même partiellement, enrichit à la fois celui qui "
        "vient, le pays qui accueille, et la famille restée au pays, dont les "
        "transferts reçus dépassent largement l'aide publique au "
        "développement.</p>"
        "<p><strong>Et voici sa limite, que Clemens énonce lui-même.</strong> "
        "Ce calcul suppose que les institutions du pays d'accueil — droit, "
        "confiance, administration — continuent de produire cette "
        "productivité. C'est une hypothèse, pas un résultat. Elle est "
        "raisonnable pour des flux de l'ordre de ceux dont il est question "
        "ici ; elle cesserait de l'être à une tout autre échelle. C'est l'une "
        "des raisons pour lesquelles ce programme est borné, et le "
        "<a href=\"index.html#limites\">dit</a>.</p>", "vigilance")

    corps += """
<h2 id="faux-debat">Trois faux débats</h2>
"""

    corps += g.depliant(
        "« Il faut des quotas votés par le Parlement »",
        "<p>Un quota fixe un nombre à l'avance, sans savoir quels emplois "
        "existeront l'an prochain ni qui se présentera. Il ne dit rien de la "
        "qualité des dossiers et ne supprime aucun délai : il ajoute une "
        "contrainte de volume à une machine déjà lente. Et il ne s'applique "
        "ni à l'asile, ni aux Européens, ni aux liens familiaux protégés par "
        "la Constitution et la Convention européenne des droits de l'homme "
        "— c'est-à-dire à la majeure partie des entrées. Le Conseil "
        "constitutionnel a censuré la disposition en 2024.</p>"
        "<p>Le libéralisme lui préfère des <strong>critères</strong> : des "
        "conditions écrites, vérifiables, connues d'avance, que chacun sait "
        "remplir ou non. Un critère se conteste devant un juge ; un quota "
        "épuisé ne se conteste pas.</p>"
        "<p><strong>Mais refuser les quotas ne dispense pas de répondre à la "
        "question qu'ils posent</strong> : qui décide, et comment le peuple "
        "reprend-il la main s'il juge que c'est trop ? C'est l'objet de notre "
        "<a href=\"programme.html#sept\">septième engagement</a>, et nous ne "
        "prétendons pas que la question était illégitime.</p>")

    corps += g.depliant(
        "« L'immigration coûte X milliards »",
        "<p>Tout dépend de ce qu'on compte. Les études sérieuses incluent les "
        "impôts et cotisations versés, les prestations reçues, les biens "
        "publics consommés, et l'effet sur la croissance ; elles aboutissent à "
        "un solde proche de zéro. Les chiffres spectaculaires s'obtiennent en "
        "comptant les dépenses sans les recettes, ou en imputant aux immigrés "
        "une part des dépenses générales de l'État.</p>"
        "<p>La bonne question n'est pas « combien coûte l'immigration ? » mais "
        "« combien coûte l'immigration <em>empêchée de travailler</em> ? ». À "
        "celle-là, la réponse est chiffrable, et nous la chiffrons dans "
        "<a href=\"programme.html#chiffrage\">le programme</a> : "
        "l'hébergement et l'allocation de l'attente, la lutte contre "
        "l'irrégularité, et les cotisations non perçues.</p>")

    corps += g.depliant(
        "« On ne peut pas accueillir toute la misère du monde »",
        "<p>La phrase de Michel Rocard, souvent tronquée, se poursuivait par "
        "« mais elle doit en prendre fidèlement sa part ». Le débat utile "
        "n'est pas entre zéro et l'infini : c'est celui des règles. Personne "
        "ici ne propose la suppression des frontières ni l'accès automatique "
        "de tous à tout, et nous avons écrit "
        "<a href=\"index.html#limites\">où nous nous arrêtons</a> plutôt que "
        "de laisser la question ouverte.</p>"
        "<p>La proposition libérale est bornée et vérifiable : un droit de "
        "venir travailler quand un employeur embauche, un contrôle réel des "
        "identités et des casiers judiciaires, les règles de solidarité "
        "existantes inchangées, l'exécution effective des décisions "
        "d'éloignement, et un réexamen annuel devant le Parlement. C'est plus "
        "sélectif que le système actuel sur ce qui compte — la sécurité, la "
        "fraude — et beaucoup plus ouvert sur ce qui enrichit tout le monde : "
        "le travail.</p>")

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html">Lire la proposition</a>
  <a href="objections.html">Les objections sérieuses</a>
</div>
"""
    return corps
