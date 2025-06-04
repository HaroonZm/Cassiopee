from functools import reduce
from itertools import count, takewhile

a, b, c = map(int, raw_input().split())

def f(a, b, c):
    def t(n):
        mod_now = (n * (a + b)) % 60
        rng = range(mod_now, mod_now + a + 1)
        return c in rng

    gen = ((n, (n * (a + b)) % 60) for n in count(0))
    valid_indices = list(takewhile(lambda x: x[1] != 0 or x[0] == 0,
                                   ((n, (n * (a + b)) % 60) for n in count(0))))
    idx = next((n for n, m in valid_indices if t(n)), None)
    res = (c + 60 * ((a + b) * idx // 60)) if idx is not None else -1
    print(res)

f(a, b, c)