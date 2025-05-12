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
    p = F()
    n = I()
    d = collections.defaultdict(list)
    for _ in range(n-1):
        x,y,c = LI()
        d[x-1].append((y-1,c))
        d[y-1].append((x-1,c))
    f = [None] * n
    f[0] = (0,0)
    q = [(0,0)]
    while q:
        x,b = q[0]
        q = q[1:]
        for y,c in d[x]:
            if f[y]:
                continue

            q.append((y,b+1))
            f[y] = (b+1, c)

    s = 0
    for b,c in f:
        s += p**b * c
    r = s
    for b,c in f:
        r += p**b * s
    return r

print(main())