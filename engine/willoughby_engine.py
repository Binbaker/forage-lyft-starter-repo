from engine.engine import Engine 

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage : int, last_service_milage : int):
        self.current_mileage = current_mileage
        self.last_service_milage = last_service_milage

    def need_service(self) -> bool:
        return (self.current_mileage - self.last_service_milage) > 60_000