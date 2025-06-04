N, D = map(int, input().split())
d = list(map(int, input().split()))
Q = int(input())
q = list(map(lambda x: int(x)-1, input().split()))
dis = [0] * (N+1)
dis[0] = D
i = 0
while i < N:
    dis[i+1] = min(dis[i], abs(dis[i] - d[i]))
    i += 1
dp = [0] * (N+1)
dp[N] = 1
i = N-1
while i >= 0:
    if d[i] // 2 >= dp[i+1]:
        dp[i] = dp[i+1]
    else:
        dp[i] = dp[i+1] + d[i]
    i -= 1
qi = 0
while qi < Q:
    if dis[q[qi]] < dp[q[qi]+1]:
        print("NO")
    else:
        print("YES")
    qi += 1