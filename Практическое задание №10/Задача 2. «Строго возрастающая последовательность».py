try1 = int(input ("Введите первое число: "))


while True:
    try2 = int(input ("Введите второе число: "))
    if try1 >= try2:
        print ("Ошибка. Второе число должно быть больше первого!")
    else:
        break

while True:
        try3 = int(input ("Введите третье число: "))
        if try2 >= try3:
            print ("Ошибка. Третье число должно быть больше второго!")
        else:
            print ("Последовательность принята!")
            break
