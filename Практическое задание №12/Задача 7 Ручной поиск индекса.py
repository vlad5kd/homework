numbers = [10, 20, 30, 40, 50]

user_number = int(input("Введите число: "))

is_found = False

for i in range(len(numbers)):
    if numbers[i] == user_number:
        print(f"Индекс числа {user_number} равен {i}")
        is_found = True
        break

if is_found == False:
    print(f"Число {user_number} отсутствует в списке. Нет такого числа")