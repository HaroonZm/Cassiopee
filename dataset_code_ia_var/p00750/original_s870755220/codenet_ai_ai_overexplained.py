import math  # Import the math module, which provides mathematical functions like sqrt, ceil, floor, etc.
import string  # Import the string module, which contains string constants and utility functions for string manipulation.
import itertools  # Import itertools for efficient looping constructs and combinatorial generators.
import fractions  # Import fractions to work easily with rational numbers using the Fraction class.
import heapq  # Import heapq, a library for heap/priority queue algorithms.
import collections  # Import collections for specialized container datatypes like defaultdict, deque, Counter, etc.
import re  # Import re, the regular expressions library in Python, for advanced string searching and manipulation.
import array  # Import array module for space-efficient arrays of basic C types.
import bisect  # Import bisect for maintaining a list in sorted order without having to sort the list after each insertion.
import sys  # Import the sys module which provides access to system-specific functions and variables.
import random  # Import random module for generating pseudo-random numbers and performing random selections.
import time  # Import time module for working with time-related functions.
import copy  # Import copy for shallow and deep copy operations of objects.
import functools  # Import functools for higher-order functions: functions that act on or return other functions.

# Increase the maximum depth of the Python interpreter stack to allow deep recursions.
sys.setrecursionlimit(10**7)  # The default limit is quite small (usually 1000).

inf = 10**20  # Assigns a sufficiently large integer value that can act as mathematical infinity in practical scenarios.
eps = 1.0 / 10**13  # A very small real number, useful as an epsilon for floating-point comparisons.
mod = 10**9+7  # A large prime number commonly used as a modulus in competitive programming to avoid integer overflow issues.

# 4-direction vector: up, right, down, left. Each tuple represents the dx, dy offset.
dd = [(-1,0),(0,1),(1,0),(0,-1)]

# 8-direction vector: includes diagonals. Used often in grid-based problems to traverse all adjacent cells.
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Helper function: Reads a line from standard input, splits it by whitespace, and converts each element to int.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Helper function: Similar to LI(), but subtracts 1 from each integer (useful for 0-based indexing).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Helper function: Reads a line from standard input, splits it, and converts to float.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Helper: Reads a line, splits by whitespace, returns as a list of strings.
def LS():
    return sys.stdin.readline().split()

# Reads a single integer from input.
def I():
    return int(sys.stdin.readline())

# Reads a single float.
def F():
    return float(sys.stdin.readline())

# Reads a line from input, removes ending newline, and returns as a string.
def S():
    return input()

# Prints string and flushes the output buffer to ensure that output appears immediately (important in interactive problems).
def pf(s):
    return print(s, flush=True)

# Segment Tree class for efficient range queries and updates.
class Seg():
    # Constructor:
    # na: size of the array or the initial array itself
    # default: default value for the operation (e.g., 0 for sum, infinity for min)
    # func: function to merge two segments, like sum or min or max
    def __init__(self, na, default, func):
        # If na is a list, get its length; else, treat na as the length.
        if isinstance(na, list):
            n = len(na)  # Length of na
        else:
            n = na  # Assume na is the size
        i = 1  # Initialize exponent for calculating required power-of-two length
        while 2**i <= n:
            i += 1  # Increase i until 2**i > n, to pad segment tree to next power of two
        self.D = default  # Store the default element for the segment tree (e.g., 0, inf, etc.)
        self.H = i  # Store tree height
        self.N = 2**i  # Number of leaves in the segment tree (always a power of two >= n)
        # If na was a list, create segment tree with the elements in their right positions
        if isinstance(na, list):
            # Construct the leaves, pad front for 1-based tree indexing, pad end for non-complete last leaves
            self.A = [default] * (self.N) + na + [default] * (self.N-n)
            # Build tree values from bottom up by merging children using the func provided
            for i in range(self.N-1,0,-1):
                self.A[i] = func(self.A[i*2], self.A[i*2+1])
        else:
            # If only size was given, initialize all with the default value
            self.A = [default] * (self.N*2)
        self.F = func  # Merge function for this segment tree

    # Returns the value at position i (i-th leaf element, 0-based indexing)
    def find(self, i):
        # The actual data starts at index self.N in self.A
        return self.A[i + self.N]

    # Updates the element at position i with value x and recalculates all relevant tree nodes.
    def update(self, i, x):
        i += self.N  # Convert the leaf index to the correct position in self.A
        self.A[i] = x  # Update the value at leaf
        while i > 1:  # Move up the tree and update parents
            i = i // 2  # Move to parent node
            self.A[i] = self.merge(self.A[i*2], self.A[i*2+1])  # Merge children to update parent

    # Merge two values using the function provided at construction.
    def merge(self, a, b):
        return self.F(a, b)

    # Returns the value merged over the entire range (overall segment tree root).
    def total(self):
        return self.A[1]

    # Range query: returns result of merging elements in [a, b)
    def query(self, a, b):
        A = self.A  # Alias for the array
        l = a + self.N  # Shift to leaf index for the left bound (inclusive)
        r = b + self.N  # Ditto for right bound (exclusive)
        res = self.D  # Start with the default element (e.g., zero or inf)
        while l < r:
            # If l is odd (right child), the range covers A[l]
            if l % 2 == 1:
                res = self.merge(res, A[l])  # Merge A[l] into current result
                l += 1  # Move to the next right neighbor
            # If r is odd before decrement, the rightmost segment is not covered yet
            if r % 2 == 1:
                r -= 1  # Move back to the covered segment
                res = self.merge(res, A[r])  # Merge A[r]
            l >>= 1  # Move l up to its parent
            r >>= 1  # Move r up to its parent
        return res  # Final result after going through all relevant segments

# Main function where the main task occurs
def main():
    rr = []  # This list will gather the answers for each test case for printing at the end

    # Function f processes a single test case of the problem
    # n: number of nodes
    # m: number of edges
    # s: start node
    # g: target node
    def f(n, m, s, g):
        # Helper function to parse one edge description
        def _f(a):
            x, y, lab = a  # Edge goes from x to y and has a label 'lab'
            return [int(x), int(y), lab]  # Convert x and y to int, keep lab as string

        # Read m lines, parse each line as an edge using _f, get a list of edges.
        a = [_f(LS()) for _ in range(m)]

        # e will be the adjacency list: key=node, value=list of tuples (neighbor, cost)
        e = collections.defaultdict(list)

        # Build adjacency list but reversed: edges added as e[y].append((x,1))
        for x, y, lab in a:  # For each edge in input
            e[y].append((x, 1))  # Reverse the direction: store y->x with cost 1

        # Function to do Dijkstra's/0-1 BFS from starting node s
        def search(s):
            d = collections.defaultdict(lambda: inf)  # Distance from s to each node, default is inf
            d[s] = 0  # Distance to s itself is zero
            q = []  # The priority queue: stores (distance, node)
            heapq.heappush(q, (0, s))  # Initialize with start node
            v = collections.defaultdict(bool)  # Visited flag for each node
            while len(q):  # While the queue is not empty
                k, u = heapq.heappop(q)  # Get node with smallest distance so far
                if v[u]:
                    continue  # Skip if this node was already processed
                v[u] = True  # Mark this node as visited

                for uv, ud in e[u]:  # Explore neighbors (uv) with their edge costs (ud)
                    if v[uv]:
                        continue  # Skip already processed
                    vd = k + ud  # New tentative distance
                    if d[uv] > vd:  # If new path is shorter, update
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))  # Re-add uv to queue with new distance
            return d  # Return distances

        # Run search from target 'g', filling in minimum distances from all nodes to g
        d = search(g)
        if d[s] == inf:  # If s can't reach g (distance is infinite)
            return 'NO'  # There's no valid path

        # Recompute e: build direct adjacency from x to y, only if both ends are reachable
        e = collections.defaultdict(list)
        ee = [[''] * n for _ in range(n)]  # Matrix of labels
        for x, y, lab in a:
            if d[x] == inf or d[y] == inf:
                continue  # Skip if unreachable from g
            e[x].append((y, lab))  # Standard adjacency: for each x, add y and label lab
            ee[x][y] = lab  # Store label for edge x->y

        ml = 0  # Max string length for path
        for k, v in e.items():
            vl = max(map(lambda x: len(x[1]), v))  # Largest label length for outgoing edges from k
            ml += vl  # Accumulate
        ml = ml * 2 + 2  # Double that plus 2 (used as path string length limiting value)

        # Search for lex smallest path from s to g
        def search2(s, g):
            d = collections.defaultdict(lambda: None)  # Best string for each (node, length) pair
            d[(s, 0)] = ''  # Empty string is the best path from s with length 0
            q = []
            heapq.heappush(q, ('', (s, 0)))  # Start from s and string ''
            v = collections.defaultdict(bool)  # Visited state for each (node, length)
            while len(q):  # While priority queue is not empty
                k, u = heapq.heappop(q)  # String so far, (node, length)
                if v[u]:  # If already processed, skip
                    continue
                v[u] = True  # Mark as processed

                for uv, ud in e[u[0]]:  # For all outgoing edges from this node
                    vd = k + ud  # Append edge label to path string
                    vl = len(vd)  # Compute current string length
                    if vl >= ml:  # If path is too long, skip to avoid cycles/infinite loops
                        continue
                    uv = (uv, vl)  # The new state: (neighbor, string length so far)
                    if v[uv]:  # If already visited, skip
                        continue
                    if d[uv] is None or d[uv] > vd:  # If no string yet or found a better (smaller) string
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))  # Add next state to the queue
            # Find the lex smallest string from s to g at any string length < ml
            return min([d[(g, _)] for _ in range(ml) if not d[(g, _)] is None])

        dg = search2(s, g)  # Run search for best path string from s to g
        if len(dg) >= ml // 2:  # If answer is too long (no valid solution)
            return 'NO'
        return dg  # Else, return the found path string

    while 1:  # Loop over all input test cases
        n, m, s, g = LI()  # Read four integers: number of nodes, number of edges, start, goal
        if n == 0:  # Input termination condition
            break
        rr.append(f(n, m, s, g))  # Process and append the answer for this test case

    return '\n'.join(map(str, rr))  # Output result answers as multi-line string

print(main())  # Call main() and print its result (this runs the solution)