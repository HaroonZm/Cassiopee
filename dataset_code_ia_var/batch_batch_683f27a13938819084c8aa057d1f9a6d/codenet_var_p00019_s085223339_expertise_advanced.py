from functools import cache

@cache
def f(n: int) -> int:
    return n * f(n - 1) if n else 1

print(f(int(input())))