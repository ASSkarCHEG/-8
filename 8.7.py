s = input('Введите число: ')
n = s.isdigit()
while n == False:
    s = input('Ошибка. Попробуйте ещё раз. Введите число ещё раз: ')
    n = s.isdigit()
print(f'Введено целое число: {s}')