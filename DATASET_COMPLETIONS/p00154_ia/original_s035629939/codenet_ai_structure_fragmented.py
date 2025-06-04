import sys
from array import array

def read_m():
    return int(input())

def init_dp(m):
    dp = [array('I', [0] * 1001) for _ in range(m + 1)]
    dp[0][0] = 1
    return dp

def read_v_c():
    return map(int, input().split())

def update_dp_for_item(dp, i, v, c):
    for j in range(1001):
        for k in range(c + 1):
            next_pos = j + v * k
            if next_pos > 1000:
                continue
            dp[i + 1][next_pos] += dp[i][j]

def process_items(dp, m):
    for i in range(m):
        v, c = read_v_c()
        update_dp_for_item(dp, i, v, c)

def read_n():
    return int(input())

def read_x():
    return int(input())

def print_results(dp, m, n):
    for _ in range(n):
        x = read_x()
        print(dp[m][x])

def main_loop():
    while True:
        m = read_m()
        if m == 0:
            return 0
        dp = init_dp(m)
        process_items(dp, m)
        n = read_n()
        print_results(dp, m, n)

def main():
    sys.exit(main_loop())

if __name__ == '__main__':
    main()