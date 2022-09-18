from abc import ABC, abstractmethod

class Serviable(ABC):

    @abstractmethod
    def need_service(self):
        pass
   