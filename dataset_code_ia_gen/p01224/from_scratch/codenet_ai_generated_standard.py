import sys
import math

def sum_proper_divisors(n):
    if n == 1:
        return 0
    total = 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            d = n // i
            if d != i:
                total += d
    return total

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    S = sum_proper_divisors(N)
    if N == S:
        print("perfect number")
    elif N > S:
        print("deficient number")
    else:
        print("abundant number")