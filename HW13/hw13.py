class MyOwnIterator:

    def __init__(self, data, start_index, end_index):
        self.__data = data
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index and self.__start_index < len(self.__data) and len(
                str(self.__start_index)) <= 1 and len(str(self.__end_index)) <= 1:
            value = self.__data[self.__start_index]
            self.__start_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = MyOwnIterator([51, 23, 66, 15, 6, 18, 23, 10, 99], 5, 7)

    for items in iterator:
        print(items)
