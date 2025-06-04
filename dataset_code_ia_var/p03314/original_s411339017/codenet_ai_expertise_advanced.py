from functools import lru_cache
from itertools import islice

MOD = 10**9 + 7
n, k, m = map(int, input().split())
a = list(map(int, input().split()))

@lru_cache(None)
def has_permutation(a_tuple):
    # Check if any window contains a permutation of 1..k (using set for O(1) lookup)
    a_list = list(a_tuple)
    needed = set(range(1, k+1))
    for window in (set(islice(a_list, i, i + k)) for i in range(m - k + 1)):
        if len(window) == k and window == needed:
            return True
    return False

def prefix_unique_length(a_seq):
    # Returns length of prefix with all distinct values from 1..k
    seen = [False] * (k+1)
    for idx, ai in enumerate(a_seq):
        if seen[ai]:
            return idx
        seen[ai] = True
    return len(a_seq)

# Fast sum of dp vectors
def vec_sum(v): return sum(v) % MOD

uniq_pref = prefix_unique_length(a)
if uniq_pref < m:
    # Use memoryview for very fast access if available, or numpy if this is a real bottleneck
    dp_fw = [[0]*k for _ in range(n-m+1)]
    dp_bw = [[0]*k for _ in range(n-m+1)]
    if not has_permutation(tuple(a)):
        dp_fw[0][prefix_unique_length(reversed(a))] = 1
        dp_bw[0][uniq_pref] = 1
    for i in range(n-m):
        for j in range(k):
            dp_fw[i+1][j] = dp_fw[i][j]
            dp_bw[i+1][j] = dp_bw[i][j]
        for j in range(k-2, 0, -1):
            dp_fw[i+1][j] = (dp_fw[i+1][j] + dp_fw[i+1][j+1]) % MOD
            dp_bw[i+1][j] = (dp_bw[i+1][j] + dp_bw[i+1][j+1]) % MOD
        for j in range(k-1):
            dp_fw[i+1][j+1] = (dp_fw[i+1][j+1] + dp_fw[i][j] * (k-j)) % MOD
            dp_bw[i+1][j+1] = (dp_bw[i+1][j+1] + dp_bw[i][j] * (k-j)) % MOD

    tot = pow(k, n-m, MOD)
    ans = 0
    cached_sum_fw = [vec_sum(row) for row in dp_fw]
    cached_sum_bw = [vec_sum(row) for row in dp_bw]
    for i in range(n-m+1):
        lcnt = i
        rcnt = n-m-i
        t = (tot - cached_sum_fw[rcnt] * cached_sum_bw[lcnt] % MOD + MOD) % MOD
        ans = (ans + t) % MOD
    print(ans)
else:
    dp = [[0]*k for _ in range(n+1)]
    dp2 = [[0]*k for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(1, k):
            dp[i+1][j] = dp[i][j]
            dp2[i+1][j] = dp2[i][j]
        for j in range(k-2, 0, -1):
            dp[i+1][j] = (dp[i+1][j] + dp[i+1][j+1]) % MOD
            dp2[i+1][j] = (dp2[i+1][j] + dp2[i+1][j+1]) % MOD
        for j in range(k-1):
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j] * (k-j)) % MOD
            dp2[i+1][j+1] = (dp2[i+1][j+1] + dp2[i][j] * (k-j)) % MOD
        for j in range(m, k):
            dp2[i+1][j] = (dp2[i+1][j] + dp[i+1][j]) % MOD
    f = 1
    for v in range(m):
        f = f * (k-v) % MOD
    t = vec_sum(dp2[n]) * pow(f, MOD-2, MOD) % MOD
    ans = ((n-m+1) * pow(k, n-m, MOD) - t) % MOD
    print(ans)