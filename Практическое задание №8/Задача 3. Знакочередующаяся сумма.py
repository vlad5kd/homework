SUM = 0

n = int(input("Введите натуральное число: "))

for i in range (1, n + 1):
    if i % 2 != 0:
        SUM = SUM + i
    else:
        SUM = SUM - i

print (SUM)
