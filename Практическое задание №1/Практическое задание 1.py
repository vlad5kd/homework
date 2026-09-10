import time


def calculate_discount(price, discount_percent):
    final_price = price - (price * (discount_percent / 100))
    return final_price


def main():
    print("=== Старт программы ===")
    item_name = input("Что покупаем? ")
    cost = float(input("Сколько стоит? "))

    print("Считаем скидку...")
    time.sleep(1)

    result = calculate_discount(cost, 10)
    print(f"Товар: {item_name}")
    print(f"Цена со скидкой 10%: {result} руб.")
    print("=== Конец ===")


if __name__ == "__main__":
    main()