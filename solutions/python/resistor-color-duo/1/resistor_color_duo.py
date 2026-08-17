"""The input here is a list of colors (example: ["red", "green"]) the function below prints only int value of first 2 colors in the list."""

colors_map_for_resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors): 
    """Using if/else condition: RETURNS NUMERIC VALUE OF FIRST 2 VALUES IN COLORS[]"""
    result = 0
    values_in_input = colors[:2]
    for index, color in enumerate(values_in_input):
        if index == 0:
            result += colors_map_for_resistor.index(color) * 10
        else:
            result += (colors_map_for_resistor.index(color))
    return result    