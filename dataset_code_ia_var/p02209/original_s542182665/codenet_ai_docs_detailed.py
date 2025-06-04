from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
from decimal import *
import sys

# Augment the recursion limit for environments working with deep recursion
sys.setrecursionlimit(10 ** 6)

# Utility lambda to convert a string to an integer and subtract 1 (useful for 0-based indexing)
int1 = lambda x: int(x) - 1

# Utility function to print a list or iterable, each element on a new line
p2D = lambda x: print(*x, sep="\n")

def II():
    """
    Reads a single integer from standard input.
    Returns:
        int: The integer read.
    """
    return int(sys.stdin.readline())

def MI():
    """
    Reads a line of integers from standard input and unpacks them.
    Returns:
        tuple: Tuple of integers.
    """
    return map(int, sys.stdin.readline().split())

def MI1():
    """
    Reads a line of integers from standard input, converts them to 0-based indexing, and unpacks them.
    Returns:
        tuple: Tuple of 0-based integers.
    """
    return map(int1, sys.stdin.readline().split())

def MF():
    """
    Reads a line of floats from standard input and unpacks them.
    Returns:
        tuple: Tuple of floats.
    """
    return map(float, sys.stdin.readline().split())

def LI():
    """
    Reads a line of integers from standard input and returns them as a list.
    Returns:
        list: List of integers.
    """
    return list(map(int, sys.stdin.readline().split()))

def LI1():
    """
    Reads a line of integers from standard input, converts them to 0-based indexing, and returns as a list.
    Returns:
        list: List of 0-based integers.
    """
    return list(map(int1, sys.stdin.readline().split()))

def LF():
    """
    Reads a line of floats from standard input and returns them as a list.
    Returns:
        list: List of floats.
    """
    return list(map(float, sys.stdin.readline().split()))

def LLI(rows_number):
    """
    Reads multiple lines, each containing integers, from standard input.
    Args:
        rows_number (int): Number of rows/lines to read.
    Returns:
        list: List of lists of integers.
    """
    return [LI() for _ in range(rows_number)]

# Directions for 4-way movement on a grid: down, right, up, left
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    """
    Reads input values, processes bitmasks to maximize the number of elements not included in combinations
    that sum to a target value, and prints the result.

    The problem interpreted is: Given n numbers and an integer k, find the minimum number of numbers 
    to remove so that, in every subset, there is no subset whose sum is exactly k. (Or: max number of numbers left.)

    The function uses bitmask DP to mark all supersets of any subset whose sum is k,
    and finds the largest subset of unused bits (unmarked sets).
    """
    # Read n and k: n is the number of elements, k is the target sum
    n, k = MI()
    # Read the list of n integers
    aa = LI()
    # Create a boolean list to mark which subsets (as bitmasks) are "used"
    # by supersetting a set which sums to k
    bek = [False] * (1 << n)

    # Iterate over all possible subsets represented by bitmasks (from 0 to 2^n - 1)
    for bit in range(1 << n):
        if not bek[bit]:
            # Calculate sum for the current subset (bitmask); include aa[i] if the ith bit is set
            s = sum(a for i, a in enumerate(aa) if bit >> i & 1)
            # If current subset's sum is exactly k, mark it "bek"
            if s == k:
                bek[bit] = True
            else:
                continue
        # After marking a subset which sums to k, mark all of its supersets as "bek"
        for j in range(n):
            bek[bit | 1 << j] = True

    mx = 0  # Stores the largest population count (max subset size) for still-allowed sets
    for bit in range(1 << n):
        if bek[bit]:
            continue  # If bit is already used/marked, skip
        # Count number of 1s (elements included in subset)
        popcnt = bin(bit).count("1")
        # Keep track of maximum population count of all subsets not marked
        if popcnt > mx:
            mx = popcnt
    # Output the minimum number of elements to remove to avoid subsets summing to k
    print(n - mx)

main()