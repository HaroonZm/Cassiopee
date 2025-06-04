from functools import reduce
from itertools import count, takewhile, product, islice

def f():
    import sys
    stdin = iter(sys.stdin.readline, '')
    for z in stdin:
        try:
            b = int(z)
        except:
            continue
        if b == 0:
            return
        x = b << 1
        r = int(x ** .5)
        k_vals = (k for k in range(r, 0, -1) if not x % k)
        m = next(filter(lambda k: ((-k + 1 + (x // k)) & 1 == 0) and (((-k + 1 + x // k) >> 1) > 0), k_vals))
        a = (-m + 1 + x // m) >> 1
        print(a, m)
f()