from functools import reduce
from operator import mul

def pairwise_sum(x):
    return (lambda y: reduce(mul, y, 1)//2)([x, x-1])

n, m = map(int, input().split())
res = (
    0 if all([n == 1, m == 1]) else
    pairwise_sum(m)*(n == 1) +
    pairwise_sum(n)*(m == 1) +
    ((pairwise_sum(n) + pairwise_sum(m)) * (n != 1 and m != 1))
)
print(res)