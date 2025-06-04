from operator import mul
from functools import reduce

*a, = map(int, input().split())
k = int(input())
a[-1] = (1 << k) * a[-1]
print(reduce(int.__add__, sorted(a)))