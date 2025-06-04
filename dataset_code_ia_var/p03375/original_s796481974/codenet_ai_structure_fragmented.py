def read_input():
    return map(int, input().split())

def get_mod(m):
    return m

def get_list_size(n):
    return n + 2

def init_factorial_list(size):
    return [1] * size

def compute_factorial_list(f_list, mod):
    for i in range(len(f_list) - 1):
        f_list[i + 1] = int((f_list[i] * (i + 1)) % mod)
    return f_list

def compute_inverse_list(f_list, mod):
    return [pow(x, mod-2, mod) for x in f_list]

def comb_init(f_list, f_r_list, mod):
    def comb(N, r):
        if N < r or r < 0:
            return 0
        else:
            a = f_list[N]
            b = f_r_list[N - r]
            c = f_r_list[r]
            return (((a * b) % mod) * c) % mod
    return comb

def init_st_table(n):
    return [[0 for _ in range(n+1)] for _ in range(n+1)]

def fill_st_table(st, n, mod):
    st[0][0] = 1
    for i in range(1, n+1):
        st[i][0] = 1
        for j in range(1, i+1):
            fill_st_item(st, i, j, mod)
    return st

def fill_st_item(st, i, j, mod):
    val1 = st[i-1][j-1]
    val2 = (j+1) * st[i-1][j]
    st[i][j] = (val1 + val2) % mod

def update_ans(ans, res, i, mod):
    if i % 2 == 0:
        ans += res
    else:
        ans -= res
    ans %= mod
    return ans

def compute_res(comb_fn, n, i, MOD):
    c = comb_fn(n, i)
    exp1 = pow(2, n - i, MOD-1)
    exp2 = pow(2, exp1, MOD)
    res = (c * exp2) % MOD
    return res

def compute_tmp(st, i, n, MOD):
    tmp = 0
    for j in range(i+1):
        val = st[i][j] * pow(2, (n-i) * j, MOD)
        tmp = (tmp + val) % MOD
    return tmp

def update_res(res, tmp, MOD):
    res = (res * tmp) % MOD
    return res

def main():
    n, m = read_input()
    MOD = get_mod(m)
    list_size = get_list_size(n)
    f_list = init_factorial_list(list_size)
    f_list = compute_factorial_list(f_list, MOD)
    f_r_list = compute_inverse_list(f_list, MOD)
    comb_fn = comb_init(f_list, f_r_list, MOD)
    st = init_st_table(n)
    st = fill_st_table(st, n, MOD)
    ans = 0
    for i in range(n+1):
        res = compute_res(comb_fn, n, i, MOD)
        tmp = compute_tmp(st, i, n, MOD)
        res = update_res(res, tmp, MOD)
        ans = update_ans(ans, res, i, MOD)
    print(ans)

main()