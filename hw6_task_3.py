import random

if __name__ == "__main__":

    def is_prime():
        var = random.randint(2, 1000)
        if var == 2 or var == 3:
            return var, True
        if var % 2 == 0 or var % 3 == 0 or var % 4 == 0 or var % 5 == 0 or var % 6 == 0 or var % 7 == 0 or var % 8 == 0 or var % 9 == 0:
            return var, False
        for i in range(4, 1001):
            if var % i == 0:
                return var, False
            else:
                return var, True


    res, var = is_prime()
    print(res)
    print(var)


