from HW11_craft_interface import ICraft
from HW11_submarine_interface import Isubmarine


# Inheritance
# Abstraction
class Submarine(ICraft, Isubmarine):

    def __init__(self):
        self._motor_status = False  # Hiding
        self.latitude = 0
        self.longitude = 0
        self.depth = 0
        self._in_dock = True  # Hiding
        self._shooting = False  # Hiding
        self._periscope_status = False  # Hiding

    # Polymorphism
    def get_coordinates_and_move(self, latitude, longitude):
        if isinstance(latitude, int) and len(str(latitude)):
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

