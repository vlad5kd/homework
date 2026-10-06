PIN = 4590

while True:
    tries = int(input ("Введите пин-код: "))
    if tries == PIN:
        print ("Доступ разрешен")
        break
    else:
        print ("Ошибка. Попробуйте еще раз")