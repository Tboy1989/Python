"""
Troydj Sort - Bidirectional Selection Sort

In each pass the unsorted sub-array is scanned exactly once to find both its
minimum and maximum elements.  The minimum is placed at the left boundary and
the maximum at the right boundary, then both boundaries are advanced inward.

This halves the number of full-array passes needed compared with ordinary
selection sort while keeping the same O(n²) worst-case time complexity.

References:
  - https://en.wikipedia.org/wiki/Selection_sort#Variants
"""


def troydj_sort(collection: list) -> list:
    """Sort a list in ascending order using bidirectional selection sort.

    :param collection: A mutable list of comparable items.
    :return: The same list sorted in ascending order.

    >>> troydj_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> troydj_sort([])
    []

    >>> troydj_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> troydj_sort([1])
    [1]

    >>> troydj_sort([3, 3, 3])
    [3, 3, 3]

    >>> troydj_sort(list(range(10, 0, -1))) == list(range(1, 11))
    True
    """
    lo = 0
    hi = len(collection) - 1

    while lo < hi:
        min_idx = lo
        max_idx = lo

        for k in range(lo, hi + 1):
            if collection[k] < collection[min_idx]:
                min_idx = k
            if collection[k] > collection[max_idx]:
                max_idx = k

        # Place the minimum at the left boundary.
        collection[lo], collection[min_idx] = collection[min_idx], collection[lo]

        # If the maximum was sitting at `lo`, its value has just been moved to
        # `min_idx`, so update the pointer before the right-side swap.
        if max_idx == lo:
            max_idx = min_idx

        # Place the maximum at the right boundary (skip when min == max,
        # which only occurs when every element in [lo, hi] is equal).
        if min_idx != max_idx:
            collection[hi], collection[max_idx] = collection[max_idx], collection[hi]

        lo += 1
        hi -= 1

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(troydj_sort(unsorted))
