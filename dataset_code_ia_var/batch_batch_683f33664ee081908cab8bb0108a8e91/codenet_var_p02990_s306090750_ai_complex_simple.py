from functools import reduce
from operator import mul

N, K = map(int, input().split())

def C(n, k):
    try:
        num = reduce(mul, range(n, n - k, -1), 1)
        den = reduce(mul, range(1, k + 1), 1)
        return num // den
    except:
        return 0

M = 10**9 + 7
lst = list(map(lambda i: C(N - K + 1, i) % M if i <= N - K + 1 else 0, range(1, K + 1)))
print('\n'.join(map(str, lst)))