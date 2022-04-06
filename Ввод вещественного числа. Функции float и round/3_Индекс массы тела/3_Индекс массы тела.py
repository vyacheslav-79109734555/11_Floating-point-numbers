height = float(input('Ваш рост в (м): '))
weight = float(input('Ваш вес в (кг.): '))
bmi = round(weight / height ** 2, 2)  # индекс массы тела
print('Ваш индекс массы тела: ', bmi)
if bmi < 18.5:
    print('У Вас недостаточная масса тела ')
elif bmi < 25:
    print('У Вас нормальная масса тела ')
elif bmi < 30:
    print('У Вас избыточная масса тела ')
else:
    print('У Вас ожирение ')
