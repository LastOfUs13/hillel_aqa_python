class MyOwnIterator:

    def __init__(self, data, start_index, end_index):
        self.__data = data
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index and self.__start_index < len(self.__data):
            value = self.__data[self.__start_index]
            self.__start_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = MyOwnIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], -1, 2)

    for items in iterator:
        print(items)

