"""The function to figure out if the sentence is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once. The function takes a string as input and returns True if it is a pangram, and False otherwise."""

def is_pangram(sentence):
    """Using set() and .issubset in this option."""
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)