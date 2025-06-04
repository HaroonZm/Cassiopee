import sys
import itertools
from functools import partial

read = sys.stdin.buffer.read

N, M, *A = map(int, read().split())

def f(x, y, k):
    # Calcule le nombre de pas entre x et y avec décalage si besoin
    y_wrap = y + M * (x > y)
    k_wrap = k + M * (k <= x)
    if k_wrap <= y_wrap:
        return (y_wrap - k_wrap) + 1
    return y_wrap - x

A = [a - 1 for a in A]
pairs = zip(A, A[1:])

DDX = [0] * M
add_X = add_DX = 0

for x, y in pairs:
    a, b = f(x, y, M - 2), f(x, y, M - 1)
    add_X += b
    add_DX += b - a
    d = (y - x) % M
    DDX[(y + 1) % M] += d
    DDX[(y + 2) % M] -= (d - 1)
    DDX[(x + 2) % M] -= 1

it_acc = itertools.accumulate
DX = [add_DX + v for v in it_acc(DDX)]
X = [add_X + v for v in it_acc(DX)]

print(min(X))