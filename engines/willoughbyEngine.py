from engine.engine import Engine 

class WilloughbyEngine(Engine):
    def __init__(self, last_service_milage : int, current_mileage : int):
        self.last_service_milage = last_service_milage
        self.current_mileage = current_mileage

    def need_service(self) -> bool:
        return (self.current_mileage - self.last_service_milage) > 60_000