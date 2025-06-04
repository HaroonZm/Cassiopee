import sys
sys.setrecursionlimit(10**7)

def solve(m, objects):
    n = len(objects)
    objs = [int(o, 2) for o in objects]
    all_mask = (1 << m) - 1

    from functools import lru_cache

    @lru_cache(None)
    def dfs(mask, group):
        if len(group) <= 1:
            return 0
        res = float('inf')
        used = [False]*m
        for x in group:
            for i in range(m):
                used[i] = True
        for f in range(m):
            # partition the group by feature f
            s0 = tuple(x for x in group if (objs[x] & (1 << (m - 1 - f))) == 0)
            s1 = tuple(x for x in group if (objs[x] & (1 << (m - 1 - f))) != 0)
            if s0 and s1:
                v = 1 + max(dfs(mask | (1<<f), s0), dfs(mask | (1<<f), s1))
                if v < res:
                    res = v
        if res == float('inf'):
            return 0
        return res

    return dfs(0, tuple(range(n)))

input=sys.stdin.readline
while True:
    m,n = map(int,input().split())
    if m==0 and n==0: break
    objects=[input().strip() for _ in range(n)]
    print(solve(m,objects))