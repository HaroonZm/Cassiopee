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

# Increase the recursion limit to handle large recursions in DFS/BFS if needed
sys.setrecursionlimit(10 ** 7)

# Global constants
inf = 10 ** 20  # A very large value representing infinity
eps = 1.0 / 10 ** 10  # Small epsilon for floating point comparisons
mod = 10 ** 9 + 7  # A large prime for modulo operations (not used here)
# Direction vectors for grid movements: up, right, down, left
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# All 8 neighbors (including diagonals)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    """
    Reads a line from standard input and returns a list of integers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Reads a line from standard input and returns a list of integers minus 1 (zero-indexed).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Reads a line from standard input and returns a list of floats.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Reads a line from standard input and returns a list of strings.
    """
    return sys.stdin.readline().split()

def I():
    """
    Reads a line from standard input and returns an integer.
    """
    return int(sys.stdin.readline())

def F():
    """
    Reads a line from standard input and returns a float.
    """
    return float(sys.stdin.readline())

def S():
    """
    Reads a line from standard input and returns a string.
    """
    return input()

def pf(s):
    """
    Prints a string and flushes the standard output.
    
    Args:
        s: The string to print.
    """
    return print(s, flush=True)

def bs(f, mi, ma):
    """
    Generic binary search.
    Finds the smallest integer x in [mi, ma) where f(x) == False,
    assuming f is monotonic.
    
    Args:
        f: Monotonic function from int -> bool.
        mi: The minimum integer to consider (inclusive).
        ma: The maximum integer to consider (exclusive).
    Returns:
        The boundary integer.
    """
    mm = -1
    while ma > mi:
        mm = (ma + mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    """
    Main function to solve the maze problem as per the input specification.
    Processes multiple cases from standard input and prints answers for each.
    
    Returns:
        str: Output lines joined by newlines.
    """
    rr = []  # Stores results for each case

    def f(n, m):
        """
        Processes a single case for an n x m maze.
        
        Args:
            n (int): Number of rows in the maze.
            m (int): Number of columns in the maze.
        
        Returns:
            int: The answer for this case (maximum minimum detour length or -1).
        """
        # Read the input for the maze: walls and possible connections
        # Input has n*2-1 rows, alternating between cell and wall info
        a = [LI() for _ in range(n * 2 - 1)]

        # e represents the connectivity graph (adjacency list)
        e = collections.defaultdict(set)
        # ds will collect sets of cell pairs that are directly connected (no wall between them)
        ds = []

        # Parse maze connectivity from input
        for i in range(n):
            for j in range(m):
                # Vertical connections (i < n-1): check wall below
                if i < n - 1 and a[i * 2 + 1][j] == 0:
                    # Connect (i, j) to (i+1, j) and vice versa
                    e[(i, j)].add((i + 1, j))
                    e[(i + 1, j)].add((i, j))
                    ds.append(set([(i, j), (i + 1, j)]))
                # Horizontal connections (j < m-1): check wall to right
                if j < m - 1 and a[i * 2][j] == 0:
                    # Connect (i, j) to (i, j+1) and vice versa
                    e[(i, j)].add((i, j + 1))
                    e[(i, j + 1)].add((i, j))
                    ds.append(set([(i, j), (i, j + 1)]))

        def search(s, ns):
            """
            Performs Dijkstra's algorithm from node s, skipping edges in ns.
            Used to compute minimum distances from s with a specific edge "blocked".
            
            Args:
                s (tuple): Starting coordinate (row, col).
                ns (set): Set of nodes representing the blocked edge.
            Returns:
                dict: Minimum distances from s to all nodes (default is inf).
            """
            d = collections.defaultdict(lambda: inf)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while q:
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                for uv in e[u]:
                    # Don't revisit visited nodes or use the blocked edge
                    if v[uv]:
                        continue
                    if uv in ns and u in ns:
                        continue
                    vd = k + 1
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))

            return d

        nd = collections.defaultdict(lambda: -1)
        # For every directly connected pair (no wall between), 
        # consider as if the edge is "gone": What's the max detour created?
        for ns in ds:
            td = search((n - 1, m - 1), ns)
            for k in ns:
                if nd[k] < td[k]:
                    nd[k] = td[k]

        def ff(mx):
            """
            Predicate for binary search: checks if there exists a path from (0,0) to (n-1,m-1)
            such that the length at all points plus their associated maximum detour is less than mx.
            
            Args:
                mx (int): Minimum cycle detour length to check.
            Returns:
                bool: True if possible, False otherwise.
            """
            def search2(s):
                """
                Dijkstra's algorithm from starting cell s, 
                skipping all states with total cost >= mx (considering extra detours).
                
                Args:
                    s (tuple): Starting coordinate.
                Returns:
                    dict: Minimum distances to all points from s.
                """
                d = collections.defaultdict(lambda: inf)
                d[s] = 0
                q = []
                heapq.heappush(q, (0, s))
                v = collections.defaultdict(bool)
                while q:
                    k, u = heapq.heappop(q)
                    if v[u]:
                        continue
                    v[u] = True

                    for uv in e[u]:
                        if v[uv]:
                            continue
                        vd = k + 1
                        if vd + nd[uv] >= mx:
                            continue
                        if d[uv] > vd:
                            d[uv] = vd
                            heapq.heappush(q, (vd, uv))

                return d

            fd = search2((0, 0))
            # If the distance to goal is at least mx, return True (not possible to do better)
            return fd[(n - 1, m - 1)] >= mx

        mm = n * m * 3  # Upper bound for number of steps (a sufficiently large number)
        r = bs(ff, 0, mm)  # Binary search the answer

        if r >= mm:
            return -1  # Not possible, so return -1

        return r - 1  # Return the maximum minimal detour length

    # Main loop: read and process multiple test cases
    while True:
        n, m = LI()
        if n == 0:  # End of input condition
            break
        rr.append(f(n, m))

    return '\n'.join(map(str, rr))

if __name__ == "__main__":
    print(main())