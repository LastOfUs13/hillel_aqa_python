class Wagon:

    def __init__(self, number):
        self.__number = number
        self.__passengers = {}
        self.__available_places = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __len__(self):
        return len(self.__passengers)

    def __setitem__(self, place, passenger):
        if len(self.__passengers) < 10 and place in self.__available_places:
            self.__passengers[place] = passenger
            self.__available_places.remove(place)
        else:
            raise TypeError("select another place or wagon")

    def __getitem__(self, item):
        return self.__passengers[item]

    def __str__(self):
        return f"{self.__dict__}"


class Train:

    def __init__(self):
        self.__wagons = []

    def __add__(self, new_wagon):
        return self.__wagons.append(new_wagon)

    def __len__(self):
        return len(self.__wagons)


if __name__ == '__main__':
    wagon = Wagon(1)
    wagon.__setitem__(3, 'Misha')
    wagon.__setitem__(1, 'David')
    print(wagon)
    print(len(wagon))
    wagon.__setitem__(5, 'Marichka')
    print(wagon)
    train = Train()
    train.__add__(wagon)
    print(len(train))

