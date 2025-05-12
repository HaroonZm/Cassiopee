#!/usr/bin/env python
from math import *

while True:
    r, n = map(int, raw_input().split())
    if r == 0:
        break

    m = {}
    for i in range(-50, 50):
        m[i] = 0

    for loop in range(n):
        x1, x2, h = map(int, raw_input().split())
        for i in range(x1, x2):
            m[i] = max(m[i], h)

    ans = 100
    for i in range(-r, 0):
        rem = r - sqrt(r * r - (i + 1) * (i + 1)) + m[i]
        ans = min(rem, ans)

    for i in range(0, r):
        rem = r - sqrt(r * r - i * i) + m[i]
        ans = min(rem, ans)

    print ans