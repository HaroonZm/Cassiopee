#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """
    Reads a line from standard input and returns a list of integers.

    Returns:
        list[int]: List of integers read from input.
    """
    return list(map(int, sys.stdin.readline().split()))

def I():
    """
    Reads a single integer from standard input.

    Returns:
        int: Integer read from input.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a line from standard input and returns a list of lists,
    splitting on spaces.

    Returns:
        list[list]: List of lists, typically of strings.
    """
    return list(map(list, sys.stdin.readline().split()))

def S():
    """
    Reads a line from standard input and returns it as a list of characters,
    excluding the last character (usually the newline).

    Returns:
        list[str]: List of characters in the input line, without the newline.
    """
    return list(sys.stdin.readline())[:-1]

def IR(n):
    """
    Reads n lines from standard input, each as an integer.

    Args:
        n (int): Number of lines to read.

    Returns:
        list[int]: List of integers read from input.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    """
    Reads n lines from standard input, each as a list of integers.

    Args:
        n (int): Number of lines to read.

    Returns:
        list[list[int]]: List of lists of integers read from input.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    """
    Reads n lines from standard input, each as a list of characters
    (minus the newline).

    Args:
        n (int): Number of lines to read.

    Returns:
        list[list[str]]: List of character lists read from input.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    """
    Reads n lines from standard input, each as a list of lists (splitting).

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of lists from each line, split by spaces.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Increase recursion depth in case of deep recursions in DFS
sys.setrecursionlimit(1000000)

# Commonly used modulus
mod = 1000000007

# ---------------------- Problem A Function ----------------------

def A():
    """
    Problem A: Performs combinatorial calculations based on input values n and k.
    Loops through valid l, i ranges and calculates combinations by hand (efficient 
    for small ranges) summing up into 'ans'. Prints the final result.
    """
    n, k = LI()
    ans = 0
    for l in range(1, n + 1):
        for i in range(1000):
            if i * k > l:
                break
            j = l - i * k + i
            # Only proceed if j is odd
            if j % 2:
                j //= 2
                j += 1
                s = 1
                # Calculate combinations C(j, i)
                for a in range(i):
                    s *= j - a
                    s //= a + 1
                ans += s
    print(ans)
    return

# ---------------------- DFS Utilitary Functions ----------------------

def dfs(d, k, f, n, nu, v, e):
    """
    Performs a DFS to try all possible pairings with conditions and maximizes 'ans'.

    Args:
        d (int): Current depth in recursion tree.
        k (list): List being updated during DFS, used for direction/matching.
        f (list): Flags showing which nodes are available.
        n (int): Number of elements.
        nu (int): n // 2, half the number of elements.
        v (list): List of input data, sorted in B().
        e (dict): Dictionary mapping node pairs to directions/vectors.
    """
    global ans
    if d == nu:
        l = defaultdict(int)
        for i in k:
            l[i] += 1
        res = 0
        for v in l.values():
            res += calc(v)
        if res > ans:
            ans = res
    else:
        # Find first available position (f[p] == 1)
        for i in range(n):
            if f[i]:
                p = i
                break
        # Create a new flag list, with p set to 0 (paired/used)
        f_ = [f[i] if i != p else 0 for i in range(n)]
        for q in range(p + 1, n):
            if f[q]:
                # Get vector/direction for this pair
                m = e[(p, q)]
                # Construct new k for this pairing
                k_ = [k[i] if i != d else m for i in range(nu)]
                # Set q to unavailable in flags
                f__ = [f_[i] if i != q else 0 for i in range(n)]
                dfs(d + 1, k_, f__, n, nu, v, e)

def calc(n):
    """
    Given n, returns the number of unordered pairs that can be made (n choose 2).

    Args:
        n (int): Number of elements.

    Returns:
        int: n*(n-1)//2 (number of pairs).
    """
    return n * (n - 1) // 2

def gcd(a, b):
    """
    Computes the greatest common divisor (GCD) of a and b.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: GCD of a and b.
    """
    if a == 0:
        return b
    return gcd(b % a, a)

# Global variable (used in dfs/B)
ans = 0

# ---------------------- Problem B Function ----------------------

def B():
    """
    Problem B: Reads n pairs of coordinates, finds unique vectors for every pair,
    and tries all pairings using DFS to maximize matching conditions (as determined
    by direction equality or count of pairs). Prints the final calculated answer.
    """
    n = I()
    nu = n // 2  # Number of pairs that will be formed
    v = LIR(n)   # Read n points (each: [x, y])
    v.sort()     # Sort for consistency
    e = defaultdict(set)  # Map from (p, q) -> direction vector

    # For every pair of points (p, q), store the direction, simplified by GCD
    for p in range(n):
        for q in range(p + 1, n):
            x, y = v[q][0] - v[p][0], v[q][1] - v[p][1]
            if x == 0:
                if y < 0:
                    m = (0, -1)
                else:
                    m = (0, 1)
            elif y == 0:
                m = (1, 0)
            else:
                g = gcd(x, abs(y))
                m = (x // g, y // g)
            e[(p, q)] = m

    # Use f to keep track of unpaired points
    f = [1 for _ in range(n)]
    k = [None for _ in range(nu)]  # List of directions in pairings
    dfs(0, k, f, n, nu, v, e)
    print(ans)
    return

# ---------------------- Problem C Function ----------------------

def C():
    """
    Placeholder for Problem C. Reads data, performs processing on connections,
    builds adjacency, then (for now) prints intermediate structures.
    """
    while True:
        n = I()
        if n == 0:
            break
        v = [input().split() for _ in range(n)]
        d = defaultdict(int)
        f = [[1 for _ in range(n)] for _ in range(n)]
        i = 0
        s = 0
        while i < n:
            v[i][1] = int(v[i][1])
            v[i][2] = int(v[i][2])
            # Remove zero items and sum
            if v[i][2] == 0:
                s += v[i][1]
                v.pop(i)
                n -= 1
            else:
                d[v[i][0]] = i
                i += 1

        for i in range(n):
            for j in v[i][3:]:
                f[i][d[j]] = 0
        e = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if f[i][j]:
                    e[i].append(j)
        for i in e:
            print(i)
        print(ans)
    return

# ---------------------- Problem D Function ----------------------

def D():
    """
    Problem D: Calculates the maximum number of overlapping intervals for n given
    intervals, with additional computation for maximizing a separate related value.
    Prints both maximum values found.
    """
    n = I()
    s = [0 for _ in range(100001)]  # Interval coverage at each point
    l = LIR(n)   # Read interval endpoints [a, b] pairs
    l.sort(key=lambda x: x[1])  # Sort by right endpoint
    r = [l[i][0] for i in range(n)]
    r.sort()
    f = [0 for _ in range(100001)]  # Cumulative count up to each point

    # Mark interval starts/ends for prefix sum
    for a, b in l:
        s[a] += 1
        s[b] -= 1
        f[b] += 1

    # Compute prefix sums of coverage and up-to counts
    for i in range(100000):
        s[i + 1] += s[i]
        f[i + 1] += f[i]
    ans = 0

    # For each interval, compute the number of intervals that do not overlap
    for a, b in l:
        ri = bisect.bisect_left(r, b)
        ri = n - ri
        le = f[a]
        ans = max(ans, n - (ri + le))
    print(ans, max(s))
    return

# ---------------------- Problem E Function ----------------------

def E():
    """
    Problem E: For a set of n nodes with costs and m edges, process nodes in order
    of cost, and perform BFS-style traversal to update an answer array. Incomplete.
    """
    n = I()
    c = LI()
    f = [[i, c[i]] for i in range(n)]
    f.sort(key=lambda x: x[1])  # Sort nodes by cost
    v = [[] for _ in range(n)]  # Adjacency list
    m = I()
    for _ in range(m):
        a, b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    q = deque()
    bfs_map = [1 for _ in range(n)]  # Visited array
    ans = [0 for _ in range(n)]
    for i, j in f:
        if not bfs_map[i]:
            continue
        q.append((i, -1))
        bfs_map[i] = 0
        ans[i] = 1
        while q:
            x, pre = q.popleft()
            for y in v[x]:
                if bfs_map[y]:
                    if x == 0:
                        bfs_map[y] = 0
                        q.append((y, x))
    print(sum(ans))
    return

# ---------------------- Placeholders for Problems F-J ----------------------

def F():
    """
    Placeholder for Problem F.
    """
    return

def G():
    """
    Placeholder for Problem G.
    """
    return

def H():
    """
    Placeholder for Problem H.
    """
    return

def I_():
    """
    Placeholder for Problem I.
    """
    return

def J():
    """
    Placeholder for Problem J.
    """
    return

# ---------------------- Solve/Driver Code ----------------------

if __name__ == "__main__":
    # Calls Problem B function by default when script is run directly
    B()