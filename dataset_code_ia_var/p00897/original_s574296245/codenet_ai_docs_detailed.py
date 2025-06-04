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

# Augment the recursion limit to support deep recursions if needed.
sys.setrecursionlimit(10**7)

# Define common constants used throughout the code
inf = 10**20                # A representation of infinity (very large number)
eps = 1.0 / 10**13          # Epsilon for floating-point comparisons
mod = 10**9 + 7             # A common modulus value for problems involving modular arithmetic

# Directions for grid or graph traversal (4 directions and 8 directions)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    """
    Reads a line from standard input, splits it into space-separated tokens, and converts each token to an int.

    Returns:
        List[int]: A list of integers read from the line.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Reads a line from standard input, splits it into space-separated tokens, converts each token to an int, and subtracts 1 from each.

    Returns:
        List[int]: A list of integers (0-based) read from the line.
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Reads a line from standard input, splits it into space-separated tokens, and converts each token to a float.

    Returns:
        List[float]: A list of floats read from the line.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Reads a line from standard input and splits it into a list of strings (tokens).

    Returns:
        List[str]: A list of input tokens as strings.
    """
    return sys.stdin.readline().split()

def I():
    """
    Reads a single integer value from standard input.

    Returns:
        int: The integer read from the line.
    """
    return int(sys.stdin.readline())

def F():
    """
    Reads a single float value from standard input.

    Returns:
        float: The floating-point value read from the line.
    """
    return float(sys.stdin.readline())

def S():
    """
    Reads a single line from standard input as a string (trailing newline removed).

    Returns:
        str: The input line as a string.
    """
    return input()

def pf(s):
    """
    Prints a string immediately (flushing output), for use in interactive problems.

    Args:
        s (Any): The data to print.
    """
    print(s, flush=True)

def main():
    """
    Main function to process input cases and compute answers.

    Returns:
        str: The answers for each test case, joined by newline characters.
    """
    rr = []  # List to store results for each test case

    def f(n, m, cap):
        """
        Solves a single test case: computes the minimum "cost" to travel from point s to point t, given graph structure,
        recharge stations, and fuel tank capacity, modified as per problem constraints.

        Args:
            n (int): Number of roads (edges) in the graph.
            m (int): Number of recharge stations.
            cap (int): Fuel tank capacity.

        Returns:
            int: The minimum cost to reach the destination, or -1 if not reachable.
        """
        # Multiply the initial fuel capacity by 10 (according to the problem's specifics)
        cap *= 10

        # Read starting and target node IDs
        s, t = LS()

        # Build the undirected, weighted graph
        e = collections.defaultdict(list)
        for _ in range(n):
            a, b, c = LS()
            c = int(c)
            e[a].append((b, c))
            e[b].append((a, c))

        # Read names of recharge stations into a set for quick lookup
        cs = set([S() for _ in range(m)])

        def search(s, t):
            """
            Performs a modified Dijkstra search to find the minimum cost path from s to t,
            respecting the fuel constraints and recharging at stations.

            Args:
                s (str): Starting node.
                t (str): Target node.

            Returns:
                int or None: Minimum cost if reachable, otherwise None.
            """
            # d[(node, fuel_left)]: current best cost to reach (node, fuel_left)
            d = collections.defaultdict(lambda: inf)
            d[(s, cap)] = 0

            # Priority queue elements: (current cost, (node, fuel_left))
            q = []
            heapq.heappush(q, (0, (s, cap)))

            # v[vertex]: has this state (node, fuel_left) been expanded
            v = collections.defaultdict(bool)

            while q:
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True

                # Check if we've reached the target node
                if u[0] == t:
                    return k

                # Explore neighbors
                for uv, ud in e[u[0]]:
                    uc = u[1] - ud  # Fuel left after traveling to neighbor
                    if uc < 0:
                        continue  # Can't travel if not enough fuel

                    # If this is a recharge station, refuel to full capacity
                    if uv in cs:
                        uc = cap

                    next_state = (uv, uc)
                    if v[next_state]:
                        continue

                    vd = k + ud  # New total distance

                    if d[next_state] > vd:
                        d[next_state] = vd
                        heapq.heappush(q, (vd, next_state))

            # Not reachable
            return None

        # Compute the answer for this test case
        r = search(s, t)
        if r is None:
            return -1

        return r

    while True:
        # Read graph parameters for each test case
        n, m, l = LI()
        if n == 0:
            break
        # Solve and collect the answer for this test case
        rr.append(f(n, m, l))

    # Combine results into a single output string
    return '\n'.join(map(str, rr))

# The script execution entry point
print(main())