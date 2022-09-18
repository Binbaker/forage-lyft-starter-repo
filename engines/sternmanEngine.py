from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on : bool):
        self.warning_light_is_on = warning_light_is_on

    def need_serivce(self) -> bool:
        return warning_light_is_on
