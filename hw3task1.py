mlist = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for index in range(len(mlist)):
    if index % 2 == 0:
        even_tuple = ("index - " + str(index) + ", key- " + str(mlist[index]))
        even.append(even_tuple)

    else:
        odd_tuple = ("index - " + str(index) + ", key-" + str(mlist[index]))
        odd.append(odd_tuple)

print('list of even indexes - ' + str(even))
print('list of odd indexes - ' + str(odd))
