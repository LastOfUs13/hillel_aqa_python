from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyReaderAndWriter:

    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_file(self, user_data):
        if user_data == self.__result:
            self.__is_actual = False
        else:
            self.__writer.write_file(user_data)
            return self.__result


if __name__ == '__main__':
    txt_reader = TxtReader('some.txt')
    txt_writer = TxtWriter('some.txt')
    proxy_func = TxtProxyReaderAndWriter(txt_reader, txt_writer)
    # print(proxy_func.read_file())
    proxy_func.write_file("hello,it's me")
