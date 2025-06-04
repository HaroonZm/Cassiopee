def read_input():
    try:
        w, h = map(int, raw_input().split())
        return w, h
    except:
        return 0, 0

def is_end_case(w, h):
    return (w | h) == 0

def make_dp_table(w, h):
    return [[[0] * (w + 1) for _ in xrange(h + 1)] for _ in xrange(4)]

def initialize_dp(dp):
    dp[0][1][0] = 1
    dp[3][0][1] = 1

def update_dp_cell(dp, y, x):
    update_dp_0(dp, y, x)
    update_dp_1(dp, y, x)
    update_dp_2(dp, y, x)
    update_dp_3(dp, y, x)

def update_dp_0(dp, y, x):
    dp[0][y + 1][x] += dp[0][y][x] + dp[2][y][x]

def update_dp_1(dp, y, x):
    dp[1][y][x + 1] += dp[0][y][x]

def update_dp_2(dp, y, x):
    dp[2][y + 1][x] += dp[3][y][x]

def update_dp_3(dp, y, x):
    dp[3][y][x + 1] += dp[1][y][x] + dp[3][y][x]

def fill_dp(dp, w, h):
    for y in xrange(h):
        for x in xrange(w):
            update_dp_cell(dp, y, x)

def calculate_answer(dp, w, h):
    return sum(dp[i][h-1][w-1] for i in xrange(4))

def print_result(ans):
    print ans % 100000

def solve_case(w, h):
    dp = make_dp_table(w, h)
    initialize_dp(dp)
    fill_dp(dp, w, h)
    ans = calculate_answer(dp, w, h)
    print_result(ans)

def main():
    while True:
        w, h = read_input()
        if is_end_case(w, h):
            break
        solve_case(w, h)

main()