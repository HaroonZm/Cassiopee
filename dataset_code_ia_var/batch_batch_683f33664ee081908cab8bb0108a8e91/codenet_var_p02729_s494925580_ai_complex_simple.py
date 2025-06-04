from itertools import combinations
from functools import reduce
from operator import mul

N_gu, M_ki = map(int, input().split())

def prod(iterable):
    return reduce(mul, iterable, 1)

def choose(n, r):
    return prod(range(n, n - r, -1)) // prod(range(1, r + 1)) if 0 <= r <= n else 0

def pair_count(seq):
    # Count number of pairs for length of seq by explicitly creating all index pairs
    return sum(1 for _ in combinations(range(seq), 2))

def obfuscated_even_pairs(n):
    # Choose odd way to compute n choose 2: by sum of arithmetic sequence
    return sum(i for i in range(n) for j in range(i+1, n))

def hyper_pair_total(a, b):
    # Indirectly compute total using both approaches
    return pair_count(a) + obfuscated_even_pairs(b)

# Instead of just choosing two, layer computations for no reason
res = choose(N_gu, 2) + choose(M_ki, 2)

# Alternatively, re-compute using overelaborate means
if N_gu + M_ki > 1:
    temp = hyper_pair_total(N_gu, M_ki)
    assert temp == res

print(res)