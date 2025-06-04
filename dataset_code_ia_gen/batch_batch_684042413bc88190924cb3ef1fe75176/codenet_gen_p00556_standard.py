import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [int(input()) for _ in range(N)]

cnt = [0]*(M+1)
for s in S: cnt[s]+=1

change = [[0]*(N+1) for _ in range(M+1)]
for i in range(N):
    for j in range(1, M+1):
        change[j][i+1] = change[j][i]
    change[S[i]][i+1] += 1

INF = 10**9
dp = [[INF]*(M+1) for _ in range(M+1)]
for i in range(M+1):
    dp[i][i] = 0

for length in range(1, M+1):
    for l in range(1, M-length+2):
        r = l + length -1
        length_sum = sum(cnt[l:r+1])
        if length == 1:
            dp[l][r] = 0
            continue
        for mid in range(l, r):
            left_sum = sum(cnt[l:mid+1])
            right_sum = sum(cnt[mid+1:r+1])
            left_correct = change[mid][length_sum] - change[mid][0]
            right_correct = change[r][length_sum] - change[r][0] - (change[mid][length_sum] - change[mid][0])
            cost = dp[l][mid] + dp[mid+1][r] + length_sum - (left_correct + right_correct)
            if cost < dp[l][r]:
                dp[l][r] = cost

ans = dp[1][M]
print(ans)