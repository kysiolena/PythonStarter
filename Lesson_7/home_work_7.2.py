links = {}

while True:
    short_link = input('Enter short URL: ')

    if short_link:
        while True:
            link = input('Enter URL: ')

            if link:
                links[short_link] = link

                break

        option = input('Do you want to add another link? (Yes/No) ')

        if option.lower() == 'no':
            break

while True:
    short_link = input('Enter short URL for get full url: ')

    if short_link in links:
        print(f'Full link is: {links.get(short_link)}')

        option = input('Do you want to get another link? (Yes/No) ')

        if option.lower() == 'no':
            break
    else:
        print(f'Short URL {short_link} does not exist.')

print()

for short_link, link in links.items():
    print(f'{short_link=} {link=}')
