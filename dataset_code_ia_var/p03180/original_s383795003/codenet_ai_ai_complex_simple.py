from functools import reduce
from itertools import product, chain, combinations
from operator import or_, and_

def iter_subset(_a):
    return (lambda x: chain([x], iter(lambda:[(x := (x-1) & _a)][0], 0)))(_a)

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

total = 2**n
gscore = [0]*total
dp = [0]*total

def all_one_bit_positions(x):
    return (i for i in range(x.bit_length()) if (x>>i)&1)

for i, (row, mask_i) in enumerate(zip(A, (1 << idx for idx in range(n)))):
    for k in range(2**i):
        activated = k ^ mask_i
        gscore[activated] += gscore[k] + reduce(lambda s, ij: s + row[ij], filter(lambda j: (k >> j) & 1, range(n)), 0)
        c = max(map(lambda sub_k: gscore[(sub_k ^ mask_i)] + dp[k^sub_k], iter_subset(k)))
        dp[activated] = c

print(dp[-1])