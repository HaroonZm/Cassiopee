def read_input():
    return input().split()

def parse_ints(strs):
    return list(map(int, strs))

def get_N_T():
    input_vals = read_input()
    return parse_ints(input_vals)

def get_l(N):
    return parse_ints(read_input())

def get_diff(a, b):
    return b - a

def compute_increment(diff, T):
    if diff < T:
        return diff
    return T

def accumulate_ans(l, N, T):
    ans = 0
    for i in range(N - 1):
        diff = get_diff(l[i], l[i + 1])
        inc = compute_increment(diff, T)
        ans = increment_ans(ans, inc)
    return ans

def increment_ans(ans, value):
    return ans + value

def add_T(ans, T):
    return ans + T

def print_result(res):
    print(res)

def main():
    N, T = get_N_T()
    l = get_l(N)
    ans = accumulate_ans(l, N, T)
    res = add_T(ans, T)
    print_result(res)

main()