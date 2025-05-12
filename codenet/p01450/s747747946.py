import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

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

    def f(n,w):
        a = sorted([I() for _ in range(n)], reverse=True)
        dp = [0] * (w+1)
        dp[0] = 1
        sm = sum(a)
        if sm <= w:
            return 1
        r = 0
        for c in a:
            sm -= c
            if w >= sm:
                r += sum(dp[max(0,w-sm-c+1):w-sm+1])
                r %= mod
            for j in range(w-c,-1,-1):
                dp[j+c] += dp[j]
                dp[j+c] %= mod
        return r % mod

    while 1:
        n,m = LI()
        if n == 0:
            break
        rr.append(f(n,m))
        break

    return '\n'.join(map(str,rr))

print(main())