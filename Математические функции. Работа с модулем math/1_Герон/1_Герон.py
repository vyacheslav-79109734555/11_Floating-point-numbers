import math

a = float(input('Введите координату "a": '))
b = float(input('Введите координату "b": '))
c = float(input('Введите координату "c": '))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Площадь треугольника равна:', s)
