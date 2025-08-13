# https://onlinemschool.com/math/assistance/equation/quadratic/

import math

a = int(input('Type number A:'))
b = int(input('Type number B:'))
c = int(input('Type number C:'))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print('Since the discriminant is less than zero, the quadratic equation has no real roots.')
elif discriminant == 0:
    x = -b / 2 * a

    print(f'The quadratic equation has one root: {x}')
else:
    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print(f'The quadratic equation has two roots {x_1} and {x_2}')
