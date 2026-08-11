import math

"""This is a task in witch only 1 function for calculating scores in a darts game.""" 
# See the solution using hypotenuse (wiithout math.hypoth(x, y))
def score(x, y):   
    """the function witch calculates the amount of points. """
    
    hypotenuse = math.sqrt((x ** 2 + y ** 2 ))
    
    if hypotenuse <= 1: 
        return 10
    
    if hypotenuse <= 5:
        return 5
    
    if hypotenuse <= 10:
        return 1
    
    return 0