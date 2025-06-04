#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """
    Reads a single line from standard input and converts it into a list of integers.

    Returns:
        list: List of integers read from input.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Reads a single integer from standard input.

    Returns:
        int: The integer read from input.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a single line from input, splits it by whitespace, and converts each word into a list of its characters.

    Returns:
        list: List of lists, where each list contains characters of each word found in the line.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Reads a single line from standard input and returns a list of its characters, excluding the newline at the end.

    Returns:
        list: List of characters from the input line.
    """
    return list(sys.stdin.readline())[:-1]

def IR(n):
    """
    Reads n integers from standard input (one per line).

    Args:
        n (int): Number of integers to read.

    Returns:
        list: List of integers read from input.
    """
    return [I() for _ in range(n)]

def LIR(n):
    """
    Reads n lines from standard input, each containing a list of integers.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of integer lists, each representing a line from input.
    """
    return [LI() for _ in range(n)]

def SR(n):
    """
    Reads n lines from standard input, each line returned as a list of its characters.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: List of character lists, each representing a line from input.
    """
    return [S() for _ in range(n)]

def LSR(n):
    """
    Reads n lines from standard input, splitting each line into words,
    and converts each word into a list of its characters.

    Args:
        n (int): Number of lines to read.

    Returns:
        list: A list of lists (for n lines) containing lists of lists of characters (for each word per line).
    """
    return [LS() for _ in range(n)]

# Increase the recursion limit for deep recursions if necessary.
sys.setrecursionlimit(1000000)
# Modulus constant (commonly used in competitive programming)
mod = 1000000007

def solve():
    """
    Main function to process the problem logic:
    1. Reads an integer s.
    2. If s == 1, prints 1 and exits.
    3. Finds all divisors of s.
    4. For all divisors, uses mathematical properties and combinatorial analysis to
       count certain sequences accordingly.
    5. Prints the computed answer.
    """

    def sum_of_arithmetic_sequence(a, b):
        """
        Calculates the sum of an arithmetic sequence from a to b inclusive.
        Uses the formula for the sum of an arithmetic progression.

        Args:
            a (int): Starting integer of the sequence.
            b (int): Ending integer of the sequence.

        Returns:
            int: The sum of integers from a to b.
        """
        return ((b + a) * (b - a + 1)) >> 1

    def divisors(n):
        """
        Computes all divisors of the given integer n.

        Args:
            n (int): The target integer.

        Returns:
            list: A sorted list containing all positive divisors of n.
        """
        if n < 4:
            return [1, n]
        res = [1]
        i = 2
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                m = n // i
                if i != m:
                    res.append(m)
            i += 1
        res.append(n)
        return res

    s = I()  # Read input integer s

    # Edge case: if s == 1, only one sequence possible
    if s == 1:
        print(1)
        return

    # Find all divisors of s
    lis = divisors(s)

    # f: stores counts for sums, initialized to 0
    f = defaultdict(lambda: 0)
    # p: memory to prevent double-counting for (a,b) pairs
    p = defaultdict(lambda: 1)

    # Sort the divisor list for ordered processing
    lis.sort()

    for k in lis:
        # First loop: consider pairs (a, b) such that a + b = k and a <= b
        for a in range(1, k + 1):
            b = k - a
            if a <= b:
                # Ensure this (a, b) pair is only processed once
                if p[(a, b)]:
                    # Increment count for this sum of arithmetic sequence
                    f[sum_of_arithmetic_sequence(a, b)] += 1
                    p[(a, b)] = 0

        # Second loop: investigate further (a, b) that relate to current k and s
        for a in range(1, s + 1):
            b = k + a - 1
            if p[(a, b)]:
                s_ = sum_of_arithmetic_sequence(a, b)
                if s_ > s:
                    break
                f[s_] += 1
                p[(a, b)] = 0

    ans = 0
    # Finally, accumulate the answer by multiplying possible f[k] * f[s // k] for each divisor k
    for k in lis:
        ans += f[k] * f[s // k]

    print(ans)
    return

if __name__ == "__main__":
    solve()