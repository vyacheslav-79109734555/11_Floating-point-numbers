bet = int(input('Введите ставку: '))
coefficient = float(input('Введите коэффициент: '))  # преобразовать строку в число
winning = bet * coefficient
print('Выигрыш составил: ', round(winning, 2))  # округляет вещественное число
