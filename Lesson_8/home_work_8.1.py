MY_NAME = 'Olena'


def greet(name: str = None) -> str:
    print(f'Hello, {name if name else MY_NAME}!!! 😀')


greet()
greet('Olha')
