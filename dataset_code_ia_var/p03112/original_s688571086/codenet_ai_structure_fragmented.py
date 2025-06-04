import sys
import bisect

def get_input():
    return sys.stdin.readline

def read_initial_values(input_func):
    a, b, q = map(int, input_func().split())
    return a, b, q

def read_list(n, input_func):
    return [int(input_func()) for _ in range(n)]

def get_bisect_positions(lst, x):
    idx_right = bisect.bisect_left(lst, x)
    idx_right = idx_right - 1 if idx_right == len(lst) else idx_right
    idx_left = idx_right - 1 if idx_right > 0 else idx_right
    return idx_left, idx_right

def calc_min_time(s, t, x, s_left, s_right, t_left, t_right):
    res = []
    for i in [s_left, s_right]:
        for j in [t_left, t_right]:
            res.append(single_time_query(s, t, x, i, j))
    return min(res)

def single_time_query(s, t, x, i, j):
    return min(abs(x - s[i]), abs(x - t[j])) + abs(t[j] - s[i])

def process_queries(q, s, t, input_func):
    for _ in range(q):
        x = int(input_func())
        s_left, s_right = get_bisect_positions(s, x)
        t_left, t_right = get_bisect_positions(t, x)
        ans = calc_min_time(s, t, x, s_left, s_right, t_left, t_right)
        print(ans)

def main():
    input_func = get_input()
    a, b, q = read_initial_values(input_func)
    s = read_list(a, input_func)
    t = read_list(b, input_func)
    process_queries(q, s, t, input_func)

main()