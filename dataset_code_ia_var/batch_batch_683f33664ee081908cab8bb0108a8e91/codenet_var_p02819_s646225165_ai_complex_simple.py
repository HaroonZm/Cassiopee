from functools import partial
from itertools import count, takewhile

def isprime(n):
    return not any(map(partial(lambda d, k: k % d == 0, k=n), takewhile(lambda x: x*x < n, count(2))))

x = int(input())
next(print(y) or None for y in count(x) if isprime(y))