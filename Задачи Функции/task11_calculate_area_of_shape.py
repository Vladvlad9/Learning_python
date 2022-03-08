"""
В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
Для вычисления площади каждой фигуры должна быть написана отдельная функция.
"""


def circle(numbers: int, select: int):

    if select == 1:
        s = 3.14 * numbers ** 2
        return print(f'Площадь круга через радиус равен - {s}')
    elif select == 2:
        s = numbers**2/4*3.14
        return print(f'Площадь круга через диаметр равен - {s}')
    elif select == 3:
        s = numbers**2/(4*3.14)
        return print(f'Площадь круга через длину окружности равен - {s}')

def rectangle():
    pass

def triangle():
    pass


print('Выберите что вычеслить:\n'
      '1.Площадь круга\n'
      '2.Площадь прямоугольника\n'
      '3.Площадь треугольника')

user_select = int(input('Введите значение '))
if user_select == 1:
    print('Вы выбрали вычесление круга\n'
          'Площадь круга через:\n'
          '1.Радиус\n'
          '2.Диаметр\n'
          '3.Длину окружности\n'
          )
    select_calculate = int(input('Выберите вариант вычесления '))
    select_number = int(input('Введите значение для вычесления '))
    print(circle(select_number, select_calculate))

