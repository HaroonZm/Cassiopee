#!/usr/bin/env python3
import sys
import bisect
from functools import partial
from operator import itemgetter

sys.setrecursionlimit(1 << 25)
MOD = 10**9 + 7

# Input utilities with modern Python features
def input_ints(): return list(map(int, sys.stdin.readline().split()))
def input_int(): return int(sys.stdin.readline())
def input_lines(f, n): return [f() for _ in range(n)]

def powerset_sums(nums):
    n = len(nums)
    sums_by_count = [[] for _ in range(n + 1)]
    for mask in range(1 << n):
        s = bits = 0
        for i in range(n):
            if mask & (1 << i):
                s += nums[i]
                bits += 1
        sums_by_count[bits].append(s)
    return sums_by_count

def solve():
    n, k, l, r = input_ints()
    arr = input_ints()
    n1 = n // 2
    n2 = n - n1

    left_sums = powerset_sums(arr[:n1])
    right_sums = powerset_sums(arr[n1:])
    list(map(list.sort, right_sums))  # Sort each for binary search

    result = sum(
        sum(
            bisect.bisect_right(right_sums[k - cnt_left], r - s_l)
            - bisect.bisect_left(right_sums[k - cnt_left], l - s_l)
            for s_l in left_sums[cnt_left]
        )
        for cnt_left in range(min(k, n1) + 1)
        if k - cnt_left <= n2
    )
    print(result)

if __name__ == "__main__":
    solve()