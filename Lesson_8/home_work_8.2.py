from Lesson_8.calculator import exponentiation, division

# Or use numpy.arange()
min_number = -5.0
max_number = 5.0
step = 0.5

current = min_number
while current <= max_number:
    num_1 = current
    num_2 = max_number - current * 2

    try:
        print('Exponentiation:', num_1, exponentiation(num_1, 2), sep=' | ')
        print('Division:', num_1, num_2, division(num_1, num_2), sep=' | ')
    except ZeroDivisionError as e:
        print('Division:', num_1, num_2, e, sep=' | ')
    except TypeError as e:
        print('TypeError: ', e)

    current += step
