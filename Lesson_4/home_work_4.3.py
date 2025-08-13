rows = 7
columns = 0
for row in range(rows):
    columns += 1

    print('*' * columns, end='')

    print(' ' * (rows - columns + 1), end='')

    print()
