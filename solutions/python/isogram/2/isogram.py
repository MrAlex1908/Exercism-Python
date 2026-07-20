"""The script checks if a word is an isogram, using set (множество)"""

def is_isogram(phrase):
    result = phrase.lower().replace("-", "").replace(" ", "")
    return len(result) == len(set(result))