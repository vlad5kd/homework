AMOUNT_3 = 0
AMOUNT_LAST = 0
AMOUNT_EVENS = 0
SUM_BIGGER_5 = 0
MULTIPLY_BIGGER_7 = 1
AMOUNT_0_AND_5 = 0

n =  int(input ("Введите натуральное число: "))

last_digit = n % 10

while n > 0:
    digit = n % 10

    if digit == 3:
        AMOUNT_3 += 1

    if digit == last_digit:
        AMOUNT_LAST += 1

    if digit % 2 == 0:
        AMOUNT_EVENS += 1

    if digit > 5:
        SUM_BIGGER_5 += digit

    if digit > 7:
        MULTIPLY_BIGGER_7 *= digit

    if digit == 0 or digit == 5:
        AMOUNT_0_AND_5 += 1

    n = n // 10

print (f"Количество цифр 3: {AMOUNT_3}")
print (f"Последняя цифра встречается {AMOUNT_LAST} раз")
print (f"Количество чётных цифр: {AMOUNT_EVENS}")
print (f"Сумма цифр, больших пяти: {SUM_BIGGER_5}")
print (f"Произведение цифр, больших семи: {MULTIPLY_BIGGER_7}")
print (f"Цифры 0 и 5 встречаются {AMOUNT_0_AND_5} раз")



