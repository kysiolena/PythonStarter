from Lesson_8.calculator import is_numeric, division, sum_numbers, subtract_numbers, multiply_numbers, exponentiation, \
    square_root, cube_root

CALCULATE_ACTIONS = {
    1: {
        'title': 'Додавання',
        'need_two_numbers': True,
        'callback': sum_numbers
    },
    2: {
        'title': 'Віднімання',
        'need_two_numbers': True,
        'callback': subtract_numbers
    },
    3: {
        'title': 'Множення',
        'need_two_numbers': True,
        'callback': multiply_numbers
    },
    4: {
        'title': 'Ділення',
        'need_two_numbers': True,
        'callback': division
    },
    5: {
        'title': 'Зведення в ступінь',
        'need_two_numbers': True,
        'callback': exponentiation
    },
    6: {
        'title': 'Зведення до квадратного кореня',
        'need_two_numbers': False,
        'callback': square_root
    },
    7: {
        'title': 'Зведення до кубічного кореня',
        'need_two_numbers': False,
        'callback': cube_root
    },
}
EXIT_ACTION = 'x'

# Calculate option
while True:
    print('Let\'s try to calculate something...')
    print()

    actions = ' \n'.join(map(lambda a: f'{a[0]} - {a[1]['title']}', CALCULATE_ACTIONS.items()))
    print(actions)
    print()

    action = input(
        f'Select type of calculate operations ({min(CALCULATE_ACTIONS.keys())}-{max(CALCULATE_ACTIONS.keys())}). '
        f'Or enter {EXIT_ACTION.upper()} for exit: '
    )
    print()

    if is_numeric(action):
        action = int(action)

        action_item = CALCULATE_ACTIONS.get(action)

        if action_item:
            # Default numbers
            number_1 = None
            number_2 = None

            try:
                # Number 1
                while True:
                    number_1 = input(f'Enter the {'first ' if action_item['need_two_numbers'] else ''}number: ')

                    # To float
                    if is_numeric(number_1):
                        number_1 = float(number_1)

                        break
                    else:
                        print('The first number must be an integer or floating point number.')

                if action_item['need_two_numbers']:
                    # Number 2
                    while True:
                        number_2 = input('Enter the second number: ')

                        # To int
                        if is_numeric(number_2):
                            number_2 = float(number_2)

                            break
                        else:
                            print('The second number must be an integer or floating point number.')

                result = None
                if number_2 is not None:
                    result = action_item['callback'](number_1, number_2)
                else:
                    result = action_item['callback'](number_1)

                print(f'Result of {action_item['title']} is {result}. \n')
            except ZeroDivisionError as e:
                print(e)
            except TypeError as e:
                print(e)
    elif action and action.lower() == EXIT_ACTION:
        print('Bye!')
        break
    else:
        print('You have entered an invalid action...')
