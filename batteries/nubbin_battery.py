from batteries.battery import Battery 

class Nubbin_battery(Battery):
    def __init__(self, last_service_date : date, current_date : date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def need_service(self) -> bool:
        return self.last_service_date.replace(year=self.last_service_date+4) < self.current_date