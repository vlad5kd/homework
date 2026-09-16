# 1.
my_list = [1, 2, 3]
print("Список:", my_list)
my_list[0] = 100
print("Измененный список:", my_list)
# Если в квадратных скобках выбрать позицию числа и потом присввоить новое значение, то оно изменится в списке

# 2.
my_tuple = (1, 2, 3)
print("Кортеж:", my_tuple)
my_tuple[0] = 100
print("Измененный кортеж:", my_tuple)
# Python выдал ошибку TypeError: 'tuple' object does not support item assignment. потому что кортеж - это не изменяемый список.

# 3.
my_string = "cat"
print("Строка:", my_string)
my_string[0] = "b"
# Python выдал ошибку TypeError: 'str' object does not support item assignment, так как строки так же являются неизменяемыми.
