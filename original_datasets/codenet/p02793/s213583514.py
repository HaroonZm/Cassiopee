import sys
from collections import deque
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations
from bisect import bisect, bisect_left

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    c = a * b
    while a % b > 0:
        a, b = b, a % b
    return b

def solve():
    input = sys.stdin.readline
    mod = 7 + 10 ** 9
    N = int(input())
    A = [int(a) for a in input().split()]
    if N == 1: print(1)
    else:
        lcm = A[0]
        for i in range(1, N):
            gcd_a = gcd(lcm, A[i])
            lcm = lcm * A[i] // gcd_a
        lcm %= mod
        sumB = 0
        for i,a in enumerate(A):
            sumB += lcm * pow(a, mod - 2, mod)
            sumB %= mod

        print(sumB)
    return 0

if __name__ == "__main__":
    solve()