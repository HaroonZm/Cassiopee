import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, K = na()
mod = 1000000007

a = [0]
for d in range(1, K+1):
    a.append(pow(K//d, n, mod))
for i in range(K, 0, -1):
    j = 2*i
    while j <= K:
        a[i] -= a[j]
        j += i
    if a[i] < 0:
        a[i] %= mod
        if a[i] < 0: a[i] += mod

ans = 0
for i in range(1, K+1):
    ans += i*a[i]
print(ans%mod)