omnivores = {'John': 'vegetarian', 'Michael': 'omnivore', 'Inga': 'vegetarian', 'Oliver': 'omnivore'}
vegetarians = {'Sam': 'vegetarian', 'Kat': 'vegetarian'}

omnivores_and_vegetables = {**omnivores, **vegetarians}

for key, values in omnivores_and_vegetables.items():
<<<<<<< HEAD
    if values == 'vegetarian':
        print(key + ' will add to list of guests ')
        
=======
    print(key + ' will add to list of guests ')
>>>>>>> c1f9d0d (fixes)
