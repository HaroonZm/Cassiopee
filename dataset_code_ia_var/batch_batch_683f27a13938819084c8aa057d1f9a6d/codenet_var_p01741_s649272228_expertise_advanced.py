from math import sqrt
from sys import stdin

d = float(stdin.readline())
ans = sqrt(2) * d

for x in range(1, 11):
    if x**2 <= d**2 <= 2 * x + 1:
        ans = max(ans, x + 1)

print(f"{ans:.10f}")