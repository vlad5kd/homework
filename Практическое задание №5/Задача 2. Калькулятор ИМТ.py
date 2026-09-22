weight, height = map(float, input("Введите свой вес и рост через пробел: ").split())

body_mass_index = weight / (height ** 2)

print (f"Индекс Массы Тела составляет: {body_mass_index:.1f}")