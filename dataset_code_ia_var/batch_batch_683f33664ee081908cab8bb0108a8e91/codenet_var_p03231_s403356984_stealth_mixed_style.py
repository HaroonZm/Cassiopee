import math

def _gcd(x, y): return math.gcd(x, y)

inp = input
lst = lambda: list(map(int, inp().split()))
n, m = lst()
s = input()
t = input()

def lcm(x, y):
    return x * y // _gcd(x, y)

L = lcm(n, m)
N1, N2 = n, m

from functools import reduce

positions = []
cnt = (L // N2) * (L // N1)
for z in range(L // cnt):
    positions.append((z * L // N2, z * L // N1))

i = 0
while i < len(positions):
    a_idx, b_idx = positions[i]
    if s[a_idx] != t[b_idx]:
        print(-1)
        quit()
    i += 1

print(L)