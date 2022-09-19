import sys 
sys.path.append( "/home/yossef/Desktop/forage_lyft_starter_repo/")

import unittest
from datetime import datetime
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_no_need_service(self):
        warning_light_is_on = False 

        eng = SternmanEngine(warning_light_is_on)
        self.assertFalse(eng.need_service())

    def test_need_service(self):
        warning_light_is_on = True

        eng = SternmanEngine(warning_light_is_on)
        self.assertTrue(eng.need_service())

