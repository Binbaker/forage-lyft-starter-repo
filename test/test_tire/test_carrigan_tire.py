import unittest
import sys
sys.path.append("/home/yossef/Desktop/forage_lyft_starter_repo/")

from tire.carrigan_tire import CarriganTire


class carriagnTireTest(unittest.TestCase):
    def tire_need_service(self):
        sensors = [0, 0.2, 0.7, 0.8]

        tire = CarriganTire(sensors)
        self.assertTrue(tire.need_service())


    def tire_NO_need_service(self):
        sensors = [0, 0.9, 1, 0.8]

        tire = CarriganTire(sensors)
        self.assertFalse(tire.need_service())
