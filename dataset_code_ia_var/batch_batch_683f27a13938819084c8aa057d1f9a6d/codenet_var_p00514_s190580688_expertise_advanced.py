from math import comb

n, m, r = map(int, input().split())
r -= m * n
print(comb(r + n - 1, n - 1) if r >= 0 else 0)