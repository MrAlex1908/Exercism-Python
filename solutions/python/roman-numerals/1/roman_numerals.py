"""Convert an integer to its Roman numeral representation."""
def roman(number):
    """Convert an integer to its Roman numeral representation.

    Parameters:
        number (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the integer.
    """
    if not (0 < number < 4000):
        raise ValueError("Number must be between 1 and 3999")

    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    result = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value

    return result
    