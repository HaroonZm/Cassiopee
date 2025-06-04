from functools import lru_cache

MOD = 10**9 + 7

@lru_cache(maxsize=None)
def power(x: int, n: int, d: int = MOD) -> int:
    if n == 0:
        return 1
    if n % 2:
        return (power(x, n // 2, d) ** 2 * x) % d
    else:
        return pow(power(x, n // 2, d), 2, d)

def solve():
    m, n = map(int, input().split())
    print(power(m, n))

solve()