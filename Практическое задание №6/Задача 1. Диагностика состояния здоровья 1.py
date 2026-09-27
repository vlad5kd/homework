temp = float(input ("Введите свою температуру: "))
pressure = int(input ("Введите свое давление; "))
pulse = int(input ("Введите свой пульс: "))

if (temp < 35 or temp > 38) or (pressure < 105 or pressure > 140) or (pulse < 55 or pulse > 110):
    print("Вам требуется врач")

elif 36 <= temp <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("У вас нормальное состояние")

else:
    print("У вас легкое недомогание")
