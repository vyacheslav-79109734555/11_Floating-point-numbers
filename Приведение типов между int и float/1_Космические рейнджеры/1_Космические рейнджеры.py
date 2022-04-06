income = int(input('Сколько чатлов? '))
cr = 2200
wallet = income / cr
print('Это', wallet, 'CR')
if income > cr * 0.5:
    print('Можно купить кораблей: ', int(wallet / 0.5))
