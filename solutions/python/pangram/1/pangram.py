"""The function to figure out if the sentence is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once. The function takes a string as input and returns True if it is a pangram, and False otherwise."""

def is_pangram(sentence):
    """_The function checks if the sentence contains every letter of the alphabet at least once."""
    
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    
    for letter in alphabet:
        if letter not in sentence_set:
            return False
            
    return True