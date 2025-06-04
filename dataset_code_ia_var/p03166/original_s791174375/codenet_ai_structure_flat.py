import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
inf = float('inf')

n, m = map(int, input().split())

es = tuple(set() for _ in range(n))
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    es[x].add(y)

used = [False] * n
dp = [inf] * n

ans = 0
stack = []
for start in range(n):
    if used[start]:
        ans = max(ans, dp[start])
        continue
    stack2 = []
    stack.append((start, 0, False))
    while stack:
        v, res, post = stack.pop()
        if post:
            dp[v] = res
            used[v] = True
            stack2.pop()
            if stack2:
                parent = stack2[-1]
                dp[parent] = max(dp[parent], dp[v]+1)
        else:
            if used[v]:
                if stack2:
                    parent = stack2[-1]
                    dp[parent] = max(dp[parent], dp[v]+1)
                continue
            res = 0
            stack.append((v, res, True))
            stack2.append(v)
            for u in es[v]:
                if not used[u]:
                    stack.append((u, 0, False))
                else:
                    dp[v] = max(dp[v], dp[u]+1)
    ans = max(ans, dp[start])

print(ans)