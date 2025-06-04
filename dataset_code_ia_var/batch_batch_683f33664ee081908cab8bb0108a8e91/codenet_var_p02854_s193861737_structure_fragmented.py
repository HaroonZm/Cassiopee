def read_int():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def compute_sum(lst):
    return sum(lst)

def compute_half(value):
    return value / 2

def in_bounds(i, n):
    return i < n

def update_cumsum(ans1, ai):
    return ans1 + ai

def increment_i(i):
    return i + 1

def loop_condition(ans1, half_x, i, n):
    return ans1 < half_x and in_bounds(i, n)

def decrement_i(i):
    return i - 1

def subtract(a, b):
    return a - b

def compute_ans2(x, ans1):
    return subtract(x, ans1)

def subtract_from_ans1(ans1, ai):
    return ans1 - ai

def abs_val(x):
    return abs(x)

def compute_diff(ans1, ans2):
    return abs_val(subtract(ans1, ans2))

def print_result(res):
    print(res)

def main():
    n = read_int()
    a = read_list()
    x = compute_sum(a)
    half_x = compute_half(x)
    i = 0
    ans1 = 0
    while loop_condition(ans1, half_x, i, n):
        ans1 = update_cumsum(ans1, a[i])
        i = increment_i(i)
    i = decrement_i(i)
    ans2 = compute_ans2(x, ans1)
    ans1 = subtract_from_ans1(ans1, a[i])
    diff = compute_diff(ans1, ans2)
    res = subtract(a[i], diff)
    print_result(res)

main()