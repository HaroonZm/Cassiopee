def read_input():
    return input()

def get_length(s):
    return len(s)

def get_inf(n):
    return n + 1

def make_next_table(n, inf):
    return [[inf] * 26 for _ in range(n + 1)]

def char_to_index(c):
    return ord(c) - ord('a')

def fill_next_table(s, n, inf, nex):
    def process_position(i, c):
        ic = char_to_index(c)
        for j in range(26):
            nex[n - i - 1][j] = (n - i - 1) if j == ic else nex[n - i][j]
    for i, c in enumerate(s[::-1]):
        process_position(i, c)

def make_dp(n):
    return [n] * (n + 3)

def set_dp_terminal_cases(dp, inf):
    dp[inf] = 0
    dp[inf + 1] = 0

def compute_min_next(dp, nex, i, inf):
    tmp = inf
    for j in range(26):
        cur = dp[nex[i][j] + 1] + 1
        if cur < tmp:
            tmp = cur
        if tmp == 1:
            break
    return tmp

def fill_dp(n, inf, dp, nex):
    for i in range(n, -1, -1):
        dp[i] = compute_min_next(dp, nex, i, inf)

def initialize_answer_list():
    return []

def get_next_dp_value(dp, nex, i, j):
    return dp[nex[i][j] + 1]

def get_char_from_index(j):
    return chr(j + ord('a'))

def build_answer(dp, nex, ans, n):
    i = 0
    for v in range(dp[0] - 1, -1, -1):
        for j in range(26):
            if get_next_dp_value(dp, nex, i, j) != v:
                continue
            ans.append(get_char_from_index(j))
            i = nex[i][j] + 1
            break

def join_answer(ans):
    return ''.join(ans)

def main():
    S = read_input()
    N = get_length(S)
    INF = get_inf(N)
    nex = make_next_table(N, INF)
    fill_next_table(S, N, INF, nex)
    dp = make_dp(N)
    set_dp_terminal_cases(dp, INF)
    fill_dp(N, INF, dp, nex)
    ans = initialize_answer_list()
    build_answer(dp, nex, ans, N)
    result = join_answer(ans)
    print(result)

main()