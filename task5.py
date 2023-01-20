vip_room = frozenset(('David', 'Mark', 'Bruce'))
room = frozenset((None, 'Michael', 'Kat', None))

all_guests = frozenset.union(vip_room, room)
for x in all_guests:
    if x == None:
        continue
    print(x)
