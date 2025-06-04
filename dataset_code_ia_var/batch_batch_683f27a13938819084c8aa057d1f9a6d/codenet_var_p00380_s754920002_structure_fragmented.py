import sys

def read_input():
    readline = sys.stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    Q = int(readline())
    swaps = [tuple(map(int, readline().split())) for _ in range(Q)]
    return N, A, Q, swaps

def clone_and_sort(A):
    C = A[:]
    C.sort()
    return C

def compute_powers(N, base, MOD):
    B = [0]*N
    v = 1
    for i in range(N):
        B[i] = v
        v = v * base % MOD
    return B

def initial_P_Q(A, C, B):
    P = 0
    Q = 0
    for i in range(len(A)):
        P += B[i] * A[i]
        Q += B[i] * C[i]
    return P, Q

def check_initial_eq(P, Q):
    return P == Q

def print_zero_and_exit():
    print(0)
    exit(0)

def update_P(P, p, q, r):
    return P + r * p - r * q

def perform_swap(A, x, y):
    A[x], A[y] = A[y], A[x]

def process_swaps(N, A, B, P, Q, swaps):
    for i, (x, y) in enumerate(swaps):
        x -= 1
        y -= 1
        p = A[x]
        q = A[y]
        r = B[y] - B[x]
        P = update_P(P, p, q, r)
        if P == Q:
            print(i+1)
            return
        perform_swap(A, x, y)
    print(-1)

def main():
    MOD = 4253024257
    base = 3
    N, A, _, swaps = read_input()
    C = clone_and_sort(A)
    B = compute_powers(N, base, MOD)
    P, Q = initial_P_Q(A, C, B)
    if check_initial_eq(P, Q):
        print_zero_and_exit()
    process_swaps(N, A, B, P, Q, swaps)

main()