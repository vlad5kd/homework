INITIAL_BALANCE = 1000

while True:
    print("=====МЕНЮ БАНКОМАТА=====")
    print ("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")

    num = int(input ("Введите номер операции: "))

    if num == 1:
        print (f"Текущий баланс: {INITIAL_BALANCE}")

    elif num == 2:
        if INITIAL_BALANCE >= 100:
            INITIAL_BALANCE -= 100
            print ("Снято")
        else:
            print ("Недостаточно средств.")

    elif num == 3:
        INITIAL_BALANCE += 100
        print ("Баланс пополнен")

    elif num == 4:
        print ("До свидания!")
        break

    else:
        print ("Неверная команда")

