from typing import Callable


def find_the_even(some_data):
    for item in some_data:
        if item % 2 == 0:
            print(item)


def filter_func(some_func: Callable, data):
    return some_func(data)


random_numbers = [7, 5, 22, 9, 200, 16, 15, 8]

if __name__ == "__main__":

    filter_func(find_the_even, random_numbers)
