def read_N():
    return int(input())

def read_A():
    return [int(x) for x in input().split()]

def initial_min():
    return 100000000

def initial_max():
    return -100000000

def find_min_index(A, N):
    curr_min = initial_min()
    min_idx = 0
    for i in range(N):
        if A[i] < curr_min:
            curr_min = A[i]
            min_idx = i + 1
    return curr_min, min_idx

def find_max_index(A, N):
    curr_max = initial_max()
    max_idx = 0
    for i in range(N):
        if A[i] > curr_max:
            curr_max = A[i]
            max_idx = i + 1
    return curr_max, max_idx

def all_non_negative(mi):
    return mi >= 0

def all_non_positive(ma):
    return ma <= 0

def print_result(cnt):
    print(cnt)

def print_forward(N):
    for i in range(N-1):
        print(i+1, i+2)

def print_backward(N):
    for i in range(N-1):
        print(N-i, N-i-1)

def abs_greater(ma, mi):
    return abs(ma) > abs(mi)

def print_max_everywhere(ma_n, N):
    for i in range(N):
        print(ma_n, i+1)

def print_min_everywhere(mi_n, N):
    for i in range(N):
        print(mi_n, i+1)

def main():
    N = read_N()
    A = read_A()
    mi, mi_n = find_min_index(A, N)
    ma, ma_n = find_max_index(A, N)
    if all_non_negative(mi):
        print_result(N-1)
        print_forward(N)
    elif all_non_positive(ma):
        print_result(N-1)
        print_backward(N)
    else:
        print_result(2*N-1)
        if abs_greater(ma, mi):
            print_max_everywhere(ma_n, N)
            print_forward(N)
        else:
            print_min_everywhere(mi_n, N)
            print_backward(N)

main()