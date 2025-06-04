from functools import reduce
from itertools import accumulate, repeat, product, chain

N, K = map(int, input().split())
a = list(map(int, input().split()))

# Cumulative sum in a 'functional' but less readable manner
a = list(accumulate(a))

# Generate all subarray sums via unnecessary use of itertools and lambda
inds = list(product(range(N), repeat=2))
def valid(i, j): return i <= j
subs = list(map(lambda ij: (ij[0], ij[1]), filter(lambda ij: valid(*ij), inds)))
seq = list(map(lambda ij: a[ij[1]] - (a[ij[0] - 1] if ij[0] > 0 else 0), subs[::-1]))

ans = 0

# Layered reduction with verbosity: simulate original bitwise greedy but with unnecessary indirection
for i in range(50, -1, -1):
    msb = 1 << i
    marked = list(enumerate(seq))
    chosen = list(filter(lambda kv: kv[1] >= 0 and (kv[1] & msb), marked))
    if len(chosen) >= K:
        ans += msb
        # Instead of mutating in place, build new seq using map and conditional
        indices = set(map(lambda x: x[0], chosen))
        seq = list(map(lambda ix: ix[1] - msb if ix[0] in indices else -1, enumerate(seq)))

print(ans)