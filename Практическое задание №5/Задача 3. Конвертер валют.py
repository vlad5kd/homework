USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует доллары в рубли по курсу
    :param amount_usd: количество долларов
    :return: вычисление кол-ва рублей по курсу
    """
    result = amount_usd * USD_TO_RUB
    return result

amount_usd = float(input("Введите сумму в долларах: "))
amount_rub = convert_usd_to_rub(amount_usd)

print(f"{amount_usd:.2f} $ по текущему курсу составляет {amount_rub:.2f} руб.")
