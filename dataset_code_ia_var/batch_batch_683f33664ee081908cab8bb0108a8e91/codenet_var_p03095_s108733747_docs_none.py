import sys
import math
from collections import Counter

N = int(input())
S = input()

MOD = 1000000007

ans = 1
counter = Counter()
counter[S[0]] += 1

for ch in S[1:]:
    if ch in counter:
        tmp = 1
        for k, cnt in counter.items():
            if k == ch:
                continue
            tmp = (tmp * (1 + cnt)) % MOD
        ans = (ans + tmp) % MOD
        counter[ch] += 1
    else:
        ans = (2 * ans) % MOD
        ans = (ans + 1) % MOD
        counter[ch] += 1

print(ans)