def bs(v):
    nc = 0
    m = len(v)
    while m:
        swaps = 0
        for j in range(m - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                nc += 1
                swaps += 1
        if swaps == 0:
            break
        m -= 1
    return nc

import sys
input = sys.stdin.readline

while (n := int(input())):
    v = [int(input()) for _ in range(n)]
    print(bs(v))