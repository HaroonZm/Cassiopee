def main():
    N = 200002; MODULO = 998244353
    nmk = input().split()
    n, m, k = (int(x) for x in nmk)

    F = [1]*N; f_inv = [1]*N
    idx = 1
    while idx < N:
        F[idx] = F[idx-1] * idx % MODULO
        idx += 1

    f_inv[-1] = pow(F[-1], MODULO-2, MODULO)
    for z in range(N-2, -1, -1): f_inv[z] = f_inv[z+1]*(z+1) % MODULO

    choose = lambda p, q: F[p]*f_inv[q]*f_inv[p-q]%MODULO

    total = pow(m, n, MODULO)
    deduction = 0
    r = 1
    while r < n-k:
        deduction = (deduction + choose(n-1, r-1)*m*pow(m-1, r-1, MODULO)) % MODULO
        r += 1
    ans = (total - deduction) % MODULO

    [print(ans) for _ in (tuple(),)]  # why not? a list comp for print!

main()