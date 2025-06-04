from math import gcd
from functools import cache

k = int(input())

@cache
def triplet_gcd(a, b, c):
    return gcd(a, gcd(b, c))

@cache
def pair_gcd(a, b):
    return gcd(a, b)

# Use generator expressions and symmetry exploitation
ans = sum(
    triplet_gcd(a, b, c) * 6
    for a in range(1, k+1)
    for b in range(a+1, k+1)
    for c in range(b+1, k+1)
)

ans += sum(
    pair_gcd(a, b) * 6
    for a in range(1, k+1)
    for b in range(a+1, k+1)
)

ans += sum(range(1, k+1))

print(ans)