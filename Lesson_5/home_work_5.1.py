while True:
    full_name = input('Enter your fullname: ')
    full_name_list = tuple(filter(None, full_name.split()))

    is_alpha_full_name = True
    is_title_full_name = True

    for word in full_name_list:
        if not word.isalpha():
            print(f'The word «{word}» must consist only of letters.')

            is_alpha_full_name = False

        if not word.istitle():
            print(f'The word «{word}» must begin with a capital letter.')

            is_title_full_name = False

    if is_title_full_name and is_title_full_name:
        print(f'Welcome, {' '.join(full_name_list)}!')
        break
