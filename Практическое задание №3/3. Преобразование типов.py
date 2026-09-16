try:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print ("Сумма = " , result)
except ValueError:
    print ("Ошибка: вы ввели не число!")