#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """Reads a single line from stdin and parses it into a list of integers."""
    return list(map(int, sys.stdin.readline().split()))

def I():
    """Reads a single line from stdin and parses it as an integer."""
    return int(sys.stdin.readline())

def LS():
    """Reads a single line from stdin, splits into space-separated items, and returns a list of lists (each character)."""
    return list(map(list, sys.stdin.readline().split()))

def S():
    """Reads a single line from stdin and returns it as a list of characters, excluding the trailing newline."""
    return list(sys.stdin.readline())[:-1]

def IR(n):
    """
    Reads n lines from stdin, parsing each as an integer.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of integers from each line.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    """
    Reads n lines from stdin, parsing each line into a list of integers.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of integer lists.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    """
    Reads n lines from stdin, parsing each line into a list of characters.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of character lists.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    """
    Reads n lines from stdin, parsing each line into space-separated lists of characters.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of lists of lists of characters.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Increase the maximum recursion limit for deep recursions
sys.setrecursionlimit(1000000)

# Default modulus value for modular arithmetic
mod = 1000000007

def A():
    """
    Processes inputs in an infinite loop.
    For each set, reads a number n and a list of n integers.
    Computes the mean m, then counts how many values are less than or equal to m.
    If n==0, ends the process.
    """
    while True:
        n = I()
        if n == 0:
            quit()
        a = LI()
        m = sum(a) / n
        c = 0
        for i in range(n):
            if a[i] <= m:
                c += 1
        print(c)
    return

def B():
    """
    Processes multiple input sets in an infinite loop.
    For each set:
      - Reads a number n.
      - Reads n pairs of start and end times in "HH:MM:SS" format.
      - Counts at every second how many intervals are ongoing, and outputs the maximum concurrency.
    Ends if n==0.
    """
    while True:
        n = I()
        if n == 0:
            quit()
        # Create timeline for all seconds in a day
        t = [0 for _ in range(24 * 3600)]
        for i in range(n):
            x, y = input().split()
            # Convert time strings to lists of ints
            x = list(map(int, x.split(":")))
            y = list(map(int, y.split(":")))
            # Calculate seconds since midnight
            l = x[0] * 3600 + x[1] * 60 + x[2]
            r = y[0] * 3600 + y[1] * 60 + y[2]
            # Increment at start, decrement at end
            t[l] += 1
            t[r] -= 1
        ans = 0
        for i in range(24 * 3600 - 1):
            # Accumulate current ongoing intervals
            t[i + 1] += t[i]
            ans = max(ans, t[i])
        print(ans)
    return

def C():
    """
    Reads a single integer n.
    Prints:
      1 if n == 0
      2 if n == 1
      1 if n == 2
      0 otherwise
    """
    n = I()
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    elif n == 2:
        print(1)
    else:
        print(0)
    return

def D():
    """
    Reads a graph definition: number of nodes n, edges m, and two vertices s and t.
    Runs Dijkstra's algorithm from both s and t to compute shortest path distances.
    For each node, counts the number of nodes reachable from t in a given number of steps less than (distance from s to t) - 2.
    Prints the total number of such node pairs.
    """

    def dijkstra(start):
        """
        Implements Dijkstra's algorithm from a given start node.
        Returns the list of minimum distances from start to all other nodes.

        Args:
            start (int): Start node index.

        Returns:
            list: List of shortest path lengths from start.
        """
        distance = [float("inf") for _ in range(n)]
        pq = [[0, start]]
        distance[start] = 0
        while pq:
            dx, x = heappop(pq)
            for y in adj[x]:
                if dx + 1 < distance[y]:
                    distance[y] = distance[x] + 1
                    heappush(pq, [distance[y], y])
        return distance

    # Read graph input
    n, m, s, t = LI()
    s -= 1  # zero-based indices
    t -= 1
    adj = [[] for _ in range(n)]
    for i in range(m):
        x, y = LI()
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)
    # Compute shortest distances from both s and t
    dist_s = dijkstra(s)
    dist_t = dijkstra(t)
    k = dist_s[t] - 2  # Target value for node pair counts
    dist_count = defaultdict(int)
    ans = 0
    # Count occurrences of nodes with given distance from t
    for d in dist_t:
        dist_count[d] += 1
    # For each node, add to answer the number of nodes at the required "opposite" distance
    for d in dist_s:
        ans += dist_count[max(-1, k - d)]
    print(ans)
    return

def E():
    """
    Placeholder for problem E solution.
    """
    return

def F():
    """
    Placeholder for problem F solution.
    """
    return

def G():
    """
    Placeholder for problem G solution.
    """
    return

def H():
    """
    Placeholder for problem H solution.
    """
    return

def I_():
    """
    Placeholder for problem I solution.
    """
    return

def J():
    """
    Placeholder for problem J solution.
    """
    return

if __name__ == "__main__":
    # Run problem D by default when executing the script
    D()