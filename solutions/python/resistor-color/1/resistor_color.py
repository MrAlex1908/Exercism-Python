"""Rasberry Pi resistor color mind-map."""

colors_map_for_resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def color_code(color):
    """The function returns numeric value of the current "resistor" color."""
    return colors_map_for_resistor.index(color)


def colors():
    """The function returns all possible colours of resistor."""
    return colors_map_for_resistor
