#!/usr/bin/python

from itertools import *
import sys

#################### Library ####################
# (No library functions are defined in the original code,
# but this section is reserved for utility/helper functions.)

#################### Naive ####################
# (No naive implementation is provided in the original script.)

#################### Process ####################

def read_input():
    """
    Reads the input data from stdin.

    Returns:
        tuple: A tuple (N, v) where:
            - N (int): Number of items (universally indexed from 1 to N)
            - v (list of tuples): Each tuple (a, flag) represents:
                a (int): The cost associated with selecting the subset
                flag (int): Bitmask representing the items included in the subset
    Input format:
        The first line contains two integers N and M.
        The next M blocks each describe a subset (set, cost) as:
            - a b   : a is the cost of the subset, b is not used
            - cs... : space-separated list of integer item indices included in the subset
    """
    [N, M] = map(int, raw_input().split())
    v = []
    for k in range(M):
        a, b = map(int, raw_input().split())
        # Read the next line: indices of elements in the current subset
        cs = [int(e) for e in raw_input().split()]
        # Compute the bitmask 'flag' with bits set for each element in cs
        flag = reduce(lambda x, y: x | (1 << (y - 1)), cs, 0)
        v.append((a, flag))
    return (N, v)

def proc():
    """
    Solves the problem using Dynamic Programming (DP) with bitmasks.

    For N items and M available sets with costs, it calculates the minimal
    total cost required to cover all items by selecting from the provided sets.

    Returns:
        int: The minimal cost to cover all N items, or -1 if not possible.
    """
    N, v = read_input()
    L = 1 << N  # Total possible combinations of N items (as bitmask)
    memo = [10 ** 9] * L  # DP array: minimal cost for each subset (bitmask)
    memo[0] = 0  # Base case: cost to cover no items is 0

    # Iterate through all possible subsets (bitmask n)
    for n in range(L - 1):
        # Try using each available set (a: cost, flag: items provided)
        for a, flag in v:
            n1 = n | flag  # New subset after using this set
            # Take the minimal cost: previous cost to create n + cost of this set
            memo[n1] = min(memo[n1], memo[n] + a)

    # If it's impossible to cover all items, return -1
    if memo[L - 1] == 10 ** 9:
        return -1
    else:
        return memo[L - 1]

#################### Main ####################

# Run the process and print result
print proc()