"""Count the number of eggs represented by 1 bits in a display value."""\
    
def egg_count(display_value):
    """Return the number of 1 bits in the binary representation of display_value."""
    eggs_number = 0 
    
    while display_value > 0: 
        if (display_value % 2) == 1:
            eggs_number += 1
        display_value = display_value // 2
        
    return eggs_number
