MAX = 0

while True:
    num = int(input("Введите натуральное число. Для выхода введите 0: "))
    if num > MAX:
        MAX = num

    if num == 0:
        break

if MAX == 0:
    print ("Вы не ввели никаких натуральных чисел.")
else:
    print (f"Самое большее число из введенных: {MAX}")