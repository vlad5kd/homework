import math

x = float(input ("Введите число градусов x: "))

pi = math.pi
r = (x * pi)/180
result = math.sin (r) + math.cos (r) + (math.tan (r)**2)

print ("Результат: ", result)
