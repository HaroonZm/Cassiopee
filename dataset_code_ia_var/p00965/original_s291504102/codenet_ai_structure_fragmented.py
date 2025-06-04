import sys
from bisect import bisect

def read_input():
    n = int(input())
    P = [read_pair() for _ in range(n)]
    return n, P

def read_pair():
    return list(map(int, input().split()))

def get_A(P):
    return [a for a, b in P]

def get_B(P):
    return [b for a, b in P]

def sort_list(lst):
    lst_sorted = lst[:]
    lst_sorted.sort()
    return lst_sorted

def bisect_left_on_B(B, a):
    return bisect(B, a)

def bisect_right_on_A(A, b):
    return bisect(A, b - 1)

def compute_left(B, a):
    return bisect_left_on_B(B, a)

def compute_right(A, b, n):
    return n - bisect_right_on_A(A, b)

def update_ans(ans, value):
    return max(ans, value)

def policy1(P, n):
    A = get_A(P)
    B = get_B(P)
    A_sorted = sort_list(A)
    B_sorted = sort_list(B)
    ans = 1
    for a, b in P:
        left = compute_left(B_sorted, a)
        right = compute_right(A_sorted, b, n)
        ans = update_ans(ans, n - (left + right))
    return ans

def initialize_D(M):
    return [0]*M

def increment_D(D, a):
    D[a] += 1

def decrement_D(D, b):
    D[b] -= 1

def fill_D(P, D):
    for a, b in P:
        increment_D(D, a)
        decrement_D(D, b)
    return D

def accumulate_D(D, M):
    for i in range(1, M):
        D[i] += D[i-1]
    return D

def find_max_D(D):
    return max(D)

def policy2(P, M):
    D = initialize_D(M)
    D = fill_D(P, D)
    D = accumulate_D(D, M)
    return find_max_D(D)

def main():
    n, P = read_input()
    M = 10**5+1
    ans1 = policy1(P, n)
    ans2 = policy2(P, M)
    print(ans1, ans2)

if __name__ == "__main__":
    main()