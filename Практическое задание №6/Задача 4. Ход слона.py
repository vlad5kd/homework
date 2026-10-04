cell1x, cell1y = map(int, input("Введите номер столбца и номер строки для первой клетки:").split())
cell2x, cell2y = map(int, input("Введите номер столбца и номер строки для второй клетки:").split())

if (cell1x - cell1y == cell2x - cell2y) or (cell1x + cell1y == cell2x + cell2y):
    print("YES")
else:
    print("NO")