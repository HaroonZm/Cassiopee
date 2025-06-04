def input_n_and_k():
    return map(int, input().split())

def initialize_A(n):
    return [-1] * n

def input_d():
    return int(input())

def input_a():
    return list(map(int, input().split()))

def update_A_for_a(A, a):
    d = len(a)
    for j in range(d):
        x = to_zero_indexed(a[j])
        set_A_if_unset(A, x)

def to_zero_indexed(val):
    return val - 1

def set_A_if_unset(A, idx):
    if A[idx] == -1:
        A[idx] = 1

def count_minus_ones(A):
    cnt = 0
    for i in range(len(A)):
        if is_minus_one(A[i]):
            cnt += 1
    return cnt

def is_minus_one(val):
    return val == -1

def solve():
    n, k = input_n_and_k()
    A = initialize_A(n)
    for i in range(k):
        d = input_d()
        a = input_a()
        update_A_for_a(A, a)
    ans = count_minus_ones(A)
    print(ans)

solve()