import sys
from functools import lru_cache

def solve():
    readline = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    M_N = readline()
    if not M_N:
        return False
    M, N = map(int, M_N.split())
    if M == N == 0:
        return False
    B = [int(readline(), 2) for _ in range(N)]
    B_tuple = tuple(B)  # For lru_cache

    @lru_cache(maxsize=None)
    def dfs(s, t):
        c = sum(((b & s) == t) for b in B_tuple)
        if c <= 1:
            return 0
        choices = (max(dfs(s | (1 << i), t), dfs(s | (1 << i), t | (1 << i))) + 1
                   for i in range(M) if not (s & (1 << i)))
        return min(choices, default=0)

    write(f"{dfs(0, 0)}\n".encode())
    return True

while solve():
    pass