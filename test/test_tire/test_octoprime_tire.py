import unittest
import sys
sys.path.append("/home/yossef/Desktop/forage_lyft_starter_repo/")

from tire.octoprime_tire import OctoprimeTire

class OctoprimTest(unittest.TestCase):
    def Test_need_service(self):
        sensors = [0.5, 1, 0.5, 1]

        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.need_service())

    def Test_NO_need_service(self):
        sensors = [0, 1, 0, 1]

        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.need_service())
