def get_input():
    return map(int, input().split())

def compute_factorials_and_invs(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs

def modnCr(n, r, mod, fac, inv):
    if n < 0 or r < 0 or n < r:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod

def should_break(one, two, N):
    return one + two > N

def get_dist(one, two):
    return one + two * 2

def get_zero(N, one, two, mod, fac, inv):
    return modnCr(N, one + two, mod, fac, inv)

def get_now_dist_less_X(one, two, zero, mod, fac, inv):
    return modnCr(one + two, one, mod, fac, inv) * zero

def get_dtwo(two, dist, X):
    return two - (dist - X + 1)

def get_now_dist_between_X_and_2X(one, dtwo, zero, mod, fac, inv):
    return modnCr(one + dtwo, one, mod, fac, inv) * zero

def should_continue_dist_equals_X(dist, X):
    return dist == X

def should_continue_dist_between_X_and_2X(dist, X):
    return (dist - X) % 2 == 0

def get_now_all_twos(X, one, zero):
    if X % 2 == 1 and one == 0:
        return zero
    return 0

def update_ans(ans, now, mod):
    return (ans + now) % mod

def main():
    N, X = get_input()
    mod = 998244353
    fac, inv = compute_factorials_and_invs(N + 10, mod)
    ans = 0
    for two in range(N + 1):
        for one in range(N + 1):
            if should_break(one, two, N):
                break
            dist = get_dist(one, two)
            zero = get_zero(N, one, two, mod, fac, inv)
            now = 0
            if dist < X:
                now = get_now_dist_less_X(one, two, zero, mod, fac, inv)
            elif should_continue_dist_equals_X(dist, X):
                continue
            elif dist < 2 * X:
                if should_continue_dist_between_X_and_2X(dist, X):
                    continue
                dtwo = get_dtwo(two, dist, X)
                if dtwo >= 0:
                    now = get_now_dist_between_X_and_2X(one, dtwo, zero, mod, fac, inv)
            elif X % 2 == 1 and one == 0:
                now = get_now_all_twos(X, one, zero)
            ans = update_ans(ans, now, mod)
    print(ans)

main()