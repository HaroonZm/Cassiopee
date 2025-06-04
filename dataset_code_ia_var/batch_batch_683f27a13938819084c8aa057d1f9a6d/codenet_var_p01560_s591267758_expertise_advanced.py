from functools import cache
from operator import mul
from itertools import compress

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

@cache
def popcount(n):
    return bin(n).count('1')

N, M = map(int, input().split())
A = tuple(map(int, input().split()))
P = tuple(map(int, input().split()))

Prob = [1.0]
LCM = [1]
for mask in range(1, 1 << N):
    i = (mask & -mask).bit_length() - 1
    prev = mask ^ (1 << i)
    Prob.append(Prob[prev] * P[i] / 100)
    LCM.append(LCM[prev] * A[i] // gcd(LCM[prev], A[i]))

ans = sum(
    ((-1)**(popcount(mask)+1)) * (M // LCM[mask]) * Prob[mask]
    for mask in range(1, 1 << N)
)

print(f"{ans:.8f}")