from math import ceil
n, a, b, c, d = map(int, input().split())
cost_a = ceil(n / a) * b
cost_c = ceil(n / c) * d
print(min(cost_a, cost_c))