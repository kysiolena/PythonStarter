import math

from Lesson_8.calculator import is_numeric

"""
Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c.
Усередині цієї функції створити змінні x1, x2 зі значенням None
(спочатку приймаємо, що рівняння не має коренів) та функцію calc_rezult з
формальними параметрами зовнішньої функції quadratic_equation.
Всередині функції calc_rezult здійснити пошук дискримінанта,
згідно з результатом якого зробити розрахунок коренів рівняння.
Зовнішня функція quadratic_equation має повернути перелік значень коренів квадратного рівняння.
Надати можливість користувачеві ввести з клавіатури формальні параметри для передачі їх у
створену функцію quadratic_equation, результати роботи функції відобразити на екрані.
"""


# https://onlinemschool.com/math/assistance/equation/quadratic/

def quadratic_equation(a: int | float, b: int | float, c: int | float) -> tuple[int | float | None, int | float | None]:
    x1 = None
    x2 = None

    def calc_rezult(a: int | float, b: int | float, c: int | float):
        nonlocal x1, x2

        discriminant = b ** 2 - 4 * a * c

        if discriminant == 0:
            x1 = -b / 2 * a
        elif discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    calc_rezult(a, b, c)

    return x1, x2


# print(quadratic_equation(11, 2, -3))
# print(quadratic_equation(4, -20, 25))
# print(quadratic_equation(1, 2, 3))


while True:
    a = input('Enter number A: ')
    b = input('Enter number B: ')
    c = input('Enter number C: ')

    print()

    if is_numeric(a) and is_numeric(b) and is_numeric(c):
        print('Корені рівняння: ', quadratic_equation(float(a), float(b), float(c)))
    else:
        print('Введіть коректні значення чисел А, B, C')

    action = input('Завершити? (Так/Ні)')

    if action and action.lower() == 'так':
        break
