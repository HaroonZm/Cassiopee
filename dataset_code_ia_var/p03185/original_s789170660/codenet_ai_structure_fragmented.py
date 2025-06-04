def read_input():
    return map(int, open(0).read().split())

def split_input(values):
    n, C, *H = values
    return n, C, H

def initialize_dp():
    return [0]

def initialize_P():
    return [0]

def f(dp, H, I, h):
    return dp[I] + H[I] * (H[I] - 2 * h)

def c(H, dp, x, y, z):
    lhs = (H[y] - H[x]) * (f(dp, H, y, 0) - f(dp, H, z, 0))
    rhs = (H[z] - H[y]) * (f(dp, H, x, 0) - f(dp, H, y, 0))
    return lhs > rhs

def get_candidate_indices(P):
    return P[0], P[1]

def pop_front(P):
    P.pop(0)

def pop_back(P):
    P.pop()

def append_dp(dp, value):
    dp.append(value)

def append_P(P, value):
    P.append(value)

def compute_new_dp_val(dp, P, H, C, i):
    idx = P[0]
    return f(dp, H, idx, H[i]) + H[i] ** 2 + C

def check_pop_front(P, dp, H, i):
    if len(P) > 1 and f(dp, H, P[0], H[i]) > f(dp, H, P[1], H[i]):
        return True
    return False

def check_pop_back(P, dp, H, i):
    if len(P) > 1 and c(H, dp, P[-2], P[-1], i):
        return True
    return False

def process(n, C, H):
    dp = initialize_dp()
    P = initialize_P()
    for i in range(1, n):
        while check_pop_front(P, dp, H, i):
            pop_front(P)
        val = compute_new_dp_val(dp, P, H, C, i)
        append_dp(dp, val)
        while check_pop_back(P, dp, H, i):
            pop_back(P)
        append_P(P, i)
    return dp

def main():
    values = read_input()
    n, C, H = split_input(values)
    dp = process(n, C, H)
    print(dp[-1])

main()