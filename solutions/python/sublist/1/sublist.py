"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    """
    Function for defining relationships between 2 lists.
    Algorythm of the function: 
    1. defining equality 
    2. defining longest and shortest list 
    3. defining unequality (if there are no longest and shortest)
    4. Defining SUBLIST
    5. Defining SUPERLIST
    """
    if list_one == list_two: 
        return EQUAL
    if len(list_one) > len(list_two):
        long_list = list_one
        short_list = list_two
        list_one_is_long = True
    elif len(list_one) < len(list_two):
        long_list = list_two
        short_list = list_one
        list_one_is_long = False
    else:
        return UNEQUAL
    for value in range(len(long_list) - len(short_list) +1):
        if long_list[value : value + len(short_list)] == short_list:
            if list_one_is_long: 
                return SUPERLIST
            else:
                return SUBLIST
    return UNEQUAL