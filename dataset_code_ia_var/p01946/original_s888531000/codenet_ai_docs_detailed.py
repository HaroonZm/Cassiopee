#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math

# Increase the recursion limit for safety with recursive algorithms
sys.setrecursionlimit(10**5)

# Redefine input to stdin readline for faster input operations
input = sys.stdin.readline

# Aliases for mathematical functions
sqrt = math.sqrt

# =========================
# Utility Input Functions
# =========================

def LI():
    """
    Read a line of input and return a list of integers.
    Example: For input "1 2 3", returns [1, 2, 3]
    """
    return list(map(int, input().split()))

def LF():
    """
    Read a line of input and return a list of floats.
    Example: For input "1.2 3.4", returns [1.2, 3.4]
    """
    return list(map(float, input().split()))

def LI_():
    """
    Read a line of input and return a list of integers decremented by 1.
    Useful for zero-indexed problems.
    Example: For input "2 3 4", returns [1, 2, 3]
    """
    return list(map(lambda x: int(x)-1, input().split()))

def II():
    """
    Read a line of input and return it as an integer.
    """
    return int(input())

def IF():
    """
    Read a line of input and return it as a float.
    """
    return float(input())

def LS():
    """
    Read a line of input and return a list of lists (each character as an element).
    Example: For input "abc def", returns [['a', 'b', 'c'], ['d', 'e', 'f']]
    """
    return list(map(list, input().split()))

def S():
    """
    Read a line of input, strip whitespace, and return list of characters.
    Example: For input "hello", returns ['h', 'e', 'l', 'l', 'o']
    """
    return list(input().rstrip())

def IR(n):
    """
    Read n lines of integer input and return as a list.
    Each line contains a single integer.
    """
    return [II() for _ in range(n)]

def LIR(n):
    """
    Read n lines, each containing space-separated integers.
    Return as a list of lists of integers.
    """
    return [LI() for _ in range(n)]

def FR(n):
    """
    Read n lines of float input and return as a list.
    Each line contains a single float.
    """
    return [IF() for _ in range(n)]

def LFR(n):
    """
    Read n lines, each containing space-separated floats.
    Return as a list of lists of floats.
    """
    return [LF() for _ in range(n)]

def LIR_(n):
    """
    Read n lines, each containing space-separated integers (zero-indexed).
    Decrement each integer by 1.
    Return as list of lists.
    """
    return [LI_() for _ in range(n)]

def SR(n):
    """
    Read n lines. Each line is a string; return list of lists of characters.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Read n lines. Each line is split into words, each word is split into characters.
    Return list of lists of lists.
    """
    return [LS() for _ in range(n)]

# Common modulus and infinity constant for use in problems
mod = 1000000007
inf = float('INF')

# =========================
# Problem A Implementation
# =========================

def A():
    """
    Solve Problem A as defined.
    Read three integers s, t, d from input:
      - s: initial value (like a score, counter, etc.)
      - t: the target (threshold) value to reach or fall below
      - d: the number of steps in a period
    Then read a list w of d integers (changes or steps per period).

    The goal is to determine the first time (1-indexed) when the score reaches or goes below t,
    or if it will never happen under the rules, output -1.

    Details:
        - At each step i (for i in 0..d-1):
            add w[i] to s (named sb).
            If sb <= t at any point, print i + 1 and return.
        - If sum of period (sumw) is non-negative, and the threshold was not crossed,
          output -1, as the threshold will never be reached.
        - Otherwise, perform full cycles as much as possible to reduce s quickly,
          then simulate step by step until the threshold is crossed.
    """
    # Read initial values: s = starting value; t = target threshold; d = steps per period
    s, t, d = LI()
    # Read the list of step increments/decrements
    w = LI()
    # Calculate the sum of one period (for cycles)
    sumw = sum(w)
    # sb is the current value in the loop
    sb = s
    # mins is the minimum value reached during the first period
    mins = s

    # Simulate the first period, check after each step
    for i in range(d):
        sb += w[i]
        mins = min(mins, sb)
        if sb <= t:
            # Reached (or crossed below) the target after i+1 steps
            print(i + 1)
            return

    # If no crossing, but the period sum doesn't decrease the value, solution is impossible
    if sumw >= 0:
        print(-1)
    else:
        # Calculate the minimum number of full periods required to possibly reach threshold
        ans = ((mins - t) // abs(sumw)) * d
        # Reduce initial value s by as many full periods as possible
        s += ans // d * sumw

        # Stepwise simulation after bulk periods, until we cross the threshold
        i = 0
        while True:
            if s <= t:
                print(ans + i)
                return
            # Take next step (cycle back via modulo)
            s += w[i % d]
            i += 1
        # Unreachable, left for completeness
        print(ans + i + 1)
    return

# =========================
# Default Empty Functions
# =========================

def B():
    """
    Placeholder for Problem B logic.
    """
    return

def C():
    """
    Placeholder for Problem C logic.
    """
    return

def D():
    """
    Placeholder for Problem D logic.
    """
    return

def E():
    """
    Placeholder for Problem E logic.
    """
    return

def F():
    """
    Placeholder for Problem F logic.
    """
    return

def G():
    """
    Placeholder for Problem G logic.
    """
    return

def H():
    """
    Placeholder for Problem H logic.
    """
    return

# =========================
# Main Solver Entry Point
# =========================

if __name__ == '__main__':
    # Run the solution for Problem A by default when executed
    A()