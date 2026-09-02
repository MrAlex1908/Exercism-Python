"""Count the number of eggs represented by 1 bits in a display value."""
def egg_count(display_value):
    """Return the number of 1 bits in the binary representation of display_value."""
    counter_list = []
    while display_value > 0:
        counter_list.append(display_value % 2)
        display_value = display_value // 2
    
    counter_list.reverse()    
    binary_value = counter_list
    eggs_number = 0 
    
    for value in binary_value:
        if  value == 1:
            eggs_number += 1
    return eggs_number