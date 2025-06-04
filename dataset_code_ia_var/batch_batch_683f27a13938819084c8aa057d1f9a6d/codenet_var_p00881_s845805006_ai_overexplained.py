import math  # Module providing mathematical functions such as sqrt, sin, cos, etc.
import string  # Module with common string operations and constants like ascii_letters
import itertools  # Module providing functions that create iterators for efficient looping
import fractions  # Module for rational number arithmetic (working with fractions)
import heapq  # Module providing functions for implementing heaps based priority queues
import collections  # Module with high-performance container datatypes (like deque, Counter)
import re  # Module for regular expressions (string searching and manipulation)
import array  # Module to use space-efficient arrays (only same data-type elements)
import bisect  # Module to maintain lists in sorted order without having to sort the list
import sys  # Module that provides access to some variables and functions used or maintained by the interpreter
import random  # Module to generate pseudo-random numbers for various distributions
import time  # Module providing various time-related functions
import copy  # Module that provides functions for copying objects (shallow and deep copy)
import functools  # Module for higher-order functions (functions that act on or return other functions)

# The following line sets the maximum depth of the Python interpreter stack to a high value (10 million)
# This allows the program to run recursive functions without hitting the recursion limit as easily
sys.setrecursionlimit(10**7)

# Define a very large number to represent infinity (can be used as a default maximum value)
inf = 10**20

# Define a very small number (epsilon), commonly used in floating point comparisons for precision
eps = 1.0 / 10**13

# Define a large modulus value often used in competitive programming and modular arithmetic problems
mod = 10**9+7

# dd is a simple list of tuples indicating movement in the four cardinal directions (up, right, down, left)
# Each tuple represents a change in row (dx) and column (dy)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# ddn is a similar list representing 8 possible directions (including diagonals)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# The following functions are convenient aliases for standard input parsing (useful for competitive programming):

# Reads a line from standard input (user input), splits it based on whitespace, converts each split part to int, and returns as a list.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Same as LI() but decrements each integer by 1 (used for converting to 0-based indices)
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Reads a line from input, splits, converts each part to float, and returns as a list.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Reads a line from input and returns split strings as a list (no type conversion)
def LS():
    return sys.stdin.readline().split()

# Reads a line from input and converts it to an integer
def I():
    return int(sys.stdin.readline())

# Reads a line from input and converts it to a float
def F():
    return float(sys.stdin.readline())

# Reads a line from input and returns it as a string (using built-in input())
def S():
    return input()

# Prints a string (or any value), and flushes the output stream immediately to ensure it appears right away
def pf(s):
    return print(s, flush=True)

# The main() function is the entry point of this script's logic
def main():
    # Initialize an empty list to collect results for each test case
    rr = []

    # Define a function f taking two parameters: n and m
    # Presumably, n is the length of each binary string, m is the number of such strings
    def f(n, m):
        # Create a list a by reading m strings, converting each from base 2 to an integer using int(..., 2)
        a = [int(S(), 2) for _ in range(m)]

        # Initialize the minimum bit position to test (mi) to 0
        mi = 0
        # Find the maximum value in the list 'a' to determine how many bits are needed
        ma = max(a)
        # Find the bit-length required to represent the maximum element in 'a'
        # Increment mi until 2**mi is greater than ma, so mi is the smallest number where 2**mi > ma
        while 2**mi <= ma:
            mi += 1

        # Generate a list of powers of 2 from 2**0 up to 2**(mi), used as masks to test each bit position
        ii = [2**i for i in range(mi+1)]

        # Initialize an empty dictionary to memoize function calls to avoid recomputation (dynamic programming)
        fm = {}

        # Define a recursive helper function _f which takes a list of integers 'a' as parameter
        def _f(a):
            # Convert the list 'a' to a tuple 'k' to use it as a dictionary key (lists can't be dictionary keys but tuples can)
            k = tuple(a)
            # If the function result is already cached in 'fm', return it to avoid redundant computation
            if k in fm:
                return fm[k]
            
            # Base case: if 'a' contains fewer than 2 elements, no further splitting is possible
            if len(a) < 2:
                fm[k] = 0
                return 0

            # Initialize 'r' to infinity to keep track of the optimal (minimum) value found
            r = inf

            # Iterate over each bit position (represented by values in 'ii')
            for i in ii:
                # Split the list 'a' into two groups based on whether the current bit is set (1) or not (0)
                a1 = []
                a2 = []
                for c in a:
                    if i & c:  # If the current bit is set in c
                        a1.append(c)
                    else:
                        a2.append(c)
                # If all elements ended up in the same group (no split possible for this bit), skip this bit
                if not a1 or not a2:
                    continue
                # Recursively compute the value for both groups
                r1 = _f(a1)
                r2 = _f(a2)
                # The current result is the greater of the two sub-results plus one for the current split
                tr = max(r1, r2) + 1
                # If this split gives a better (smaller) result, store it
                if r > tr:
                    r = tr
            # Store the computed result in the memoization dictionary, and also return it
            fm[k] = r
            return r

        # Call the recursive function starting with the full list 'a'
        r = _f(a)
        # Return the computed result for this test case
        return r

    # Loop to read and process test cases until the input specifies termination (n == 0)
    while 1:
        # Read two integers 'n' and 'm' from input using LI()
        n, m = LI()
        # If n is 0, break out of the loop (no more test cases)
        if n == 0:
            break
        # Call function f with parameters n and m and append its result to the results list 'rr'
        rr.append(f(n, m))

    # Join all elements in 'rr' as strings separated by newline characters and return as the program output
    return '\n'.join(map(str, rr))

# Call the main function and print its result to standard output
print(main())