prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
total_sum = sum(prices)

average_price = total_sum / len(prices)

print(f"Самый дорогой товар: {max_price} руб.")
print(f"Самый дешевый товар: {min_price} руб.")
print(f"Общая стоимость всех товаров: {total_sum} руб.")
print(f"Средняя цена товара: {average_price:.2f} руб.")