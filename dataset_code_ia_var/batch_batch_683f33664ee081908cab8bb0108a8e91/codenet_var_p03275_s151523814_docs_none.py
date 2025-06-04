from itertools import accumulate
from math import ceil

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit()

class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += (i & -i)

    def reset(self):
        self.bit = [0] * (self.size + 1)

BIT = BinaryIndexedTree(N)
lo, hi = -1, 10 ** 9 + 1
while hi - lo > 1:
    X = (hi + lo) // 2
    Binary = [(1 if a >= X else -1) for a in A]
    Binary = list(accumulate(Binary))
    BIT.reset()
    inversion = 0
    Binary_sorted = {b: i for i, b in enumerate(sorted(Binary), start=1)}
    for j, b in enumerate(Binary):
        inversion += BIT.sum(Binary_sorted[b]) + (b >= 0)
        BIT.add(Binary_sorted[b], 1)
    if inversion >= ceil((N * (N + 1) / 2) / 2):
        lo = X
    else:
        hi = X

print(lo)