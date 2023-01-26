friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print("Names".center(15, "*"))
for names in friends:
    print(f'{names.rjust(10)}')