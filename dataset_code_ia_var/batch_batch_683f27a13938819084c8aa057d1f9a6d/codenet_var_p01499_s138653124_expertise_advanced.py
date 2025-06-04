from sys import stdin
from collections import Counter
from itertools import accumulate

MOD = 10**9 + 7

n, t = map(int, stdin.readline().split())
d = [int(stdin.readline()) for _ in range(n)]
counter = Counter(d)

max_d = max(d)
mx = max_d + t + 2

counts = [0] * (mx)
for key, val in counter.items():
    if key < mx:
        counts[key] = val

cum = list(accumulate(reversed(counts)))
cum = cum[::-1] + [0]

ans = 1
for i, x in enumerate(sorted(d, reverse=True)):
    mul = i + 1 - cum[x + t + 1]
    ans = (ans * mul) % MOD

print(ans)