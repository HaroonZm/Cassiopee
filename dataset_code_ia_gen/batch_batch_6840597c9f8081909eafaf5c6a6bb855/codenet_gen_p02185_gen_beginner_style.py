MOD = 10**9 + 7

S = input().strip()
T = input().strip()
n = len(S)

dp = [[0, 0] for _ in range(n+1)]
# dp[i][0] = number of ways up to i, and T' prefix == S prefix
# dp[i][1] = number of ways up to i, and T' prefix < S prefix
dp[0][0] = 1
sum_dp = [[0, 0] for _ in range(n+1)]
# sum_dp[i][b] = sum of all numbers formed up to i with state b

for i in range(n):
    s_digit = int(S[i])
    if T[i] == '?':
        digits = range(10)
    else:
        digits = [int(T[i])]
    for b in [0,1]:
        count = dp[i][b]
        total_sum = sum_dp[i][b]
        if count == 0:
            continue
        for d in digits:
            if b == 0:
                # must ensure prefix equal or less
                if d < s_digit:
                    nb = 1
                elif d == s_digit:
                    nb = 0
                else:
                    continue
            else:
                nb = 1
            dp[i+1][nb] = (dp[i+1][nb] + count) % MOD
            # sum of numbers up to i+1:
            # total_sum *10 + d * count
            sum_dp[i+1][nb] = (sum_dp[i+1][nb] + (total_sum * 10 + d * count) ) % MOD

res = (sum_dp[n][0] + sum_dp[n][1]) % MOD
print(res)