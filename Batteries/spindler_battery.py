import battery

class spindler_class(battery):
    def __init__(self, last_service_date : date, current_date : date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def need_service(self) -> bool:
        return self.last_service_date.replace(year=last_service_date.year+2) < self.current_date

