m = int(input ("Введите стартовое количество организмов: "))
p = float(input ("Введите среднесуточное увеличение в процентах: "))
n = int(input ("количество дней для размножения: "))

current = m # Текущая популяция

for i in range (1, n + 1):
    print (f"День {i}, размер популяции: {current:.2f}")
    current = current + (current * (p / 100))
