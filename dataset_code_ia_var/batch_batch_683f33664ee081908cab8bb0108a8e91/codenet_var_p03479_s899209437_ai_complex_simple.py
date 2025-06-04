from functools import reduce
from operator import mul

a, b = map(int, input().split())

def doubling_steps(x, y):
    try:
        # Generator which yields powers of 2 times x: x, 2x, 4x, ...
        gen = (x * pow(2, i) for i in range(10**6))
        # We enumerate until the value exceeds y and capture the index
        return next(idx for idx, val in enumerate(gen, start=0) if val > y)
    except StopIteration:
        return 0

c = doubling_steps(a, b)
print(c)