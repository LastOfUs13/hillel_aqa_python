long_string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
filtered = long_string.replace("=", " ").replace("&", " ").replace("s", "", 5).split()
my_dict = {filtered[i]: filtered[i + 1] for i in range(0, len(filtered), 2)}
print(my_dict)

