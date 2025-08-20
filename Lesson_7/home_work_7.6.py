from collections import namedtuple

''' «Бібліотека» '''

Book = namedtuple('Book', 'author work')

library = set()

# Add
library.add(Book('Richard Bach', 'Jonathan Livingston Seagull'))
library.add(Book('Richard Bach', 'Illusions: The Adventures of a Reluctant Messiah'))
library.add(Book('Richard Bach', 'The Bridge Across Forever: A Love Story'))
library.add(Book('Elizabeth Gilbert', 'Eat Pray Love'))
library.add(Book('Elizabeth Gilbert', 'The Signature of All Things'))
library.add(Book('Elizabeth Gilbert', 'Eat Pray Love Made Me Do It'))
library.add(Book('Jack London', 'Martin Eden'))
library.add(Book('Jack London', 'The Iron Heel'))
library.add(Book('Fannie Flagg', 'Fried Green Tomatoes at the Whistle Stop Cafe'))
library.add(Book('Ocean Vuong', 'The Emperor of Gladness'))

print(f'{library=}')
print('=' * 10)

# Remove
book_for_remove = Book('Ocean Vuong', 'The Emperor of Gladness')
# print('Remove: ', library.remove(book_for_remove))
# Discard (without error)
print('Discard: ', library.discard(book_for_remove))

library_sorted_by_author = list(library)
library_sorted_by_author.sort(key=lambda book: book.author.lower())
print(f'{library_sorted_by_author=}')
print('=' * 10)

library_sorted_by_work = list(library)
library_sorted_by_work.sort(key=lambda book: book.work.lower())
print(f'{library_sorted_by_work=}')
print('=' * 10)
