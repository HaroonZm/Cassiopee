from functools import lru_cache

L, X = map(int, input().split())

@lru_cache(maxsize=None)
def h(l):
    return 1 if l == 0 else 2 * h(l - 1) + 3

@lru_cache(maxsize=None)
def f(l, x):
    if l == 0:
        return int(x > 0)
    if x == 0:
        return 0
    hl1 = h(l - 1)
    if x == 1:
        return 0
    elif x <= hl1 + 1:
        return f(l - 1, x - 1)
    elif x == hl1 + 2:
        return f(l - 1, hl1) + 1
    elif x <= 2 * hl1 + 2:
        return f(l - 1, hl1) + 1 + f(l - 1, x - hl1 - 2)
    else:
        return 2 * f(l - 1, hl1) + 1

print(f(L, X))