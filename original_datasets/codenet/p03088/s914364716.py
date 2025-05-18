# D - We Like AGC
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
N = int(readline())
# dp[i][j][k][l] := i桁目 3文字前 ２文字前 1文字前
dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
dp[0][3][3][3] = 1

for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0:
                    continue
                for a in range(4):
                    if k == 0 and l == 1 and a == 2:
                        continue
                    if k == 1 and l == 0 and a == 2:
                        continue
                    if k == 0 and l == 2 and a == 1:
                        continue
                    if j == 0 and l == 1 and a == 2:
                        continue
                    if j == 0 and k == 1 and a == 2:
                        continue
                    dp[i+1][k][l][a] += dp[i][j][k][l] 
                    dp[i+1][k][l][a] %= MOD
ans = 0

for j in range(4):
    for k in range(4):
        for l in range(4):  
            ans += dp[N][j][k][l]
            ans %= MOD
print(ans)