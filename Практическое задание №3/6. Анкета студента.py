# 1. Сбор данных от пользователя
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")

# 2. Преобразование типов
age = int(age_str)
subjects = subjects_str.split(",")

# 3. Создание словаря
student = {
    "name": name,
    "age": age,
    "subjects": subjects
}

# 4. Красивый вывод анкеты
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")

print("=" * 30)
