PRICE_FOR_KILOMETER = 49.5
KILOMETERS = 100

def calculate_taxi_cost (distance, consumption):
    """
    Расчет стоимости поездки на такси и необходимое количество бензина для поездки
    :param distance: расстояние, которое проехало такси
    :param consumption: количество литров бензина, которое машина потребляет на 100 км
    :return: итоговая стоимость поездки на такси
    """
    fuel_requirement = distance * (consumption / KILOMETERS)
    result = fuel_requirement * PRICE_FOR_KILOMETER
    return fuel_requirement, result

distance = float(input ("Введите расстояние, которое проехало такси (км): "))
consumption = float(input ("Введите количество литров бензина, которое машина потребляет на 100 км: "))

fuel_requirement, calculate_taxi_cost = calculate_taxi_cost(distance, consumption)

print (f"Для поездки на такси необходимо {fuel_requirement:.2f} литров бензина.")
print (f"Стоимость поездки составляет {calculate_taxi_cost:.2f} руб.")