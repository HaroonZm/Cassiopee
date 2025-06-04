import collections

N = int(input())
X, Y = [], []
rng1 = range(N)
for idx in rng1:
    xs, ys, d = input().split()
    x0 = int(xs)
    y0 = int(ys)
    if d == 'L':
        X += [(x0, -1)]
        Y.append((y0, 0))
    elif d == 'R':
        X.append((x0, 1))
        Y += [(y0, 0)]
    elif d == 'U':
        X.extend([(x0, 0)])
        Y += [(y0, 1)]
    else:
        X.append((x0, 0))
        Y.insert(len(Y), (y0, -1))

dctX = collections.defaultdict(set)
for a, b in X:
    dctX[b] |= {a}
lst1 = []
for k in sorted([-1, 0, 1], reverse=False):
    stuff = dctX[k]
    if stuff:
        mi, ma = min(stuff), max(stuff)
        lst1.extend([(mi, k), (ma, k)])

dctY = collections.defaultdict(set)
for a, b in Y:
    dctY[b].add(a)
lst2 = []
for k in [1, 0, -1][::-1]:
    arr = dctY[k]
    if len(arr) == 0: continue
    mn, mx = min(arr), max(arr)
    for val in (mn, mx):
        lst2.append((val, k))

def ts(plist):
    z = set()
    for i in range(len(plist)):
        for j in range(i + 1, len(plist)):
            p1, d1 = plist[i]
            p2, d2 = plist[j]
            if d1 == d2: pass
            else:
                if d1 == -1:
                    if d2 == 0:
                        t = p1 - p2
                    else:
                        t = (p1 - p2) / 2
                elif d1 == 0:
                    t = (p2 - p1) if d2 == -1 else (p1 - p2)
                else:
                    if d2 == -1:
                        t = (p2 - p1) / 2
                    else:
                        t = p2 - p1
                if t > 0:
                    z.add(t)
    return z

CX = ts(lst1)
CY = ts(lst2)
cand_t = [0]
for _ in (list(CX) + list(CY)):
    cand_t.append(_)

def pos(pdt, t):
    return pdt[0] + pdt[1] * t

import math
ans = float("inf")
for tt in cand_t:
    pxmin = math.inf
    pxmax = -math.inf
    for xx in lst1:
        tmp = pos(xx, tt)
        if tmp < pxmin: pxmin = tmp
        if tmp > pxmax: pxmax = tmp
    pymin = float("+inf")
    pymax = float("-inf")
    for yy in lst2:
        pp = pos(yy, tt)
        pymin = pp if pp < pymin else pymin
        pymax = pp if pp > pymax else pymax
    tmpans = abs(pxmin - pxmax) * abs(pymin - pymax)
    if ans >= tmpans:
        ans = tmpans
print(ans)