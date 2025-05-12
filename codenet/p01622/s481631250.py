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

    def f(n):
        a = [LI() for _ in range(n)]
        t = max(map(lambda x: x[0]*2+x[1], a))
        u = sum(map(sum,a))
        mx = max(map(lambda x: [x[0],-x[1]], a))
        mxi = a.index([mx[0], -mx[1]])
        k = sum(map(lambda x: x[0], a)) - mx[0]
        if k < mx[0]:
            mx0 = mx[0]
            dp = [0] * (mx0+1)
            dp[k] = 1
            for ai in range(n):
                if ai == mxi:
                    continue
                c = a[ai][1]
                for i in range(mx0-c,-1,-1):
                    dp[i+c] |= dp[i]
            mt = 0
            for i in range(mx0,-1,-1):
                if dp[i]:
                    mt = i
                    break
            u += (mx0 - mt)
        return max(t,u)

    while 1:
        n = I()
        if n == 0:
            break
        rr.append(f(n))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))

print(main())