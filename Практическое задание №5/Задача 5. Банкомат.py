B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

amount = int(input("Введите сумму для снятия: "))

count_5000 = amount // B5000
amount = amount % B5000
count_2000 = amount // B2000
amount = amount % B2000
count_1000 = amount // B1000
amount = amount % B1000
count_500 = amount // B500
amount = amount % B500
count_200 = amount // B200
amount = amount % B200
count_100 = amount // B100
amount = amount % B100

print("Отчет о выдаче купюр:")
print(f"Купюр по {B5000}: {count_5000} шт.")
print(f"Купюр по {B2000}: {count_2000} шт.")
print(f"Купюр по {B1000}: {count_1000} шт.")
print(f"Купюр по {B500}: {count_500} шт.")
print(f"Купюр по {B200}: {count_200} шт.")
print(f"Купюр по {B100}: {count_100} шт.")