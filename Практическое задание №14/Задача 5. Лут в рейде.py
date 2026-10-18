n = int(input("Введите вместимость рюкзака (N): "))
raw_loot = input("Введите ценности предметов через пробел: ").split()

loot = []
for item in raw_loot:
    loot.append(int(item))

loot.sort(reverse=True)

max_value = 0
limit = min(n, len(loot))

for i in range(limit):
    if loot[i] > 0:
        max_value += loot[i]

print(f"Максимальная суммарная ценность лута: {max_value}")