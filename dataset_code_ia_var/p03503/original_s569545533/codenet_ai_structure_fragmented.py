def read_n():
    return int(input())

def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]

def init_c(n):
    return [0] * n

def count_matching_bits(i, j):
    return (i >> j) & 1

def update_c_for_bit(F, c, j, n):
    for k in range(n):
        if F[k][j] == 1:
            c[k] += 1

def calc_tmp(P, c, n):
    tmp = 0
    for l in range(n):
        tmp += P[l][c[l]]
    return tmp

def try_combination(i, F, P, n):
    c = init_c(n)
    for j in range(10):
        if count_matching_bits(i, j):
            update_c_for_bit(F, c, j, n)
    tmp = calc_tmp(P, c, n)
    return tmp

def solve(F, P, n):
    ans = -10**9
    for i in range(1, 2 ** 10):
        tmp = try_combination(i, F, P, n)
        if tmp > ans:
            ans = tmp
    print(ans)

def main():
    N = read_n()
    F = read_matrix(N)
    P = read_matrix(N)
    solve(F, P, N)

main()