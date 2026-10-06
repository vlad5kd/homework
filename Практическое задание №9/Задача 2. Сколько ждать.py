name = input ("Введите имена участников блиц-игры: ")

while name != "Александра":
    name = input ("Введите имена участников блиц-игры: ")

people_between = 0
name = input ("Введите имена участников блиц-игры: ")

while name != "Левон":
    people_between = people_between + 1
    name = input ("Введите имена участников блиц-игры: ")

    if name == "Левон":
        break

print (people_between)