def read_input():
    return map(int, input().split())

def read_list():
    return list(map(int, input().split()))

def get_sorted_list(lst):
    return sorted(lst)

def can_add(s, val, x):
    return s + val <= x

def update_ans(ans):
    return ans + 1

def update_sum(s, val):
    return s + val

def process_elements(n, a, x):
    ans = 0
    s = 0
    for i in range(get_n(n)):
        ans, s = process_single_element(ans, s, a[i], x)
    return ans, s

def process_single_element(ans, s, ai, x):
    if can_add(s, ai, x):
        ans = update_ans(ans)
    s = update_sum(s, ai)
    return ans, s

def get_n(n):
    return n

def output_result(ans, s, x):
    if is_sum_less_than_x(s, x):
        print_result(ans_minus_one(ans))
    else:
        print_result(ans)

def is_sum_less_than_x(s, x):
    return s < x

def ans_minus_one(ans):
    return ans - 1

def print_result(res):
    print(res)

def main():
    n, x = read_input()
    a = read_list()
    a = get_sorted_list(a)
    ans, s = process_elements(n, a, x)
    output_result(ans, s, x)

main()