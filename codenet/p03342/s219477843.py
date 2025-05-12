import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def solve():
    n = getN()
    lis = getList()
    xo, su = 0, 0
    ans = 0
    l, r = 0, 0
    forward = True
    while True:
        # print(l, r, ans, xo, su)
        if r == n:
            print(ans)
            return
        if forward:
            xo = xo^lis[r]
            su += lis[r]
            if xo == su:

                ans += r - l + 1
                r += 1
            else:
                forward = False
        else:
            xo = xo^lis[l]
            su -= lis[l]
            if xo == su:
                forward = True
                ans += r - l
                r += 1
                l += 1
            else:
                l += 1

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()