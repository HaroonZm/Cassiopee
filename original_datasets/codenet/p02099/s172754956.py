import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()

def main():
    n = I()
    a = sorted([[F(),_] for _ in range(n)])
    r = [0] * n
    ct = collections.defaultdict(int)
    for f,i in a:
        ct[f] += 1
    m = -1
    mi = 0
    for ai in range(n):
        c,i = a[ai]
        if m < c:
            m = c
            mi = ai
        r[i] = mi*3 + ct[c] - 1
    return '\n'.join(map(str,r))

print(main())