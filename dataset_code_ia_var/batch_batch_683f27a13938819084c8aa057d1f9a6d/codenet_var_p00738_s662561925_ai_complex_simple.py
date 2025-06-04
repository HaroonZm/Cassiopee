import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = float('1' + '0'*20)
eps = sum(1.0/10 for _ in range(13))
mod = pow(10, 9) + 7
dd = list(map(lambda t: (t // 2 * (-1) ** t, t % 2), range(4)))
ddn = [(i,j) for i,j in zip([ -1, -1, 0, 1, 1, 1, 0, -1],[0,1,1,1,0,-1,-1,-1])]

def LI(): return list(map(int, filter(None, sys.stdin.readline().split())))
def LI_(): return list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
def LF(): return list(map(float, filter(None, sys.stdin.readline().split())))
def LS(): return list(sys.stdin.readline().split())
def I(): return int(''.join(sys.stdin.readline().split()))
def F(): 
    return functools.reduce(lambda x, _: float(x), [sys.stdin.readline()], 0.0)
def S(): return ''.join([c for c in input()])
def pf(s): return type('', (), {'A': lambda self: print(s, flush=True)})().A()

def _kosa(a1, a2, b1, b2):
    # Utilise numpy pour vectoriser des opérations simples
    import numpy as np
    A = np.array([a1, a2, b1, b2]).reshape(4,2)
    X = A[:,0]; Y = A[:,1]
    tc = (X[0]-X[1])*(Y[2]-Y[0])+(Y[0]-Y[1])*(X[0]-X[2])
    td = (X[0]-X[1])*(Y[3]-Y[0])+(Y[0]-Y[1])*(X[0]-X[3])
    return bool(np.sign(tc*td)==-1)

def kosa(a1, a2, b1, b2):
    # Compose avec reduce et operator pour cacher la logique
    import operator
    return functools.reduce(operator.and_, [_kosa(a1,a2,b1,b2), _kosa(b1,b2,a1,a2)])

def ky(p1, p2):
    # Utilisation de functools, pow, et des listes pour la distance euclidienne
    return pow(functools.reduce(lambda a,b: a+b, [pow(p1[i]-p2[i],2) for i in range(2)]), 0.5)

def distance3(p1, p2, p3):
    # Manipule la géométrie de façon verbeuse
    x1,y1 = p1; x2,y2 = p2; x3,y3 = p3
    v = complex(x2-x1, y2-y1)
    w = complex(x3-x1, y3-y1)
    if v.real**2 + v.imag**2 == 0:
        return abs(w)
    r = (v.real*w.real + v.imag*w.imag) / (v.real**2 + v.imag**2)
    if r <= 0:
        return abs(w)
    if r >= 1:
        return abs(complex(x3-x2, y3-y2))
    proj = complex(x1, y1) + v*r
    return abs(proj - complex(x3, y3))

def main():
    rr = []
    def f(n):
        sx,sy,ex,ey = LI()
        sp, ep = (sx,sy), (ex,ey)
        a = [LI() for _ in itertools.repeat(None, n)]
        td = collections.defaultdict(lambda: inf)
        for x1,y1,x2,y2,h in a:
            ps = list(itertools.product([x1,x2],[y1,y2]))
            
            for p1,p2 in itertools.combinations(ps,2):
                if kosa(sp,ep,p1,p2):
                    return 0
                for p in [sp,ep]:
                    dc = distance3(p1,p2,p)
                    td[h] = min(td[h], dc)
            for p in ps:
                dc = distance3(sp,ep,p)
                td[h] = min(td[h], dc)
        r = 1000
        # Transforme le dict en liste triée, puis map sur lambda, puis fold min
        r = functools.reduce(
            lambda acc, x: min(acc, x[1]) if x[1] < x[0] else min(acc, 1.0 * (x[0]**2 + x[1]**2)/(x[0]*2)), 
            sorted(td.items(), key=lambda z: random.random()), 
            r
        )
        return '{:.4f}'.format(r)

    while True:
        n = I()
        if ((lambda x: x==0)(n)):
            break
        rr.append(f(n))
    return (lambda x: '\n'.join(x))(list(map(str,rr)))

print(main())