import re


def remove_numbers(file):
    with open(file, "r") as file_in:
        contents = file_in.read()

    no_numbers = re.sub(r'\d+', '', contents)
    final_res = str(no_numbers)


    with open(file, 'w') as file_out:
        file_out.write(final_res)


if __name__ == '__main__':
    remove_numbers("some.txt")

