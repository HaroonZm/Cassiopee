import sys
import math

def read_input():
    return sys.stdin.readline().rstrip()

def parse_input():
    N, X, M = map(int, read_input().split())
    return N, X, M

def init_list(X):
    return [X]

def init_D(M):
    return [0] * M

def set_D_at_X(D, X):
    D[X] = 1

def process_l(L, M):
    return L[-1] ** 2 % M

def cycle_detected(D, l):
    return D[l] != 0

def process_cycle(L, D, l, k, N):
    n = N - k + 1
    one_cycle = k - D[l]
    mass = sum(L[D[l]-1:])
    ans = n // one_cycle * mass
    res = sum(L[D[l]-1 : D[l] + (n % one_cycle) - 1])
    return ans + res + sum(L)

def is_l_zero(l):
    return l == 0

def advance_L(L, l):
    L.append(l)

def update_D(D, l, k):
    D[l] = k

def print_and_exit(val):
    print(val)
    exit()

def main_loop(N, X, M):
    L = init_list(X)
    D = init_D(M)
    set_D_at_X(D, X)
    k = 2
    while k < N + 1:
        l = process_l(L, M)
        if cycle_detected(D, l):
            result = process_cycle(L, D, l, k, N)
            print_and_exit(result)
        if is_l_zero(l):
            print_and_exit(sum(L))
        advance_L(L, l)
        update_D(D, l, k)
        k += 1
    print(sum(L))

def main():
    N, X, M = parse_input()
    main_loop(N, X, M)

if __name__ == "__main__":
    main()