from itertools import count
from math import log

def count_factors(n, p):
    if n < p:
        return 0
    total = 0
    denom = p
    while denom <= n:
        total += n // denom
        denom *= p
    return total

for N_str in iter(input, '0'):
    N = int(N_str)
    t2 = count_factors(N, 2)
    t5 = count_factors(N, 5)
    print(min(t2, t5))