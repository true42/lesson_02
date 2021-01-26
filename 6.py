def list_product(list):
    data_list = []
    for item in list:
        if item not in data_list:
            data_list.append(item)
    return data_list
name = []
price = []
count = []
unit = []
products = []
id = 1
analytics = {
    'name': None,
    'price': None,
    'count': None,
    'unit': None
    }
product = {
    'name': None,
    'price': None,
    'count': None,
    'unit': None
    }

while True:
    continue_chek = input("Продолжаем?: ").lower()
    if continue_chek == 'нет':
        break
    product['name'] = input("Введите название продукта: ")
    name.append(product['name'])
    product['price'] = input("Введите цену: ")
    price.append(product['price'])
    product['count'] = input('Введите количество: ')
    count.append(product['count'])
    product['unit'] = input('Введите единицу измерения: ')
    unit.append(product['unit'])
    products.append((id, product.copy()))
    id += 1

analytics['name'] = list_product(name)
analytics['price'] = list_product(price)
analytics['count'] = list_product(count)
analytics['unit'] = list_product(unit)

print(*products)
print(f"""{analytics['name']}
      {analytics['price']}
      {analytics['count']}
      {analytics['unit']}""")