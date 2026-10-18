numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(f"Длина списка: {len(numbers)}")

last_index = len(numbers) - 1
print(f"Последний элемент: {numbers[last_index]}")

print(f"Список в обратном порядке: {numbers[::-1]}")

if 5 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO")

numbers.pop(0)
numbers.pop()
print(f"Список после удаления крайних элементов: {numbers}")