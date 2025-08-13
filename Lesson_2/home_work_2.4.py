symbols = input('Type 10 symbols:')

sum_of_symbol_codes = 0
for symbol in symbols:
    print(symbol, ord(symbol))
    sum_of_symbol_codes += ord(symbol)

print(f'{sum_of_symbol_codes=}')
