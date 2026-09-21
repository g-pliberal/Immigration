"""Les objections sérieuses, et ce qu'on y répond.

Une page de programme qui n'expose que ses arguments ne convainc personne :
elle donne au lecteur le sentiment, souvent juste, qu'on lui cache la moitié
du dossier. Les objections reprises ici sont celles qui se tiennent — pas des
épouvantails commodes —, et plusieurs ne reçoivent pas de réponse complète.
C'est dit.

Quatre objections ont été ajoutées après relecture. Les sept premières étaient
toutes économiques ou juridiques : la page répondait très bien à des questions
d'économiste et pas du tout à celles qu'on pose réellement dans le débat
français. Une objection qu'on n'écrit pas est une objection qu'on paraît
craindre.
"""

from __future__ import annotations

from .. import gabarit as g

PAGE = {
    "fichier": "objections.html",
    "titre": "Objections — et ce que nous y répondons",
    "description": (
        "Appel d'air, salaires, logement, services publics, intégration, "
        "identité, sécurité, souveraineté, État-providence, sous-citoyenneté, "
        "fuite des cerveaux : onze objections au programme libéral sur "
        "l'immigration, et leurs réponses."),
}


def construire() -> str:
    corps = g.affiche(
        "Pour aller plus loin",
        "Les objections <span class=\"serif\">qui se tiennent</span>",
        "Onze objections, dans leur version forte — celle que formulerait "
        "quelqu'un d'informé et de bonne foi, pas la caricature qu'il est "
        "facile de renverser. Elles viennent de la droite, de la gauche, et "
        "de gens qui ne sont d'aucun camp.")

    corps += g.plan([
        ("appel-air", "L'appel d'air"),
        ("salaires", "Les salaires"),
        ("logement", "Le logement"),
        ("services-publics", "L'école et l'hôpital"),
        ("integration", "L'intégration"),
        ("identite", "L'identité et la laïcité"),
        ("securite", "La sécurité"),
        ("souverainete", "Qui décide ?"),
        ("providence", "L'État-providence"),
        ("sous-citoyennete", "Une main-d'œuvre, pas des gens"),
        ("cerveaux", "La fuite des cerveaux"),
    ])

    corps += g.cle(
        "« Vous allez créer un appel d'air »",
        "En partie, oui — et c'est assumé pour le travail. Une règle plus "
        "simple fera venir davantage de gens qui viennent travailler.",
        corps="<p>Ce que la recherche montre, c'est que les flux répondent "
              "surtout à la demande de travail et aux réseaux déjà installés, "
              "et beaucoup moins aux règles d'accès aux prestations. Notre "
              "réforme agit précisément là : elle ouvre la voie légale du "
              "travail, dont l'accès suppose un contrat ou une promesse "
              "d'embauche. Elle rend la France plus attirante pour celui qui "
              "a un employeur.</p>"
              "<p><strong>Une contradiction qu'il faut corriger, parce "
              "qu'elle était dans ce site.</strong> Nous écrivions que la "
              "réforme n'était « strictement pas plus attirante » pour qui "
              "n'a pas de promesse d'embauche. C'était faux, et notre propre "
              "engagement 4 le démentait : ouvrir le travail dès le dépôt "
              "d'une demande d'asile rend bien la France plus attirante pour "
              "quelqu'un qui arrive sans employeur. Nous le maintenons — "
              "parce qu'interdire de travailler à quelqu'un dont la demande "
              "sera acceptée une fois sur deux est absurde et coûteux — mais "
              "nous cessons de prétendre que c'est sans effet.</p>"
              "<p>La contrepartie est écrite dans le même engagement : "
              "instruction en six mois, et exécution effective des rejets "
              "définitifs. C'est la rapidité, et non l'interdiction de "
              "travailler, qui empêche la demande d'asile de devenir une voie "
              "d'entrée détournée.</p>"
              "<p>Enfin, une chose que nos adversaires ont raison de "
              "souligner : <strong>nous ne savons pas chiffrer l'ampleur de "
              "la réponse</strong>. Aucun pays comparable n'a mené exactement "
              "cette politique. C'est pourquoi le programme prévoit des "
              "critères révisables et un "
              "<a href=\"programme.html#sept\">réexamen annuel</a>, et non "
              "une promesse de nombre.</p>",
        identifiant="appel-air")

    corps += g.cle(
        "« Cela fera baisser les salaires des Français »",
        "La littérature économique, très abondante, trouve des effets faibles "
        "à nuls en moyenne. Elle est aussi plus disputée qu'on ne le dit "
        "quand elle nous arrange.",
        corps="<p>La raison de fond tient en une phrase : un travailleur n'est "
              "pas seulement une offre de travail, c'est aussi une demande de "
              "biens, de services et de logement, donc des emplois. Les "
              "études d'épisodes réels — arrivées massives et soudaines — ne "
              "retrouvent pas l'effondrement des salaires que la théorie la "
              "plus simple prédit.</p>"
              "<p><strong>Et voici la controverse, plutôt que de la laisser "
              "découvrir.</strong> L'épisode de Mariel, étudié par David Card "
              "en 1990, est l'étude la plus citée et la plus contestée de "
              "toute la discipline : George Borjas en a tiré en 2016 des "
              "résultats inverses en changeant le sous-échantillon, Giovanni "
              "Peri et Vasil Yasenov ont défendu la conclusion initiale, et "
              "la question n'est pas tranchée. Dans le même esprit, les "
              "travaux de Dustmann, Schönberg et Stuhler sur les navetteurs "
              "tchèques trouvent, eux, des effets négatifs marqués sur "
              "l'emploi local. Citer ces auteurs comme s'ils allaient tous "
              "dans notre sens serait malhonnête.</p>"
              "<p>Ce qui reste solide après la controverse : les effets sont "
              "modestes à l'échelle d'un pays, ils se concentrent sur les "
              "moins qualifiés du même bassin d'emploi et sur les immigrés "
              "déjà installés, et ils dépendent de la vitesse d'ajustement "
              "des salaires et de l'investissement.</p>"
              "<p>Il y a mieux : notre réforme <em>protège</em> les salaires "
              "bas. Aujourd'hui, la concurrence la plus dure vient du travail "
              "non déclaré, où l'on ne peut ni exiger le minimum légal, ni se "
              "syndiquer, ni porter plainte. Rendre ces travailleurs légaux, "
              "c'est les obliger à coûter ce que coûte un salarié déclaré, et "
              "supprimer l'avantage de l'employeur qui triche.</p>",
        source="Card (1990) ; Borjas (2016) ; Peri et Yasenov (2019) ; "
               "Dustmann, Schönberg et Stuhler (2017) ; synthèses OCDE — voir "
               "Sources.",
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
              "pas un détail — et c'est pourquoi la tension locative figure "
              "parmi les <a href=\"programme.html#sept\">trois seuils</a> qui "
              "nous obligeraient à resserrer les critères d'entrée.</p>",
        identifiant="logement")

    corps += g.cle(
        "« L'école, l'hôpital et les transports ne suivront pas »",
        "Objection légitime, et distincte de celle du logement : elle porte "
        "sur des services publics déjà saturés, dont la capacité ne s'achète "
        "pas en un an. Nous n'avons pas de réponse miracle, et nous "
        "n'inventons pas de chiffre.",
        corps="<p>Ce qu'on peut dire honnêtement tient en trois points. "
              "<strong>Un</strong> : la charge dépend du nombre d'arrivants, "
              "que cette réforme augmente sur la voie du travail, et non du "
              "statut de ces arrivants — un enfant est scolarisé que son "
              "parent travaille légalement ou non. Notre réforme ne crée donc "
              "pas la charge scolaire ; elle en change le financement, en "
              "rendant contributeur un parent qui ne l'était pas.</p>"
              "<p><strong>Deux</strong> : la saturation est très inégalement "
              "répartie, et elle est, dans certains services, un problème "
              "d'offre de personnel que l'immigration de travail "
              "<em>résout</em> plutôt qu'elle ne l'aggrave — l'hôpital et le "
              "grand âge recrutent aujourd'hui des soignants étrangers dont "
              "le dossier attend des mois.</p>"
              "<p><strong>Trois</strong> : ce que nous ne savons pas, c'est "
              "l'effet local net, commune par commune. Il n'existe pas de "
              "travail français récent qui permette de le chiffrer. C'est une "
              "incertitude réelle, et c'est la raison pour laquelle le "
              "septième engagement existe.</p>",
        identifiant="services-publics")

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
        "« Vous ne parlez que d'économie. Une nation n'est pas un marché du travail »",
        "L'objection est juste, et elle ne se réfute pas avec des chiffres de "
        "PIB. Ce site répondait très bien à des questions d'économiste et pas "
        "du tout à celle-là — c'était un aveu de faiblesse.",
        corps="<p>Disons d'abord ce que nous ne concédons pas. L'idée d'un "
              "remplacement de population ne décrit pas ce que montrent les "
              "chiffres : huit millions d'immigrés, dont un tiers sont "
              "français, dans un pays de 68 millions d'habitants, avec une "
              "rupture de série statistique qui interdit même de lire "
              "correctement l'évolution récente."
              + g.renvoi("immigres") + " Une politique publique ne se bâtit "
              "pas sur une thèse que ses propres données contredisent.</p>"
              "<p>Cela dit, l'objection sérieuse demeure, et elle est "
              "celle-ci : <em>une société absorbe à un rythme, et ce rythme "
              "n'est pas une variable économique</em>. Trois éléments de "
              "réponse, dont aucun n'est une réfutation complète.</p>"
              "<p><strong>L'emploi est le premier lien d'appartenance</strong>, "
              "avant la langue et avant l'école — et notre droit commence par "
              "l'interdire. Un homme qui travaille, paie ses cotisations et "
              "peut changer de patron n'est pas dans la même situation "
              "sociale que le même homme maintenu trois ans dans l'attente et "
              "l'informel. C'est le seul levier d'intégration que ce "
              "programme actionne, mais c'est le plus puissant qu'une loi "
              "sache actionner.</p>"
              "<p><strong>La laïcité et l'ordre public ne se négocient "
              "pas</strong>, et ce n'est pas une concession que nous ferions "
              "à contrecœur : ce sont les conditions auxquelles une société "
              "peut se permettre d'être ouverte sur le reste. La loi "
              "s'applique à tous, sans accommodement, et un libéral n'a "
              "aucune raison de s'en excuser.</p>"
              "<p><strong>Et ce que nous ne savons pas.</strong> Le rythme "
              "auquel une société absorbe ne se mesure pas comme un solde "
              "budgétaire. Nous n'avons pas d'indicateur honnête à proposer, "
              "et nous refusons d'en fabriquer un pour faire croire que la "
              "question est réglée. C'est une raison de plus de soumettre les "
              "critères d'entrée à un "
              "<a href=\"programme.html#sept\">débat annuel</a> plutôt qu'à "
              "une règle figée.</p>",
        identifiant="identite")

    corps += g.cle(
        "« Et la sécurité ? »",
        "Un programme libéral n'a aucune raison d'être laxiste sur la "
        "délinquance — et toutes les raisons de vouloir un État qui puisse "
        "réellement éloigner un étranger condamné.",
        corps="<p>Aujourd'hui, l'administration prononce environ 140 000 "
              "décisions d'éloignement pour en exécuter de l'ordre de 11 %, "
              "et ses moyens sont dispersés sur cette masse. En cessant de "
              "poursuivre des gens dont le seul tort est de travailler sans "
              "l'accord d'un service, elle concentre ses moyens sur les "
              "étrangers condamnés et les menaces avérées — où l'éloignement "
              "est justifié, et où il devient possible.</p>"
              "<p><strong>Une honnêteté qui nous coûte un argument.</strong> "
              "Les éloignements augmentent : 24 985 l'an dernier, dont 15 569 "
              "forcés, en hausse de 15,7 % et de 21 %."
              + g.renvoi("eloignements") + " Dire que « rien ne bouge » "
              "n'est plus exact, et nous ne le dirons pas. Ce qui reste vrai, "
              "c'est l'écart entre le nombre de décisions écrites et le "
              "nombre de départs réalisés — et cet écart-là, une loi ne le "
              "comble pas : il dépend de laissez-passer consulaires que "
              "seule une négociation diplomatique obtient.</p>"
              "<p>S'y ajoutent deux gains directs de la régularisation du "
              "travail : des identités établies et vérifiées plutôt qu'une "
              "population sans existence administrative, et des victimes ou "
              "témoins qui peuvent enfin aller au commissariat sans risquer "
              "l'expulsion.</p>",
        identifiant="securite")

    corps += g.cle(
        "« Vous refusez les quotas : alors plus personne ne décide »",
        "L'objection est fondée, et notre première version n'y répondait pas. "
        "Nous maintenons le refus des quotas — pour des raisons juridiques, "
        "pas idéologiques — et nous rendons la décision au Parlement par un "
        "autre chemin.",
        corps="<p>Pourquoi les quotas ne marchent pas : ils ne s'appliquent ni "
              "à l'asile, ni aux Européens, ni aux liens familiaux protégés "
              "par la Constitution et la Convention européenne des droits de "
              "l'homme, c'est-à-dire à la majeure partie des entrées ; le "
              "Conseil constitutionnel les a censurés en 2024 ; et un plafond "
              "épuisé ne se conteste pas devant un juge, alors qu'un critère "
              "se conteste.</p>"
              "<p>Ce que nous mettons à la place n'est pas rien : les "
              "critères d'entrée — durée de présence, durée d'activité, "
              "seuils de rémunération — sont fixés <strong>par la loi</strong> "
              "et révisables par elle chaque année, à la hausse comme à la "
              "baisse, sur la base d'indicateurs publiés à l'avance. Le "
              "Parlement ne vote pas un nombre ; il règle des conditions, ce "
              "qui produit un effet sur le nombre et reste attaquable devant "
              "un juge.</p>"
              "<p><strong>Et le référendum ?</strong> La décision du Conseil "
              "constitutionnel du 11 avril 2024 montre que même la voie "
              "référendaire est bornée par les droits constitutionnellement "
              "garantis. Promettre de trancher la question par référendum "
              "sans le dire serait vendre une solution qu'on ne peut pas "
              "livrer.</p>",
        source="Conseil constitutionnel, décisions n° 2023-863 DC du "
               "25 janvier 2024 et n° 2024-6 RIP du 11 avril 2024.",
        identifiant="souverainete")

    corps += g.cle(
        "« Frontières ouvertes et État-providence sont incompatibles »",
        "Nous sommes d'accord avec Milton Friedman : il faut choisir. Nous "
        "choisissons d'ouvrir <strong>le travail</strong> — et nous avons "
        "renoncé à la carence sociale que nous proposions, parce qu'elle est "
        "inconstitutionnelle.",
        corps="<p>La version précédente de ce programme différait de cinq ans "
              "l'accès des étrangers en séjour régulier aux prestations non "
              "contributives. Le Conseil constitutionnel a jugé le "
              "<strong>11 avril 2024</strong> qu'une condition de cinq ans de "
              "résidence portait une « atteinte disproportionnée » aux "
              "exigences des dixième et onzième alinéas du Préambule de "
              "1946 — sur le fond, et non pour un motif de procédure comme "
              "cette page l'écrivait à tort. S'y ajoutent la directive "
              "européenne sur le permis unique, la jurisprudence de la CJUE "
              "et trente-neuf conventions bilatérales de sécurité sociale.</p>"
              "<p><strong>Notre réponse à Friedman ne passe donc plus par la "
              "carence, mais par la condition d'entrée elle-même.</strong> La "
              "voie que nous ouvrons exige un contrat ou une promesse "
              "d'embauche : elle n'est pas, par construction, une voie "
              "d'accès à l'aide sociale. Un travailleur déclaré cotise dès le "
              "premier mois. Et les durées de résidence qui existent "
              "déjà — cinq ans pour le RSA, dix pour l'ASPA — sont "
              "maintenues, sans qu'aucune soit ajoutée. Le "
              "<a href=\"programme.html#cinq\">tableau prestation par "
              "prestation</a> dit exactement ce qui change : rien.</p>"
              "<p>Cette réponse est moins spectaculaire que la précédente. "
              "Elle a l'avantage d'exister encore après le contrôle de "
              "constitutionnalité.</p>",
        source="M. Friedman, conférence de 1978 ; Conseil constitutionnel, "
               "décision n° 2024-6 RIP du 11 avril 2024 ; directive "
               "2011/98/UE, art. 12 ; CJUE, 19 décembre 2024, C-664/23.",
        identifiant="providence")

    corps += g.cle(
        "« Vous voulez de la main-d'œuvre, pas des habitants »",
        "C'est l'objection de gauche, et elle mérite mieux que le silence : "
        "un droit au séjour adossé à un contrat de travail fait bien du "
        "séjour une fonction de l'utilité économique. Nous l'assumons en "
        "partie, et nous la corrigeons sur trois points précis.",
        corps="<p><strong>Ce que nous assumons.</strong> Oui, la voie que ce "
              "programme ouvre est une voie de travail, donc sélective. Elle "
              "ne remplace ni l'asile, ni le droit de vivre en famille, qui "
              "sont des droits et non des sélections — et que ce programme "
              "laisse intacts.</p>"
              "<p><strong>Ce que nous corrigeons.</strong> D'abord, le titre "
              "<em>n'est plus attaché à l'employeur</em> : c'est exactement "
              "l'inverse d'un programme patronal, puisque c'est le lien de "
              "dépendance qui permet aujourd'hui de payer moins et d'exiger "
              "plus. Ensuite, le titre <a href=\"programme.html#perte-emploi\">"
              "survit douze mois à la perte d'emploi</a> : un licenciement ne "
              "vaut pas expulsion. Enfin, la rémunération doit atteindre le "
              "minimum légal de la branche, ce qui retire tout intérêt à "
              "recruter à l'étranger pour payer moins.</p>"
              "<p><strong>Et ce que nous avons retiré.</strong> La carence de "
              "cinq ans sur les prestations créait précisément la "
              "sous-citoyenneté que cette objection dénonce : cotiser "
              "pleinement en recevant partiellement, pendant cinq ans. Elle "
              "ne figure plus au programme. La critique a porté.</p>",
        identifiant="sous-citoyennete")

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
        "<p><strong>Ce que nous ne savons pas.</strong> L'ampleur de la "
        "réponse migratoire à une ouverture du travail ; l'effet local sur "
        "les loyers et sur les services publics pendant les années "
        "d'ajustement ; le rythme auquel une société absorbe, qui ne se "
        "mesure pas comme un solde budgétaire ; et l'effet net de la réforme "
        "sur le volume du contentieux, puisque éloigner davantage en produit. "
        "Une page de programme qui prétendrait avoir la réponse à ces quatre "
        "questions mentirait.</p>"
        "<p><strong>Et ce sur quoi nous avons changé d'avis</strong>, à force "
        "de nous faire ces objections nous-mêmes : la carence de cinq ans sur "
        "les prestations, abandonnée ; l'asile en trois mois, devenu six ; le "
        "« strictement pas plus attirant », retiré ; et les 40 % du "
        "contentieux administratif, ramenés à ce qu'ils sont.</p>",
        "avertissement")

    corps += """
<div class="actions">
  <a class="bouton" href="chiffres.html">Vérifier tous les chiffres</a>
  <a href="programme.html">Relire le programme</a>
</div>
"""
    return corps
