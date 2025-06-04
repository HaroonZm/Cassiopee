import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

# Optionally increase recursion limit if using deep recursion
# sys.setrecursionlimit(1000000)

# Input aliases for convenience and code brevity
input = sys.stdin.readline  # Fast input reading
getS = lambda: input().strip()  # Get string input and strip whitespace
getN = lambda: int(input())     # Get integer input
getList = lambda: list(map(int, input().split()))  # Get list of integers from input
getZList = lambda: [int(x) - 1 for x in input().split()]  # Get list of zero-indexed integers

INF = float("inf")         # Representation of infinity
MOD = 10**9 + 7            # Common modulus for computations
divide = lambda x: pow(x, MOD-2, MOD)  # Modular inverse using Fermat's little theorem

def solve():
    """
    For a given array, counts the number of contiguous subarrays where the sum and
    the bitwise XOR of the subarray elements are equal.
    
    The function reads input:
        - n: the length of the array
        - lis: the array of integers
    
    Logic:
        Uses a two-pointer technique to maintain a window [l, r) where the sum and XOR
        are equal. Extends r as long as the property holds, else increments l.
        For every valid window, counts the number of subarrays ending at r that start from [l, r).
    Outputs:
        Prints the count of such subarrays.
    """
    n = getN()             # Read the length of the array
    lis = getList()        # Read the array elements

    xo, su = 0, 0          # Initialize XOR and sum of the current window
    ans = 0                # Initialize the answer

    l, r = 0, 0            # Left and right pointers of the window
    forward = True         # Direction flag: True to move right pointer, False to move left

    while True:
        # Uncomment for step-by-step debug
        # print(l, r, ans, xo, su)

        if r == n:
            # All elements have been considered
            print(ans)
            return

        if forward:
            # Expand the window by moving the right pointer
            xo = xo ^ lis[r]           # Update XOR with the next element
            su += lis[r]               # Update sum with the next element

            if xo == su:
                # The window [l, r] is valid
                ans += r - l + 1       # Add the valid subarrays ending at position r
                r += 1                 # Move right pointer forward
            else:
                # Window became invalid, need to shrink from the left
                forward = False
        else:
            # Shrink the window from the left until it becomes valid
            xo = xo ^ lis[l]           # Remove the leftmost element from XOR
            su -= lis[l]               # Remove the leftmost element from sum

            if xo == su:
                # Window [l+1, r] is now valid
                forward = True         # Can move forward again
                ans += r - l           # Count valid subarrays for the new window
                r += 1                 # Advance right pointer
                l += 1                 # Advance left pointer
            else:
                l += 1                 # Continue to shrink the window

def main():
    """
    Handles multiple test cases, calling solve() for each one.
    Reads:
        - n: number of test cases
    For each test case, invokes the solve() function.
    """
    n = getN()
    for _ in range(n):
        solve()
    return

if __name__ == "__main__":
    # Entry point when executed as a script.
    # Uncomment main() if solving multiple test cases; for a single case, call solve() directly.
    # main()
    solve()