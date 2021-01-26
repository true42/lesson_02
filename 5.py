my_list = [7, 5, 3, 3, 2]
user_number = int(input("Введите число: "))

for number in range(len(my_list)):
    if user_number > my_list[number]:
        my_list.insert(number, user_number)
        break
    elif my_list[number] == my_list[-1]:
        my_list.append(user_number)

print(*my_list)