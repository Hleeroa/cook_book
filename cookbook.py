with open('recipes.txt', encoding = 'utf-8') as f:
    cook = []
    for ingredients in str(f.read()).split('\n\n'):
        cook.append(ingredients)
    cook_book = {}
    for obecto in cook:
        key, ingredient = obecto.split('\n', 1)
        demivalues = []
        values = []
        for demivalue in ingredient.split('\n')[1:]:
            a = []
            for i in demivalue.split(' | '):
                a.append(i)
                if len(a) == 3:
                    value = {'ingredient_name': a[0], 'quantity': a[1], 'measure': a[2]}
                    values.append(value)
        cook_book[key] = values


def get_shop_list_by_dishes(dishes, person_count):
    company_cook = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for materials in cook_book.get(dish):
                for material in materials.keys():
                    if material == 'quantity':
                        materials['quantity'] = int(materials.get('quantity')) * person_count
                company_cook.setdefault(materials.get('ingredient_name'), {k: materials[k] for k in ('quantity',
                                                                                                     "measure")})
    return company_cook


print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 18))
