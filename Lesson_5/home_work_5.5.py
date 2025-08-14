MIN_NUMBERS_COUNT = 5

while True:
    numbers_str = input('Please enter at least 5 digits separated by commas: ')
    numbers_tuple = tuple(map(int, numbers_str.split(',')))

    if len(numbers_tuple) < MIN_NUMBERS_COUNT:
        print('Must be at least 5 digits.')
    else:
        print(tuple(sorted(numbers_tuple)))

        break
