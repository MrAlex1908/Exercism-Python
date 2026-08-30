"""
Find all valid anagrams of a target word from a list of candidates.
"""
def find_anagrams(word, candidates):
    """
    Find all anagrams of a given word among the provided candidates.

    Comparison is case-insensitive, but matching candidates are returned
    with their original letter case. A word is not considered an anagram
    of itself.
    """
    word_letters = list(word.lower())
    result = []

    for candidate in candidates:
        word_letters_copy = word_letters.copy()
        candidate_letters = list(candidate.lower())
        is_anagram = True

        if candidate.lower() == word.lower():
            is_anagram = False

        for letter in candidate_letters:
            if letter in word_letters_copy:
                word_letters_copy.remove(letter)
            else:
                is_anagram = False
                break

        if len(word_letters_copy) == 0 and is_anagram:
            result.append(candidate)

    return result
    