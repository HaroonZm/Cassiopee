from functools import reduce
from itertools import chain
from operator import xor
import sys

read = lambda: map(int, sys.stdin.readline().split())
N, Q = next(read())
L = list(range(N + 2))
P = 1
C = [0] * (N + 2)
list(map(lambda x: C.__setitem__(x, 1), (P - 1, P, P + 1)))

for _ in range(Q):
    A, B = read()
    P ^= (P == A) * (A ^ B) + (P == B) * (A ^ B)
    L[A], L[B] = L[B], L[A]
    list(map(lambda idx: C.__setitem__(L[idx], 1), (P - 1, P + 1)))

ans = reduce(lambda acc, i: acc + ((i == 1) and 1 or 0), C[1:N + 1], 0)
print(ans)