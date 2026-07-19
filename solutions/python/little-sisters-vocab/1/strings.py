"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    result_task_1 = "un" + word 
    return result_task_1


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return ' :: '.join([prefix] + prefixed_words)
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    # Check if the word ends with 'ness'
    if word.endswith('ness'):
        # Remove the 'ness' suffix
        root_word = word[:-4]
        
        # Check if the root word ends with 'i' and the original word had a consonant before 'y'
        if root_word.endswith('i') and len(root_word) > 1 and root_word[-2] not in 'aeiou':
            # Replace 'i' with 'y'
            root_word = root_word[:-1] + 'y'
        
        return root_word
    else:
        return word  # Return the original word if it doesn't end with 'ness'

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
   
    words = sentence.split()    
    adjective = words[index]
    
    adjective = adjective.strip('.,!?')
    
    verb = adjective + 'en'
    
    return verb
    
