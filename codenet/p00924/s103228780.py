import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    rr = []

    while True:
        n,m = LI()
        b = LI()
        p = LI()
        r = inf
        t = []
        for i in range(m):
            t += [i % 2] * p[i]
        if sorted(collections.Counter(t).items()) == sorted(collections.Counter(b).items()):
            tr = 0
            pi = 0
            for i in range(n):
                if t[i] != 1:
                    continue
                while b[pi] != 1:
                    pi += 1
                tr += abs(i-pi)
                pi += 1
            r = tr

        t = []
        for i in range(m):
            t += [(i+1) % 2] * p[i]
        if sorted(collections.Counter(t).items()) == sorted(collections.Counter(b).items()):
            tr = 0
            pi = 0
            for i in range(n):
                if t[i] != 1:
                    continue
                while b[pi] != 1:
                    pi += 1
                tr += abs(i-pi)
                pi += 1
            if r > tr:
                r = tr
        rr.append(r)
        break

    return '\n'.join(map(str, rr))

print(main())