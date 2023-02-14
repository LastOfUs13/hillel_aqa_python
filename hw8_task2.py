def even_squared_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number ** 2


if __name__ == '__main__':

    for square in even_squared_numbers(0, 1000000000):
        print(square)

