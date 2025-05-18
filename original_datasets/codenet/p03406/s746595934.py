import sys
input = sys.stdin.readline

def main():
    def com(com_n, com_r):
        return fac[com_n] * inv[com_r] * inv[com_n - com_r] % md

    md = 10 ** 9 + 7
    n, m = map(int, input().split())
    aa = list(map(lambda x: int(x) - 1, input().split()))
    n2 = 2 ** n

    # combinationの準備
    n_max = n2
    fac = [1]
    inv = [1] * (n_max + 1)
    k_fac_inv = 1
    for i in range(1, n_max + 1):
        k_fac_inv = k_fac_inv * i % md
        fac.append(k_fac_inv)
    k_fac_inv = pow(k_fac_inv, md - 2, md)
    for i in range(n_max, 1, -1):
        inv[i] = k_fac_inv
        k_fac_inv = k_fac_inv * i % md

    dp = [[0] * n2 for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m):
        a = aa[m - 1 - i]
        for b in range(n2):
            pre = dp[i][b]
            if pre == 0: continue
            dp[i + 1][b] = (dp[i + 1][b] + pre) % md
            k = 1
            for _ in range(n):
                if b & k == 0 and n2 - a - b >= k:
                    nb = b | k
                    dp[i + 1][nb] = (dp[i + 1][nb] + pre * com(n2 - 1 - a - b, k - 1)) % md
                k <<= 1
    for b in range(n2):
        k = 1
        p = n2 - 1 - b
        for _ in range(n):
            if b & k == 0:
                dp[m][b] = dp[m][b] * com(p, k) % md
                p -= k
            k <<= 1
    ans = 0
    for b in range(n2):
        coff = -1 if bin(b).count("1") % 2 else 1
        ans = ans + coff * dp[m][b]
    k = 1
    for _ in range(n - 1):
        k <<= 1
        ans = ans * fac[k] % md
    ans = ans * n2 % md
    print(ans)

main()