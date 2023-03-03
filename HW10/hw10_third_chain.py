"""first class"""


class Reptilia:

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

    @staticmethod
    def define_two_famous_species():
        return 'Two most famous species of reptiles - crocodiles and turtles '

    def answer_about_your_favour_reptilies(self):
        return f"I like {self.kind}.Mostly you can find this one at {self.habitat}"

    def hunting_on(self, kind, victim):
        return f"{kind} hunting on {victim}"


if __name__ == '__main__':
    queen_cobra = Reptilia()
    queen_cobra.kind = "Queen cobra"
    queen_cobra.habitat = "Jungles"
    print(queen_cobra.answer_about_your_favour_reptilies())
    print(queen_cobra.hunting_on(queen_cobra.kind, "small rodents"))

"""second class"""


class Crocodile(Reptilia):

    def __init__(self, kind: str = None, habitat: str = None, favourite_food: str = None):
        super().__init__(kind, habitat)
        self.__favourite_food = favourite_food

    @property
    def favourite_food(self):
        return self.__favourite_food

    @favourite_food.setter
    def favourite_food(self, new_favourite_food):
        self.__favourite_food = new_favourite_food

    @staticmethod
    def describe_the_most_dangerous_enemies():
        return 'Jaguars are most dangerous crocodiles enemies'

    def tell_about_generation(self, species, size_of_generation):
        return f"{species}  can lay up to {size_of_generation} at a time "


if __name__ == '__main__':
    crocodile = Crocodile()
    crocodile.kind = 'Aligator'
    crocodile.habitat = 'Amazon river'
    crocodile.favourite_food = 'meat'
    print(crocodile.tell_about_generation(crocodile.kind, "10 eggs"))
    print(crocodile.hunting_on(crocodile.kind, "zebras"))

"""third class"""


class Crocodile(Reptilia):
    def __init__(self, kind: str = None, habitat: str = None, favourite_food: str = None):
        super().__init__(kind, habitat)
        self.__favourite_food = favourite_food

    @property
    def favourite_food(self):
        return self.__favourite_food

    @favourite_food.setter
    def favourite_food(self, new_favourite_food):
        self.__favourite_food = new_favourite_food

    @staticmethod
    def describe_the_most_dangerous_enemies():
        return 'Jaguars are most dangerous crocodiles enemies'

    def tell_about_generation(self, species, size_of_generation):
        return f"{species} can lay up to {size_of_generation} at a time "


class Turtle(Crocodile):
    def __init__(self, kind: str = None, habitat: str = None, favourite_food: str = None, life_size: int = None):
        super().__init__(kind, habitat, favourite_food)
        self.__life_size = life_size

    @property
    def life_size(self):
        return self.__life_size

    @life_size.setter
    def life_size(self, new_life_size):
        condition = new_life_size >= 50 and new_life_size <= 200
        if isinstance(new_life_size, int) and condition:
            self.__life_size = new_life_size
        else:
            raise TypeError('Check your data please')

    def find_out_how_long_turtles_can_live(self):
        return f"{self.__life_size} years-not so bad, isn't it?"


if __name__ == '__main__':
    leo = Turtle()
    leo.kind = 'Turtle'
    leo.habitat = 'some island'
    leo.life_size = 75
    print(leo.find_out_how_long_turtles_can_live())
    print(leo.tell_about_generation(leo.kind, 50))

"""fourth class"""


class Comodo(Reptilia):

    def __init__(self, kind: str = None, habitat: str = None, favourite_food: str = None):
        super().__init__(kind, habitat)
        self.__favorite_food = favourite_food

    @property
    def favorite_food(self):
        return self.__favorite_food

    @favorite_food.setter
    def favorite_food(self, new___favorite_food):
        self.__favorite_food = new___favorite_food

    def find_out_is_comodo_omnivorous(self, scepies, favorite_food):
        return f"{scepies} prefer {favorite_food}"


if __name__ == '__main__':
    comodo = Comodo('Komodo dragon', 'dragon island', 'different kind of meat')
    print(comodo.find_out_is_comodo_omnivorous(comodo.kind, comodo.favorite_food))
    print(comodo.hunting_on(comodo.kind, "turtles,dogs, cats, goats, buffaloes"))

"""fifth class"""


class Chameleon(Reptilia):

    def __init__(self, kind: str = None, habitat: str = None, funny_facts: str = None):
        super().__init__(kind, habitat)
        self.__fanny_facts = funny_facts

    @property
    def fanny_facts(self):
        return self.__fanny_facts

    @fanny_facts.setter
    def fanny_facts(self, new_fanny_facts):
        self.__fanny_facts = new_fanny_facts

    def find_out_chameleon_secret(self):
        return f"{self.kind} can {self.fanny_facts}"


if __name__ == '__main__':
    chameleon = Chameleon('Chameleon', 'some woods', 'change skin colour')
    print(chameleon.find_out_chameleon_secret())
