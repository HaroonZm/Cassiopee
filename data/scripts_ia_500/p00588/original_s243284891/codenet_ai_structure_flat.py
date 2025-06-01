#!/usr/bin/env python

import sys
sys.setrecursionlimit(10000000)
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    S1 = 'N' + S[:N*2] + 'N'
    S2 = 'N' + S[N*2:] + 'N'
    sx1 = 100000
    gx1 = -1
    sx2 = 100000
    gx2 = -1
    ans = 0
    i = 0
    while i <= N:
        if S1[i*2] == 'Y' or S1[i*2+1] == 'Y':
            ans += 1
            if i < sx1:
                sx1 = i
            if i > gx1:
                gx1 = i
        if S2[i*2] == 'Y' or S2[i*2+1] == 'Y':
            ans += 1
            if i < sx2:
                sx2 = i
            if i > gx2:
                gx2 = i
        i += 1
    if sx1 > sx2:
        ans += 1
    if gx1 < gx2:
        ans += 1
    print(N + ans)