raw_prices = input("Введите цены предметов через пробел: ").split()

prices = []
for item in raw_prices:
    prices.append(int(item))

asc_prices = prices.copy()
asc_prices.sort()

desc_prices = prices.copy()
desc_prices.sort(reverse=True)

reverse_order = prices[::-1]

print(f"Сортировка по возрастанию: {asc_prices}")
print(f"Сортировка по убыванию: {desc_prices}")
print(f"Оригинальный порядок (от старых к новым): {prices}")
print(f"Обратный порядок (от новых к старым): {reverse_order}")