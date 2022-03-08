"""
 Написать функцию, которая определяет количество разрядов (единицы, дестки, сотни) введенного целого числа.
 Пример:
5 - одноразрядное число
15 - двухразрядное число
1400 - четырех разрядное числ
"""


def number_of_digits(number: int) -> int:
    i = 0
    while number > 0:
        number = number//10
        i += 1
    return i


numbers = input('Введите число: ')

if numbers.isdigit():
    print(f'Количество разрядов в числе {numbers} - {number_of_digits(int(numbers))}')
else:
    print(f'Вы ввели "{numbers}", а не число')

