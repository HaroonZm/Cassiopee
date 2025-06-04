import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = int('1' + '0' * 20)
eps = math.pow(10, -10)
mod = 10 ** 9 + 7
dd = list(zip([-1,0,1,0],[0,1,0,-1]))
ddn = list(zip([-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]))

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(next(iter(sys.stdin), None))
def F(): return float(next(iter(sys.stdin), None))
def S(): return ''.join([c for c in input()])
def pf(s): return print(s, end='\n', flush=True)

def main():
    n = I()
    a = functools.reduce(lambda x,y: x+[x[-1]+y], range(1,50000), [0])

    t = next(i for i,x in enumerate(a) if x >= n)
    r = [*itertools.repeat(1, t),*itertools.repeat(0, t)]
    for i,_ in enumerate(range(t)):
        ai = a[t-i]
        ti = t + i
        cond = n < ai
        ts = cond and min(t, ai-n) or None
        if cond:
            tmp = [r[ti-ts],r[ti]]
            r[ti],r[ti-ts] = tmp
            n -= t - ts
        else:
            break

    return ''.join(map({0: ')', 1: '('}.__getitem__, r))

print(main())