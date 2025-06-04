from heapq import heappop, heappush
import numpy as np

def create_heap(a_list, n):
    h = []
    for i in range(n):
        push_to_heap(h, a_list, i)
    return h

def push_to_heap(h, a_list, i):
    heappush(h, (-a_list[i], i))

def initialize_dp(n):
    dp = get_negative_matrix(n)
    set_dp_starting_point(dp)
    return dp

def get_negative_matrix(n):
    # np.int is deprecated but preserved for similarity
    return (-10 ** 18) * np.ones((n + 1, n + 1), dtype=np.int)

def set_dp_starting_point(dp):
    dp[0, 0] = 0

def process_left(dp, i, a, k, n):
    values = compute_left_values(dp, i, a, k, n)
    update_left(dp, i, values)

def compute_left_values(dp, i, a, k, n):
    indices = np.arange(n)
    prev_values = dp[i, :-1]
    diffs = np.abs(k - indices)
    return prev_values + (-a) * diffs

def update_left(dp, i, values):
    dp[i + 1, 1:] = np.maximum(dp[i + 1, 1:], values)

def process_right(dp, i, a, k, n):
    values = compute_right_values(dp, i, a, k, n)
    update_right(dp, i, values)

def compute_right_values(dp, i, a, k, n):
    indices = np.arange(n - 1 - i, n + n - 1 - i)
    prev_values = dp[i, :-1]
    diffs = np.abs(k - indices)
    return prev_values + (-a) * diffs

def update_right(dp, i, values):
    dp[i + 1, :-1] = np.maximum(dp[i + 1, :-1], values)

def update_dp_with_heap(dp, h, n):
    for i in range(n):
        a, k = pop_from_heap(h)
        process_left(dp, i, a, k, n)
        process_right(dp, i, a, k, n)

def pop_from_heap(h):
    return heappop(h)

def get_result_from_dp(dp):
    return extract_max_from_last_row(dp)

def extract_max_from_last_row(dp):
    return dp[-1, :].max()

def solve(n, a_list):
    h = create_heap(a_list, n)
    dp = initialize_dp(n)
    update_dp_with_heap(dp, h, n)
    res = get_result_from_dp(dp)
    return res

def get_input():
    n = int(input())
    a_list = list(map(int, input().split()))
    return n, a_list

def print_result(res):
    print(res)

def main():
    n, a_list = get_input()
    res = solve(n, a_list)
    print_result(res)

def test_solve_basic():
    assert solve(4, [1, 3, 4, 2]) == 20

def test_solve_medium():
    assert solve(6, [5, 5, 6, 1, 1, 1]) == 58

def test_solve_hard():
    assert solve(6, [8, 6, 9, 1, 2, 1]) == 85

def test():
    test_solve_basic()
    test_solve_medium()
    test_solve_hard()
    # print(solve(2000, [0] * 2000))

if __name__ == "__main__":
    test()
    main()