num = int(input("Введите число от 0 до 36: "))

if num < 0 or num > 36:
    print("Ошибка ввода")

elif num == 0:
    print("Цвет кармана: зеленый")

elif (1 <= num <= 10 or 19 <= num <= 28):
    if num % 2 == 0:
        print("Цвет кармана: черный")
    else:
        print("Цвет кармана: красный")

else:
    if num % 2 == 0:
        print("Цвет кармана: красный")
    else:
        print("Цвет кармана: черный")