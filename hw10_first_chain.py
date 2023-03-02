"""first class"""


class Animals:

    def __init__(self, kind: str = None, habitat: str = None):
        self.__kind = kind
        self.__habitat = habitat

    @property
    def kind(self):
        return self.__kind

    @property
    def habitat(self):
        return self.__habitat

    @kind.setter
    def kind(self, new_kind):
        self.__kind = new_kind

    @habitat.setter
    def habitat(self, new_habitat):
        self.__habitat = new_habitat

    @classmethod
    def create_new_animal(cls, kind, habitat):
        return cls(kind, habitat)

    def hunting_on(self, kind, victim):
        return f"{kind} hunting on {victim}"

    def like_to_eat(self, kind, food):
        return f"{kind} like to eat {food}"


if __name__ == '__main__':
    bear = Animals.create_new_animal('White bear', 'Alyaska')
    print(bear.hunting_on(bear.kind, "seal"))

"""second class"""


class Fishes(Animals):

    def __init__(self, kind: str = None, habitat: str = None, lengths: int = None):
        super().__init__(kind, habitat)
        self.__lengths = lengths

    @property
    def lengths(self):
        return self.__lengths

    @lengths.setter
    def lengths(self, new_lengths):
        self.__lengths = new_lengths

    def how_much_distance_can_overcome(self, kind, distance):
        return f"{kind} can overcome more that kilometres {distance} looking for eat"


if __name__ == '__main__':
    shark = Fishes()
    shark.kind = 'White shark'
    shark.habitat = 'all oceans around the world'
    shark.lengths = 5
    print(shark.hunting_on(shark.kind, 'any smallest fishes'))
    print(shark.how_much_distance_can_overcome(shark.kind, 3))

"""third class"""


class Whales(Fishes):

    def __init__(self, kind: str = None, habitat: str = None, lengths: int = None, weight: int = None):
        super().__init__(kind, habitat, lengths)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    def whales_can_do_for_peoles(self, kind):
        return f"{kind}-like other whales utilize carbon dioxide"


if __name__ == '__main__':
    whale = Whales()
    whale.kind = 'Big blue whale'
    whale.habitat = "North Ocean"
    whale.weight = 40
    whale.lengths = 5
    print(whale.whales_can_do_for_peoles(whale.kind))

"""fourth class"""


class KillerWhale(Whales):

    def __init__(self, kind: str = None, habitat: str = None, lengths: int = None, weight: int = None,
                 relationships_with_human: str = None):
        super().__init__(kind, habitat, lengths, weight)
        self.__relationships_with_human = relationships_with_human

    @property
    def relationships_with_human(self):
        return self.__relationships_with_human

    @relationships_with_human.setter
    def relationships_with_human(self, new_relationships_with_human):
        self.__relationships_with_human = new_relationships_with_human

    def describe_new_relationships_with_human(self):
        return f"{self.kind} {self.relationships_with_human} with human.But they are hunters - you should keep it in mind."


if __name__ == '__main__':
    killer_whale = KillerWhale()
    killer_whale.kind = 'Killer Whale'
    killer_whale.habitat = 'North ocean'
    killer_whale.weight = 25
    killer_whale.lengths = 5
    killer_whale.relationships_with_human = "friendly"
    print(killer_whale.describe_new_relationships_with_human())

"""fifth class"""


class ResidentKillerWhale(KillerWhale):

    def __init__(self, kind: str = None, habitat: str = None, lengths: int = None, weight: int = None,
                 relationships_with_human: str = None):
        super().__init__(kind, habitat, lengths, weight, relationships_with_human)

    def describe_the_residents(self):
        return 'Residents - it is the most common of the three populations in the coastal waters of the Pacific Northeast.'


if __name__ == '__main__':
    resident = ResidentKillerWhale()
    resident.kind = 'Resident Killer Whale'
    resident.habitat = 'Pacific Northeast'
    resident.lengths = 24
    resident.weight = 44
    print(resident.describe_the_residents())
    print(resident.hunting_on(resident.kind, "mostly fish and occasionally cephalopods"))
