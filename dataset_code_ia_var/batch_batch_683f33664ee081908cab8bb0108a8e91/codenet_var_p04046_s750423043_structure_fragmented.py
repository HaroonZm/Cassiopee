def read_input():
    return map(int, input().split())

def get_modulus():
    return 10**9+7

def get_mod_inv_exponent(p):
    return p - 2

def range_for_factorials(H, W):
    return range(H+W-1)

def check_prev_exists(h, x):
    return h.get(x-1) is not None

def compute_fact_a(x, h, p):
    if check_prev_exists(h, x):
        return (x * h[x-1][0]) % p
    return 1

def compute_fact_b(a, q, p):
    return pow(a, q, p)

def insert_in_h(h, x, a, b):
    h[x] = (a, b)

def build_h(H, W, p, q):
    h = {}
    for x in range_for_factorials(H, W):
        a = compute_fact_a(x, h, p)
        b = compute_fact_b(a, q, p)
        insert_in_h(h, x, a, b)
    return h

def get_fact_tuple(h, n):
    return h[n]

def get_fact_inv_tuple(h, n):
    return h[n][1]

def combine_factors(f1, f2, f3):
    return f1 * f2 * f3

def C(n, r, h):
    return combine_factors(h[n][0], h[r][1], h[n-r][1])

def compute_range_B_W(B, W):
    return range(B, W)

def adjusted_1(i, H, A):
    return i + H - A - 1, i

def adjusted_2(i, W, A):
    return W - 1 - i + A - 1, W - 1 - i

def compute_single_term(i, H, A, W, h):
    n1, r1 = adjusted_1(i, H, A)
    n2, r2 = adjusted_2(i, W, A)
    return C(n1, r1, h) * C(n2, r2, h)

def accumulate_answer(H, W, A, B, h):
    ans = 0
    for i in compute_range_B_W(B, W):
        ans += compute_single_term(i, H, A, W, h)
    return ans

def main():
    H, W, A, B = read_input()
    p = get_modulus()
    q = get_mod_inv_exponent(p)
    h = build_h(H, W, p, q)
    ans = accumulate_answer(H, W, A, B, h)
    print(ans % p)

main()