#!/usr/bin/env python3
# ITP2_11_D: Bitset 2 - Enumeration of Combinations

def combination(n, k):
    """
    Generate all combinations of k elements from n elements using bit manipulation.

    Args:
        n (int): The total number of elements (elements are indexed from 0 to n-1).
        k (int): The number of elements in each combination.

    Yields:
        list[int]: A list containing the indices of the selected elements for each combination, in ascending order.

    Example:
        >>> list(combination(3, 2))
        [[0, 1], [0, 2], [1, 2]]
    """
    def _combination(i, j, mask):
        """
        Recursive helper function to generate all valid combinations.

        Args:
            i (int): The current element index being considered.
            j (int): The number of elements left to select.
            mask (int): The current bitmask representing which elements have been chosen.

        Yields:
            list[int]: The next valid combination represented as a list of indices.
        """
        if i > n:
            # If the index exceeds n, stop the recursion.
            return
        if j == 0:
            # If no elements left to select, yield the current combination.
            yield nums(n, mask)
        elif i <= n:
            # Include current index i in the combination.
            yield from _combination(i + 1, j - 1, mask | (1 << i))
            # Exclude current index i from the combination.
            yield from _combination(i + 1, j, mask)

    # Start the recursion with the first element, all k elements to be selected, and an empty bitmask.
    yield from _combination(0, k, 0)

def nums(size, bit):
    """
    Convert a bitmask to a list of indices where the bits are set.

    Args:
        size (int): The total number of possible indices.
        bit (int): The integer bitmask representing selected elements.

    Returns:
        list[int]: List containing the indices where the bitmask has 1s.

    Example:
        >>> nums(4, 7)
        [0, 1, 2]
    """
    return [n for n in range(size) if bit & (1 << n)]

def bit(nums):
    """
    Convert a list of indices to a corresponding bitmask representation.

    Args:
        nums (list[int]): The list of indices to set in the bitmask.

    Returns:
        int: Bitmask integer representing the indices.

    Example:
        >>> bit([0, 1, 2])
        7
    """
    return sum(1 << n for n in nums)

def run():
    """
    Main function to read input, generate, and print all combinations in order of their bitmask value.

    Reads:
        Two space-separated integers n and k from standard input.

    Prints:
        For each combination, prints its bitmask (as an integer), a colon, and the corresponding combination, all elements space-separated.
    """
    # Parse two integers n and k from input
    n, k = [int(i) for i in input().split()]

    # Generate all combinations, sort by bitmask value for consistent output
    for ns in sorted(combination(n, k), key=bit):
        # Print bitmask value and the combination
        print("{}: {}".format(bit(ns), " ".join(str(i) for i in ns)))

if __name__ == '__main__':
    run()