from collections import OrderedDict, defaultdict, ChainMap

# OrderedDict
print('OrderedDict')

d = OrderedDict.fromkeys('abcde')
print(''.join(d))

d.move_to_end('b')
print(''.join(d))

d.move_to_end('b', last=False)
print(''.join(d))

# defaultdict
# Використовуючи list як default_factory, можна легко згрупувати послідовність пар ключ-значення в словник списків:
print()
print('defaultdict')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(s)

d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(sorted(d.items()))

# ChainMap
# ChainMap групує кілька dicts або інших відображень разом, щоб створити єдине оновлюване подання. Якщо maps не вказано, надається єдиний порожній словник, щоб новий ланцюжок завжди мав принаймні одне відображення.

print()
print('ChainMap')

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chained = ChainMap(adjustments, baseline)

print(chained.get('art'))  # van gogh
