def check_month():
    global number_month
    try:
        number_month = int(input('Ввведите № месяца: '))
    except ValueError:
        print('Введите число')
        check_month()

    if number_month > 12 or number_month < 1:
        print('Номера месяца находятся в пределах от 1 до 12')
        return check_month()
    else:
        return number_month

year = {'summer': [6, 7, 8],
        'winter': [12, 1, 2],
        'spring': [3, 4, 5],
        'autumn': [9, 10, 11]
        }

month_user = check_month()

for season in year.keys():
    for month in year[season]:
        if month_user == month:
            print(f"{season} month")
            break
