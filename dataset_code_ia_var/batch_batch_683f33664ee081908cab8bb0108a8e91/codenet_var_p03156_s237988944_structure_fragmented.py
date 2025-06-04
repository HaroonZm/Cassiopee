import sys

def custom_input():
    return sys.stdin.readline().strip()

def get_N():
    return int(custom_input())

def get_A_B():
    return list(map(int, custom_input().split()))

def get_P(N):
    return list(map(int, custom_input().split()))

def initialize_sum_list():
    return [0]*3

def check_less_equal(val, ref):
    return val <= ref

def increment_sum_list_leq_A(P_i, A, sum_list):
    if check_less_equal(P_i, A):
        sum_list[0] += 1
    return sum_list

def increment_sum_list_leq_B(P_i, A, B, sum_list):
    if check_less_equal(P_i, B) and not check_less_equal(P_i, A):
        sum_list[1] += 1
    return sum_list

def increment_sum_list_else(P_i, B, sum_list):
    if not check_less_equal(P_i, B):
        sum_list[2] += 1
    return sum_list

def process_P(N, A, B, P, sum_list):
    for i in range(N):
        P_i = P[i]
        sum_list = increment_sum_list_leq_A(P_i, A, sum_list)
        sum_list = increment_sum_list_leq_B(P_i, A, B, sum_list)
        sum_list = increment_sum_list_else(P_i, B, sum_list)
    return sum_list

def get_min_sum(sum_list):
    return min(sum_list)

def main():
    N = get_N()
    A_B = get_A_B()
    A, B = A_B[0], A_B[1]
    P = get_P(N)
    sum_list = initialize_sum_list()
    sum_list = process_P(N, A, B, P, sum_list)
    result = get_min_sum(sum_list)
    print(result)

main()