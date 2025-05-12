from heapq import heappop, heappush, heapify

MAX_MONEY = 2500
INF = float("inf")
n, m, s = map(int, input().split())
s = min(s, MAX_MONEY)
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append((v, a, b))
    graph[v].append((u, a, b))
cd = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[INF] * (MAX_MONEY+10) for _ in range(n)]
dp[0][s] = 0

q = [(0, 0, s)]
while q:
    dist, v, money = heappop(q)
    if dp[v][money] < dist: continue
    for nv, fare, cost in graph[v]:
        nm = money - fare
        if nm < 0: continue
        if dp[nv][nm] > dp[v][money] + cost:
            dp[nv][nm] = dp[v][money] + cost
            heappush(q, (dp[nv][nm], nv, nm))
    
    nm = min(money+cd[v][0], MAX_MONEY)
    if dp[v][nm] > dp[v][money] + cd[v][1]:
        dp[v][nm] = dp[v][money] + cd[v][1]
        heappush(q, (dp[v][nm], v, nm))

for i in range(1, n):
    print(min(dp[i]))