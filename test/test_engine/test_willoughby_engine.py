import sys 
sys.path.append( "/home/yossef/Desktop/forage_lyft_starter_repo/")

import unittest
from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_no_need_service(self):
        current_mileage = 0
        last_serivce_mileage = 0

        eng = WilloughbyEngine(current_mileage, last_serivce_mileage)
        self.assertFalse(eng.need_service())

    def test_need_service(self):
        current_mileage = 80000 
        last_serivce_mileage = 10000

        eng = WilloughbyEngine(current_mileage, last_serivce_mileage)
        self.assertTrue(eng.need_service())