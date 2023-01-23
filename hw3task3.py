friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for dude in friends:
    if dude not in enemies:
        print(f"{dude} ,we are the best friends")
    if dude in enemies:
        print(f"{dude} ,we are not friends any more")
    if dude == 'James':
        continue
