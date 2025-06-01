N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

# dp[i][j] : i日目までに都市jにいるときの最小疲労度
# iは1からMまでの日数, jは0からNまでの都市の番号
INF = 10**9
dp = [[INF]*(N+1) for _ in range(M+1)]
dp[0][0] = 0

for day in range(1, M+1):
    for city in range(N+1):
        # 待機した場合は疲労度変わらず、前の日と同じ疲労度
        if dp[day-1][city] < dp[day][city]:
            dp[day][city] = dp[day-1][city]
        # 移動できるなら移動する場合の疲労度計算
        if city > 0 and dp[day-1][city-1] != INF:
            cost = dp[day-1][city-1] + D[city-1] * C[day-1]
            if cost < dp[day][city]:
                dp[day][city] = cost

# 都市Nにたどり着く最小疲労度をM日以内で探す
ans = INF
for day in range(N, M+1):
    if dp[day][N] < ans:
        ans = dp[day][N]

print(ans)