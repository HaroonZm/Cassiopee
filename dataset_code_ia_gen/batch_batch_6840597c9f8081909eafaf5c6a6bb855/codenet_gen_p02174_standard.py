import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

res = 0
pow2 = 1
for i, x in enumerate(X, 1):
    res += pow2 * pow(x, i, MOD)
    res %= MOD
    pow2 = pow2 * 2 % MOD

print(res % MOD)