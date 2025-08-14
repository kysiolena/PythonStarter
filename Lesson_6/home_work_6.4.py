while True:
    numbers_count = int(input('How many numbers do you want to create a list of?: '))
    numbers_str = input(f'Please enter {numbers_count} integers separated by commas: ')
    numbers_list = list(map(int, numbers_str.split(',')))

    if len(numbers_list) != numbers_count:
        print(f'The list must contain {numbers_count} integers.')
    else:
        print(numbers_list)
        print()

        while True:
            option = int(input(
                'Після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку,'
                'а після натискання клавіші 2 – за зростанням, 3 – вийти: '
            ))

            print()
            match option:
                case 1:
                    print(list(reversed(numbers_list)))
                case 2:
                    print(sorted(numbers_list))
                case 3:
                    break
                case _:
                    continue

        break
