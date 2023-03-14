class TxtWriter:

    def __init__(self, file_path):
        self.__file_path = file_path

    def write_file(self, user_data):
        with open(self.__file_path, 'w') as file:
            file.write(user_data)

