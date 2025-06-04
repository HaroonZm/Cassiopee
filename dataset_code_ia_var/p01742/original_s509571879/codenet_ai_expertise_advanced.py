import sys
from functools import lru_cache

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    MOD = 10**9 + 7
    N = int(readline())
    M = 20
    L = 26
    S = [readline().strip().ljust(M, chr(0)) for _ in range(N)]
    S = [[ord(ch) for ch in row] for row in S]
    ca = ord('a')
    cq = ord('?')

    @lru_cache(maxsize=None)
    def dfs(l, r, p, c):
        if l == r:
            return 1
        if p == M:
            return int(l + 1 == r)
        if c == L + 1:
            return 0
        # Option 1: skip this character (try next c)
        res = dfs(l, r, p, c + 1)
        ch = ca + c - 1
        # Option 2: try to find a segment where each s[p] == ch or '?'
        for i in range(l + 1, r + 1):
            for idx in range(l, i):
                if S[idx][p] != ch and S[idx][p] != cq:
                    break
            else:
                res = (res + dfs(l, i, p + 1, 0) * dfs(i, r, p, c + 1)) % MOD
                continue
            break
        return res % MOD

    write(f"{dfs(0, N, 0, 0)}\n")

solve()