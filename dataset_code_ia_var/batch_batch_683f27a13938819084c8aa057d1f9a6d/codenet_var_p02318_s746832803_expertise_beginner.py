def edit_dist(S0, S1):
    len_s0 = len(S0)
    len_s1 = len(S1)
    dp = [0] * (len_s1 + 1)
    for j in range(len_s1 + 1):
        dp[j] = j

    for i in range(1, len_s0 + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, len_s1 + 1):
            if S0[i - 1] == S1[j - 1]:
                cost = 0
            else:
                cost = 1
            temp = dp[j]
            dp[j] = min(
                prev + cost,        # substitution
                dp[j] + 1,          # deletion
                dp[j - 1] + 1       # insertion
            )
            prev = temp
    return dp[len_s1]

if __name__ == "__main__":
    s0 = input()
    s1 = input()
    print(edit_dist(s0, s1))