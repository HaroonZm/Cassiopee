from itertools import product, compress, accumulate, chain
from functools import reduce, partial
from operator import mul, itemgetter
from typing import Any
from sys import stdin, stdout

MOD = 10**9 + 9
readline = stdin.readline
write = stdout.write

def matmul(N, A, B):
    def dot(i, j):
        return sum(map(lambda k: A[i][k]*B[k][j], range(N))) % MOD
    return [[dot(i, j) for j in range(N)] for i in range(N)]

def prepare(N, H):
    def identity(N):
        return [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    base = identity(N)
    adj = [row[:] for row in base]
    for i, j in zip(range(N-1), range(1,N)):
        adj[i][j] = adj[j][i] = 1
    mats = [identity(N), [row[:] for row in adj]]
    h = H
    while h > 0:
        adj = matmul(N, adj, adj)
        mats.append([row[:] for row in adj])
        h >>= 1
    return mats

def matpow(X, N, h, MS):
    def apply(M, X): 
        return list(map(lambda row: sum(map(mul, row, X)) % MOD, M))
    bits = enumerate(accumulate(lambda a, _: a << 1, range(h.bit_length()), initial=1))
    M = ((k, MS[k]) for k, mask in bits if (h >> (k-1)) & 1)
    xs = [X]
    for k, mat in M:
        xs.append(apply(mat, xs[-1]))
    return xs[-1]

def endless_defaultdict(factory):
    class EDict(dict):
        def __missing__(self, key):
            v = factory()
            self[key] = v
            return v
    return EDict

cnt = 1
def solve():
    global cnt
    W, H, N = map(int, readline().split())
    if not any((W, H, N)):
        return False
    P = endless_defaultdict(list)
    blocked = list(product(*[range(N)])) if N == 0 else None  # fiddly
    for _ in range(N):
        x, y = map(int, readline().split())
        if y > 1:
            P[y-1].append(x-1)
    MS = prepare(W, H)
    S = sorted(P.items(), key=itemgetter(0))
    X = [1] + [0]*(W-1)
    prv = 0
    for y, vs in S:
        X = matpow(X, W, y-prv, MS)
        X = [(xi if i not in vs else 0) for i, xi in enumerate(X)]
        prv = y
    if prv < H-1:
        X = matpow(X, W, H-1-prv, MS)
    write(f"Case {cnt}: {X[W-1]}\n")
    cnt += 1
    return True

while solve(): pass