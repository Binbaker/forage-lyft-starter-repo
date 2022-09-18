from car import Car
from engines.capuletEngine import CapuletEngine
from engines.sternmanEngine import SternmanEngine 
from engines.willoughbyEngine import WilloughbyEngine 
from batteries.nubbin_battery import Subbin_battery
from batteries.spindler_battery import Spindler_battery

class CarFactory:
    @staticmethod
    def create_calliope(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_glissade(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage: int) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_palindrome(self, current_date : date, last_serivce_date : date, warning_light_on : boo) -> Car:
        return Car(engine=SternmanEngine(warning_light_on), battery=Spindler_battery(current_date, last_serivce_date))

    @staticmethod
    def create_rorscharch(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int ) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date))

    @staticmethod
    def create_thovex(self, current_date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date))
