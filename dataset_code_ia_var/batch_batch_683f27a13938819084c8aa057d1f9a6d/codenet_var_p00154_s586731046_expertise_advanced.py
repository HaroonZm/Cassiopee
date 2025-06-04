import sys
from functools import lru_cache
readline = sys.stdin.readline
write = sys.stdout.write
ans = []

while True:
    if (M := int(readline())) == 0:
        break

    P = [tuple(map(int, readline().split())) for _ in range(M)]

    @lru_cache(maxsize=None)
    def dfs(i, rest):
        if i == M:
            return int(rest == 0)
        a, b = P[i]
        return sum(
            dfs(i + 1, rest - k * a)
            for k in range(0, min(b, rest // a) + 1)
        )

    G = int(readline())
    ans.extend(str(dfs(0, int(readline()))) for _ in range(G))

write('\n'.join(ans) + '\n')