import random
import math

def is_prime():
    var = random.randint(2, 1000)
    for i in range(2, int(math.sqrt(var)) + 1):
        if var % i == 0:
            return var, False
    return var, True

res, var = is_prime()

if __name__ == '__main__':

    print(res)
    print(var)

