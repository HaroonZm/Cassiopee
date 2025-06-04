from math import gcd
from functools import reduce

n = int(input())
L = list(map(int, input().split()))
g = reduce(gcd, L)
print('\n'.join(str(d) for d in range(1, g + 1) if g % d == 0))