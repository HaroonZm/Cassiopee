import itertools
import sys
import math
from functools import lru_cache
from queue import Queue
from operator import mul
from functools import reduce

input = sys.stdin.readline

def main():
    """
    Reads input values and computes the maximum length of a substring containing at most k blocks of consecutive '1's.
    The function reads two integers n and k, where n is the length of the binary string s and k is the maximum allowed
    groups of '1's. It then reads the string s, processes it, and prints the maximum length substring containing at most
    k blocks of consecutive '1's.
    """
    # Read n (length of string) and k (max number of blocks of '1's) from input
    n, k = list(map(int, input().split()))
    # Read the binary string s and append a sentinel character '2' to mark the end of the string
    s = input().strip() + '2'
    ret = 0  # Initialize the result variable to store the maximum length found

    def next0(l: int) -> int:
        """
        Finds the index of the next occurrence of '0' or the string-ending sentinel '2' starting from index l + 1.

        Args:
            l (int): Index to start searching from.

        Returns:
            int: The index of the next '0' or '2', but not exceeding n (the length of the original string).
        """
        if l >= n:
            return l
        l += 1
        while s[l] != '2' and s[l] != '0':
            l += 1
        return min(l, n)

    def next1(l: int) -> int:
        """
        Finds the index of the next occurrence of '1' or the string-ending sentinel '2' starting from index l + 1.

        Args:
            l (int): Index to start searching from.

        Returns:
            int: The index of the next '1' or '2', but not exceeding n (the length of the original string).
        """
        if l >= n:
            return l
        l += 1
        while s[l] != '2' and s[l] != '1':
            l += 1
        return min(l, n)

    # Initialize window pointers
    start = 0  # Start index of the current substring window
    end = 0    # End index of the current substring window

    # Advance 'end' pointer so that the window contains at most k groups of consecutive '1's:
    # 1. Move to the first group of '0's (skipping leading '1's)
    end = next0(end)
    # 2. For each group, move to the next '1', then the next '0' to cover a group of '1's
    for _ in range(k):
        end = next1(end)
        end = next0(end)

    # Initialize the result with the initial window size
    ret = end - start

    # Slide the window: move start and end, maintaining at most k groups of '1's
    while end < n:
        # Move start to the next group of '1's past a block of zeros
        start = next1(next0(start))
        # Move end to the next group of '0's past a block of ones
        end = next0(next1(end))
        # Update the result if we've got a longer valid window
        ret = max(ret, end - start)

    # Output the maximum length found
    print(ret)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()