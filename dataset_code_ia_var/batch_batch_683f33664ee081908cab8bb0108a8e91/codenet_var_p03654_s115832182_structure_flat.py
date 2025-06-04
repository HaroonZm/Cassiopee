import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
abd = []
for i in range(n-1):
    abd.append(list(map(int, input().split())))
if n == 2:
    print(abd[0][2])
    exit()
graph = []
deg = []
for i in range(n+1):
    graph.append([])
    deg.append(0)
for a, b, d in abd:
    graph[a].append((b, d))
    graph[b].append((a, d))
    deg[a] += 1
    deg[b] += 1
stack = []
root = 0
dp = []
sm = []
mx = []
for i in range(n+1):
    dp.append([])
    sm.append(1)
    mx.append(0)
for i in range(1, n+1):
    if deg[i] == 1:
        stack.append(i)
    elif root == 0:
        root = i
        deg[i] += 1
ans = 0
flg = 0
while stack:
    x = stack.pop()
    if dp[x]:
        sm[x] += sum(dp[x])
    if sm[x]*2 == n:
        flg = 1
    for y, d in graph[x]:
        if deg[y] > 1:
            dp[y].append(sm[x])
            if sm[x] == n-sm[x]:
                ans += (sm[x]*2-1)*d
            else:
                ans += min(sm[x], n-sm[x])*2*d
            deg[y] -= 1
            if deg[y] == 1:
                stack.append(y)
dmn = 10**18
if not flg:
    for a, b, d in abd:
        for v in (a, b):
            if not mx[v]:
                if dp[v]:
                    mx[v] = max(max(dp[v]), n-1-sm[v])
                else:
                    mx[v] = n-2
        if min(mx[a], mx[b])*2 < n:
            if d < dmn:
                dmn = d
    ans -= dmn
print(ans)