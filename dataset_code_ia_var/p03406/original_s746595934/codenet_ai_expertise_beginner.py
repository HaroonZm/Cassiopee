import sys

def main():
    input = sys.stdin.readline
    md = 10 ** 9 + 7
    n, m = map(int, input().split())
    aa = list(map(lambda x: int(x) - 1, input().split()))
    n2 = 2 ** n

    # On prépare les factorielles et leurs inverses
    n_max = n2
    fac = [1] * (n_max + 1)
    inv = [1] * (n_max + 1)
    for i in range(1, n_max + 1):
        fac[i] = fac[i - 1] * i % md
    inv[n_max] = pow(fac[n_max], md - 2, md)
    for i in range(n_max, 0, -1):
        inv[i - 1] = inv[i] * i % md

    def com(n1, n2):
        if n2 < 0 or n2 > n1:
            return 0
        return fac[n1] * inv[n2] % md * inv[n1 - n2] % md

    dp = []
    for i in range(m + 1):
        dp.append([0] * n2)
    dp[0][0] = 1

    for i in range(m):
        a = aa[m - 1 - i]
        for b in range(n2):
            pre = dp[i][b]
            if pre == 0:
                continue
            dp[i + 1][b] = (dp[i + 1][b] + pre) % md
            k = 1
            for j in range(n):
                if (b & k) == 0 and n2 - a - b >= k:
                    nb = b | k
                    dp[i + 1][nb] = (dp[i + 1][nb] + pre * com(n2 - 1 - a - b, k - 1)) % md
                k = k << 1

    for b in range(n2):
        k = 1
        p = n2 - 1 - b
        for j in range(n):
            if (b & k) == 0:
                dp[m][b] = dp[m][b] * com(p, k) % md
                p -= k
            k = k << 1

    ans = 0
    for b in range(n2):
        if bin(b).count("1") % 2 == 1:
            coff = -1
        else:
            coff = 1
        ans = ans + coff * dp[m][b]

    k = 1
    for i in range(n - 1):
        k = k << 1
        ans = ans * fac[k] % md

    ans = ans * n2 % md
    print(ans)

main()