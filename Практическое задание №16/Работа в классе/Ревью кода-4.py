count = 0
p = 1  # для произведения нужна 1, иначе всегда будет 0
for i in range(1, 11):  # до 11, чтобы цикл прошел 10 раз
    x = int(input())
    if x >= 0:  # >= 0, так как ноль тоже неотрицательный
        p = p * x
        count = count + 1
if count > 0:
    print(count)  # выводим count вместо x
    print(p)
else:
    print('NO')