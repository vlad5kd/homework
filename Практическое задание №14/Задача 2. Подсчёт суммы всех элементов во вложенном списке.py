import random

rows = 4
cols = 4
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 50))
    matrix.append(row)

print("Исходный вложенный список:")
for row in matrix:
    print(row)

print()
total_sum = 0
max_row_sum = 0
max_row_index = 0

for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]

    print(f"Сумма элементов строки {i}: {row_sum}")
    total_sum += row_sum

    if i == 0 or row_sum > max_row_sum:
        max_row_sum = row_sum
        max_row_index = i

print(f"\nОбщая сумма всех элементов: {total_sum}")
print(f"Строка с максимальной суммой: индекс {max_row_index} (сумма = {max_row_sum})")