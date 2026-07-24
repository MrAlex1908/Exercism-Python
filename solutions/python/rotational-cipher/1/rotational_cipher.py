"""The function for implementation of the rotational cipher (ROT13) or another algorithm. It takes a string as input and returns the ROT13 encoded string."""

def rotate(text, key):
    """ The function goes through three possible cases: char is a lowercase letter, char is an uppercase letter, and char is not a letter. It shifts the letters by the key value and wraps around if necessary. """
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result