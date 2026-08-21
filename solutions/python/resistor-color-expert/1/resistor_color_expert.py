"""
The file contains function that can transform colors from resistors to a real values of ohms with tolerances. 
In this option of task 4 and 5 colors on input are allowed.
Edge-case input with only black color, should be equal 0 ohms.
"""

COLORS_MAP = [
    "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
    ]
TOLERANCE_MAP = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}

def resistor_label(colors):
    """
    Can transform colors from resistors to a real values of ohms with tolerances and label them accordingly.
    """
    # The edge-case:
    first_color = colors[0]
    if len(colors) == 1 and first_color == "black": 
        return "0 ohms"
    
    # The case with 4 color input:
    first_2_colors = colors[:2]
    numeric_value_4_band = 0

    if len(colors) == 4:
        for index, color in enumerate(first_2_colors):
            if index == 0:
                numeric_value_4_band += (COLORS_MAP.index(color)) * 10
            else: 
                numeric_value_4_band += (COLORS_MAP.index(color))

        # algorithm for 3rd value in list[colors] when there are 4 colors 
        color_3 = colors[2]
        multiplier_how_much_zeros = 10 ** (COLORS_MAP.index(color_3))
        final_multiplied_value = numeric_value_4_band * multiplier_how_much_zeros
    
        # algorithm for 4th value in list[colors]
        color_4 = colors[3]
        tolerance_value = TOLERANCE_MAP.get(color_4)
    
    # THE CASE WITH 5 COLOR INPUT:
    first_3_colors = colors[:3]
    numeric_value_5_band = 0
    
    if len(colors) == 5:
        for index, color in enumerate(first_3_colors):
            if index == 0:
                numeric_value_5_band += (COLORS_MAP.index(color)) * 100
            elif index == 1: 
                numeric_value_5_band += (COLORS_MAP.index(color)) * 10
            else:
                numeric_value_5_band += (COLORS_MAP.index(color))

        # algorithm for 4th value in list[colors] when there are 5 colors 
        color_4 = colors[3]
        multiplier_how_much_zeros = 10 ** (COLORS_MAP.index(color_4))
        final_multiplied_value = numeric_value_5_band * multiplier_how_much_zeros
    
        # algorithm for 5th value in list[colors]
        color_5 = colors[4]
        tolerance_value = TOLERANCE_MAP.get(color_5)
        
    # choosing the label
    
    if final_multiplied_value < 1000:
        return f"{final_multiplied_value} ohms {tolerance_value}"
    if final_multiplied_value < 1000000 : 
        kiloohms_numeric_value = final_multiplied_value / 1000
        if kiloohms_numeric_value.is_integer():
            return f"{int(kiloohms_numeric_value)} kiloohms {tolerance_value}"
        else:
            return f"{final_multiplied_value / 1000} kiloohms {tolerance_value}"
    if final_multiplied_value < 1000000000:
        megaohms_numeric_value = final_multiplied_value / 1000000
        if megaohms_numeric_value.is_integer():
            return f"{int(megaohms_numeric_value)} megaohms {tolerance_value}"
        else:
            return f"{final_multiplied_value / 1000000} megaohms {tolerance_value}"
    else:
        gigaohms_numeric_value = final_multiplied_value / 1000000000
        if gigaohms_numeric_value.is_integer():
            return f"{int(gigaohms_numeric_value)} gigaohms {tolerance_value}"
        else:
            return f"{final_multiplied_value / 1000000000} gigaohms {tolerance_value}"