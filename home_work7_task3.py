if __name__ == "__main__":

    from typing import Callable


    def map_func(some_func: Callable, data):
        return some_func(data)


    def find_the_perimetr_for_quadrate(size):
        return size * 4


    result = map_func(find_the_perimetr_for_quadrate, 5)
    print(result)
