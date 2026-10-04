COUNT = 0

for i in range (1, 11):
    number = int(input (f"Введите {i} число:"))
    if number % 2 == 0:
        COUNT = COUNT + 1

if COUNT == 10:
    print ("YES")
else:
    print ("NO")

