import math

from Lesson_8.calculator import is_numeric


def is_numeric(string: str) -> bool:
    """ Check numeric string """
    # Try to convert the string to a float
    # If the conversion is successful, return True
    try:
        float(string)
        return True
    # If a ValueError is thrown, it means the conversion was not successful
    # This happens when the string contains non-numeric characters
    except ValueError:
        return False


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
