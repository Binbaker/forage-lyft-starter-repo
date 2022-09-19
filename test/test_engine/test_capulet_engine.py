import sys 
sys.path.append( "/home/yossef/Desktop/forage_lyft_starter_repo/")


import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_no_need_service(self):
        current_mileage = 0
        last_serivce_mileage = 0

        eng = CapuletEngine(current_mileage, last_serivce_mileage)
        self.assertFalse(eng.need_service())

    def test_need_service(self):
        current_mileage = 50000
        last_serivce_mileage = 10000

        eng = CapuletEngine(current_mileage, last_serivce_mileage)
        self.assertTrue(eng.need_service())