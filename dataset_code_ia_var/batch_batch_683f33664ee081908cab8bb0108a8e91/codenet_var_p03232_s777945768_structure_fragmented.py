def get_mod():
    return 10**9+7

def init_arrays(n):
    arr = [1] * (n + 1)
    return arr[:], arr[:], arr[:]

def compute_k(n, mod, k):
    for i in range(1, n + 1):
        k[i] = k[i-1] * i % mod

def compute_gk(n, mod, k, gk):
    gk[n] = pow(k[n], mod - 2, mod)
    for i in range(n, 0, -1):
        gk[i-1] = gk[i] * i % mod

def compute_kb1(n, gk, k, kb1, mod):
    for i in range(1, n + 1):
        kb1[i] = gk[i] * k[i-1] % mod

def compute_kerui(n, kb1, kerui, mod):
    for i in range(1, n + 1):
        kerui[i] = (kerui[i-1] + kb1[i]) % mod

def get_kerui(n, gk, k, mod):
    kb1 = [1] * (n + 1)
    compute_kb1(n, gk, k, kb1, mod)
    kerui = [0] * (n + 1)
    compute_kerui(n, kb1, kerui, mod)
    return kerui

def calc_ans(n, a, kerui, k, mod):
    ans = 0
    for i in range(n):
        temp = (kerui[i+1] + kerui[n-i] - 1) % mod
        ans = (ans + a[i] * temp) % mod
    ans = (ans * k[n]) % mod
    return ans

def remov(n, a):
    mod = get_mod()
    k, gk, kb1 = init_arrays(n)
    compute_k(n, mod, k)
    compute_gk(n, mod, k, gk)
    kerui = get_kerui(n, gk, k, mod)
    return calc_ans(n, a, kerui, k, mod)

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(remov(n, a))

main()