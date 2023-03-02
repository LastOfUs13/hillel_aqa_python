from abc import ABC, abstractmethod


# Abstraction
class Isubmarine(ABC):

    @abstractmethod
    def _dive(self):
        pass

    @abstractmethod
    def _raising_the_periscope(self):
        pass

    @abstractmethod
    def _scan_an_area(self):
        pass

    @abstractmethod
    def _rocket_launch(self):
        pass

    @abstractmethod
    def _lowering_the_periscope(self):
        pass

    @abstractmethod
    def _emergence(self):
        pass

