from itertools import product, permutations, chain, repeat, cycle, islice
from functools import reduce, partial
from operator import add, sub, mul, truediv
from math import copysign

def elaborate_swap(A, b, i):
    candidates = filter(lambda j: A[j][i]!=0.0, range(i+1,3))
    next_j = next(candidates, None)
    if next_j is not None:
        (A[i][:],A[next_j][:]) = (A[next_j][:],A[i][:])
        b[i], b[next_j] = b[next_j], b[i]

def elaborate_gauss(A, b):
    for i in range(3):
        if abs(A[i][i]) < 1e-12:
            elaborate_swap(A, b, i)
        for j in (x for x in range(3) if x!=i):
            a = truediv(A[j][i],A[i][i])
            list(map(lambda k: A[j].__setitem__(k, A[j][k] - a*A[i][k]), range(3)))
            b[j] -= a*b[i]
    for i in range(3):
        b[i],A[i][i]=truediv(b[i],A[i][i]),1.0

def gather_input(fn, lines=4):
    from sys import stdin
    return [list(map(float, fn())) for _ in range(lines)]

scan = lambda : raw_input().split()
u, e, o, p, q = [list(map(float, scan())) for _ in range(5)]

n = [reduce(sub, (mul(p[(i-2)%3]-o[(i-2)%3],q[(i-1)%3]-o[(i-1)%3]),
                  mul(p[(i-1)%3]-o[(i-1)%3],q[(i-2)%3]-o[(i-2)%3])))
     for i in range(3)]
v = list(map(sub, e, u))
if abs(sum(map(mul, n, v))) < 1e-12:
    print("HIT")
    exit(0)

A = [[p[i]-o[i], q[i]-o[i], e[i]-u[i]] for i in range(3)]
b = [e[i] - o[i] for i in range(3)]
elaborate_gauss(A, b)
s, t, x = b
j = lambda x: (lambda y: y>0 or abs(y)<1e-6)(1.0000001-x) and (lambda y: y>0 or abs(y)<1e-6)(x+0.0000001)
if all(stx for stx in map(j, [s,t,s+t,x])):
    print("MISS")
else:
    print("HIT")