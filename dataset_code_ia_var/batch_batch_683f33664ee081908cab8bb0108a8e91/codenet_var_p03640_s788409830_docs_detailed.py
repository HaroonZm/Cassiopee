import sys
import re
import os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd

def input():
    """
    Reads a single line from standard input and strips any trailing whitespace.
    Returns:
        str: The input line with no trailing newline or spaces.
    """
    return sys.stdin.readline().strip()

def INT():
    """
    Reads a line from input and converts it to an integer.
    Returns:
        int: The integer value from the input line.
    """
    return int(input())

def MAP():
    """
    Reads a line from input and maps each space-separated value to an integer.
    Returns:
        map: An iterator of integers from the input line.
    """
    return map(int, input().split())

def S_MAP():
    """
    Reads a line from input and maps each space-separated value to a string.
    Returns:
        map: An iterator of strings from the input line.
    """
    return map(str, input().split())

def LIST():
    """
    Reads a line from input, splits by spaces, and returns a list of integers.
    Returns:
        list: A list of integers from the input line.
    """
    return list(map(int, input().split()))

def S_LIST():
    """
    Reads a line from input, splits by spaces, and returns a list of strings.
    Returns:
        list: A list of strings from the input line.
    """
    return list(map(str, input().split()))

# Set a very high recursion limit which may be necessary for deep recursion
sys.setrecursionlimit(10 ** 9)

# Constants for infinity and modulo (commonly used in competitive programming)
INF = float('inf')
mod = 10 ** 9 + 7

def fill_grid(H, W, A):
    """
    Fills an HxW grid with color numbers (1-based), in a snake-like serpentine pattern.
    Each color k appears A[k-1] times in total. Even rows are filled left to right, odd rows right to left.
    
    Args:
        H (int): Number of rows in the grid.
        W (int): Number of columns in the grid.
        A (list of int): List specifying the amount of times to use each color (1-based).
    
    Returns:
        list: A 2-dimensional list representing the filled grid.
    """
    # Initialize the grid with zeros
    grid = [[0] * W for _ in range(H)]
    # k: current index in A (color number is k+1)
    k = 0
    # Traverse each row
    for h in range(H):
        # Even-indexed rows are filled left to right
        if h % 2 == 0:
            rng = range(W)
        # Odd-indexed rows are filled right to left
        else:
            rng = range(W - 1, -1, -1)
        # Fill the row
        for w in rng:
            # Assign current color (k+1)
            grid[h][w] = k + 1
            # Decrease remaining quota for this color
            A[k] -= 1
            # If color quota depleted, move to next color
            if A[k] == 0:
                k += 1
    return grid

def main():
    """
    Main execution function that reads inputs, fills the grid as per the rules, and prints the result.
    """
    # Read grid dimensions
    H, W = MAP()
    # Number of different colors
    N = INT()
    # List containing the number of times each color should be placed
    A = LIST()
    # Fill the grid using the specific pattern
    filled_grid = fill_grid(H, W, A)
    # Output the grid row by row
    for row in filled_grid:
        print(*row, end="\n")

if __name__ == "__main__":
    main()