"""
Functions for checking whether brackets in a string are balanced
and correctly nested.
"""
def is_paired(input_string):
    """
Check whether (), [], and {} brackets in the input string are balanced.

Any other characters are ignored.

Args:
    input_string (str): The string to check.

Returns:
    bool: True if all brackets are balanced and correctly nested,
    otherwise False.
"""
    opening_brackets = ["{", "[", "("]
    closing_brackets = ["}", "]", ")"]
    memory = []
    for char in input_string:
        if char in opening_brackets:
            memory.append(char)      
        if char in closing_brackets and memory == []:
            return False
        if char in closing_brackets:
            if opening_brackets.index(memory.pop()) != closing_brackets.index(char):
                return False
    if len(memory) != 0: 
        return False 
    return True