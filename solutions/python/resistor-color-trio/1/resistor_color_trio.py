colors = ["black", "white", "violet"]

"""
The file (window) contains def() for reverting the colors of transistor to the ohms value

"""

colors_map_for_resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    """_summary_:
    The function help to revert colors to ohms values. 

    Args:
        colors (_list_): 3 colors possible on the input
    """
    first_2_colors = colors[:2]
    colors_numeric_value = 0
    
    for index, color in enumerate(first_2_colors):
        if index == 0:
            colors_numeric_value += (colors_map_for_resistor.index(color)) * 10
        else: 
            colors_numeric_value += (colors_map_for_resistor.index(color))
            
    # algorithm for 3 value in list[colors] 
    
    last_color = colors[2]
    multiplier_how_much_zeros = 10 ** (colors_map_for_resistor.index(last_color))
    
    # getting the ohms value:

    result_value = colors_numeric_value * multiplier_how_much_zeros
    
    # choosing the label
    
    if result_value < 1000:
        return f"{result_value} ohms"
    if result_value < 1000000 : 
        return f"{result_value // 1000} kiloohms"
    if result_value < 1000000000:
        return f"{result_value // 1000000} megaohms"
    else:
        return f"{result_value // 1000000000} gigaohms"