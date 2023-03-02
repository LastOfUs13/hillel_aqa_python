from HW11_craft_interface import ICraft
from HW11_submarine_interface import Isubmarine


# Inheritance
# Abstraction
class Submarine(ICraft, Isubmarine):

    def __init__(self):
        # Hiding
        self.__motor_status = False
        self.__latitude = 0
        self.__longitude = 0
        self.__depth = 0
        self.__in_dock = True
        self.__shooting = False
        self.__periscope_status = False

    @property
    def motor_status(self):
        return self.__motor_status

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def depth(self):
        return self.__depth

    @property
    def in_dock(self):
        return self.__in_dock

    @property
    def shooting(self):
        return self.__shooting

    @property
    def periscope_status(self):
        return self.__periscope_status

    @motor_status.setter
    def motor_status(self, new_motor_status):
        self.__motor_status = new_motor_status

    @latitude.setter
    def latitude(self, new_latitude):
        self.__latitude = new_latitude

    @longitude.setter
    def longitude(self, new_longitude):
        self.__longitude = new_longitude

    @depth.setter
    def depth(self, new_depth):
        self.__depth = new_depth

    @in_dock.setter
    def in_dock(self, new_in_dock):
        self.__in_dock = new_in_dock

    @shooting.setter
    def shooting(self, new_shooting):
        self.__shooting = new_shooting

    @periscope_status.setter
    def periscope_status(self, new_periscope_status):
        self.__periscope_status = new_periscope_status

    # Polymorphism

    def get_coordinates_and_move(self, latitude, longitude):
        print(f'We are preparing to move next coordinates :{latitude},{longitude}')
        with open('coordinates', 'w') as file:
            file.write(f"{latitude},{longitude}")
        self._start_motor()

    # Encapsulation
    def _start_motor(self):
        self._motor_status = True
        print('Motor is on')
        self._dive()

    # Encapsulation
    def _dive(self):
        print('Diving...')
        self._depth = -5
        self._dock = False
        print('We are on the way')
        self._stop_motor()

    def _deep_dive(self):
        self.depth -= 10
        print('current depth is', self.depth)

    # Encapsulation
    def _stop_motor(self):
        print('We arrived')
        self._motor_status = False
        self._raising_the_periscope()
        with open('coordinates', "r+") as file:
            coordinates = file.read()
            upd = coordinates.split(",")
            self.latitude = upd[0]
            self.longitude = upd[1]

    # Encapsulation
    def _raising_the_periscope(self):
        print('Raising the periscope...')
        self._scan_an_area()

    # Encapsulation
    def _scan_an_area(self):
        print("Scanning...")
        from random import randint
        scanning = randint(0, 1)
        if scanning == 0:
            print('There is no enemies')
            self._lowering_the_periscope()
        else:
            enemies = input('There is enemies.Want to attack?y/n ')
            if enemies == "y":
                self._shooting = True
                self._rocket_launch()
            elif enemies == "n":
                self._lowering_the_periscope()
            else:
                print('Wrong command,need time to data processing,deep diving...')
                self._deep_dive()

    # Encapsulation
    def _rocket_launch(self):
        print('Enemy is terminated')
        self._lowering_the_periscope()

    # Encapsulation
    def _lowering_the_periscope(self):
        print('Lowering the periscope...')
        self._emergence()

    # Encapsulation
    def _emergence(self):
        self._depth = +5
        print("We are on the surface")
