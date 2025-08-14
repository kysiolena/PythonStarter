import time
from functools import reduce

min_number = 1
max_number = 100

start_time = time.time()

list_prime_numbers = []

# for number in range(min_number, max_number + 1):
#     division_count = 0
#     for div_number in range(1, number + 1):  # range(1, (number + 1) // 2 + 1)
#         if number % div_number == 0:
#             division_count += 1
#
#     if division_count == 2:
#         if number == 1:
#             continue
#
#         list_prime_numbers.append(number)

for num in range(min_number, max_number + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False

                break
                division_count += 1

        if is_prime:
            list_prime_numbers.append(num)

print(list_prime_numbers)
# print(time.time() - start_time)

operation_sum = input('Do you want to get the sum of these numbers? (Yes/No)')
if operation_sum.lower() == 'yes':
    print(sum(list_prime_numbers))

operation_product = input('Do you want to get the product of these numbers? (Yes/No)')
if operation_sum.lower() == 'yes':
    print(reduce(lambda a, b: a * b, list_prime_numbers))
