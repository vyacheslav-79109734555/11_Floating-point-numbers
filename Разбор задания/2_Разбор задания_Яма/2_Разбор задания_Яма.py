numb = int(input('Введите число N: '))  # 5
for line in range(numb):
    for left_numb in range(numb, numb - line - 1, -1):
        print(left_numb, end='')
    point_count = 2 * (numb - line - 1)
    print('.' * point_count, end='')
    for rignt_numb in range(numb - line, numb + 1):
        print(rignt_numb, end='')
    print()
