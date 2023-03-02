from abc import ABC, abstractmethod


# Abstraction

class ICraft(ABC):

    @abstractmethod
    def get_coordinates_and_move(self, latitude, longitude):
        pass

    @abstractmethod
    def _start_motor(self):
        pass

    @abstractmethod
    def _stop_motor(self):
        pass

