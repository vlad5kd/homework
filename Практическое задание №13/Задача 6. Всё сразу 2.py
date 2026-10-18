numbers = [8, 9, 10, 11]
print(f"Исходный список: {numbers}")

numbers[1] = 17
print(f"После замены второго элемента на 17: {numbers}")

numbers.extend([4, 5, 6])
print(f"После добавления 4, 5 и 6 в конец: {numbers}")

removed_first = numbers.pop(0)
print(f"После удаления первого элемента ({removed_first}): {numbers}")

numbers.extend(numbers.copy())
print(f"После удвоения списка: {numbers}")

numbers.insert(3, 25)

print(f"Итоговый список после вставки 25 по индексу 3:\n{numbers}")