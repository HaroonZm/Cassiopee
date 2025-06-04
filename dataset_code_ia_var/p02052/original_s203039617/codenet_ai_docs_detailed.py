#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

# Utility functions for common input patterns, with detailed docstrings.

def LI():
    """
    Reads a single line from standard input, splits it by whitespace, and returns a list of integers.
    Returns:
        list[int]: The list of integers parsed from the input line.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Reads a single line from standard input and parses it as an integer.
    Returns:
        int: The integer parsed from the input line.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a single line from standard input, splits it by whitespace, and returns a list of character lists,
    where each element of the resulting list is a list of characters from a corresponding word.
    Returns:
        list[list[str]]: List of character lists from split words.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Reads a single line from standard input and returns it as a list of characters, without the trailing newline.
    Returns:
        list[str]: List of characters from the input line, minus the newline.
    """
    return list(sys.stdin.readline())[:-1]

def IR(n):
    """
    Reads n lines from standard input, each line parsed as an integer.
    Args:
        n (int): number of lines to read.
    Returns:
        list[int]: List of integers, one from each line.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Reads n lines from standard input, each line split into a list of integers.
    Args:
        n (int): number of lines to read.
    Returns:
        list[list[int]]: List of integer lists, one for each line.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Reads n lines from standard input, with each line as a list of characters (without the newline).
    Args:
        n (int): number of lines to read.
    Returns:
        list[list[str]]: List containing lists of characters for each input line.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Reads n lines from standard input, and for each line, creates a list of lists of characters from split words.
    Args:
        n (int): number of lines to read.
    Returns:
        list[list[list[str]]]: List containing for each line a list of character lists from split words.
    """
    return [LS() for _ in range(n)]

# Set recursion limit high enough for recursive algorithms
sys.setrecursionlimit(1000000)

# Constant for modulo operations, commonly used in competitive programming
mod = 1000000007

def A():
    """
    Solves the problem for part A:
    - Reads the height and width of a grid
    - Reads in the grid of characters (each cell: e.g., '.', 'B')
    - Calculates the largest Manhattan distance between any two 'B' cells
      (where the Manhattan distance between (x1, y1) and (x2, y2) is |x1-x2| + |y1-y2|).
    - Prints the result.
    """
    h, w = LI()            # Read height and width of the grid
    s = SR(h)              # Read h lines of the grid, each as a list of characters
    ans = 1                # Initialize answer (minimum distance)
    # Iterate through each position in the grid
    for y in range(h):
        for x in range(w):
            # If current cell is 'B'...
            if s[y][x] == "B":
                # Compare with every 'B' cell in the grid
                for y_ in range(h):
                    for x_ in range(w):
                        if s[y_][x_] == "B":
                            # Update ans with the maximum Manhattan distance found so far
                            ans = max(ans, abs(y - y_) + abs(x - x_))
    print(ans)
    return

def B():
    """
    Placeholder for Problem B.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def C():
    """
    Placeholder for Problem C.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def D():
    """
    Placeholder for Problem D.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def E():
    """
    Placeholder for Problem E.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def F():
    """
    Placeholder for Problem F.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def G():
    """
    Placeholder for Problem G.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def H():
    """
    Placeholder for Problem H.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def I_():
    """
    Placeholder for Problem I (named I_ to avoid redeclaration).
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

def J():
    """
    Placeholder for Problem J.
    Reads an integer n from standard input.
    """
    n = I()
    # Implement problem-specific logic here
    return

if __name__ == "__main__":
    # Run problem A by default when the script is executed directly.
    A()