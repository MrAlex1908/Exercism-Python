"""
Encode and decode text using the Atbash cipher.

The Atbash cipher replaces each letter of the alphabet with the letter
at the same position from the reversed alphabet. Digits remain unchanged.
Encoded text is grouped into blocks of five characters.
"""

plain = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

cipher = [
    'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n',
    'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'
]


def encode(plain_text):
    """
    Encode text using the Atbash cipher.

    Letters are converted to lowercase and replaced with their corresponding
    Atbash letters. Digits are preserved, while spaces and punctuation are
    ignored. The encoded result is grouped into blocks of five characters.

    Args:
        plain_text (str): Text to encode.

    Returns:
        str: Atbash-encoded text grouped into blocks of five characters.
    """
    lower_text_encode = plain_text.lower()

    encoded_text = ""

    for symbol in lower_text_encode:
        if symbol in plain:
            searching_index = plain.index(symbol)
            encoded_text += cipher[searching_index]

        if symbol.isdigit():
            encoded_text += symbol

    result = " ".join(
        [encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)]
    )

    return result


def decode(ciphered_text):
    """
    Decode text encrypted with the Atbash cipher.

    Encoded letters are converted back using the reversed alphabet.
    Digits remain unchanged, while spaces between encoded groups are ignored.

    Args:
        ciphered_text (str): Atbash-encoded text.

    Returns:
        str: Decoded text without spaces between cipher groups.
    """
    lower_text_decode = ciphered_text.lower()

    decoded_text = ""

    for char in lower_text_decode:
        if char in cipher:
            search_index = cipher.index(char)
            decoded_text += plain[search_index]

        if char.isdigit():
            decoded_text += char

    return decoded_text