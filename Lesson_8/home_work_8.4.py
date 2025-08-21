from Lesson_8.calculator import is_numeric, arithmetic_mean

MAX_NUMBERS = 3

while True:
    print('Let\'s try to get arithmetic mean of some numbers...')
    print()

    numbers = []
    while len(numbers) < MAX_NUMBERS:
        number = input(f'Enter {len(numbers) + 1} number: ')

        if number is not None and is_numeric(number):
            number = float(number)

            numbers.append(number)
        else:
            print('You can enter only numbers')

    print()
    print(f'Result is {arithmetic_mean(*numbers)}')

    print()
    is_continue = input('Do you want to continue? (Yes/No): ')

    if is_continue is not None and is_continue.lower() == 'yes':
        continue
    else:
        break
