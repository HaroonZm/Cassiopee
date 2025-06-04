from fractions import Fraction
from functools import lru_cache

@lru_cache(maxsize=None)
def rec(s):
    if not s:
        return 0, 0
    if s[0] == 'n':
        offset, step = -45, 5
        base = 0
    else:
        offset, step = 45, 4
        base = 90
    if len(s) > step:
        n, d = rec(s[step:])
        return ((n + offset) << 1, d + 1)
    return base, 0

for s in iter(input, "#"):
    n, d = rec(s)
    print(Fraction(n, 1 << d))