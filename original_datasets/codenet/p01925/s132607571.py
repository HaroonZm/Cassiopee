#!/usr/bin/env python3
#AOJ C

while 1:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    I = [list(map(int,input().split())) for _ in range(M)]
    P = [0 for _ in range(N)]
    mP = [0 for _ in range(N)]
    for i in range(M):
        k = I[i][1]
        if k == 1:
            mP[I[i][2]-1] += I[i][0]
        for j in range(k):
            P[I[i][2+j]-1] += I[i][0]
    maxp = 0
    minp = float("inf")
    for i in range(N):
        if maxp < P[i]:
            maxp = P[i]
            index = i
    for i in range(N):
        if i != index:
            if minp > mP[i]:
                minp = mP[i]
    f = 0
    for i in range(N):
        if i != index:
            if mP[i] == 0:
                f = 1
    if f:
        print(max(P)+1)
    else:
        print(max(P)+1-minp)