vip_room = {'place1': 'David', 'place2': 'Ketrin', 'place3': 'Misha', 'place4': 'Mark'}
room = {'place5': 'Peter', 'place6': 'Maria', 'place7': None, 'place8': None}

all_guests = {**vip_room, **room}
for names in all_guests.values():
    if names == None:
        continue
    print(names)
