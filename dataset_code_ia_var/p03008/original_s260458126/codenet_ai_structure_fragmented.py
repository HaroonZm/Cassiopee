import sys
range = xrange
input = raw_input

def read_int():
    return int(input())

def read_int_list():
    return [int(x) for x in input().split()]

def initialize_dp(size):
    dp = [0] * (size + 1)
    dp[size] = size
    return dp

def compute_extra(a, b, idx):
    sell = a[idx]
    extra = b[idx] - sell
    return sell, extra

def update_dp(dp, sell, extra):
    for i in reversed(range(len(dp) - sell)):
        dp[i] = max(dp[i], dp[i + sell] + extra)

def dp_round(n, A, B):
    dp = initialize_dp(n)
    for j in range(3):
        sell, extra = compute_extra(A, B, j)
        if extra > 0:
            update_dp(dp, sell, extra)
    return max(dp)

def swap_lists(a, b):
    return b, a

def process(A, B, n):
    first_max = dp_round(n, A, B)
    A, B = swap_lists(A, B)
    second_max = dp_round(first_max, A, B)
    return second_max

def main():
    n = read_int()
    A = read_int_list()
    B = read_int_list()
    result = process(A, B, n)
    print(result)

main()