def s0():
    """
    Reads a single line of input as a string.

    Returns:
        str: The input string.
    """
    return input()


def s1():
    """
    Reads a line of input and splits it into a list of strings.

    Returns:
        list[str]: The split input line as a list of strings.
    """
    return input().split()


def s2(n):
    """
    Reads 'n' lines of input, each as a string.

    Args:
        n (int): Number of input lines to read.

    Returns:
        list[str]: List containing 'n' input strings.
    """
    return [input() for _ in range(n)]


def s3(n):
    """
    Reads 'n' lines of input, splitting each line into a list of strings.

    Args:
        n (int): Number of input lines to read.

    Returns:
        list[list[str]]: List containing 'n' lists of split strings.
    """
    return [input().split() for _ in range(n)]


def s4(n):
    """
    Reads 'n' lines of input and converts each line to a list of characters.

    Args:
        n (int): Number of input lines to read.

    Returns:
        list[list[str]]: List of 'n' lists, where each inner list contains characters from each input string.
    """
    return [[x for x in s] for s in s2(n)]


def n0():
    """
    Reads a single integer value from input.

    Returns:
        int: The input integer.
    """
    return int(input())


def n1():
    """
    Reads a line of input, splits it by spaces, and converts each element to an integer.

    Returns:
        list[int]: List of integers parsed from the input line.
    """
    return [int(x) for x in input().split()]


def n2(n):
    """
    Reads 'n' integer values from input, one per line.

    Args:
        n (int): Number of integers to read.

    Returns:
        list[int]: List of 'n' integers.
    """
    return [int(input()) for _ in range(n)]


def n3(n):
    """
    Reads 'n' lines of input, each line containing space-separated integers, and returns them as a list of lists.

    Args:
        n (int): Number of input lines to read.

    Returns:
        list[list[int]]: List of 'n' lists of integers.
    """
    return [[int(x) for x in input().split()] for _ in range(n)]


def t3(n):
    """
    Reads 'n' lines of input, each line containing space-separated integers, and returns them as a list of integer tuples.

    Args:
        n (int): Number of input lines to read.

    Returns:
        list[tuple[int]]: List of 'n' tuples of integers.
    """
    return [tuple(int(x) for x in input().split()) for _ in range(n)]


def p0(b, yes="Yes", no="No"):
    """
    Prints 'yes' string if the condition is True, otherwise prints 'no' string.

    Args:
        b (bool): Condition to evaluate.
        yes (str, optional): String to print if condition is True. Defaults to "Yes".
        no (str, optional): String to print if condition is False. Defaults to "No".
    """
    print(yes if b else no)


# Example utility imports (useful for typical competitive programming tasks)
# Uncomment as needed.
# from sys import setrecursionlimit
# setrecursionlimit(1000000)
# from collections import Counter, deque, defaultdict
# import itertools
# import math
# import networkx
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappush, heappop


# Main script logic with detailed comments:

# Read the number of elements in the list.
n = n0()

# Read 'n' integers, one per line, and store them in the list 'a'.
a = n2(n)

# Create a sorted copy of list 'a' in ascending order.
b = sorted(a)

# The largest value in the list.
m1 = b[-1]

# The second largest value in the list.
m2 = b[-2]

# For each element in the original list, print m2 if it is equal to the largest value,
# otherwise print m1. This can be used, for example, to answer "what's the largest value
# except i-th element?" in some problem settings.
for i in a:
    p0(i == m1, m2, m1)