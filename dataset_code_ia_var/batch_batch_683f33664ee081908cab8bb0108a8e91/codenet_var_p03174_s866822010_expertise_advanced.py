from functools import lru_cache
from sys import stdin

n = int(stdin.readline())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
mod = 10 ** 9 + 7

@lru_cache(maxsize=None)
def dp(mask):
    if mask == 0:
        return 1
    i = bin(mask).count('1') - 1
    return sum(dp(mask ^ (1 << j)) for j in range(n) if (mask & (1 << j)) and a[i][j]) % mod

print(dp((1 << n) - 1))