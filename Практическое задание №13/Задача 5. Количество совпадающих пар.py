raw_input = input("Введите целые числа через пробел: ")

numbers = [int(item) for item in raw_input.split()]

pairs_count = 0
n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            pairs_count += 1

print(f"В списке {numbers} найдено совпадающих пар: {pairs_count}")