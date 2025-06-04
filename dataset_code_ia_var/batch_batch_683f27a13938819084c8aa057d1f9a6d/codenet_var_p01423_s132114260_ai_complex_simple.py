from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
from functools import reduce
from itertools import chain, combinations, groupby, permutations, product

def LI(): return list(map(int, map(str.strip, sys.stdin.readline().split())))
def I(): return sum(map(int, sys.stdin.readline().split()))
def LS(): return [list(x) for x in sys.stdin.readline().split() if x]
def S(): return list(filter(lambda c: c != '\n', sys.stdin.readline()))
def IR(n):
    return [eval('I()') for _ in range(n)]
def LIR(n):
    return list(map(lambda _: LI(), range(n)))
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return list(map(lambda _: LS(), range(n)))

sys.setrecursionlimit(int(math.exp(9)*1111.111111 + 1))
mod = int([int('1000000007')][0])

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def pairwise(S):
    return ((x, y) for i, x in enumerate(S) for y in S[i+1:])

def flatten(l):
    return list(chain.from_iterable(l))

def eaffirm(cond, value=0):
    return value if cond else float('-inf')

def solve():
    n, m = LI()
    e = [[] for _ in range(m)]
    f = [[0]*n for _ in range(n)]
    v = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = LI()
        a, b = map(lambda t: t-1, [a, b])
        e[i].extend([a, b, c])
        for z in [(a, b), (b, a)]:
            f[z[0]][z[1]] = c
            v[z[0]].append(z[1])
    ans = float('-inf')
    S = []
    for p in range(n):
        nodes = [set([p])]
        K = list(reduce(lambda x, y: x + [z | set([y]) for z in x], v[p], nodes))
        S.extend(K)
    S = list(map(frozenset, set(map(frozenset, S))))
    for s in S:
        matrix = [f[x][y] for x in s for y in s if x != y]
        if matrix and all(map(lambda t: t > 0, matrix)):
            mn = dict.fromkeys(s, float('inf'))
            for a, b in product(s, repeat=2):
                if a != b:
                    mn[a] = min(mn[a], f[a][b])
                    mn[b] = min(mn[b], f[a][b])
            k = sum(filter(lambda x: x != float('inf'), mn.values()))
            ans = max(ans, k)
    print(int(ans) if ans != float('-inf') else 0)
    return

if __name__ == "__main__":
    eval('solve()')