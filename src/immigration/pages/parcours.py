"""Parcours comparés : le même cas, sous le droit actuel et sous la réforme.

Les données sont écrites ici, en Python, et déposées dans la page sous forme
de JSON : le comparateur les lit sans qu'aucun chiffre n'existe en double.

**Trois colonnes, et non deux.** La version précédente mettait en regard des
délais CONSTATÉS aujourd'hui et des délais PROMIS par la réforme : deux barres
qui n'ont pas la même nature, comparées sur la même échelle. Un journaliste
avait raison d'appeler cela trompeur. La colonne du milieu rétablit la
comparaison honnête — ce que la loi garantit aujourd'hui, c'est-à-dire presque
rien —, et les barres promises sont hachurées pour qu'on ne les confonde pas
avec des mesures.

Deux autres corrections, moins visibles et tout aussi nécessaires :

* **l'étape consulaire est rétablie** dans la colonne proposée. Le visa long
  séjour relève du code des visas européen ; le programme ne le supprime pas
  et ne peut pas le supprimer. La faire disparaître de notre colonne, c'était
  s'attribuer un gain que la réforme ne produit pas ;
* **la durée de présence exigée apparaît** comme une étape, y compris quand
  elle vaut zéro mois pour le cas considéré. L'engagement 1 la conserve comme
  critère ; le comparateur l'avait effacée.
"""

from __future__ import annotations

import json

from .. import gabarit as g

PAGE = {
    "fichier": "parcours.html",
    "titre": "Parcours comparés — aujourd'hui et sous la réforme",
    "description": (
        "Ingénieure, aide-soignante, saisonnier, étudiant diplômé, demandeur "
        "d'asile : combien de temps avant de travailler légalement en France "
        "en pratique, ce que la loi garantit aujourd'hui, et ce qu'elle "
        "garantirait sous le programme libéral."),
}

# Une étape : [libellé, durée en mois]. Une durée `null` signifie « aucun délai
# opposable » — c'est le cas général de la colonne du milieu, et c'est tout
# l'argument : aujourd'hui, la loi ne promet rien.
INDEFINI = None

CAS = [
    {
        "cle": "ingenieur",
        "nom": "Ingénieure recrutée par une PME",
        "resume": "Diplômée d'un master, hors Union européenne, encore à "
                  "l'étranger, embauchée en CDI par une entreprise de "
                  "40 salariés.",
        "colonnes": [
            {"genre": "constate", "titre": "Aujourd'hui, en pratique",
             "etapes": [
                 ["Recherche d'un employeur prêt à faire les démarches", 3],
                 ["Demande d'autorisation de travail par l'employeur", 2],
                 ["Instruction, situation de l'emploi comprise", 2],
                 ["Demande de visa long séjour au consulat", 2],
                 ["Validation du titre en préfecture après l'arrivée", 1],
             ]},
            {"genre": "garanti", "titre": "Aujourd'hui, ce que la loi garantit",
             "etapes": [
                 ["Instruction du permis : quatre mois (directive 2011/98), "
                  "sans sanction si le délai est dépassé", 4],
                 ["Autorisation de travail et visa : aucun délai opposable, "
                  "et le silence vaut refus", INDEFINI],
             ]},
            {"genre": "promesse",
             "titre": "Avec le programme, ce que la loi garantirait",
             "etapes": [
                 ["Recherche d'un employeur (inchangée)", 3],
                 ["Dépôt en ligne : contrat, identité, casier", 0.5],
                 ["Décision ou silence valant accord (8 semaines)", 2],
                 ["Visa long séjour au consulat — étape maintenue, code des "
                  "visas européen", 2],
             ]},
        ],
        "note": "Le titre « talent » existe pour les diplômés très bien "
                "rémunérés et raccourcit le parcours actuel — mais il ne "
                "couvre qu'une petite partie des recrutements. Et le gain de "
                "la réforme est ici plus faible qu'annoncé dans notre "
                "première version : l'étape consulaire subsiste.",
    },
    {
        "cle": "aide-soignante",
        "nom": "Aide-soignante dans un Ehpad",
        "resume": "Déjà en France depuis trois ans, employée sans titre dans "
                  "un établissement qui ne trouve personne.",
        "colonnes": [
            {"genre": "constate", "titre": "Aujourd'hui, en pratique",
             "etapes": [
                 ["Attente des trois ans de présence exigés (art. L. 435-4)", 12],
                 ["Constitution du dossier d'admission exceptionnelle", 3],
                 ["Obtention de l'accord écrit de l'employeur", 3],
                 ["Instruction préfectorale, décision discrétionnaire", 6],
                 ["Recours en cas de refus, fréquent", 8],
             ]},
            {"genre": "garanti", "titre": "Aujourd'hui, ce que la loi garantit",
             "etapes": [
                 ["Aucun droit : l'admission exceptionnelle est "
                  "discrétionnaire, et l'article L. 435-4 expire le "
                  "31 décembre 2026", INDEFINI],
             ]},
            {"genre": "promesse",
             "titre": "Avec le programme, ce que la loi garantirait",
             "etapes": [
                 ["Durée de présence exigée : douze mois — déjà atteinte ici", 0],
                 ["Durée d'activité exigée : six mois — déjà atteinte ici", 0],
                 ["Preuve du travail par faisceau d'indices", 1],
                 ["Dépôt en ligne : identité, casier, employeur identifié", 0.5],
                 ["Décision ou silence valant accord (8 semaines)", 2],
             ]},
        ],
        "note": "C'est le cas que la loi de 2024 a voulu traiter par une voie "
                "« métiers en tension » temporaire, discrétionnaire, et qui "
                "expire dans quelques semaines. Les deux premières étapes de "
                "la colonne de droite valent zéro mois pour elle, mais "
                "existent : le programme conserve une durée de présence, et "
                "le comparateur doit la montrer.",
    },
    {
        "cle": "saisonnier",
        "nom": "Saisonnier agricole",
        "resume": "Quatre mois de récolte, un employeur identifié, un retour "
                  "prévu au pays.",
        "colonnes": [
            {"genre": "constate", "titre": "Aujourd'hui, en pratique",
             "etapes": [
                 ["Demande d'autorisation de travail saisonnier", 2],
                 ["Visa consulaire", 2],
                 ["Formalités à l'arrivée", 0.5],
                 ["Et tout recommence à la saison suivante", 4.5],
             ]},
            {"genre": "garanti", "titre": "Aujourd'hui, ce que la loi garantit",
             "etapes": [
                 ["Aucun délai opposable, et la récolte n'attend pas",
                  INDEFINI],
             ]},
            {"genre": "promesse",
             "titre": "Avec le programme, ce que la loi garantirait",
             "etapes": [
                 ["Dépôt en ligne par l'employeur, réponse sous quinze jours",
                  0.5],
                 ["Visa consulaire — étape maintenue", 2],
                 ["Saisons suivantes : titre pluriannuel, aucune démarche", 0],
             ]},
        ],
        "note": "Ici le problème n'est pas le volume mais le calendrier : une "
                "récolte n'attend pas quatre mois d'instruction, et c'est "
                "ainsi que le travail non déclaré s'installe dans un secteur "
                "entier. Les titres saisonniers ont reculé d'environ 30 % en "
                "un an.",
    },
    {
        "cle": "etudiant",
        "nom": "Étudiant diplômé d'un master français",
        "resume": "Formé en France, aux frais partagés du contribuable "
                  "français et de sa famille, il cherche un premier emploi.",
        "colonnes": [
            {"genre": "constate", "titre": "Aujourd'hui, en pratique",
             "etapes": [
                 ["Autorisation provisoire de séjour après le diplôme", 2],
                 ["Recherche d'emploi, durée limitée par le titre", 6],
                 ["Changement de statut étudiant vers salarié", 4],
                 ["Instruction et validation du nouveau titre", 3],
             ]},
            {"genre": "garanti", "titre": "Aujourd'hui, ce que la loi garantit",
             "etapes": [
                 ["Durée de l'autorisation provisoire de séjour", 12],
                 ["Changement de statut : aucun délai opposable, et le "
                  "silence vaut refus", INDEFINI],
             ]},
            {"genre": "promesse",
             "titre": "Avec le programme, ce que la loi garantirait",
             "etapes": [
                 ["Le titre étudiant vaut autorisation de travailler", 0],
                 ["Recherche d'emploi sans horloge administrative", 6],
                 ["Simple déclaration de changement de situation", 0.5],
             ]},
        ],
        "note": "Former un ingénieur puis l'obliger à partir faute de "
                "changement de statut dans les délais est la définition même "
                "d'une politique qui se nuit à elle-même. Aucune étape "
                "consulaire ici : il est déjà en France.",
    },
    {
        "cle": "asile",
        "nom": "Demandeur d'asile",
        "resume": "Arrivé avec une demande recevable, il veut travailler en "
                  "attendant la décision. Plus d'une demande sur deux aboutit "
                  "aujourd'hui à une protection.",
        "colonnes": [
            {"genre": "constate", "titre": "Aujourd'hui, en pratique",
             "etapes": [
                 ["Enregistrement au guichet unique", 1],
                 ["Interdiction de travailler pendant six mois", 6],
                 ["Instruction OFPRA", 5],
                 ["Recours devant la CNDA", 9],
             ]},
            {"genre": "garanti", "titre": "Aujourd'hui, ce que la loi garantit",
             "etapes": [
                 ["Accès au travail : au-delà de six mois, et sur "
                  "autorisation (CESEDA, art. L. 554-1)", 6],
                 ["Instruction et recours : aucun délai total opposable",
                  INDEFINI],
             ]},
            {"genre": "promesse",
             "titre": "Avec le programme, ce que la loi garantirait",
             "etapes": [
                 ["Enregistrement, droit de travailler ouvert aussitôt", 0.5],
                 ["Instruction et recours : six mois opposables, trois à "
                  "terme", 6],
             ]},
        ],
        "note": "Le parcours proposé est plus court pour tout le monde : "
                "protection accordée plus vite à qui y a droit — c'est "
                "désormais la majorité —, décision de rejet exécutable pour "
                "les autres, avant qu'une vie entière se soit installée. Six "
                "mois et non trois : voir l'engagement 4.",
    },
]

# L'échelle des barres, en mois. Elle doit dépasser le parcours le plus long —
# 32 mois pour l'aide-soignante —, faute de quoi la barre est écrêtée et
# affiche 24 mois sous un total qui en annonce 32. C'était le cas.
DUREE_MAX = 36


def construire() -> str:
    corps = g.affiche(
        "La proposition",
        "Le même cas, <span class=\"serif\">trois colonnes</span>",
        "Une politique migratoire ne se juge pas sur un principe mais sur ce "
        "qu'elle fait subir à quelqu'un. Choisissez une situation : la page "
        "montre ce qui se passe aujourd'hui, ce que la loi garantit "
        "aujourd'hui — c'est-à-dire presque rien — et ce qu'elle garantirait "
        "sous le programme.")

    options = "".join(
        f'<option value="{c["cle"]}">{c["nom"]}</option>' for c in CAS)

    corps += f"""
<div class="creme" id="comparateur">
  <p class="surtitre">Comparateur</p>
  <h2>Combien de temps avant de travailler légalement&nbsp;?</h2>
  <form class="filtres" id="choix">
    <div>
      <label for="cas">Situation</label>
      <select id="cas" name="cas">{options}</select>
    </div>
  </form>
  <p class="discret" id="resume-cas"></p>
  <ul class="legende-barres">
    <li><span class="temoin constate" aria-hidden="true"></span>Plein&nbsp;:
    délai <strong>constaté</strong></li>
    <li><span class="temoin garanti" aria-hidden="true"></span>Hachuré&nbsp;:
    délai <strong>promis par un texte</strong></li>
  </ul>
  <div id="resultat" aria-live="polite"></div>
  <noscript>
    <p>Le comparateur a besoin de JavaScript. Les mêmes parcours sont décrits
    en toutes lettres dans <a href="aujourdhui.html">Aujourd'hui</a> et dans
    <a href="programme.html">Le programme</a>.</p>
  </noscript>
</div>
"""

    corps += g.note(
        "<p><strong>Ce que ces barres comparent, et ce qu'elles ne comparent "
        "pas.</strong> La première colonne agrège des délais constatés — "
        "recherche d'employeur comprise, quand elle conditionne la "
        "démarche — et varie fortement selon la préfecture, la nationalité et "
        "le dossier. Les deux autres sont des <em>promesses de texte</em>, "
        "hachurées pour cette raison : celle du milieu est la promesse du "
        "droit actuel, celle de droite serait celle de la loi que nous "
        "proposons. Comparer une mesure à une promesse sans le dire serait "
        "trompeur, et ce comparateur le faisait.</p>", "avertissement")

    corps += """
<h2 id="lecture">Ce que ces parcours ont en commun</h2>
<p>Dans les cinq cas, la différence ne vient pas d'un assouplissement des
conditions : l'identité est vérifiée, le casier consulté, le contrat contrôlé
dans les trois colonnes, et l'étape consulaire subsiste pour qui arrive de
l'étranger. Elle vient de trois choses, et de trois seulement.</p>
"""

    corps += g.points([
        ("L'acte qu'on supprime",
         "L'autorisation de travail, doublon d'un titre de séjour qui dit déjà "
         "qui est là et à quel titre."),
        ("Le délai qu'on borne",
         "Huit semaines et un silence valant accord transforment une attente "
         "indéfinie — la colonne du milieu — en une date connue d'avance."),
        ("Le pouvoir discrétionnaire qu'on remplace",
         "Des critères écrits et chiffrés, opposables devant un juge, au lieu "
         "d'une appréciation au cas par cas qu'aucun demandeur ne peut "
         "anticiper."),
    ])

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html">Lire les sept engagements</a>
  <a href="objections.html">Les objections</a>
</div>
"""

    donnees = json.dumps({"cas": CAS, "dureeMax": DUREE_MAX},
                         ensure_ascii=False, indent=1)
    corps += (f'<script type="application/json" id="donnees-parcours">'
              f"{donnees}</script>")
    return corps


SCRIPTS = '<script src="moteur/js/parcours.js" defer></script>'
