import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

N = input()
i0 = 0
while i0 < N:
    lst = []
    while len(lst) < 9:
        lst_ = raw_input().split()
        for S in lst_:
            lst.append(int(S, 16))
    res = lst[8]
    lst = lst[:8]
    diff = (sum(lst) - res) % (1 << 32)
    diff_lst = []
    i1 = 0
    while i1 < 32:
        D = 0
        for j in lst:
            if j & (1 << i1) == 0:
                D += (1 << i1)
            else:
                D -= (1 << i1)
        if res & (1 << i1) == 0:
            D -= (1 << i1)
        else:
            D += (1 << i1)
        D %= (1 << 32)
        diff_lst.append((D, 1 << i1))
        i1 += 1
    L1 = [(diff, 0)]
    i2 = 0
    while i2 < 16:
        P = diff_lst[i2]
        L = []
        j2 = 0
        while j2 < len(L1):
            p = L1[j2]
            L.append(((p[0] + P[0]) % (1 << 32), p[1] + P[1]))
            j2 += 1
        L1 += L
        i2 += 1
    L2 = [[0, 0]]
    i3 = 16
    while i3 < 32:
        P = diff_lst[i3]
        L = []
        j3 = 0
        while j3 < len(L2):
            p = L2[j3]
            L.append(((p[0] + P[0]) % (1 << 32), p[1] + P[1]))
            j3 += 1
        L2 += L
        i3 += 1
    L1.sort()
    L2.sort()
    if L1[0][0] == 0:
        print hex(L1[0][1])[2:]
        i0 += 1
        continue
    pos = len(L2) - 1
    for p in L1:
        while pos >= 0 and p[0] + L2[pos][0] > (1 << 32):
            pos -= 1
        if pos >= 0 and p[0] + L2[pos][0] == (1 << 32):
            print hex(p[1] + L2[pos][1])[2:]
            break
    i0 += 1