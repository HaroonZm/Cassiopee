from math import ceil

n, a, b, c, d = map(int, input().split())
options = [ceil(n / a) * b, ceil(n / c) * d]
print(min(options))