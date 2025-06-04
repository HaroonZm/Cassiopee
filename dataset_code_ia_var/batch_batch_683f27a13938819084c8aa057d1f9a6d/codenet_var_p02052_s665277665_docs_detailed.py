import sys
from operator import itemgetter
from fractions import gcd  # Greatest common divisor
from math import ceil, floor  # Rounding operations
from copy import deepcopy  # Deep copy for lists
from itertools import accumulate  # Cumulative sums
from collections import Counter  # Frequency counting
import math
from functools import reduce

# Increase recursion limit to avoid RecursionError for deep recursions
sys.setrecursionlimit(200000)

#-----------------------------------------------------------------------------
# Input utility function definitions
#-----------------------------------------------------------------------------

def ii():
    """
    Reads a single integer from standard input.

    Returns:
        int: The integer read from the input.
    """
    return int(sys.stdin.readline())

def mi():
    """
    Reads a line of input and returns a map of integers.

    Returns:
        tuple: A tuple of integers read from the line.
    """
    return map(int, sys.stdin.readline().rstrip().split())

def lmi():
    """
    Reads a line of input and returns a list of integers.

    Returns:
        list: A list of integers read from the input line.
    """
    return list(map(int, sys.stdin.readline().rstrip().split()))

def li():
    """
    Reads a line of input and returns a list of its characters.

    Returns:
        list: A list where each element is a character from the input line.
    """
    return list(sys.stdin.readline().rstrip())

def debug(*args, sep=" ", end="\n"):
    """
    Prints debug information to standard error if running in optimized mode.

    Args:
        *args: Variable length argument list to print.
        sep (str, optional): String inserted between values. Default is a space.
        end (str, optional): String appended after the last value. Default is newline.

    Note:
        No output occurs if __debug__ is True (the default).
    """
    if not __debug__:
        print("debug:", *args, file=sys.stderr, sep=sep, end=end)

#-----------------------------------------------------------------------------
# Main logic
#-----------------------------------------------------------------------------

# Read the grid dimensions H (height) and W (width)
H, W = mi()

# Read the grid as a list of H rows, where each row is a list of characters
S = [li() for i in range(H)]

# List to store the positions (i, j) of all cells containing 'B'
ans = []

# Iterate over all cells and collect all positions where 'B' is found
for i in range(H):
    for j in range(W):
        if S[i][j] == "B":
            ans.append((i, j))

# First, sort by the sum of the coordinates (i + j)
ans.sort(key=lambda x: x[0] + x[1])
debug(ans[-1])  # Debug: print the position with the maximum (i + j)
debug(ans[0])   # Debug: print the position with the minimum (i + j)

# Calculate the Manhattan distance between the two extreme points with respect to (i + j)
tmp = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])

# Second, sort by (i + (W - j)) which is another diagonal direction
ans.sort(key=lambda x: x[0] + (W - x[1]))
debug(ans[-1])  # Debug: print the position with the maximum (i + (W - j))
debug(ans[0])   # Debug: print the position with the minimum (i + (W - j))

# Calculate the Manhattan distance between the two extreme points with respect to (i + (W - j))
tmp2 = abs(ans[-1][0] - ans[0][0]) + abs(ans[-1][1] - ans[0][1])

# Output the maximum of the two computed distances
print(max(tmp, tmp2))