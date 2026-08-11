import math

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