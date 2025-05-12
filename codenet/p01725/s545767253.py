import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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
    s = S()

    t = []
    k = 0
    kf = False
    for c in s:
        if '0' <= c <= '9':
            k *= 10
            k += int(c)
            kf = True
        else:
            if kf:
                t.append(k)
            k = 0
            t.append(c)
            kf = False
    if kf:
        t.append(k)

    def calc(a,b,o):
        if o == '+':
            return a + b
        if o == '-':
            return a - b
        return a * b

    def f(s, ops):
        t = s[:]
        ff = True
        while ff:
            ff = False
            ti = -1
            for i in range(len(t)-1,-1,-1):
                if t[i] == '(':
                    ti = i
                    break
            if ti < 0:
                break
            tj = -1
            for i in range(ti+1,len(t)):
                if t[i] == ')':
                    tj = i + 1
                    break
            t[ti:tj] = [f(t[ti+1:tj-1], ops)]
            ff = True

        for i in range(3):
            nt = []
            for c in t:
                if isinstance(c, int):
                    if len(nt) > 1 and ops[nt[-1]] == i:
                        kt = calc(nt[-2],c,nt[-1])
                        nt[-2] = kt
                        del nt[-1]
                    else:
                        nt.append(c)
                else:
                    nt.append(c)
            t = nt
        return t[0]

    r = -inf
    for a in itertools.product(range(3), repeat=3):
        tr = f(t, {'+': a[0], '-': a[1], '*': a[2]})
        if r < tr:
            r = tr

    return r

print(main())