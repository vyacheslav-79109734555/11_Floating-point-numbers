rows = int(input('Введите количество уровней пирамиды: '))  # количество строк в пирамиде
new_num = 1
for line in range(rows):
    space_count = rows - line - 1
    print('    ' * space_count, end='')
    for number in range(line + 1):
        print(new_num, end='     ')
        new_num += 2
    print()
