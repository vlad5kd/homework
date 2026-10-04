n = int(input("Введите количество чисел: "))

max1 = int(input("Введите 1 число: "))
max2 = 0

for i in range(2, n + 1):
    num = int(input(f"Введите {i} число: "))

    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(f"Наибольшее число последовательности: {max1}")
print(f"Второе наибольшее число последовательности: {max2}")