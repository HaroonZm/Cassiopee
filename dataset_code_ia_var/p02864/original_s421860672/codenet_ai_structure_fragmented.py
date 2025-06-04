import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 5)

def get_mod():
    return 10 ** 9 + 7

def get_inf():
    return float('INF')

def get_stdin_readline():
    return sys.stdin.readline

def parse_first_line(readline):
    return map(int, readline().split())

def parse_heights_line(readline):
    return list(map(int, readline().split()))

def init_heights(N, readline):
    H_list = parse_heights_line(readline)
    return [0] + H_list + [0]

def init_dp(N, INF):
    dp = []
    for _ in range(N + 1):
        dp.append([INF] * (N + 1))
    return dp

def set_dp_base_case_zero(dp, N):
    for i in range(N + 1):
        dp[i][0] = 0

def set_dp_first_j(H, dp, N):
    for i in range(1, N + 1):
        dp[i][1] = H[i]

def update_dp_for_j(dp, H, N):
    for i in range(1, N + 1):
        for j in range(2, i + 1):
            update_dp_for_j_k(dp, H, i, j)

def update_dp_for_j_k(dp, H, i, j):
    for k in range(1, i):
        dp[i][j] = min(dp[i][j], dp[k][j - 1] + max(0, H[i] - H[k]))

def find_min_ans(dp, N, K, INF):
    ans = INF
    for i in range(1, N + 1):
        ans = min(ans, dp[i][N - K])
    return ans

def print_result(ans):
    print(ans)

def main():
    set_recursion_limit()
    INF = get_inf()
    readline = get_stdin_readline()
    N, K = parse_first_line(readline)
    H = init_heights(N, readline)
    dp = init_dp(N, INF)
    set_dp_base_case_zero(dp, N)
    set_dp_first_j(H, dp, N)
    update_dp_for_j(dp, H, N)
    ans = find_min_ans(dp, N, K, INF)
    print_result(ans)

if __name__ == '__main__':
    main()