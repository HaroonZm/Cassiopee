MOD = 10**9 + 7

def beautiful_sequences(N, M):
    # Total sequences of length N with 0/1: 2^N
    total = pow(2, N, MOD)

    # Count sequences without M consecutive 1s using DP
    dp = [0] * (M)  # dp[i]: sequences ending with i consecutive 1s, i < M
    dp[0] = 1  # empty sequence considered ended with 0 consecutive 1s
    for _ in range(N):
        new_dp = [0]*M
        # Add '0' resets consecutive ones count to 0
        total_zero = sum(dp) % MOD
        new_dp[0] = total_zero
        # Add '1' increases consecutive ones count by 1, must be < M
        for i in range(M-1):
            new_dp[i+1] = dp[i]
        dp = new_dp

    no_M = sum(dp) % MOD
    return (total - no_M) % MOD

N, M = map(int, input().split())
print(beautiful_sequences(N, M))