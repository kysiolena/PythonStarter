NUMBERS_COUNT = 3
COLORS = ('Red', 'Green', 'Blue')

user_color_tuple = tuple()
for color in COLORS:
    while True:
        number = int(input(f'Enter a value for the {color} color between 0 and 255: '))

        if 0 <= number <= 255:
            user_color_tuple += (number,)
            break
        else:
            print(f'The number {number} is not a valid RGB value. It must be between 0 and 255.')

print(f'rgb{user_color_tuple}')
