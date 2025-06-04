import sys

def read_input():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    return h, w, a, b

def get_ofset():
    return 80 * 164

def initialize_dp(h, w):
    return [[0 for _ in range(w)] for _ in range(h)]

def set_dp_start(dp, a, b, ofset):
    diff1 = a[0][0] - b[0][0]
    diff2 = b[0][0] - a[0][0]
    dp[0][0] |= 1 << (diff1 + ofset)
    dp[0][0] |= 1 << (diff2 + ofset)

def update_dp_cell(dp, i, j, A, ni, nj):
    dp[ni][nj] |= (dp[i][j] << A)
    dp[ni][nj] |= (dp[i][j] >> A)

def process_row(dp, i, j, a, b, h, w):
    if i < h - 1:
        A = abs(a[i+1][j] - b[i+1][j])
        update_dp_cell(dp, i, j, A, i+1, j)
        
def process_col(dp, i, j, a, b, h, w):
    if j < w - 1:
        A = abs(a[i][j+1] - b[i][j+1])
        update_dp_cell(dp, i, j, A, i, j+1)

def process_dp(dp, a, b, h, w):
    for i in range(h):
        for j in range(w):
            process_row(dp, i, j, a, b, h, w)
            process_col(dp, i, j, a, b, h, w)

def search_min_diff_positive(dp, ofset, h, w):
    limit = 80 * 330
    for i in range(ofset, limit):
        if (dp[h-1][w-1] >> i) & 1:
            return i - ofset
    return float('inf')

def search_min_diff_negative(dp, ofset, h, w):
    for i in reversed(range(ofset)):
        if (dp[h-1][w-1] >> i) & 1:
            return ofset - i
    return float('inf')

def get_final_ans(min_pos, min_neg):
    return min(min_pos, min_neg)

def main():
    h, w, a, b = read_input()
    ofset = get_ofset()
    dp = initialize_dp(h, w)
    set_dp_start(dp, a, b, ofset)
    process_dp(dp, a, b, h, w)
    min_pos = search_min_diff_positive(dp, ofset, h, w)
    min_neg = search_min_diff_negative(dp, ofset, h, w)
    ans = get_final_ans(min_pos, min_neg)
    print(ans)

if __name__ == '__main__':
    main()