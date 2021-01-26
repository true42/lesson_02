list = [1, 2.56, 'text', None, [1, 2.56, 'text', None]]

print(f'Есть список "list" — {list}')

for i in range(len(list)):
    print(f'Тип {i+1}-го элемента в списке "list" — {str(type(list[i]))[7:-1]}')
