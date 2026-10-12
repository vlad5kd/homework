data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]

last_three = data[-3:]

reversed_data = data[::-1]

odd_index = data[1::2]

print(f"Первая тройка чисел: {first_three}")
print(f"Последняя тройка чисел: {last_three}")
print(f"Список в обратном порядке: {reversed_data}")
print(f"Элементы с нечётными индексами: {odd_index}")