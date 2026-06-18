"""Functions for classifying triangles."""


def is_valid_triangle(sides):
    """Return True if the given sides can form a triangle."""
    side_one, side_two, side_three = sides

    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False

    return (
        side_one + side_two >= side_three
        and side_two + side_three >= side_one
        and side_one + side_three >= side_two
    )


def equilateral(sides):
    """Return True if the given sides form an equilateral triangle."""
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return side_one == side_two and side_one == side_three


def isosceles(sides):
    """Return True if the given sides form an isosceles triangle."""
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return (
        side_one == side_two
        or side_two == side_three
        or side_one == side_three
    )


def scalene(sides):
    """Return True if the given sides form a scalene triangle."""
    if not is_valid_triangle(sides):
        return False

    side_one, side_two, side_three = sides
    return (
        side_one != side_two
        and side_two != side_three
        and side_one != side_three
    )