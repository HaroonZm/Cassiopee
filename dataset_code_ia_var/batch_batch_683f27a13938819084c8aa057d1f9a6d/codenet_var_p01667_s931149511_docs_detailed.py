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

# Augment the recursion depth limit to allow deep recursions
sys.setrecursionlimit(10**7)

# Define commonly used constants
inf = 10**20  # Represents infinity for practical purposes
eps = 1.0 / 10**10  # Epsilon for floating-point comparison
mod = 10**9+7  # Modulo value often used in competitive programming
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # 4-directional (up, right, down, left) movement offsets
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]  # 8-directional movement (including diagonals)

def LI():
    """
    Reads a line from standard input and returns a list of integers.

    Returns:
        list: List of integers read from input.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Reads a line from standard input and returns a list of integers decremented by 1.

    Returns:
        list: List of integers (each minus one) read from input.
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Reads a line from standard input and returns a list of floats.

    Returns:
        list: List of floats read from input.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Reads a line from standard input and returns it as a list of string tokens.

    Returns:
        list: List of strings (tokens) read from input.
    """
    return sys.stdin.readline().split()

def I():
    """
    Reads a line from standard input and returns it as an integer.

    Returns:
        int: Integer read from input.
    """
    return int(sys.stdin.readline())

def F():
    """
    Reads a line from standard input and returns it as a float.

    Returns:
        float: Float read from input.
    """
    return float(sys.stdin.readline())

def S():
    """
    Reads a line from standard input (removes trailing newlines).

    Returns:
        str: String read from input.
    """
    return input()

def pf(s):
    """
    Prints the provided argument and flushes the standard output.

    Args:
        s (any): The object to print.
    """
    print(s, flush=True)

def main():
    """
    Main function to solve the logic problem using constraint propagation and cycle detection.
    The function reads a set of constraints for several entities (indexed 0 to m-1) and constructs
    an implication graph based on variable inequalities. It uses DFS to detect cycles in this graph.

    Returns:
        str: 'Yes' if no contradiction/cycle is found, 'No' otherwise.
    """
    # Read two integers: m (number of entities), n (unused variable count)
    m, n = LI()

    # dp and dm store constraints:
    # dp: stores '<' constraints; dm: stores '<=' constraints
    dp = collections.defaultdict(list)  # variable -> list of (threshold, entity) for '>'
    dm = collections.defaultdict(list)  # variable -> list of (threshold, entity) for '<='

    # Reading all constraints for each entity
    for i in range(m):
        k = I()  # number of constraints for entity i
        for _ in range(k):
            s, c, t = LS()
            # Store the constraint based on its type
            if c == '<=':
                # 'variable <= threshold': store as (threshold, entity)
                dm[int(s)].append((int(t), i))
            else:
                # 'variable > threshold': store as (threshold, entity)
                dp[int(s)].append((int(t), i))

    # Build implication graph: e[i] contains nodes j such that i (entity) must come before j
    e = collections.defaultdict(set)

    # For each variable, find all (entity, threshold) pairs for '<=' and '>' constraints
    for var in list(dm.keys()):
        ml = dm[var]  # '<=' constraints for variable var
        pl = dp[var]  # '>' constraints for variable var
        for tm, i in ml:  # for each '<=' constraint
            for tp, j in pl:  # for each '>' constraint
                # If thresholds cause a contradiction order, add an edge in implication graph
                if tm < tp:
                    e[i].add(j)

    # v stores visit state of nodes during DFS: 0 = not visited, 1 = visiting, 2 = fully visited
    v = collections.defaultdict(int)

    def f(i):
        """
        Perform DFS on the implication graph starting from node i to detect cycles.
        
        Args:
            i (int): The starting entity index.

        Returns:
            bool: True if no cycle detected starting from i, False otherwise.
        """
        if v[i] == 2:
            # Node i already processed with no cycle
            return True
        if v[i] == 1:
            # Cycle detected (back edge to currently visiting node)
            return False
        v[i] = 1  # Mark as currently visiting
        for n in e[i]:
            if not f(n):
                return False  # If any descendant has a cycle, propagate False
        v[i] = 2  # Mark as fully processed
        return True

    # Run cycle detection for each entity to ensure all components are checked
    for i in range(m):
        if not f(i):
            return 'No'  # Contradiction found (cycle exists)

    return 'Yes'  # No contradictions detected

# Execute main and print the result
print(main())