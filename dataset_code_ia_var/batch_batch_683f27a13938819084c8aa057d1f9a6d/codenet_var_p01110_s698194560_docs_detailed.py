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
    Main function to read inputs, process each test case, and produce outputs.

    The function reads the initial parameters for the paper folding problem
    repeatedly until a line '0 0 0 0' is encountered, which terminates the input.

    For each test case, it:
    - Reads the number of rows N, columns M, number of folds T, and number of queries P.
    - Reads T folds with directions and positions.
    - Reads P coordinates to query number of paper layers.
    - For each test case, computes and outputs the number of layers at queried positions.
    """
    while True:
        N, M, T, P = read_ints()
        # Check termination condition
        if (N, M, T, P) == (0, 0, 0, 0):
            break
        # Read folding operations
        F = [read_ints() for _ in range(T)]
        # Read positions to query
        H = [read_ints() for _ in range(P)]
        # Process the test case and output result
        print(*solve(N, M, T, P, F, H), sep='\n')

def solve(N, M, T, P, F, H):
    """
    Simulates the paper folding and evaluates the number of layers at specific positions.

    Args:
        N (int): Number of rows (height) of the paper.
        M (int): Number of columns (width) of the paper.
        T (int): Number of fold instructions.
        P (int): Number of queries.
        F (List[List[int]]): List of fold operations [direction, position].
                             direction = 1 for vertical fold, 2 for horizontal fold.
                             position = fold line index (starts at 1).
        H (List[List[int]]): List of positions to query, each as [x, y]
                             (x: column index, y: row index).

    Returns:
        List[int]: Number of layers at each query position after all folds.
    """
    # Initialize paper matrix: each cell starts with 1 layer.
    width = N
    height = M
    paper = [[1] * width for _ in range(height)]

    for direction, c in F:
        # When direction == 1, vertical fold; fold along the vertical line at column c
        if direction == 1:
            # The new width is the larger of c or width-c columns after folding
            new_width = max(c, width - c)
            # Initialize a new blank paper with new_width columns
            npaper = [[0] * new_width for _ in range(height)]
            for y in range(height):
                # Fold left part from [0...c-1], mirror onto [0...(c-1)]
                for dx in range(c):
                    npaper[y][c - 1 - dx] += paper[y][dx]
                # Copy right part from [c...width-1], shift to fit
                for dx in range(c, width):
                    npaper[y][dx - c] += paper[y][dx]
            width = new_width
            paper = npaper
            continue

        # Horizontal fold (direction == 2): fold along the horizontal line at row c.
        # After the fold, the new height will be larger of c or height-c.
        new_height = max(c, height - c)
        npaper = [[0] * width for _ in range(new_height)]
        for x in range(width):
            # Fold upper part from [0...c-1], mirror onto [0...(c-1)]
            for dy in range(c):
                npaper[c - 1 - dy][x] += paper[dy][x]
            # Copy lower part from [c...height-1], shift to fit
            for dy in range(c, height):
                npaper[dy - c][x] += paper[dy][x]
        height = new_height
        paper = npaper

    # For each query, return the number of layers at specified (x, y)
    return [paper[y][x] for x, y in H]

###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ

def inp():
    """
    Reads a single line from standard input and removes trailing newline/whitespace.

    Returns:
        str: The input line stripped of trailing whitespace.
    """
    return sys.stdin.readline().rstrip()

def read_int():
    """
    Reads a line from input and converts it to an integer.

    Returns:
        int: The integer read from input.
    """
    return int(inp())

def read_ints():
    """
    Reads a line from input and converts it into a list of integers.

    Returns:
        List[int]: List of integers read from input line.
    """
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    """
    Debug print function; only prints if the DEBUG flag is set in OS environment.

    Args:
        *value: Values to be printed.
        sep (str): Separator between values.
        end (str): String appended after the last value.
    """
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()