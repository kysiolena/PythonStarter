str_1 = 'Дано два рядки.'
str_2 = 'Виведіть на екран символи, які є в обох рядках.'

set_str_1 = set(str_1)
set_str_2 = set(str_2)

common_symbols = set_str_1 & set_str_2  # set_str_1.intersection(set_str_2)

print(common_symbols)
