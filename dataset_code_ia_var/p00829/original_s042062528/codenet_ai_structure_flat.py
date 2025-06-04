import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

N = input()
N = int(N)
i = 0
while i < N:
    lst = []
    while len(lst) < 9:
        lst_ = raw_input().split()
        idx = 0
        while idx < len(lst_):
            S = lst_[idx]
            lst.append(int(S, 16))
            idx += 1
    res = lst[8]
    lst = lst[:8]
    diff = (sum(lst) - res) % (1 << 32)
    diff_lst = []
    i2 = 0
    while i2 < 32:
        D = 0
        j2 = 0
        while j2 < 9:
            if j2 < 8:
                val = lst[j2]
            else:
                val = ((1 << 32) - 1) ^ res
            if val & (1 << i2) == 0:
                D += (1 << i2)
            else:
                D -= (1 << i2)
            j2 += 1
        D %= (1 << 32)
        diff_lst.append((D, 1 << i2))
        i2 += 1
    L1 = [(diff, 0)]
    i3 = 0
    while i3 < 16:
        P = diff_lst[i3]
        L = []
        pidx = 0
        while pidx < len(L1):
            p = L1[pidx]
            L.append(((p[0] + P[0]) % (1 << 32), p[1] + P[1]))
            pidx += 1
        L1 += L
        i3 += 1
    L2 = [[0, 0]]
    i4 = 16
    while i4 < 32:
        P = diff_lst[i4]
        L = []
        pidx = 0
        while pidx < len(L2):
            p = L2[pidx]
            L.append(((p[0] + P[0]) % (1 << 32), p[1] + P[1]))
            pidx += 1
        L2 += L
        i4 += 1
    L1.sort()
    L2.sort()
    if L1[0][0] == 0:
        print hex(L1[0][1])[2:]
        i += 1
        continue
    pos = len(L2) - 1
    found = False
    pidx = 0
    while pidx < len(L1):
        p = L1[pidx]
        while p[0] + L2[pos][0] > (1 << 32):
            pos -= 1
            if pos < 0:
                break
        if pos >= 0 and p[0] + L2[pos][0] == (1 << 32):
            print hex(p[1] + L2[pos][1])[2:]
            found = True
            break
        pidx += 1
    i += 1