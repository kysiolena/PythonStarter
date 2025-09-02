import random
from collections.abc import Callable

from colorama import Fore

from Project_1.utils import is_end


def run_game(game: Callable) -> None:
    """
    Run Game

    :param game: Callable
    :return: None
    """

    if callable(game):
        game()
    else:
        raise KeyError('Invalid game key')


def game_rock_paper_scissors() -> None:
    """
    Rock Paper Scissors

    :return: None
    """

    options = ('Rock', 'Paper', 'Scissors')
    options_lower = tuple(map(lambda option: option.lower(), options))
    options_first_letters_lower = tuple(map(lambda option: option[0].lower(), options))

    def is_winner(first_gamer_choice: str, second_gamer_choice: str) -> bool | None:
        # The same choices
        if first_gamer_choice == second_gamer_choice:
            return None

        # Check another variants
        match first_gamer_choice:
            case 'rock':
                if second_gamer_choice == 'scissors':
                    return True
                else:
                    return False
            case 'paper':
                if second_gamer_choice == 'rock':
                    return True
                else:
                    return False
            case 'scissors':
                if second_gamer_choice == 'paper':
                    return True
                else:
                    return False
            case _:
                return None

    while True:
        opponent_choice = random.choice(options)

        print()
        choice = input('What is your choice: Rock(R), Paper(P) or Scissors(S)?')

        is_first_letter = choice.lower() in options_first_letters_lower
        is_full = choice.lower() in options_lower

        if choice and (is_full or is_first_letter):
            choice = options[
                options_first_letters_lower.index(choice.lower()) if is_first_letter else options_lower.index(
                    choice.lower())]

            print(Fore.BLUE + 'You chose ' + choice)
            print(Fore.YELLOW + 'Your opponent chose ' + opponent_choice)
            print((Fore.GREEN + 'You won!') if is_winner(choice.lower(), opponent_choice.lower()) else (
                    Fore.LIGHTRED_EX + 'You lost!'))
            print(Fore.BLACK)

            if is_end('Do you want to end the game?'):
                print('Bye!')
                break
        else:
            print(Fore.RED + 'Invalid choice.')
            print(Fore.BLACK)


def game_wheel_of_fortune() -> None:
    """
    Wheel of Fortune

    :return: None
    """
    print('Today fortune is on your side! 🤩 You just won! 🌚')


def game_guess_number() -> None:
    """
    Guess The Number

    :return: None
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    while True:
        hidden_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        while True:
            print()
            user_number = input(f'Guess the number between {MIN_NUMBER} and {MAX_NUMBER}: ')

            if user_number.isdigit():
                user_number = int(user_number)

                if user_number == hidden_number:
                    print(Fore.GREEN + 'Congrats! You guessed the number! 😀')
                    print(Fore.BLACK)
                    break
                else:
                    print(
                        Fore.YELLOW + f'Hidden number is {'greater' if hidden_number > user_number else 'less'} than {user_number}...')

                    print(Fore.BLACK)

            else:
                print(Fore.RED + 'Invalid number!')
                print(Fore.BLACK)

        if is_end('Don\'t want to repeat the game?'):
            print('Bye!')
            break
