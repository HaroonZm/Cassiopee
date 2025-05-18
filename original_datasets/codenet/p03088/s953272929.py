p = 10**9+7
N = int(input())
dp = [[[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if i==0:
                    dp[3][i][j][k][l] = 1
for i in range(4):
    dp[3][i][0][1][2] = 0
    dp[3][i][1][0][2] = 0
    dp[3][i][0][2][1] = 0
for n in range(4,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for x in range(4):
                        dp[n][i][j][k][l] = (dp[n][i][j][k][l]+dp[n-1][x][i][j][k]*(str(j)+str(k)+str(l)!="012")\
                            *(str(j)+str(k)+str(l)!="102")*(str(j)+str(k)+str(l)!="021")\
                            *(str(i)+str(k)+str(l)!="012")*(str(i)+str(j)+str(l)!="012"))%p
cnt = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                cnt = (cnt+dp[N][i][j][k][l])%p
print(cnt)