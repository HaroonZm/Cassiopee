import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**5)

def get_input():
    return sys.stdin.readline, sys.stdout.write

def parse_first_line(readline):
    return list(map(int, readline().split()))

def parse_int_list(readline):
    return list(map(int, readline().split()))

def prefix_sum(M, S):
    su = [0] * (M + 1)
    r = 0
    for i in range(M):
        r = r + S[i]
        su[i + 1] = r
    return su

def sorted_K(K):
    K.sort()
    return K

def create_memo(N):
    return [[-1] * N for _ in range(N)]

def get_sa(K, a):
    return K[a]

def get_sb(K, b):
    return K[b]

def swap_if_needed(sa, sb):
    if not sa < sb:
        return sb, sa
    return sa, sb

def range_sum(su, sa, sb):
    return su[sb] - su[sa - 1]

def value_div(L, val):
    return val // L

def calc(a, b, K, su, L):
    sa = get_sa(K, a)
    sb = get_sb(K, b)
    sa, sb = swap_if_needed(sa, sb)
    rs = range_sum(su, sa, sb)
    return value_div(L, rs)

def dfs(i, a, b, N, K, su, L, memo, calc_func):
    if i == N:
        return calc_func(a, b, K, su, L)
    if memo[a][b] != -1:
        return memo[a][b]
    val1 = dfs(i + 1, a, i, N, K, su, L, memo, calc_func) + calc_func(b, i, K, su, L)
    val2 = dfs(i + 1, b, i, N, K, su, L, memo, calc_func) + calc_func(a, i, K, su, L)
    r = min(val1, val2)
    memo[a][b] = r
    return r

def main_solve():
    set_recursion_limit()
    readline, write = get_input()
    first = parse_first_line(readline)
    N, M, L = first
    K = parse_int_list(readline)
    S = parse_int_list(readline)
    su = prefix_sum(M, S)
    K = sorted_K(K)
    memo = create_memo(N)
    def calc_wrapper(a, b, K=K, su=su, L=L):
        return calc(a, b, K, su, L)
    result = dfs(1, 0, 0, N, K, su, L, memo, calc_wrapper)
    write("%d\n" % result)

main_solve()