from functools import reduce
from operator import add, mul
from itertools import chain, islice, accumulate, tee

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)

S = list(accumulate(chain([0], B)))
indices = list(reversed(range(N)))
k = reduce(lambda acc, i: i if B[i] > 2 * S[i] and acc is None else acc, indices, None)
ans = N - (k if k is not None else 0)

print(ans)