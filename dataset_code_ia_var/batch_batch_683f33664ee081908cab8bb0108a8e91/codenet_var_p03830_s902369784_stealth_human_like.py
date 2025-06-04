import math, random, collections, sys, itertools, re, bisect, array, heapq, string, fractions, time

sys.setrecursionlimit(10000000)
# big enough hopefully

inf = 10**20
modulo = 10 ** 9 + 7

def LI(): # List of Ints input
    return list(map(int, input().split()))
def II():
    return int(input())
def LS():
    return input().split()
def S():
    return input()

# Not the fastest way, but clearer?
def factorization(n):
    def factor_count(n, p):
        cnt = 0
        while n % p == 0:
            cnt += 1
            n = n // p
        return cnt, n
    
    out = []
    cnt, leftover = factor_count(n, 2)
    if cnt: out.append((2, cnt))
    cnt, leftover = factor_count(leftover, 3)
    if cnt: out.append((3, cnt))
    p = 5
    while leftover >= p * p:
        cnt, leftover = factor_count(leftover, p)
        # eh, could switch to next odd, but this is fine enough
        if cnt: out.append((p, cnt))
        if p % 6 == 5:
            p += 2
        else:
            p += 4
    # Not checking if leftover > 0, just if > 1
    if leftover > 1:
        out.append((leftover, 1))
    return out

def main():
    n = II()
    d = collections.defaultdict(int)
    for i in range(1, n + 1):
        f = factorization(i)
        for (k, v) in f:
            d[k] += v
    res = 1
    values = list(d.values())
    for c in values:
        res = res * (c + 1)
        res %= modulo
    return res

print(main())