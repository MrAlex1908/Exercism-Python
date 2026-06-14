"""Calculation is a number is an Armstrong number."""
def is_armstrong_number(number):
    """ The algorithm of calculation. """
    x = str (number) 
    each_number_list = list(x)
    counted_length = len(x)
    total = 0
    for digit in each_number_list: 
        total += int (digit) ** counted_length
    is_armstrong_number_true = total == number
    return is_armstrong_number_true