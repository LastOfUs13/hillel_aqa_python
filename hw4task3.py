long_string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
for smtng in long_string:
    if "=" in long_string:
        new_string = long_string.replace("=", " ")
    if "&" in long_string:
        new_string_2 = new_string.replace("&", " ")
    if "s" in new_string_2:
        new_string_3 = new_string_2.replace("s", "", 5)
    if " " in new_string_3:
        new_list = new_string_3.split()

my_dict = {new_list[i]: new_list[i + 1] for i in range(0, len(new_list), 2)}
print(my_dict)