"""The script checks if a word is an isogram, using buffer (множество)"""

def is_isogram(phrase):
    buffer_str = ""
    clean_phrase = phrase.lower().replace("-", "").replace(" ", "")
    for char in clean_phrase:
        if char not in buffer_str:
            buffer_str +=  char
        else:
            return False
    return True