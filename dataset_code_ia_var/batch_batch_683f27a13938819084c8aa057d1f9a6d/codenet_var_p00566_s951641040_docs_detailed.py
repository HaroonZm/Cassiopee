#!/usr/bin/python3

import os
import sys

def main():
    """
    Main entry point of the program.

    Reads the grid dimensions and the grid itself from standard input,
    solves the problem, and prints the result.
    """
    H, W = read_ints()  # Read height and width of the grid
    A = [read_ints() for _ in range(H)]  # Read grid values row by row
    print(solve(H, W, A))  # Solve the problem and output the answer

def solve(H, W, A):
    """
    Computes the minimum cost given a grid and its dimensions.

    For every possible cell (ay, ax) in the grid, calculates the sum over all cells
    of A[y][x] multiplied by min(|y - ay|, |x - ax|), and returns the minimum such cost.

    Args:
        H (int): Height of the grid.
        W (int): Width of the grid.
        A (List[List[int]]): 2D list representing the grid values.

    Returns:
        int: The minimal value of the described sum over all possible centers.
    """
    best = 2 ** 63  # Initialize best to a large number (simulate infinity)
    for ay in range(H):
        for ax in range(W):
            s = 0  # The current sum for center (ay, ax)
            for y in range(H):
                for x in range(W):
                    distance = min(abs(y - ay), abs(x - ax))  # Minimum distance as defined
                    s += A[y][x] * distance
            best = min(best, s)  # Update best if a smaller value is found
    return best

###############################################################################

# Debug mode is on if the 'DEBUG' environment variable exists
DEBUG = 'DEBUG' in os.environ

def inp():
    """
    Reads a single line of input from standard input, stripped of trailing whitespace.

    Returns:
        str: The input line without trailing newline/whitespace.
    """
    return sys.stdin.readline().rstrip()

def read_int():
    """
    Reads an integer from standard input.

    Returns:
        int: The parsed integer from the input.
    """
    return int(inp())

def read_ints():
    """
    Reads a line of integers from standard input.

    Returns:
        List[int]: A list of integers parsed from the input line.
    """
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    """
    Prints debugging output if DEBUG mode is enabled.

    Args:
        *value: Values to print (same as print()).
        sep (str): Separator between values.
        end (str): String appended after the last value.
    """
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()