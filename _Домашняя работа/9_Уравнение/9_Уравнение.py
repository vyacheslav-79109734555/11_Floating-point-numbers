import math

print('Решение уравнения ax^2+bx+c=0, \nпри этом a ≠ 0')
a = float(input('Введите значения a = '))
b = float(input('Введите значения b = '))
c = float(input('Введите значения c = '))
d = b ** 2 - 4 * a * c
if d > 0:
    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    if x_1 > x_2:
        print(f'Уравнение имеет два корня: наибольший - {round(x_1, 3)}, наименьший - {round(x_2, 3)}.')
        print('x_1 = (-b + math.sqrt(d)) / (2 * a) =', x_1)
        print('x_2 = (-b - math.sqrt(d)) / (2 * a) =', x_2)
    else:
        print(f'Уравнение имеет два корня: наибольший - {round(x_2, 3)}, наименьший - {round(x_1, 3)}.')
        print('x_2 = (-b - math.sqrt(d)) / (2 * a) =', x_2)
        print('x_1 = (-b + math.sqrt(d)) / (2 * a) =', x_1)
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print(f'Уравнение имеет один корень: {round(x, 3)}')
    print('x = (-b + math.sqrt(d)) / (2 * a) =', x)
else:
    print('корней нет')
