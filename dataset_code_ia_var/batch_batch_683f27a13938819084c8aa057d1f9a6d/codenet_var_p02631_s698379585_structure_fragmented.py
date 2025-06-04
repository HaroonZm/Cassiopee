import sys

def get_input():
    return sys.stdin.readline

def read_n(input_func):
    return int(input_func())

def read_array(input_func):
    return [int(a) for a in input_func().split()]

def init_ans(n):
    return [-1] * n

def compute_total(a_list):
    total = 0
    for a in a_list:
        total ^= a
    return total

def compute_ans(a_list, total):
    ans_list = []
    for a in a_list:
        ans_list.append(total ^ a)
    return ans_list

def print_ans(ans_list):
    print(*ans_list, sep = " ")

def solve():
    input_func = get_input()
    n = read_n(input_func)
    a_list = read_array(input_func)
    ans_list = process_solution(a_list, n)
    print_ans(ans_list)
    return 0

def process_solution(a_list, n):
    ans = init_ans(n)
    total = compute_total(a_list)
    ans = compute_ans(a_list, total)
    return ans

if __name__ == "__main__":
    solve()