"""The script checks if a word is an isogram, using buffer"""

def is_isogram(phrase):
    """The function that creates buffer string and using ```for``` cycle escapes when finds a char that was already added in buffer string """
    buffer_str = ""
    clean_phrase = phrase.lower().replace("-", "").replace(" ", "")
    for char in clean_phrase:
        if char not in buffer_str:
            buffer_str +=  char
        else:
            return False
    return True