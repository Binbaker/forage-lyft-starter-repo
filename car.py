from servicable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def need_serivce(self) -> bool:
        return self._engine.need_serivce() or self._battery.need_serivce() 
        
