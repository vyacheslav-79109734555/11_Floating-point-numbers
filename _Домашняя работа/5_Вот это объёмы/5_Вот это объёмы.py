radius = float(input('Введите радиус случайной планеты: '))
volume_planet = 4 / 3 * 3.14 * radius ** 3
volume_globe = 10.8321 * 10 ** 11
if volume_planet < volume_globe:
    result = round(volume_globe / volume_planet, 3)
    print('Объём планеты Земля больше в:', result, 'раз')
elif volume_planet > volume_globe:
    result = round(volume_planet / volume_globe, 3)
    print(f'Объём планеты Земля меньше в: (1/{round(volume_globe / volume_planet, 3)}) = {result} раз')
else:
    print('Объём планеты одинаковый')
