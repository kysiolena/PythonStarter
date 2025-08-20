list_1 = [45, 11, 8, 9, 6, 78, 2, 3, 18]
list_2 = [5, 1, 81, 9, 6, 73, 2, 31, 8]

set_list_1 = set(list_1)
set_list_2 = set(list_2)

diff_1 = set_list_1 - set_list_2  # set_list_1.difference(set_list_2)
diff_2 = set_list_2 - set_list_1  # set_list_2.difference(set_list_1)

print(diff_1)
print(diff_2)
