import math

def score(x, y):   
    """the function witch calculates the amount of points. """
    
    hypotenuse = math.hypot(x, y)
    
    if hypotenuse <= 1: 
        return 10
    
    if hypotenuse <= 5:
        return 5
    
    if hypotenuse <= 10:
        return 1
    
    return 0