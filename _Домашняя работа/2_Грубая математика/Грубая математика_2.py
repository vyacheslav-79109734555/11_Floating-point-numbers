import math

segNum = int(input('Введите количество чисел: '))

for n in range(segNum):
    number = float(input(f'Введите {n + 1}- е число " x ": '))
    if number > 0:
        print(f'x = {math.ceil(number)}, log(x) = {math.log(math.ceil(number))}')
    else:
        print(f'x = {math.floor(number)}, exp(x) = {math.exp(math.floor(number))}')
