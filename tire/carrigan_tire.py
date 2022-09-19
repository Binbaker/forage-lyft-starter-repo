from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def need_service(self):
        for n in self.sensors:
            if (n >= 0.9):
                return True
        return False

