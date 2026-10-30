import random

print("--- Этап 1: База растений ---")

names_pool = ["Роза", "Тюльпан", "Пион", "Лилия"]
colors_pool = ["красный", "желтый", "белый", "розовый"]
sizes_pool = ["малый", "средний", "крупный"]
speeds_pool = ["медленный", "средний", "быстрый"]

farm_data = ""
for i in range(4):
    name = names_pool[i]
    color = random.choice(colors_pool)
    size = random.choice(sizes_pool)
    speed = random.choice(speeds_pool)

    plant_info = f"{name} {color} {size} {speed}"
    farm_data = farm_data + plant_info
    if i < 3:
        farm_data = farm_data + ", "

print(f"Сгенерированная строка: {farm_data}\n")

plants_list = farm_data.split(", ")

print("Растения на ферме:")
for plant in plants_list:
    print(plant)
print()

print("--- Этап 2: Скрещивание ---")

hybrids_db = "Роза+Тюльпан=Розотюльпан;Пион+Лилия=Пиолилия;Роза+Пион=Розопион;"
print(f"База гибридов: {hybrids_db}")

chosen_plants = random.sample(plants_list, 2)
parent1_full = chosen_plants[0]
parent2_full = chosen_plants[1]

p1_parts = parent1_full.split(" ")
p2_parts = parent2_full.split(" ")

name1 = p1_parts[0]
name2 = p2_parts[0]
print(f"Выбраны для скрещивания: {name1} и {name2}")

combo1 = f"{name1}+{name2}="
combo2 = f"{name2}+{name1}="

recipes = hybrids_db.split(";")
hybrid_name = ""

for recipe in recipes:
    if recipe.startswith(combo1) or recipe.startswith(combo2):
        eq_index = recipe.find("=")
        hybrid_name = recipe[eq_index + 1:]

if hybrid_name != "":
    print(f"Получен гибрид: {hybrid_name}")
else:
    print("Эти растения нельзя скрестить")
print()

print("--- Этап 3: Характеристики гибрида ---")
print(f"Родитель 1: {parent1_full}")
print(f"Родитель 2: {parent2_full}\n")

color1 = p1_parts[1]
color2 = p2_parts[1]

if name1 <= name2:
    hybrid_color = color1
else:
    hybrid_color = color2

print(f"Цвет гибрида: {hybrid_color}")

size1 = p1_parts[2]
size2 = p2_parts[2]

if size1 == size2:
    hybrid_size = size1
elif "малый" in (size1, size2) and "средний" in (size1, size2):
    hybrid_size = "малый/средний"
elif "малый" in (size1, size2) and "крупный" in (size1, size2):
    hybrid_size = "малый/крупный"
else:
    hybrid_size = "средний/крупный"

print(f"Размер гибрида: {hybrid_size}")

speed1 = p1_parts[3]
speed2 = p2_parts[3]

if speed1 == "медленный" or speed2 == "медленный":
    hybrid_speed = "медленный"
elif speed1 == "средний" or speed2 == "средний":
    hybrid_speed = "средний"
else:
    hybrid_speed = "быстрый"

print(f"Скорость роста гибрида: {hybrid_speed}")