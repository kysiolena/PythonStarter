if __name__ == '__main__':
    guests = []

    while (True):
        print(
            '1 - Додати гостя \n'
            '2 - Видалити гостя \n'
            '3 - Переглянути список гостей \n'
            '4 - Перевірити наявність гостя \n'
            '5 - Переглянути кількість гостей \n'
            '6 - Вихід \n'
        )

        action = int(input('Виберiть дiю (1-6):'))

        match action:
            case 1:
                guest_name = input('Enter guest name:')

                if guest_name:
                    guests.append(guest_name)

            case 2:
                guest_index = int(input('Enter guest ID:'))

                if len(guests) == 0:
                    print('Guests list is empty!')
                elif guest_index < len(guests):
                    del guests[guest_index]
                else:
                    print('Guest ID is not correct!')

            case 3:
                if len(guests) == 0:
                    print('Guests list is empty now...')
                else:
                    for index, guest in enumerate(guests, start=1):
                        print(f'{index} - {guest}')

            case 4:
                guest_name = input('Enter guest name:')

                if guest_name.lower() in map((lambda guest_x: guest_x.lower()), guests):
                    print('Гостя запрошено')
                else:
                    print('Гостя не запрошено')

            case 5:
                print(f'Загальна кількість запрошених гостей {len(guests)}')

            case 6:
                print('Bye!')

                break
            case _:
                print('I dont\'t understand you...')

        print(' ' * 20)
        print('=' * 20)
        print(' ' * 20)
