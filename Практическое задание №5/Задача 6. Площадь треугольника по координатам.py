import math

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между точками
    :param x1: координата x первой точки
    :param y1: координата y первой точки
    :param x2: координата x второй точки
    :param y2: координата y второй точки
    :return:расстояние между точками
    """
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return result

def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона
    :param a: сторона А треугольника
    :param b: сторона B треугольника
    :param c: сторона C треугольника
    :return: формула Герона для вычисления площади
    """
    p = (a + b + c) / 2
    result = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return result

ax, ay = map(float, input("Введите координаты точки A через пробел: ").split())
bx, by = map(float, input("Введите координаты точки B через пробел: ").split())
cx, cy = map(float, input("Введите координаты точки C через пробел: ").split())

side_ab = calculate_distance (ax, ay, bx, by)
side_bc = calculate_distance(bx, by, cx, cy)
side_ca = calculate_distance(cx, cy, ax, ay)

triangle_area = calculate_triangle_area(side_ab, side_bc, side_ca)

print(f"Площадь треугольника: {triangle_area:.2f}")