omnivores = {'John': 'vegetarian', 'Michael': 'omnivore', 'Inga': 'vegetarian', 'Oliver': 'omnivore'}
vegetarians = {'Sam': 'vegetarian', 'Kat': 'vegetarian'}

omnivores_and_vegetables = {**omnivores, **vegetarians}

for key, values in omnivores_and_vegetables.items():
    print(key + ' will add to list of guests ')
