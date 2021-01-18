user_list = input('Введите данные через запятую: ').split(',')

print(*user_list)

for i in range(0, (len(user_list)//2*2), 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(*user_list)