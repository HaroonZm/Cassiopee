n = str(input())
p = int(input())

keta = len(n)
Dp = [[[0 for _ in range(2)] for _ in range(keta+1)]for _ in range(keta+1)]

Dp[0][0][1] = 1
10
for i in range(keta):
    for j in range(i+1):
        for k in range(10):
            if k == 0:
                if k < int(n[i]):
                    Dp[i+1][j][0] += Dp[i][j][0]
                    Dp[i+1][j][0] += Dp[i][j][1]
                    
                elif k == int(n[i]):
                    Dp[i+1][j][1] += Dp[i][j][1]
                    Dp[i+1][j][0] += Dp[i][j][0]
                
                else:
                    Dp[i+1][j][0] += Dp[i][j][0]
            
            else:
                if k < int(n[i]):
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                    Dp[i+1][j+1][0] += Dp[i][j][1]
                elif k == int(n[i]):
                    Dp[i+1][j+1][1] += Dp[i][j][1]
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                else:
                    Dp[i+1][j+1][0] += Dp[i][j][0]

if p > keta:
    print(0)
else:
    print(sum(Dp[-1][p]))