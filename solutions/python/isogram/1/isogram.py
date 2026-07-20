def is_isogram(phrase):
    result = phrase.lower().replace("-", "").replace(" ", "")
    return len(result) == len(set(result))