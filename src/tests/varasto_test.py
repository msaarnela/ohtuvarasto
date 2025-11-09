import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    # uudet testit
        self.varasto2 = Varasto(0)
        self.varasto3 = Varasto(10, -1)
        self.varasto4 = Varasto(10, 50)
        self.varasto5 = Varasto(20, 15)

    def test_tilavuus_nolla(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_alkusaldo_negatiivinen(self):
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_alkusaldo_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto4.saldo, 10)

    def test_lisattava_maara_pienempi_kuin_nolla(self):
        self.varasto4.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto4.saldo, 10)

    def test_lisattava_maara_mahtuu(self):
        self.varasto3.lisaa_varastoon(50)
        self.assertAlmostEqual(self.varasto3.saldo, 10)

    def test_ota_varastosta_negatiivinen_maara(self):
        self.assertAlmostEqual(self.varasto3.ota_varastosta(-5), 0)

    def test_ota_varastosta_enemman_kuin_mahdollista(self):
        self.assertAlmostEqual(self.varasto4.ota_varastosta(500), 10)
        self.assertAlmostEqual(self.varasto4.saldo, 0)

    def test_tulostus(self):
        self.assertEqual(str(self.varasto5), 'saldo = 15, vielä tilaa 5')

    # alkuperäiset testit

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
