import math

distance = float(input('Введите дистанцию до цели:'))
angle = float(input('Введите угол:'))
angle /= 57.2858  # перевод угла из радианов в градусы

x = math.cos(angle) * distance
y = math.sin(angle) * distance

print('Координаты вражеского танка:', x, ',', y)
