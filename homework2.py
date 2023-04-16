from pprint import pprint

cook_book = {
'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},       
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],       
'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'}, 
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}],
'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
    {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = {'measure': new_shop_list_item['measure'], 'quantity': new_shop_list_item['quantity']}
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item
    return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
pprint(shop_list, sort_dicts=False, width=100)

