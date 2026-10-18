n = int(input("Введите количество строк: "))
chars_list = []

for i in range(n):
    line = input("Введите строку: ")
    chars_list.extend(line)

print(f"Список всех символов: {chars_list}")