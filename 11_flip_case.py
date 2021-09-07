def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lower = to_swap.lower()
    upper = to_swap.upper()

    flipped = ""

    for letter in phrase:
        if letter == lower:
            flipped += upper
        elif letter == upper:
            flipped += lower
        else:
            flipped += letter
    return flipped