if __name__ == "__main__":

    some = [5, 6, 1, 100, 5]


    def find_min(*args):
        data = list(*args)
        new_list = sorted(data)
        return new_list[0]


    def find_max(*args):
        data = list(*args)
        new_list2 = sorted(data, reverse=True)
        return new_list2[0]


    def find_min_and_max(*args):
        print("max value is -", find_max(*args), "\n min value is -", find_min(*args))

find_min_and_max(some)