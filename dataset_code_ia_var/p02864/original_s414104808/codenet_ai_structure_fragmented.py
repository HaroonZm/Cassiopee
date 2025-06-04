import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10 ** 9 + 7

def get_input():
    return sys.stdin.readline().rstrip()

def parse_n_and_k(input_fn):
    line = input_fn()
    return map(int, line.split())

def parse_heights(input_fn, n):
    line = input_fn()
    heights = list(map(int, line.split()))
    return [0] + heights

def create_dp_table(n, k):
    return [[INF] * (n - k + 1) for _ in range(n + 1)]

def initialize_dp(dp):
    dp[0][0] = 0

def compute_cost(H, x, x0):
    return max(0, H[x] - H[x0])

def update_dp_cell(dp, H, x, y):
    candidates = [dp[x0][y - 1] + compute_cost(H, x, x0) for x0 in range(x)]
    dp[x][y] = min(candidates)

def fill_dp(dp, H, n, k):
    for x in range(1, n + 1):
        for y in range(1, n - k + 1):
            update_dp_cell(dp, H, x, y)

def find_minimum(dp, n, k):
    values = [dp[x][n - k] for x in range(n + 1)]
    return min(values)

def print_result(result):
    print(result)

def resolve():
    n, k = parse_n_and_k(get_input)
    H = parse_heights(get_input, n)
    dp = create_dp_table(n, k)
    initialize_dp(dp)
    fill_dp(dp, H, n, k)
    result = find_minimum(dp, n, k)
    print_result(result)

resolve()