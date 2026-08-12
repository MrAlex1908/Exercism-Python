"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    list_of_round_numbers = [number]
    
    while len(list_of_round_numbers) != 3: 
        number += 1 
        list_of_round_numbers.append(number)
    return list_of_round_numbers


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    
    all_rounds_list = rounds_1 + rounds_2
    return all_rounds_list 


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True
    else: 
        return False    


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    result = sum(hand) / len(hand)
    return result 


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    first_card = hand[0]
    last_card = hand[-1]
    arithmetic_mean = (first_card + last_card) / 2

    index_of_middle_card = len(hand) // 2
    middle_card = hand[index_of_middle_card]

    true_average = card_average(hand)
    
    return arithmetic_mean == true_average or middle_card == true_average

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_cards = hand[::2]
    odd_cards = hand[1::2]

    average_even_cards = card_average(even_cards)
    average_odd_cards = card_average(odd_cards)

    return average_even_cards == average_odd_cards


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    last_card = hand[-1]

    if last_card == 11: 
        doubled_last_card = last_card * 2
        hand[-1] = doubled_last_card
    return hand
