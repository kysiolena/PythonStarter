MIN_NUMBERS_COUNT = 5

while True:
    numbers_str = input('Please enter at least 5 digits separated by commas: ')
    numbers_tuple = tuple(map(int, numbers_str.split(',')))

    if len(numbers_tuple) < MIN_NUMBERS_COUNT:
        print('Must be at least 5 digits.')
    else:
        sum_numbers = sum(numbers_tuple)
        second_number = numbers_tuple[1]
        penultimate_number = numbers_tuple[-2:-1][0]  # numbers_tuple[len(numbers_tuple) - 2]
        arithmetic_mean_numbers = sum_numbers / len(numbers_tuple)

        print(f'{second_number=}; {penultimate_number=}; {arithmetic_mean_numbers=}')
        print('Sum: ', second_number + penultimate_number + arithmetic_mean_numbers)
        break
