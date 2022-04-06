cost_euro = float(input('Введите стоимость товара: '))
cost_usd = cost_euro * 1.25
cost_rub = round(cost_usd * 60.87, 2)
print('Стоимость Вашей покупки в рублях:', cost_rub)
