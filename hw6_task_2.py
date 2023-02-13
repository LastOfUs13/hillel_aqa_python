import math


def find_square_data(side: int):
    perimetr = side * 4
    area = side * side
    diagonal = math.sqrt(2) * side

    return perimetr, area, diagonal

if __name__ == '__main__':

    result = find_square_data(side=5)
    print(result)


