from engine.engine import Engine 

class CapuletEngine(Engine):
    def __init__(self, current_mileage : int, last_serivce_mileage : int):
        self.current_mileage = current_mileage 
        self.last_serivce_mileage = last_serivce_mileage
    
    def need_service(self) -> bool:
        return (self.current_mileage - self.last_serivce_mileage) > 30_000 