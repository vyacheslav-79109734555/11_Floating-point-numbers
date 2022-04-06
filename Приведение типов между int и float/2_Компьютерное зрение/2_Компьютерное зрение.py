while True:
    print('Введите местоположение фигуры')
    x_variable = float(input('По горизонтали: '))
    y_variable = float(input('По вертикали: '))
    x = int(x_variable * 10)
    y = int(y_variable * 10)
    if 0 > x or x > 7 or 0 > y or y > 7:
        print('Клетки с такой координатой не существует')
    else:
        print('Фигура находится в клетке (', x, ',', y, ')')
