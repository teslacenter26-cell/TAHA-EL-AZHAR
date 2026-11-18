import unittest

from analyse import detecter


def evenement(i, heure, resultat="echec", compte="atlas", ip="192.0.2.10"):
    return (i, compte, ip, "2026-10-12T" + heure + "Z", resultat)


class DetectionTest(unittest.TestCase):
    def setUp(self):
        self.succes = evenement(10, "08:10:00", "succes")
        self.quatre = [evenement(i, f"08:0{i}:00") for i in range(1, 5)]

    def test_borne_incluse_et_entree_desordonnee(self):
        lignes = [self.succes, evenement(5, "08:00:00")] + self.quatre
        self.assertEqual(detecter(lignes), [(*self.succes[:4], 5)])

    def test_quatre_echecs(self):
        self.assertEqual(detecter(self.quatre + [self.succes]), [])

    def test_evenements_hors_groupe_ou_hors_fenetre(self):
        for extra in [evenement(5, "07:59:59"), evenement(5, "08:10:01"),
                      evenement(5, "08:10:00"), evenement(5, "08:05:00", compte="dune"),
                      evenement(5, "08:05:00", ip="192.0.2.20")]:
            with self.subTest(extra=extra):
                self.assertEqual(detecter(self.quatre + [extra, self.succes]), [])
