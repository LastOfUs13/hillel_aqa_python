if __name__ == "__main__":

    def clean_all_the_lines(file):
        with open(file, 'w') as file:
            file.writelines("")


    clean_all_the_lines(file="")

