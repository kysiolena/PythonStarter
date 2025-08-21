"""
Створіть магазин канцтоварів використовуючи списки для зберігання елементів.
Для додавання елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані
у вигляді кортежу додавати у створений список на початку. Результат вивести на екран.
Під час створення дотримуйтесь правил специфікації PEP 8.
"""
from collections import namedtuple

# product tuple
Product = namedtuple('Product', 'title price')

# default list of products
products = []


def crete_product() -> Product:
    """ Create Product """
    prod_title = input('Enter title of the product: ')
    prod_price = input('Enter price of the product: ')

    return Product(prod_title, prod_price)


def store_product(product: Product):
    """ Store Product """
    products.append(product)


# create products
while True:
    prod = crete_product()

    store_product(prod)

    action = input('Create another one? (Yes/No): ')

    if action and action.lower() == 'no':
        print('Bye!')
        break

# show products list
print(products)
