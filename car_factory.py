from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine 
from engine.willoughby_engine import WilloughbyEngine 
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory:

    @staticmethod
    def create_calliope(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int, senosrs : list) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date), tire=CarriganTire(sensors))

    @staticmethod
    def create_glissade(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage: int, senosrs : list) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Spindler_battery(current_date, last_serivce_date), tire=OctoprimeTire(sensors))

    @staticmethod
    def create_palindrome(current_date : date, last_serivce_date : date, warning_light_on : bool, senosrs : list) -> Car:
        return Car(engine=SternmanEngine(warning_light_on), battery=Spindler_battery(current_date, last_serivce_date), tire=OctoprimeTire(sensors))

    @staticmethod
    def create_rorscharch(current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int, senosrs : list) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date), tire=CarriganTire(senosrs))

    @staticmethod
    def create_thovex(current_date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int, senosrs : list) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=Nubbin_battery(current_date, last_serivce_date), tire=OctoprimeTire(senosrs))
