def edit_dist(S0, S1):
    i = len(S0)
    j = len(S1)
    dp = [i for i in range(len(S1) + 1)]

    for i in range(1, i+1):
        dp_prev = dp[:]
        dp[0] = i
        for j in range(1, j+1):
            dp[j] = min(dp_prev[j-1] + (S0[i-1] is not S1[j-1]), dp_prev[j] + 1, dp[j-1] + 1)
    return dp[-1]

if __name__ == "__main__":
    s0 = input()
    s1 = input()
    print(edit_dist(s0, s1))