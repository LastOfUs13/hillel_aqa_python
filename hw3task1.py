even_list = []
odd_list = []

some = [1, 2, 3, 4, 5, 6, 7, 8]
for index, numbers in enumerate(some):
    if index % 2 == 0:
        even_indexes = (index, numbers)
        even_list.append(even_indexes)

    else:
        odd_indexes = (index, numbers)
        odd_list.append(odd_indexes)

print('Here is even indexes - ' + str(even_list))
print('Here is odd indexes- ' + str(odd_list))