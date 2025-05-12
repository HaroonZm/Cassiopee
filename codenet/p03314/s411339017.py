MOD = 10 ** 9 + 7
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
def include_perm(a):
    for i in range(m - k + 1):
        seen = [False] * (k + 1)
        for j in range(i, i + k):
            if seen[a[j]]:
                break
            seen[a[j]] = True
        else:
            return True
    return False
def unique_len(a):
    seen = [False] * (k+1)
    ans = 0
    for ai in a:
        if seen[ai]:
            break
        seen[ai] = True
        ans += 1
    return ans
if unique_len(a) < m:
    dp_fw = [[0] * k for _ in range(n-m+1)]
    dp_bw = [[0] * k for _ in range(n-m+1)]
    if not include_perm(a):
        dp_fw[0][unique_len(reversed(a))] = 1
        dp_bw[0][unique_len(a)] = 1
    for i in range(n-m):
        for j in range(k):
            dp_fw[i+1][j] = dp_fw[i][j]
            dp_bw[i+1][j] = dp_bw[i][j]
        for j in range(k-2, 0, -1):
            dp_fw[i+1][j] += dp_fw[i+1][j+1]
            dp_fw[i+1][j] %= MOD
            dp_bw[i+1][j] += dp_bw[i+1][j+1]
            dp_bw[i+1][j] %= MOD
        for j in range(k-1):
            dp_fw[i+1][j+1] += dp_fw[i][j] * (k-j)
            dp_fw[i+1][j] %= MOD
            dp_bw[i+1][j+1] += dp_bw[i][j] * (k-j)
            dp_bw[i+1][j] %= MOD
    ans = 0
    tot = pow(k, n-m, MOD)
    for i in range(n-m+1):
        lcnt = i
        rcnt = n - m - i
        t = tot - sum(dp_fw[rcnt]) * sum(dp_bw[lcnt])
        ans = (ans + t) % MOD
    print(ans)
else:
    dp = [[0] * k for _ in range(n+1)]
    dp2 = [[0] * k for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(1, k):
            dp[i+1][j] = dp[i][j]
            dp2[i+1][j] = dp2[i][j]
        for j in range(k-2, 0, -1):
            dp[i+1][j] += dp[i+1][j+1]
            dp[i+1][j] %= MOD
            dp2[i+1][j] += dp2[i+1][j+1]
            dp2[i+1][j] %= MOD
        for j in range(k-1):
            dp[i+1][j+1] += dp[i][j] * (k-j)
            dp[i+1][j+1] %= MOD
            dp2[i+1][j+1] += dp2[i][j] * (k-j)
            dp2[i+1][j+1] %= MOD
        for j in range(m, k):
            dp2[i+1][j] += dp[i+1][j]
            dp2[i+1][j] %= MOD
    f = 1
    for i in range(m):
        f = f * (k - i) % MOD
    t = sum(dp2[n]) * pow(f, MOD-2, MOD) % MOD
    ans = ((n-m+1) * pow(k, n-m, MOD) - t) % MOD
    print(ans)