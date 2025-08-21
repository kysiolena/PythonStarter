from Lesson_8.calculator import is_numeric, check_body_mass_index

while True:
    print('Let\'s try to get your BMI...')
    print()

    parameters = {
        'weight': 0,
        'height': 0
    }

    for parameter in parameters.keys():
        while True:
            number = input(f'Enter your {parameter.capitalize()}: ')

            if number is not None and is_numeric(number):
                number = float(number)

                parameters[parameter] = number
                break
            else:
                print(f'{parameter.capitalize()} must be number')

    print()
    print(f'Result is {check_body_mass_index(height=parameters['height'], weight=parameters['weight']).upper()}')

    print()
    is_finish = input('If you want to finish, enter \'off\': ')

    if is_finish is not None and is_finish.lower() == 'off':
        break
    else:
        continue
