import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

from math import floor, ceil, sqrt, factorial, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy

inf = float('inf')
mod = 10 ** 9 + 7

def pprint(*A):
    for a in A:
        for x in a:
            print(x)

def MI():
    return map(int, input().split())

def MI_():
    return map(lambda x: int(x) - 1, input().split())

def LI():
    return list(MI())

def LI_():
    return [int(x) - 1 for x in input().split()]

def main():
    # On lit N et M
    N, M = map(int, input().split())
    # On lit la liste A
    A = list(map(int, input().split()))
    # On lit M intervalles
    LR = []
    for _ in range(M):
        l, r = map(int, input().split())
        l -= 1  # On convertit en index 0-based
        r -= 1
        LR.append((l, r))
    # On trie la liste des segments LR
    LR.sort()
    # NG_left[i] indique depuis où on ne peut pas aller
    NG_left = [i for i in range(N)]
    index = 0
    for l, r in LR:
        for i in range(max(index, l), r + 1):
            NG_left[i] = l
            index = i + 1
    # Calcul dynamique
    dp = [0] * N
    dp[0] = A[0]
    for i in range(1, N):
        if NG_left[i] == 0:
            dp[i] = max(dp[i - 1], A[i])
        else:
            dp[i] = max(dp[i - 1], A[i] + dp[NG_left[i] - 1])
    print(dp[-1])

if __name__ == '__main__':
    main()