"""Parcours comparés : le même cas, sous le droit actuel et sous la réforme.

Les données sont écrites ici, en Python, et déposées dans la page sous forme
de JSON : le comparateur les lit sans qu'aucun chiffre n'existe en double.
Les durées sont des ORDRES DE GRANDEUR de délais constatés, pas des
engagements de l'administration — la page le dit à l'écran, pas seulement
dans ce commentaire.
"""

from __future__ import annotations

import json

from .. import gabarit as g

PAGE = {
    "fichier": "parcours.html",
    "titre": "Parcours comparés — aujourd'hui et sous la réforme",
    "description": (
        "Ingénieur, aide-soignante, saisonnier, étudiant diplômé, demandeur "
        "d'asile : combien de temps avant de travailler légalement en France "
        "aujourd'hui, et combien sous le programme libéral."),
}

# Chaque cas : les étapes du droit actuel et celles de la réforme, avec la
# durée de chacune en mois. `note` dit ce que le cas a de particulier.
CAS = [
    {
        "cle": "ingenieur",
        "nom": "Ingénieure recrutée par une PME",
        "resume": "Diplômée d'un master, hors Union européenne, embauchée en "
                  "CDI par une entreprise de 40 salariés.",
        "actuel": [
            ["Recherche d'un employeur prêt à faire les démarches", 3],
            ["Demande d'autorisation de travail par l'employeur", 2],
            ["Instruction, situation de l'emploi comprise", 2],
            ["Demande de visa long séjour au consulat", 2],
            ["Validation du titre en préfecture après l'arrivée", 1],
        ],
        "propose": [
            ["Recherche d'un employeur", 3],
            ["Dépôt en ligne du dossier : contrat, identité, casier", 0.5],
            ["Décision ou silence valant accord (8 semaines)", 2],
        ],
        "note": "Le titre « talent » existe pour les diplômés très bien "
                "rémunérés et raccourcit ce parcours — mais il ne couvre "
                "qu'une petite partie des recrutements.",
    },
    {
        "cle": "aide-soignante",
        "nom": "Aide-soignante dans un Ehpad",
        "resume": "Déjà en France depuis trois ans, employée sans titre dans "
                  "un établissement qui ne trouve personne.",
        "actuel": [
            ["Attente de la durée de présence exigée par la circulaire", 12],
            ["Constitution du dossier d'admission exceptionnelle", 3],
            ["Obtention de l'accord écrit de l'employeur", 3],
            ["Instruction préfectorale, décision discrétionnaire", 6],
            ["Recours en cas de refus, fréquent", 8],
        ],
        "propose": [
            ["Dépôt en ligne : emploi déclaré, identité, casier", 0.5],
            ["Décision ou silence valant accord (8 semaines)", 2],
        ],
        "note": "C'est le cas que la loi de 2024 a voulu traiter par une voie "
                "« métiers en tension » temporaire, qui reste "
                "discrétionnaire et expire.",
    },
    {
        "cle": "saisonnier",
        "nom": "Saisonnier agricole",
        "resume": "Quatre mois de récolte, un employeur identifié, un retour "
                  "prévu au pays.",
        "actuel": [
            ["Demande d'autorisation de travail saisonnier", 2],
            ["Visa consulaire", 2],
            ["Formalités à l'arrivée", 0.5],
        ],
        "propose": [
            ["Dépôt en ligne par l'employeur, réponse sous quinze jours", 0.5],
            ["Titre saisonnier pluriannuel, réutilisable chaque saison", 0],
        ],
        "note": "Ici le problème n'est pas le volume mais le calendrier : une "
                "récolte n'attend pas quatre mois d'instruction, et c'est "
                "ainsi que le travail non déclaré s'installe dans un secteur "
                "entier.",
    },
    {
        "cle": "etudiant",
        "nom": "Étudiant diplômé d'un master français",
        "resume": "Formé en France, aux frais partagés du contribuable "
                  "français et de sa famille, il cherche un premier emploi.",
        "actuel": [
            ["Autorisation provisoire de séjour après le diplôme", 2],
            ["Recherche d'emploi, durée limitée par le titre", 6],
            ["Changement de statut étudiant vers salarié", 4],
            ["Instruction et validation du nouveau titre", 3],
        ],
        "propose": [
            ["Le titre étudiant vaut autorisation de travailler", 0],
            ["Recherche d'emploi sans horloge administrative", 6],
            ["Simple déclaration de changement de situation", 0.5],
        ],
        "note": "Former un ingénieur puis l'obliger à partir faute de "
                "changement de statut dans les délais est la définition même "
                "d'une politique qui se nuit à elle-même.",
    },
    {
        "cle": "asile",
        "nom": "Demandeur d'asile",
        "resume": "Arrivé avec une demande recevable, il veut travailler en "
                  "attendant la décision.",
        "actuel": [
            ["Enregistrement au guichet unique", 1],
            ["Interdiction de travailler pendant six mois", 6],
            ["Instruction OFPRA", 5],
            ["Recours devant la CNDA, suspensif", 9],
        ],
        "propose": [
            ["Enregistrement, droit de travailler ouvert aussitôt", 0.5],
            ["Instruction et recours, objectif trois mois", 3],
        ],
        "note": "Le parcours proposé est plus court pour tout le monde : "
                "protection accordée plus vite à qui y a droit, décision de "
                "rejet exécutable pour les autres, avant qu'une vie entière "
                "se soit installée.",
    },
]

DUREE_MAX = 24  # l'échelle des barres, en mois


def construire() -> str:
    corps = g.affiche(
        "La proposition",
        "Le même cas, <span class=\"serif\">deux parcours</span>",
        "Une politique migratoire ne se juge pas sur un principe mais sur ce "
        "qu'elle fait subir à quelqu'un. Choisissez une situation : la page "
        "montre les étapes d'aujourd'hui et celles du programme, avec les "
        "durées constatées.")

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
  <div id="resultat" aria-live="polite"></div>
  <noscript>
    <p>Le comparateur a besoin de JavaScript. Les mêmes parcours sont décrits
    en toutes lettres dans <a href="aujourdhui.html">Aujourd'hui</a> et dans
    <a href="programme.html">Le programme</a>.</p>
  </noscript>
</div>
"""

    corps += g.note(
        "<p><strong>Ces durées sont des ordres de grandeur.</strong> Elles "
        "agrègent des délais constatés — recherche d'employeur comprise, "
        "quand elle conditionne la démarche — et varient fortement selon la "
        "préfecture, la nationalité et le dossier. Elles ne valent ni "
        "engagement, ni information administrative. Les durées du parcours "
        "proposé sont celles qu'imposerait la loi que nous proposons, pas "
        "celles d'une administration observée.</p>", "avertissement")

    corps += """
<h2 id="lecture">Ce que ces parcours ont en commun</h2>
<p>Dans les cinq cas, la différence ne vient pas d'un assouplissement des
conditions : l'identité est vérifiée, le casier consulté, le contrat contrôlé
dans les deux colonnes. Elle vient de trois choses, et de trois seulement.</p>
"""

    corps += g.points([
        ("L'acte qu'on supprime",
         "L'autorisation de travail, doublon d'un titre de séjour qui dit déjà "
         "qui est là et à quel titre."),
        ("Le délai qu'on borne",
         "Huit semaines et un silence valant accord transforment une attente "
         "indéfinie en une date connue d'avance."),
        ("Le pouvoir discrétionnaire qu'on remplace",
         "Des critères écrits, opposables devant un juge, au lieu d'une "
         "appréciation au cas par cas qu'aucun demandeur ne peut anticiper."),
    ])

    corps += """
<div class="actions">
  <a class="bouton" href="programme.html">Lire les six engagements</a>
  <a href="objections.html">Les objections</a>
</div>
"""

    donnees = json.dumps({"cas": CAS, "dureeMax": DUREE_MAX},
                         ensure_ascii=False, indent=1)
    corps += (f'<script type="application/json" id="donnees-parcours">'
              f"{donnees}</script>")
    return corps


SCRIPTS = '<script src="moteur/js/parcours.js" defer></script>'
