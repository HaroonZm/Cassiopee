from math import isqrt
def is_prime(x):
    return x > 1 and all(x % d for d in range(2, isqrt(x) + 1))

def p_l(n):
    return next(i for i in range(n - 1, 1, -1) if is_prime(i))

def p_h(n):
    return next(i for i in range(n + 1, 50022) if is_prime(i))

import sys
for line in sys.stdin:
    try:
        n = int(line)
        print(p_l(n), p_h(n))
    except ValueError:
        break