from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tire) -> None:
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def need_serivce(self) -> bool:
        return self.engine.need_serivce() or self.battery.need_serivce() or self.tire.need_service() 
        
