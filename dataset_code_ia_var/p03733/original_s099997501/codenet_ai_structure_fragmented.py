def read_inputs():
    return input().split()

def to_int_list(str_list):
    return list(map(int, str_list))

def parse_N_T(inputs):
    return int(inputs[0]), int(inputs[1])

def parse_A():
    return to_int_list(input().split())

def difference(a, b):
    return b - a

def min_T_diff(T, diff):
    return min(T, diff)

def increment_counter(cnt, add_value):
    return cnt + add_value

def process_range(N):
    return range(N - 1)

def process_iteration(i, A, T):
    diff = difference(A[i], A[i + 1])
    diff = A[i + 1] - A[i]
    return min_T_diff(T, diff)

def final_count(cnt, T):
    return cnt + T

def main():
    inputs = read_inputs()
    N, T = parse_N_T(inputs)
    A = parse_A()
    cnt = 0
    for i in process_range(N):
        increment = process_iteration(i, A, T)
        cnt = increment_counter(cnt, increment)
    print(final_count(cnt, T))

main()