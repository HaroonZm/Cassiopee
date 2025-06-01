def read_input():
    return map(int, input().split())

def is_termination_condition(N, M, S):
    return max(N, M, S) == 0

def compute_constants(N, M, S):
    p = N * N
    q = M - p
    T = S - (p * (p + 1)) // 2
    return p, q, T

def initialize_dp(p, T):
    dp = [[0 for _ in range(T + 1)] for _ in range(p + 1)]
    dp[0][0] = 1
    return dp

def update_dp_cell(dp, i, j, q, MOD):
    dp[i][j] = dp[i-1][j]
    if j - i >= 0:
        dp[i][j] += dp[i][j - i]
    if j - i - q >= 0:
        dp[i][j] -= dp[i-1][j - i - q]
    dp[i][j] %= MOD

def fill_dp(dp, p, q, T, MOD):
    for i in range(1, p + 1):
        for j in range(T + 1):
            update_dp_cell(dp, i, j, q, MOD)

def solve(N, M, S):
    MOD = 10 ** 5
    p, q, T = compute_constants(N, M, S)
    dp = initialize_dp(p, T)
    fill_dp(dp, p, q, T, MOD)
    return dp[p][T]

def main():
    while True:
        N, M, S = read_input()
        if is_termination_condition(N, M, S):
            break
        ans = solve(N, M, S)
        print(ans)

main()