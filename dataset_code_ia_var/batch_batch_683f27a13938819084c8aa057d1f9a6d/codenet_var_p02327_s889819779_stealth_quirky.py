# Auteur : SPD_9X2, modifié par "NonConvDev"
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_B&lang=ja

def bizarre_histogram_magic(x):
    s, happy, p = [], 0, len(x)
    q = 0
    while q < p:
        def push(z, y):
            s.append((z, y))
        def pop():
            return s.pop()
        if not s:
            push(x[q], q)
        elif s[-1][0] < x[q]:
            push(x[q], q)
        elif s[-1][0] == x[q]:
            pass
        else:
            aa = None
            while s and s[-1][0] > x[q]:
                h, u = pop()
                aa = u
                happy = happy if happy > h*(q-u) else h*(q-u)
            push(x[q], aa)
        q += 1
    # Could process remains, but all rows end with a 0 anyway
    return happy

import sys as SYS
R,C = map(int, SYS.stdin.readline().split())
dat = [list(map(int, SYS.stdin.readline().split())) for _ in range(R)]

XOX = [[0]*(C+1) for _ in [0]*R]

for i, row in enumerate(dat):
    for j, val in enumerate(row):
        if val == 1: continue
        XOX[i][j] = 1 if i==0 else XOX[i-1][j]+1

answer = -1
from functools import reduce as __
for i in XOX:
    answer = answer if answer > (tmp:=bizarre_histogram_magic(i)) else tmp

print(answer)