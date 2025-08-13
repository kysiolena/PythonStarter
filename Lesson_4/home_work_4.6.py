USER_LOGIN = 'Olena'
USER_PASSWORD = '1111'
ATTEMPTS_COUNT_MAX = 3

attempt = 1
while attempt <= ATTEMPTS_COUNT_MAX:
    login = input('Enter your login: ')
    password = input('Enter your password: ')

    if login == USER_LOGIN and password == USER_PASSWORD:
        print(f'Авторизацію успішно пройдено з {attempt} спроби')
        break
    elif attempt == ATTEMPTS_COUNT_MAX:
        print(f'You have used up all {ATTEMPTS_COUNT_MAX} attempts to enter correct data. Please try again later.')
    else:
        print('Incorrect authorization data.')

    attempt += 1
