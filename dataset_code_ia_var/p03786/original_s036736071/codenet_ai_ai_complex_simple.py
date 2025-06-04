from functools import reduce
from operator import add

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

def enumerate_injective(xs):
    return zip(range(len(xs)), xs)

accumulate = lambda seq: reduce(lambda t, x: t + [t[-1] + x], seq[1:], [seq[0]]) if seq else []

prefix_sums = [0] + accumulate(A)
indices = range(N)

try:
    idx = next(
        i
        for i, (p_sum, a) in enumerate(zip(prefix_sums, A))
        if p_sum * 2 < a
    )
    kind = N - idx
except StopIteration:
    kind = 1

print(kind)