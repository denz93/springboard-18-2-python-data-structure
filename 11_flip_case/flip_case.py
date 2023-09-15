def flip_case(phrase: str, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return "".join(map(lambda char: char.upper() if char == to_swap.lower() else (char.lower() if char == to_swap.upper() else char) ,phrase))
