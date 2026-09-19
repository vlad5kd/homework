import random
import math

x = random.randint(-10,10)
y = random.randint(-10,10)
d = math.sqrt(x**2) + (y*2)

print ("Точка на плоскости: ", x,y)
print ("Расстояние от начала координат:", d)