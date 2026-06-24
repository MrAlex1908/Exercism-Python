"""The file contains function for translating Eng to Pig Latin language."""
def translate(text):
    """This function must translate English to Pig Latin language."""
    vowels = (("a", "e", "i", "o", "u"))
    clean_word_preparation = text.strip()
    words = clean_word_preparation.split()
    pig_latin_words = []    
    
    # START OF TRANSLATION
    for clean_word in words:
        translated_word = None
        ## Rule 1
        if clean_word.startswith(("a", "e", "i", "o", "u", "yt", "xr")): 
            translated_word = clean_word + "ay"
        
        if translated_word is None:
            
            ## Rule 3 
            qu_letters = "qu"
            for index_rule_3, letter_rule_3 in enumerate(clean_word):
                
                if clean_word[index_rule_3:index_rule_3+2] == qu_letters:
                    qu_word_part = clean_word[:index_rule_3+2]
                    word_part_without_qu = clean_word[index_rule_3 + 2:]
                    translated_word = word_part_without_qu + qu_word_part + "ay"
                    break
                    
                if letter_rule_3 in vowels: 
                    break
                    
        if translated_word is None:
            
            ## Rule 2
            for index, letter in enumerate(clean_word):
                if letter in vowels:
                    consonant_in_the_beginning_of_word = clean_word[:index]
                    rest_part_of_the_word = clean_word[index:]
                    translated_word = rest_part_of_the_word + consonant_in_the_beginning_of_word + "ay"
                    break
                     
        if translated_word is None:        
            ## Rule 4
            for index_rule_4, letter_rule_4 in enumerate(clean_word): 
                if letter_rule_4 == "y":
                    part_before_y = clean_word[:index_rule_4]
                    part_after_y = clean_word[index_rule_4:]
                    translated_word = part_after_y + part_before_y + "ay"
                    break
                
        pig_latin_words.append(translated_word)
        
    result = " ".join(pig_latin_words)
    return result