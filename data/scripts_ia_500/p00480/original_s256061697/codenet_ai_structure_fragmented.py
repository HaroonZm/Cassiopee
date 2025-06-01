def read_integer():
    return int(input())

def read_integer_list():
    return [int(i) for i in input().split()]

def create_dp_table(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def initialize_dp(dp, first_num):
    dp[0][first_num] = 1

def update_dp_for_index(dp, i, nums):
    for j in range(21):
        update_dp_for_value(dp, i, j, nums)

def update_dp_for_value(dp, i, j, nums):
    add_val = j + nums[i+1]
    sub_val = j - nums[i+1]
    if 0 <= add_val <= 20:
        dp[i+1][add_val] += dp[i][j]
    if 0 <= sub_val <= 20:
        dp[i+1][sub_val] += dp[i][j]

def compute_dp(dp, nums, n):
    for i in range(n - 2):
        update_dp_for_index(dp, i, nums)

def print_result(dp, n, nums):
    print(dp[n - 2][nums[n - 1]])

def main():
    n = read_integer()
    nums = read_integer_list()
    dp = create_dp_table(n - 1, 21)
    initialize_dp(dp, nums[0])
    compute_dp(dp, nums, n)
    print_result(dp, n, nums)

main()