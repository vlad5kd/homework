import math

def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника
    :param width: ширина прямоугольника
    :param height: высота прямоугольника
    :return: площадь прямоугольника
    """
    result = width * height
    return result

def  calculate_circle_area(radius):
    """
    Вычисляет площадь круга
    :param radius: радиус круга
    :return: площадь круга
    """
    result = math.pi * (radius ** 2)
    return result

width, height = map(float, input ("Введите стороны прямоугольника через пробел: ").split())
radius = float(input("Введите радиус круга: "))

print (f"Площадь прямоугольника: {calculate_rectangle_area(width, height):.2f}")
print (f"Площадь круга: {calculate_circle_area(radius):.2f}")