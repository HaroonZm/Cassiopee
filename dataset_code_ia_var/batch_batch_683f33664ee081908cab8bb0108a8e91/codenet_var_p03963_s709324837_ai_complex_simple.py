from functools import reduce
from operator import mul

n, k = map(int, input().split())

def prod(seq):
    return reduce(mul, seq, 1)

print(prod([k] + [(k-1)] * (n-1)))