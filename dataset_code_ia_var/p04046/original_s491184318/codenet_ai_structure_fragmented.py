def get_mod() -> int:
    return 10 ** 9 + 7

def get_n() -> int:
    return 2 * 10 ** 5 + 1

def get_input() -> tuple:
    return tuple(map(int, input().split()))

def init_inv_list_size(n: int) -> list:
    return [0, 1]

def compute_single_inv(i: int, mod: int, inv: list) -> int:
    return mod - ((mod // i) * inv[mod % i]) % mod

def inv_mod_loop(n: int, mod: int, inv: list, i: int = 2) -> list:
    if i > n:
        return inv
    inv.append(compute_single_inv(i, mod, inv))
    return inv_mod_loop(n, mod, inv, i + 1)

def inv_mod(n: int, mod: int) -> list:
    inv = init_inv_list_size(n)
    inv = inv_mod_loop(n, mod, inv)
    return inv

def init_fact_list_size() -> list:
    return [1, 1]

def compute_next_fact_value(res: int, i: int, mod: int) -> int:
    return res * i % mod

def fact_loop(n: int, mod: int, fac: list, res: int, i: int = 2) -> tuple:
    if i > n:
        return fac
    res = compute_next_fact_value(res, i, mod)
    fac.append(res)
    return fact_loop(n, mod, fac, res, i + 1)

def fact(n: int, mod: int) -> list:
    fac = init_fact_list_size()
    res = 1
    fac = fact_loop(n, mod, fac, res)
    return fac

def init_fact_inv_list_size() -> list:
    return [1, 1]

def compute_next_fact_inv_value(facInv: list, inv: list, i: int, mod: int) -> int:
    return facInv[i-1] * inv[i] % mod

def fact_inv_loop(n: int, inv: list, mod: int, facInv: list, i: int = 2) -> list:
    if i > n:
        return facInv
    facInv.append(compute_next_fact_inv_value(facInv, inv, i, mod))
    return fact_inv_loop(n, inv, mod, facInv, i + 1)

def fact_inv(n: int, inv: list, mod: int) -> list:
    facInv = init_fact_inv_list_size()
    facInv = fact_inv_loop(n, inv, mod, facInv)
    return facInv

def nCr_possible(n: int, r: int) -> bool:
    return 0 <= r <= n

def nCr_core(n: int, r: int, mod: int, fac: list, facInv: list) -> int:
    return ((fac[n] * facInv[r]) % mod) * facInv[n - r] % mod

def nCr(n: int, r: int, mod: int, fac: list, facInv: list) -> int:
    if not nCr_possible(n, r):
        return 0
    return nCr_core(n, r, mod, fac, facInv)

def prepare_factorials(n: int, mod: int) -> tuple:
    inv = inv_mod(n, mod)
    fac = fact(n, mod)
    facInv = fact_inv(n, inv, mod)
    return inv, fac, facInv

def single_term(h: int, B: int, H: int, W: int, MOD: int, fac: list, facInv: list) -> int:
    left = nCr(h + (B - 1), h, MOD, fac, facInv)
    right = nCr((H - h - 1) + (W - B - 1), W - B - 1, MOD, fac, facInv)
    return left * right % MOD

def compute_sum(H: int, W: int, A: int, B: int, MOD: int, fac: list, facInv: list) -> int:
    def loop(h: int, ans: int) -> int:
        if h >= H - A:
            return ans
        temp = single_term(h, B, H, W, MOD, fac, facInv)
        ans = (ans + temp) % MOD
        return loop(h + 1, ans)
    return loop(0, 0)

def main():
    MOD = get_mod()
    n = get_n()
    H, W, A, B = get_input()
    inv, fac, facInv = prepare_factorials(n, MOD)
    ans = compute_sum(H, W, A, B, MOD, fac, facInv)
    print(ans)

main()