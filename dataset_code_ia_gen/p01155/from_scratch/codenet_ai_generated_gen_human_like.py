import math
import sys

def factor_pairs(n):
    pairs = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break

    a_factors = factor_pairs(a)
    b_factors = factor_pairs(b)

    min_sum = None
    for a1, a2 in a_factors:
        for b1, b2 in b_factors:
            seq = sorted([a1, a2, b1, b2])
            diff_sq_sum = (seq[1]-seq[0])**2 + (seq[2]-seq[1])**2 + (seq[3]-seq[2])**2
            if min_sum is None or diff_sq_sum < min_sum:
                min_sum = diff_sq_sum

    print(min_sum)