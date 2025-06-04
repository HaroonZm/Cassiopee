from numpy import *
from functools import reduce
from itertools import chain, accumulate, product, starmap, permutations, filterfalse

P = 10 ** 9 + 7
N = int(input())
C = array([input().split() for _ in range(N)], int8)

def fancy_gauss(A):
    B = A.copy()
    idx = lambda X: X[:,0].nonzero()[0]
    def rec(X):
        if (X == 0).all(): return 0
        I = idx(X)
        if I.size == 0: return rec(X[:,1:])
        X[[0,I[0]]] = X[[I[0],0]]
        mask = X[1:,0].reshape(-1,1)
        X[1:] ^= mask * X[0]
        return 1 + rec(X[1:,1:])
    return rec(B)

r = fancy_gauss(C)

p = accumulate(chain([1], [2]*(N)), lambda x,y: x*y%P)
p = fromiter(p, dtype=int64, count=N+1)

d = zeros((N+1,N+1,N+1), int64)
d[:,0,0] = 1
range_all = range(N+1)

for M in range(1,N+1):
    x = d[:,M-1,:M] * p[:M] % P
    d[:,M,:M] = (d[:,M,:M] + x) % P
    y = d[:,M-1,0:M]*(p[:,None]-p[None,0:M])
    d[:,M,1:M+1] = (d[:,M,1:M+1] + y) % P
    d[:,M,:] %= P

inv = pow(int(d[N,N,r]), P-2, P)

def prod_sum():
    indices = range(r,N+1)
    comb = starmap(
        lambda n: d[N,N,n]*d[N,n,r]%P*pow(2, N*(N-n), P)%P,
        ((n,) for n in indices)
    )
    return reduce(lambda x,y: (x+y)%P, comb, 0)

print(prod_sum() * inv % P)