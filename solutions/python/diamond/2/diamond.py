"""Generate alphabet diamonds from uppercase letters."""

import string

ALPHABET = list(string.ascii_uppercase)


def rows(letter):
    """Return a diamond-shaped list of strings ending at the given letter.

    The diamond starts with "A", expands alphabetically until the supplied
    uppercase letter, and then mirrors the upper half in reverse order.

    Args:
        letter: An uppercase letter that determines the widest row.

    Returns:
        A list of strings representing the complete diamond.
    """
    if letter == "A":
        return list(letter)

    upper_diamond = []
    letter_index = ALPHABET.index(letter)
    alphabet_range = ALPHABET[:(letter_index + 1)]

    for current_index, current_letter in enumerate(alphabet_range):
        outer_spaces = letter_index - current_index
        current_str_length = current_index * 2 + 1
        inner_spaces = current_str_length - 2

        if current_index == 0:
            upper_diamond.append(
                (" " * outer_spaces)
                + current_letter
                + (" " * outer_spaces)
            )
        else:
            upper_diamond.append(
                (" " * outer_spaces)
                + current_letter
                + (" " * inner_spaces)
                + current_letter
                + (" " * outer_spaces)
            )

    lower_diamond = upper_diamond[:-1]
    lower_diamond.reverse()

    result = upper_diamond + lower_diamond
    return result