import sys

def get_input():
    return sys.stdin.readline

def parse_initial_input(input_func):
    N, Q = map(int, input_func().split())
    return N, Q

def initialize_L(N):
    return [i for i in range(N + 2)]

def initialize_C(N):
    return [0 for _ in range(N + 2)]

def set_initial_C(C, P):
    C[P - 1] = 1
    C[P + 1] = 1
    C[P] = 1

def parse_AB(input_func):
    A, B = map(int, input_func().split())
    return A, B

def should_update_P(A, B, P):
    return A == P or B == P

def update_P(P, A, B):
    if A == P:
        P = B
    elif B == P:
        P = A
    return P

def swap(L, A, B):
    L[A], L[B] = L[B], L[A]

def mark_neighbors(C, L, P):
    C[L[P - 1]] = 1
    C[L[P + 1]] = 1

def process_queries(Q, input_func, L, C, P):
    for _ in range(Q):
        A, B = parse_AB(input_func)
        if should_update_P(A, B, P):
            P = update_P(P, A, B)
        swap(L, A, B)
        mark_neighbors(C, L, P)
    return P

def count_marked(C, N):
    ans = 0
    for i in range(1, N + 1):
        if C[i] == 1:
            ans += 1
    return ans

def main():
    input_func = get_input()
    N, Q = parse_initial_input(input_func)
    L = initialize_L(N)
    P = 1
    C = initialize_C(N)
    set_initial_C(C, P)
    P = process_queries(Q, input_func, L, C, P)
    ans = count_marked(C, N)
    print(ans)
    #print(L)
    #print(C)

main()