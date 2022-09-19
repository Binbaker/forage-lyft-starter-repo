from datetime import date
from car import Car
from engine.capuletEngine import CapuletEngine
from engine.sternmanEngine import SternmanEngine 
from engine.willoughbyEngine import WilloughbyEngine 
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery

class CarFactory:

    @staticmethod
    def create_calliope(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_glissade(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage: int) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_palindrome(current_date : date, last_serivce_date : date, warning_light_on : bool) -> Car:
        return Car(engine=SternmanEngine(warning_light_on), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_rorscharch(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int ) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date))

    @staticmethod
    def create_thovex(current_date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date))
