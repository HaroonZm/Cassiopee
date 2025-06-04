import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

# Increase the recursion limit to allow for deep recursion,
# which is sometimes necessary for large problem inputs or deep recursive calls.
sys.setrecursionlimit(10**7)

# Define some common constants
inf = 10**20                          # A very large value to denote infinity in algorithms
eps = 1.0 / 10**13                    # A small epsilon value for float comparison
mod = 10**9 + 7                       # A common modulus, often used in modular arithmetic problems

# Directions for grid-based navigation (4 cardinal directions)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Directions for grid-based navigation (8 directions, including diagonals)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


# ========================
# Input utility functions
# ========================

def LI():
    """
    Read a line from standard input and parse it into a list of integers.

    Returns:
        list of int: The next line from input, split into integers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Read a line from standard input and parse it into a list of integers (0-based).

    Returns:
        list of int: The next line from input, split into integers, and subtracts one from each (for 0-based indexing).
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Read a line from standard input and parse it into a list of floats.

    Returns:
        list of float: The next input line, split into floats.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Read a line from standard input and parse it into a list of strings.

    Returns:
        list of str: The next input line, split by whitespace.
    """
    return sys.stdin.readline().split()

def I():
    """
    Read a single integer from standard input.

    Returns:
        int: The next input line converted to an integer.
    """
    return int(sys.stdin.readline())

def F():
    """
    Read a single float from standard input.

    Returns:
        float: The next input line converted to a float.
    """
    return float(sys.stdin.readline())

def S():
    """
    Read an entire line from standard input and return as a string.

    Returns:
        str: The next line from input, including any whitespace or newline.
    """
    return input()

def pf(s):
    """
    Print a string to standard output and flush immediately.

    Args:
        s (str): The string to print.
    """
    return print(s, flush=True)

# ========================
# Union-Find (Disjoint-Set) Data Structure
# ========================
class UnionFind:
    """
    Union-Find (Disjoint-Set) data structure with path compression and union by size.

    Attributes:
        table (list of int): Each element points to its parent, negative stands for a root and magnitude is the set size.
    """
    def __init__(self, size):
        """
        Initialize UnionFind structure.

        Args:
            size (int): Number of elements in the disjoint set.
        """
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        """
        Find the root of the set containing element x, with path compression.

        Args:
            x (int): The element whose set representative is to be found.

        Returns:
            int: The representative (root) of the set containing x.
        """
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        """
        Unite the sets that contain x and y.

        Args:
            x (int): First element to union.
            y (int): Second element to union.

        Returns:
            bool: True if a union was performed, False if x and y were already in the same set.
        """
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            # Union by size: attach smaller tree to larger tree.
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def subsetall(self):
        """
        Get all current roots and the size of the corresponding sets.

        Returns:
            list of tuple: Each tuple contains (representative index, size of the set).
        """
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

# ========================
# Main algorithm logic
# ========================
def main():
    """
    Main function to process the problem data and compute the required output.

    Returns:
        str: The computed result for each test case, joined as a single string.
    """
    rr = []  # This list will store answers for all test cases

    def f(n, m):
        """
        Process one test case with n nodes and m edges, using UnionFind to compute MST-like properties.

        Args:
            n (int): Number of nodes in the graph.
            m (int): Number of edges in the graph.

        Returns:
            str: Result in the format "rc r" where rc is the count, r is the sum.
        """
        # Read all edges. Each edge: (node1, node2, cost), and append its index.
        ee = [LI() + [_] for _ in range(m)]
        # Sort edges by weight, then by index.
        e = sorted(ee, key=lambda x: [x[2], x[3]])

        s = []        # List to store indices of edges chosen for MST
        ns = []       # List to store edges not part of the MST
        uf = UnionFind(n+1)  # Union-Find for MST construction (1-based index)
        t = 0         # Total cost so far (not used here)
        ttc = 0       # Number of edges in MST so far (not used here)

        # Kruskal's Algorithm to construct MST
        for a, b, c, i in e:
            if uf.union(a, b):
                s.append(i)
                t += c
                ttc += 1
            else:
                ns.append((a, b, c))

        r = 0        # Accumulate sum for result
        rc = 0       # Count the number of edges satisfying some property

        # For each edge in the MST...
        for si in s:
            tr = 0   # temp sum for this iteration (not used here)
            tc = 0   # temp count for this iteration (not used here)
            uf = UnionFind(n+1)
            w = ee[si][2]  # Weight of the current MST edge

            # Rebuild MST without edge si
            for sj in s:
                if si == sj:
                    continue
                uf.union(ee[sj][0], ee[sj][1])

            sf = True  # Flag to check if edge si is not easily replaced
            # Try to replace si with a non-MST edge of same weight
            for a, b, c in ns:
                if c == w and uf.union(a, b):
                    sf = False
                    break
            if sf:
                rc += 1
                r += w

        return '{} {}'.format(rc, r)

    # Read and process input until end (n == 0)
    while 1:
        n, m = LI()
        if n == 0:
            break
        rr.append(f(n, m))
        break

    return '\n'.join(map(str, rr))

# Run the main function and output its result
print(main())