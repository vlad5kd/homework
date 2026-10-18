import random

rows = 4
cols = 5
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 10))
    matrix.append(row)

print("Сгенерированный список:")
for row in matrix:
    print(row)

target = int(input("\nВведите значение для поиска: "))
is_found = False

print(f"Результаты поиска числа {target}:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Найдено на позиции: строка {i}, элемент {j} (индекс [{i}][{j}])")
            is_found = True

if not is_found:
    print(f"Элемент {target} в списке не найден.")