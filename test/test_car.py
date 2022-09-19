import sys 
sys.path.append("..")

import unittest
from datetime import datetime
from engine.capuletEngine import CapuletEngine
from engine.sternmanEngine import SternmanEngine
from engine.willoughbyEngine import WilloughbyEngine
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_no_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 2)

        nub_battery = NubbinBattery(last_serivce_date, today)
        self.assertFalse(nub_battery.need_service())
    
    def test_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 5)

        nub_battery = NubbinBattery(last_serivce_date, today)
        self.assertTrue(nub_battery.need_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_no_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 2)

        spin_battery = NubbinBattery(last_serivce_date, today)
        self.assertFalse(spin_battery.need_service())
    
    def test_need_service(self):
        today = datetime.today().date()
        last_serivce_date = today.replace(year=today.year - 5)

        spin_battery = NubbinBattery(last_serivce_date, today)
        self.assertTrue(spin_battery.need_service())

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


class TestSternmanEngine(unittest.TestCase):
    def test_no_need_service(self):
        warning_light_is_on = False 

        eng = SternmanEngine(warning_light_is_on)
        self.assertFalse(eng.need_service())

    def test_need_service(self):
        warning_light_is_on = True

        eng = SternmanEngine(warning_light_is_on)
        self.assertTrue(eng.need_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_no_need_service(self):
        current_mileage = 0
        last_serivce_mileage = 0

        eng = CapuletEngine(current_mileage, last_serivce_mileage)
        self.assertFalse(eng.need_service())

    def test_need_service(self):
        current_mileage = 80000 
        last_serivce_mileage = 10000

        eng = CapuletEngine(current_mileage, last_serivce_mileage)
        self.assertTrue(eng.need_service())

if __name__ == "__main__":
    unittest.main()