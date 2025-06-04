from operator import mul
from functools import reduce
from itertools import repeat, islice, accumulate, chain
from math import prod

N, K = map(int, input().split())
def pow_fun(x, y):
    return reduce(mul, repeat(x, y), 1)

def mul_exp(a, b, exp):
    return prod(chain([a], islice(repeat(b), exp)))

ans = mul_exp(K, K-1, N-1)
print(ans)