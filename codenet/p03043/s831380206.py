#!/usr/bin/env python3

import math

n, k = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    x = max(0, math.ceil(math.log(k/i, 2)))
    # print(x)
    ans += 1/n*(0.5)**x
print(ans)