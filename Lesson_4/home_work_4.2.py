number = int(input('Enter an integer number greater than 0: '))

factorial = 1
for n in range(1, number + 1):
    factorial *= n

print(f'{number}! = {factorial}')
