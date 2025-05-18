N = int(input())

C = input()

S = list(C)

dp = [[0 for i in range(8)] for j in range(N + 1)]

dp[0][1] = 1

for i in range(N):
    if C[i] == "J":
        dp[i + 1][1] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4];
        dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6];
        dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7];
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7];
        dp[i + 1][5] = 0;
        dp[i + 1][6] = 0;
        dp[i + 1][7] = 0;
    if C[i] == 'O':
        dp[i + 1][1] = 0;
        dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6];
        dp[i + 1][3] = 0;
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7];
        dp[i + 1][5] = dp[i][2] + dp[i][4] + dp[i][5] + dp[i][6];
        dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7];
        dp[i + 1][7] = 0;
    if C[i] == 'I':
        dp[i + 1][1] = 0;
        dp[i + 1][2] = 0;
        dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7];
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7];
        dp[i + 1][5] = 0;
        dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7];
        dp[i + 1][7] = dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7];

print((dp[N][1] + dp[N][2] + dp[N][3] + dp[N][4] + dp[N][5] + dp[N][6] + dp[N][7]) % 10007)