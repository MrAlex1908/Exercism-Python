"""
Implement binary search iteratively on a sorted list.

The search range is repeatedly narrowed by adjusting its start and end
boundaries until the requested value is found or no elements remain.
"""


def find(search_list, value):
    """
    Find the index of a value in a sorted list using binary search.

    Repeatedly checks the middle element of the current search range and
    narrows the range to either the left or right half.

    Args:
        search_list: A sorted list of values to search.
        value: The value to find.

    Returns:
        The index of the requested value.

    Raises:
        ValueError: If the value is not present in the list.
    """
    start = 0
    end = len(search_list) - 1

    while end >= start:
        mid = (end + start) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            end = mid - 1
        elif search_list[mid] < value:
            start = mid + 1

    raise ValueError("value not in array")