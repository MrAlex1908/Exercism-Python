"""The calculation of number of grains in one sqare and calculation of total number of grains. """

def square(number):
    """ The calculation of number of grains in this function. """
    # when the square value is not in the acceptable range    
    if number <= 0 or number> 64:
        raise ValueError("square must be between 1 and 64")
        
    number_of_grains = 2 ** (number -1)
    return number_of_grains

def total():
    """ The calculation of total number of grains on the chessboard in this function. """
    total_grains = 0
    for square_number in range(1, 65):
        total_grains += square(square_number)
    return total_grains 
