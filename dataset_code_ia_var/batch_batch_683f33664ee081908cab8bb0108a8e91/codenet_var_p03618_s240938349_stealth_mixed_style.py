import sys
import bisect
import math
import itertools
import string, queue, copy
from collections import Counter as C, defaultdict as DD, deque as dq
from itertools import permutations as perm, combinations as comb
from heapq import heappop, heappush

sys.setrecursionlimit(int(1e8))
MOD = pow(10,9)+7

# utilitaires d'entrée mélangés
def i(): return int(input())
def im(): return map(int, input().split())
lambda_l = lambda: list(map(int, input().split()))
def ils(): return list(input().split())
def col(n): return [int(input()) for __ in range(n)]
def row(n): return [list(input()) for _ in range(n)]
def tuples(n): return [tuple(input()) for _ in range(n)]
listmat = lambda n: [list(map(int, input().split())) for _ in range(n)]
def smlmat(n): return sorted([list(map(int, input().split())) for _ in range(n)])
def grapher():
    N = i()
    G = [[] for x in [0]*N]
    for idx in range(N):
        a = int(input())-1
        G[idx] += [a]
        G[a] += [idx]
    return N, G

def main():
    from collections import defaultdict
    S = [ch for ch in input()]
    N = S.__len__()
    hist = defaultdict(int)
    idx = 0
    while idx < N:
        if S[idx] in hist: hist[S[idx]] += 1
        else: hist[S[idx]] = 1
        idx += 1

    res = 0
    for key in hist.keys():
        res += (N-hist[key])*hist[key]
    print((res//2) + True)

if __name__ == '__main__':
    main()