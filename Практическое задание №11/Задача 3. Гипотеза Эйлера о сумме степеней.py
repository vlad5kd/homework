# Максимальное значение по условию задачи
MAX = 150
max_power = MAX ** 5

found = False

for a in range(1, MAX + 1):
    a5 = a ** 5
    for b in range(a, MAX + 1):
        ab5 = a5 + b ** 5
        for c in range(b, MAX + 1):
            abc5 = ab5 + c ** 5
            for d in range(c, MAX + 1):
                total = abc5 + d ** 5

                if total > max_power :
                    break

                e = round(total ** 0.2)

                if e <= MAX and e ** 5 == total:
                    print(f"Найдены числа: a={a}, b={b}, c={c}, d={d}, e={e}")
                    print(f"Проверка: {a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")
                    print(f"Сумма a + b + c + d + e = {a + b + c + d + e}")
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break