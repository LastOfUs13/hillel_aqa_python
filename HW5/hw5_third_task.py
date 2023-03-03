"""task3"""
import re

with open("text.txt", 'r') as file:
    file_data = file.read()

res = re.findall(r"[A-z]", file_data)

cast_in_string = str(res)
final_sring = cast_in_string.lower().replace("[", "").replace(",", "").replace(" ", "").replace("'", "").replace("]",
                                                                                                                 "")

new_dict = {}
for letters in final_sring:
    key = letters
    value = final_sring.count(letters)
    new_dict.update({key: value})

print(new_dict)




