"""
Calculate the sum of unique multiples below a given limit.

For each non-zero factor, find its positive multiples below the limit,
remove duplicates, and return their total sum.

Args:
    limit (int): The upper boundary (exclusive).
    multiples (list[int]): A list of unique, non-negative integers.

Returns:
    int: The sum of all unique multiples.
"""


def sum_of_multiples(limit, multiples):
    """Return the sum of unique multiples below the specified limit."""

    result = set()

    # Collect unique multiples of each non-zero factor.
    for number in multiples:
        if number != 0:
            for multiple in range(number, limit, number):
                result.add(multiple)

    # Calculate and return the total sum.
    return sum(result)