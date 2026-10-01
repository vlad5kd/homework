COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90

print ("=== Мею кафе ===")
print ()
print ("1 - Кофе☕ (120 рублей)")
print ("2 - Чай 🍵 (80 рублей)")
print ("3 - Сок 🧃 (100 рублей)")
print ("4 - Вода 💧 (50 рублей)")
print ("5 - Лимонад 🥤 (90 рублей)")
print ()

drink = int(input ("Введите номер напитка из списка выше (1-5): "))
portion =  int(input ("Введите количество порций (1-10): "))

print ("Возможные скидки:")
print ("STUDENT - 20%")

discount = input ("Введите код скидки из списка выше (заглавными буквами): ")

match drink:
    case 1:
        drink = "Кофе ☕"
        price = COFFEE
    case 2:
        drink = "Чай 🍵"
        price = TEA
    case 3:
        drink = "Сок 🧃"
        price = JUICE
    case 4:
        drink = "Вода 💧"
        price = WATER
    case 5:
        drink = "Лимонад 🥤"
        price = LEMONADE

print ("=================================")
print ("||        КВИТАНЦИЯ КАФЕ       ||")
print ("=================================")
print ()

if portion % 10 == 1:
    word = "порция"
elif portion % 10 == 2 or portion % 10 == 3 or portion % 10 == 4:
    word = "порции"
else:
    word = "порций"

print (f"Товар: {drink}")
print (f"Цена за 1 порцию: {price} руб.")
print (f"Количество порций: {portion} {word}")
sum = price * portion
print (f"Сумма: {sum} руб.")

if discount == "STUDENT":
    discount = sum * 0.2
    print (f"Скидка STUDENT - 20%: -{int(discount)}")
else: discount = 0

print ("=================================")
print (f"💰 К ОПЛАТЕ: {int(sum - discount)} руб.")
print ("=================================")
