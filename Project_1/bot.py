from colorama import Fore, Back  # , Style

from Project_1.constants import FILMS, GAMES, MUSIC
from Project_1.content import get_joke, get_some_by_genre
from Project_1.games import run_game, game_rock_paper_scissors, game_guess_number, game_wheel_of_fortune
from Project_1.utils import is_end


def start_bot():
    WANTS = (
        {
            'key': 'joke',
            'title': 'Get a random joke',
            'filter': (),
            'handler': get_joke
        },
        {
            'key': 'film',
            'title': 'Get a movie recommendation',
            'filter': ('genre', FILMS.keys()),
            'handler': get_some_by_genre
        },
        {
            'key': 'music',
            'title': 'Get a song recommendation',
            'filter': ('genre', MUSIC.keys()),
            'handler': get_some_by_genre
        },
        {
            'key': 'game',
            'title': 'Get a game recommendation',
            'filter': (
                'type', GAMES.keys()
            ),
            'handler': get_some_by_genre
        },
        {
            'key': 'play',
            'title': 'Play the game',
            'filter': ('game', [
                {
                    'title': 'Rock Paper Scissors',
                    'handler': game_rock_paper_scissors
                },
                {
                    'title': 'Guess The Number',
                    'handler': game_guess_number
                },
                {
                    'title': 'Wheel of Fortune',
                    'handler': game_wheel_of_fortune
                }
            ]
                       ),
            'handler': run_game
        },
    )

    def draw_error(text: str = 'Something went wrong...'):
        print(Back.LIGHTMAGENTA_EX, end='')
        print(Fore.RED, end='')
        print(text)

    def draw_answer(text: str):
        print(Back.BLUE, end='')
        print(Fore.LIGHTCYAN_EX, end='')
        print(text)

    def draw_separator():
        print('=' * 7)

    def set_style_for_end_check():
        print(Back.YELLOW, end='')
        print(Fore.GREEN, end='')

    def set_style_for_dialog():
        print(Back.LIGHTMAGENTA_EX, end='')
        print(Fore.BLUE, end='')

    def reset_style():
        print(Back.RESET, end='')
        print(Fore.RESET, end='')

    while True:
        set_style_for_dialog()

        print('Select what do you want to do?')

        for index, want in enumerate(WANTS):
            print(f'\t{index + 1}. {want['title']}')

        choice = input(f'Enter number from 1 to {len(WANTS)}: ')

        if choice.isdigit():
            choice = int(choice)

            if choice <= len(WANTS):
                # film, game, etc.
                choice_item = WANTS[choice - 1]
                choice_filter_item = None

                choice_filter = choice_item['filter'] if choice_item and choice_item['filter'] else tuple()
                if len(choice_filter) == 2:
                    # genre, type, game, etc.
                    key = choice_filter[0]
                    values = list(choice_filter[1])

                    print(f'\tSelect the {key}')

                    for index, value in enumerate(values):
                        print(f'\t\t{index + 1}. {value if isinstance(value, str) else value['title']}')

                    choice_filter_input = input(f'Enter number from 1 to {len(values)}: ')

                    if choice_filter_input.isdigit():
                        choice_filter_input = int(choice_filter_input)

                        if choice_filter_input <= len(values):
                            choice_filter_item = values[choice_filter_input - 1]

                    draw_separator()

                    # run handler with parameters
                    if callable(choice_item['handler']):
                        if isinstance(choice_filter_item, str):
                            # display something
                            draw_answer(
                                f'Your {choice_item['key']} recommendation is «{choice_item['handler'](choice_item['key'], choice_filter_item)}»')
                            set_style_for_dialog()
                        elif callable(choice_filter_item['handler']):
                            # run something
                            reset_style()
                            choice_item['handler'](choice_filter_item['handler'])
                            set_style_for_dialog()
                else:
                    draw_separator()

                    # run handler without parameters
                    if callable(choice_item['handler']):
                        draw_answer(choice_item['handler']())
                        set_style_for_dialog()

                set_style_for_end_check()
                if is_end('Do you want to stop communicating with the Bot?'):
                    break
            else:
                draw_error('Invalid number! Try again...')
                set_style_for_dialog()

        else:
            draw_error('Invalid number! Try again...')
            set_style_for_dialog()
