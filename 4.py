user_text = input("Введите текст: ").split(' ')

for number in range(len(user_text)):
    print(f'{number+1}) {user_text[number][:10]}')
