import random

rows = 4
cols = 5
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-20, 20))
    matrix.append(row)

filtered_matrix = []

for i in range(len(matrix)):
    positive_row = []
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0:
            positive_row.append(matrix[i][j])
    filtered_matrix.append(positive_row)

print(f"Исходный список:\n{matrix}")
print(f"\nОтфильтрованный список (только > 0):\n{filtered_matrix}")