def read_n_k():
    return map(int, input().split())

def initialize_sunuke(N):
    return [1]*N

def read_d():
    return int(input())

def read_A():
    return list(map(int, input().split()))

def update_sunuke_with_A(Sunuke, A):
    for ii in range(len(A)):
        set_sunuke_zero(Sunuke, A, ii)

def set_sunuke_zero(Sunuke, A, ii):
    Sunuke[A[ii]-1] = 0

def process_all_K(Sunuke, K):
    for i in range(K):
        process_single_input(Sunuke)

def process_single_input(Sunuke):
    d = read_d()
    A = read_A()
    update_sunuke_with_A(Sunuke, A)

def print_result(Sunuke):
    print(sum(Sunuke))

def main():
    N, K = read_n_k()
    Sunuke = initialize_sunuke(N)
    process_all_K(Sunuke, K)
    print_result(Sunuke)

main()