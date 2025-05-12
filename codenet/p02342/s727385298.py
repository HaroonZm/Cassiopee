from collections import defaultdict

N, K = map(int, input().split())
MOD = 10**9 + 7

def partition_num(n, k, mod):
    partition = {i: defaultdict(int) for i in range(n + 1)}
    for j in range(1, k+1):
        partition[0][j] = 1
    for i in range(1, n+1):
        partition[i][1] = 1
        for j in range(2, k+1):
            if i - j >= 0:
                partition[i][j] = (partition[i][j - 1] + partition[i - j][j]) % mod
            else:
                partition[i][j] = partition[i][j - 1] % mod
    return partition
if N-K >= 0:
    p = partition_num(N-K, K, MOD)
    ans = p[N-K][K]
else:
    ans = 0
print(ans)