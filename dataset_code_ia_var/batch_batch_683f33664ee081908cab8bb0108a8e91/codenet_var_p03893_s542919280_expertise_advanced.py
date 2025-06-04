from functools import lru_cache

x = int(input())

@lru_cache(maxsize=None)
def f(n):
    return 7 if n == 1 else (res := f(n - 1)) * 2 + 1

print(f(x) - 1)