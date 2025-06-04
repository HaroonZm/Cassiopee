def get_input():
    return int(input()), list(map(int, input().split()))

def binary_search(lo, hi, N, A, check_func):
    while lo < hi:
        mid = compute_mid(lo, hi)
        if check_func(N, A, mid):
            hi = mid
        else:
            lo = mid_increment(lo)
    return lo

def compute_mid(lo, hi):
    return (lo + hi) // 2

def lo_init():
    return 0

def hi_init():
    return int(1e18)

def min_value(a, b):
    return min(a, b)

def max_value(a, b):
    return max(a, b)

def cnt_increment(cnt):
    return cnt + 1

def ceil_division(a, b):
    return -(-a // b)

def should_increment_cnt(a, x, N):
    return a + x >= N

def get_x(n, i):
    return n - i

def process_a_element(a, x, N):
    return a + x - N + 1

def compute_additional_cnt(a, x, N):
    return ceil_division(process_a_element(a, x, N), N + 1)

def for_a_loop(A, x, N):
    cnt = 0
    for a in A:
        if should_increment_cnt(a, x, N):
            cnt += compute_additional_cnt(a, x, N)
    return cnt

def check_loop_iter(n, N):
    return min_value(n, N) + 1

def in_check_loop(i, n):
    return get_x(n, i)

def check(N, A, n):
    for i in range(check_loop_iter(n, N)):
        x = in_check_loop(i, n)
        cnt = for_a_loop(A, x, N)
        if cnt <= x:
            return True
    return False

def lo_less_than_hi(lo, hi):
    return lo < hi

def mid_increment(lo):
    return lo + 1

def print_result(result):
    print(result)

def main():
    N, A = get_input()
    lo = lo_init()
    hi = hi_init()
    result = binary_search(lo, hi, N, A, check)
    print_result(result)

if __name__ == "__main__":
    main()