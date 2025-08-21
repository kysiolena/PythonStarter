def sum_numbers(start: int, end: int) -> int:
    if start == end:
        return end
    else:
        return start + sum_numbers(start + 1, end)


# result
print(sum_numbers(3, 8))

# test result
print(sum(range(3, 9)))
