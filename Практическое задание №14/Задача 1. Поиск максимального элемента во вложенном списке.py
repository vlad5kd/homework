import random

rows = 4
cols = 5
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(10, 99))
    matrix.append(row)

print("Сгенерированный список:")
for row in matrix:
    print(row)

max_value = matrix[0][0]
max_row = 0
max_col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

print(f"\nМаксимальный элемент: {max_value}")
print(f"Позиция: индекс строки = {max_row}, индекс элемента = {max_col}")