TOTAL = 0

while True:
    price = int(input ("Введите стоимость товара: "))

    if price < 0:
        print ("Ошибка цены")
        continue
    elif price == 0:
        break
    else:
        TOTAL += price

if TOTAL > 1000:
    discount = TOTAL * 0.1
    TOTAL = TOTAL - discount

print (f"Итоговая сумма к оплате: {TOTAL}")

