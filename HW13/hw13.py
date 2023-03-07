class MyOwnIterator:

    def __init__(self, data, start_index, end_index):
        self.data = data
        self.start_index = start_index
        self.end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index < self.end_index:
            value = self.data[self.start_index]
            self.start_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator = MyOwnIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6)

    for items in iterator:
        print(items)