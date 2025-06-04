#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """
    Reads a line from standard input, splits it into space-separated components,
    and returns a list of integers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Reads a single integer value from standard input.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a line from standard input, splits it into components based on spaces,
    and returns a list of lists, each containing the characters of the component.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Reads a line from standard input and returns it as a list of characters.
    If the line ends with a newline character, it is removed.
    """
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    """
    Reads n lines, each containing a single integer, and returns them as a list.
    
    Args:
        n (int): Number of lines to read.
    
    Returns:
        List[int]: List containing n integers.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Reads n lines from standard input, each containing space-separated integers,
    and returns them as a list of lists of integers.
    
    Args:
        n (int): Number of lines to read.
    
    Returns:
        List[List[int]]: List containing n lists of integers.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Reads n lines from standard input, returning each as a list of characters.
    
    Args:
        n (int): Number of lines to read.
    
    Returns:
        List[List[str]]: Each line as a list of characters.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Reads n lines from standard input, splitting each into space-separated words,
    and returns a list of lists of lists of characters.
    
    Args:
        n (int): Number of lines to read.
    
    Returns:
        List[List[List[str]]]: Nested list structure for each word per line.
    """
    return [LS() for _ in range(n)]

# Increase recursion limit for large recursions if needed
sys.setrecursionlimit(1000000)

# Pre-defined modulus value for modular arithmetic if required
mod = 1000000007

def solve():
    """
    Reads input parameters and performs a simulation to find out after how many steps the value
    's' becomes less than or equal to 't' by sequentially adding changes from list 'w', possibly
    repeating the sequence in cycles. Prints the earliest (1-based) step at which 's' <= 't',
    or prints -1 if it never occurs.
    
    Input format expected from stdin:
        - First line: three integers s, t, d (initial value, threshold, sequence length)
        - Second line: d integers (the sequence of changes w)
    
    No explicit return value.
    """
    # Read initial values and sequence parameters
    s, t, d = LI()
    w = LI()  # Sequence of changes
    W = -sum(w)  # Cumulative total decrease (negative sum of w)
    
    if W <= 0:
        # If the cumulative change can never lower 's' below 't', simulate up to d steps
        for i in range(d):
            s += w[i]
            if s <= t:
                print(i + 1)
                return
        # If not decreased sufficiently after full cycle, impossible
        print(-1)
    else:
        # If sufficiently decreasing, proceed to simulate and compute cycles
        S = [s]  # Track the partial sum of 's' after each step
        for i in range(d):
            S.append(S[-1] + w[i])
            if S[-1] <= t:
                # If at any step, the value drops below or equals the threshold, output steps taken
                print(i + 1)
                return
        # Find lowest reached value and its first occurrence
        m = min(S)
        for j in range(d + 1):
            if S[j] == m:
                break
        s = S[j]
        # Rotate sequence so "w" starts from the suffix after reaching minimum
        w = w[j:] + w[:j]
        # Calculate number of full cycles to bring 's' below or equal to 't'
        k = (s - t) // W
        s -= k * W
        if s <= t:
            print(k * d + j)
            return
        # After k cycles, simulate step by step to find exact step
        for i in range(d):
            s += w[i]
            if s <= t:
                print(k * d + i + 1 + j)
                return
    return

# Entry point: calls the solve function if this file is executed as a script
if __name__ == "__main__":
    solve()