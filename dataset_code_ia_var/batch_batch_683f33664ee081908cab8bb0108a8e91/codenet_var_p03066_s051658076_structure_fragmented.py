import sys

def read_input():
    return sys.stdin.readline().rstrip()

def get_first_line():
    return map(int, read_input().split())

def init_permutation_count_array(N):
    return [[0] * (2 * i + 1) for i in range(N + 1)]

def set_base_case(A):
    A[0][0] = 1

def update_permutation_counts(A, N, P):
    def add_and_reduce(a, b):
        a += b
        if a >= P:
            a -= P
        return a
    for i in range(N):
        process_row_update(A, i, P, add_and_reduce)

def process_row_update(A, i, P, add_and_reduce):
    for j in range(i, 2 * i + 1):
        A[i + 1][j + 1] = add_and_reduce(A[i + 1][j + 1], A[i][j])
        A[i + 1][j + 2] = add_and_reduce(A[i + 1][j + 2], A[i][j])

def init_B(N):
    return [0] * (N + 1)

def type1_update(B, A, N, X):
    for i in range(N + 1):
        type1_inner_update(B, A, i, X)

def type1_inner_update(B, A, i, X):
    for j in range(i, min(2 * i + 1, X)):
        B[i] += A[i][j]

def type2_update(B, N, X):
    if X % 2 == 1:
        for i in range(X, N + 1):
            B[i] += 1

def type3_update(B, A, N, X, P):
    for i in range(1, X):
        a = X - 1 - 2 * i
        if a < 0:
            continue
        process_type3_inner(B, A, a, i, N, P)

def process_type3_inner(B, A, a, i, N, P):
    for j in range((a + 1) // 2, a + 1):
        k = j + 2 * i
        if k > N:
            break
        B[k] += A[j][a]
        if B[k] >= P:
            B[k] -= P

def compute_answer(B, A, N, P):
    ans = 0
    for i, b in enumerate(B):
        ans = accumulate_answer(ans, b, A, N, i, P)
    return ans

def accumulate_answer(ans, b, A, N, i, P):
    return (ans + b * A[-1][-1 - i]) % P

def main():
    N, X = get_first_line()
    P = 998244353
    A = init_permutation_count_array(N)
    set_base_case(A)
    update_permutation_counts(A, N, P)
    B = init_B(N)
    type1_update(B, A, N, X)
    type2_update(B, N, X)
    type3_update(B, A, N, X, P)
    ans = compute_answer(B, A, N, P)
    print(ans)

main()