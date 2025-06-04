import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

def input():
    """
    Reads a line from sys.stdin and removes the trailing newline character.

    Returns:
        str: The input line without the trailing newline.
    """
    return sys.stdin.readline()[:-1]

def ruiseki(lst):
    """
    Computes the prefix sum (cumulative sum) of a list, returning a new list that prepends 0.

    Args:
        lst (list of int): The input list.

    Returns:
        list of int: The prefix sum array, starting with 0.
    """
    return [0] + list(accumulate(lst))

def celi(a, b):
    """
    Performs ceiling division between a and b, equivalent to math.ceil(a / b).

    Args:
        a (int): Numerator.
        b (int): Denominator (should not be zero).

    Returns:
        int: Ceiling of a divided by b.
    """
    return -(-a // b)

# Increase the recursion limit to allow for deep recursions
sys.setrecursionlimit(5000000)

# Modulo constant (often used for problems involving large numbers or modular arithmetic)
mod = pow(10, 9) + 7

# List of all lowercase English letters
al = [chr(ord('a') + i) for i in range(26)]

# 4-direction movement vectors (down, right, up, left)
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# Read the number of elements
n = int(input())

# Read a list of integers
a = list(map(int, input().split()))

# Initialize answer to 0
ans = 0

# Two pointers l (left) and r (right), both initially at 0
l, r = 0, 0

# cnt will store the sum of the current window, xor the xor-sum.
cnt = 0
xor = 0

# Sliding window approach: count number of contiguous subarrays such that
# the xor equals the sum of all numbers in that subarray.
for i in range(n):
    l = i
    # Expand the window if l == r to initially include the ith element
    if l == r:
        cnt += a[i]
        xor += a[i]
        r += 1
    # Continue expanding right boundary as long as condition holds and we don't exceed list bounds.
    while r + 1 <= n and (xor ^ a[r]) == cnt + a[r]:
        xor ^= a[r]
        cnt += a[r]
        r += 1
    # Remove a[i] from cnt and xor, as left pointer will be moved forward
    cnt -= a[i]
    xor -= a[i]
    # The number of valid subarrays starting at i is r - l
    ans += r - l

# Output the total count of such subarrays
print(ans)