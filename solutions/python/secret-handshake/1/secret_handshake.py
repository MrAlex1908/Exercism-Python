"""
Convert binary secret handshake codes into their corresponding actions.
"""

list_of_actions = ["wink", "double blink", "close your eyes", "jump", "Reverse the order of the operations in the secret handshake."] 

def commands(binary_str):
    """Convert a binary string into a sequence of secret handshake actions.

    The binary string is read from right to left. Each of the first four
    bits corresponds to a specific action, while the fifth bit reverses
    the order of the collected actions.

    Args:
        binary_str (str): A binary string representing the secret handshake.

    Returns:
        list[str]: A list of actions corresponding to the binary code.
    """
    what_to_do = []
    reversed_binary_str = binary_str[::-1]
    for index, char in enumerate(reversed_binary_str):
        if index != 4:
            if char == "1":
                what_to_do.append(list_of_actions[index])
        elif char == "1":
            what_to_do.reverse()
    return what_to_do