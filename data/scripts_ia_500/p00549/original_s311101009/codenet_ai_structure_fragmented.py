import sys

def set_recursion_limit():
    sys.setrecursionlimit(100000)

def read_input():
    N = int(input())
    input_str = input()
    return N, input_str

def initialize_constants():
    BIG_NUM = 2000000000
    HUGE_NUM = 99999999999999999
    MOD = 1000000007
    EPS = 0.000000001
    J = 0
    O = 1
    I = 2
    JO = 3
    OI = 4
    return J, O, I, JO, OI

def create_dp_matrix(N, categories):
    return [[0]*categories for _ in range(N+1)]

def update_dp_for_character(dp, i, char, J, O, I, JO, OI, num_JOI):
    if char == "J":
        dp[i][J] += 1
    elif char == "O":
        dp[i][O] += 1
        dp[i][JO] += dp[i-1][J]
    else:  # char == "I"
        dp[i][I] += 1
        dp[i][OI] += dp[i-1][O]
        num_JOI += dp[i-1][JO]
    return dp, num_JOI

def accumulate_dp(dp, i, categories):
    for k in range(categories):
        dp[i][k] += dp[i-1][k]
    return dp

def calculate_maximum(dp, N, JO, OI):
    return max(dp[N][JO], dp[N][OI])

def update_maximum_for_position(maximum, dp, i, N, input_char, J, I):
    if input_char == "J":
        maximum = max(maximum, dp[i][J] * (dp[N][I] - dp[i][I]))
    elif input_char == "O":
        maximum = max(maximum, dp[i-1][J] * (dp[N][I] - dp[i][I]))
    else:
        maximum = max(maximum, dp[i-1][J] * (dp[N][I] - dp[i][I] + 1))
    return maximum

def main():
    set_recursion_limit()
    J, O, I, JO, OI = initialize_constants()
    N, input_str = read_input()
    dp = create_dp_matrix(N, 5)
    num_JOI = 0

    for i in range(1, N+1):
        dp, num_JOI = update_dp_for_character(dp, i, input_str[i-1], J, O, I, JO, OI, num_JOI)
        dp = accumulate_dp(dp, i, 5)

    maximum = calculate_maximum(dp, N, JO, OI)

    for i in range(1, N+1):
        maximum = update_maximum_for_position(maximum, dp, i, N, input_str[i-1], J, I)

    print("%d" % (num_JOI + maximum))

main()