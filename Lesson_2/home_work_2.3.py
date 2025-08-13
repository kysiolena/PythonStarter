# https://onlinemschool.com/math/assistance/equation/quadratic/

a = int(input('Type number A:'))
b = int(input('Type number B:'))
c = int(input('Type number C:'))

discriminant = b ** 2 - 4 * a * c
discriminant_sqr = discriminant ** 0.5

x_1 = (-b + discriminant_sqr) / (2 * a)
x_2 = (-b - discriminant_sqr) / (2 * a)

print(x_1, x_2)
