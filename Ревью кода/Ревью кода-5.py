n = int(input())
max_digit = -1  # поставил -1 вместо n % 10 (т.к. 0 тоже кратен 3)
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # поменял знак < на >
            max_digit = digit  # поменял местами, присваиваем в max_digit
    n = n // 10  # деление // вместо %
if max_digit == -1:  # сравниваем с -1, а не с 0
    print('NO')
else:
    print(max_digit)