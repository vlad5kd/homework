TAX_RATE = 0.13

annual_income = float(input ("Введите свой годовой доход: "))

tax = annual_income * TAX_RATE
income_after_tax = annual_income - tax

print (f"Общая сумма дохода: {annual_income:.2f} руб.")
print (f"Сумма рассчитанного налога: {tax:.2f} руб.")
print (f"Сумма «на руки» после вычета налога: {income_after_tax:.2f} руб.")