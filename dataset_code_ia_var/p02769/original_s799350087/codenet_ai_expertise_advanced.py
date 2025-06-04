import math
from functools import reduce
from collections import deque
import sys

sys.setrecursionlimit(10**7)

from typing import Iterator

def get_nums_l() -> list[int]:
    return list(map(int, input().split()))

def get_nums_n(n: int) -> list[int]:
    return [int(input()) for _ in range(n)]

def get_all_int() -> Iterator[int]:
    return map(int, sys.stdin.read().split())

def log(*args) -> None:
    print("DEBUG:", *args, file=sys.stderr)

MOD = 10**9 + 7
_MAX = 400020

kaijo = [1]
for i in range(1, _MAX):
    kaijo.append(kaijo[-1] * i % MOD)

inv_kaijo = [1] * _MAX
inv_kaijo[-1] = pow(kaijo[-1], MOD-2, MOD)
for i in range(_MAX - 2, -1, -1):
    inv_kaijo[i] = inv_kaijo[i+1] * (i+1) % MOD

def inv(x: int) -> int:
    return pow(x, MOD-2, MOD)

def nPk(n: int, k: int) -> int:
    if 0 <= k <= n:
        return kaijo[n] * inv_kaijo[n - k] % MOD
    return 0

def nCk(n: int, k: int) -> int:
    if 0 <= k <= n:
        return kaijo[n] * inv_kaijo[k] % MOD * inv_kaijo[n - k] % MOD
    return 0

n, k = get_nums_l()

if k >= n - 1:
    print(nCk(n + n - 1, n) % MOD)
    sys.exit()

ans = sum(
    nCk(n, z) * nCk(n - 1, z) % MOD
    for z in range(1, k + 1)
)
ans = (ans + 1) % MOD

print(ans)