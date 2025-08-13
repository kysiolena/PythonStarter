set_all = {'Guest_1', 'Guest_2', 'Guest_3', 'Guest_4', 'Guest_5', 'Guest_6', 'Guest_7', 'Guest_8'}
set_vip = {'Guest_1', 'Guest_4', 'Guest_7'}
set_left = {'Guest_3', 'Guest_7'}

no_vip = set_all.difference(set_vip)
left_vip = set_left.intersection(set_vip)
no_left_vip = set_vip.difference(left_vip)
no_left = set_all.difference(set_left)

print(no_vip)
print(left_vip)
print(no_left_vip)
print(no_left)
