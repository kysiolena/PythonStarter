import random

import pyjokes

from Project_1.constants import FILMS, GAMES, MUSIC


def get_joke() -> str:
    """
    Get the joke

    :return: str
    """
    return pyjokes.get_joke()


def get_some_by_genre(some: str = 'film', genre: str = 'fantasy') -> str:
    """
    Get the film or music, or game by genre

    :param some: str
    :param genre: str
    :return: str
    """
    some_dict = dict()
    match some.lower():
        case 'film':
            some_dict = FILMS
        case 'music':
            some_dict = MUSIC
        case 'game':
            some_dict = GAMES

    if genre.lower() in some_dict.keys():
        return random.choice(some_dict[genre.lower()])
    else:
        return f'Sorry... But genre «{genre}» doesn\'t exist in our list of {some.lower()}s.'
