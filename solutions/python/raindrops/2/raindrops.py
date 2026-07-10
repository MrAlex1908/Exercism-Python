"""Convert numbers into raindrop sounds."""
def convert(number):
    """This function converts numbers to sounds of rain."""
    result = ""
    if number % 3 == 0:
        result += "Pling" 
    if number % 5 == 0: 
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "": 
        result = str(number)
    return result