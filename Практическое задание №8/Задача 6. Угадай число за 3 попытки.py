import random

number = random.randint(1, 10)


for i in range (1, 4):
    user_try = int(input (f"Попытка {i}. Введите число от 1 до 10: "))

    if user_try == number:
        print ("Угадали!")
        break
    elif user_try > number:
        print ("Неверно, загаданное число меньше.")
    elif user_try < number:
        print("Неверно, загаданное число больше.")

if user_try != number:
    print (f"Вы не отгадали с трех попыток. Загаданное число: {number}")

