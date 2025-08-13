# https://www.rapidtables.com/calc/math/Cos_Calculator.html
import math

print(
    '1 - додавання \n'
    '2 - віднімання \n'
    '3 - множення \n'
    '4 - ділення \n'
    '5 - зведення в ступінь \n'
    '6 - квадратний корінь \n'
    '7 - кубічний корінь \n'
    '8 - синус \n'
    '9 - косинус \n'
    '10 - тангенс \n'
)
operation_type = int(input('Enter operation type: '))

if operation_type > 10:
    print('Wrong number of operation type!')
    # Terminate program
    exit()

# 1 (required)
number_1 = int(input(f'Enter number{' 1' if operation_type <= 5 else ''}: '))

if operation_type <= 5:
    # 2 (optional)
    number_2 = int(input('Enter number 2: '))
elif operation_type >= 8:
    # Degrees to radians for trigonometric functions
    number_1 = math.radians(number_1)

match operation_type:
    # додавання
    case 1:
        print(number_1 + number_2)
    # віднімання
    case 2:
        print(number_1 - number_2)
    # множення
    case 3:
        print(number_1 * number_2)
    # ділення
    case 4:
        print(number_1 / number_2)
    # зведення в ступінь
    case 5:
        print(number_1 ** number_2)
    # квадратний корінь
    case 6:
        print(math.sqrt(number_1))
    # кубічний корінь
    case 7:
        print(number_1 ** (1 / 3))
    # синус
    case 8:
        print(math.sin(number_1))
    # косинус
    case 9:
        print(math.cos(number_1))
    # тангенс
    case 10:
        print(math.tan(number_1))
    case _:
        pass
