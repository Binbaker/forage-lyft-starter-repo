import sys 
sys.path.append( "/home/yossef/Desktop/forage_lyft_starter_repo/")

import unittest
from datetime import datetime 
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_no_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 2)

        battery = NubbinBattery(last_serivce_date, today)
        self.assertFalse(battery.need_service())
    
    def test_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_serivce_date, today)
        self.assertTrue(battery.need_service())


