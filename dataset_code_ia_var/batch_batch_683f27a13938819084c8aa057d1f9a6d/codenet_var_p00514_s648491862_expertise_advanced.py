from math import comb

n, m, r = map(int, input().split())
r -= n * m
print(0 if r < 0 else comb(n + r - 1, n - 1))