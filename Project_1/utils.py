def is_end(message: str = 'Do you want to stop?') -> bool:
    """
    Checks if the user wants to stop the program

    :param message: str
    :return: bool
    """
    choice = input(f'{message} (Yes/No): ')
    if choice.lower() == 'yes':
        return True
    else:
        return False
