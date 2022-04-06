import math

distance = float(input('Введите расстояние до цели: '))
angle = float(input('Введите угол: '))

angle /= 57.2758
x = math.cos(angle) * distance
y = math.sin(angle) * distance

print('Координаты вражеского танка:', x, ',', y)
print()
