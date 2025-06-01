MOD = 10**9 + 7

def beautiful_sequences_count(N, M):
    # dp[i][0]: sequences of length i that do NOT contain M consecutive 1s
    # dp[i][1]: sequences of length i that DO contain at least one sequence of M consecutive 1s
    # To handle this, we actually need to track sequences by the maximum length of consecutive 1s at the end,
    # since presence of M consecutive 1s anywhere means a "beautiful" sequence.

    # Instead, a better approach:
    # Let dp[i][j] = number of sequences of length i ending with j consecutive 1s (j from 0 to M)
    # For j == M, it means sequence contains at least one M-length consecutive 1s ending at position i.
    # We are interested in sequences that have at least one run of length M:
    # So total number of beautiful sequences = sum over dp[N][j] for j = M (all sequences that end with M consecutive ones)
    # Plus sequences that had M consecutive ones earlier (which can be tracked by once we reach j=M, we stay at j=M)
    # So we'll use j in [0..M], once j reaches M, it stays at M (meaning found a run >= M already)
    
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    # Base case: length 0, no sequence, considered as dp[0][0] = 1 (empty)
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        # Set current count:
        # If we put 0 at position i:
        # resets consecutive 1 count to 0
        dp[i][0] = sum(dp[i-1]) % MOD
        # If we put 1 at position i:
        # increase consecutive 1 count by 1, but capped at M
        for j in range(1, M +1):
            # if j < M, dp[i][j] = dp[i-1][j-1]
            # if j == M, dp[i][M] = dp[i-1][M-1] + dp[i-1][M] (stay at M because once found run >= M)
            if j < M:
                dp[i][j] = dp[i-1][j-1] % MOD
            else:
                dp[i][M] = (dp[i-1][M-1] + dp[i-1][M]) % MOD
    
    # The number of sequences of length N that contain at least one run of M consecutive 1s is:
    # all sequences - sequences that never reached j==M
    total = pow(2, N, MOD)
    no_beautiful = sum(dp[N][0:M]) % MOD
    result = (total - no_beautiful) % MOD
    return result

N, M = map(int, input().split())
print(beautiful_sequences_count(N, M))