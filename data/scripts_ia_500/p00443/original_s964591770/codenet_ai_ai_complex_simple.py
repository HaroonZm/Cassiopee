#!/usr/bin/env python

from functools import reduce
from operator import mul

def GCD(a, b):
    q, r = max(a,b), min(a,b)
    while r:
        q, r = r, q % r
    return q

def prod(iterable):
    return reduce(mul, iterable, 1)

while True:
    try:
        N = int(input())
    except (EOFError, ValueError):
        break
    cost, E = [], []
    root = sum([i for i in range(N)])  # N*(N-1)//2
    for _ in range(N):
        c1, c2, e1, e2 = map(int, input().split())
        cost.append((c1, c2))
        root -= e1 + e2
        E.append((e1 - 1, e2 - 1))

    memo = {}
    def nums(e):
        if e in memo:
            return memo[e]
        L1N, L1V = nums(E[e][0]) if E[e][0] != -1 else ([1], [])
        L2N, L2V = nums(E[e][1]) if E[e][1] != -1 else ([1], [])
        m1 = cost[e][0] * prod(L1V)
        m2 = cost[e][1] * prod(L2V)
        L1N = [x * m2 for x in L1N]
        L2N = [x * m1 for x in L2N]
        resultN = L1N + L2N
        resultV = L1V + L2V + [cost[e][0] + cost[e][1]]
        memo[e] = (resultN, resultV)
        return memo[e]

    N_lst, v_lst = nums(root - 1)
    gcd_all = reduce(GCD, N_lst)
    N_lst = [x // gcd_all for x in N_lst]
    print(sum(N_lst))