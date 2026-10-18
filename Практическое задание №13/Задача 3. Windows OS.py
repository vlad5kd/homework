file_path = input("Введите путь к файлу в Windows: ")

parts = file_path.split("\\")

for folder in parts:
    print(folder)