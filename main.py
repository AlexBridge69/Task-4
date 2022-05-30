# Написать программу преобразования десятичного числа в двоичное
number_10_system = int(input('Задайте первую строку: '))
number_2_system = ''
while number_10_system > 0:
    number_2_system = str(number_10_system % 2) + number_2_system
    number_10_system //= 2
print(f'Введённое число в десятичной системе, в двоичной системе выглядит так: {number_2_system}')
