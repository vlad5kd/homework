n = int(input ("Введите натуральное число: "))

current = 1

while current <= n:
    if (5 <= current <= 9) or (17 <= current <= 37) or (78 <= current <= 87):
        current = current + 1
        continue

    print (current)
    current = current + 1