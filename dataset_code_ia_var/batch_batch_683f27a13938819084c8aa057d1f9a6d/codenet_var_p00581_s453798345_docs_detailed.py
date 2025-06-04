#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    """
    Main function to execute the program workflow.
    It reads input for the problem, processes it, and outputs the solution.
    """
    # Read dimensions of the grid
    H, W = read_ints()

    # Read the grid itself as a list of strings
    S = [inp() for _ in range(H)]

    # Solve the problem using the solve function and print the result
    print(solve(H, W, S))

def solve(H, W, S):
    """
    Computes the total number of patterns in the grid that meet the criteria described below.

    Specifically, for each cell containing 'J', counts the number of pairs ('O' to the right, 'I' below)
    such that in each row (to the right of the J) there is an 'O', and in each column (below the J) 
    there is an 'I'. Sums this quantity for all 'J' in the grid.

    Args:
        H (int): The number of rows in the grid.
        W (int): The number of columns in the grid.
        S (List[str]): The grid itself, represented as a list of strings.

    Returns:
        int: The total count of valid patterns as described above.
    """
    # o_table[y][x] keeps, for each cell (y, x), the number of 'O's to the right
    # (including current cell) in the row y
    o_table = [[0] * W for _ in range(H)]
    for y in range(H):
        count = 0
        # Traverse the row from right to left
        for x in range(W - 1, -1, -1):
            if S[y][x] == 'O':
                count += 1
            o_table[y][x] = count

    # i_table[y][x] keeps, for each cell (y, x), the number of 'I's below
    # (including current cell) in the column x
    i_table = [[0] * W for _ in range(H)]
    for x in range(W):
        count = 0
        # Traverse the column from bottom to top
        for y in range(H - 1, -1, -1):
            if S[y][x] == 'I':
                count += 1
            i_table[y][x] = count

    # Compute the answer: for each 'J', multiply corresponding counts and sum up
    ans = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == 'J':
                ans += o_table[y][x] * i_table[y][x]

    return ans

###############################################################################
# AUXILIARY FUNCTIONS

# Set DEBUG flag based on the environment variable
DEBUG = 'DEBUG' in os.environ

def inp():
    """
    Reads a line from the standard input, stripping the trailing newline.

    Returns:
        str: The input line with the trailing newline removed.
    """
    return sys.stdin.readline().rstrip()

def read_int():
    """
    Reads a single integer from the standard input.

    Returns:
        int: The parsed integer from the input line.
    """
    return int(inp())

def read_ints():
    """
    Reads a line from the standard input, splits it into tokens, and converts each to an integer.

    Returns:
        List[int]: The list of integers read from the input.
    """
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    """
    Prints debugging messages to the standard output if the DEBUG flag is set.

    Args:
        *value: Values to print.
        sep (str, optional): Separator to use between values. Defaults to ' '.
        end (str, optional): Endline character to use. Defaults to '\\n'.
    """
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()