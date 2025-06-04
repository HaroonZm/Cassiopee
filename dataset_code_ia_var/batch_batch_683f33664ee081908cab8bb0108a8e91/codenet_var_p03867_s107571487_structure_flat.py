import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n, k = list(map(int, input().split()))
M = 10**9+7

# Énumérer les diviseurs de n (structure plate)
s = set()
i = 1
while i * i <= n:
    if n % i == 0:
        s.add(i)
        s.add(n // i)
    i += 1
ds = sorted(list(s))
m = len(ds)
nums = [None] * m
i = 0
while i < m:
    val = pow(k, (ds[i]+1)//2, M)
    j = 0
    while j < i:
        if ds[i] % ds[j] == 0:
            val -= nums[j]
            val %= M
        j += 1
    nums[i] = val % M
    i += 1

ans = 0
inv2 = pow(2, M-2, M)
i = 0
while i < m:
    if ds[i] % 2 == 0:
        ans += ds[i] * nums[i] * inv2
    else:
        ans += ds[i] * nums[i]
    ans %= M
    i += 1
print(ans % M)