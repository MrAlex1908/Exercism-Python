"""
The file contains function that can transform colors from resistors
to a real values of ohms with tolerances.

In this option of task 4 and 5 colors on input are allowed.
Edge-case input with only black color, should be equal 0 ohms.
"""

COLORS_MAP = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

TOLERANCE_MAP = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def choose_label(final_multiplied_value, tolerance_value):
    """
    Choose the correct resistance unit and create the final label.
    """

    if final_multiplied_value < 1000:
        return f"{final_multiplied_value} ohms {tolerance_value}"

    if final_multiplied_value < 1000000:
        kiloohms_numeric_value = final_multiplied_value / 1000

        if kiloohms_numeric_value.is_integer():
            kiloohms_numeric_value = int(kiloohms_numeric_value)

        return f"{kiloohms_numeric_value} kiloohms {tolerance_value}"

    if final_multiplied_value < 1000000000:
        megaohms_numeric_value = final_multiplied_value / 1000000

        if megaohms_numeric_value.is_integer():
            megaohms_numeric_value = int(megaohms_numeric_value)

        return f"{megaohms_numeric_value} megaohms {tolerance_value}"

    gigaohms_numeric_value = final_multiplied_value / 1000000000

    if gigaohms_numeric_value.is_integer():
        gigaohms_numeric_value = int(gigaohms_numeric_value)

    return f"{gigaohms_numeric_value} gigaohms {tolerance_value}"


def resistor_label(colors):
    """
    Can transform colors from resistors to a real values of ohms
    with tolerances and label them accordingly.
    """

    # The edge-case:
    first_color = colors[0]

    if len(colors) == 1 and first_color == "black":
        return "0 ohms"

    # The case with 4 color input:
    if len(colors) == 4:
        first_2_colors = colors[:2]
        numeric_value_4_band = 0

        for index, color in enumerate(first_2_colors):
            if index == 0:
                numeric_value_4_band += COLORS_MAP.index(color) * 10
            else:
                numeric_value_4_band += COLORS_MAP.index(color)

        # Algorithm for 3rd value when there are 4 colors.
        color_3 = colors[2]
        multiplier_how_much_zeros = 10 ** COLORS_MAP.index(color_3)
        final_multiplied_value = (
            numeric_value_4_band * multiplier_how_much_zeros
        )

        # Algorithm for 4th value.
        color_4 = colors[3]
        tolerance_value = TOLERANCE_MAP.get(color_4)

    # The case with 5 color input:
    elif len(colors) == 5:
        first_3_colors = colors[:3]
        numeric_value_5_band = 0

        for index, color in enumerate(first_3_colors):
            if index == 0:
                numeric_value_5_band += COLORS_MAP.index(color) * 100
            elif index == 1:
                numeric_value_5_band += COLORS_MAP.index(color) * 10
            else:
                numeric_value_5_band += COLORS_MAP.index(color)

        # Algorithm for 4th value when there are 5 colors.
        color_4 = colors[3]
        multiplier_how_much_zeros = 10 ** COLORS_MAP.index(color_4)
        final_multiplied_value = (
            numeric_value_5_band * multiplier_how_much_zeros
        )

        # Algorithm for 5th value.
        color_5 = colors[4]
        tolerance_value = TOLERANCE_MAP.get(color_5)

    else:
        raise ValueError("Invalid number of resistor colors")

    return choose_label(final_multiplied_value, tolerance_value)