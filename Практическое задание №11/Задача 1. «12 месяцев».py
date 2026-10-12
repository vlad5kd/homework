YEAR = 365
MONTHS = 12

print ("Решения уравнения 28n + 30k + 31m = 365:")
for n in range(1, MONTHS + 1):
    for k in range(1, MONTHS + 1):
        for m in range(1, MONTHS + 1):
            if (28 * n) + (30 * k) + (31 * m) == YEAR:
                print(f"месяцев по 28 дней: {n}, месяцев по 30 дней: {k}, месяцев по 31 дню: {m}")