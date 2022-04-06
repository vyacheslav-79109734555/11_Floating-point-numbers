down = int(input('Введите нижнюю границу измерения: '))
up = int(input('Введите верхнюю границу измерения: '))
step = int(input('Введите шаг: '))
f = 32

print('C', '______', 'F')
for gradus in range(down, up, step):
    farengates = 1.8 * gradus + f
    if gradus == 0:
        farengates = 32
    print(f'{gradus} _____ {int(farengates)}', sep='\t')
print(f'{up} ____ {int(up * 1.8 + 32)}', sep='\t')
