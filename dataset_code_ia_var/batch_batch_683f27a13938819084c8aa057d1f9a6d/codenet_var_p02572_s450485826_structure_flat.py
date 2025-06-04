import itertools

n = int(input())
a = list(map(int, input().split()))
MOD = 10**9 + 7

lis = []
s = 0
for x in a:
    s += x
    lis.append(s)

total = 0
i = 0
while i < n - 1:
    x = a[i]
    y = lis[n - 1] - lis[i]
    total += (x * y) % MOD
    i += 1

print(total % MOD)