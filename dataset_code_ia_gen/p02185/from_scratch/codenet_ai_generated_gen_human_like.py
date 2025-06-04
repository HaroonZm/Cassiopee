MOD = 10**9 + 7

S = input().strip()
T = input().strip()
n = len(S)

# dp[i][flag] = (count, sum) number of ways and sum of values for t' prefix of length i
# flag = 0: prefix t' == prefix S
# flag = 1: prefix t' < prefix S
dp = [[(0, 0), (0, 0)] for _ in range(n+1)]
# base case: empty prefix, one way, sum=0, equal flag
dp[0][0] = (1, 0)

for i in range(n):
    s_digit = int(S[i])
    t_char = T[i]
    for flag in range(2):
        count, total = dp[i][flag]
        if count == 0:
            continue
        if t_char == '?':
            digits = range(10)
        else:
            digits = [int(t_char)]
        for d in digits:
            if flag == 0:
                # prefix equal so far
                if d < s_digit:
                    nflag = 1
                    ncount = count
                    nsum = (total * 10 + count * d) % MOD
                    c, s_ = dp[i+1][nflag]
                    dp[i+1][nflag] = ((c + ncount) % MOD, (s_ + nsum) % MOD)
                elif d == s_digit:
                    nflag = 0
                    ncount = count
                    nsum = (total * 10 + count * d) % MOD
                    c, s_ = dp[i+1][nflag]
                    dp[i+1][nflag] = ((c + ncount) % MOD, (s_ + nsum) % MOD)
                else:
                    # d > s_digit : invalid, skip
                    continue
            else:
                # flag == 1: prefix already smaller than S, can put any digit
                nflag = 1
                ncount = count
                nsum = (total * 10 + count * d) % MOD
                c, s_ = dp[i+1][nflag]
                dp[i+1][nflag] = ((c + ncount) % MOD, (s_ + nsum) % MOD)

ans = (dp[n][0][1] + dp[n][1][1]) % MOD
print(ans)