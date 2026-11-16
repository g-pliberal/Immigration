"""Les tests du calendrier des sources (``src/immigration/editions.py``).

Ils ne figent aucune date de publication — elles changent à chaque mise à
jour. Ils vérifient que chaque chiffre du registre a une édition déclarée, et
que ``verifier()`` signale, puis fait échouer, ce qu'elle dit signaler et
faire échouer, sur un calendrier inventé pour l'occasion.

Aucune dépendance : ``python -m unittest discover -s tests``.
"""

from __future__ import annotations

import datetime
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from immigration import editions as e  # noqa: E402
from immigration.chiffres import CHIFFRES  # noqa: E402
from immigration.echeances import DATE_ECRITE, PREAVIS  # noqa: E402

JOUR = datetime.date(2030, 3, 1)
EDITION = e.Edition("Rapport imaginaire 2030", "mars 2030", JOUR)


def verifier(aujourdhui: datetime.date, prochaines=None, cles=None):
    prochaines = prochaines or {"a": EDITION, "b": EDITION}
    return e.verifier(aujourdhui, prochaines, cles or set(prochaines))


class Registre(unittest.TestCase):
    def test_chaque_chiffre_a_son_edition(self):
        self.assertEqual(set(e.PROCHAINES), set(CHIFFRES))

    def test_une_edition_datee_dit_quand(self):
        for cle, edition in e.PROCHAINES.items():
            if edition.attendue is not None:
                self.assertTrue(edition.quand, cle)

    def test_quand_ne_porte_pas_de_date_a_declarer(self):
        # « 1er février 2027 » sur la page serait une date à venir que la
        # vérification des échéances refuserait.
        for cle, edition in e.PROCHAINES.items():
            self.assertIsNone(DATE_ECRITE.search(edition.quand), cle)


class Verifier(unittest.TestCase):
    def test_rien_loin_de_l_echeance(self):
        fautes, avert = verifier(JOUR - datetime.timedelta(days=PREAVIS + 1))
        self.assertEqual((fautes, avert), ([], []))

    def test_preavis(self):
        fautes, avert = verifier(JOUR - datetime.timedelta(days=PREAVIS))
        self.assertEqual(fautes, [])
        self.assertEqual(len(avert), 1)
        self.assertIn("a, b", avert[0])  # une édition, un seul signalement

    def test_parue_signalee_sans_echouer(self):
        for ecart in (0, e.DELAI - 1):
            fautes, avert = verifier(JOUR + datetime.timedelta(days=ecart))
            self.assertEqual(fautes, [], ecart)
            self.assertIn("devrait être parue", avert[0])

    def test_echoue_passe_le_delai(self):
        fautes, avert = verifier(JOUR + datetime.timedelta(days=e.DELAI))
        self.assertEqual(len(fautes), 1)
        self.assertEqual(avert, [])

    def test_ponctuel_jamais_signale(self):
        fautes, avert = verifier(
            datetime.date(2099, 1, 1), {"a": e.ponctuel("Aucune prévue")})
        self.assertEqual((fautes, avert), ([], []))

    def test_chiffre_sans_edition(self):
        fautes, _ = verifier(JOUR, {"a": EDITION}, {"a", "b"})
        self.assertEqual(len(fautes), 1)
        self.assertIn("« b »", fautes[0])

    def test_edition_sans_chiffre(self):
        fautes, _ = verifier(JOUR - datetime.timedelta(days=365),
                             {"a": EDITION, "z": EDITION}, {"a"})
        self.assertEqual(len(fautes), 1)
        self.assertIn("« z »", fautes[0])


if __name__ == "__main__":
    unittest.main()
