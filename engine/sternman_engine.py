from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on : bool):
        self.warning_light_is_on = warning_light_is_on

    def need_service(self) -> bool:
        return self.warning_light_is_on
