"""Les tests du chiffrage (``src/immigration/chiffrage.py``).

Ce qu'ils vérifient, et ce qu'ils ne vérifient pas. Les chiffres changeront —
le passage aux montants de la loi de finances pour 2027 est le prochain —, et
un test qui recopierait un solde publié échouerait à chaque mise à jour sans
rien apprendre à personne. Ces tests ne figent donc AUCUN montant du
chiffrage. Ils vérifient :

* les mécanismes, sur des valeurs inventées pour l'occasion : la lecture d'un
  nombre dans le registre, les rythmes année par année, les cohortes de
  régularisations, l'attente d'asile ;
* les promesses que le module écrit dans sa documentation, sur les vraies
  hypothèses : un scénario prudent qui ne dépasse jamais le favorable, des
  lignes qui s'additionnent exactement en solde, des bornes respectées, une
  formule qui ne cite que ce que le calcul utilise ;
* que ``verifier()`` attrape bien les fautes qu'elle dit attraper.

Aucune dépendance : ``python -m unittest discover -s tests``.
"""

from __future__ import annotations

import itertools
import pathlib
import re
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from immigration import chiffrage as c  # noqa: E402
from immigration.chiffres import CHIFFRES, Chiffre  # noqa: E402

PRES = 1e-6  # tolérance en M€ : un millième d'euro


def milieux() -> dict[str, float]:
    return {k: (h.bas + h.haut) / 2 for k, h in c.HYPOTHESES.items()}


def valeurs(**surcharges: float):
    """Une ``Valeur`` inventée : les clés données, et rien d'autre."""
    table = {k.replace("_", "-"): v for k, v in surcharges.items()}
    return table.__getitem__


def fiche(valeur: str, exact: str = "") -> Chiffre:
    return Chiffre(valeur=valeur, mesure="", source="", url="", annee="",
                   exact=exact)


# ---------------------------------------------------------------------------
# La lecture du registre
# ---------------------------------------------------------------------------


class Lecture(unittest.TestCase):
    """``_lu`` : le premier nombre de la valeur publiée d'une fiche."""

    def lire(self, texte: str, echelle: float = 1.0, exact: str = "") -> float:
        with mock.patch.dict(CHIFFRES, {"essai": fiche(texte, exact)}):
            return c._lu("essai", echelle)

    def test_milliers_separes_par_une_espace(self):
        self.assertEqual(self.lire("955 080 titres"), 955_080)

    def test_espaces_insecables(self):
        self.assertEqual(self.lire("1 234 567"), 1_234_567)

    def test_virgule_decimale(self):
        self.assertAlmostEqual(self.lire("222,2 millions d'euros"), 222.2)

    def test_milliers_et_decimales(self):
        self.assertAlmostEqual(self.lire("1 234,5 €"), 1234.5)

    def test_pourcentage_avec_echelle(self):
        self.assertAlmostEqual(self.lire("52 %", echelle=0.01), 0.52)

    def test_premier_nombre_seulement(self):
        self.assertEqual(self.lire("environ 40 000, dont 12 000 mineurs"),
                         40_000)

    def test_exact_prime_sur_valeur(self):
        self.assertEqual(self.lire("environ 950 000", exact="955 080"), 955_080)

    def test_sans_nombre_echoue(self):
        with self.assertRaises(ValueError):
            self.lire("non publié")

    def test_toutes_les_fiches_lues_par_le_chiffrage_se_lisent(self):
        for h in c.HYPOTHESES.values():
            if h.chiffre:
                self.assertIn(h.chiffre, CHIFFRES)


# ---------------------------------------------------------------------------
# Les rythmes
# ---------------------------------------------------------------------------


class Rythmes(unittest.TestCase):
    """Les fonctions qui étalent un effet sur les années."""

    RYTHMES = (c._loi, c._asile, c._transition, c._rattrapage,
               c._titre_quatre_ans, c._contentieux)

    def test_entre_zero_et_un(self):
        for f, annee in itertools.product(self.RYTHMES, range(1, 11)):
            with self.subTest(rythme=f.__name__, annee=annee):
                self.assertGreaterEqual(f(annee), 0.0)
                self.assertLessEqual(f(annee), 1.0)

    def test_effets_durables_pleins_en_annee_cinq(self):
        for f in (c._loi, c._asile, c._titre_quatre_ans, c._contentieux):
            with self.subTest(rythme=f.__name__):
                self.assertEqual(f(5), 1.0)

    def test_effets_durables_croissants(self):
        for f in (c._loi, c._asile, c._titre_quatre_ans, c._contentieux):
            suite = [f(a) for a in range(1, 8)]
            with self.subTest(rythme=f.__name__):
                self.assertEqual(suite, sorted(suite))

    def test_effets_temporaires_eteints_en_annee_cinq(self):
        for f in (c._transition, c._rattrapage):
            with self.subTest(rythme=f.__name__):
                self.assertEqual(f(4), 0.0)
                self.assertEqual(f(5), 0.0)

    def test_la_loi_votee_vaut_une_demi_annee(self):
        self.assertEqual(c._loi(1), 0.5)
        self.assertEqual(c._loi(2), 1.0)

    def test_aucun_renouvellement_evite_la_premiere_annee(self):
        self.assertEqual(c._titre_quatre_ans(1), 0.0)

    def test_hors_delai_va_du_debut_au_regime(self):
        v = valeurs(hors_delai_debut=0.2, hors_delai_regime=0.02)
        suite = [c._hors_delai(v, a) for a in range(1, 7)]
        self.assertAlmostEqual(suite[0], 0.2)
        self.assertAlmostEqual(suite[1], 0.11)
        self.assertAlmostEqual(suite[2], 0.065)
        self.assertAlmostEqual(suite[3], 0.02)
        self.assertAlmostEqual(suite[5], 0.02)
        self.assertEqual(suite, sorted(suite, reverse=True))


# ---------------------------------------------------------------------------
# Les mécanismes, sur des valeurs inventées
# ---------------------------------------------------------------------------


class Mecanismes(unittest.TestCase):

    def test_renouvellements_evites(self):
        v = valeurs(renouvellements_travail_etudes=1000,
                    part_renouvellements_evites=0.5)
        self.assertEqual(c._renouvellements_evites(v, 1), 0.0)
        self.assertAlmostEqual(c._renouvellements_evites(v, 2), 250)
        self.assertAlmostEqual(c._renouvellements_evites(v, 3), 500)

    def test_reduction_asile_compte_le_mois_qui_suit_la_decision(self):
        v = valeurs(delai_asile_actuel=10, delai_asile_programme=6)
        self.assertAlmostEqual(c._reduction_asile(v), 1 - 7 / 11)

    def test_reduction_asile_nulle_a_delai_inchange(self):
        v = valeurs(delai_asile_actuel=10, delai_asile_programme=10)
        self.assertAlmostEqual(c._reduction_asile(v), 0.0)

    def test_mois_gagnes_suivent_le_rythme_de_l_asile(self):
        v = valeurs(delai_asile_actuel=10, delai_asile_programme=6)
        for a in range(1, 6):
            self.assertAlmostEqual(c._mois_gagnes(v, a), 4 * c._asile(a))

    def test_regularisations_annuelles(self):
        v = valeurs(regularisations_debut=100, regularisations_regime=300)
        self.assertEqual([c._regularisations(v, a) for a in range(1, 6)],
                         [50, 100, 100, 300, 300])

    def test_cohortes_comptees_pour_moitie_l_annee_d_entree(self):
        v = valeurs(regularisations_debut=100, regularisations_regime=300)
        self.assertEqual([c._regularises(v, a) for a in range(1, 6)],
                         [25, 100, 200, 400, 700])

    def test_cohortes_presentes_en_annee_cinq(self):
        # Une régularisation par an : une demi-cohorte l'année du vote (la loi
        # ne court que six mois), trois pleines, une demie l'année 5.
        v = valeurs(regularisations_debut=1, regularisations_regime=1)
        self.assertAlmostEqual(c._regularises(v, 5), 4.0)

    def test_la_formule_affichee_compte_les_memes_cohortes(self):
        # La formule de la sensibilité écrit le nombre de cohortes en clair :
        # il doit être celui que le calcul retient en année 5.
        s = next(s for s in c.SENSIBILITES if s.cle == "regularisations")
        ecrit = re.search(r"× ([\d,]+) cohortes", s.formule)
        self.assertIsNotNone(ecrit, s.formule)
        v = valeurs(regularisations_debut=1, regularisations_regime=1)
        self.assertAlmostEqual(float(ecrit.group(1).replace(",", ".")),
                               c._regularises(v, 5))

    def test_prelevements_par_regularise(self):
        v = valeurs(part_non_declares=0.5, prelevements_smic=10_000,
                    quotite=0.6)
        self.assertAlmostEqual(c._prelevements_par_regularise(v), 3_000)

    def test_demandeurs_au_travail(self):
        v = valeurs(delai_asile_actuel=12, delai_asile_programme=6,
                    demandes_asile=1000, part_adultes=0.8,
                    emploi_demandeurs=0.25)
        # Année 1 : 0,6 mois gagné, la loi à moitié de l'année.
        attendu = 1000 * 0.8 * (12 - 0.6) / 12 * 0.25 * 0.5
        self.assertAlmostEqual(c._demandeurs_au_travail(v, 1), attendu)
        # Régime : six mois d'attente, la loi pleine.
        self.assertAlmostEqual(c._demandeurs_au_travail(v, 5), 100)

    def test_citees(self):
        self.assertEqual(c.citees("{a} × {b-2} − {a} + {Majuscule} {}"),
                         ["a", "b-2", "a"])


# ---------------------------------------------------------------------------
# La structure du chiffrage
# ---------------------------------------------------------------------------


class Structure(unittest.TestCase):

    def test_verifier_passe(self):
        c.verifier()

    def test_cles_des_postes_uniques(self):
        cles = [p.cle for p in c.POSTES]
        self.assertEqual(len(cles), len(set(cles)))

    def test_blocs_et_engagements_connus(self):
        blocs = {b for b, _, _ in c.BLOCS}
        for p in c.POSTES:
            with self.subTest(poste=p.cle):
                self.assertIn(p.bloc, blocs)
                self.assertIn(p.engagement, c.ENGAGEMENTS)

    def test_les_blocs_partagent_les_postes(self):
        par_bloc = [p for b, _, _ in c.BLOCS for p in c.postes_du_bloc(b)]
        self.assertCountEqual([p.cle for p in par_bloc],
                              [p.cle for p in c.POSTES])

    def test_les_engagements_partagent_les_postes(self):
        par_engagement = [p for e in c.ENGAGEMENTS
                          for p in c.postes_de_l_engagement(e)]
        self.assertCountEqual([p.cle for p in par_engagement],
                              [p.cle for p in c.POSTES])

    def test_engagement_et_bloc_combines(self):
        for e, (b, _, _) in itertools.product(c.ENGAGEMENTS, c.BLOCS):
            for p in c.postes_de_l_engagement(e, b):
                self.assertEqual((p.engagement, p.bloc), (e, b))

    def test_une_formule_ne_cite_que_ce_que_le_calcul_lit(self):
        # Un lecteur qui refait le compte avec la formule doit retrouver les
        # hypothèses du calcul : une clé citée mais jamais lue serait un leurre.
        m = milieux()
        for p in c.POSTES:
            lues: set[str] = set()

            def v(cle: str) -> float:
                lues.add(cle)
                return m[cle]

            for a in c.ANNEES:
                p.calcul(v, a)
            with self.subTest(poste=p.cle):
                self.assertLessEqual(set(c.citees(p.formule)), lues)
        for s in c.SENSIBILITES:
            lues = set()

            def v(cle: str) -> float:
                lues.add(cle)
                return m[cle]

            s.calcul(v)
            with self.subTest(sensibilite=s.cle):
                self.assertLessEqual(set(c.citees(s.formule)), lues)


# ---------------------------------------------------------------------------
# Les scénarios et les totaux, sur les vraies hypothèses
# ---------------------------------------------------------------------------


class Scenarios(unittest.TestCase):

    def test_scenario_inconnu(self):
        with self.assertRaises(ValueError):
            c.scenario("median", 1)

    def test_scenario_mis_en_cache(self):
        self.assertIs(c.scenario("prudent", 3), c.scenario("prudent", 3))

    def test_valeurs_dans_les_bornes(self):
        for nom, annee in itertools.product(("prudent", "favorable"), c.ANNEES):
            s = c.scenario(nom, annee)
            self.assertEqual(set(s), set(c.HYPOTHESES))
            for cle, h in c.HYPOTHESES.items():
                with self.subTest(scenario=nom, annee=annee, hypothese=cle):
                    self.assertGreaterEqual(s[cle], h.bas)
                    self.assertLessEqual(s[cle], h.haut)
                    if h.bas == h.haut:
                        self.assertEqual(s[cle], h.bas)

    def test_aucune_hypothese_seule_ne_fait_mieux_ou_pire(self):
        # La promesse de ``scenario`` : un sommet où changer une seule
        # hypothèse ne dégrade plus (prudent) ni n'améliore plus (favorable).
        for nom, annee in itertools.product(("prudent", "favorable"), c.ANNEES):
            s = c.scenario(nom, annee)
            base = c._somme(c.POSTES, s, annee)
            signe = 1 if nom == "favorable" else -1
            for cle, h in c.HYPOTHESES.items():
                for borne in (h.bas, h.haut):
                    autre = c._somme(c.POSTES, {**s, cle: borne}, annee)
                    with self.subTest(scenario=nom, annee=annee,
                                      hypothese=cle, borne=borne):
                        self.assertLessEqual(signe * (autre - base), PRES)

    def test_prudent_milieu_favorable(self):
        for annee in c.ANNEES:
            prudent, favorable = c.solde(annee)
            with self.subTest(annee=annee):
                self.assertLessEqual(prudent, c.milieu(annee) + PRES)
                self.assertLessEqual(c.milieu(annee), favorable + PRES)

    def test_chaque_poste_entre_ses_extremes_n_est_pas_exige(self):
        # Les scénarios sont ceux du SOLDE : une ligne peut être plus haute
        # dans le prudent que dans le favorable. ``fourchette`` trie quand même.
        for annee in c.ANNEES:
            for p in c.POSTES:
                bas, haut = c.fourchette([p], annee)
                self.assertLessEqual(bas, haut)

    def test_le_solde_est_la_somme_des_lignes(self):
        for nom, annee in itertools.product(("prudent", "favorable"), c.ANNEES):
            lignes = sum(c.montant(p, annee, nom) for p in c.POSTES)
            blocs = sum(c.total(c.postes_du_bloc(b), annee, nom)
                        for b, _, _ in c.BLOCS)
            plus, moins = c.plus_et_moins(annee, nom)
            attendu = c.solde(annee)[0 if nom == "prudent" else 1]
            with self.subTest(scenario=nom, annee=annee):
                self.assertAlmostEqual(lignes, attendu, delta=PRES)
                self.assertAlmostEqual(blocs, attendu, delta=PRES)
                self.assertAlmostEqual(plus + moins, attendu, delta=PRES)
                self.assertGreaterEqual(plus, 0)
                self.assertLessEqual(moins, 0)

    def test_milieu_par_defaut_sur_tous_les_postes(self):
        for annee in c.ANNEES:
            self.assertAlmostEqual(c.milieu(annee), c.milieu(annee, c.POSTES))

    def test_poids_des_hypotheses(self):
        for annee in c.ANNEES:
            poids = c.poids_des_hypotheses(annee)
            ecarts = [e for _, e in poids]
            cles = {k for k, _ in poids}
            with self.subTest(annee=annee):
                self.assertEqual(ecarts, sorted(ecarts, reverse=True))
                self.assertTrue(all(e >= 0 for e in ecarts))
                self.assertEqual(cles, {k for k, h in c.HYPOTHESES.items()
                                        if h.bas != h.haut})


# ---------------------------------------------------------------------------
# Les sensibilités
# ---------------------------------------------------------------------------


class Sensibilites(unittest.TestCase):

    def test_bornes_encadrent_le_milieu(self):
        m = milieux()
        for s in c.SENSIBILITES:
            bas, haut = c.sensibilite(s)
            with self.subTest(sensibilite=s.cle):
                self.assertLessEqual(bas, haut)
                self.assertLessEqual(bas, s.calcul(m.__getitem__) + PRES)
                self.assertLessEqual(s.calcul(m.__getitem__), haut + PRES)

    def test_signes(self):
        signes = {s.cle: c.sensibilite(s) for s in c.SENSIBILITES}
        self.assertLess(signes["eloignements"][1], 0)
        self.assertLess(signes["demandes"][1], 0)
        self.assertGreater(signes["travailleurs"][0], 0)

    def test_regularisations_lineaires_en_volume(self):
        # La sensibilité suppose le chiffrage linéaire en volume : deux
        # tranches valent deux fois une, et zéro régularisation ne vaut rien.
        m = milieux()
        volumes = ("regularisations-debut", "regularisations-regime")

        def effet(n: float) -> float:
            v = lambda k: n if k in volumes else m[k]  # noqa: E731
            return sum(p.calcul(v, 5) for p in c.POSTES
                       if p.cle.startswith("regularises-"))

        une = c._par_regularisations(m.__getitem__)
        self.assertAlmostEqual(effet(10_000), une, delta=PRES)
        self.assertAlmostEqual(effet(20_000), 2 * une, delta=PRES)
        self.assertAlmostEqual(effet(0), 0.0, delta=PRES)


# ---------------------------------------------------------------------------
# ``verifier`` attrape-t-elle ce qu'elle dit attraper ?
# ---------------------------------------------------------------------------


class Verifier(unittest.TestCase):

    def setUp(self):
        # Les scénarios sont mis en cache : un essai ne doit pas déteindre.
        sauvegarde = dict(c._SCENARIOS)
        c._SCENARIOS.clear()
        self.addCleanup(lambda: (c._SCENARIOS.clear(),
                                 c._SCENARIOS.update(sauvegarde)))

    def remplacer(self, cle: str, **champs):
        h = c.HYPOTHESES[cle]
        nouvelle = c.Hypothese(**{**h.__dict__, **champs})
        return mock.patch.dict(c.HYPOTHESES, {cle: nouvelle})

    def une_cle(self) -> str:
        return next(iter(c.HYPOTHESES))

    def test_borne_basse_superieure(self):
        cle = self.une_cle()
        h = c.HYPOTHESES[cle]
        with self.remplacer(cle, bas=h.haut + 1), \
                self.assertRaisesRegex(ValueError, "borne basse"):
            c.verifier()

    def test_nature_inconnue(self):
        with self.remplacer(self.une_cle(), nature="intuition"), \
                self.assertRaisesRegex(ValueError, "nature"):
            c.verifier()

    def test_fiche_inconnue(self):
        with self.remplacer(self.une_cle(), chiffre="fiche-qui-n-existe-pas"), \
                self.assertRaisesRegex(KeyError, "fiche inconnue"):
            c.verifier()

    def test_hypothese_orpheline(self):
        orpheline = c.Hypothese("Personne ne me cite", 1, 2, "€", "hypothese",
                                "Pour l'essai.")
        with mock.patch.dict(c.HYPOTHESES, {"orpheline": orpheline}), \
                self.assertRaisesRegex(KeyError, "orpheline"):
            c.verifier()

    def test_formule_qui_cite_une_inconnue(self):
        modele = c.POSTES[0]
        faux = c.Poste(**{**modele.__dict__, "cle": "faux",
                          "formule": "{hypothese-inconnue} × 2"})
        with mock.patch.object(c, "POSTES", c.POSTES + [faux]), \
                self.assertRaisesRegex(KeyError, "hypothese-inconnue"):
            c.verifier()


if __name__ == "__main__":
    unittest.main()
