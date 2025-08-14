new_list = []
for number in range(1, 30):
    if number % 2:
        new_list.append(number)

number = int(input('Enter number: '))

if number in new_list:
    repeat_count = new_list.count(number)
    index = new_list.index(number)

    print(f'Kількість повторів {repeat_count} та його позицію у цьому списку {index}')
else:
    print('Entered number is out of range.')
