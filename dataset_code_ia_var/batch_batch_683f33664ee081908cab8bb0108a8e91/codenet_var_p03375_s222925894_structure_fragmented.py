import numpy as np

def factorial_mod(n, m):
    f = 1
    for i in range(1, n + 1):
        f = f * i % m
    return f

def precompute_inverses(n, m, fn):
    inv = [1] * (n + 1)
    f = pow(fn, m - 2, m)
    inv[n] = f
    for i in range(n, 0, -1):
        f = f * i % m
        inv[i - 1] = f
    return inv

def prepare(n, m):
    fn = factorial_mod(n, m)
    inv = precompute_inverses(n, m, fn)
    return fn, inv

def gen_initial_stir2(size):
    stir2 = np.zeros(size, dtype=np.int64)
    stir2[0] = 1
    return stir2

def gen_upd(size):
    return np.arange(2, size + 1, dtype=np.int64)

def power_mod(a, x, m):
    ret = 1
    yield ret
    for _ in range(x):
        ret = ret * a % m
        yield ret

def nCi_compute(fn, inv, n, i, m):
    return fn * inv[i] % m * inv[n - i] % m

def sum_i_on(stir2, pow2_iter, i, m):
    i_with = np.fromiter(pow2_iter, dtype=np.int64)
    partial = (stir2[ : i + 1] * i_with % m).sum() % m
    return partial

def update_stir2(stir2, upd, i, m):
    stir2[1 : i + 2] = (stir2[1 : i + 2] * upd[ : i + 1] + stir2[ : i + 1]) % m

def append_ex2(ex2, m):
    ex2.append(ex2[-1] ** 2 % m)

def run_main():
    N, M = get_input()
    fn, inv = prepare(N, M)
    stir2 = gen_initial_stir2(N + 2)
    upd = gen_upd(N + 2)
    ex2 = generate_ex2(N, M)
    ans = compute_loops(N, M, fn, inv, stir2, upd, ex2)
    print(ans)

def get_input():
    return map(int, input().split())

def generate_ex2(N, M):
    ex2 = [2]
    for _ in range(N):
        append_ex2(ex2, M)
    return ex2

def compute_loops(N, M, fn, inv, stir2, upd, ex2):
    ans = 0
    si = 1
    for i in range(N + 1):
        nci = nCi_compute(fn, inv, N, i, M)
        pow2_iter = power_mod(pow(2, N - i, M), i, M)
        i_on = sum_i_on(stir2, pow2_iter, i, M)
        temp = (nci * i_on % M) * (ex2[N - i] % M) % M * si % M
        ans = (ans + temp) % M
        update_stir2(stir2, upd, i, M)
        si = update_si(si)
    return ans

def update_si(si):
    return si * -1

run_main()