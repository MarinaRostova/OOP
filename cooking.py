cook_book = {}

with open('file.txt', 'rt', encoding="utf8") as file:
    for l in file:
       dish_name = l.strip()
       dish_dict = []
       ing_dict = {}
       count = file.readline()
       for i in range(int(count)):
          emp = file.readline()
          ingredient_name, quantity, measure  = emp.strip().split(' | ')
          dish_dict.append({'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})
          p = { dish_name: dish_dict }

       blank_line = file.readline()
       cook_book.update(p)
#print(f'cook_book = {cook_book}')



def get_shop_list_by_dishes(person_count: int, dishes: list):
    new_list = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in new_list:
                    new_list[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    new_list[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(new_list)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])






