import sys

def read_input():
    return sys.stdin.readline

def get_mod():
    return 10 ** 9 + 7

def get_n_and_m(input_func):
    return map(int, input_func().split())

def get_aa(input_func):
    return list(map(lambda x: int(x) - 1, input_func().split()))

def get_n2(n):
    return 2 ** n

def get_n_max(n2):
    return n2

def init_fac(n_max, md):
    fac = [1]
    k_fac_inv = 1
    for i in range(1, n_max + 1):
        k_fac_inv = k_fac_inv * i % md
        fac.append(k_fac_inv)
    return fac, k_fac_inv

def init_inv(n_max, md):
    return [1] * (n_max + 1)

def powmod(a, b, md):
    return pow(a, b, md)

def fill_inv(inv, k_fac_inv, n_max, md):
    for i in range(n_max, 1, -1):
        inv[i] = k_fac_inv
        k_fac_inv = k_fac_inv * i % md
    return inv

def com(com_n, com_r, fac, inv, md):
    return fac[com_n] * inv[com_r] * inv[com_n - com_r] % md

def make_dp_table(m, n2):
    return [[0] * n2 for _ in range(m + 1)]

def set_dp_base_case(dp):
    dp[0][0] = 1

def update_dp_i(dp, i, a, n, n2, md, fac, inv, com_func):
    for b in range(n2):
        pre = dp[i][b]
        if pre == 0:
            continue
        dp[i + 1][b] = (dp[i + 1][b] + pre) % md
        k = 1
        for _ in range(n):
            if b & k == 0 and n2 - a - b >= k:
                nb = b | k
                to_add = pre * com_func(n2 - 1 - a - b, k - 1, fac, inv, md)
                dp[i + 1][nb] = (dp[i + 1][nb] + to_add) % md
            k <<= 1

def fill_dp_main_loop(dp, aa, m, n, n2, md, fac, inv, com_func):
    for i in range(m):
        a = aa[m - 1 - i]
        update_dp_i(dp, i, a, n, n2, md, fac, inv, com_func)

def update_dp_m_b(dp, m, b, n, n2, md, fac, inv, com_func):
    k = 1
    p = n2 - 1 - b
    for _ in range(n):
        if b & k == 0:
            dp[m][b] = dp[m][b] * com_func(p, k, fac, inv, md) % md
            p -= k
        k <<= 1

def fill_dp_after(dp, m, n, n2, md, fac, inv, com_func):
    for b in range(n2):
        update_dp_m_b(dp, m, b, n, n2, md, fac, inv, com_func)

def calc_coff(b):
    return -1 if bin(b).count("1") % 2 else 1

def accumulate_ans(dp, m, n2):
    ans = 0
    for b in range(n2):
        coff = calc_coff(b)
        ans += coff * dp[m][b]
    return ans

def mult_fact(ans, fac, n):
    k = 1
    for _ in range(n - 1):
        k <<= 1
        ans = ans * fac[k] % get_mod()
    return ans

def mult_n2(ans, n2):
    return ans * n2 % get_mod()

def main():
    input_func = read_input()
    md = get_mod()
    n, m = get_n_and_m(input_func)
    aa = get_aa(input_func)
    n2 = get_n2(n)
    n_max = get_n_max(n2)
    fac, k_fac_inv_val = init_fac(n_max, md)
    inv = init_inv(n_max, md)
    k_fac_inv = powmod(fac[-1], md - 2, md)
    inv = fill_inv(inv, k_fac_inv, n_max, md)
    dp = make_dp_table(m, n2)
    set_dp_base_case(dp)
    fill_dp_main_loop(dp, aa, m, n, n2, md, fac, inv, com)
    fill_dp_after(dp, m, n, n2, md, fac, inv, com)
    ans = accumulate_ans(dp, m, n2)
    ans = mult_fact(ans, fac, n)
    ans = mult_n2(ans, n2)
    print(ans)

main()