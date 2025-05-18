#!/usr/bin/env python3
while True:
    d, e = map(int, input().split())
    if d == 0:
        break
    ans = 10**5
    for x in range(d + 1):
        y = d - x
        ans = min(ans, abs((x**2 + y**2)**0.5 - e))
    print(ans)