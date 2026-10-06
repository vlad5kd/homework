COIN_1 = 0
COIN_5 = 0
COIN_10 = 0
COIN_25 = 0

price = int(input ("Введите цену за услугу Ведьмка: "))

while price >= 25:
    COIN_25 = price // 25
    remainder =  price - (COIN_25 * 25)
    break

while price >= 10:
    COIN_10 = remainder // 10
    remainder = remainder - (COIN_10 * 10)
    break

while price >= 5:
    COIN_5 = remainder // 5
    remainder = remainder - (COIN_5 * 5)
    break

while price >= 1:
    COIN_1 = remainder // 1
    remainder = remainder - (COIN_1 * 1)
    break

all_coins = COIN_25 + COIN_10 + COIN_5 + COIN_1

print (f"Для оплаты Ведьмаку понадобится {all_coins} монет. Из них:")
print (f"{COIN_25} номиналом в 25")
print (f"{COIN_10} номиналом в 10")
print (f"{COIN_5} номиналом в 5")
print (f"{COIN_1} номиналом в 1")