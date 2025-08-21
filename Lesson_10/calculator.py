import math

from Lesson_8.calculator import is_numeric


def exponentiation(number: int | float, power: int | float) -> int | float:
    """ Зведення в ступінь """
    if not is_numeric(str(number)) or not is_numeric(str(power)):
        raise TypeError('Only numbers are allowed.')

    return math.pow(number, power)


def square_root(number_1: int | float) -> int | float:
    """ Зведення до квадратного кореня """
    return math.sqrt(number_1)


def cube_root(number_1: int | float) -> int | float:
    """ Зведення до кубічного кореня """
    return math.cbrt(number_1)
