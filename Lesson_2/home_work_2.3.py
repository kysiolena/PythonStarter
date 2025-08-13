# https://onlinemschool.com/math/assistance/equation/quadratic/

a = int(input('Type number A:'))
b = int(input('Type number B:'))
c = int(input('Type number C:'))

discriminant = b ** 2 - 4 * a * c
discriminant_sqrt = discriminant ** 0.5

x_1 = (-b + discriminant_sqrt) / (2 * a)
x_2 = (-b - discriminant_sqrt) / (2 * a)

print(x_1, x_2)
