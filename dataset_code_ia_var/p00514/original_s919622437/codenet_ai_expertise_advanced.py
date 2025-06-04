from math import comb
n, m, r = map(int, input().split())
a = r - n * m
print(comb(a + n - 1, a) if a >= 0 else 0)