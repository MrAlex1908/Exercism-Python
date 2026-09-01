"""
Implement binary search recursively on a sorted list.

The search range is repeatedly narrowed through recursive calls until
the requested value is found or the search boundaries cross.
"""


def find(search_list, value):
    """
    Find the index of a value in a sorted list using recursive binary search.

    Args:
        search_list: A sorted list of values to search.
        value: The value to find.

    Returns:
        The index of the requested value.

    Raises:
        ValueError: If the value is not present in the list.
    """

    def search(start, end):
        """
        Search recursively within the specified index boundaries.

        Args:
            start: The first index of the current search range.
            end: The last index of the current search range.

        Returns:
            The index of the requested value.

        Raises:
            ValueError: If the search range is exhausted without finding
                the value.
        """
        if start > end:
            raise ValueError("value not in array")

        mid = (start + end) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            return search(start, mid - 1)
        else:
            return search(mid + 1, end)

    return search(0, len(search_list) - 1)