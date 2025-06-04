from math import ceil
from itertools import product
from operator import mul

N = int(input())
P = tuple(map(int, input().split()))
T = tuple(map(int, input().split()))

limits = [ceil(N / t) for t in T]
ans = float('inf')

for i, j, k in product(*(range(l + 1) for l in limits[:3])):
    rem = N - i * T[0] - j * T[1] - k * T[2]
    l = max(0, ceil(rem / T[3]))
    cost = sum(map(mul, (i, j, k, l), P))
    ans = min(ans, cost)

print(ans)