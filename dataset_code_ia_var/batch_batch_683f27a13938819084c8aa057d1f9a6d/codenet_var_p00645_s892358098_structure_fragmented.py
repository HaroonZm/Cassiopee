def create_arr():
    arr = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]
    for r1 in range(5):
        for c1 in range(5):
            for r2 in range(r1, 5):
                for c2 in range(c1, 5):
                    for r in range(r1, r2+1):
                        for c in range(c1, c2+1):
                            arr[r1][c1][r2][c2] |= (1 << (5*r+c))
    return arr

def initialize_memo():
    return [-1] * (1 << 25)

def get_first_set_bit(b, n):
    for r1 in range(n):
        for c1 in range(n):
            if b & (1 << (5*r1+c1)):
                return True, r1, c1
    return False, None, None

def can_proceed_set_bit(f):
    return f

def break_out_of_loop(f):
    return f

def update_ans(ans, value):
    return min(ans, value)

def set_memo(memo, b, value):
    memo[b] = value

def query_memo(memo, b):
    return memo[b]

def has_cached_result(memo, b):
    return memo[b] >= 0

def is_terminal_state(b):
    return b == 0

def update_b(b, rr, cc, r2, c2, arr):
    return b ^ arr[rr][cc][r2][c2]

def build_matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]

def matrix_to_bitmask(a, n):
    b = 0
    for r in range(n):
        for c in range(n):
            if a[r][c]:
                b |= (1 << (5*r+c))
    return b

def print_myon(ans):
    print("myon" * ans)

def process_once(arr, memo, n):
    a = build_matrix(n)
    b = matrix_to_bitmask(a, n)
    ans = calc(b, arr, memo, n)
    print_myon(ans)

def calc(b, arr, memo, n):
    if is_terminal_state(b):
        set_memo(memo, b, 0)
        return 0
    if has_cached_result(memo, b):
        return query_memo(memo, b)

    f, rr, cc = get_first_set_bit(b, n)
    if not can_proceed_set_bit(f):
        set_memo(memo, b, 0)
        return 0

    ans = 25
    for r2 in range(rr, n):
        for c2 in range(cc, n):
            k = update_b(b, rr, cc, r2, c2, arr)
            ans = update_ans(ans, calc(k, arr, memo, n) + 1)
    set_memo(memo, b, ans)
    return ans

def needs_to_break_from_while(n):
    return n == 0

def read_n():
    return int(input())

def main_loop():
    arr = create_arr()
    memo = initialize_memo()
    while True:
        n = read_n()
        if needs_to_break_from_while(n):
            break
        process_once(arr, memo, n)

main_loop()