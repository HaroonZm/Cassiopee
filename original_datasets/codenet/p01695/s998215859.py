import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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
        n = I()
        if n == 0:
            break
        a = [S() for _ in range(n)] + ['']
        b = [0] * (n+1)
        for i in range(1,n):
            s = a[i]
            b[i] = len(s.split('.')) - 1
        r = [[c for c in t] for t in a[:n]]
        for i in range(n):
            t = b[i]
            if t == 0:
                continue
            r[i][t-1] = '+'
            ni = i
            for j in range(i+1,n):
                if b[j] < t:
                    break
                if b[j] == t:
                    ni = j
                    break
            for j in range(i+1,ni):
                r[j][t-1] = '|'
            for j in range(t-1):
                if r[i][j] == '.':
                    r[i][j] = ' '
        for c in r:
            rr.append(''.join(c))

    return '\n'.join(map(str, rr))

print(main())