cell1x, cell1y = map(int, input("Введите номер столбца и номер строки для первой клетки:").split())
cell2x, cell2y = map(int, input("Введите номер столбца и номер строки для второй клетки:").split())

if (cell1x + cell1y) % 2 == 0:
    color1 = 1 # Белый
else:
    color1 = 2 # Чёрный

if (cell2x + cell2y) % 2 == 0:
     color2 = 1  # Белый
else:
     color2 = 2  # Чёрный

if color1 == color2:
    print ("YES")
else:
    print ("NO")