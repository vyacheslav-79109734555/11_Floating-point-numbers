while True:
    print('Введите местоположение коня: ')
    x_point = float(input('Введите точку Х: '))
    y_point = float(input('Введите точку У: '))
    x = int(x_point * 10)
    y = int(y_point * 10)
    if 0 > x or x > 7 or 0 > y or 0 > 7:
        print('Клетки с такой координатой не существует')
    else:
        print('Введите местоположение точки на доске: ')
    x_I_point = float(input('Введите точку Х_ход: '))
    y_I_point = float(input('Введите точку У_ход: '))
    x_I = int(x_I_point * 10)
    y_I = int(y_I_point * 10)
    print('Конь в клетке (', x, ',', y, ')', 'Точка в клетке (', x_I, ',', y_I, ')', )
    if abs((x - x_I) * (y - y_I)) == 2:
        print('Да, конь может ходить в эту точку')
    else:
        print('Нет, конь не может ходить в эту точку')
