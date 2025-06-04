from functools import lru_cache
import sys

sys.setrecursionlimit(1 << 20)
MOD = 10 ** 9 + 7

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

@lru_cache(maxsize=None)
def dfs(mask, cnt):
    if mask == (1 << N) - 1:
        return 1
    # Utilisation intelligente de bit_count (dispo Python 3.10+), sinon cnt est donné comme argument
    res = sum(
        dfs(mask | (1 << i), cnt + 1)
        for i, v in enumerate(A[cnt])
        if not (mask >> i) & 1 and v
    )
    return res % MOD

print(dfs(0, 0))