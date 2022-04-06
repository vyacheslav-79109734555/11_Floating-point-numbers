import math

size_File = int(input('Укажите размер файла для скачивания: '))
speed_File = int(input('Какова скорость вашего соединения?: '))
counter_percent = 0
download = 0
for i in range(1, size_File):
    download += speed_File
    if download >= size_File:
        print('Прошло', i, 'сек. Скачано', size_File, 'из', size_File, 'Мб', '( 100 )%')
        break
    elif download < size_File:
        ratio = size_File / speed_File
        result_percent = 100 / ratio
        counter_percent += math.ceil(result_percent)
        print('Прошло', i, 'сек. Скачано', download, 'из', size_File, 'Мб (', counter_percent, ')%')
