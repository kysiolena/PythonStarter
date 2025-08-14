int_list = []
new_list = []
for number in range(1, 30):
    int_list.append(number)

    if number % 2:
        new_list.append(number)

print(f'{int_list=}')
print(f'{new_list=}')

repeat = int(input('How many times do you want to duplicate this list? '))

copied_new_list = []
for _ in range(repeat):
    copied_new_list.extend(new_list)

print(f'{copied_new_list=}')

int_list.clear()

print(f'After clear {int_list=}')
