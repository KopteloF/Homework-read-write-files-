from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingred = int(file.readline().strip())
        ingred_list = []
        for _ in range(ingred):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingred_list.append({
                'ingredient_name':ingredient_name,
                'quantity':int(quantity),
                'measure':measure
            })
        file.readline()
        cook_book[dish] = ingred_list
    pprint(cook_book, sort_dicts=False, width=100)
