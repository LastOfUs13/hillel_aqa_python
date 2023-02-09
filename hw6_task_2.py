import math

if __name__ == "__main__":
    def find_square_data(side: int):
        perimetr = side * 4
        area = side * side
        diagonal = math.sqrt(2) * side

        return perimetr, area, diagonal


    result = find_square_data(side=5)
    print(result)

    """Another way to solve"""

    from typing import Callable


    def find_perimetr(size):
        perimetr = size * 4
        return perimetr


    def find_area(size):
        area = size * size
        return area


    def find_diagonal(size):
        diagonal = math.sqrt(2) * size
        return diagonal


    def find_perimetr_and_area(callback: Callable, size):
        return callback(size)


    list_of_data = [find_perimetr_and_area(find_perimetr, 5), find_perimetr_and_area(find_area, 5),
                    find_perimetr_and_area(find_diagonal, 5)]

    my_tuple = tuple(list_of_data)
    print(my_tuple)



