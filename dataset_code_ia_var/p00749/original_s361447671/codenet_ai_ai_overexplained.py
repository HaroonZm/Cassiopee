import math  # Import module for mathematical functions and constants
import string  # Import module for string operations
import itertools  # Import module for working with iterators
import fractions  # Import module for rational number arithmetic
import heapq  # Import module for heap queue algorithms (priority queue)
import collections  # Import module for specialized container datatypes
import re  # Import module for regular expressions (string matching)
import array  # Import module for efficient arrays of numeric values
import bisect  # Import module for list bisection algorithms
import sys  # Import module that provides access to variables used or maintained by the interpreter
import random  # Import module for generating random numbers
import time  # Import module for time access and conversions
import copy  # Import module for object copying operations
import functools  # Import module for higher-order functions and operations on callable objects

# Set the maximum depth of the Python interpreter stack to a very large value to prevent recursion limit issues
sys.setrecursionlimit(10**7)

# Define a variable representing a very large number (used as infinity)
inf = 10**20

# Define a small number as "epsilon" for floating point comparisons to avoid precision issues
eps = 1.0 / 10**13

# Define a large prime number, often used as a modulus for hash or modular arithmetic
mod = 10**9+7

# Define a list of 2D direction vectors for movement in 4 directions (up, right, down, left)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Define a list of 2D direction vectors for movement in 8 directions (including diagonals)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Define function to read a line from the standard input and convert it into a list of integers
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Define function to read a line from standard input, convert to integers, and decrement each by 1
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Define function to read a line from standard input and convert it into a list of floats
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Define function to read a line from standard input and split it into a list of strings
def LS():
    return sys.stdin.readline().split()

# Define function to read a single integer from standard input
def I():
    return int(sys.stdin.readline())

# Define function to read a single floating-point number from standard input
def F():
    return float(sys.stdin.readline())

# Define function to read a line from input (alias for input())
def S():
    return input()

# Define function to print a value to standard output and immediately flush the output buffer
def pf(s):
    return print(s, flush=True)

# Adjust epsilon value for later (used for binary search tolerance)
eps = 1e-4

# Define function to perform a binary search on floating point numbers between mi and ma, using predicate function f
def bsa(f, mi, ma):
    mm = -1  # Initialize the variable to store the current midpoint (set to an invalid value initially)
    while ma > mi + eps:  # Loop until the search interval is smaller than epsilon
        mm = (ma + mi) / 2.0  # Compute the midpoint between mi and ma
        if f(mm):  # If the predicate function returns True for the midpoint
            mi = mm + eps  # Move the lower bound up, just past mm by eps
        else:
            ma = mm  # Otherwise, move the upper bound down to mm
    if f(mm):  # After loop, check if the endpoint still satisfies f
        return mm + eps  # Return value just past mm if true
    return mm  # Otherwise, return mm

# Define the main function for the program's core logic
def main():
    rr = []  # Initialize an empty list to store the results for each test case

    # Define a helper function 'f' taking width (w) and height (h) as parameters
    def f(w, h):
        """
        a: 2D list representation of the input grid, padded with an extra row and column of '.' characters (dots) on all sides.
        sf: 2D list to keep track of visited cells and their region/blobs indices (None for unvisited/empty), has dimensions (h+2) x (w+2).
        bs: List of lists, where each inner list contains coordinates belonging to a particular region/blob.
        bi: Counter for the number of distinct regions in the grid (incremented each time a new region is found).
        """
        # Build the grid with a border of '.' on all sides for ease of bounds checking.
        a = [['.'] * (w + 2)] + \
            [['.'] + [c for c in S()] + ['.'] for _ in range(h)] + \
            [['.'] * (w + 2)]
        # Create an empty grid to track region ids (None means unvisited, otherwise stores region number)
        sf = [[None] * (w + 2) for _ in range(h + 1)] + [[0] * (w + 2)]
        # List of blobs (regions), where each blob is represented as a list of (i,j) tuples
        bs = []
        # Counter for region indices, starting from 0, increments for each new detected region
        bi = 0
        # Loop through all positions except for the padded border (1 to h, 1 to w)
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                # If the cell is already assigned to a region or it is empty, skip
                if sf[i][j] or a[i][j] == '.':
                    continue
                # Found a new blob/region, increment the region index
                bi += 1
                c = a[i][j]  # The character for the current region blob ('#' or similar)
                q = []  # Queue for BFS region expansion
                q.append((i, j))  # Start with the initial cell
                sf[i][j] = bi  # Mark as visited with region index
                qt = 0  # Queue pointer for BFS iteration
                # Begin BFS for the connected component (flood fill)
                while len(q) > qt:
                    qi, qj = q[qt]  # Get current cell from the queue
                    qt += 1  # Move to next in queue
                    # Explore four cardinal directions
                    for di, dj in dd:
                        ni = qi + di  # Neighbor row coordinate
                        nj = qj + dj  # Neighbor column coordinate
                        # If already assigned to a region or not the same character, skip
                        if sf[ni][nj] or a[ni][nj] != c:
                            continue
                        sf[ni][nj] = bi  # Mark neighbor as part of current region
                        q.append((ni, nj))  # Add neighbor cell to the queue
                bs.append(q)  # After BFS, add the list of this region's coordinates to 'bs'

        # The following commented-out block would print the region map (for debugging)
        # print('\n'.join(' '.join(map(lambda x: '.' if x is None else str(x), _)) for _ in sf))

        # Define recursive function that, for given region id 'i', performs computation related to stability
        def _f(i):
            l = inf  # Variable for storing leftmost boundary (initialize to infinity)
            r = -inf  # Variable for storing rightmost boundary (initialize to negative infinity)
            bt = set()  # Set to store region indices below the current region (bottom neighbors)
            tt = set()  # Set to store region indices above the current region (top neighbors)
            bi = bs[i - 1]  # List of positions (row, col) for the i-th blob (i-1 because 0-based indexing in Python)
            wd = collections.defaultdict(int)  # Dictionary counting occurrences based on column (j) indices
            # Examine all cells in the current region
            for si, sj in bi:
                wd[sj] += 1  # Count occurrences (to be used for balance calc)
                # Check the region id directly below (downwards neighbor)
                c = sf[si + 1][sj]
                # If neighbor exists and is not the same region, add to bottom list
                if not c is None and c != i:
                    bt.add(c)
                    # Update left and rightmost columns
                    if l > sj:
                        l = sj
                    if r < sj:
                        r = sj
                # Check the region id directly above (upwards neighbor) for possible stacking
                c = sf[si - 1][sj]
                if not c is None and c != i:
                    tt.add(c)  # Add region above to the top list
            # If there is not exactly one region below, this region is unstable or unsupported
            if len(bt) != 1:
                return
            # Recursively process all regions above this one
            for ti in tt:
                td = _f(ti)  # Recursive call for the top region
                if td is None:  # If any recursion returns None, propagate instability
                    return
                # Merge the count dictionaries together
                for k in td.keys():
                    wd[k] += td[k]
            # Define function for balance calculation – used by binary search bsa
            def __f(j):
                w = 0  # Initialize net torque/balance sum
                for k in wd.keys():
                    w += (k - j) * wd[k]  # For each column, add weighted delta (centered on j)
                # print('jw', j, w)
                return w > 0  # Returns True if net balance is toward the right (positive)

            w = bsa(__f, 0, 11) + 0.5  # Find the balance point using binary search, adjust by 0.5 as per method
            # print('lr', l, r)
            # print(i, wd)
            # print(i, w)
            # If the computed center of gravity (w) falls outside region's left/right boundaries, it's unstable
            if w < l + eps*10 or w > r + 1 - eps*10:
                return
            return wd  # If all checks pass, return updated dictionary including merged above-regions

        bti = -1  # Initialize variable to hold the region just above the bottom (supporting region)
        # Search for any cell in the second-from-the-bottom row (just above the padding) that is not empty
        for j in range(1, w + 1):
            if sf[-2][j]:
                bti = sf[-2][j]
        # print('bti', bti)
        # Begin recursive stability check from supporting region at bottom
        r = _f(bti)
        if r is None:
            return 'UNSTABLE'  # If any check failed, report 'UNSTABLE'
        return 'STABLE'  # Otherwise, the structure is 'STABLE'

    # Continuously read input grids until an end marker (0 0) is encountered
    while 1:
        n, m = LI()  # Read two integers: n (width), m (height) for the next grid, per test case
        if n == 0 and m == 0:  # Termination condition (input end)
            break
        rr.append(f(n, m))  # Compute result for current test case and store
        # print('rr', rr[-1])

    # After all test cases are processed, join the results into lines and return as a single string
    return '\n'.join(map(str, rr))

# Call the main function, print its return value to standard output
print(main())