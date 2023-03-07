class Wither:

    def __init__(self):
        self.name = 'Geralt'

    def __str__(self):
        for key, value in self.__dict__.items():
            return f"{self.__class__.__name__}:{{\n\t\t {key}:{value}\n}}"


if __name__ == '__main__':
    white_wolf = Wither()
    print(white_wolf)


