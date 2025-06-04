N = int(input())
S = input()
dp = []
for i in range(N + 1):
    row = []
    for j in range(N + 1):
        row.append(0)
    dp.append(row)
r = 0
i = N - 1
while i >= 0:
    s = S[i]
    j = N - 1
    while j >= i:
        if s == S[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
        else:
            dp[i][j] = 0
        if dp[i][j] < (j - i):
            r = max(r, dp[i][j])
        else:
            r = max(r, j - i)
        j -= 1
    i -= 1
print(r)