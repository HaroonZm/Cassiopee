import bisect

import sys
input_func = raw_input if 'raw_input' in globals() else input

while 1:
    N = int(input_func())
    if N == 0:
        break
    D = {}
    i = 0
    while i < N:
        line = input_func().split()
        name = line[0]
        h = int(line[1])
        t = int(line[2])
        stt = h * 24 * 60 + (t // 100) * 60 + (t % 100)
        D[name] = stt
        i += 1
    P = int(input_func())
    Tlist = [-99999999, 999999999]
    i = 0
    while i < P:
        f = input_func()
        Tlist.append(D.pop(f))
        i += 1
    Tlist.sort()
    i = 0
    broken = False
    while i < P + 1:
        if Tlist[i + 1] < Tlist[i] + 30:
            print -1
            broken = True
            break
        i += 1
    if not broken:
        ans = P
        E = D.values()
        E = sorted(E)
        j = 0
        while j < len(E):
            st = E[j]
            idx = bisect.bisect(Tlist, st)
            if (st - Tlist[idx - 1]) >= 30 and (Tlist[idx] - st) >= 30:
                ans += 1
                bisect.insort(Tlist, st)
            j += 1
        print ans