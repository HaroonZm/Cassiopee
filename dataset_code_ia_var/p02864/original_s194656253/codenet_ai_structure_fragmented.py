def read_input():
    N_K = input().split()
    N = int(N_K[0])
    K = int(N_K[1])
    return N, K

def read_heights():
    H = [int(i) for i in input().split()]
    return H

def preprocess_heights(H):
    return [0] + H  # 1-indexed

def is_n_equals_k(N, K):
    return N == K

def is_k_zero(K):
    return K == 0

def compute_ans_when_k_zero(N, H):
    ans = 0
    for i in range(N):
        ans += max(H[i+1] - H[i], 0)
    return ans

def initialize_dp(N, K):
    size = N - K + 1
    dp = []
    for _ in range(N + 1):
        dp.append([10 ** 12] * size)
    return dp

def set_dp_x1(dp, N, H):
    for x in range(N + 1):
        dp[x][1] = H[x]

def update_dp(dp, N, K, H):
    for y in range(2, N - K + 1):
        update_dp_for_y(dp, y, N, H)

def update_dp_for_y(dp, y, N, H):
    for x in range(N + 1):
        update_dp_for_x(dp, x, y, H)

def update_dp_for_x(dp, x, y, H):
    for i in range(1, x):
        candidate = dp[i][y - 1] + max(0, H[x] - H[i])
        if candidate < dp[x][y]:
            dp[x][y] = candidate

def find_min_ans(dp, N, K):
    min_ans = dp[0][N - K]
    for i in range(1, N + 1):
        if dp[i][N - K] < min_ans:
            min_ans = dp[i][N - K]
    return min_ans

def output_result(ans):
    print(ans)

def main():
    N, K = read_input()
    H_input = read_heights()
    H = preprocess_heights(H_input)

    if is_n_equals_k(N, K):
        output_result(0)
        return
    elif is_k_zero(K):
        ans = compute_ans_when_k_zero(N, H)
        output_result(ans)
        return

    dp = initialize_dp(N, K)
    set_dp_x1(dp, N, H)
    update_dp(dp, N, K, H)
    ans = find_min_ans(dp, N, K)
    output_result(ans)

if __name__ == '__main__':
    main()