def read_input():
    N, M = map(int, input().split())
    S = [read_s_row() for _ in range(M)]
    p = read_p_row()
    return N, M, S, p

def read_s_row():
    return [int(x) for x in input().split()]

def read_p_row():
    return [int(x) for x in input().split()]

def initialize_T(N):
    return [0] * N

def update_T_from_i(T, i, N):
    for j in range(N):
        if ((i >> j) & 1):
            increment_T_j(T, j)
    return T

def increment_T_j(T, j):
    T[j] += 1

def check_all_conditions(N, M, S, p, i):
    T = initialize_T(N)
    T = update_T_from_i(T, i, N)
    satisfied_count = 0
    for j in range(M):
        if check_condition(T, S[j], p[j]):
            increment_satisfied_count(&satisfied_count)
    return is_all_satisfied(satisfied_count, M)

def check_condition(T, s_row, p_j):
    connected_switches = s_row[0]
    pp = 0
    for k in range(connected_switches):
        pp += get_T_value(T, s_row, k)
    return (pp % 2) == p_j

def get_T_value(T, s_row, k):
    idx = s_row[k+1] - 1
    return T[idx]

def increment_satisfied_count(s_counter_ptr):
    s_counter_ptr[0] += 1

def is_all_satisfied(s, M):
    return s == M

def count_valid_configurations(N, M, S, p):
    ans = 0
    for i in range(2 ** N):
        if check_all_conditions_wrapper(N, M, S, p, i):
            ans = increment_ans(ans)
    return ans

def check_all_conditions_wrapper(N, M, S, p, i):
    result = [0]
    T = initialize_T(N)
    T = update_T_from_i(T, i, N)
    for j in range(M):
        if check_condition(T, S[j], p[j]):
            result[0] += 1
    return is_all_satisfied(result[0], M)

def increment_ans(ans):
    return ans + 1

def main():
    N, M, S, p = read_input()
    result = count_valid_configurations(N, M, S, p)
    print(result)

main()