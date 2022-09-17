import Car
import Engines.CapuletEngine
import Engines.SternmanEngine
import Engines.WilloughbyEngine
import Batteries.nubbin_battery
import Batteries.spindler_battery

class CarFactory:
    def create_calliope(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=spindler_battery(current_date, last_serivce_date))

    def create_glissade(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage: int) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=spindler_battery(current_date, last_serivce_date))

    def create_palindrome(self, current_date : date, last_serivce_date : date, warning_light_on : boo) -> Car:
        return Car(engine=SternmanEngine(warning_light_on), battery=spindler_battery(current_date, last_serivce_date))

    def create_rorscharch(self, current_date : date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int ) -> Car:
        return Car(engine=WilloughbyEngine(current_milleage, last_serivce_mileage), battery=nubbin_battery(current_date, last_serivce_date))

    def create_thovex(self, current_date, last_serivce_date : date, current_milleage : int, last_serivce_mileage : int) -> Car:
        return Car(engine=CapuletEngine(current_milleage, last_serivce_mileage), battery=nubbin_battery(current_date, last_serivce_date))
