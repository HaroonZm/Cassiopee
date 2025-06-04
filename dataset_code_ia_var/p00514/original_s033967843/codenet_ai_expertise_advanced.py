from math import comb

n, m, r = map(int, input().split())
extra = r - m * n
print(0 if extra < 0 else comb(extra + n - 1, n - 1))