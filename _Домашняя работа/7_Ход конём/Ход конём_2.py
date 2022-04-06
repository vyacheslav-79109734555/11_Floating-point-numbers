print('Введите местоположение коня: ')
x_point = float(input('Введите точку Х: '))
y_point = float(input('Введите точку У: '))

print('Введите местоположение точки на доске: ')
x_I_point = float(input('Введите точку Х_ход: '))
y_I_point = float(input('Введите точку У_ход: '))

x = int(x_point * 10)
y = int(y_point * 10)
x_I = int(x_I_point * 10)
y_I = int(y_I_point * 10)

if 0 > x or x > 7 or 0 > y or 0 > 7:
    print('Клетки с такой координатой не существует')
print(f'Конь в клетке ({x}, {y}). Точка в клетке ({x_I}, {y_I}).')
if (7 >= x >= 0) and (7 >= y >= 0) and (7 >= x_I >= 0) and (7 >= y_I >= 0):
    x_fact = abs(x - x_I)
    y_fact = abs(y - y_I)
    if (x_fact == 2 and y_fact == 1) or (x_fact == 1 and y_fact == 2):
        print('Да, конь может ходить в эту точку')
    else:
        print('Конь не может ходить в этом направлении!')
else:
    print('Введите корректные данные!')

