import random

symbols = "000011лмз"
maze = "нф"

for i in range(23):
    maze = maze + random.choice(symbols)

temp_list = list(maze)
random.shuffle(temp_list)
maze = "".join(temp_list)

print(f"Сгенерированная строка: {maze}")
print()

print("--- Задание 1.1 ---")
print(maze[0:5])
print(maze[5:10])
print(maze[10:15])
print(maze[15:20])
print(maze[20:25])
print()

print("--- Задание 1.2 ---")
start_index = maze.find("н")
start_row = start_index // 5
start_col = start_index % 5
print(f"Координаты входа (н): строка {start_row}, столбец {start_col}")
print()

print("--- Задание 1.3 ---")
exit_index = maze.find("ф")
exit_row = exit_index // 5
exit_col = exit_index % 5
print(f"Координаты выхода (ф): строка {exit_row}, столбец {exit_col}")
print()

print("--- Задание 1.4 ---")
distance = abs(start_row - exit_row) + abs(start_col - exit_col)
print(f"Расстояние между входом и выходом: {distance} шагов")
print()

print("--- Задание 1.5 ---")
coins = maze.count("м")
coins_visual = "🟡" * coins
print(f"Собрано монет: 🟡x{coins} или {coins_visual}")
print()

print("--- Задание 1.6 ---")
hp = 100
traps = maze.count("л")
enemies = maze.count("з")

damage = traps * 10 + enemies * 50
hp_left = hp - damage

if hp_left < 0:
    hp_left = 0

full_hearts = hp_left // 10
empty_hearts = 10 - full_hearts
hearts_bar = "♥" * full_hearts + "♡" * empty_hearts

print(f"Ловушек: {traps}, врагов: {enemies}. Потеряно HP: {damage}")
print(f"Итог здоровья ({hp_left} HP): {hearts_bar}")
print()

print("--- Задание 1.7 ---")
emoji_maze = maze
emoji_maze = emoji_maze.replace("0", "⬜")
emoji_maze = emoji_maze.replace("1", "⬛")
emoji_maze = emoji_maze.replace("л", "🔷")
emoji_maze = emoji_maze.replace("м", "🟡")
emoji_maze = emoji_maze.replace("ф", "🟫")
emoji_maze = emoji_maze.replace("з", "🐷")
emoji_maze = emoji_maze.replace("н", "⭐")

print(emoji_maze[0:5])
print(emoji_maze[5:10])
print(emoji_maze[10:15])
print(emoji_maze[15:20])
print(emoji_maze[20:25])