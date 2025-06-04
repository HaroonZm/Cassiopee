#!/usr/bin/env python3

from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    """
    Reads a line from standard input, splits it into tokens, converts each token to int,
    and returns the resulting list of integers.
    """
    return list(map(int, sys.stdin.readline().split()))

def I():
    """
    Reads a line from standard input, strips it, converts it to an integer and returns it.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Reads a line from standard input, splits it into tokens, and converts each token into a list of characters.
    Returns a list of list of characters.
    """
    return list(map(list, sys.stdin.readline().split()))

def S():
    """
    Reads a line from standard input and returns it as a list of characters (excluding the trailing newline).
    """
    return list(sys.stdin.readline())[:-1]

def IR(n):
    """
    Reads n lines from standard input, each line expected to be an integer.
    Returns a list of integers.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    """
    Reads n lines from standard input, each line expected to be space-separated integers.
    Returns a list of lists of integers.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    """
    Reads n lines from standard input, each line as a list of characters.
    Returns a list of character lists.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    """
    Reads n lines from standard input, each line returned as a list of words
    (each word as a list of characters).
    Returns a list of lists of character lists.
    """
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Raise recursion depth to allow parsing deep recursive expressions.
sys.setrecursionlimit(1000000)

# Define a commonly used modulo constant.
mod = 1000000007

def A():
    """
    Main function to process expressions and compute their values and equivalence counts.
    It repeatedly reads two lines:
    - The first line is an expression string encoding an expression tree with variables (a, b, c, d) and operators [+ * ^].
    - The second line provides digits to use as the assignment for each variable.
    The function substitutes the variables, evaluates the result, and determines in how many ways
    (over all digit assignments to a, b, c, d from [0-9]) the expression would yield the same value.
    Prints the evaluated value and the count for each input, until an expression line starting with '.' is read.
    """

    def parse_hash(s, i):
        """
        Recursive parser for evaluating the expression.
        Args:
            s (list): The expression as a list where variables are already substituted as digits.
            i (int): Current parsing position.
        Returns:
            (int, int): Tuple of (computed value, next parsing position).
        """
        if s[i] == "[":
            i += 1
            op, i = parse_op(s, i)
            h1, i = parse_hash(s, i)
            h2, i = parse_hash(s, i)
            i += 1  # skip closing ']'
            return calc(op, h1, h2), i
        else:
            return parse_letter(s, i)

    def parse_op(s, i):
        """
        Parses an operator from the current position.
        Args:
            s (list): The expression list.
            i (int): Current position.
        Returns:
            (str, int): The operator and next position.
        """
        return s[i], i + 1

    def parse_letter(s, i):
        """
        Parses a digit or leaf node from the current position.
        Args:
            s (list): The expression list.
            i (int): Current position.
        Returns:
            (int, int): The digit value and next position.
        """
        return s[i], i + 1

    def calc(op, h1, h2):
        """
        Applies an operator to two operands.
        Args:
            op (str): The operator ('+', '*', or '^').
            h1 (int): First operand.
            h2 (int): Second operand.
        Returns:
            int: The result of applying op to h1 and h2.
        """
        if op == "+":
            return h1 | h2  # Bitwise OR
        elif op == "*":
            return h1 & h2  # Bitwise AND
        else:
            return h1 ^ h2  # Bitwise XOR

    while True:
        s = S()  # Read expression string as list of characters
        if s[0] == ".":
            break  # Exit on '.' line
        t = S()  # Read the variable assignments as list of characters (digits as strings)
        n = len(s)
        # Substitute variables 'a', 'b', 'c', 'd' with their corresponding values from t
        s0 = [s[i] for i in range(n)]
        for i in range(n):
            if s0[i] == "a":
                s0[i] = int(t[0])
            elif s0[i] == "b":
                s0[i] = int(t[1])
            elif s0[i] == "c":
                s0[i] = int(t[2])
            elif s0[i] == "d":
                s0[i] = int(t[3])
        # Evaluate the expression tree for the given assignment
        p = parse_hash(s0, 0)[0]
        ans = 0  # Counter for assignments yielding same evaluated value
        # Iterate over all possible assignments of a, b, c, d (digits 0-9)
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        # For each assignment, create an expression with those digits substituted
                        s0 = [s[i] for i in range(n)]
                        for i in range(n):
                            if s0[i] == "a":
                                s0[i] = a
                            elif s0[i] == "b":
                                s0[i] = b
                            elif s0[i] == "c":
                                s0[i] = c
                            elif s0[i] == "d":
                                s0[i] = d
                        # Evaluate the expression for this assignment
                        p0 = parse_hash(s0, 0)[0]
                        if p == p0:
                            ans += 1
        print(p, ans)

    return

def B():
    """
    Placeholder function for problem B.
    """
    return

def C():
    """
    Placeholder function for problem C.
    """
    return

def D():
    """
    Placeholder function for problem D.
    """
    return

def E():
    """
    Placeholder function for problem E.
    """
    return

def F():
    """
    Placeholder function for problem F.
    """
    return

def G():
    """
    Placeholder function for problem G.
    """
    return

def H():
    """
    Placeholder function for problem H.
    """
    return

def I_():
    """
    Placeholder function for problem I.
    """
    return

def J():
    """
    Placeholder function for problem J.
    """
    return

if __name__ == "__main__":
    A()