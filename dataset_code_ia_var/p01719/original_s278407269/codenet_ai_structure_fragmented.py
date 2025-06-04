import sys

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_initial_parameters():
    return map(int, sys.stdin.readline().split())

def read_matrix(d):
    return [read_int_list() for _ in range(d)]

def create_dp_array(size):
    return [0] * size

def reset_dp(dp, size):
    for i in range(size):
        dp[i] = 0

def compute_next_x(curr_x, n, dp, k, pp, d):
    next_x = curr_x
    for i in range(n):
        for j in range(curr_x + 1):
            if j - pp[k][i] >= 0:
                new_val = dp[j - pp[k][i]] + pp[k + 1][i]
                if dp[j] < new_val:
                    dp[j] = new_val
            result_x = (curr_x - j) + dp[j]
            if next_x < result_x:
                next_x = result_x
    return next_x

def iterate_over_k(d, n, dp, pp, curr_x):
    for k in range(d - 1):
        reset_dp(dp, curr_x + 1)
        next_x = compute_next_x(curr_x, n, dp, k, pp, d)
        curr_x = next_x
    return curr_x

def output_result(result):
    print(result)

def main():
    n, d, x = read_initial_parameters()
    pp = read_matrix(d)
    dp = create_dp_array(100001)
    curr_x = x
    curr_x = iterate_over_k(d, n, dp, pp, curr_x)
    output_result(curr_x)

if __name__ == '__main__':
    main()