from math import pi, e

print_var = 5

count = int(input('Введите количество повторов: '))

print(print_var * count)
print(pi * print_var * count)
print(e * 2)

while print_var >= 0:
    print_var -= 1

str_var = 'my string'
sum_var = 0
for elem in str_var:
    sum_var += pow(str_var.find(elem), 2)
    print("sum=", sum_var)


def my_func(atr=1):
    print('atr', atr)


print(my_func(atr=5))
