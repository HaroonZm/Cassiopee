import sys

def set_recursion_limit():
    sys.setrecursionlimit(100000)

def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def initialize_dp(n, size):
    dp = []
    for _ in range(n-1):
        dp.append([0]*size)
    return dp

def set_initial_dp_value(dp, index, value):
    dp[0][value] = 1

def is_dp_zero(dp, i, k):
    return dp[i-1][k] == 0

def can_add(k, val, max_val):
    return k + val <= max_val

def can_subtract(k, val, min_val):
    return k - val >= min_val

def add_to_dp(dp, i, k, val):
    dp[i][k+val] += dp[i-1][k]

def subtract_from_dp(dp, i, k, val):
    dp[i][k-val] += dp[i-1][k]

def process_dp_values(N, MIN, MAX, dp, table):
    for i in range(1, N-1):
        for k in range(MIN, MAX+1):
            if is_dp_zero(dp, i, k):
                continue
            if can_add(k, table[i], MAX):
                add_to_dp(dp, i, k, table[i])
            if can_subtract(k, table[i], MIN):
                subtract_from_dp(dp, i, k, table[i])

def print_result(dp, N, table):
    print("%d" % (dp[N-2][table[N-1]]))

def main():
    set_recursion_limit()
    BIG_NUM = 2000000000
    HUGE_NUM = 99999999999999999
    MOD = 1000000007
    EPS = 0.000000001

    MIN = 0
    MAX = 20
    SIZE = 21

    N = read_integer()
    dp = initialize_dp(N, SIZE)
    table = read_integer_list()

    set_initial_dp_value(dp, 0, table[0])
    process_dp_values(N, MIN, MAX, dp, table)
    print_result(dp, N, table)

main()