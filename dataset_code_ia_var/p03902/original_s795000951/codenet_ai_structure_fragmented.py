import sys
from math import log2
from itertools import accumulate

def read_input():
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(N)]
    return N, M, A

def get_max_element(A):
    return max(max(row) for row in A)

def handle_M1(N, A):
    if N == 1 or all(A[i][0] < A[i+1][0] for i in range(N-1)):
        print("0")
    else:
        print("-1")

def compute_logB(B):
    return log2(B)

def compute_logBi(logB):
    return int(logB)

def get_INF():
    return 10**18

def build_INFL(INF, length):
    return [INF]*length

def min_custom(a, b):
    return a if a < b else b

def update_by_accumulate(P, t):
    for _ in range(t):
        P[:] = accumulate(P)

def build_V(t, L):
    V = [1]*L
    for k in range(1, L):
        V[k] = V[k-1] * (t + k - 1)//k
    return V

def add_weighted_sums(P, V, L):
    for i in range(L-1, 0, -1):
        P[i] += sum(P[j] * V[i-j] for j in range(i))

def fill_infl(P, logBi, M, INFL):
    if logBi+2 < M:
        P[logBi+2:] = INFL

def gen(P, t, logB, logBi, M, INFL):
    L = min_custom(logBi+2, M)
    if t <= logB:
        update_by_accumulate(P, t)
    else:
        V = build_V(t, L)
        add_weighted_sums(P, V, L)
        fill_infl(P, logBi, M, INFL)

def parse_row_pair(A, i):
    a0, a1 = A[i][:2]
    b0, b1 = A[i+1][:2]
    return a0, a1, b0, b1

def advance_if_less(a0, b0):
    return a0 < b0

def fail_if_greater(a0, b0):
    return a0 > b0

def calc_v(t0, a0, a1, b1):
    return max(t0*a0 + a1 - b1, 0)

def divisible(v, b0):
    return v % b0 == 0

def get_t1_from_v(v, b0):
    return v // b0

def get_t1_ceiling(v, b0):
    return (v + b0 - 1) // b0

def check_P_leq_A(P, A_i):
    return list(P) <= list(A_i)

def check_A_leq_P(A_next, P):
    return list(A_next) <= list(P)

def update_T_T_and_ans(T, i1, t1, ans):
    T[i1] = t1
    ans += t1
    return ans

def main():
    N, M, A = read_input()
    B = get_max_element(A)
    if M == 1:
        handle_M1(N, A)
        return
    logB = compute_logB(B)
    logBi = compute_logBi(logB)
    INF = get_INF()
    INFL = build_INFL(INF, M - logBi-2)
    T = [0]*N
    ans = 0
    P = [0]*M

    for i in range(N-1):
        a0, a1, b0, b1 = parse_row_pair(A, i)
        if advance_if_less(a0, b0):
            continue
        if fail_if_greater(a0, b0):
            ans = -1
            break
        t0 = T[i]
        v = calc_v(t0, a0, a1, b1)
        if not divisible(v, b0):
            t1 = get_t1_ceiling(v, b0)
            ans = update_T_T_and_ans(T, i+1, t1, ans)
            continue
        t1 = get_t1_from_v(v, b0)
        if t0 <= t1:
            P[:] = A[i+1]
            gen(P, t1 - t0, logB, logBi, M, INFL)
            if check_P_leq_A(P, A[i]):
                t1 += 1
        else:
            P[:] = A[i]
            gen(P, t0 - t1, logB, logBi, M, INFL)
            if check_A_leq_P(A[i+1], P):
                t1 += 1
        ans = update_T_T_and_ans(T, i+1, t1, ans)
    print(ans)

main()