N = int(input())
C = input()
S = [*C]
dp = []
for _ in range(N+1):
    dp.append([0]*8)
dp[0][1] = 1

def ssum(arr, idxs):
    return sum(arr[i] for i in idxs)

for i in range(N):
    c = C[i]
    if c == 'J':
        dp[i+1][1] = dp[i][1]+dp[i][2]+dp[i][3]+dp[i][4]
        dp[i+1][2] = ssum(dp[i], [1,2,3,4,5,6])
        dp[i+1][3] = dp[i][1]+dp[i][2]+dp[i][3]+dp[i][4]+dp[i][6]+dp[i][7]
        dp[i+1][4] = ssum(dp[i], [1,2,3,4,5,6,7])
        dp[i+1][5] = dp[i+1][6] = dp[i+1][7] = 0
    elif c == 'O':
        dp[i+1][1] = 0
        dp[i+1][2] = ssum(dp[i], [1,2,3,4,5,6])
        dp[i+1][3] = 0
        dp[i+1][4] = ssum(dp[i], range(1,8))
        dp[i+1][5] = dp[i][2] + dp[i][4] + dp[i][5] + dp[i][6]
        dp[i+1][6] = sum(dp[i][j] for j in [2,3,4,5,6,7])
        dp[i+1][7] = 0
    elif c == 'I':
        dp[i+1][1] = 0; dp[i+1][2] = 0
        dp[i+1][3] = ssum(dp[i], [1,2,3,4,6,7])
        dp[i+1][4] = ssum(dp[i], range(1,8))
        dp[i+1][5] = 0
        dp[i+1][6] = ssum(dp[i], [2,3,4,5,6,7])
        dp[i+1][7] = dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]

res = sum(dp[N][1:8])%10007
print(res)