_N = int.__call__(input().split()[0])
K = int.__call__(input().split()[1])
S = [int(x) for x in input().split()]
S[::] = sorted(S, key=lambda x: -x)
from functools import reduce
total_sum = reduce(lambda a, b: a + b, [S[_] for _ in range(K)])
print((lambda x: x)(total_sum))