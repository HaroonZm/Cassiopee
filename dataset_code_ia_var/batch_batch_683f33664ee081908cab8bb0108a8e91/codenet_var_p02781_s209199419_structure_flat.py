n = str(input())
p = int(input())
keta = len(n)
Dp = [[[0 for _ in range(2)] for _ in range(keta+1)] for _ in range(keta+1)]
Dp[0][0][1] = 1
i = 0
while i < keta:
    j = 0
    while j <= i:
        k = 0
        while k < 10:
            digit = int(n[i])
            if k == 0:
                if k < digit:
                    Dp[i+1][j][0] += Dp[i][j][0]
                    Dp[i+1][j][0] += Dp[i][j][1]
                elif k == digit:
                    Dp[i+1][j][1] += Dp[i][j][1]
                    Dp[i+1][j][0] += Dp[i][j][0]
                else:
                    Dp[i+1][j][0] += Dp[i][j][0]
            else:
                if k < digit:
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                    Dp[i+1][j+1][0] += Dp[i][j][1]
                elif k == digit:
                    Dp[i+1][j+1][1] += Dp[i][j][1]
                    Dp[i+1][j+1][0] += Dp[i][j][0]
                else:
                    Dp[i+1][j+1][0] += Dp[i][j][0]
            k += 1
        j += 1
    i += 1
if p > keta:
    print(0)
else:
    print(Dp[keta][p][0] + Dp[keta][p][1])