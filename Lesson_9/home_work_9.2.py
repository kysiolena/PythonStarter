text = input('Enter some text: ')

# text without spaces
text_without_spaces = ''.join(list(filter(None, text.split())))

# text without spaces reversed
reversed_text = text_without_spaces[::-1]

if text_without_spaces.lower() == reversed_text.lower():
    print(f'Фраза «{text}» є паліндромом')
else:
    print(f'Фраза «{text}» НЕ є паліндромом')
