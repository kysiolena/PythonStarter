a = 1
b = 21

sum_natural_numbers = 0
for i in range(a, b + 1):
    sum_natural_numbers += i

arithmetic_mean = round(sum_natural_numbers / b)

sum_natural_numbers_multiple_of_arithmetic_mean = 0
for i in range(a, b + 1):
    if not i % arithmetic_mean:
        sum_natural_numbers_multiple_of_arithmetic_mean += i

print(sum_natural_numbers_multiple_of_arithmetic_mean)
