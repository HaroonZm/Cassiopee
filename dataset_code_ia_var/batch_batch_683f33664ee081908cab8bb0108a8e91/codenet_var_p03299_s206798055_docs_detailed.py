from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce

# Augment maximum recursion depth to handle deep recursion in some problem settings
sys.setrecursionlimit(2147483647)

# Define an infinity constant for later use, common practice in competitive programming
INF = 10 ** 13

#---------------------
# Input utility functions
#---------------------
def LI():
    """
    Reads a line from standard input and returns it as a list of integers.
    
    Returns:
        list of int: List of integers from input.
    """
    return list(map(int, sys.stdin.readline().split()))

def I():
    """
    Reads a line from standard input and returns it as an integer.

    Returns:
        int: The integer value from input.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a line from buffered standard input, returns it as a list of strings
    (words, split by whitespace).

    Returns:
        list of str: List of words as strings.
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

def S():
    """
    Reads a line from buffered standard input and returns it as a string.

    Returns:
        str: String from input.
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

def IR(n):
    """
    Reads 'n' lines from standard input, returning a list of integers.

    Args:
        n (int): Number of lines to read.

    Returns:
        list of int: List of integer values from input.
    """
    return [I() for i in range(n)]

def LIR(n):
    """
    Reads 'n' lines from standard input, each containing multiple integers, and
    returns them as a list of integer lists.

    Args:
        n (int): Number of lines to read.

    Returns:
        list of list of int: 2D list of integers from input.
    """
    return [LI() for i in range(n)]

def SR(n):
    """
    Reads 'n' lines from input, each as a string.

    Args:
        n (int): Number of lines to read.

    Returns:
        list of str: List of input strings.
    """
    return [S() for i in range(n)]

def LSR(n):
    """
    Reads 'n' lines from input, each as a list of strings (split by whitespace).

    Args:
        n (int): Number of lines to read.

    Returns:
        list of list of str: 2D list of strings.
    """
    return [LS() for i in range(n)]

def SRL(n):
    """
    Reads 'n' lines from input, splitting each string into a list of its characters.

    Args:
        n (int): Number of lines to read.

    Returns:
        list of list of str: 2D list of characters.
    """
    return [list(S()) for i in range(n)]

def MSRL(n):
    """
    Reads 'n' lines from input, converting each character to an integer, and returns
    as a list of lists of integers (useful for matrices input).

    Args:
        n (int): Number of lines to read.

    Returns:
        list of list of int: 2D list of integers.
    """
    return [[int(j) for j in list(S())] for i in range(n)]

#---------------------
# Modulo constant (commonly used for problem constraints)
#---------------------
mod = 10 ** 9 + 7

#---------------------
# Main logic
#---------------------

# Read the integer n, which probably represents the length or size of the problem input
n = I()

# Read a list of n integers H, representing heights (or similar problem-specific values)
H = LI() + [1]  # Append 1 at the end to simplify boundary conditions

# Initialize the dp (dynamic programming) array of size n+1, all values set to 1
dp = [1] * (n + 1)

# Dynamic programming state updates
for k in range(n):
    # Initialize a new dp array for transitions, all values set to 0
    new_dp = [0] * (n + 1)
    for i in range(n + 1):
        # If the (i-th) height is strictly greater than H[k], special update
        if H[i] > H[k]:
            # Doubling the number of ways
            new_dp[i] = dp[k] * 2
        # If the previous height is less than or equal to the current one, update accordingly
        elif H[k - 1] <= H[i]:
            # Use dp[i], multiply by 2 and adjust by power of two depending on height difference
            new_dp[i] = dp[i] * 2 * pow(2, H[k] - H[i], mod)
        # If previous height is greater than current, add possible ways
        elif H[k - 1] > H[k]:
            new_dp[i] = dp[i] + dp[k]
        # For all other cases, use both dp[i] and dp[k-1], adjusting similarly with powers of two
        else:
            new_dp[i] = (dp[i] + dp[k - 1]) * pow(2, H[k] - H[k - 1], mod)
        # Apply modulo to avoid overflow
        new_dp[i] %= mod
    # Update dp array to new values for the next iteration
    dp = new_dp

# Output the result; typically, the answer is the last element in dp
print(dp[-1])