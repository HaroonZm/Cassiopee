#!/usr/bin/env python3

k, a, b = map(int, input().split())

if a >= b:
    print(k + 1)
else:
    if k <= a:
        print(k + 1)
    elif a + 2 > b:
        print(k + 1)
    else:
        saisyomade = a + 1
        kk = k - saisyomade
        print(b + (kk // 2) * (b - a) + kk % 2)