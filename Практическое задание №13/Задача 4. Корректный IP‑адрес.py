ip_address = input("Введите IP-адрес для проверки: ")
numbers_str = ip_address.split(".")

is_correct = True

for item in numbers_str:
    num = int(item)
    if num < 0 or num > 255:
        is_correct = False

if is_correct == True:
    print("ДА")
else:
    print("НЕТ")
