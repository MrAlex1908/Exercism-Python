""" The function for calculation the leap year. """
def leap_year(year):
    """ The function for calculation the leap year. """
    if year % 400 == 0:   
        return True 
    if year % 100 == 0:  
        return False
    if year  % 4 == 0:  
        return True 
    else:
        return False