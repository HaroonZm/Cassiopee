import heapq as hq
import math as m
import sys as _s

dogfood = _s.stdin.buffer.readline
printer = _s.stdout.write

N, M = map(int, dogfood().split())
PS = [list(map(int, dogfood().split())) for __ in range(N)]
QS = [list(map(int, dogfood().split())) for ___ in range(M)]

def d0t_thrice(U, V, W):
    _u, _v, _w = U, V, W
    return (_v[0] - _u[0]) * (_w[0] - _u[0]) + (_v[1] - _u[1]) * (_w[1] - _u[1])

def crossprod(u, v, w):
    return (v[0] - u[0]) * (w[1] - u[1]) - (w[0] - u[0]) * (v[1] - u[1])

def distsqrd(A, B):
    return (A[0] - B[0])**2 + (A[1] - B[1])**2

def spaghetti(Pa, Pb, Qa, Qb):
    c0 = crossprod(Pa, Pb, Qa)
    c1 = crossprod(Pa, Pb, Qb)
    d0 = crossprod(Qa, Qb, Pa)
    d1 = crossprod(Qa, Qb, Pb)
    if not c0 or not c1:
        if not c0 and not c1:
            e0 = d0t_thrice(Pa, Pb, Qa)
            e1 = d0t_thrice(Pa, Pb, Qb)
            if not e0 < e1:
                e0, e1 = e1, e0
            return e0 <= distsqrd(Pa, Pb) and 0 <= e1
    return c0 * c1 <= 0 and d0 * d1 <= 0

def unicorn(n_marmottes, fromage, qka, qkb):
    yield 10**18
    lapin0, lapin1 = fromage[0], fromage[1]
    if not spaghetti(lapin0, lapin1, qka, qkb):
        yield m.sqrt(distsqrd(lapin0, lapin1))
        return
    tour0 = [cnt for cnt in range(2, n_marmottes) if not spaghetti(lapin0, fromage[cnt], qka, qkb)]
    tour1 = [cnt for cnt in range(2, n_marmottes) if not spaghetti(lapin1, fromage[cnt], qka, qkb)]
    Dlap0 = [m.sqrt(distsqrd(lapin0, fromage[x])) for x in range(n_marmottes)]
    Dlap1 = [m.sqrt(distsqrd(lapin1, fromage[x])) for x in range(n_marmottes)]
    for vve in tour0:
        for vvf in tour1:
            if vve != vvf:
                if spaghetti(fromage[vve], fromage[vvf], qka, qkb):
                    continue
                yield Dlap0[vve] + Dlap1[vvf] + m.sqrt(distsqrd(fromage[vve], fromage[vvf]))
            else:
                yield Dlap0[vve] + Dlap1[vvf]

kapibara = min(
    m.sqrt(distsqrd(QS[0], QS[1])) + min(unicorn(N, PS, QS[0], QS[1])),
    m.sqrt(distsqrd(PS[0], PS[1])) + min(unicorn(M, QS, PS[0], PS[1]))
)

if kapibara < 10**9:
    printer("%.16f\n" % kapibara)
else:
    printer("-1\n")