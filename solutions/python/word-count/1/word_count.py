def count_words(sentence):
    """Count the occurrences of each word in a given sentence"""
    
    sentence = sentence.lower()
    words = []
    current_word = ""
    
    for index, char in enumerate(sentence):
        if char.isalnum():
            current_word += char

        elif (
            char == "'"
            and index > 0
            and index < len(sentence) - 1
            and sentence[index - 1].isalnum()
            and sentence[index + 1].isalnum()
        ):
            current_word += char

        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    
    if current_word:
        words.append(current_word)
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count
