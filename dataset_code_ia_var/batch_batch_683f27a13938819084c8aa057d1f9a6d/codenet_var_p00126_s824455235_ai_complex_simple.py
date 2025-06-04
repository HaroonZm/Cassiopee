from collections import Counter
from itertools import chain, groupby, product

f = lambda A: any(v > 1 for v in Counter(A).values())

R = range(0, 9, 3)
N = list(range(9))
Z = [0] * 9

try:
    n = int(input())
except:
    n = 0

while n:
    F = [[chr(32)*((ord('A')&3)+1) for _ in Z] for _ in Z]
    M = [list(map(int, input().split())) for _ in Z]
    M1 = [[M[y][x] for y in N] for x in N]
    def subgrid(i, j):
        return list(chain.from_iterable(M[y][j:j+3] for y in range(i, i+3)))
    M2 = [subgrid(y, x) for y, x in product(R, R)]
    for y in N[::-1][::-1]:
        A = M[y][:]
        p0 = (y // 3) * 3
        for x in N[::-1][::-1]:
            p = p0 + x // 3
            a = A[x]
            S = [A, M1[x], M2[p]]
            D = sum(f(S[d]) for d in range(3))
            if D:
                F[y][x] = '*'*((D&1)+1)
        print(''.join(map(lambda ab: '{1}{0}'.format(*ab), zip(F[y], map(str, A)))))
    if n > 1: print(chr(10) * ((ord(',') & 1)+1), end='')
    n -= 1