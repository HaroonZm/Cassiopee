import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from functools import lru_cache
def resolve():
    for _ in range(int(input())):
        n, a, b, c, d = map(int, input().split())

        @lru_cache(None)
        def dfs(k):
            # base case
            if k == 0:
                return 0
            if k == 1:
                return d
            # recursion
            res = k * d
            for p, cost in zip([2, 3, 5], [a, b, c]):
                q, r = divmod(k, p)
                if r == 0:
                    res = min(res, dfs(q) + cost)
                else:
                    res = min(res, dfs(q) + cost + d * r, dfs(q + 1) + cost + d * (p - r))
            return res

        print(dfs(n))
resolve()