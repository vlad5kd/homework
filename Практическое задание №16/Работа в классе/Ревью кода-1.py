n = int(input())  # добавил int()
product = 1  # поставил 1 вместо n % 10
while n > 0:  # поменял >= 10 на > 0, чтобы первая цифра тоже считалась
    digit = n % 10
    product = product * digit
    n //= 10
print(product)