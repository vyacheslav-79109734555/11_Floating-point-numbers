cost_euro = float(input('Введите стоимость товара: '))
cost_usd = 1.25
cost_rub = 60.87
print(f'Стоимость Вашей покупки в рублях: {round(cost_usd * cost_rub * cost_euro, 2)}')
