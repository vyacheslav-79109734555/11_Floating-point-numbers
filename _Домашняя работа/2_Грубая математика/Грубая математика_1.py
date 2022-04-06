import math

while True:
    segNum = input('Введите количество чисел: ')
    if segNum.isdigit():
        print('ok', end='\n')
        break
    print('Ошибка ввода! попробуйте еще раз: ')
for num in range(int(segNum)):
    print('Введите', num + 1, '- е число " x ": ', end='')
    x = float(input())
    if x > 0:
        x = math.ceil(x)
        print('x =', x, ' log(x) =', math.log(x))
    else:
        x = math.floor(x)
        print('x =', x, ' exp(x) =', math.exp(x))
print()
