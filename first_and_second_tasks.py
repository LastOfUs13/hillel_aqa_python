"""task1"""
import os
import random

# import shutil
#
# shutil.rmtree("test")

if __name__ == '__main__':
    os.makedirs("./test/data")
    os.chdir("./test/data")

some_list = []


def get_the_numbers():
    left_op = random.randint(1, 100)
    right_op = random.randint(1, 100)
    operator = random.randint(1, 3)

    return left_op, right_op, operator


for _ in range(100):
    some_list.append(get_the_numbers())

with open('my_file.txt', 'w') as file:
    for lines in some_list:
        file.write(str(lines)[1:-1])
        file.write("\n")

"""task2"""

with open('my_file.txt', 'r') as file:
    for elems in some_list:
        new_lsit = list(elems)
        if new_lsit[2] == 1:
            print(new_lsit[0] + new_lsit[1])
        if new_lsit[2] == 2:
            print(new_lsit[0] - new_lsit[1])
        if new_lsit[2] == 3:
            print(new_lsit[0] * new_lsit[1])



