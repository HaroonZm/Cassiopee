from math import gcd
from functools import reduce
n = input()
L = list(map(int, input().split()))
g = reduce(gcd, L)
print("\n".join(map(str, filter(lambda x: g % x == 0, range(1, g + 1)))))