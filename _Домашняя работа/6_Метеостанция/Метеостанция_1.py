down = int(input('Введите нижнюю границу измерения: '))
up = int(input('Введите верхнюю границу измерения: '))
step = int(input('Введите шаг: '))
f = 32

upper_F = int(32 + up * 1.8)  # 122
print('C', '______', 'F')
for gradus in range(down, up + step, step):
    if gradus < up:
        print(gradus, '_____', f + int(gradus * 1.8))
    else:
        print(up, '_____', upper_F)
