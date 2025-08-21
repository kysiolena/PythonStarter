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

    return number ** power


def division(number_1: int | float, number_2: int | float) -> int | float:
    """ Ділення """
    if not is_numeric(str(number_1)) or not is_numeric(str(number_2)):
        raise TypeError('Only numbers are allowed.')

    if number_2 != 0:
        return number_1 / number_2
    else:
        raise ZeroDivisionError('You try to divide a number with 0.')


def sum_numbers(number_1: int | float, number_2: int | float) -> int | float:
    """ Додавання """
    if not is_numeric(str(number_1)) or not is_numeric(str(number_2)):
        raise TypeError('Only numbers are allowed.')

    return number_1 + number_2


def subtract_numbers(number_1: int | float, number_2: int | float) -> int | float:
    """ Віднімання """
    if not is_numeric(str(number_1)) or not is_numeric(str(number_2)):
        raise TypeError('Only numbers are allowed.')

    return number_1 - number_2


def multiply_numbers(number_1: int | float, number_2: int | float) -> int | float:
    """ Множення """
    if not is_numeric(str(number_1)) or not is_numeric(str(number_2)):
        raise TypeError('Only numbers are allowed.')

    return number_1 * number_2


def square_root(number_1: int | float) -> int | float:
    """ Зведення до квадратного кореня """
    return exponentiation(number_1, 1 / 2)


def cube_root(number_1: int | float) -> int | float:
    """ Зведення до кубічного кореня """
    return exponentiation(number_1, 1 / 3)


def arithmetic_mean(*numbers: int | float) -> int | float:
    """ Середнє арифметичне """
    if not all(is_numeric(str(num)) for num in numbers):
        raise TypeError('Only numbers are allowed.')

    return sum(numbers) / len(numbers)


def check_body_mass_index(height: int | float, weight: int | float) -> str:
    """ Індекс маси тіла

        height: int | float - meters
        weight: int | float - kilograms

        BMI lower 18.5:

        Your BMI is considered insufficient. Keep in mind that an underweight BMI may pose certain health risks. Consult your doctor for more information on BMI calculations.

        BMI  within 18.5 – 24.9:

        Normally. Healthy weight helps reduce the risk of serious illness and means that you are close to your fitness goals.

        BMI above 30:

        It is considered overweight. Excessive weight may increase the risk of cardiovascular disease. Think about how to change your lifestyle to improve your health.
    """
    if not is_numeric(str(height)) or not is_numeric(str(weight)):
        raise TypeError('Weight and Height must be numbers.')

    bmi = weight / height ** 2

    if bmi < 18.5:
        return 'недостатня вага'
    elif 18.5 <= bmi <= 24.9:
        return 'маса тіла в нормі'
    else:
        return 'слідкуйте за фігурою'
