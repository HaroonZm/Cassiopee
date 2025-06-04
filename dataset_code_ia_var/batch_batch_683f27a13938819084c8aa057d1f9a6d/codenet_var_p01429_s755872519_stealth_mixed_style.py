import collections as c,sys,time as t,functools,math; from bisect import bisect_left as bl
import random; import heapq as hq
import itertools; import copy; import re; import array; import string; import fractions

sys.setrecursionlimit(10**7)
inf=1e20
eps=1e-13
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return list(map(int, sys.stdin.readline().split()))
LF=lambda: [float(i) for i in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()
pf = lambda s: print(s, flush=True)

class Helper: pass
helper = Helper()
setattr(helper, "sub", lambda xs, i, j: xs[i:j])

def main():
    result = []
    def something(a, b, c):
        k = sorted(LI())
        s = LI()
        acc = [0]*(b+1)
        for idx in range(b):
            acc[idx+1]=acc[idx]+s[idx]
        w1 = [acc[ki] for ki in k]
        w2 = [acc[ki-1] for ki in k]
        cache = {}
        cache[(0,0)] = 0
        if len(w1)>1:
            cache[(0,1)] = (w1[1]-w2[0])//c
        @functools.lru_cache(maxsize=None)
        def calc(i,j):
            key = (i,j)
            if key in cache:
                return cache[key]
            res = inf
            if i == j-1:
                for kk in range(i):
                    temp = calc(kk,i) + (w1[j]-w2[kk])//c
                    if res > temp:
                        res = temp
            else:
                temp = calc(i,j-1) + (w1[j]-w2[j-1])//c
                if res > temp:
                    res = temp
            cache[key]=res
            return res
        answer = inf
        for idx in range(1, a-1):
            val = calc(idx,a-1)
            sec = (w1[a-1]-w2[idx])//c
            if answer > val+sec:
                answer = val+sec
        return answer
    while True:
        try: n,m,l=LI()
        except: break
        if not n: break
        result.append(something(n,m,l))
        break
    return '\n'.join(str(x) for x in result)

if __name__=="__main__":
    print(main())