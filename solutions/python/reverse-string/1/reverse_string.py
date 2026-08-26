"""
Reverse a given string using recursion.

The function processes the string from the end toward the beginning,
recursively reducing the remaining part until the base case is reached.
"""
def reverse(text):
    """
Reverse the provided string recursively.

Args:
    text (str): The string to reverse.

Returns:
    str: The reversed string.
"""
    # Base case the exit from recursion
    if text == "":
        return ""

    current_word = text[:-1]
    
    return text[-1] + reverse(current_word)
