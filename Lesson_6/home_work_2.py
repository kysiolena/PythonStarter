NUMBERS_COUNT = 3

print(f'Let\'s create two digital lists of {NUMBERS_COUNT} items each.')

lists = []
for list_index in range(2):
    lists.append([])
    for list_item_index in range(NUMBERS_COUNT):
        while True:
            item = input(f'Enter {list_item_index + 1} number for List {list_index + 1}: ')

            if item and isinstance(item, str):
                item = int(item)
            else:
                continue

            if isinstance(item, int) and isinstance(lists[list_index], list):
                lists[list_index].append(item)

                break
            else:
                continue

lists_unique = []
for list_x_index, list_x in enumerate(lists):
    lists_unique.append([])
    for list_item in list_x:
        # Unique items from List_x
        if isinstance(lists_unique[list_x_index], list) and list_item not in lists_unique[list_x_index]:
            lists_unique[list_x_index].append(list_item)

lists_unique_1: list = lists_unique[0] + list(filter(lambda x: x not in lists_unique[0], lists_unique[1]))
lists_unique_2: list = lists_unique[1] + list(filter(lambda x: x not in lists_unique[1], lists_unique[0]))

print(lists_unique_1, lists_unique_2, sep='\n')
print('*' * 10)

# lists_unique_1.reverse()
# lists_unique_2.reverse()
lists_unique_reversed_1 = lists_unique_1[::-1]
lists_unique_reversed_2 = lists_unique_2[::-1]

print(lists_unique_reversed_1, lists_unique_reversed_2, sep='\n')
print('*' * 10)

lists_unique_1.sort()
lists_unique_2.sort()

print(lists_unique_1, lists_unique_2, sep='\n')
print('*' * 10)

lists_unique_1.sort(reverse=True)
lists_unique_2.sort(reverse=True)

print(lists_unique_1, lists_unique_2, sep='\n')
print('*' * 10)
