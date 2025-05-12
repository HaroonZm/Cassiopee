import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

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
    n = I()
    a = [LS() for _ in range(n)]

    def f(s):
        r = 0
        c = 1
        for t in s:
            if t == 'm':
                r += c * 1000
                c = 1
            elif t == 'c':
                r += c * 100
                c = 1
            elif  t == 'x':
                r += c * 10
                c = 1
            elif t == 'i':
                r += c
                c = 1
            else:
                c = int(t)
        return r

    def g(i):
        r = ''
        if i >= 1000:
            k = i // 1000
            if k > 1:
                r += str(k)
            r += 'm'
            i %= 1000
        if i >= 100:
            k = i // 100
            if k > 1:
                r += str(k)
            r += 'c'
            i %= 100
        if i >= 10:
            k = i // 10
            if k > 1:
                r += str(k)
            r += 'x'
            i %= 10
        if i >= 1:
            k = i
            if k > 1:
                r += str(k)
            r += 'i'
        return r

    for s,t in a:
        rr.append(g(f(s)+f(t)))

    return '\n'.join(map(str, rr))

print(main())